#!/usr/bin/env python3
"""Single-process qualification child for supervisor v10 (parent narrowed scope e441d858...af22b).
No fork, exec, subprocess or multiprocessing call. Supersedes frozen/unrun child v6. Busy control is one spinning
process with the supervisor's TEST threshold zero; global lane busy cap remains 2. Fork/zombie/escape modes from the
old generic package are removed, not silently qualified by this single-process contract.
Usage: guard_qual_child_v7.py SCENARIO LIFE_S. All destinations are fixed beneath QROOT/SCENARIO, never argv-selected.
GO waiting and flood writes are nonblocking and checked against a monotonic deadline from module entry (not a claim
about interpreter startup). The parent also retains its independent supervisor/spawn deadline. Normal descendants do
not exist. ignore/identity can outlive the supervisor; parent must verify this PID ended and audit its late output.
Mutations use exact new scenario fixtures through retained no-follow directory descriptors; no create on append,
regular file, link count one. The pin fixture's bytes are verified. No prior-run file is modified.
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
QROOT = LANE + "/qual-pkg-v5-v10"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
SCENARIOS = {"go_unlisted", "ok", "rc_nonzero", "missing_output", "mutate_pin", "mutate_evidence", "stray_file",
             "deadline", "flood", "busy", "rss", "ignore", "identity"}


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
        if name in ("ok", "go_unlisted", "rc_nonzero"):
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
