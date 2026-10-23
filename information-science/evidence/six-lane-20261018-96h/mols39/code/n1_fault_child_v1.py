#!/usr/bin/env python3
"""MOLS39 N1 fault-case CHILD v1 (ContinueCFR21c). WRITTEN ONLY. Run ONLY as the single child of
n1_fault_driver_v1.py under an exact parent GO for one case; never import it.

INSTRUMENTED RawIO fault (labelled as such). The child installs sys.stdout = a REAL io.TextIOWrapper over a
REAL io.BufferedWriter(buffer_size=8192) whose raw layer is FaultRaw. FaultRaw.write follows the RawIOBase
contract over the real fd 1 (the driver's capture pipe). Planned calls either pass bytes through, write a
strict prefix and return its length, return None (the RawIOBase/FileIO would-block result of a full
non-blocking pipe, so CPython's BufferedWriter itself raises BlockingIOError and keeps every unwritten byte
pending), or raise KeyboardInterrupt after a complete pass-through write. Every call after the planned fault
passes through, so any later flush retry (interpreter shutdown or finalizer) would succeed and be captured.
An optional real time.sleep is part of the plan. No clock, /bin/date, exit code or return value is faked.

The child then executes the ACTUAL pinned entrypoint bytes (sha256-checked here; the entrypoint itself
sha256-checks the actual pinned algorithm) as __main__. No entrypoint or algorithm logic is copied.
Child-only exit codes: 82 argv, 83 case dir/trace create, 84 entry read, 85 entry digest, 86 compile, 87 entrypoint
returned, 88 trace write failure (exits at once). 82..86 occur before the entrypoint starts.
"""
import builtins
import hashlib
import io
import json
import math
import os
import stat
import sys
import time

FORMAT = "mols39-n1-fault-child-v1"
BUFFER_SIZE = 8192
ENTRY_CAP = 1 << 20
TRACE_NAME = "fault-trace.jsonl"
FAULTS = ("none", "wouldblock", "interrupt")


def _die(code):
    os._exit(code)


