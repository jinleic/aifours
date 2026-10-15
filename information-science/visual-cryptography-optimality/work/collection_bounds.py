#!/usr/bin/env python3
"""Universal deterministic-collection lower bounds, not basis constraints.

In every black encoding M, W_Q(M)-W_F(M)>=g whenever F is
forbidden and F is a subset of qualified Q. Security supplies a white
encoding with exactly the same F restriction; its Q weight is at least
its F weight, and worst-case contrast separates every black/white pair.
Thus the following integer multicover system is necessary for each
individual black matrix, even for non-basis collection schemes.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys
import time
import z3


def certify(record, timeout, directory):
    n = record['n']
    k = 2**n
    minimal = record['minimal_qualified']
    q = [s for s in range(k) if any(s & b == b for b in minimal)]
    forbidden = [s for s in range(k) if s not in q]
    m = record['minimum_expansion']['m']
    alpha = Fraction(record['lp']['alpha'])
    # ceil(1/alpha) already excludes every smaller length than this.
    lp_lower = (alpha.denominator + alpha.numerator - 1) // alpha.numerator
    if lp_lower == m:
        return {'id': record['id'], 'minimum_collection_lower_bound': m,
                'method': 'exact rational LP', 'result': 'certified'}
    variables = [z3.Int(f'black_column_{t}') for t in range(k)]
    solver = z3.Solver()
    solver.set(timeout=timeout*1000)
    solver.add([x >= 0 for x in variables])
    solver.add(z3.Sum(variables) <= m-1)
    for s in q:
        for f in forbidden:
            if f & s == f:
                solver.add(z3.Sum([variables[t] for t in range(k) if t & s and t & f == 0]) >= 1)
    query = directory / f"{record['id']}-collection-black.smt2"
    query.write_text(solver.to_smt2())
    start = time.monotonic()
    result = solver.check()
    certified = result == z3.unsat
    output = {'id': record['id'], 'minimum_collection_lower_bound': m if certified else lp_lower,
              'method': 'unavoidable black patterns', 'result': str(result),
              'query': str(query), 'command': f'z3 {query}', 'seconds': time.monotonic()-start}
    if result == z3.sat:
        output['relaxation_witness_not_a_VCS'] = [solver.model().eval(x).as_long() for x in variables]
    if result == z3.unknown:
        output['reason'] = solver.reason_unknown()
    return output


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--queries', type=Path, required=True)
    p.add_argument('--timeout', type=int, default=60)
    a = p.parse_args()
    a.queries.mkdir(parents=True, exist_ok=True)
    records = json.loads(a.input.read_text())['records']
    results = [certify(r, a.timeout, a.queries) for r in records]
    summary = {'command': ' '.join(sys.argv), 'z3': z3.get_version_string(), 'records': results}
    a.output.write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps([r for r in results if r['method'] != 'exact rational LP'], indent=2))
