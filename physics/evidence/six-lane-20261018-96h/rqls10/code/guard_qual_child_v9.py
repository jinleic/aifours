#!/usr/bin/env python3
"""V12 qualification child. Normal modes stay single-process; explicit ownership-negative modes below are NOT science.
Parent correction fabe57ab...4155a2 requires owned/unproved process controls under their OWN individual GOs.
Only busy2 spins two processes (parent + one child), reserving TWO CPU slots at test threshold1; no busy3.
Ownership group/slow/fast/double-fork/zombie workloads report intended PIDs and use a shared absolute monotonic
lifetime from module entry. Descendant exceptions exit1, never masked as success. GO and flood are nonblocking.
Fixed QROOT/SCENARIO output and exact no-create/no-follow/single-link fixture mutations; no prior run changed.
The parent independently proves each reported/owned/unproved identity ended and audits late artifacts before release.
Injected helper tests should never deliver GO to this child; if they do, its output makes the acceptance fail.
Usage: guard_qual_child_v9.py SCENARIO LIFE_S. No execution is authorized by this source.
"""
import time
START_MONO, START_EPOCH = time.monotonic(), time.time()
import json
import math
import os
import select
import signal
import stat
import sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v7-v12"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
SCENARIOS = {"go_unlisted", "ok", "rc_nonzero", "missing_output", "mutate_pin", "mutate_evidence", "stray_file",
             "deadline", "flood", "busy", "busy2", "rss", "ignore", "identity", "date_fault",
             "helper_overrun", "helper_group", "helper_eof", "ownership_group", "ownership_slow",
             "ownership_fast", "ownership_double", "zombie_hold"}


def directory(path):
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for c in path.lstrip("/").split("/"):
            if c in ("", ".", ".."):
                raise ValueError("invalid directory component")
            nxt = os.open(c, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def complete_write(fd, data):
    view = memoryview(data)
    while view:
        n = os.write(fd, view)
        if n <= 0:
            raise OSError("zero-progress write")
        view = view[n:]


def wait_go(deadline):
    fd, old = 0, os.get_blocking(0)
    data = b""
    try:
        os.set_blocking(fd, False)
        while time.monotonic() < deadline and len(data) <= 16:
            ready, _, _ = select.select([fd], [], [], max(0, deadline - time.monotonic()))
            if not ready:
                return False
            try:
                b = os.read(fd, 17 - len(data))
            except BlockingIOError:
                continue
            if not b:
                return False
            data += b
            if b"\n" in data:
                return data == b"GO\n"
        return False
    finally:
        os.set_blocking(fd, old)


def create_json(outfd, name, obj):
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=outfd)
    try:
        complete_write(fd, (json.dumps(obj, sort_keys=True, allow_nan=False) + "\n").encode())
        os.fsync(fd)
    finally:
        os.close(fd)


