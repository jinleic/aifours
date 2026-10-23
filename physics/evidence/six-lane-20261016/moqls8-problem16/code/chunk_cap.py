"""Cooperative stop for a running leaf runner (3 h chunk cap and shared disk floor; SIGTERM + bounded wait only,
never SIGKILL, never deletes). Every 10 s: if the runner has exited, write a receipt and stop; if time ≥ --stop-at
(epoch seconds) or filesystem free < --floor, SIGTERM the runner first (no further leaf starts; the in-flight leaf
gets no receipt and stays UNSTARTED in the ledger), then SIGTERM the in-flight solver/checker (processes whose command
line contains --child-pattern), wait ≤ 120 s, write the receipt.
python -B chunk_cap.py --runner-pid PID --stop-at EPOCH --child-pattern strict_L2/w0 --path DIR --receipt R.json
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import time


def alive(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    st = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return bool(st) and not st.startswith("Z")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner-pid", type=int, required=True)
    ap.add_argument("--stop-at", type=float, required=True)
    ap.add_argument("--child-pattern", required=True)
    ap.add_argument("--path", required=True)
    ap.add_argument("--receipt", required=True)
    ap.add_argument("--floor", type=int, default=12_000_000_000)
    a = ap.parse_args()
    lowest = None
    while alive(a.runner_pid):
        free = shutil.disk_usage(a.path).free
        lowest = free if lowest is None else min(lowest, free)
        if time.time() >= a.stop_at or free < a.floor:
            why = "chunk_cap" if time.time() >= a.stop_at else "disk_floor"
            os.kill(a.runner_pid, signal.SIGTERM)
            time.sleep(2)
            kids = [int(x) for x in subprocess.run(["pgrep", "-f", a.child_pattern], capture_output=True,
                                                   text=True).stdout.split() if int(x) != os.getpid()]
            for p in kids:
                try:
                    os.kill(p, signal.SIGTERM)
                except OSError:
                    pass
            t0 = time.time()
            while time.time() - t0 < 120 and any(alive(p) for p in kids + [a.runner_pid]):
                time.sleep(2)
            with open(a.receipt, "x") as fh:
                json.dump({"event": why, "time": time.ctime(), "free": free, "signalled": [a.runner_pid] + kids,
                           "still_alive": [p for p in kids + [a.runner_pid] if alive(p)]}, fh)
            return
        time.sleep(10)
    with open(a.receipt, "x") as fh:
        json.dump({"event": "runner_finished", "time": time.ctime(), "lowest_free": lowest}, fh)


if __name__ == "__main__":
    main()
