#!/usr/bin/env python3
"""Run only reviewer-authored controls, retaining exact clock and exit receipts."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

root = pathlib.Path(__file__).resolve().parent
control = root / 'reviewer-f195-controls-v1.py'
stdout_path = root / 'reviewer-f195-controls-v1.stdout.json'
stderr_path = root / 'reviewer-f195-controls-v1.stderr.txt'
receipt_path = root / 'reviewer-f195-controls-v1-receipt.json'
for p in (stdout_path, stderr_path, receipt_path):
    if p.exists():
        raise FileExistsError(p)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def save(path, data):
    with path.open('xb') as f:
        f.write(data)

source_sha = sha(control)
runner_sha = sha(pathlib.Path(__file__))
started = clock()
start_mono = time.monotonic()
cap = 115
try:
    p = subprocess.run([sys.executable, '-B', str(control)], cwd=root,
                       stdin=subprocess.DEVNULL, capture_output=True, timeout=cap)
    timed_out = False
    out, err, exit_code = p.stdout, p.stderr, p.returncode
except subprocess.TimeoutExpired as e:
    timed_out = True
    out, err, exit_code = e.stdout or b'', e.stderr or b'', None
elapsed = time.monotonic() - start_mono
finished = clock()
save(stdout_path, out)
save(stderr_path, err)
try:
    parsed_status = json.loads(out).get('status') if out else None
except (json.JSONDecodeError, UnicodeDecodeError):
    parsed_status = None
source_after = sha(control)
status = 'UNKNOWN_CAP' if timed_out else ('PASS' if exit_code == 0 and parsed_status == 'PASS'
                                           and source_sha == source_after else 'FAIL')
receipt = {'status': status, 'started_native': started, 'finished_native': finished,
           'elapsed_monotonic_seconds': round(elapsed, 6), 'timeout_seconds': cap,
           'timed_out': timed_out, 'exit_code': exit_code,
           'command': [sys.executable, '-B', str(control)],
           'python_version': sys.version, 'source_sha256_before': source_sha,
           'source_sha256_after': source_after, 'runner_sha256': runner_sha,
           'stdout': {'path': stdout_path.name, 'bytes': len(out), 'sha256': sha(stdout_path)},
           'stderr': {'path': stderr_path.name, 'bytes': len(err), 'sha256': sha(stderr_path)}}
save(receipt_path, (json.dumps(receipt, indent=2, sort_keys=True) + '\n').encode())
print(json.dumps(receipt, indent=2, sort_keys=True))
sys.exit(0 if status == 'PASS' else 1)
