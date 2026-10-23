#!/usr/bin/env python3
"""Run a command, sample the summed RSS of its whole process tree every second, and kill the tree
if the sum exceeds a cap. Usage: watch_cmd.py <cap-kb> <jsonl-log> -- command args...
Prints (to stdout) and appends (to the log) one JSON line with exit code, seconds, peak and cap."""
import json
import os
import signal
import subprocess
import sys
import time


def tree(root):
    out = subprocess.run(['ps', '-axo', 'pid=,ppid=,rss='], capture_output=True, text=True).stdout
    kids, rss = {}, {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 3 and all(x.isdigit() for x in parts):
            pid, ppid, r = map(int, parts)
            kids.setdefault(ppid, []).append(pid)
            rss[pid] = r
    stack, pids, total = [root], [], 0
    while stack:
        p = stack.pop()
        pids.append(p)
        total += rss.get(p, 0)
        stack.extend(kids.get(p, []))
    return total, pids


def main():
    cap, log = int(sys.argv[1]), sys.argv[2]
    cmd = sys.argv[sys.argv.index('--') + 1:]
    t0 = time.time()
    proc = subprocess.Popen(cmd)
    peak, killed = 0, False
    while proc.poll() is None:
        time.sleep(1)
        total, pids = tree(proc.pid)
        peak = max(peak, total)
        if total > cap and not killed:
            for p in reversed(pids):
                try:
                    os.kill(p, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            killed = True
    rec = {'command': ' '.join(cmd)[-240:], 'exit_code': proc.returncode,
           'seconds': round(time.time() - t0, 1), 'peak_kb': peak, 'cap_kb': cap, 'killed': killed}
    line = json.dumps(rec)
    print(line, flush=True)
    with open(log, 'a') as f:
        f.write(line + '\n')
    sys.exit(137 if killed else proc.returncode)


if __name__ == '__main__':
    main()
