#!/usr/bin/env python3
"""go_exec_shim_v1.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Child entry point for owned_supervisor_v2.py:
reads exactly one line from stdin; only if it is b"GO\n" it replaces itself (os.execv, same PID and process group)
by argv[1:] (argv[1] an absolute executable path); on EOF or any other line it exits 3 without running anything."""
import os, sys
line = sys.stdin.buffer.readline()
if line != b"GO\n":
    sys.exit(3)
os.execv(sys.argv[1], sys.argv[1:])
