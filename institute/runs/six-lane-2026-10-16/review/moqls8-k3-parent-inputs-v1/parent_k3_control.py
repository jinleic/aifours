"""Parent check of the K3 relaxed positive control (three quantum squares) for the frozen encoders.
1. Completion X, Y, Z from the worker receipt: Latin, first row 0..7, and with the control pair five MOLS(8).
2. Rebuild both --quantum 123 --p4 none CNFs with the pinned encoders under /usr/bin/python3; compare bytes.
3. Parent-derived 1344 unit clauses S_s(c,k) = [k == W_s(c)] for s = 1,2,3 and every cell outside row 0; solve the
   rebuilt CNF plus units with CaDiCaL (A) / kissat (B); check the model against every clause here.
4. Solve the rebuilt free CNFs and check their models. Solvers use native time limits; nothing is killed.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
INP = HERE / 'inputs'
CTL = INP / 'evidence/k3_fixed/relaxed_ctrl_v1'
OUT = HERE / 'k3-control'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


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
    if cur:
        raise ValueError('unterminated clause')
    return nv, clauses


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
    base = json.loads((CTL / 'nmax0000.squares.json').read_text())
    comp = [R['completion'][k] for k in ('X', 'Y', 'Z')]
    five = base + comp
    rec = {'completion_valid': len(base) == 2 and all(latin(L) for L in five)
           and all(L[0] == list(range(8)) for L in comp)
           and all(orth(five[a], five[b]) for a in range(5) for b in range(a + 1, 5)), 'rows': []}
    sq = CTL / 'nmax0000.squares.json'
    for enc, solver, pinned in (('a', 'cadical', 'a_nmax0000_noP4.cnf'), ('b', 'kissat', 'b_nmax0000_noP4.cnf')):
        cnf = OUT / ('%s_noP4.cnf' % enc)
        argv = ['/usr/bin/python3', '-B', str(INP / ('code/enc8_%s2.py' % enc)), '--mode', 'fixed', '--slopes', '',
                '--squares', str(sq), '--quantum', '123', '--p4', 'none', '--cnf', str(cnf)]
        if enc == 'a':
            argv += ['--map', str(cnf) + '.map.json']
        r = subprocess.run(argv, capture_output=True, text=True)
        row = {'encoder': enc, 'encode_rc': r.returncode, 'rebuilt_sha256': sha(cnf), 'pinned_sha256': sha(CTL / pinned)}
        row['rebuilt_equal'] = row['rebuilt_sha256'] == row['pinned_sha256']
        nv, clauses = read_cnf(cnf)
        if enc == 'a':
            M = json.loads(Path(str(cnf) + '.map.json').read_text())['vars']
            var = lambda s, i, j, k: M[json.dumps(['S%d' % s, [i, j], k])]
        else:
            M = json.loads((CTL / 'b_nmax0000_noP4.cnf.map.json').read_text())
            var = lambda s, i, j, k: M[json.dumps(['S', s, i, j, k])]
        units = [[var(s, i, j, k) if k == W[i][j] else -var(s, i, j, k)]
                 for s, W in ((1, comp[0]), (2, comp[1]), (3, comp[2]))
                 for i in range(1, 8) for j in range(8) for k in range(8)]
        row['units'] = len(units)
        rc, model = solve(solver, cnf)
        row['free_rc'] = rc
        row['free_model_ok'] = rc == 10 and satisfied(clauses, model)
        fixed = OUT / ('%s_noP4_parentfixed.cnf' % enc)
        with open(fixed, 'x') as f:
            f.write('p cnf %d %d\n' % (nv, len(clauses) + len(units)))
            for c in clauses + units:
                f.write(' '.join(map(str, c)) + ' 0\n')
        rc2, model2 = solve(solver, fixed)
        row['fixed_rc'] = rc2
        row['fixed_model_ok'] = rc2 == 10 and satisfied(clauses + units, model2)
        rec['rows'].append(row)
    rec['verdict'] = 'PASS' if rec['completion_valid'] and all(
        r['encode_rc'] == 0 and r['rebuilt_equal'] and r['units'] == 1344 and r['free_model_ok'] and r['fixed_model_ok']
        for r in rec['rows']) else 'FAIL'
    with open(HERE / 'k3-control-receipt.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'rows': [{k: r[k] for k in ('encoder', 'rebuilt_equal', 'free_model_ok', 'fixed_model_ok')} for r in rec['rows']]}))


if __name__ == '__main__':
    main()
