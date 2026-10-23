"""Run the prompt-only Claude-written checker (checker.py, extracted verbatim) on the pinned witness and on the
parent's retained control fixtures, under python3 -B and python3 -O -B. Records stdout/stderr reasons.
Expected reasons are mapped from the parent checker's reason names to this checker's reason vocabulary."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIN = HERE.parent / 'btd14-28-parent-inputs-v1'
CHK = HERE / 'checker.py'
W = PIN / 'btd14-28-witness-v1.btd'
P = ['14', '28', '8', '3', '14', '7', '6']
MAP = {'row-composition': 'row-composition', 'inner-product': 'inner-product', 'column-sum': 'column-sum',
       'header': 'header', 'final-LF': 'final-LF', 'alphabet': 'alphabet', 'line-count': 'line-count',
       'forbidden-whitespace': 'forbidden-byte', 'sha256-mismatch': 'sha256'}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(file, params, digest, flags):
    r = subprocess.run(['/usr/bin/python3'] + flags + [str(CHK)] + params + [str(file), digest],
                       capture_output=True, text=True)
    return {'rc': r.returncode, 'stdout': r.stdout.strip(), 'stderr': r.stderr.strip()}


rows = []
controls = json.loads((PIN / 'controls-result.json').read_text())['rows']
for flags in (['-B'], ['-O', '-B']):
    res = run(W, P, sha(W), flags)
    rows.append({'case': 'witness', 'flags': flags, **res, 'ok': res['rc'] == 0 and res['stdout'] == 'VALID'})
    res = run(W, P, '0' * 64, flags)
    rows.append({'case': 'witness-wrong-sha', 'flags': flags, **res,
                 'ok': res['rc'] == 1 and res['stderr'] == 'INVALID: sha256'})
    res = run(W, ['14', '28', '8', '3', '14', '7', '5'], sha(W), flags)
    rows.append({'case': 'witness-wrong-params', 'flags': flags, **res,
                 'ok': res['rc'] == 1 and res['stderr'] == 'INVALID: header'})
    for c in controls:
        f = PIN / 'controls' / (c['name'] + '.btd')
        params = ['3', '6', '2', '1', '4', '2', '1'] if c['name'] == 'positive-small-two-circulant' else P
        digest = '0' * 64 if c['name'] == 'mut-wrong-sha' else sha(f)
        res = run(f, params, digest, flags)
        if c['result'] == 'VALID':
            ok = res['rc'] == 0 and res['stdout'] == 'VALID'
        else:
            ok = res['rc'] == 1 and res['stderr'] == 'INVALID: ' + MAP[c['reason']]
        rows.append({'case': c['name'], 'flags': flags, 'expected_parent_reason': c['reason'], **res, 'ok': ok})
rec = {'checker_sha256': sha(CHK), 'note_sha256': sha(HERE.parent / 'btd14-28-claude-checker-v1.note.md'),
       'rows': rows, 'verdict': 'PASS' if all(r['ok'] for r in rows) else 'FAIL'}
with open(HERE / 'result.json', 'x') as f:
    json.dump(rec, f, indent=1)
    f.write('\n')
print(json.dumps({'verdict': rec['verdict'], 'n': len(rows), 'bad': [(r['case'], r['flags'], r['stdout'], r['stderr']) for r in rows if not r['ok']]}))
