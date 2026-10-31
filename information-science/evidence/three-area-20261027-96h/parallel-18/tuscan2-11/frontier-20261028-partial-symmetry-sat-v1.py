#!/usr/bin/env python3
"""Bounded SAT search for actual T2(11) squares with PARTIAL row symmetry.

A full symbol automorphism is impossible for odd prime order (proved
separately). Here only some rows are tied: a symbol permutation g of order k
(given by cycle lengths) and b base rows, each followed by its k-1 position-
wise images g(R),...,g^{k-1}(R); the remaining 11-b*k rows are completely
free. The whole array must be an actual linear Tuscan-2 square (D1 exactly
once, D2 at most once). Any SAT model is decoded and checked; UNSAT/UNKNOWN
concern only this structured subclass and never the original problem.
Usage: SCRIPT CYCLES(comma) B OUT.json OUT.cnf SECONDS SEED
"""
import hashlib
import itertools
import json
import subprocess
import sys
import time
from math import lcm
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


def make_g(cycles):
    if sum(cycles) != N or any(c < 1 for c in cycles):
        raise ValueError('cycle lengths must sum to 11')
    g = list(range(N)); start = 0
    for length in cycles:
        block = list(range(start, start + length))
        for i, v in enumerate(block):
            g[v] = block[(i + 1) % length]
        start += length
    return g


def build(cycles, b):
    g = make_g(cycles)
    k = lcm(*cycles)
    if k < 2 or b < 1 or b * k > N:
        raise ValueError('need nontrivial g and b*k <= 11')
    f = CNF()
    X = [[[f.var() for _ in range(N)] for _ in range(N)] for _ in range(N)]
    S = [[[f.var() if a != c else None for c in range(N)] for a in range(N)] for _ in range(N)]
    T = [[[f.var() if a != c else None for c in range(N)] for a in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            f.eo(X[r][c][v] for v in range(N))
        for v in range(N):
            f.eo(X[r][c][v] for c in range(N))
        for a in range(N):
            f.eo([S[r][a][x] for x in range(N) if x != a] + [X[r][N - 1][a]])
            f.eo([S[r][x][a] for x in range(N) if x != a] + [X[r][0][a]])
            f.eo([T[r][a][x] for x in range(N) if x != a] + [X[r][N - 1][a], X[r][N - 2][a]])
            f.eo([T[r][x][a] for x in range(N) if x != a] + [X[r][0][a], X[r][1][a]])
            for x in range(N):
                if x == a:
                    continue
                f.add(-S[r][a][x], -T[r][a][x])
                for c in range(N):
                    if c + 1 < N:
                        f.add(-S[r][a][x], -X[r][c][a], X[r][c + 1][x])
                        f.add(-X[r][c][a], -X[r][c + 1][x], S[r][a][x])
                    else:
                        f.add(-S[r][a][x], -X[r][c][a])
                    if c + 2 < N:
                        f.add(-T[r][a][x], -X[r][c][a], X[r][c + 2][x])
                        f.add(-X[r][c][a], -X[r][c + 2][x], T[r][a][x])
                    else:
                        f.add(-T[r][a][x], -X[r][c][a])
                for y in range(N):
                    if y != a and y != x:
                        f.add(-S[r][a][x], -S[r][x][y], T[r][a][y])
    for a in range(N):
        for x in range(N):
            if a != x:
                f.eo(S[r][a][x] for r in range(N))
                f.amo(T[r][a][x] for r in range(N))
    for v in range(N):
        f.eo(X[r][0][v] for r in range(N))
        f.eo(X[r][N - 1][v] for r in range(N))
    for j in range(b):
        for i in range(k - 1):
            src, dst = j * k + i, j * k + i + 1
            for c in range(N):
                for v in range(N):
                    f.add(-X[src][c][v], X[dst][c][g[v]])
                    f.add(X[src][c][v], -X[dst][c][g[v]])
    return f, X, g, k


def main(argv):
    if len(argv) != 7:
        raise ValueError('usage: SCRIPT CYCLES B OUT.json OUT.cnf SECONDS SEED')
    cycles = [int(x) for x in argv[1].split(',')]
    b = int(argv[2]); out, cnf = Path(argv[3]), Path(argv[4]); seconds, seed = int(argv[5]), int(argv[6])
    f, X, g, k = build(cycles, b)
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
        result = {'kind': 'partial_symmetry_t2_11_sat', 'cycles': cycles, 'order': k, 'base_rows': b,
                  'free_rows': N - b * k, 'g': g, 'variables': f.n, 'clauses': len(f.clauses),
                  'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
                  'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'command': command, 'returncode': rc, 'status': status,
                  'elapsed_ms': round((time.monotonic() - t0) * 1000), 'solver_stdout_tail': so[-3000:],
                  'scope': 'Structured subclass only; UNSAT/UNKNOWN say nothing about unrestricted T2(11).'}
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = [[next(v for v in range(N) if X[r][c][v] in assigned) for c in range(N)] for r in range(N)]
            d1 = [(x[i], x[i + 1]) for x in rows for i in range(N - 1)]
            d2 = [(x[i], x[i + 2]) for x in rows for i in range(N - 2)]
            ok = all(sorted(x) == list(range(N)) for x in rows) and len(set(d1)) == 110 and len(set(d2)) == 99
            result.update({'rows': rows, 'internal_check_ok': ok, 'zero_score_claim': ok,
                           'best_pair_collision_score': 0 if ok else None,
                           'd1_pair_collisions': 0 if ok else None, 'd2_pair_collisions': 0 if ok else None,
                           'd1_excess_events': 0 if ok else None, 'd2_excess_events': 0 if ok else None})
        json.dump(result, res, indent=2, sort_keys=True)
        res.write('\n')
    print(json.dumps({k2: result.get(k2) for k2 in ('cycles', 'order', 'base_rows', 'free_rows', 'status',
                                                     'elapsed_ms', 'internal_check_ok')}))


if __name__ == '__main__':
    main(sys.argv)
