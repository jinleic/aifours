#!/usr/bin/env python3
"""Drain helper for the parent F_one replay desk (parent DRAIN request). At the next natural pipeline boundary of
the running replay_v1.py driver -- a NEW '<label> verdict ...' or 'gate <label>: projected N' driver-log line, both
printed only after the previous pipeline's children were reaped and before the next gate's first decision -- send
the driver exactly one SIGTERM, which makes its gate return 'stopped' without admitting a new native replay. Never
signals while a native child of the driver is alive; never SIGKILL; bounded 120 s wait after the signal.
Usage: /usr/bin/python3 -I -B drain_v1.py DRIVER_LOG OUT_JSON   (OUT_JSON created exclusively)
"""
import datetime
import json
import os
import re
import signal
import subprocess
import sys
import time

NATIVE = {"cadical", "drat-trim"}
TRIGGER = re.compile(rb"^\S+ (?:\S+ verdict \S+ |gate \S+: projected \d+$)")


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="milliseconds")


def ps_state(pid):
    p = subprocess.run(["/bin/ps", "-o", "stat=", "-p", str(pid)], capture_output=True)
    s = p.stdout.decode().strip()
    return s or None


def native_children(pid):
    p = subprocess.run(["/bin/ps", "-axo", "pid=,ppid=,comm="], capture_output=True)
    out = []
    for line in p.stdout.decode("utf-8", "replace").splitlines():
        parts = line.split(None, 2)
        if len(parts) == 3 and parts[1] == str(pid) and os.path.basename(parts[2].strip()) in NATIVE:
            out.append({"pid": int(parts[0]), "comm": os.path.basename(parts[2].strip())})
    return out


def alive(pid):
    s = ps_state(pid)
    return s is not None and not s.startswith("Z")


def main():
    log_path, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if os.path.lexists(out):
        raise SystemExit("ABORT: output exists")
    with open(log_path, "rb") as f:
        first = f.readline().decode()
        f.seek(0, 2)
        pos = f.tell()
    m = re.search(r"driver pid (\d+)", first)
    pid = int(m.group(1))
    args = subprocess.run(["/bin/ps", "-ww", "-o", "args=", "-p", str(pid)], capture_output=True).stdout.decode().strip()
    if "replay_v1.py run" not in args:
        raise SystemExit("ABORT: pid %d is not the replay driver: %r" % (pid, args))
    rec = {"started_at": now(), "driver_pid": pid, "driver_args": args, "driver_log": log_path,
           "rule": __doc__.strip(), "events": []}
    print("watching driver pid %d from log offset %d at %s" % (pid, pos, rec["started_at"]), flush=True)
    buf, sent_mono = b"", None
    while True:
        is_alive = alive(pid)
        with open(log_path, "rb") as f:
            f.seek(pos)
            data = f.read()
        pos += len(data)
        buf += data
        parts = buf.split(b"\n")
        buf = parts.pop()
        for ln in parts:
            if sent_mono is None and TRIGGER.match(ln):
                kids = native_children(pid)
                if kids:
                    rec["events"].append({"at": now(), "event": "trigger skipped: native child alive", "kids": kids,
                                          "line": ln.decode("ascii", "replace")})
                    continue
                os.kill(pid, signal.SIGTERM)
                sent_mono = time.monotonic()
                rec["events"].append({"at": now(), "event": "SIGTERM sent to driver (no native child alive)",
                                      "line": ln.decode("ascii", "replace")})
                print("SIGTERM sent at %s after line: %s" % (rec["events"][-1]["at"], ln.decode()), flush=True)
        if not is_alive:
            rec["events"].append({"at": now(), "event": "driver exited"})
            break
        if sent_mono is not None and time.monotonic() - sent_mono > 120:
            rec["events"].append({"at": now(), "event": "driver alive 120 s after SIGTERM; no escalation"})
            break
        time.sleep(0.1)
    rec["finished_at"] = now()
    rec["driver_alive_at_end"] = alive(pid)
    rec["native_children_of_driver_at_end"] = native_children(pid)
    with open(out, "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec, indent=1), flush=True)


if __name__ == "__main__":
    main()