def _anchored_dir(path):
    """Walk an absolute normalized directory path from '/' without following symlinks; return its fd."""
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("absolute normalized directory path required")
    parts = path.split("/")[1:]
    if not parts or any(p in ("", ".", "..") for p in parts):
        raise OSError("non-normalized directory path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def _anchored_read(path, cap):
    """Anchored parent walk, NONBLOCK|NOFOLLOW leaf, regular one-link size<=cap, cap+1 consumption."""
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("absolute normalized file path required")
    parent_path, sep, name = path.rpartition("/")
    if not sep or name in ("", ".", ".."):
        raise OSError("non-normalized file path")
    parent = _anchored_dir(parent_path) if parent_path else os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > cap:
            raise OSError("file kind/link/cap")
        blocks, total = [], 0
        while True:
            block = os.read(fd, min(65536, cap + 1 - total))
            if not block:
                break
            total += len(block)
            if total > cap:
                raise OSError("file grew beyond cap")
            blocks.append(block)
        if os.fstat(fd).st_nlink != 1:
            raise OSError("file link count changed")
        return b"".join(blocks)
    finally:
        os.close(fd)


class FaultRaw(io.RawIOBase):
    """INSTRUMENTED raw layer over the real fd 1. Plan: optional strict prefix, then one planned action."""

    def __init__(self, trace_fd, prefix_bytes, fault, sleep_s):
        super().__init__()
        self._trace_fd = trace_fd
        self._prefix = prefix_bytes
        self._fault = fault
        self._sleep = sleep_s
        self._calls = 0
        self._done = False

    def writable(self):
        return True

    def trace(self, record):
        # A trace failure is a harness failure, never the planned stdout fault: exit 88 at once.
        try:
            line = (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
            view = memoryview(line)
            while view:
                count = os.write(self._trace_fd, view)
                if count <= 0:
                    raise OSError("trace zero write")
                view = view[count:]
        except (OSError, ValueError, TypeError):
            os._exit(88)

    def _pass(self, data):
        view = memoryview(data)
        written = 0
        while view:
            count = os.write(1, view)
            if count <= 0:
                raise OSError("stdout zero write")
            written += count
            view = view[count:]
        return written

    def write(self, b):
        data = bytes(b)
        self._calls += 1
        call = self._calls
        record = {"call": call, "requested": len(data), "t_monotonic_enter": time.monotonic()}
        if self._done:
            record["action"] = "pass_after_plan"
            record["written"] = self._pass(data)
            self.trace(record)
            return record["written"]
        if self._prefix > 0 and call == 1:
            k = min(self._prefix, len(data) - 1)
            if k < 1:
                self._done = True
                record["action"] = "prefix_impossible_pass"
                record["written"] = self._pass(data)
                self.trace(record)
                return record["written"]
            count = os.write(1, data[:k])
            record["action"] = "strict_prefix"
            record["written"] = count
            self.trace(record)
            return count
        self._done = True
        if self._fault == "wouldblock":
            if self._sleep > 0:
                record["sleep_requested_s"] = self._sleep
                time.sleep(self._sleep)
            record["t_monotonic_before_return"] = time.monotonic()
            record["action"] = "return_None_wouldblock"
            record["written"] = 0
            self.trace(record)
            return None
        record["written"] = self._pass(data)
        if self._sleep > 0:
            record["sleep_requested_s"] = self._sleep
            time.sleep(self._sleep)
        record["t_monotonic_before_return"] = time.monotonic()
        if self._fault == "interrupt":
            record["action"] = "pass_then_raise_KeyboardInterrupt"
            self.trace(record)
            raise KeyboardInterrupt("instrumented fault after complete pass-through write")
        record["action"] = "pass_planned"
        self.trace(record)
        return record["written"]


def main():
    argv = sys.argv[1:]
    if (len(argv) < 13 or argv[0] != "--case-dir" or argv[2] != "--entry" or argv[4] != "--entry-sha256"
            or argv[6] != "--prefix-bytes" or argv[8] != "--fault" or argv[10] != "--sleep-s" or argv[12] != "--"):
        _die(82)
    case_dir, entry, entry_sha = argv[1], argv[3], argv[5]
    prefix_s, fault, sleep_text = argv[7], argv[9], argv[11]
    entry_args = argv[13:]
    if not prefix_s.isascii() or not prefix_s.isdigit() or len(prefix_s) > 4 or fault not in FAULTS:
        _die(82)
    prefix = int(prefix_s)
    try:
        sleep_s = float(sleep_text)
    except ValueError:
        _die(82)
    if not math.isfinite(sleep_s) or not 0.0 <= sleep_s <= 30.0 or prefix > 4096:
        _die(82)
    if len(entry_sha) != 64 or any(c not in "0123456789abcdef" for c in entry_sha):
        _die(82)
    try:
        dfd = _anchored_dir(case_dir)
        try:
            trace_fd = os.open(TRACE_NAME, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=dfd)
        finally:
            os.close(dfd)
    except OSError:
        _die(83)
    try:
        src = _anchored_read(entry, ENTRY_CAP)
    except OSError:
        _die(84)
    observed = hashlib.sha256(src).hexdigest()
    if observed != entry_sha:
        _die(85)
    raw = FaultRaw(trace_fd, prefix, fault, sleep_s)
    stream = io.TextIOWrapper(io.BufferedWriter(raw, buffer_size=BUFFER_SIZE), encoding="utf-8",
                              errors="strict", newline="\n", line_buffering=False, write_through=False)
    raw.trace({"format": FORMAT, "record": "start", "pid": os.getpid(), "ppid": os.getppid(),
               "pgid": os.getpgid(0), "sid": os.getsid(0), "uid": os.getuid(), "euid": os.geteuid(),
               "entry": entry, "entry_sha256": observed, "buffer_size": BUFFER_SIZE,
               "prefix_bytes": prefix, "fault": fault, "sleep_s": sleep_s,
               "python": sys.version, "t_monotonic": time.monotonic(),
               "label": "INSTRUMENTED RawIO fault under real io.BufferedWriter/io.TextIOWrapper"})
    try:
        code = compile(src, entry, "exec")
    except Exception:
        _die(86)
    sys.stdout = stream
    sys.argv = [entry] + entry_args
    namespace = {"__name__": "__main__", "__file__": entry, "__builtins__": builtins,
                 "__package__": None, "__spec__": None, "__doc__": None}
    exec(code, namespace)
    _die(87)


if __name__ == "__main__":
    main()
