#!/usr/bin/env python3
"""Aggregate lane RSS watchdog, revision 4 (REV11b, parent decision 2026-10-17 ~16:1x). It never sends a signal to
any process: there is no os.kill / signal-module / terminate code path in this file.

Every INTERVAL (<= 2 s) one `ps` snapshot is taken. Lane processes are grouped by owner: a lane runner is a Python
process whose argv contains the exact absolute path <LANE>/src/<name> for a name in RUNNERS; its group is itself plus
all of its descendants (ppid chain). Lane processes not under a runner whose command line contains the lane path form
the group 'other'. Lane RSS = sum over all groups.
  * Trip (lane RSS > LIMIT_KB, default 8 GiB): admissions are paused -- cycle2/tokens/COUNT := 0 and the stop files in
    STOPS are created -- an alert JSON cycle2/RSS-ALERT4-<time>.json (or next to --log) is written with the time, the
    lane RSS, every group (pid, kind, RSS of each member) and the token metadata (content of each token file and the
    pids that have it open, informational only), and the watchdog exits. Running stages stay bounded by their native
    solver limits and checker budgets; recovery (resuming admissions) is a parent decision.
  * Disk floor: free bytes < 12e9 -> the stop files are created (admissions refused by the revision-12 runners).
  * Every WINDOW seconds one line is appended to the samples log: first and last sample clock of the window, samples,
    lane RSS max (KB), busy_all max/mean (state R among runners and descendants), busy solver/checker max/mean,
    runners max, token COUNT. Samples are observations, not a proof of any bound.
Usage: rss_watchdog4.py [--limit-kb N] [--log FILE] [INTERVAL_S [WINDOW_S]]
"""
import json
import os
import subprocess
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, "cycle2")
TOK = os.path.join(C2, "tokens")
RUNNERS = ("run_hard12.py", "run_m2_12.py", "smoke_rev12b.py", "smoke12_runner.py")
SOLVERS = ("kissat", "cadical", "drat-trim")
STOPS = ("STOP-hard12", "STOP-m2r12")
FLOOR = 12000000000


def snapshot():
    out = subprocess.run(["ps", "-Ao", "pid=,ppid=,stat=,rss=,command="], capture_output=True, text=True).stdout
    procs = {}
    for line in out.splitlines():
        parts = line.split(None, 4)
        if len(parts) < 5:
            continue
        pid, ppid, stat, rss, cmd = int(parts[0]), int(parts[1]), parts[2], int(parts[3]), parts[4]
        procs[pid] = {"pid": pid, "ppid": ppid, "stat": stat, "rss": rss, "cmd": cmd[:240], "full": cmd,
                      "exe": os.path.basename(cmd.split()[0]) if cmd.split() else ""}
    rset = {p["pid"] for p in procs.values() if "python" in p["exe"].lower() and
            any(os.path.join(LANE, "src", r) in p["full"].split() for r in RUNNERS)}
    owner = {}
    for pid in procs:
        cur, seen = pid, 0
        while cur in procs and seen < 64:
            if cur in rset:
                owner[pid] = cur
                break
            cur = procs[cur]["ppid"]
            seen += 1
    groups = {r: {"runner": r, "cmd": procs[r]["cmd"], "members": []} for r in rset}
    other = {"runner": None, "cmd": None, "members": []}
    for pid, p in procs.items():
        if pid in owner:
            groups[owner[pid]]["members"].append(p)
        elif LANE in p["full"]:
            other["members"].append(p)
    for g in list(groups.values()) + [other]:
        g["rss_kb"] = sum(m["rss"] for m in g["members"])
    return groups, other


def token_metadata():
    meta = []
    for i in range(8):
        p = os.path.join(TOK, "t%d" % i)
        if not os.path.exists(p):
            continue
        try:
            content = open(p).read().strip()
        except OSError:
            content = None
        opened_by = subprocess.run(["lsof", "-t", p], capture_output=True, text=True).stdout.split()
        meta.append({"token": "t%d" % i, "content": content, "open_by_pids": opened_by})
    return meta


