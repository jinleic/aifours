#!/usr/bin/env python3
"""Bounded exact n=32 search with both 2-path uniqueness and conservation.

A SAT model is directly rechecked; an UNSAT/UNKNOWN result is only a solver
outcome until independently certified. Neither outcome solves Shor completion.
"""
from collections import Counter
import json
import sys
import z3

N = 32
ROWS = {0: (0, 1, 7, 13, 14), 3: (0, 2, 4, 6),
        8: (0, 2, 4, 6), 11: (0, 1, 2)}
OLD = {(i, j) for i, tails in ROWS.items() for j in tails}


def solve(timeout_ms):
    if not 1 <= timeout_ms <= 120000:
        raise ValueError('timeout must be between1 and120000 milliseconds')
    x = [[z3.Bool(f'x_{i}_{j}') for j in range(N)] for i in range(N)]
    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*(x[i][j] for i, j in OLD))
    solver.add(z3.PbEq([(v, 1) for row in x for v in row], N))
    for d in range(1, N//2 + 1):
        row, col = z3.Bools(f'rd_{d} cd_{d}')
        solver.add(z3.Not(z3.And(row, col)))
        for i in range(N):
            for j in range(N):
                solver.add(z3.Implies(z3.And(x[i][j], x[i][(j+d)%N]), row))
                solver.add(z3.Implies(z3.And(x[i][j], x[(i+d)%N][j]), col))
    degree = [z3.Sum([z3.If(x[i][j], 1, 0) for j in range(N)]) for i in range(N)]
    for gamma in range(N):
        # Count all first atoms by their suffix j, and all next-atom heads.
        solver.add(z3.Sum([z3.If(x[i][j], degree[(gamma-j)%N], 0)
                           for i in range(N) for j in range(N)]) == N)
    res = solver.check()
    out = {'n': N, 'timeout_ms': timeout_ms, 'solver_result': str(res),
           'scope': 'finite two-boundary layer only; no full UD/completeness decision'}
    if res == z3.sat:
        model = solver.model()
        pairs = [(i,j) for i in range(N) for j in range(N) if z3.is_true(model.eval(x[i][j]))]
        if len(pairs) != N or not OLD <= set(pairs):
            raise AssertionError('bad model cardinality/mandatory atoms')
        keys, seams = set(), Counter()
        for i,j in pairs:
            for k,l in pairs:
                key = (i,(j+k)%N,l)
                if key in keys:
                    raise AssertionError('actual two-atom collision')
                keys.add(key)
                seams[key[1]] += 1
        if any(seams[g] != N for g in range(N)):
            raise AssertionError('actual seam conservation failed')
        out['pairs'] = pairs
        out['directly_checked_paths'] = len(keys)
        out['per_seam'] = [seams[g] for g in range(N)]
    elif res == z3.unknown:
        out['reason_unknown'] = solver.reason_unknown()
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: bayonet-conservation-sat.py TIMEOUT_MS')
    print(json.dumps(solve(int(sys.argv[1])), indent=2, sort_keys=True))
