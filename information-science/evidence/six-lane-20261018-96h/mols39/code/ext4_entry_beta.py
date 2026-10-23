#!/usr/bin/env python3
"""Source-only beta-route successor3 entrypoint: bounded GO, owned real output root, full anchored
parent-walk + regular/nlink1/cap checks for source/input preflight, exact source-byte digest injection.
No raw bytes read in preflight; the algorithm itself consumes once through its anchored reader.
Before algorithm main begins, entry errors92/93/95/96 may emit ONE diagnostic JSON line.
After main begins ANY escaping exception or invalid return status fails QUIETLY with94; algorithm
stdout may already be partially/finally emitted and no second wrapper line may be appended.
No execution authorized; GLOBAL HOLD, separate qualified supervisor and exact parent GO required.
"""
import os
import sys
import time
import select

_T0 = time.monotonic()
GO_WAIT_S = 120.0


def _no_go():
    os._exit(97)


def _await_go():
    buf = b""
    while len(buf) < 3:
        remaining = GO_WAIT_S - (time.monotonic() - _T0)
        if remaining <= 0:
            _no_go()
        try:
            ready, _, _ = select.select([0], [], [], remaining)
        except (OSError, ValueError):
            _no_go()
        if not ready:
            _no_go()
        try:
            chunk = os.read(0, 3 - len(buf))
        except OSError:
            _no_go()
        if not chunk:
            _no_go()
        buf += chunk
        if time.monotonic() - _T0 >= GO_WAIT_S:
            _no_go()
    if buf != b"GO\n":
        _no_go()
    try:
        ready, _, _ = select.select([0], [], [], 0)
        if ready and os.read(0, 1):
            _no_go()
    except (OSError, ValueError):
        _no_go()
    # Fresh clock after the final read/probe, immediately before successful admission.
    if time.monotonic() - _T0 >= GO_WAIT_S:
        _no_go()


_await_go()

import hashlib
import json
import stat
import types

ROLE = "beta"
ALGO_PATH = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_beta.py"
ALGO_SHA256 = "a319a4be1cc219a2de4c53211ac61cabc42bdc19d000f8bc740c6e4bc262b978"
MODULE_NAME = "ext4_beta"
ALGO_CAP = 1 << 20
INPUT_CAPS = {'--raw': 1048576}
OUTPUT_VALUES = {}


def _emit(status, reason, code):
    try:
        print(json.dumps({"status": status, "reason": reason}, sort_keys=True), flush=True)
    except Exception:
        pass
    sys.exit(code)


