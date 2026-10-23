#!/usr/bin/env python3
"""go_entry_expectations_v1.py (ContinueCFR21, mols39 lane; launch-contract entrypoint, written 2026-10-19T07:10:40-0700; NOT executed when frozen;
stdlib only). One of four entrypoints built from the same template; they differ only in the five @-constants and in
the call block at the end.
Entrypoint for the unchanged algorithm file
  /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/check_cert_runs_v2.py
  (sha256 d7be83ffa375818f45efe6513a77990e36e5af504d6483a167ce679f1d3a5959)
under a supervisor that publishes the launch identity, then writes b"GO\n" to the child's stdin and closes it.
Protocol:
  1. Before anything else (no input read, computation or write), read exactly one line from stdin. Unless it is
     exactly b"GO\n" (EOF, other bytes or a missing newline all fail), exit 97 at once: nothing is printed and no
     file is created.
  2. Only after GO: read the algorithm file and check its sha256 against the pinned value. On mismatch print one JSON
     line {"status": "ALGORITHM_PIN_MISMATCH"} and exit 96. Otherwise compile the hashed bytes and execute them as a
     fresh module named "check_cert_runs_v2", so its own __main__ block does not run. If that fails, print one JSON line
     {"status": "ALGORITHM_LOAD_ERROR"} and exit 95.
  3. Call the module's main(argv) with this process's argv[1:] and exit with its status.
No other behaviour is added; the algorithm itself is not modified."""
import sys

if sys.stdin.buffer.readline() != b"GO\n":
    sys.exit(97)

import hashlib
import types

ALGO_PATH = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/check_cert_runs_v2.py"
ALGO_SHA256 = "d7be83ffa375818f45efe6513a77990e36e5af504d6483a167ce679f1d3a5959"
MODULE_NAME = "check_cert_runs_v2"


def _load():
    with open(ALGO_PATH, "rb") as fh:
        src = fh.read()
    if hashlib.sha256(src).hexdigest() != ALGO_SHA256:
        print('{"status": "ALGORITHM_PIN_MISMATCH"}', flush=True)
        sys.exit(96)
    try:
        code = compile(src, ALGO_PATH, "exec")
        mod = types.ModuleType(MODULE_NAME)
        mod.__file__ = ALGO_PATH
        sys.modules[MODULE_NAME] = mod
        exec(code, mod.__dict__)
    except Exception:
        print('{"status": "ALGORITHM_LOAD_ERROR"}', flush=True)
        sys.exit(95)
    return mod


_mod = _load()
sys.exit(_mod.main(sys.argv[1:]))
