"""Run the independently authored prompt-only checker on every retained parent fixture, with and without -O."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIN = HERE.parent / 'brd26-parent-inputs-v1'
CONTROLS = json.loads((PIN / 'controls-seed-result.json').read_text())['rows']


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def execute(path, params, digest, flags):
    r = subprocess.run(['/usr/bin/python3'] + flags + [str(HERE / 'checker.py')] + list(map(str, params))
                       + [str(path), digest], capture_output=True, text=True)
    return {'rc': r.returncode, 'stdout': r.stdout.strip(), 'stderr': r.stderr.strip()}


rows = []
for flags in (['-B'], ['-O', '-B']):
    for control in CONTROLS:
        path = PIN / 'controls-v1' / (control['name'] + '.brd')
        digest = '0' * 64 if control['reason'] == 'sha256' else sha(path)
        r = execute(path, control['params'], digest, flags)
        if control['result'] == 'VALID':
            ok = r['rc'] == 0 and r['stdout'] == 'VALID'
        else:
            reason = 'forbidden-byte' if control['reason'] == 'forbidden-whitespace' else control['reason']
            ok = r['rc'] == 1 and r['stderr'] == 'INVALID: ' + reason
        rows.append({'case': control['name'], 'flags': flags, 'expected_reason': control['reason'], **r, 'ok': ok})
    w = PIN / 'brd26-130-witness-v1.brd'
    r = execute(w, [26, 130, 25, 6, 4], sha(w), flags)
    rows.append({'case': 'correct-witness-wrong-CLI-parameters', 'flags': flags, **r,
                 'ok': r['rc'] == 1 and r['stderr'] == 'INVALID: header'})
rec = {'checker_sha256': sha(HERE / 'checker.py'),
       'note_sha256': sha(HERE.parent / 'brd26-claude-checker-v1.note.md'),
       'runs': len(rows), 'rows': rows, 'verdict': 'PASS' if all(r['ok'] for r in rows) else 'FAIL'}
with open(HERE / 'result.json', 'x') as f:
    json.dump(rec, f, indent=1)
    f.write('\n')
print(json.dumps({'verdict': rec['verdict'], 'runs': len(rows), 'bad': [r for r in rows if not r['ok']]}))
