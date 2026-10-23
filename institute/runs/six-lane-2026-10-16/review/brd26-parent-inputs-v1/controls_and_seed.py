"""Retained parent BRD control fixtures and independent six-base-block expansion.
No worker imports. Checks both marginal failures and a sign-only corruption preserving all support counts.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE / 'check_brd_parent.py'
RAW = (HERE / 'brd26-130-witness-v1.brd').read_bytes()
P = [26, 130, 25, 5, 4]
OUT = HERE / 'controls-v1'
OUT.mkdir(exist_ok=False)


def render(M, params):
    return ('BRD ' + ' '.join(map(str, params)) + '\n' + '\n'.join(' '.join(map(str, row)) for row in M) + '\n').encode()


def trial(name, raw, params, expected, reason=None, digest=None):
    f = OUT / (name + '.brd')
    with open(f, 'xb') as h:
        h.write(raw)
    h = hashlib.sha256(raw).hexdigest()
    recpath = OUT / (name + '.json')
    run = subprocess.run(['/usr/bin/python3', '-B', str(CHECKER), str(f)] + list(map(str, params))
                         + [digest or h, str(recpath)], capture_output=True, text=True)
    rec = json.loads(recpath.read_text())
    ok = rec['result'] == expected and (reason is None or rec.get('reason') == reason)
    return {'name': name, 'params': params, 'sha256': h, 'rc': run.returncode, 'result': rec['result'],
            'reason': rec.get('reason'), 'expected_reason': reason, 'ok': ok}


M = [list(map(int, s.split())) for s in RAW.decode().split('\n')[1:-1]]
rows = [trial('positive-witness', RAW, P, 'VALID')]
# Paley symmetric conference matrix on F5 union infinity: BRD(6,6,5,5,4).
chi = lambda x: 0 if x % 5 == 0 else (1 if x % 5 in (1, 4) else -1)
C6 = [[0 if i == j else (1 if i == 5 or j == 5 else chi(i - j)) for j in range(6)] for i in range(6)]
rows.append(trial('positive-Paley6', render(C6, [6, 6, 5, 5, 4]), [6, 6, 5, 5, 4], 'VALID'))
C4 = [[0, 1, 1, 1], [-1, 0, 1, -1], [-1, -1, 0, 1], [-1, 1, -1, 0]]
rows.append(trial('positive-conference4', render(C4, [4, 4, 3, 3, 2]), [4, 4, 3, 3, 2], 'VALID'))
for kind in ('row-permutation', 'column-permutation', 'row-sign', 'column-sign'):
    A = [r[:] for r in M]
    if kind == 'row-permutation':
        A[0], A[25] = A[25], A[0]
    elif kind == 'column-permutation':
        for r in A:
            r[0], r[129] = r[129], r[0]
    elif kind == 'row-sign':
        A[0] = [-x for x in A[0]]
    else:
        for r in A:
            r[0] = -r[0]
    rows.append(trial('positive-' + kind, render(A, P), P, 'VALID'))
A = [r[:] for r in M]
j = next(j for j, x in enumerate(A[0]) if x)
A[0][j] = 0
rows.append(trial('mut-row-weight', render(A, P), P, 'INVALID', 'row-weight'))
A = [r[:] for r in M]
j = next(j for j, x in enumerate(A[0]) if x)
l = A[0].index(0)
A[0][l], A[0][j] = A[0][j], 0
rows.append(trial('mut-column-weight', render(A, P), P, 'INVALID', 'column-weight'))
A = [r[:] for r in M]
j = next(j for j, x in enumerate(A[0]) if x)
A[0][j] = -A[0][j]
rows.append(trial('mut-pair-signs', render(A, P), P, 'INVALID', 'pair-sign-balance'))
A = [r[:] for r in M]
A[0][0] = -2
rows.append(trial('mut-alphabet', render(A, P), P, 'INVALID', 'alphabet'))
rows.append(trial('mut-header', RAW.replace(b'BRD 26 130 25 5 4', b'BRD 26 130 25 6 4', 1), P, 'INVALID', 'header'))
rows.append(trial('mut-no-final-LF', RAW[:-1], P, 'INVALID', 'final-LF'))
rows.append(trial('mut-double-final-LF', RAW + b'\n', P, 'INVALID', 'final-LF'))
rows.append(trial('mut-CRLF', RAW.replace(b'\n', b'\r\n'), P, 'INVALID', 'forbidden-whitespace'))
rows.append(trial('mut-extra-row', RAW + RAW.split(b'\n')[1] + b'\n', P, 'INVALID', 'line-count'))
lines = RAW.split(b'\n');lines[1] = b' '.join(lines[1].split(b' ')[:-1])
rows.append(trial('mut-short-row', b'\n'.join(lines), P, 'INVALID', 'row-length'))
rows.append(trial('mut-wrong-sha', RAW, P, 'INVALID', 'sha256', digest='0' * 64))
# Independently expand the worker-reported signed seed; infinity is point25.
regular = [
    [(0, -1), (13, -1), (16, -1), (18, -1), (24, 1)],
    [(3, -1), (8, 1), (16, 1), (22, -1), (24, -1)],
    [(2, 1), (7, -1), (10, 1), (11, 1), (17, 1)],
    [(1, 1), (10, -1), (12, 1), (13, 1), (14, -1)],
    [(3, -1), (6, -1), (13, 1), (24, 1), (25, -1)],
]
short = [(2, 1), (7, 1), (12, 1), (17, 1), (22, 1)]
columns = []
for base, shifts in [(b, range(25)) for b in regular] + [(short, range(5))]:
    for s in shifts:
        col = [0] * 26
        for x, sign in base:
            y = (x + s) % 25 if x != 25 else 25
            if col[y]:
                raise ValueError('Seed has a repeated point')
            col[y] = sign
        columns.append(col)
expanded = [[c[i] for c in columns] for i in range(26)]
expanded_raw = render(expanded, P)
with open(HERE / 'seed-expanded-v1.brd', 'xb') as f:
    f.write(expanded_raw)
seed_equal = expanded_raw == RAW
rows.append(trial('positive-parent-seed', expanded_raw, P, 'VALID'))
rec = {'checker_sha256': hashlib.sha256(CHECKER.read_bytes()).hexdigest(), 'rows': rows,
       'seed': {'regular': regular, 'short': short, 'column_orbits': [25] * 5 + [5],
                'expanded_sha256': hashlib.sha256(expanded_raw).hexdigest(), 'byte_equal': seed_equal},
       'verdict': 'PASS' if seed_equal and all(r['ok'] for r in rows) else 'FAIL'}
with open(HERE / 'controls-seed-result.json', 'x') as f:
    json.dump(rec, f, indent=1)
    f.write('\n')
print(json.dumps({'verdict': rec['verdict'], 'controls': len(rows), 'seed_byte_equal': seed_equal,
                  'bad': [r for r in rows if not r['ok']]}))
sys.exit(0 if rec['verdict'] == 'PASS' else 1)
