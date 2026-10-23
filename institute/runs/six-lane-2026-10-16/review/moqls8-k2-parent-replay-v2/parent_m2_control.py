"""Parent check of the worker's relaxed positive control (item M2) for the frozen K2 encoders.

1. The completion X, Y recorded in the worker receipt: Latin, first row 0..7, and together with nmax00's three
   squares a set of five mutually orthogonal Latin squares.
2. Rebuild both --p4 none CNFs with the pinned encoders under /usr/bin/python3 and compare bytes with the pinned CNFs.
3. Derive the 896 unit clauses S_s(c, k) = [k == X(c)] (s = 1) / [k == Y(c)] (s = 2) for every cell c outside row 0
   from the encoders' own variable maps, append them to the rebuilt CNF, solve with CaDiCaL (A) / kissat (B), and
   check the returned model against every clause with this script's own checker.
4. Also solve the rebuilt free CNFs and check their models.
Children are never killed; solvers run with their own time limits. Writes m2-control-receipt.json (mode x).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
INP = HERE / 'inputs'
CTL = INP / 'evidence/k2_fixed/relaxed_ctrl_v1'
OUT = HERE / 'm2'
PY = '/usr/bin/python3'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def latin(L):
    return all(sorted(r) == list(range(8)) for r in L) and all(sorted(L[i][j] for i in range(8)) == list(range(8)) for j in range(8))


def orth(L, M):
    return len({(L[i][j], M[i][j]) for i in range(8) for j in range(8)}) == 64


def read_cnf(p):
    clauses, cur, nv = [], [], None
    with open(p) as f:
        for line in f:
            if line.startswith('p '):
                nv = int(line.split()[2])
                continue
            if line.startswith('c') or not line.strip():
                continue
            for t in line.split():
                v = int(t)
                if v == 0:
                    clauses.append(cur)
                    cur = []
                else:
                    cur.append(v)
    assert not cur
    return nv, clauses


def write_cnf(p, nv, clauses):
    with open(p, 'x') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')


def solve(solver, cnf):
    cmd = ['/opt/homebrew/bin/cadical', '-q', '-t', '1200', str(cnf)] if solver == 'cadical' else \
          ['/opt/homebrew/bin/kissat', '-q', '--time=1200', str(cnf)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    model = set()
    for line in r.stdout.split('\n'):
        if line.startswith('v '):
            model.update(int(t) for t in line.split()[1:] if t != '0')
    return r.returncode, model


def satisfied(clauses, model):
    return all(any(l in model for l in c) for c in clauses)


def main():
    OUT.mkdir(exist_ok=False)
    R = json.loads((CTL / 'RECEIPT.json').read_text())
    base = json.loads((CTL / 'nmax00.squares.json').read_text())
    X, Y = R['completion']['X'], R['completion']['Y']
    five = base + [X, Y]
    rec = {'started': now(), 'completion_valid': all(latin(L) for L in five) and X[0] == list(range(8))
           and Y[0] == list(range(8)) and all(orth(five[a], five[b]) for a in range(5) for b in range(a + 1, 5)),
           'rows': []}
    sq = CTL / 'nmax00.squares.json'
    for enc, solver, pinned in (('a', 'cadical', 'a_nmax00_noP4.cnf'), ('b', 'kissat', 'b_nmax00_noP4.cnf')):
        cnf = OUT / ('%s_nmax00_noP4.cnf' % enc)
        argv = [PY, '-B', str(INP / ('code/enc8_%s2.py' % enc)), '--mode', 'fixed', '--slopes', '', '--squares', str(sq),
                '--quantum', '12', '--p4', 'none', '--cnf', str(cnf)]
        if enc == 'a':
            argv += ['--map', str(cnf) + '.map.json']
        r = subprocess.run(argv, capture_output=True, text=True)
        row = {'encoder': enc, 'encode_rc': r.returncode, 'rebuilt_sha256': sha(cnf), 'pinned_sha256': sha(CTL / pinned)}
        row['rebuilt_equal'] = row['rebuilt_sha256'] == row['pinned_sha256']
        nv, clauses = read_cnf(cnf)
        # variable map (A: rebuilt map; B: the worker's pinned map, bound to the identical CNF)
        if enc == 'a':
            M = json.loads((Path(str(cnf) + '.map.json')).read_text())['vars']
            def var(s, i, j, k):
                return M[json.dumps(['S%d' % s, [i, j], k])]
        else:
            M = json.loads((CTL / 'b_nmax00_noP4.cnf.map.json').read_text())
            def var(s, i, j, k):
                return M[json.dumps(['S', s, i, j, k])]
        units = []
        for s, L in ((1, X), (2, Y)):
            for i in range(1, 8):
                for j in range(8):
                    for k in range(8):
                        v = var(s, i, j, k)
                        units.append([v if k == L[i][j] else -v])
        row['units'] = len(units)
        rc, model = solve(solver, cnf)
        row['free_rc'] = rc
        row['free_model_ok'] = rc == 10 and satisfied(clauses, model)
        fixed = OUT / ('%s_nmax00_noP4_parentfixed.cnf' % enc)
        write_cnf(fixed, nv, clauses + units)
        rc2, model2 = solve(solver, fixed)
        row['fixed_rc'] = rc2
        row['fixed_model_ok'] = rc2 == 10 and satisfied(clauses + units, model2)
        rec['rows'].append(row)
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if rec['completion_valid'] and all(
        r['encode_rc'] == 0 and r['rebuilt_equal'] and r['units'] == 896 and r['free_model_ok'] and r['fixed_model_ok']
        for r in rec['rows']) else 'FAIL'
    with open(HERE / 'm2-control-receipt.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'rows': [{k: r[k] for k in ('encoder', 'rebuilt_equal', 'free_model_ok', 'fixed_model_ok')} for r in rec['rows']]}))


if __name__ == '__main__':
    main()
