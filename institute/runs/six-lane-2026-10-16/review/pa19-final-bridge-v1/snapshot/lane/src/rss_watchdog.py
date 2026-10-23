#!/usr/bin/env python3
"""Aggregate lane RSS watchdog + busy-process sampler (parent conditions for the staged pipeline,
2026-10-17 ~15:4x). Every INTERVAL (<= 2 s) one `ps` snapshot is taken and the lane's processes are
selected: (a) solver/checker/helper processes whose command line contains the lane path (kissat,
cadical, drat-trim, extend_p1q.py/extend_b.py, all started with absolute lane paths) and (b) Python
processes running one of this lane's runner scripts (names in RUNNERS). Their RSS is summed.
  * If the sum exceeds LIMIT_KB (8 GiB): the NEWEST pipeline (largest FIFO-directory timestamp among
    the lane's kissat/cadical/drat-trim processes) is stopped with SIGTERM (its solver and checker),
    bounded wait 60 s (no SIGKILL; survivors are recorded); the case becomes UNKNOWN in its record.
    cycle2/tokens/COUNT is then lowered by one (minimum 1) and cycle2/RSS-WATCHDOG-<time>.json is
    written. Monitoring continues.
  * Every WINDOW seconds one line is appended to cycle2/watchdog-samples.log: time, samples, lane RSS
    max (KB), busy (state R) solver/checker processes min/mean/max, solver/checker process count
    max, token COUNT.
Usage: rss_watchdog.py [INTERVAL_S [WINDOW_S]]
"""
import json
import os
import re
import signal
import subprocess
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT_KB = 8 * 1024 * 1024
RUNNERS = ("run_hard10.py", "run_m2_10.py", "run_hard8.py", "run_hard9.py", "run_m2skel9.py", "run_m2partbatch5.py",
           "smoke_stream10.py", "summarize8.py", "bind_check.py", "retention_index.py", "rss_watchdog.py", "disk_guard.py")
SOLVERS = ("kissat", "cadical", "drat-trim")
FIFO_TS = re.compile(r"scratch/fifo/[^ ]*?_(\d+)_(\d{15,})/")


def snapshot():
    out = subprocess.run(["ps", "-Ao", "pid=,ppid=,stat=,rss=,command="], capture_output=True, text=True).stdout
    procs = []
    for line in out.splitlines():
        parts = line.split(None, 4)
        if len(parts) < 5:
            continue
        pid, ppid, stat, rss, cmd = int(parts[0]), int(parts[1]), parts[2], int(parts[3]), parts[4]
        exe = os.path.basename(cmd.split()[0])
        lane_cmd = LANE in cmd
        runner = any(("src/" + r) in cmd or (os.sep + r) in cmd for r in RUNNERS) and "python" in exe.lower()
        if not (lane_cmd or runner):
            continue
        kind = "solver" if exe in SOLVERS else ("runner" if runner else "helper")
        m = FIFO_TS.search(cmd)
        procs.append({"pid": pid, "ppid": ppid, "stat": stat, "rss": rss, "exe": exe, "kind": kind,
                      "fifo_ts": int(m.group(2)) if m else None, "cmd": cmd[:240]})
    return procs


def token_count():
    try:
        return int(open(os.path.join(LANE, "cycle2", "tokens", "COUNT")).read().split()[0])
    except (OSError, ValueError, IndexError):
        return None


def trip(procs, total):
    t = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    rec = {"time": t, "lane_rss_kb": total, "limit_kb": LIMIT_KB, "processes": procs, "actions": []}
    sol = [p for p in procs if p["kind"] == "solver" and p["fifo_ts"]]
    if sol:
        newest = max(p["fifo_ts"] for p in sol)
        targets = [p for p in sol if p["fifo_ts"] == newest]
        for p in targets:
            try:
                os.kill(p["pid"], signal.SIGTERM)
                rec["actions"].append({"SIGTERM": p["pid"], "exe": p["exe"], "cmd": p["cmd"]})
            except OSError as e:
                rec["actions"].append({"SIGTERM_failed": p["pid"], "err": str(e)})
        deadline = time.time() + 60
        alive = [p["pid"] for p in targets]
        while alive and time.time() < deadline:
            time.sleep(1)
            alive = [pid for pid in alive if subprocess.run(["ps", "-p", str(pid), "-o", "stat="], capture_output=True,
                                                             text=True).stdout.strip() not in ("", "Z")]
        rec["still_running_after_60s"] = alive
    c = token_count()
    if c and c > 1:
        open(os.path.join(LANE, "cycle2", "tokens", "COUNT"), "w").write("%d\n" % (c - 1))
        rec["actions"].append({"token_count": [c, c - 1]})
    json.dump(rec, open(os.path.join(LANE, "cycle2", "RSS-WATCHDOG-%s.json" % time.strftime("%Y%m%dT%H%M%S")), "w"), indent=1)


def main():
    interval = min(2.0, float(sys.argv[1])) if len(sys.argv) > 1 else 2.0
    window = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
    logp = os.path.join(LANE, "cycle2", "watchdog-samples.log")
    if not os.path.exists(logp):
        with open(logp, "w") as f:
            f.write("# time samples lane_rss_max_kb busy_min busy_mean busy_max solver_procs_max token_count\n")
    w0, n, rmax, bmin, bsum, bmax, smax = time.time(), 0, 0, 99, 0, 0, 0
    while True:
        procs = snapshot()
        total = sum(p["rss"] for p in procs)
        sol = [p for p in procs if p["kind"] == "solver"]
        busy = sum(1 for p in sol if p["stat"].startswith("R"))
        n += 1
        rmax, bmin, bmax, smax = max(rmax, total), min(bmin, busy), max(bmax, busy), max(smax, len(sol))
        bsum += busy
        if total > LIMIT_KB:
            trip(procs, total)
        if time.time() - w0 >= window:
            with open(logp, "a") as f:
                f.write("%s %d %d %d %.2f %d %d %s\n" % (time.strftime("%H:%M:%S"), n, rmax, bmin, bsum / n, bmax, smax,
                                                         token_count()))
            w0, n, rmax, bmin, bsum, bmax, smax = time.time(), 0, 0, 99, 0, 0, 0
        time.sleep(interval)


if __name__ == "__main__":
    main()
