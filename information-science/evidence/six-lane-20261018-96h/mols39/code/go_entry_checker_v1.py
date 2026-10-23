#!/usr/bin/env python3
"""go_entry_checker_v1.py (ContinueCFR21, mols39 lane; launch-contract entrypoint, written 2026-10-19T07:10:40-0700; NOT executed when frozen;
stdlib only). One of four entrypoints built from the same template; they differ only in the five @-constants and in
the call block at the end.
Entrypoint for the unchanged algorithm file
  /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py
  (sha256 e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0)
under a supervisor that publishes the launch identity, then writes b"GO\n" to the child's stdin and closes it.
Protocol:
  1. Before anything else (no input read, computation or write), read exactly one line from stdin. Unless it is
     exactly b"GO\n" (EOF, other bytes or a missing newline all fail), exit 97 at once: nothing is printed and no
     file is created.
  2. Only after GO: read the algorithm file and check its sha256 against the pinned value. On mismatch print one JSON
     line {"status": "ALGORITHM_PIN_MISMATCH"} and exit 96. Otherwise compile the hashed bytes and execute them as a
     fresh module named "cert_checker", so its own __main__ block does not run. If that fails, print one JSON line
     {"status": "ALGORITHM_LOAD_ERROR"} and exit 95.
  3. Call the module's main(argv) with this process's argv[1:] and exit with its status, mapping any exception escaping main to the checker's ERROR exit code exactly as its own __main__ block does.
No other behaviour is added; the algorithm itself is not modified."""
import sys

if sys.stdin.buffer.readline() != b"GO\n":
    sys.exit(97)

import hashlib
import types

ALGO_PATH = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py"
ALGO_SHA256 = "e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0"
MODULE_NAME = "cert_checker"


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
try:
    _status = _mod.main(sys.argv[1:])
except BaseException:                    # same mapping as the checker's own __main__ block
    _status = _mod.EXIT_CODE["ERROR"]
sys.exit(_status)
