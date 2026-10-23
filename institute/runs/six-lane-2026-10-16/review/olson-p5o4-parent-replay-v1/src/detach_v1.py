#!/usr/bin/env python3
"""Start a command in its own session: fork, setsid in the child (never a process-group leader), exec.
Replaces the failed in-place os.setsid() call of 09:28:51 (EPERM: the backgrounded python was a group leader).
Usage: python3 -B detach_v1.py CMD [ARGS...]   (stdin/stdout/stderr are inherited from the caller)
"""
import os
import sys

pid = os.fork()
if pid > 0:
    print('detached child pid=%d' % pid, flush=True)
    os._exit(0)
os.setsid()
os.execvp(sys.argv[1], sys.argv[1:])
