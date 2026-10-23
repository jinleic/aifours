#!/usr/bin/env python3
"""Stop the running replay driver at an instance boundary (no in-flight solver/checker), for the parent's
23:17 disk rule. Waits (kqueue, no polling) for the next receipt, SIGSTOPs the driver, lists its children,
and SIGTERMs it only if no solver/checker child is alive; otherwise SIGCONTs and waits for the next boundary.
Usage: boundary_stop.py DRIVER_PID RECEIPTS_DIR OUT.json
"""
import json
import os
import select
import signal
import subprocess
import sys
import time


def children(pid):
    out = subprocess.run(["/bin/ps", "-axo", "pid=,ppid=,comm="], capture_output=True, text=True).stdout
    kids = []
    for line in out.splitlines():
        parts = line.split(None, 2)
        if len(parts) == 3 and parts[1] == str(pid):
            kids.append({"pid": int(parts[0]), "comm": parts[2]})
    return kids


def main(pid, rdir, out):
    pid = int(pid)
    log = []
    fd = os.open(rdir, os.O_RDONLY)
    kq = select.kqueue()
    ev = select.kevent(fd, filter=select.KQ_FILTER_VNODE, flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
                       fflags=select.KQ_NOTE_WRITE)
    kq.control([ev], 0, 0)
    for attempt in range(10):
        n0 = len(os.listdir(rdir))
        kq.control(None, 1, 600)
        time.sleep(0.5)                       # let the driver finish writing the receipt it just created
        os.kill(pid, signal.SIGSTOP)
        for _ in range(5):                    # never stop it mid-receipt: every receipt must parse
            try:
                for name in os.listdir(rdir):
                    with open(os.path.join(rdir, name)) as f:
                        json.load(f)
                break
            except ValueError:
                os.kill(pid, signal.SIGCONT)
                time.sleep(0.3)
                os.kill(pid, signal.SIGSTOP)
        kids = children(pid)
        busy = [k for k in kids if os.path.basename(k["comm"]) in ("kissat", "cadical", "drat-trim")]
        log.append({"attempt": attempt, "receipts_before": n0, "receipts_now": len(os.listdir(rdir)),
                    "stopped_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "children": kids, "busy": busy})
        if not busy:
            os.kill(pid, signal.SIGTERM)
            os.kill(pid, signal.SIGCONT)
            for _ in range(240):
                try:
                    os.kill(pid, 0)
                except ProcessLookupError:
                    break
                time.sleep(0.25)
            log[-1]["terminated"] = True
            log[-1]["children_after"] = children(pid)
            break
        os.kill(pid, signal.SIGCONT)
    with open(out, "x") as f:
        json.dump({"driver_pid": pid, "log": log}, f, indent=1)
    print(json.dumps(log, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:])
