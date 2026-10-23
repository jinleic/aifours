"""Run a command with a wall-clock bound, stopping it cooperatively (parent safety rule): on timeout send SIGTERM, wait
up to 30 s; if it still runs, leave it running and report its pid (never SIGKILL). Prints a JSON status line.
python -B run_bounded.py --seconds 600 --stdout LOG -- CMD ARGS...
"""
from __future__ import annotations

import argparse
import json
import signal
import subprocess
import sys
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=int, required=True)
    ap.add_argument("--stdout", required=True)
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    cmd = a.cmd[1:] if a.cmd and a.cmd[0] == "--" else a.cmd
    t0 = time.time()
    with open(a.stdout, "x") as out:
        p = subprocess.Popen(cmd, stdout=out, stderr=subprocess.STDOUT)
        status = "finished"
        try:
            p.wait(timeout=a.seconds)
        except subprocess.TimeoutExpired:
            status = "timeout_sigterm"
            p.send_signal(signal.SIGTERM)
            try:
                p.wait(timeout=30)
            except subprocess.TimeoutExpired:
                status = "still_running_after_sigterm"
    print(json.dumps({"cmd": cmd, "status": status, "exit": p.returncode, "pid": p.pid,
                      "secs": round(time.time() - t0, 1)}), flush=True)


if __name__ == "__main__":
    main()
