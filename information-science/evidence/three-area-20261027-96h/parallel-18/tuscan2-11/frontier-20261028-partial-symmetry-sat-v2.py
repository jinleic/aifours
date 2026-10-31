#!/usr/bin/env python3
"""Bounded SAT search for actual T2(11) squares with PARTIAL row-orbit symmetry (v2).

Same model as v1: a symbol permutation g (canonical cycles on consecutive
symbols), b blocks of k = ord(g) rows R, gR, ..., g^(k-1)R (position-wise
images), and 11 - b*k free rows; the whole array must be an actual linear
Tuscan-2 square (D1 exactly once, D2 at most once).

v2 adds only constraints satisfied by at least one representative of every
solution orbit (proof in frontier-20261028-partial-row-orbit-obstruction-v1.md):
  * every block row starts with a symbol on a cycle of length exactly k, and a
    block's rows start with all symbols of one such cycle; relabelling by an
    element of the centraliser of g, block j uses the j-th k-cycle and its base
    row starts with that cycle's least symbol;
  * the free rows then start with the remaining symbols, in increasing order;
  * implied: in block rows a symbol on a shorter cycle is never an endpoint, and
    a D1 or D2 pair (x, y) with lcm(l_x, l_y) < k never occurs.
Any SAT model is decoded and checked here; it must also pass the independent
checker before any claim.  UNSAT/UNKNOWN concern only this structured subclass.
Usage: SCRIPT CYCLES(comma) B OUT.json OUT.cnf SECONDS SEED [--cnf-only]
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


def cycle_data(cycles):
    if sum(cycles) != N or any(c < 1 for c in cycles):
        raise ValueError('cycle lengths must sum to 11')
    g = list(range(N)); length = [0] * N; members = []; start = 0
    for size in cycles:
        block = list(range(start, start + size))
        members.append(block)
        for i, v in enumerate(block):
            g[v] = block[(i + 1) % size]
            length[v] = size
        start += size
    return g, length, members


def build(cycles, b):
    g, length, members = cycle_data(cycles)
    k = lcm(*cycles)
    kcycles = [m for m in members if len(m) == k]
    if k < 2 or b < 1 or b * k > N - 1:
        raise ValueError('need nontrivial g, b >= 1 and at least one free row')
    if b > len(kcycles):
        raise ValueError('b exceeds the number of k-cycles: excluded by the written lemma, not encoded')
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
    block_rows = b * k
    for j in range(b):
        for i in range(k - 1):
            src, dst = j * k + i, j * k + i + 1
            for c in range(N):
                for v in range(N):
                    f.add(-X[src][c][v], X[dst][c][g[v]])
                    f.add(X[src][c][v], -X[dst][c][g[v]])
        f.add(X[j * k][0][kcycles[j][0]])
    used = sorted(v for j in range(b) for v in kcycles[j])
    rest = [v for v in range(N) if v not in used]
    for r, v in zip(range(block_rows, N), rest):
        f.add(X[r][0][v])
    for r in range(block_rows):
        for a in range(N):
            if length[a] < k:
                f.add(-X[r][0][a]); f.add(-X[r][N - 1][a])
            for x in range(N):
                if x != a and lcm(length[a], length[x]) < k:
                    f.add(-S[r][a][x]); f.add(-T[r][a][x])
    return f, X, g, k, kcycles


def main(argv):
    cnf_only = '--cnf-only' in argv
    argv = [x for x in argv if x != '--cnf-only']
    if len(argv) != 7:
        raise ValueError('usage: SCRIPT CYCLES B OUT.json OUT.cnf SECONDS SEED [--cnf-only]')
    cycles = [int(x) for x in argv[1].split(',')]
    b = int(argv[2]); out, cnf = Path(argv[3]), Path(argv[4]); seconds, seed = int(argv[5]), int(argv[6])
    f, X, g, k, kcycles = build(cycles, b)
    with cnf.open('x', encoding='ascii') as stream:
        stream.write(f'p cnf {f.n} {len(f.clauses)}\n')
        for clause in f.clauses:
            stream.write(' '.join(map(str, clause)) + ' 0\n')
    result = {'kind': 'partial_symmetry_t2_11_sat_v2', 'cycles': cycles, 'order': k, 'base_rows': b,
              'free_rows': N - b * k, 'g': g, 'k_cycles_used': kcycles[:b], 'variables': f.n,
              'clauses': len(f.clauses), 'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
              'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Structured subclass only; UNSAT/UNKNOWN say nothing about unrestricted T2(11).'}
    if cnf_only:
        result.update({'status': 'cnf_only'})
    else:
        command = ['kissat', f'--time={seconds}', f'--seed={seed}', str(cnf)]
        t0 = time.monotonic()
        proc = subprocess.run(command, capture_output=True, text=True, timeout=seconds + 60, check=False)
        rc, so = proc.returncode, proc.stdout
        status = ('sat' if rc == 10 and 's SATISFIABLE' in so else
                  'unsat_unverified' if rc == 20 and 's UNSATISFIABLE' in so else
                  'unknown' if rc == 0 else 'solver_error')
        result.update({'command': command, 'returncode': rc, 'status': status,
                       'elapsed_ms': round((time.monotonic() - t0) * 1000), 'solver_stdout_tail': so[-3000:]})
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = [[next(v for v in range(N) if X[r][c][v] in assigned) for c in range(N)] for r in range(N)]
            d1 = [(x[i], x[i + 1]) for x in rows for i in range(N - 1)]
            d2 = [(x[i], x[i + 2]) for x in rows for i in range(N - 2)]
            ok = all(sorted(x) == list(range(N)) for x in rows) and len(set(d1)) == 110 and len(set(d2)) == 99
            result.update({'rows': rows, 'internal_check_ok': ok})
    with out.open('x', encoding='utf-8') as res:
        json.dump(result, res, indent=2, sort_keys=True)
        res.write('\n')
    print(json.dumps({k2: result.get(k2) for k2 in ('cycles', 'order', 'base_rows', 'free_rows', 'status',
                                                     'elapsed_ms', 'internal_check_ok', 'cnf_sha256')}))


if __name__ == '__main__':
    main(sys.argv)
