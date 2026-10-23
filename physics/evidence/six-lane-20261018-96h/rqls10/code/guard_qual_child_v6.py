#!/usr/bin/env python3
"""guard_qual_child_v6: preregistered test children for the guard qualification package v5 of code/owned_supervisor_v9.py
(plan evidence/owned_supervisor_v9-guard-qualification-plan-v5.md). Supersedes guard_qual_child_v5.py (never run) after
the Codex review of package v4 (RUN/review/rqls10-guard-qualification-v4-codex-v1.prompt.stdout.txt, findings 3-5).
Standard library only, no science.
Lifetime: every process started here ends by itself by DEADLINE = (this child's start, taken BEFORE waiting for GO)
+ LIFE_S, measured on the shared monotonic clock: the GO wait is bounded (select), loops check DEADLINE, flood writes
are non-blocking, the double-fork grandchild execs /bin/sleep for the REMAINING time only. Descendant bodies exit 0 only
on success and 1 with a traceback on stderr otherwise (no masking). Intended descendants report their identities
(pid) through the child's stdout line "IDS {...}" or OUT, without extra workload processes.
Protocol: one line "GO" on stdin within LIFE_S (else exit 6). Usage: guard_qual_child_v6.py MODE OUT LIFE_S [TARGET]
  ok                 write OUT, print exactly "line 1", "line 2", "line 3", exit 0.
  rc_nonzero         write OUT, exit 3.
  no_output          print one line, exit 0 WITHOUT writing OUT (OUT is a required output in its config).
  mutate_pin         TARGET must be exactly <run>/pinned-scratch.txt (<run> = parent of OUT's directory): open without
                     create and without following symlinks, require a regular file with one link and exactly the
                     fixture bytes, append one byte b"x", write OUT, exit 0 (exit 2 without writing if any check fails).
  mutate_evidence    TARGET must be exactly <out>/launch.json (OUT's directory): open without create and without
                     following symlinks, require a regular non-empty file with one link, append one byte b"x", write
                     OUT, exit 0 (exit 2 without writing if any check fails).
  stray_file         write OUT, then create <out>/stray.txt exclusively (no symlink following), exit 0.
  flood              write 64 KiB lines to stdout (non-blocking) until SIGTERM (default action) or DEADLINE.
  sleep              sleep in 0.1 s steps until SIGTERM (default action) or DEADLINE, then write OUT, exit 0.
  ignore_term        ignore SIGTERM (records the arrival times), sleep until DEADLINE, write OUT, exit 0.
  escape_slow        fork a grandchild that calls setsid() and sleeps until DEADLINE; the child waits 3 s, writes OUT
                     {"grandchild": pid}, exits 0.
  escape_fast        as escape_slow but the child writes OUT and exits immediately after the fork.
  double_fork_escape fork an intermediate that calls setsid(), forks a grandchild, reports the grandchild's pid through
                     a pipe and exits at once (the child reaps it); the grandchild changes cwd to /, points fds 0-2 at
                     /dev/null, closes fds 3-255 and execs /bin/sleep for the remaining time; the child writes OUT
                     {"intermediate": pid, "grandchild": pid} and exits 0.
  zombie_hold        fork a holder in the child's group; the holder forks a process that exits at once and is NOT
                     reaped for 3 s (a zombie), reports its pid through a pipe, then exits (launchd reaps the zombie);
                     the child writes OUT {"holder": pid, "zombie": pid} after reaping the holder, exits 0.
  busy2              fork ONE CPU-bound grandchild in the same process group, print "IDS {"busy_pids": [child,
                     grandchild]}" and spin itself (two CPU-bound processes in total); both stop at DEADLINE or on
                     SIGTERM (default action).
  rss                allocate and touch 320 MiB, print "IDS {"rss_pid": pid}", sleep until SIGTERM (default action) or
                     DEADLINE.
"""
import json, os, select, signal, stat, sys, time, traceback

T_START = time.monotonic()
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
try:
    MODE, OUT, LIFE = sys.argv[1], sys.argv[2], float(sys.argv[3])
    TARGET = sys.argv[4] if len(sys.argv) > 4 else None
except (IndexError, ValueError):
    sys.exit(2)
DEADLINE = T_START + LIFE
ready, _, _ = select.select([sys.stdin], [], [], max(0.0, DEADLINE - time.monotonic()))
if not ready or sys.stdin.readline().strip() != "GO":
    sys.exit(6)
OUT_DIR = os.path.dirname(os.path.abspath(OUT))
RUN_DIR = os.path.dirname(OUT_DIR)


def alive():
    return time.monotonic() < DEADLINE


def remaining():
    return max(0.0, DEADLINE - time.monotonic())


