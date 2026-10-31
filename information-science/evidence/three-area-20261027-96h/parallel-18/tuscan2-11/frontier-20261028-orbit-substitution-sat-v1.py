#!/usr/bin/env python3
"""Second, independently written CNF for T2(11) with row-orbit blocks.

Written from the definition only; it shares no code with the partial-symmetry
encoders. Block rows have NO variables of their own: row t of block j is
g^t(R_j), so "row (j,t) holds v at column c" is the literal R_j[c] = g^-t(v).
Free rows have their own variables. Every row is a permutation. For every
ordered pair (a, b) of distinct symbols, the events "a at column c and b at
column c+1 of row r" are defined by full equivalences Y <-> X & X' and exactly
one of them holds; the distance-2 events are defined the same way and at most
one holds. Nothing else is assumed: no first/last-symbol rules, no symmetry
breaking and no lemma consequences. A model is decoded and checked here.
Usage: SCRIPT CYCLES(comma) B OUT.cnf OUT.json [SOLVE_SECONDS]
"""
import hashlib
import json
import subprocess
import sys
import time
from math import lcm
from pathlib import Path

N = 11


class Formula:
    def __init__(self):
        self.top = 0
        self.clauses = []

    def new(self):
        self.top += 1
        return self.top

    def clause(self, *lits):
        self.clauses.append(lits)

    def at_most_one(self, lits):
        # sequential counter (Sinz 2005)
        if len(lits) <= 1:
            return
        prev = None
        for i, x in enumerate(lits):
            if i == len(lits) - 1:
                if prev is not None:
                    self.clause(-x, -prev)
                break
            s = self.new()
            self.clause(-x, s)
            if prev is not None:
                self.clause(-prev, s)
                self.clause(-x, -prev)
            prev = s

    def exactly_one(self, lits):
        self.clause(*lits)
        self.at_most_one(lits)


def permutation_of_cycles(cycles):
    if sum(cycles) != N:
        raise ValueError('cycle lengths must sum to 11')
    perm, start = list(range(N)), 0
    for size in cycles:
        for i in range(size):
            perm[start + i] = start + (i + 1) % size
        start += size
    return perm


def build(cycles, b):
    g = permutation_of_cycles(cycles)
    k = lcm(*cycles)
    if b * k > N:
        raise ValueError('too many block rows')
    inverse_powers = []
    power = list(range(N))
    for _ in range(k):
        inv = [0] * N
        for v in range(N):
            inv[power[v]] = v
        inverse_powers.append(inv)
        power = [g[x] for x in power]
    F = Formula()
    base = [[[F.new() for _ in range(N)] for _ in range(N)] for _ in range(b)]
    free = [[[F.new() for _ in range(N)] for _ in range(N)] for _ in range(N - b * k)]
    for grid in base + free:
        for c in range(N):
            F.exactly_one([grid[c][v] for v in range(N)])
        for v in range(N):
            F.exactly_one([grid[c][v] for c in range(N)])
    rows = []
    for j in range(b):
        for t in range(k):
            rows.append(lambda c, v, j=j, t=t: base[j][c][inverse_powers[t][v]])
    for i in range(N - b * k):
        rows.append(lambda c, v, i=i: free[i][c][v])
    for dist, exact in ((1, True), (2, False)):
        for a in range(N):
            for z in range(N):
                if a == z:
                    continue
                events = []
                for row in rows:
                    for c in range(N - dist):
                        y, p, q = F.new(), row(c, a), row(c + dist, z)
                        F.clause(-y, p); F.clause(-y, q); F.clause(y, -p, -q)
                        events.append(y)
                if exact:
                    F.exactly_one(events)
                else:
                    F.at_most_one(events)
    return F, rows, g, k


def main(argv):
    if len(argv) not in (5, 6):
        raise SystemExit('usage: SCRIPT CYCLES B OUT.cnf OUT.json [SOLVE_SECONDS]')
    cycles = [int(x) for x in argv[1].split(',')]
    b, cnf, out = int(argv[2]), Path(argv[3]), Path(argv[4])
    F, rows, g, k = build(cycles, b)
    with cnf.open('x', encoding='ascii') as stream:
        stream.write(f'p cnf {F.top} {len(F.clauses)}\n')
        for cl in F.clauses:
            stream.write(' '.join(map(str, cl)) + ' 0\n')
    record = {'kind': 'orbit_substitution_t2_11_cnf', 'cycles': cycles, 'order': k, 'base_rows': b,
              'free_rows': N - b * k, 'g': g, 'variables': F.top, 'clauses': len(F.clauses),
              'cnf_sha256': hashlib.sha256(cnf.read_bytes()).hexdigest(),
              'encoder_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if len(argv) == 6:
        seconds = int(argv[5])
        t0 = time.monotonic()
        proc = subprocess.run(['kissat', f'--time={seconds}', str(cnf)], capture_output=True, text=True,
                              timeout=seconds + 120, check=False)
        record.update({'returncode': proc.returncode, 'elapsed_ms': round((time.monotonic() - t0) * 1000),
                       'status': {10: 'sat', 20: 'unsat_unverified', 0: 'unknown'}.get(proc.returncode,
                                                                                         'solver_error')})
        if proc.returncode == 10:
            true = {int(x) for ln in proc.stdout.splitlines() if ln.startswith('v ')
                    for x in ln.split()[1:] if int(x) > 0}
            table = [[next(v for v in range(N) if row(c, v) in true) for c in range(N)] for row in rows]
            d1 = {(x[i], x[i + 1]) for x in table for i in range(N - 1)}
            d2 = {(x[i], x[i + 2]) for x in table for i in range(N - 2)}
            record.update({'rows': table, 'check_ok': all(sorted(x) == list(range(N)) for x in table)
                           and len(d1) == 110 and len(d2) == 99})
    with out.open('x', encoding='utf-8') as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({key: record.get(key) for key in ('cycles', 'base_rows', 'variables', 'clauses',
                                                         'cnf_sha256', 'status', 'elapsed_ms')}))


if __name__ == '__main__':
    main(sys.argv)
