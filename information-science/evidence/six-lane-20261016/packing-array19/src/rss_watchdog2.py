#!/usr/bin/env python3
"""Aggregate lane RSS watchdog, revision 2 (for the revision-11 staged runners; parent audit 15:4x-15:5x).
Every INTERVAL (<= 2 s) one `ps` snapshot is taken. Lane processes are grouped by OWNER: each lane runner
(Python process running a script named in RUNNERS) together with all of its descendants (solver, checker,
extend helper, any other child) forms one group; lane processes not under a runner (command line contains the
lane path) form the group 'other'. The group RSS includes the runner itself (CNF construction, compressed
proof buffers) and every descendant.
  * Trip (sum over all groups > LIMIT_KB = 8 GiB): the target is the runner holding the most recently acquired
    CPU token (token files cycle2/tokens/tN record 'pid time stage' at acquisition; the holder must currently
    have the file open, checked with lsof); if no runner holds a token, the runner of the largest group. The
    target RUNNER gets SIGTERM; its revision-11 handler forwards SIGTERM to its live children and releases its
    token only after they have exited (quarantine otherwise). Bounded wait 60 s for the runner's group to
    shrink or exit (no SIGKILL). COUNT is then lowered by one (minimum 1). Record cycle2/RSS-WATCHDOG2-<time>.json
    with every group (pid, kind, RSS) and the outcome.
  * Disk floor: if free bytes < 12e9 the stop files cycle2/STOP-hard11 and cycle2/STOP-m2r11 are created (rev-11
    runners re-check them at every admission).
  * Every WINDOW seconds one line is appended to the samples log: clock span of the window (first and last sample
    time), samples, lane RSS max (KB), busy_all max/mean (state R among runners and their descendants), busy
    solver/checker max/mean, number of lane runners/groups max, token COUNT. These are samples, not a proof of a
    bound; the bound comes from the token admission (COUNT <= 2, <= 2 busy processes per token).
Matching uses the FULL command line (records keep a 240-character prefix): a first smoke run matched on the
truncated prefix, missed the test runner (long absolute paths) and targeted the largest group instead.
Usage: rss_watchdog2.py [--limit-kb N] [--log FILE] [--once] [INTERVAL_S [WINDOW_S]]
"""
import json
import os
import signal
import subprocess
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, "cycle2")
TOK = os.path.join(C2, "tokens")
RUNNERS = ("run_hard11.py", "run_m2_11.py", "smoke_stream11.py", "smoke11_helper_runner.py")
SOLVERS = ("kissat", "cadical", "drat-trim")
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
    runners = [p for p in procs.values() if "python" in p["exe"].lower() and
               any(("src/" + r) in p["full"] or ("/" + r) in p["full"] for r in RUNNERS)]
    rset = {p["pid"] for p in runners}
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
    other = {"runner": None, "members": []}
    for pid, p in procs.items():
        if pid in owner:
            groups[owner[pid]]["members"].append(p)
        elif LANE in p["full"]:
            other["members"].append(p)
    for g in list(groups.values()) + [other]:
        g["rss_kb"] = sum(m["rss"] for m in g["members"])
    return procs, groups, other


def token_holders():
    hold = []
    for i in range(8):
        p = os.path.join(TOK, "t%d" % i)
        if not os.path.exists(p):
            continue
        try:
            txt = open(p).read().split()
            pid, since = int(txt[0]), float(txt[1])
        except (OSError, ValueError, IndexError):
            continue
        lo = subprocess.run(["lsof", "-t", p], capture_output=True, text=True).stdout.split()
        if str(pid) in lo:
            hold.append({"token": "t%d" % i, "pid": pid, "since": since, "stage": txt[2] if len(txt) > 2 else None})
    return hold


def token_count():
    try:
        return int(open(os.path.join(TOK, "COUNT")).read().split()[0])
    except (OSError, ValueError, IndexError):
        return None


def trip(groups, other, total, limit, log_dir):
    t = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    hold = token_holders()
    target = None
    live_holders = [h for h in hold if h["pid"] in groups]
    if live_holders:
        target = max(live_holders, key=lambda h: h["since"])["pid"]
    elif groups:
        target = max(groups.values(), key=lambda g: g["rss_kb"])["runner"]
    rec = {"time": t, "lane_rss_kb": total, "limit_kb": limit, "token_holders": hold, "target_runner": target,
           "groups": [{"runner": g["runner"], "cmd": g.get("cmd"), "rss_kb": g["rss_kb"],
                       "members": [{k: m[k] for k in ("pid", "ppid", "stat", "rss", "exe")} for m in g["members"]]}
                      for g in list(groups.values()) + [other]], "actions": []}
    if target:
        try:
            os.kill(target, signal.SIGTERM)
            rec["actions"].append({"SIGTERM": target})
        except OSError as e:
            rec["actions"].append({"SIGTERM_failed": target, "err": str(e)})
        t0 = time.time()
        while time.time() - t0 < 60:
            time.sleep(1)
            procs, g2, _ = snapshot()
            if target not in g2:
                rec["runner_exit_after_s"] = round(time.time() - t0, 1)
                break
        else:
            rec["runner_still_alive_after_60s"] = True
    c = token_count()
    if c and c > 1:
        open(os.path.join(TOK, "COUNT"), "w").write("%d\n" % (c - 1))
        rec["actions"].append({"token_count": [c, c - 1]})
    with open(os.path.join(log_dir, "RSS-WATCHDOG2-%s.json" % time.strftime("%Y%m%dT%H%M%S")), "w") as f:
        json.dump(rec, f, indent=1)
    return rec


def main():
    args = sys.argv[1:]
    limit, logp, once = 8 * 1024 * 1024, os.path.join(C2, "watchdog2-samples.log"), False
    rest = []
    i = 0
    while i < len(args):
        if args[i] == "--limit-kb":
            limit = int(args[i + 1])
            i += 2
        elif args[i] == "--log":
            logp = args[i + 1]
            i += 2
        elif args[i] == "--once":
            once = True
            i += 1
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
        procs, groups, other = snapshot()
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
                for n in ("STOP-hard11", "STOP-m2r11"):
                    p = os.path.join(C2, n)
                    if not os.path.exists(p):
                        with open(p, "w") as f:
                            f.write("%s watchdog2 disk floor\n" % time.strftime("%Y-%m-%dT%H:%M:%S%z"))
        except OSError:
            pass
        if total > limit:
            rec = trip(groups, other, total, limit, os.path.dirname(logp))
            if once:
                print(json.dumps({"tripped": True, "target": rec["target_runner"], "lane_rss_kb": total}), flush=True)
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
