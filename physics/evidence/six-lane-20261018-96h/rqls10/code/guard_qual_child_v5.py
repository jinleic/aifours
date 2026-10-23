#!/usr/bin/env python3
"""guard_qual_child_v5: preregistered test children for the guard qualification of code/owned_supervisor_v7.py (plan
evidence/owned_supervisor_v7-guard-qualification-plan-v4.md). Supersedes guard_qual_child_v4.py (never run) after the
parent's pre-review: busy3 (three CPU-bound processes, above the unchanged lane limit of 2) is replaced by busy2 (two
CPU-bound processes in total; its config uses busy_limit 1), and mutate_* targets must be test-owned fixtures of THIS
scenario (TARGET must lie in OUT's directory or its parent, the scenario run directory; otherwise exit 2 without
touching anything). Standard library only, no science. EVERY process started here ends by itself within LIFE_S seconds
of its own start even if it is never signalled (no permanent process).
Protocol: reads one line from stdin and requires "GO" (else exit 6). Usage:
  guard_qual_child_v5.py MODE OUT LIFE_S [TARGET]
  ok                 write OUT (one JSON line), print 3 short lines, exit 0.
  rc_nonzero         write OUT, exit 3.
  no_output          print one line, exit 0 WITHOUT writing OUT (OUT is a required output in its config).
  mutate_pin         append the byte b"x" to TARGET (this scenario's pinned scratch fixture), write OUT, exit 0.
  mutate_evidence    append the byte b"x" to TARGET (this scenario's own launch record), write OUT, exit 0.
  stray_file         write OUT and an undeclared file stray.txt next to it (exclusive create), exit 0.
  flood              print 64 KiB lines to stdout until SIGTERM (default action) or LIFE_S.
  sleep              sleep in 0.1 s steps until SIGTERM (default action) or LIFE_S, then write OUT, exit 0.
  ignore_term        ignore SIGTERM (records the arrival times), sleep until LIFE_S, write OUT, exit 0.
  escape_slow        fork a grandchild that calls setsid() and sleeps LIFE_S; the child waits 3 s, writes OUT, exits 0.
  escape_fast        as escape_slow but the child writes OUT and exits immediately after the fork.
  double_fork_escape fork an intermediate that calls setsid(), forks a grandchild and exits at once (the child reaps
                     it); the grandchild changes cwd to /, points fds 0-2 at /dev/null, closes fds 3-255 and execs
                     /bin/sleep LIFE_S (argv without any lane path); the child writes OUT and exits 0.
  zombie_hold        fork a holder in the child's group; the holder forks a process that exits at once and is NOT
                     reaped (a zombie) for 3 s, then the holder exits (launchd reaps the zombie); the child waits for
                     the holder, writes OUT, exits 0.
  busy2              fork ONE CPU-bound grandchild in the same process group and spin itself (two CPU-bound
                     processes in total); both stop at LIFE_S or on SIGTERM (default action).
  rss                allocate and touch 320 MiB, then sleep until SIGTERM (default action) or LIFE_S.
"""
import json, os, signal, sys, time

if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
MODE, OUT, LIFE = sys.argv[1], sys.argv[2], float(sys.argv[3])
TARGET = sys.argv[4] if len(sys.argv) > 4 else None
RUN_OUT = os.path.dirname(os.path.abspath(OUT))
if TARGET is not None and os.path.dirname(os.path.abspath(TARGET)) not in (RUN_OUT, os.path.dirname(RUN_OUT)):
    sys.exit(2)
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


def intermediate(t0):
    os.setsid()
    g = os.fork()
    if g == 0:
        try:
            os.chdir("/")
            fd = os.open("/dev/null", os.O_RDWR)
            for k in (0, 1, 2):
                os.dup2(fd, k)
            os.closerange(3, 256)
            os.execv("/bin/sleep", ["sleep", str(int(LIFE))])
        finally:
            os._exit(0)


def holder(t0):
    z = os.fork()
    if z == 0:
        os._exit(0)
    time.sleep(3.0)


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
if MODE == "stray_file":
    write_out({})
    with open(os.path.join(os.path.dirname(OUT), "stray.txt"), "x") as fh:
        fh.write("undeclared file\n")
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
if MODE == "double_fork_escape":
    i = fork_bounded(intermediate)
    os.waitpid(i, 0)
    write_out({"intermediate": i})
    sys.exit(0)
if MODE == "zombie_hold":
    h = fork_bounded(holder)
    os.waitpid(h, 0)
    write_out({"holder": h})
    sys.exit(0)
if MODE == "busy2":
    kid = fork_bounded(spin)
    spin(T0)
    os.waitpid(kid, 0)
    sys.exit(0)
if MODE == "rss":
    block = bytearray(320 * 1024 * 1024)
    for i in range(0, len(block), 4096):
        block[i] = 1
    while alive():
        time.sleep(0.1)
    sys.exit(0)
sys.exit(2)
