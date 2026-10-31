#!/usr/bin/env python3
"""Reviewer-only one-shot runner: 120 s hard subprocess cap, clock/exit/hash receipt, exclusive outputs."""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, 'reviewer-controls-v1.py')
RESULT = os.path.join(HERE, 'reviewer-controls-v1-result.json')
RECEIPT = os.path.join(HERE, 'reviewer-controls-v1-receipt.json')
STDOUT = os.path.join(HERE, 'reviewer-controls-v1-stdout.txt')
STDERR = os.path.join(HERE, 'reviewer-controls-v1-stderr.txt')

def clocks():
    return {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
            'local': datetime.datetime.now().astimezone().isoformat(timespec='seconds')}

def fact(path):
    data = open(path, 'rb').read()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), 'LF': data.count(b'\n')}

for p in (RESULT, RECEIPT, STDOUT, STDERR):
    if os.path.exists(p):
        raise FileExistsError('refusing same-output rerun: ' + p)
start = clocks()
t0 = time.monotonic()
script_before = fact(SCRIPT)
try:
    p = subprocess.run([sys.executable, SCRIPT], cwd=HERE, stdin=subprocess.DEVNULL,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, check=False)
    timed_out = False
    rc, out, err = p.returncode, p.stdout, p.stderr
except subprocess.TimeoutExpired as e:
    timed_out = True
    rc, out, err = None, e.stdout or b'', e.stderr or b''
end = clocks()
with open(STDOUT, 'xb') as f:
    f.write(out)
with open(STDERR, 'xb') as f:
    f.write(err)
result_obj = None
if os.path.exists(RESULT):
    result_obj = json.loads(open(RESULT, 'rb').read())
receipt = {
    'wave': 'f181-privacy-independent-bridge-matching-optima',
    'reviewer': 'ReviewF181PrivacyBridge', 'start': start, 'end': end,
    'elapsed_seconds': round(time.monotonic() - t0, 3), 'hard_timeout_seconds': 120,
    'timed_out': timed_out, 'exit_code': rc,
    'verdict': 'UNKNOWN' if timed_out else ('PASS' if rc == 0 and result_obj and result_obj['verdict'] == 'PASS' else 'FAIL'),
    'script_before': script_before, 'script_after': fact(SCRIPT),
    'script_unchanged': script_before == fact(SCRIPT), 'runner': fact(__file__),
    'stdout': fact(STDOUT), 'stderr': fact(STDERR),
    'result': fact(RESULT) if os.path.exists(RESULT) else None,
    'counts': result_obj['counts'] if result_obj else None,
    'author_code_executed_or_imported': False,
}
with open(RECEIPT, 'x', encoding='utf-8') as f:
    json.dump(receipt, f, indent=2)
    f.write('\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if receipt['verdict'] == 'PASS' else 1)
