#!/usr/bin/env python3
"""Channelled position/successor SAT model for unrestricted Tuscan-2(n).

Variables: x[r][c][v] (row r column c holds v), s[r][a][b] (b immediately
follows a in row r), t[r][a][b] (b is two places after a in row r).
Linear rows only; no Latin-column or circular condition. Constraints:
 * each row is a permutation;
 * each ordered pair (a,b), a!=b, is a D1 event in exactly one row;
 * each ordered pair is a D2 event in at most one row;
 * exact channelling s/t <-> x, per-row successor/predecessor exactly-one,
   and the redundant transitive implication s(a,b)&s(b,c) -> t(a,c).
Valid symmetry normalization: row 0 = 0..n-1 (common relabeling) and row r
starts with r (every T1 table has unique row starts). Optional redundant:
last column is a permutation (also forced by T1), and the proved non-strict
reversal endpoint lex cut E <=lex c E^{-1} c.

SAT models are decoded and directly checked here; any claimed witness must
also be checked by a separate checker. UNKNOWN/time-limit establishes nothing;
UNSAT is reported unverified unless a separately checked proof exists.
Usage: SCRIPT N OUT.json OUT.cnf SOLVER SECONDS SEED REVERSAL_CUT(0/1)
"""
import hashlib
import itertools
import json
import subprocess
import sys
import time
from pathlib import Path


class CNF:
    def __init__(self):
        self.n_vars = 0
        self.clauses = []

    def var(self):
        self.n_vars += 1
        return self.n_vars

    def add(self, *lits):
        self.clauses.append(lits)

    def amo(self, lits):
        lits = list(lits)
        if len(lits) <= 6:
            for a, b in itertools.combinations(lits, 2):
                self.add(-a, -b)
            return
        # sequential counter at-most-one
        s = [self.var() for _ in range(len(lits) - 1)]
        self.add(-lits[0], s[0])
        for i in range(1, len(lits) - 1):
            self.add(-lits[i], s[i])
            self.add(-s[i - 1], s[i])
            self.add(-lits[i], -s[i - 1])
        self.add(-lits[-1], -s[-1])

    def exactly_one(self, lits):
        lits = list(lits)
        self.add(*lits)
        self.amo(lits)


