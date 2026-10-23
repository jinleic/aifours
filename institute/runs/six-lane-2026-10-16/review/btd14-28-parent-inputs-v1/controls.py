"""Positive and intended-reason mutation controls for check_btd_parent.py. Fixtures are retained (mode x)."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE / 'check_btd_parent.py'
W = (HERE / 'btd14-28-witness-v1.btd').read_bytes()
P = ['14', '28', '8', '3', '14', '7', '6']
FIX = HERE / 'controls'
FIX.mkdir(exist_ok=False)


def run(name, raw, params, expect_result, expect_reason=None, sha=None):
    f = FIX / (name + '.btd')
    with open(f, 'xb') as h:
        h.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    out = FIX / (name + '.json')
    subprocess.run(['/usr/bin/python3', '-B', str(CHECKER), str(f)] + params + [sha or digest, str(out)],
                   capture_output=True)
    rec = json.loads(out.read_text())
    ok = rec['result'] == expect_result and (expect_reason is None or rec.get('reason') == expect_reason)
    return {'name': name, 'fixture_sha256': digest, 'result': rec['result'], 'reason': rec.get('reason'),
            'expected': [expect_result, expect_reason], 'ok': ok}


def matrix(raw):
    lines = raw.decode().split('\n')
    return lines[0], [list(map(int, l.split())) for l in lines[1:-1]]


def render(header, M):
    return (header + '\n' + '\n'.join(' '.join(map(str, r)) for r in M) + '\n').encode()


rows = []
small = render('BTD 3 6 2 1 4 2 1', [[1, 1, 0, 0, 2, 0], [0, 1, 1, 0, 0, 2], [1, 0, 1, 2, 0, 0]])
rows.append(run('positive-small-two-circulant', small, ['3', '6', '2', '1', '4', '2', '1'], 'VALID'))
rows.append(run('positive-witness', W, P, 'VALID'))
h, M = matrix(W)
Mc = [r[:] for r in M]
for r in Mc:
    r[0], r[27] = r[27], r[0]
rows.append(run('positive-column-swap', render(h, Mc), P, 'VALID'))
Mr = [r[:] for r in M]
Mr[0], Mr[13] = Mr[13], Mr[0]
rows.append(run('positive-row-swap', render(h, Mr), P, 'VALID'))
m = [r[:] for r in M]
j = m[0].index(1)
m[0][j] = 2
rows.append(run('mut-one-to-two', render(h, m), P, 'INVALID', 'row-composition'))
m = [r[:] for r in M]
found = None
for i in range(14):
    for k in range(i + 1, 14):
        for j in range(28):
            for l in range(28):
                if m[i][j] == 1 and m[i][l] == 0 and m[k][j] == 0 and m[k][l] == 1:
                    found = (i, k, j, l)
                    break
            if found:
                break
        if found:
            break
    if found:
        break
i, k, j, l = found
m[i][j], m[i][l], m[k][j], m[k][l] = 0, 1, 1, 0
rows.append(run('mut-2x2-switch', render(h, m), P, 'INVALID', 'inner-product'))
m = [r[:] for r in M]
a = m[0].index(1)
b = m[0].index(0)
m[0][a], m[0][b] = 0, 1
rows.append(run('mut-row-shift', render(h, m), P, 'INVALID', 'column-sum'))
rows.append(run('mut-header', W.replace(b'BTD 14 28 8 3 14 7 6', b'BTD 14 28 8 3 14 7 5', 1), P, 'INVALID', 'header'))
rows.append(run('mut-no-final-LF', W[:-1], P, 'INVALID', 'final-LF'))
rows.append(run('mut-alphabet', W.replace(b'\n2 0 0 1', b'\n3 0 0 1', 1), P, 'INVALID', 'alphabet'))
rows.append(run('mut-extra-row', W + W.split(b'\n')[1] + b'\n', P, 'INVALID', 'line-count'))
rows.append(run('mut-crlf', W.replace(b'\n', b'\r\n'), P, 'INVALID', 'forbidden-whitespace'))
rows.append(run('mut-wrong-sha', W, P, 'INVALID', 'sha256-mismatch', sha='0' * 64))
rec = {'checker_sha256': hashlib.sha256(CHECKER.read_bytes()).hexdigest(), 'rows': rows,
       'verdict': 'PASS' if all(r['ok'] for r in rows) else 'FAIL'}
with open(HERE / 'controls-result.json', 'x') as f:
    json.dump(rec, f, indent=1)
    f.write('\n')
print(json.dumps({'verdict': rec['verdict'], 'rows': [(r['name'], r['result'], r['reason'], r['ok']) for r in rows]}))
sys.exit(0 if rec['verdict'] == 'PASS' else 1)
