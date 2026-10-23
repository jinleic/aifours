#!/usr/bin/env python3
"""go_entry_ext_gate_v1.py (ContinueCFR21, mols39 lane; extension-search GO entrypoint v1, written 2026-10-19T07:41:54-0700; NOT executed when frozen;
stdlib only). One of four entrypoints generated from one template. They differ only in the constants block and the
role-specific tables. Normative description: evidence/lemmaU-certificate-format-v2.md section 7 (startup/containment only). Successor of the v1
entrypoints, which were never executed; this answers review ea5f29a7... findings M2, M4 and m1.
Role: gate. Algorithm: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext_search_gate_v1.py (sha256 3afde051c49920d688fd311842c366ef53f05a18d9babd0afed694aeaa7fc67b).
Exit codes owned by this entrypoint: 97 no GO (nothing printed, no file); 96 algorithm pin mismatch; 95 algorithm
load error; 94 uncaught exception (non-checker roles); 93 job root rejected; 92 argument rejected. Codes 92-96 print
exactly one JSON line."""
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
    if buf != b"GO\n":
        _no_go()
    try:
        ready, _, _ = select.select([0], [], [], 0)
        if ready and os.read(0, 1):
            _no_go()
    except (OSError, ValueError):
        _no_go()


_await_go()

import hashlib
import json
import stat
import types

ROLE = "gate"
ALGO_PATH = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext_search_gate_v1.py"
ALGO_SHA256 = "3afde051c49920d688fd311842c366ef53f05a18d9babd0afed694aeaa7fc67b"
MODULE_NAME = "ext_search_gate_v1"
ALGO_CAP = 1 << 20
INPUT_CAPS = {'--plan': 4194304}
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
            st = os.stat(value)
        except OSError:
            _emit("ENTRY_ARGUMENT_REJECTED", flag + " cannot be stat()ed", 92)
        if not stat.S_ISREG(st.st_mode) or st.st_size > INPUT_CAPS[flag]:
            _emit("ENTRY_ARGUMENT_REJECTED", flag + " is not a regular file within its size cap", 92)
    for flag in OUTPUT_VALUES:
        if flag not in seen_outputs:
            _emit("ENTRY_ARGUMENT_REJECTED", "missing " + flag, 92)


def _load():
    try:
        with open(ALGO_PATH, "rb") as fh:
            src = fh.read(ALGO_CAP + 1)
    except Exception as exc:
        _emit("ENTRY_ALGORITHM_LOAD_ERROR", "cannot read algorithm: " + type(exc).__name__, 95)
    if len(src) > ALGO_CAP:
        _emit("ENTRY_ALGORITHM_LOAD_ERROR", "algorithm exceeds its cap", 95)
    if hashlib.sha256(src).hexdigest() != ALGO_SHA256:
        _emit("ENTRY_ALGORITHM_PIN_MISMATCH", "algorithm sha256 differs from the pin", 96)
    try:
        code = compile(src, ALGO_PATH, "exec")
        mod = types.ModuleType(MODULE_NAME)
        mod.__file__ = ALGO_PATH
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
        _emit("ENTRY_UNCAUGHT_EXCEPTION", "exception escaped main", 94)
    if type(status) is not int or not 0 <= status <= 255:
        _emit("ENTRY_UNCAUGHT_EXCEPTION", "main returned a non-integer status", 94)
    sys.exit(status)


_main()
