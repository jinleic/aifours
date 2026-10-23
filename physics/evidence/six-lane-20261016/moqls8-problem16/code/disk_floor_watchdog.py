"""Run-wide disk floor guard (parent rule, 13:29 PDT): while the watched driver process runs, check the filesystem free
bytes every 10 s; if free < --floor (default 12,000,000,000 bytes), send SIGTERM to the driver and to every process whose
command line matches --child-pattern (the growing proof stream: solver and zstd), wait up to 60 s, write a receipt and
exit. Never deletes, never SIGKILL. Exits quietly when the driver ends.
python -B disk_floor_watchdog.py --driver-pid PID --child-pattern k5_split_v1/all --path LANE --receipt R.json
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
        return True
    except OSError:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--driver-pid", type=int, required=True)
    ap.add_argument("--child-pattern", required=True)
    ap.add_argument("--path", required=True)
    ap.add_argument("--receipt", required=True)
    ap.add_argument("--floor", type=int, default=12_000_000_000)
    a = ap.parse_args()
    lowest = None
    while alive(a.driver_pid):
        free = shutil.disk_usage(a.path).free
        lowest = free if lowest is None else min(lowest, free)
        if free < a.floor:
            pids = [int(x) for x in subprocess.run(["pgrep", "-f", a.child_pattern], capture_output=True,
                                                   text=True).stdout.split() if int(x) != os.getpid()]
            for pid in [a.driver_pid] + pids:
                try:
                    os.kill(pid, signal.SIGTERM)
                except OSError:
                    pass
            t0 = time.time()
            while time.time() - t0 < 60 and any(alive(p) for p in [a.driver_pid] + pids):
                time.sleep(2)
            with open(a.receipt, "x") as fh:
                json.dump({"event": "disk_floor_stop", "free_bytes": free, "floor": a.floor, "time": time.ctime(),
                           "signalled": [a.driver_pid] + pids,
                           "still_alive": [p for p in [a.driver_pid] + pids if alive(p)]}, fh)
            return
        time.sleep(10)
    with open(a.receipt, "x") as fh:
        json.dump({"event": "driver_finished", "lowest_free_bytes": lowest, "floor": a.floor, "time": time.ctime()}, fh)


if __name__ == "__main__":
    main()