def append_fixture(fdroot, name, fixture=None):
    fd = os.open(name, os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fdroot)
    try:
        st = os.fstat(fd)
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1 or not 0 < st.st_size <= 1 << 20:
            raise ValueError("mutation target is not a bounded single-link regular fixture")
        if fixture is not None and (st.st_size != len(fixture) or os.pread(fd, len(fixture), 0) != fixture):
            raise ValueError("wrong pin fixture")
        complete_write(fd, b"x")
        os.fsync(fd)
        return {"target_inode": [st.st_dev, st.st_ino], "size_before": st.st_size}
    finally:
        os.close(fd)


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in SCENARIOS:
        return 2
    name, life = sys.argv[1], float(sys.argv[2])
    if not math.isfinite(life) or not 1 <= life <= 120:
        return 2
    deadline = START_MONO + life
    if not wait_go(deadline):
        return 6
    run = QROOT + "/" + name
    rfd, ofd = directory(run), None
    try:
        ofd = os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=rfd)
        def result(extra=None):
            obj = {"scenario": name, "pid": os.getpid(), "pgid": os.getpgrp(), "ppid": os.getppid(),
                   "mono_module_entry": START_MONO, "epoch_module_entry": START_EPOCH,
                   "mono_output": time.monotonic(), "mono_life_deadline": deadline}
            if extra:
                obj.update(extra)
            create_json(ofd, "child-out.json", obj)
        if name in ("ok", "go_unlisted", "rc_nonzero", "date_fault", "helper_overrun", "helper_group", "helper_eof"):
            result()
            if name == "ok":
                complete_write(1, b"line 1\nline 2\nline 3\n")
            return 3 if name == "rc_nonzero" else 0
        if name == "missing_output":
            complete_write(1, b"no output written\n")
            return 0
        if name == "mutate_pin":
            info = append_fixture(rfd, "pinned-scratch.txt", FIXTURE)
            result(info)
            return 0
        if name == "mutate_evidence":
            info = append_fixture(ofd, "launch.json")
            result(info)
            return 0
        if name == "stray_file":
            result()
            fd = os.open("stray.txt", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=ofd)
            try:
                complete_write(fd, b"undeclared file\n")
                os.fsync(fd)
            finally:
                os.close(fd)
            return 0
        if name == "flood":
            os.set_blocking(1, False)
            line = b"x" * 65535 + b"\n"
            view = memoryview(line)
            while time.monotonic() < deadline:
                try:
                    n = os.write(1, view)
                    if n <= 0:
                        raise OSError("zero-progress flood write")
                    view = view[n:] if n < len(view) else memoryview(line)
                except BlockingIOError:
                    time.sleep(0.005)
            return 0
        if name == "busy":
            complete_write(1, ("IDS " + json.dumps({"busy_pid": os.getpid(), "mono_before_work": time.monotonic()}) + "\n").encode())
            x = 0
            while time.monotonic() < deadline:
                x += 1
            return 0
        if name == "rss":
            block = bytearray(320 * 1024 * 1024)
            for i in range(0, len(block), 4096):
                block[i] = 1
            complete_write(1, ("IDS " + json.dumps({"rss_pid": os.getpid(), "allocated": len(block)}) + "\n").encode())
            while time.monotonic() < deadline:
                time.sleep(0.05)
            return 0

        def fork_body(body):
            pid = os.fork()
            if pid == 0:
                try:
                    body()
                except BaseException as e:
                    try:
                        complete_write(2, ("DESCENDANT_ERROR %r\n" % e).encode())
                    except BaseException:
                        pass
                    os._exit(1)
                os._exit(0)
            return pid
        def sleep_to_deadline():
            while time.monotonic() < deadline:
                time.sleep(0.05)
        def spin_to_deadline():
            n = 0
            while time.monotonic() < deadline:
                n += 1
        if name == "busy2":
            kid = fork_body(spin_to_deadline)
            complete_write(1, ("IDS " + json.dumps({"busy_pids": [os.getpid(), kid]}) + "\n").encode())
            spin_to_deadline()
            _, status = os.waitpid(kid, 0)
            return 0 if status == 0 else 1
        if name in ("ownership_group", "ownership_slow", "ownership_fast"):
            def descendant():
                if name != "ownership_group":
                    os.setsid()
                sleep_to_deadline()
            kid = fork_body(descendant)
            if name != "ownership_fast":
                time.sleep(min(3.0, max(0, deadline - time.monotonic())))
            result({"grandchild": kid, "negative_control": True})
            return 0
        if name in ("ownership_double", "zombie_hold"):
            readfd, writefd = os.pipe()
            def intermediate():
                os.close(readfd)
                if name == "ownership_double":
                    os.setsid()
                kid = os.fork()
                if kid == 0:
                    if name == "zombie_hold":
                        os._exit(0)
                    os.close(writefd)
                    os.chdir("/")
                    devnull = os.open("/dev/null", os.O_RDWR)
                    for standard in (0, 1, 2):
                        os.dup2(devnull, standard)
                    os.closerange(3, 65536)
                    os.execv("/bin/sleep", ["sleep", "%.3f" % max(0, deadline - time.monotonic())])
                    os._exit(1)
                complete_write(writefd, (str(kid) + "\n").encode())
                os.close(writefd)
                if name == "zombie_hold":
                    time.sleep(min(3.0, max(0, deadline - time.monotonic())))
                    _, status = os.waitpid(kid, 0)
                    if status:
                        raise ValueError("zombie child status")
            mid = fork_body(intermediate)
            os.close(writefd)
            os.set_blocking(readfd, False)
            raw = b""
            while b"\n" not in raw and time.monotonic() < deadline:
                ready, _, _ = select.select([readfd], [], [], max(0, deadline - time.monotonic()))
                if not ready:
                    break
                try:
                    part = os.read(readfd, 32 - len(raw))
                except BlockingIOError:
                    continue
                if not part:
                    break
                raw += part
                if len(raw) > 31:
                    raise ValueError("PID report exceeds bound")
            os.close(readfd)
            kid = int(raw.strip())
            _, status = os.waitpid(mid, 0)
            result({"intermediate": mid, "grandchild": kid, "intermediate_status": status,
                    "negative_control": True})
            return 0 if status == 0 else 1

        arrivals = []
        if name == "ignore":
            signal.signal(signal.SIGTERM, lambda sig, frame: arrivals.append(time.monotonic()))
        while time.monotonic() < deadline:
            time.sleep(0.05)
        result({"term_arrivals": arrivals})
        return 0
    finally:
        if ofd is not None:
            os.close(ofd)
        os.close(rfd)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        sys.stderr.write("QUAL_CHILD_ERROR %r\n" % e)
        sys.exit(2)
