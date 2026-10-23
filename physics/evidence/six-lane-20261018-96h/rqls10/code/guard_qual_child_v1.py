#!/usr/bin/env python3
"""guard_qual_child_v1: deliberately misbehaving / well-behaved test children for the guard qualification of
code/owned_supervisor_v4.py (plan evidence/owned_supervisor_v4-guard-qualification-plan-v1.md). Standard library only,
no science. EVERY mode ends by itself within its own bounded lifetime even if it is never signalled (no permanent
process can be left behind); every spawned grandchild has the same bound.
Protocol: reads one line from stdin and requires "GO" (else exit 6 at once). Usage: guard_qual_child_v1.py MODE OUT LIFE_S
  ok           write OUT (one JSON line), print 3 short lines, exit 0.
  flood        print 64 KiB lines to stdout until SIGTERM (default action) or LIFE_S elapses.
  ignore_term  ignore SIGTERM (handler records it), sleep in 0.1 s steps until LIFE_S, write OUT, exit 0.
  escape       spawn a grandchild that calls setsid() (leaves the child's process group) and sleeps LIFE_S, then exit 0.
  busy3        spawn two CPU-bound grandchildren in the same group (each stops after LIFE_S or on SIGTERM) and spin
               itself until SIGTERM or LIFE_S.
  rss          allocate and touch 320 MiB, then sleep until SIGTERM or LIFE_S.
  sleep        sleep in 0.1 s steps until SIGTERM (default action) or LIFE_S, write OUT, exit 0.
"""
import json, os, signal, sys, time

if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
MODE, OUT, LIFE = sys.argv[1], sys.argv[2], float(sys.argv[3])
T0 = time.monotonic()


def alive():
    return time.monotonic() - T0 < LIFE


def write_out(extra):
    with open(OUT, "x") as fh:
        fh.write(json.dumps(dict({"mode": MODE, "pid": os.getpid(), "elapsed_s": time.monotonic() - T0}, **extra)) + "\n")


def spin_child():
    pid = os.fork()
    if pid == 0:
        try:
            t = time.monotonic()
            x = 0
            while time.monotonic() - t < LIFE:
                x += 1
        finally:
            os._exit(0)
    return pid


if MODE == "ok":
    write_out({})
    print("line 1")
    print("line 2")
    print("line 3")
    sys.exit(0)
if MODE == "flood":
    line = "x" * 65535 + "\n"
    while alive():
        sys.stdout.write(line)
        sys.stdout.flush()
    sys.exit(0)
if MODE == "ignore_term":
    seen = []
    signal.signal(signal.SIGTERM, lambda s, f: seen.append(time.monotonic() - T0))
    while alive():
        time.sleep(0.1)
    write_out({"sigterm_seen_at": seen})
    sys.exit(0)
if MODE == "escape":
    pid = os.fork()
    if pid == 0:
        try:
            os.setsid()
            t = time.monotonic()
            while time.monotonic() - t < LIFE:
                time.sleep(0.1)
        finally:
            os._exit(0)
    write_out({"grandchild": pid})
    sys.exit(0)
if MODE == "busy3":
    kids = [spin_child(), spin_child()]
    x = 0
    while alive():
        x += 1
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
if MODE == "sleep":
    while alive():
        time.sleep(0.1)
    write_out({})
    sys.exit(0)
sys.exit(2)
