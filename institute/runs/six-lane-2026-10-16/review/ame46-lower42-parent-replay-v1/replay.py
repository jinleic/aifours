"""Run the pinned finite-fact verifier once in a fresh output tree. Never overwrite pinned evidence."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIN = HERE.parent / 'ame46-lower42-parent-inputs-v1'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


script = HERE / 'code/verify_lower42.py'
if sha(script) != '9106089aa5fa28edad039579c74e3fd2ea999a4226bbf2592827c72970af182b':
    raise ValueError('Verifier SHA mismatch')
if (HERE / 'evidence/verify_lower42.json').exists():
    raise ValueError('Refusing verifier output overwrite')
started = now()
with open(HERE / 'stdout.txt', 'xb') as out, open(HERE / 'stderr.txt', 'xb') as err:
    r = subprocess.run(['/usr/bin/python3', '-B', str(script)], cwd=HERE / 'code', stdout=out, stderr=err)
rec = {'started': started, 'ended': now(), 'returncode': r.returncode, 'verifier_sha256': sha(script),
       'result_sha256': sha(HERE / 'evidence/verify_lower42.json'),
       'pinned_result_sha256': sha(PIN / 'evidence/verify_lower42.json'),
       'stdout_sha256': sha(HERE / 'stdout.txt'), 'pinned_stdout_sha256': sha(PIN / 'evidence/verify_lower42.stdout.txt')}
rec['result_equal'] = rec['result_sha256'] == rec['pinned_result_sha256']
rec['stdout_equal'] = rec['stdout_sha256'] == rec['pinned_stdout_sha256']
rec['verdict'] = 'PASS' if r.returncode == 0 and rec['result_equal'] and rec['stdout_equal'] else 'FAIL'
with open(HERE / 'result.json', 'x') as f:
    json.dump(rec, f, indent=1)
    f.write('\n')
print(json.dumps(rec))