def write_out(extra):
    fd = os.open(OUT, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        data = (json.dumps(dict({"mode": MODE, "pid": os.getpid(), "elapsed_s": time.monotonic() - T_START}, **extra))
                + "\n").encode("utf-8")
        view = memoryview(data)
        while view:
            k = os.write(fd, view)
            if k <= 0:
                raise OSError("zero-progress write")
            view = view[k:]
    finally:
        os.close(fd)


def say_ids(obj):
    sys.stdout.write("IDS " + json.dumps(obj, sort_keys=True) + "\n")
    sys.stdout.flush()


def fork_bounded(body):
    pid = os.fork()
    if pid == 0:
        code = 0
        try:
            body()
        except BaseException:
            code = 1
            try:
                sys.stderr.write(traceback.format_exc()[-2000:])
                sys.stderr.flush()
            except BaseException:
                pass
        os._exit(code)
    return pid


def spin():
    x = 0
    while alive():
        x += 1


def escaped_sleep():
    os.setsid()
    while alive():
        time.sleep(0.1)


def append_exact(path, want_bytes):
    """append b"x" to an existing regular file with one link, opened without create or symlink following."""
    fd = os.open(path, os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW)
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1 or st.st_size == 0:
            raise OSError("target is not a regular non-empty file with one link")
        if want_bytes is not None and (st.st_size != len(want_bytes) or os.pread(fd, st.st_size, 0) != want_bytes):
            raise OSError("target content is not the expected fixture")
        if os.write(fd, b"x") != 1:
            raise OSError("append failed")
        return st.st_size
    finally:
        os.close(fd)


def main():
    if MODE == "ok":
        write_out({})
        sys.stdout.write("line 1\nline 2\nline 3\n")
        sys.stdout.flush()
        return 0
    if MODE == "rc_nonzero":
        write_out({})
        return 3
    if MODE == "no_output":
        sys.stdout.write("no output written\n")
        sys.stdout.flush()
        return 0
    if MODE in ("mutate_pin", "mutate_evidence"):
        want_path = os.path.join(RUN_DIR, "pinned-scratch.txt") if MODE == "mutate_pin" else \
            os.path.join(OUT_DIR, "launch.json")
        if TARGET != want_path:
            return 2
        try:
            size = append_exact(TARGET, FIXTURE if MODE == "mutate_pin" else None)
        except OSError as ex:
            sys.stderr.write("MUTATION_REFUSED %r\n" % ex)
            return 2
        write_out({"mutated": TARGET, "size_before": size})
        return 0
    if MODE == "stray_file":
        write_out({})
        fd = os.open(os.path.join(OUT_DIR, "stray.txt"), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
        try:
            os.write(fd, b"undeclared file\n")
        finally:
            os.close(fd)
        return 0
    if MODE == "flood":
        os.set_blocking(1, False)
        line = b"x" * 65535 + b"\n"
        view = memoryview(line)
        while alive():
            try:
                k = os.write(1, view)
                view = view[k:] if k < len(view) else memoryview(line)
            except BlockingIOError:
                time.sleep(0.01)
        return 0
    if MODE == "sleep":
        while alive():
            time.sleep(0.1)
        write_out({})
        return 0
    if MODE == "ignore_term":
        seen = []
        signal.signal(signal.SIGTERM, lambda s, f: seen.append(time.monotonic() - T_START))
        while alive():
            time.sleep(0.1)
        write_out({"sigterm_seen_at": seen})
        return 0
    if MODE in ("escape_slow", "escape_fast"):
        g = fork_bounded(escaped_sleep)
        if MODE == "escape_slow":
            time.sleep(min(3.0, remaining()))
        write_out({"grandchild": g})
        return 0
    if MODE == "double_fork_escape":
        r, w = os.pipe()

        def intermediate():
            os.close(r)
            os.setsid()
            g = os.fork()
            if g == 0:
                try:
                    os.chdir("/")
                    fd = os.open("/dev/null", os.O_RDWR)
                    for k in (0, 1, 2):
                        os.dup2(fd, k)
                    os.closerange(3, 256)
                    os.execv("/bin/sleep", ["sleep", "%.3f" % remaining()])
                finally:
                    os._exit(1)
            os.write(w, b"%d\n" % g)
        i = fork_bounded(intermediate)
        os.close(w)
        ready_, _, _ = select.select([r], [], [], remaining())
        gpid = int(os.read(r, 32).decode().strip()) if ready_ else None
        os.close(r)
        _, status = os.waitpid(i, 0)
        write_out({"intermediate": i, "intermediate_status": status, "grandchild": gpid})
        return 0 if gpid is not None and status == 0 else 1
    if MODE == "zombie_hold":
        r, w = os.pipe()

        def holder():
            os.close(r)
            z = os.fork()
            if z == 0:
                os._exit(0)
            os.write(w, b"%d\n" % z)
            time.sleep(min(3.0, remaining()))
        h = fork_bounded(holder)
        os.close(w)
        ready_, _, _ = select.select([r], [], [], remaining())
        zpid = int(os.read(r, 32).decode().strip()) if ready_ else None
        os.close(r)
        _, status = os.waitpid(h, 0)
        write_out({"holder": h, "holder_status": status, "zombie": zpid})
        return 0 if zpid is not None and status == 0 else 1
    if MODE == "busy2":
        kid = fork_bounded(spin)
        say_ids({"busy_pids": [os.getpid(), kid]})
        spin()
        os.waitpid(kid, 0)
        return 0
    if MODE == "rss":
        block = bytearray(320 * 1024 * 1024)
        for i in range(0, len(block), 4096):
            block[i] = 1
        say_ids({"rss_pid": os.getpid()})
        while alive():
            time.sleep(0.1)
        return 0
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException:
        sys.stderr.write(traceback.format_exc()[-2000:])
        sys.exit(2)
