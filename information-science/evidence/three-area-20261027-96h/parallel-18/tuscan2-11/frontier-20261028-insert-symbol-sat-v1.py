#!/usr/bin/env python3
"""Bounded SAT search for T2(11) squares extending a given 10-row array by one symbol.

Input: ten permutations of symbols 1..10 (JSON field "rows10", or the built-in
Vatican square r*(1..10) mod 11). Symbol 0 is inserted at an unknown position
into each of these ten rows (positions 0..10), and one completely free
eleventh row is added. The solver must make the resulting 11x11 array an
actual linear Tuscan-2 square (D1 exactly once, D2 at most once). This is a
restricted subclass of T2(11); UNSAT/UNKNOWN say nothing about other squares.
Usage: SCRIPT SOURCE(vatican|PATH.json) OUT.json OUT.cnf SECONDS SEED
"""
import hashlib
import itertools
import json
import subprocess
import sys
import time
from pathlib import Path

N = 11


class CNF:
    def __init__(self):
        self.n = 0
        self.clauses = []

    def var(self):
        self.n += 1
        return self.n

    def add(self, *lits):
        self.clauses.append(lits)

    def amo(self, lits):
        lits = list(lits)
        if len(lits) <= 6:
            for a, b in itertools.combinations(lits, 2):
                self.add(-a, -b)
            return
        s = [self.var() for _ in range(len(lits) - 1)]
        self.add(-lits[0], s[0])
        for i in range(1, len(lits) - 1):
            self.add(-lits[i], s[i]); self.add(-s[i - 1], s[i]); self.add(-lits[i], -s[i - 1])
        self.add(-lits[-1], -s[-1])

    def eo(self, lits):
        lits = list(lits)
        self.add(*lits)
        self.amo(lits)


def base_rows(source):
    if source == 'vatican':
        return [[(r * j) % 11 for j in range(1, 11)] for r in range(1, 11)]
    data = json.loads(Path(source).read_bytes())
    return data['rows10']


def build(rows10):
    if len(rows10) != 10 or any(sorted(r) != list(range(1, 11)) for r in rows10):
        raise ValueError('need ten permutations of 1..10')
    f = CNF()
    X = [[[f.var() for _ in range(N)] for _ in range(N)] for _ in range(N)]
    S = [[[f.var() if a != b else None for b in range(N)] for a in range(N)] for _ in range(N)]
    T = [[[f.var() if a != b else None for b in range(N)] for a in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            f.eo(X[r][c][v] for v in range(N))
        for v in range(N):
            f.eo(X[r][c][v] for c in range(N))
        for a in range(N):
            f.eo([S[r][a][b] for b in range(N) if b != a] + [X[r][N - 1][a]])
            f.eo([S[r][b][a] for b in range(N) if b != a] + [X[r][0][a]])
            f.eo([T[r][a][b] for b in range(N) if b != a] + [X[r][N - 1][a], X[r][N - 2][a]])
            f.eo([T[r][b][a] for b in range(N) if b != a] + [X[r][0][a], X[r][1][a]])
            for b in range(N):
                if b == a:
                    continue
                f.add(-S[r][a][b], -T[r][a][b])
                for c in range(N):
                    if c + 1 < N:
                        f.add(-S[r][a][b], -X[r][c][a], X[r][c + 1][b])
                        f.add(-X[r][c][a], -X[r][c + 1][b], S[r][a][b])
                    else:
                        f.add(-S[r][a][b], -X[r][c][a])
                    if c + 2 < N:
                        f.add(-T[r][a][b], -X[r][c][a], X[r][c + 2][b])
                        f.add(-X[r][c][a], -X[r][c + 2][b], T[r][a][b])
                    else:
                        f.add(-T[r][a][b], -X[r][c][a])
                for d in range(N):
                    if d != a and d != b:
                        f.add(-S[r][a][b], -S[r][b][d], T[r][a][d])
    for a in range(N):
        for b in range(N):
            if a != b:
                f.eo(S[r][a][b] for r in range(N))
                f.amo(T[r][a][b] for r in range(N))
    for v in range(N):
        f.eo(X[r][0][v] for r in range(N))
        f.eo(X[r][N - 1][v] for r in range(N))
    P = [[f.var() for _ in range(N)] for _ in range(10)]
    for r in range(10):
        f.eo(P[r])
        for p in range(N):
            for c in range(N):
                if c < p:
                    f.add(-P[r][p], X[r][c][rows10[r][c]])
                elif c == p:
                    f.add(-P[r][p], X[r][c][0])
                else:
                    f.add(-P[r][p], X[r][c][rows10[r][c - 1]])
    return f, X


def main(argv):
    if len(argv) != 6:
        raise ValueError('usage: SCRIPT SOURCE OUT.json OUT.cnf SECONDS SEED')
    source, out, cnf = argv[1], Path(argv[2]), Path(argv[3])
    seconds, seed = int(argv[4]), int(argv[5])
    rows10 = base_rows(source)
    f, X = build(rows10)
    with out.open('x', encoding='utf-8') as res, cnf.open('x', encoding='ascii') as stream:
        stream.write(f'p cnf {f.n} {len(f.clauses)}\n')
        for clause in f.clauses:
            stream.write(' '.join(map(str, clause)) + ' 0\n')
        stream.flush()
        command = ['kissat', f'--time={seconds}', f'--seed={seed}', str(cnf)]
        t0 = time.monotonic()
        proc = subprocess.run(command, capture_output=True, text=True, timeout=seconds + 60, check=False)
        rc, so = proc.returncode, proc.stdout
        status = ('sat' if rc == 10 and 's SATISFIABLE' in so else
                  'unsat_unverified' if rc == 20 and 's UNSATISFIABLE' in so else
                  'unknown' if rc == 0 else 'solver_error')
        result = {'kind': 'symbol_insertion_extension_t2_11_sat', 'source': source, 'rows10': rows10,
                  'variables': f.n, 'clauses': len(f.clauses),
                  'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
                  'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'command': command, 'returncode': rc, 'status': status,
                  'elapsed_ms': round((time.monotonic() - t0) * 1000), 'solver_stdout_tail': so[-3000:],
                  'scope': 'Only extensions of the given ten rows by inserting symbol 0 and one new row.'}
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = [[next(v for v in range(N) if X[r][c][v] in assigned) for c in range(N)] for r in range(N)]
            d1 = [(x[i], x[i + 1]) for x in rows for i in range(N - 1)]
            d2 = [(x[i], x[i + 2]) for x in rows for i in range(N - 2)]
            ok = all(sorted(x) == list(range(N)) for x in rows) and len(set(d1)) == 110 and len(set(d2)) == 99
            result.update({'rows': rows, 'internal_check_ok': ok, 'zero_score_claim': ok,
                           'best_pair_collision_score': 0 if ok else None})
        json.dump(result, res, indent=2, sort_keys=True)
        res.write('\n')
    print(json.dumps({k: result.get(k) for k in ('source', 'status', 'variables', 'clauses', 'elapsed_ms', 'internal_check_ok')}))


if __name__ == '__main__':
    main(sys.argv)
