#!/usr/bin/env python3
"""RSS/disk guard for moqls8-encoder-binding-v1.
python -B guard.py --receipt R.json --log L.log [--limit-gib 6] -- CMD ...
Refuses to start below the free-disk floor (12e9 bytes).  Samples the aggregate RSS of CMD's process tree every 2 s
(ps); above the limit it sends SIGTERM to every process of the tree (children first) and waits at most 120 s.
Never SIGKILL.  Receipt (mode x): argv, start/end host time, return code, peak sampled tree RSS, trip record."""
import argparse
import datetime
import json
import os
import resource
import shutil
import signal
import subprocess
import time

FLOOR = 12_000_000_000


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def tree(root):
    out = subprocess.run(["ps", "-axo", "pid=,ppid=,rss="], capture_output=True, text=True).stdout
    kids, rss = {}, {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) != 3:
            continue
        pid, ppid, r = map(int, parts)
        kids.setdefault(ppid, []).append(pid)
        rss[pid] = r
    order, stack = [], [root]
    while stack:
        p = stack.pop()
        if p in rss:
            order.append(p)
        stack.extend(kids.get(p, []))
    return order, sum(rss[p] for p in order) * 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--receipt", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--limit-gib", type=float, default=6.0)
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
    limit = int(a.limit_gib * 2 ** 30)
    rec = {"cmd": cmd, "cwd": os.getcwd(), "limit_bytes": limit, "start": now(),
           "disk_free_start": shutil.disk_usage(os.path.dirname(os.path.abspath(a.receipt))).free}
    if rec["disk_free_start"] < FLOOR:
        rec["refused"] = "free disk below floor"
        with open(a.receipt, "x") as fh:
            json.dump(rec, fh, indent=1)
        raise SystemExit(3)
    peak, samples, trip = 0, 0, None
    t0 = time.time()
    with open(a.log, "x") as lg:
        p = subprocess.Popen(cmd, stdout=lg, stderr=subprocess.STDOUT)
        while p.poll() is None:
            pids, r = tree(p.pid)
            samples += 1
            peak = max(peak, r)
            if r > limit:
                trip = {"time": now(), "tree_rss": r, "pids": pids}
                for q in reversed(pids):
                    try:
                        os.kill(q, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
                deadline = time.time() + 120
                while p.poll() is None and time.time() < deadline:
                    time.sleep(1)
                trip["exited_within_bounded_wait"] = p.poll() is not None
                break
            time.sleep(2)
    rec.update(end=now(), wall_s=round(time.time() - t0, 1), returncode=p.poll(), samples=samples,
               peak_sampled_tree_rss_bytes=peak, trip=trip,
               children_maxrss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
               disk_free_end=shutil.disk_usage(os.path.dirname(os.path.abspath(a.receipt))).free)
    with open(a.receipt, "x") as fh:
        json.dump(rec, fh, indent=1)


if __name__ == "__main__":
    main()
