#!/usr/bin/env python3
"""Bounded SAT test of the circular route to T2(11).

WRITTEN equivalence used (direction circular -> linear is section 1 of
frontier-20261028-circular-regular-obstruction-v1.md; the converse is the same
count read backwards): a circular Tuscan-2 array of size 11 x 12 (12 symbols,
11 cyclic rows, every ordered pair exactly once at cyclic distance 1 and exactly
once at cyclic distance 2) exists iff there is a linear T2(11) whose second and
penultimate columns are permutations and whose eleven pairs (last symbol, first
symbol) of the rows are never distance-2 pairs. Insert symbol 11 between the
last and first symbol of every row, or delete it: the new cyclic events are
(last,*), (*,first), (penultimate,*), (*,second) and (last,first); first and
last columns are permutations in every T1 table, and 99 + 11 = 110 distance-2
events then cover all ordered pairs of the 11 old symbols exactly once.

The CNF is the channelled T2(11) model (row permutations; D1 exactly once; D2
at most once; exact channelling; unique first/last symbols), the normalization
row 0 = 0..10 and row r starts with r (valid for every T1 table), and the three
boundary conditions above. A model is decoded and checked here, including the
circular conditions after inserting symbol 11.
Usage: SCRIPT OUT.json OUT.cnf SECONDS SEED
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


def build():
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
                for c in range(N):
                    if c != a and c != b:
                        f.add(-S[r][a][b], -S[r][b][c], T[r][a][c])
    for a in range(N):
        for b in range(N):
            if a != b:
                f.eo(S[r][a][b] for r in range(N))
                f.amo(T[r][a][b] for r in range(N))
    for v in range(N):
        for col in (0, 1, N - 2, N - 1):
            f.eo(X[r][col][v] for r in range(N))
    for r in range(N):
        for a in range(N):
            for c in range(N):
                if a != c:
                    for q in range(N):
                        f.add(-X[r][N - 1][a], -X[r][0][c], -T[q][a][c])
    for c in range(N):
        f.add(X[0][c][c])
    for r in range(N):
        f.add(X[r][0][r])
    return f, X


def circular_ok(rows):
    cyc = [[N] + list(r) for r in rows]
    m = N + 1
    d1 = [(x[i], x[(i + 1) % m]) for x in cyc for i in range(m)]
    d2 = [(x[i], x[(i + 2) % m]) for x in cyc for i in range(m)]
    return len(set(d1)) == len(d1) == m * N and len(set(d2)) == len(d2) == m * N


def main(argv):
    if len(argv) != 5:
        raise SystemExit('usage: SCRIPT OUT.json OUT.cnf SECONDS SEED')
    out, cnf, seconds, seed = Path(argv[1]), Path(argv[2]), int(argv[3]), int(argv[4])
    f, X = build()
    with cnf.open('x', encoding='ascii') as stream:
        stream.write(f'p cnf {f.n} {len(f.clauses)}\n')
        for clause in f.clauses:
            stream.write(' '.join(map(str, clause)) + ' 0\n')
    t0 = time.monotonic()
    proc = subprocess.run(['kissat', f'--time={seconds}', f'--seed={seed}', str(cnf)], capture_output=True,
                          text=True, timeout=seconds + 120, check=False)
    rc = proc.returncode
    record = {'kind': 'circular_route_t2_11_sat', 'variables': f.n, 'clauses': len(f.clauses),
              'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
              'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'returncode': rc, 'elapsed_ms': round((time.monotonic() - t0) * 1000),
              'status': {10: 'sat', 20: 'unsat_unverified', 0: 'unknown'}.get(rc, 'solver_error'),
              'scope': 'Circular-route subclass only; UNSAT/UNKNOWN say nothing about unrestricted T2(11).'}
    if rc == 10:
        true = {int(v) for ln in proc.stdout.splitlines() if ln.startswith('v ')
                for v in ln.split()[1:] if int(v) > 0}
        rows = [[next(v for v in range(N) if X[r][c][v] in true) for c in range(N)] for r in range(N)]
        d1 = {(x[i], x[i + 1]) for x in rows for i in range(N - 1)}
        d2 = {(x[i], x[i + 2]) for x in rows for i in range(N - 2)}
        record.update({'rows': rows, 'linear_t2_ok': all(sorted(x) == list(range(N)) for x in rows)
                       and len(d1) == 110 and len(d2) == 99, 'circular_ok': circular_ok(rows)})
    with out.open('x', encoding='utf-8') as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: record.get(k) for k in ('status', 'elapsed_ms', 'variables', 'clauses', 'cnf_sha256',
                                                  'linear_t2_ok', 'circular_ok')}))


if __name__ == '__main__':
    main(sys.argv)