def build(n, reversal_cut):
    f = CNF()
    X = [[[f.var() for _ in range(n)] for _ in range(n)] for _ in range(n)]
    S = [[[None] * n for _ in range(n)] for _ in range(n)]
    T = [[[None] * n for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for a in range(n):
            for b in range(n):
                if a != b:
                    S[r][a][b] = f.var()
                    T[r][a][b] = f.var()
    for r in range(n):
        for c in range(n):
            f.exactly_one(X[r][c][v] for v in range(n))
        for v in range(n):
            f.exactly_one(X[r][c][v] for c in range(n))
    # channelling
    for r in range(n):
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                s, t = S[r][a][b], T[r][a][b]
                for c in range(n):
                    if c + 1 < n:
                        f.add(-s, -X[r][c][a], X[r][c + 1][b])
                        f.add(-X[r][c][a], -X[r][c + 1][b], s)
                    else:
                        f.add(-s, -X[r][c][a])
                    if c + 2 < n:
                        f.add(-t, -X[r][c][a], X[r][c + 2][b])
                        f.add(-X[r][c][a], -X[r][c + 2][b], t)
                    else:
                        f.add(-t, -X[r][c][a])
        for a in range(n):
            # successor of a, or a is last
            f.exactly_one([S[r][a][b] for b in range(n) if b != a] + [X[r][n - 1][a]])
            # predecessor of a, or a is first
            f.exactly_one([S[r][b][a] for b in range(n) if b != a] + [X[r][0][a]])
            # distance-two successor, or a in one of last two places
            f.exactly_one([T[r][a][b] for b in range(n) if b != a] + [X[r][n - 1][a], X[r][n - 2][a]])
            f.exactly_one([T[r][b][a] for b in range(n) if b != a] + [X[r][0][a], X[r][1][a]])
            for b in range(n):
                if b == a:
                    continue
                for c in range(n):
                    if c != a and c != b:
                        f.add(-S[r][a][b], -S[r][b][c], T[r][a][c])
                # D1 and D2 cannot both join a->b within one row
                f.add(-S[r][a][b], -T[r][a][b])
    for a in range(n):
        for b in range(n):
            if a != b:
                f.exactly_one(S[r][a][b] for r in range(n))
                f.amo(T[r][a][b] for r in range(n))
    for v in range(n):
        f.exactly_one(X[r][0][v] for r in range(n))
        f.exactly_one(X[r][n - 1][v] for r in range(n))
    # normalization
    for c in range(n):
        f.add(X[0][c][c])
    for r in range(n):
        f.add(X[r][0][r])
    if reversal_cut:
        # E(r) = last symbol of row r.  E'(r) = n-1-E^{-1}(n-1-r).
        prefix = f.var(); f.add(prefix)
        for r in range(1, n):
            eq = f.var(); both = []
            for v in range(n):
                left = X[r][n - 1][v]
                right = X[n - 1 - v][n - 1][n - 1 - r]
                z = f.var(); f.add(-z, left); f.add(-z, right); f.add(-left, -right, z)
                f.add(-z, eq); both.append(z)
            f.add(-eq, *both)
            for a in range(n):
                for b in range(a):
                    f.add(-prefix, -X[r][n - 1][a], -X[n - 1 - b][n - 1][n - 1 - r])
            if r < n - 1:
                nxt = f.var(); f.add(-nxt, prefix); f.add(-nxt, eq); f.add(-prefix, -eq, nxt)
                prefix = nxt
    return f, X


def check(rows, n):
    if len(rows) != n or any(sorted(r) != list(range(n)) for r in rows):
        return False, 'not permutation rows'
    d1 = [(r[i], r[i + 1]) for r in rows for i in range(n - 1)]
    d2 = [(r[i], r[i + 2]) for r in rows for i in range(n - 2)]
    if len(set(d1)) != len(d1):
        return False, 'repeated D1'
    if len(set(d2)) != len(d2):
        return False, 'repeated D2'
    return True, 'ok'


def main(argv):
    if len(argv) != 8:
        raise ValueError('usage: SCRIPT N OUT.json OUT.cnf SOLVER SECONDS SEED REVERSAL_CUT')
    n = int(argv[1]); out, cnf = Path(argv[2]), Path(argv[3]); solver = argv[4]
    seconds, seed, cut = int(argv[5]), int(argv[6]), int(argv[7])
    if n < 3 or solver not in ('kissat', 'cadical') or not 1 <= seconds <= 86400 or cut not in (0, 1):
        raise ValueError('invalid arguments')
    start = time.monotonic()
    f, X = build(n, cut)
    with out.open('x', encoding='utf-8') as res, cnf.open('x', encoding='ascii') as stream:
        stream.write(f'p cnf {f.n_vars} {len(f.clauses)}\n')
        for clause in f.clauses:
            stream.write(' '.join(map(str, clause)) + ' 0\n')
        stream.flush()
        build_ms = round((time.monotonic() - start) * 1000)
        if solver == 'kissat':
            command = ['kissat', f'--time={seconds}', f'--seed={seed}', str(cnf)]
        else:
            command = ['cadical', '-t', str(seconds), f'--seed={seed}', str(cnf)]
        t0 = time.monotonic()
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=seconds + 30, check=False)
            rc, so, se, sup = proc.returncode, proc.stdout, proc.stderr, False
        except subprocess.TimeoutExpired as exc:
            rc = None
            so = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or '')
            se = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or '')
            sup = True
        status = ('sat' if rc == 10 and 's SATISFIABLE' in so else
                  'unsat_unverified' if rc == 20 and 's UNSATISFIABLE' in so else
                  'unknown' if rc in (0, None) else 'solver_error')
        result = {'kind': 'channelled_tuscan2_sat', 'n': n, 'solver': solver, 'seed': seed,
                  'seconds': seconds, 'reversal_cut': bool(cut), 'variables': f.n_vars,
                  'clauses': len(f.clauses), 'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
                  'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'command': command, 'returncode': rc, 'status': status, 'supervisory_timeout': sup,
                  'build_ms': build_ms, 'solve_ms': round((time.monotonic() - t0) * 1000),
                  'scope': 'Linear Tuscan-2 rows, no Latin/circular assumption. UNKNOWN proves nothing; UNSAT unverified without checked proof.',
                  'solver_stdout_tail': so[-4000:], 'solver_stderr_tail': se[-2000:]}
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = []
            for r in range(n):
                row = []
                for c in range(n):
                    vals = [v for v in range(n) if X[r][c][v] in assigned]
                    if len(vals) != 1:
                        raise AssertionError('model does not decode to a unique symbol')
                    row.append(vals[0])
                rows.append(row)
            ok, why = check(rows, n)
            result.update({'rows': rows, 'internal_check_ok': ok, 'internal_check': why,
                           'zero_score_claim': ok, 'best_pair_collision_score': 0 if ok else None,
                           'd1_pair_collisions': 0 if ok else None, 'd2_pair_collisions': 0 if ok else None,
                           'd1_excess_events': 0 if ok else None, 'd2_excess_events': 0 if ok else None})
        json.dump(result, res, indent=2, sort_keys=True)
        res.write('\n')
    print(json.dumps({k: result.get(k) for k in ('n', 'solver', 'seed', 'status', 'returncode', 'variables',
                      'clauses', 'build_ms', 'solve_ms', 'internal_check_ok', 'rows')}))


if __name__ == '__main__':
    main(sys.argv)
