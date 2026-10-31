#!/usr/bin/env python3
"""Bounded two-boundary Shor one-b layer feasibility using Z3.

SAT is independently checked against all n^2 two-atom residue triples.
UNSAT/UNKNOWN are solver outcomes only, not formal proofs of noncompletion.
"""
from collections import Counter
import json
import sys
import z3

ROWS = {0: (0, 1, 7, 13, 14), 3: (0, 2, 4, 6),
        8: (0, 2, 4, 6), 11: (0, 1, 2)}
OLD = {(i, j) for i, tails in ROWS.items() for j in tails}


def solve(n, timeout_ms):
    if not 26 <= n <= 96 or not 1 <= timeout_ms <= 120000:
        raise ValueError('require 26<=n<=96 and timeout_ms<=120000')
    x = [[z3.Bool(f'e_{i}_{j}') for j in range(n)] for i in range(n)]
    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    solver.add(*(x[i][j] for i, j in OLD))
    solver.add(z3.PbEq([(v, 1) for row in x for v in row], n))
    for d in range(1, n//2 + 1):
        row_has, col_has = z3.Bools(f'row_{d} col_{d}')
        solver.add(z3.Not(z3.And(row_has, col_has)))
        for i in range(n):
            for j in range(n):
                solver.add(z3.Implies(z3.And(x[i][j], x[i][(j+d)%n]), row_has))
                solver.add(z3.Implies(z3.And(x[i][j], x[(i+d)%n][j]), col_has))
    result = solver.check()
    output = {'n': n, 'timeout_ms': timeout_ms, 'solver_result': str(result),
              'scope': 'necessary two-boundary residue layer only; not a completion decision'}
    if result == z3.sat:
        model = solver.model()
        pairs = [(i, j) for i in range(n) for j in range(n) if z3.is_true(model.eval(x[i][j]))]
        if len(pairs) != n or not OLD <= set(pairs):
            raise AssertionError('model misses old pairs or cardinality')
        seen = set()
        for i, j in pairs:
            for k, l in pairs:
                key = (i, (j+k)%n, l)
                if key in seen:
                    raise AssertionError('model violates two-boundary actual path uniqueness')
                seen.add(key)
        output['pairs'] = pairs
        output['directly_verified_two_atom_paths'] = len(seen)
        output['distinct_prefixes'] = len({i for i, _ in pairs})
        output['distinct_suffixes'] = len({j for _, j in pairs})
    elif result == z3.unknown:
        output['reason_unknown'] = solver.reason_unknown()
    return output


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: bayonet-layer-sat.py ORDER TIMEOUT_MS')
    print(json.dumps(solve(int(sys.argv[1]), int(sys.argv[2])), indent=2, sort_keys=True))
