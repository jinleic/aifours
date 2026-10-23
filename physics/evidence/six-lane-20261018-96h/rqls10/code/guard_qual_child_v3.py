#!/usr/bin/env python3
"""guard_qual_child_v3: preregistered test children for the guard qualification of code/owned_supervisor_v6.py (plan
evidence/owned_supervisor_v6-guard-qualification-plan-v2.md). Supersedes guard_qual_child_v2.py (never run); adds
rc_nonzero, no_output, mutate_pin and mutate_evidence. Standard library only, no science. EVERY process started here
ends by itself within LIFE_S seconds of its own start even if it is never signalled (no permanent process).
Protocol: reads one line from stdin and requires "GO" (else exit 6). Usage:
  guard_qual_child_v3.py MODE OUT LIFE_S [TARGET]
  ok              write OUT (one JSON line), print 3 short lines, exit 0.
  rc_nonzero      write OUT, exit 3.
  no_output       print one line, exit 0 WITHOUT writing OUT (OUT is a required output in its config).
  mutate_pin      append the byte b"x" to TARGET (a file pinned in the config), write OUT, exit 0.
  mutate_evidence append the byte b"x" to TARGET (the supervisor's launch record), write OUT, exit 0.
  flood           print 64 KiB lines to stdout until SIGTERM (default action) or LIFE_S.
  sleep           sleep in 0.1 s steps until SIGTERM (default action) or LIFE_S, then write OUT, exit 0.
  ignore_term     ignore SIGTERM (records the arrival times), sleep until LIFE_S, write OUT, exit 0.
  escape_slow     fork a grandchild that calls setsid() and sleeps LIFE_S; the child waits 3 s, writes OUT, exits 0.
  escape_fast     as escape_slow but the child writes OUT and exits immediately after the fork.
  busy3           fork two CPU-bound grandchildren in the same process group and spin itself; all stop at LIFE_S or
                  on SIGTERM (default action).
  rss             allocate and touch 320 MiB, then sleep until SIGTERM (default action) or LIFE_S.
"""
import json, os, signal, sys, time

if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
MODE, OUT, LIFE = sys.argv[1], sys.argv[2], float(sys.argv[3])
TARGET = sys.argv[4] if len(sys.argv) > 4 else None
T0 = time.monotonic()


def alive(t0=None):
    return time.monotonic() - (T0 if t0 is None else t0) < LIFE


def write_out(extra):
    with open(OUT, "x") as fh:
        fh.write(json.dumps(dict({"mode": MODE, "pid": os.getpid(), "elapsed_s": time.monotonic() - T0}, **extra)) + "\n")


def fork_bounded(body):
    pid = os.fork()
    if pid == 0:
        try:
            body(time.monotonic())
        finally:
            os._exit(0)
    return pid


def spin(t0):
    x = 0
    while alive(t0):
        x += 1


def escaped_sleep(t0):
    os.setsid()
    while alive(t0):
        time.sleep(0.1)


if MODE == "ok":
    write_out({})
    print("line 1")
    print("line 2")
    print("line 3")
    sys.exit(0)
if MODE == "rc_nonzero":
    write_out({})
    sys.exit(3)
if MODE == "no_output":
    print("no output written")
    sys.exit(0)
if MODE in ("mutate_pin", "mutate_evidence"):
    with open(TARGET, "ab") as fh:
        fh.write(b"x")
    write_out({"mutated": TARGET})
    sys.exit(0)
if MODE == "flood":
    line = "x" * 65535 + "\n"
    while alive():
        sys.stdout.write(line)
        sys.stdout.flush()
    sys.exit(0)
if MODE == "sleep":
    while alive():
        time.sleep(0.1)
    write_out({})
    sys.exit(0)
if MODE == "ignore_term":
    seen = []
    signal.signal(signal.SIGTERM, lambda s, f: seen.append(time.monotonic() - T0))
    while alive():
        time.sleep(0.1)
    write_out({"sigterm_seen_at": seen})
    sys.exit(0)
if MODE in ("escape_slow", "escape_fast"):
    g = fork_bounded(escaped_sleep)
    if MODE == "escape_slow":
        time.sleep(3.0)
    write_out({"grandchild": g})
    sys.exit(0)
if MODE == "busy3":
    kids = [fork_bounded(spin), fork_bounded(spin)]
    spin(T0)
    for k in kids:
        os.waitpid(k, 0)
    sys.exit(0)
if MODE == "rss":
    block = bytearray(320 * 1024 * 1024)
    for i in range(0, len(block), 4096):
        block[i] = 1
    while alive():
        time.sleep(0.1)
    sys.exit(0)
sys.exit(2)
