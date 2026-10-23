#!/usr/bin/env python3
"""Lane disk guard for the parent's run-wide floor (2026-10-17 13:29): every INTERVAL seconds check
filesystem free bytes; if free < 12,000,000,000 bytes:
  * create cycle2/STOP-m2skel9 and cycle2/STOP-m2partbatch5 (cooperative stop of the M2 runners);
  * SIGTERM the M1 runner processes run_hard8.py / run_hard6.py and their solver/checker children
    (identified by this lane's FIFO directory prefixes v8k_ / v8c_ / v6pb_), bounded wait, no
    SIGKILL; interrupted cases stay UNKNOWN (no record is written for them);
  * write cycle2/DISK-GUARD-<time>.json with the measurements and actions, then exit.
Sleeping loop; negligible CPU. Usage: disk_guard.py [INTERVAL_S]
"""
import json
import os
import signal
import subprocess
import sys
import time

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOOR = 12000000000


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def pids_matching(subs):
    out = subprocess.run(["ps", "-Ao", "pid=,command="], capture_output=True, text=True).stdout
    res = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        pid, _, cmd = line.partition(" ")
        if LANE in cmd or "src/run_hard" in cmd:
            if any(s in cmd for s in subs) and int(pid) != os.getpid():
                res.append((int(pid), cmd[:200]))
    return res


def main():
    interval = float(sys.argv[1]) if len(sys.argv) > 1 else 120
    while True:
        fb = free_bytes()
        if fb >= FLOOR:
            time.sleep(interval)
            continue
        t = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        rec = {"time": t, "free_bytes": fb, "floor": FLOOR, "actions": []}
        for name in ("STOP-m2skel9", "STOP-m2partbatch5"):
            p = os.path.join(LANE, "cycle2", name)
            if not os.path.exists(p):
                with open(p, "w") as f:
                    f.write("%s disk guard: free %d < %d bytes\n" % (t, fb, FLOOR))
                rec["actions"].append("created " + name)
        mains = pids_matching(["run_hard8.py", "run_hard6.py"])
        for pid, cmd in mains:
            try:
                os.kill(pid, signal.SIGTERM)
                rec["actions"].append({"SIGTERM": pid, "cmd": cmd})
            except OSError as e:
                rec["actions"].append({"SIGTERM_failed": pid, "err": str(e)})
        time.sleep(2)
        kids = pids_matching(["/v8k_", "/v8c_", "/v6pb_"])
        for pid, cmd in kids:
            try:
                os.kill(pid, signal.SIGTERM)
                rec["actions"].append({"SIGTERM": pid, "cmd": cmd})
            except OSError as e:
                rec["actions"].append({"SIGTERM_failed": pid, "err": str(e)})
        time.sleep(60)
        rec["still_running_after_60s"] = pids_matching(["run_hard8.py", "run_hard6.py", "/v8k_", "/v8c_", "/v6pb_"])
        json.dump(rec, open(os.path.join(LANE, "cycle2", "DISK-GUARD-%s.json" % time.strftime("%Y%m%dT%H%M%S")), "w"), indent=1)
        print(json.dumps(rec), flush=True)
        return


if __name__ == "__main__":
    main()
