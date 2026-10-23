#!/usr/bin/env python3
"""Bound a pure-Python, no-native-child calibration with its own real-time alarm.
Usage: run_python_bounded_c21v1.py SECONDS SCRIPT [ARGS...]
The outer lane queue records exit124 and all retained partial artifacts on a
limit; it must not interpret missing/partial checker JSON as a pass. No tool/eval
cell deadline, native child timeout, Popen.kill or SIGKILL is involved. The script
executes in this one process. Never use this for programs spawning native work.
"""
import runpy
import signal
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

seconds = int(sys.argv[1])
script = Path(sys.argv[2]).resolve()
root = Path(__file__).resolve().parents[1]
if not 1 <= seconds <= 10800 or root not in script.parents:
    raise SystemExit('invalid calibration bound/path')


def expired(signum, frame):
    print('c UNKNOWN pure-Python native alarm limit', seconds,
          datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), flush=True)
    raise SystemExit(124)


signal.signal(signal.SIGALRM, expired)
signal.alarm(seconds)
sys.dont_write_bytecode = True
sys.path.insert(0, str(script.parent))
sys.argv = [str(script)] + sys.argv[3:]
try:
    runpy.run_path(str(script), run_name='__main__')
finally:
    signal.alarm(0)
