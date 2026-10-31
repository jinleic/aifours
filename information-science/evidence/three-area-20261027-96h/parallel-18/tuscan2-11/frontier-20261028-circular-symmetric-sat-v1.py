#!/usr/bin/env python3
"""Bounded SAT search for symmetric circular Tuscan-2 arrays of size 11 x 12.

A circular Tuscan-2 array has 11 cyclic rows, each a cyclic arrangement of 12
symbols, such that every ordered pair of distinct symbols occurs exactly once
at cyclic distance 1 and exactly once at cyclic distance 2 (counting forces
exactness). Cutting every row at one symbol yields an actual linear
Tuscan-2 square of order 11, which the script reconstructs and checks.

Symmetry: a fixed-point-free permutation g of order q in {2,3} on the 12
symbols; rows form (11-b)/q orbits {R, gR, ..., g^{q-1}R} (position-wise) and
b rows fixed by g, on which g acts as the cyclic rotation by 12/q positions
(or, for q=3, by 8 positions; a selector chooses per fixed row). Every
symmetric solution of these types is a genuine circular array; failure says
nothing about asymmetric arrays or about the linear problem.
Usage: SCRIPT Q B OUT.json OUT.cnf SECONDS SEED
"""
import hashlib
import itertools
import json
import subprocess
import sys
import time
from pathlib import Path

M = 12
R = 11


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


def perm(q):
    g = list(range(M))
    for start in range(0, M, q):
        block = list(range(start, start + q))
        for i, v in enumerate(block):
            g[v] = block[(i + 1) % q]
    return g


def build(q, b):
    if q not in (2, 3) or (R - b) % q or b < 0 or b > R:
        raise ValueError('invalid orbit structure')
    g = perm(q)
    f = CNF()
    Y = [[[f.var() for _ in range(M)] for _ in range(M)] for _ in range(R)]
    S = [[[f.var() if a != c else None for c in range(M)] for a in range(M)] for _ in range(R)]
    T = [[[f.var() if a != c else None for c in range(M)] for a in range(M)] for _ in range(R)]
    for r in range(R):
        for p in range(M):
            f.eo(Y[r][p][v] for v in range(M))
        for v in range(M):
            f.eo(Y[r][p][v] for p in range(M))
        for a in range(M):
            f.eo(S[r][a][c] for c in range(M) if c != a)
            f.eo(S[r][c][a] for c in range(M) if c != a)
            f.eo(T[r][a][c] for c in range(M) if c != a)
            f.eo(T[r][c][a] for c in range(M) if c != a)
            for c in range(M):
                if c == a:
                    continue
                f.add(-S[r][a][c], -T[r][a][c])
                for p in range(M):
                    f.add(-S[r][a][c], -Y[r][p][a], Y[r][(p + 1) % M][c])
                    f.add(-Y[r][p][a], -Y[r][(p + 1) % M][c], S[r][a][c])
                    f.add(-T[r][a][c], -Y[r][p][a], Y[r][(p + 2) % M][c])
                    f.add(-Y[r][p][a], -Y[r][(p + 2) % M][c], T[r][a][c])
                for d in range(M):
                    if d != a and d != c:
                        f.add(-S[r][a][c], -S[r][c][d], T[r][a][d])
    for a in range(M):
        for c in range(M):
            if a != c:
                f.eo(S[r][a][c] for r in range(R))
                f.eo(T[r][a][c] for r in range(R))
    # symmetry: orbits of size q, position-wise images
    orbits = (R - b) // q
    row = 0
    reps = []
    for _ in range(orbits):
        members = list(range(row, row + q))
        reps.append(members[0])
        for k in range(q - 1):
            src, dst = members[k], members[k + 1]
            for p in range(M):
                for v in range(M):
                    f.add(-Y[src][p][v], Y[dst][p][g[v]])
                    f.add(Y[src][p][v], -Y[dst][p][g[v]])
        row += q
    fixed_rows = list(range(row, R))
    shift = M // q
    for r in fixed_rows:
        if q == 2:
            for p in range(M):
                for v in range(M):
                    f.add(-Y[r][p][v], Y[r][(p + shift) % M][g[v]])
        else:
            z = f.var()
            for p in range(M):
                for v in range(M):
                    f.add(-z, -Y[r][p][v], Y[r][(p + shift) % M][g[v]])
                    f.add(z, -Y[r][p][v], Y[r][(p + 2 * shift) % M][g[v]])
    # rotation normalization: symbol 0 at position 0 in orbit reps and fixed rows
    for r in reps + fixed_rows:
        f.add(Y[r][0][0])
    return f, Y, g, fixed_rows


def main(argv):
    if len(argv) != 7:
        raise ValueError('usage: SCRIPT Q B OUT.json OUT.cnf SECONDS SEED')
    q, b = int(argv[1]), int(argv[2]); out, cnf = Path(argv[3]), Path(argv[4])
    seconds, seed = int(argv[5]), int(argv[6])
    f, Y, g, fixed_rows = build(q, b)
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
        result = {'kind': 'symmetric_circular_tuscan2_11x12_sat', 'q': q, 'fixed_rows': b,
                  'g': g, 'variables': f.n, 'clauses': len(f.clauses),
                  'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
                  'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'command': command, 'returncode': rc, 'status': status,
                  'elapsed_ms': round((time.monotonic() - t0) * 1000),
                  'solver_stdout_tail': so[-3000:],
                  'scope': 'Only this symmetry/orbit type; UNKNOWN/UNSAT say nothing about other arrays.'}
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            cyc = []
            for r in range(R):
                rowv = []
                for p in range(M):
                    vals = [v for v in range(M) if Y[r][p][v] in assigned]
                    if len(vals) != 1:
                        raise AssertionError('decode failure')
                    rowv.append(vals[0])
                cyc.append(rowv)
            d1 = [(x[i], x[(i + 1) % M]) for x in cyc for i in range(M)]
            d2 = [(x[i], x[(i + 2) % M]) for x in cyc for i in range(M)]
            circ_ok = (all(sorted(x) == list(range(M)) for x in cyc) and len(set(d1)) == len(d1) == R * M
                       and len(set(d2)) == len(d2) == R * M)
            cut = M - 1
            linear = []
            for x in cyc:
                k = x.index(cut)
                linear.append([x[(k + 1 + i) % M] for i in range(M - 1)])
            l1 = [(x[i], x[i + 1]) for x in linear for i in range(M - 2)]
            l2 = [(x[i], x[i + 2]) for x in linear for i in range(M - 3)]
            lin_ok = (all(sorted(x) == list(range(M - 1)) for x in linear) and len(set(l1)) == len(l1)
                      and len(set(l2)) == len(l2))
            result.update({'circular_rows': cyc, 'circular_check_ok': circ_ok,
                           'rows': linear, 'linear_t2_check_ok': lin_ok, 'zero_score_claim': lin_ok,
                           'best_pair_collision_score': 0 if lin_ok else None,
                           'd1_pair_collisions': 0 if lin_ok else None, 'd2_pair_collisions': 0 if lin_ok else None,
                           'd1_excess_events': 0 if lin_ok else None, 'd2_excess_events': 0 if lin_ok else None})
        json.dump(result, res, indent=2, sort_keys=True)
        res.write('\n')
    print(json.dumps({k: result.get(k) for k in ('q', 'fixed_rows', 'status', 'variables', 'clauses', 'elapsed_ms',
                                                    'circular_check_ok', 'linear_t2_check_ok')}))


if __name__ == '__main__':
    main(sys.argv)