def _enter_job_root(path):
    if not path.startswith("/") or "\x00" in path:
        _emit("ENTRY_JOB_ROOT_REJECTED", "job root is not an absolute path", 93)
    parts = path.split("/")[1:]
    if any(p in ("", ".", "..") for p in parts):
        _emit("ENTRY_JOB_ROOT_REJECTED", "job root is not normalised", 93)
    try:
        fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    except OSError:
        _emit("ENTRY_JOB_ROOT_REJECTED", "cannot open /", 93)
    try:
        for p in parts:
            nfd = os.open(p, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nfd
        st = os.fstat(fd)
        if not stat.S_ISDIR(st.st_mode) or st.st_uid != os.getuid() or (st.st_mode & 0o022):
            raise OSError("job root ownership or mode")
        os.fchdir(fd)
    except OSError as exc:
        _emit("ENTRY_JOB_ROOT_REJECTED", "job root rejected: " + type(exc).__name__, 93)
    return fd


def anchored_parent(path):
    """Open every absolute parent component without following symlinks; return retained parent fd + name."""
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("absolute normalized file path required")
    components = path.split("/")[1:]
    if not components or any(c in ("", ".", "..") for c in components):
        raise OSError("non-normalized file path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in components[:-1]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd, components[-1]
    except BaseException:
        os.close(fd)
        raise


def anchored_file_fd(path, cap):
    """No raw-byte preflight read: anchor parents, open NONBLOCK, verify actual regular one-link descriptor."""
    parent, name = anchored_parent(path)
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > cap:
            raise OSError("input kind/link/cap")
        return fd
    except BaseException:
        os.close(fd)
        raise


def anchored_read_bytes(path, cap, check=None):
    if check is not None:
        check()
    fd = anchored_file_fd(path, cap)
    try:
        blocks, total = [], 0
        while True:
            if check is not None:
                check()
            block = os.read(fd, min(65536, cap + 1 - total))
            if check is not None:
                check()
            if not block:
                break
            total += len(block)
            if total > cap:
                raise OSError("input grew beyond cap")
            blocks.append(block)
        if os.fstat(fd).st_nlink != 1:
            raise OSError("input link count changed")
        return b"".join(blocks)
    finally:
        os.close(fd)


def _check_args(args):
    seen_outputs = {}
    i = 0
    while i < len(args):
        arg = args[i]
        flag, sep, value = arg.partition("=")
        if not arg.startswith("--") or (flag not in INPUT_CAPS and flag not in OUTPUT_VALUES):
            i += 1
            continue
        if not sep:
            if i + 1 >= len(args):
                _emit("ENTRY_ARGUMENT_REJECTED", "missing value for " + flag, 92)
            value = args[i + 1]
            i += 2
        else:
            i += 1
        if flag in OUTPUT_VALUES:
            if value != OUTPUT_VALUES[flag] or flag in seen_outputs:
                _emit("ENTRY_ARGUMENT_REJECTED", "output flag value must be " + OUTPUT_VALUES[flag], 92)
            seen_outputs[flag] = value
            continue
        if not value.startswith("/"):
            _emit("ENTRY_ARGUMENT_REJECTED", flag + " must be an absolute path", 92)
        try:
            # Metadata-only preflight: NO second raw-byte read. Algorithm consumes through its own anchored reader.
            input_fd = anchored_file_fd(value, INPUT_CAPS[flag])
            os.close(input_fd)
        except OSError:
            _emit("ENTRY_ARGUMENT_REJECTED", flag + " parent/link/type/cap rejected", 92)
    for flag in OUTPUT_VALUES:
        if flag not in seen_outputs:
            _emit("ENTRY_ARGUMENT_REJECTED", "missing " + flag, 92)


def _load():
    try:
        src = anchored_read_bytes(ALGO_PATH, ALGO_CAP)
    except Exception as exc:
        _emit("ENTRY_ALGORITHM_LOAD_ERROR", "cannot read algorithm: " + type(exc).__name__, 95)
    if len(src) > ALGO_CAP:
        _emit("ENTRY_ALGORITHM_LOAD_ERROR", "algorithm exceeds its cap", 95)
    observed_source_sha256 = hashlib.sha256(src).hexdigest()
    if observed_source_sha256 != ALGO_SHA256:
        _emit("ENTRY_ALGORITHM_PIN_MISMATCH", "algorithm sha256 differs from the pin", 96)
    try:
        code = compile(src, ALGO_PATH, "exec")
        mod = types.ModuleType(MODULE_NAME)
        mod.__file__ = ALGO_PATH
        # Trusted source digest from the exact already-read bytes. Algorithms do not reopen __file__.
        mod.VERIFIED_SOURCE_SHA256 = observed_source_sha256
        sys.modules[MODULE_NAME] = mod
        exec(code, mod.__dict__)
    except Exception as exc:
        _emit("ENTRY_ALGORITHM_LOAD_ERROR", "cannot load algorithm: " + type(exc).__name__, 95)
    return mod


def _main():
    argv = sys.argv[1:]
    if len(argv) < 2 or argv[0] != "--job-root":
        _emit("ENTRY_ARGUMENT_REJECTED", "argv must start with --job-root ABS", 92)
    _root_fd = _enter_job_root(argv[1])
    args = argv[2:]
    _check_args(args)
    mod = _load()
    try:
        status = mod.main(args)
    except BaseException:
        # Algorithm may already have emitted its single line. Preserve bytes; never append wrapper JSON.
        os._exit(94)
    if type(status) is not int or not 0 <= status <= 255:
        os._exit(94)
    sys.exit(status)


_main()
