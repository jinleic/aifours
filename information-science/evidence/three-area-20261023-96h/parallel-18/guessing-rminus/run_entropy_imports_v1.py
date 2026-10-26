"""Exact one-shot launcher; requires a named parent GO before execution."""
import datetime
import json
import os
import time

import check_entropy_imports_v1 as proof

start = time.monotonic()
deadline = start + 60.0
original_need = proof.need


def guarded_need(condition, reason):
    if time.monotonic() > deadline:
        raise TimeoutError('cooperative 60-second deadline reached')
    original_need(condition, reason)


proof.need = guarded_need
receipt = {'pid': os.getpid(), 'pgid': os.getpgrp(),
           'observed_start': datetime.datetime.now().astimezone().isoformat(),
           'cooperative_seconds': 60, 'children': 0}
print(json.dumps({'launch': receipt}), flush=True)
status = 'ERROR'
try:
    proof.main()
    status = 'COMPLETED'
finally:
    print(json.dumps({'settlement': {'status': status, 'pid': os.getpid(),
          'pgid': os.getpgrp(), 'observed_finish': datetime.datetime.now().astimezone().isoformat(),
          'elapsed_seconds': time.monotonic() - start}}), flush=True)
