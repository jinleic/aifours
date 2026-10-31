#!/usr/bin/env python3
"""Run only our exact controls, with a wall cap and immutable receipt files."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
files = {
    'manifest': root / 'manifest-v1.json',
    'assignment_transcription': root / 'reviewer-assignment.txt',
    'control_script': root / 'reviewer-controls.py',
    'fixture': root / 'reviewer-controls-input.json',
    'runner': Path(__file__).resolve(),
    'target': Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-global-single-split-odd-prime-power-v1.md'),
    'author_checker_read_only': Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261029-global-single-split-odd-prime-power-check-v1.py'),
}

def facts(path):
    body = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(body).hexdigest(),
            'bytes': len(body), 'LF': body.count(b'\n')}

def native_clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

output = root / 'reviewer-controls-output.json'
stderr = root / 'reviewer-controls-stderr.txt'
receipt = root / 'reviewer-controls-receipt.json'
if any(path.exists() for path in (output, stderr, receipt)):
    raise SystemExit('Refusing to overwrite a prior control artifact')
inputs = {key: facts(path) for key, path in files.items()}
start = native_clock()
timed_out = False
returncode = None
with output.open('xb') as out, stderr.open('xb') as err:
    try:
        completed = subprocess.run([sys.executable, '-B', str(files['control_script']), str(files['fixture'])],
                                   cwd=root, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                                   timeout=100, check=False)
        returncode = completed.returncode
    except subprocess.TimeoutExpired:
        timed_out = True
end = native_clock()
status = 'UNKNOWN_TIMEOUT' if timed_out else ('PASS' if returncode == 0 else 'FAIL')
if status == 'PASS':
    try:
        if json.loads(output.read_text(encoding='utf-8')).get('result') != 'PASS':
            status = 'FAIL_OUTPUT_RESULT'
    except (ValueError, OSError):
        status = 'FAIL_OUTPUT_PARSE'
result = {'clock_source': '/bin/date', 'started': start, 'finished': end,
          'cap_seconds': 100, 'timeout_is_unknown': True, 'timed_out': timed_out,
          'exit_code': returncode, 'status': status, 'inputs': inputs,
          'stdout': facts(output), 'stderr': facts(stderr),
          'command': [sys.executable, '-B', str(files['control_script']), str(files['fixture'])],
          'limitations': 'finite diagnostics only; no author code executed or imported'}
with receipt.open('x', encoding='utf-8') as out:
    json.dump(result, out, indent=2, sort_keys=True)
    out.write('\n')
print(json.dumps({'status': status, 'exit_code': returncode, 'receipt': str(receipt)}))
sys.exit(0 if status == 'PASS' else 1)
