#!/usr/bin/env python3
"""Detached launcher for desk D: starts '/usr/bin/python3 -I -B scripts/replay_v5d.py run PREEXEC' in its own
session (never in the caller's process group) with a clean environment (TMPDIR=<desk>/tmp/), stdin /dev/null and
stdout/stderr appended to a NEW console log (exclusive create), prints the driver pid and exits. It launches nothing
else and never signals anything.
Usage: /usr/bin/python3 -I -B scripts/launch_v5d.py PREEXEC logs/CONSOLE_LOG"""
import os
import subprocess
import sys

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-strengthened-parent-replay-v1"
SCRIPT = DESK + "/scripts/replay_v5d.py"


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    pre, console = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if not (pre.startswith(DESK + "/") and os.path.isfile(pre) and console.startswith(DESK + "/logs/")):
        raise SystemExit("PRE-EXEC must be a desk file and the console log must be new under logs/")
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": os.environ.get("HOME", DESK), "TMPDIR": DESK + "/tmp/",
           "LC_ALL": "C"}
    with open(console, "xb") as log:
        p = subprocess.Popen(["/usr/bin/python3", "-I", "-B", SCRIPT, "run", pre], stdin=subprocess.DEVNULL,
                             stdout=log, stderr=subprocess.STDOUT, cwd=DESK + "/tmp", env=env, start_new_session=True)
    print("driver pid %d console %s" % (p.pid, console))


if __name__ == "__main__":
    main()
