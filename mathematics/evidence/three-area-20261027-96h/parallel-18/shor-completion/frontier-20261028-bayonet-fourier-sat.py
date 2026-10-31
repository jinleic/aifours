#!/usr/bin/env python3
"""Bounded 32-layer search with exact 2-adic Fourier conservation.

The five cyclotomic disjunctions encode row-degree times column-degree
convolution constancy. SAT models are checked by direct path enumeration.
A solver UNSAT/UNKNOWN is not a formal noncompletion proof.
"""
from collections import Counter
import json
import sys
import z3

N = 32
ROWS = {0:(0,1,7,13,14), 3:(0,2,4,6), 8:(0,2,4,6), 11:(0,1,2)}
OLD = {(i,j) for i, tails in ROWS.items() for j in tails}


def solve(timeout_ms):
    if not 1 <= timeout_ms <= 120000:
        raise ValueError('timeout must be 1..120000ms')
    x = [[z3.Bool(f'x_{i}_{j}') for j in range(N)] for i in range(N)]
    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*(x[i][j] for i,j in OLD))
    solver.add(z3.PbEq([(v,1) for row in x for v in row], N))
    for d in range(1, N//2+1):
        rh,ch = z3.Bools(f'r_{d} c_{d}')
        solver.add(z3.Not(z3.And(rh,ch)))
        for i in range(N):
            for j in range(N):
                solver.add(z3.Implies(z3.And(x[i][j], x[i][(j+d)%N]), rh))
                solver.add(z3.Implies(z3.And(x[i][j], x[(i+d)%N][j]), ch))
    row = [z3.Sum([z3.If(x[i][j],1,0) for j in range(N)]) for i in range(N)]
    col = [z3.Sum([z3.If(x[i][j],1,0) for i in range(N)]) for j in range(N)]
    for k in range(1, 6):
        mod = 1 << k
        half = mod//2
        r_equal = [z3.Sum([row[i] for i in range(r,N,mod)]) ==
                   z3.Sum([row[i] for i in range(r+half,N,mod)]) for r in range(half)]
        c_equal = [z3.Sum([col[i] for i in range(r,N,mod)]) ==
                   z3.Sum([col[i] for i in range(r+half,N,mod)]) for r in range(half)]
        solver.add(z3.Or(z3.And(r_equal), z3.And(c_equal)))
    res = solver.check()
    out = {'n':N, 'timeout_ms':timeout_ms, 'solver_result':str(res),
           'scope':'two-path uniqueness/conservation only; no full UD or completion'}
    if res == z3.sat:
        M = solver.model()
        pairs = [(i,j) for i in range(N) for j in range(N) if z3.is_true(M.eval(x[i][j]))]
        if len(pairs)!=N or not OLD <= set(pairs):
            raise AssertionError('bad mandatory/cardinality')
        keys, seams = set(), Counter()
        for i,j in pairs:
            for k,l in pairs:
                key=(i,(j+k)%N,l)
                if key in keys:
                    raise AssertionError('two-boundary collision')
                keys.add(key);seams[key[1]]+=1
        if any(seams[g]!=N for g in range(N)):
            raise AssertionError('two-path conservation failed')
        out['pairs'] = pairs
        out['directly_verified_paths'] = len(keys)
        out['per_seam'] = [seams[g] for g in range(N)]
    elif res == z3.unknown:
        out['reason_unknown'] = solver.reason_unknown()
    return out


if __name__ == '__main__':
    if len(sys.argv)!=2:
        raise SystemExit('usage: bayonet-fourier-sat.py TIMEOUT_MS')
    print(json.dumps(solve(int(sys.argv[1])), indent=2, sort_keys=True))