def token_count():
    try:
        return int(open(os.path.join(TOK, "COUNT")).read().split()[0])
    except (OSError, ValueError, IndexError):
        return None


def create_stops(reason):
    made = []
    for n in STOPS:
        p = os.path.join(C2, n)
        if not os.path.exists(p):
            with open(p, "w") as f:
                f.write("%s watchdog4 %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), reason))
            made.append(n)
    return made


def trip(groups, other, total, limit, alert_dir):
    rec = {"time": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "lane_rss_kb": total, "limit_kb": limit, "signals_sent": 0}
    prev = token_count()
    with open(os.path.join(TOK, "COUNT"), "w") as f:
        f.write("0\n")
    rec["token_count"] = [prev, 0]
    rec["stop_files_created"] = create_stops("RSS trip: admissions paused")
    rec["token_metadata"] = token_metadata()
    rec["groups"] = [{"runner": g["runner"], "cmd": g["cmd"], "rss_kb": g["rss_kb"],
                      "members": [{k: m[k] for k in ("pid", "ppid", "stat", "rss", "exe")} for m in g["members"]]}
                     for g in list(groups.values()) + [other]]
    rec["outcome"] = "admissions paused; no process signalled; recovery is a parent decision"
    path = os.path.join(alert_dir, "RSS-ALERT4-%s.json" % time.strftime("%Y%m%dT%H%M%S"))
    with open(path, "w") as f:
        json.dump(rec, f, indent=1)
    return path


def main():
    args = sys.argv[1:]
    limit, logp, rest = 8 * 1024 * 1024, os.path.join(C2, "watchdog4-samples.log"), []
    i = 0
    while i < len(args):
        if args[i] == "--limit-kb":
            limit = int(args[i + 1])
            i += 2
        elif args[i] == "--log":
            logp = args[i + 1]
            i += 2
        else:
            rest.append(args[i])
            i += 1
    interval = min(2.0, float(rest[0])) if rest else 2.0
    window = float(rest[1]) if len(rest) > 1 else 30.0
    if not os.path.exists(logp):
        with open(logp, "w") as f:
            f.write("# first last samples lane_rss_max_kb busy_all_max busy_all_mean busy_sc_max busy_sc_mean runners_max count\n")
    w = None
    while True:
        now = time.time()
        groups, other = snapshot()
        total = sum(g["rss_kb"] for g in groups.values()) + other["rss_kb"]
        mem = [m for g in groups.values() for m in g["members"]]
        busy_all = sum(1 for m in mem if m["stat"].startswith("R"))
        busy_sc = sum(1 for m in mem + other["members"] if m["exe"] in SOLVERS and m["stat"].startswith("R"))
        if w is None:
            w = {"first": now, "n": 0, "rss": 0, "ba": 0, "bas": 0, "bs": 0, "bss": 0, "runners": 0}
        w["n"] += 1
        w["last"] = now
        w["rss"] = max(w["rss"], total)
        w["ba"], w["bas"] = max(w["ba"], busy_all), w["bas"] + busy_all
        w["bs"], w["bss"] = max(w["bs"], busy_sc), w["bss"] + busy_sc
        w["runners"] = max(w["runners"], len(groups))
        try:
            st = os.statvfs(LANE)
            if st.f_bavail * st.f_frsize < FLOOR:
                create_stops("disk floor")
        except OSError:
            pass
        if total > limit:
            path = trip(groups, other, total, limit, os.path.dirname(logp))
            print(json.dumps({"tripped": True, "lane_rss_kb": total, "alert": path, "signals_sent": 0}), flush=True)
            return
        if now - w["first"] >= window:
            with open(logp, "a") as f:
                f.write("%s %s %d %d %d %.2f %d %.2f %d %s\n" % (
                    time.strftime("%H:%M:%S", time.localtime(w["first"])), time.strftime("%H:%M:%S", time.localtime(w["last"])),
                    w["n"], w["rss"], w["ba"], w["bas"] / w["n"], w["bs"], w["bss"] / w["n"], w["runners"], token_count()))
            w = None
        time.sleep(interval)


if __name__ == "__main__":
    main()
