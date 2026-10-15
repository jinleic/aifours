#!/usr/bin/env python3
"""Independent exact checks: no imports from solve.py or floating point math."""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path
import platform
import sys
import time
import z3


def structure(record):
    n = record['n']
    participants = tuple(range(n))
    subsets = [frozenset(i for i in participants if mask & (1 << i))
               for mask in range(2 ** n)]
    minimal = [subsets[b] for b in record['minimal_qualified']]
    assert minimal and all(minimal)
    assert all(not (x <= y) for i, x in enumerate(minimal)
               for j, y in enumerate(minimal) if i != j)
    qualified = [i for i, s in enumerate(subsets) if any(a <= s for a in minimal)]
    forbidden = [i for i in range(len(subsets)) if i not in qualified]
    return subsets, qualified, forbidden


def all_antichains(n):
    sets = [frozenset(i for i in range(n) if b & (1 << i)) for b in range(1, 2 ** n)]
    def extend(prefix, candidates):
        yield tuple(prefix)
        for j, a in enumerate(candidates):
            yield from extend(prefix + [a], [b for b in candidates[j+1:]
                                             if not (a <= b or b <= a)])
    return {frozenset(a) for a in extend([], sets) if a}


def verify_coverage(records, max_n):
    counts = {}
    for n in range(1, max_n + 1):
        covered = set()
        selected = [r for r in records if r['n'] == n]
        for r in selected:
            subsets, _, _ = structure(r)
            a = [subsets[b] for b in r['minimal_qualified']]
            orbit = {frozenset(frozenset(p[i] for i in s) for s in a)
                     for p in permutations(range(n))}
            assert not covered.intersection(orbit), 'Duplicate isomorphism orbit'
            covered.update(orbit)
        assert covered == all_antichains(n), f'Incomplete n={n} instance coverage'
        counts[str(n)] = {'classes': len(selected), 'labelled': len(covered)}
    assert len(records) == sum(v['classes'] for v in counts.values())
    return counts


def check_witness(record, witness):
    subsets, q, forbidden = structure(record)
    k = len(subsets)
    white, black = witness['white'], witness['black']
    assert len(white) == len(black) == k
    assert all(type(v) is int and v >= 0 for v in white + black)
    assert sum(white) == sum(black) == witness['m'] and witness['m'] >= 1
    for f in forbidden:
        def histogram(weights):
            result = Counter()
            for t, count in enumerate(weights):
                result[subsets[t] & subsets[f]] += count
            return +result
        assert histogram(white) == histogram(black), 'Forbidden projection leaks'
    gaps = [sum(black[t] - white[t] for t in range(k) if subsets[t] & subsets[s]) for s in q]
    assert min(gaps) == witness['gap'] and min(gaps) >= 1, 'Incorrect witness gap'


def check_lp(record):
    subsets, q, forbidden = structure(record)
    k = len(subsets)
    cert = record['lp']
    primal = list(map(F, cert['primal']))
    u, v = map(lambda a: list(map(F, a)),
               (cert['dual_inequality'], cert['dual_equality']))
    alpha = F(cert['alpha'])
    assert len(primal) == 2*k+1 and len(u) == len(q) and len(v) == len(forbidden)+1
    assert all(x >= 0 for x in primal) and all(x <= 0 for x in u)
    assert sum(primal[:k]) == sum(primal[k:2*k]) == 1
    assert primal[-1] == alpha > 0
    # Rebuild coefficients from set disjointness, not generator code.
    moments = {s: [F(not (subsets[t] & subsets[s])) for t in range(k)] for s in range(k)}
    def gap(s):
        return sum(moments[s][t] * (primal[t]-primal[k+t]) for t in range(k))
    assert all(gap(s) == 0 for s in forbidden)
    assert all(gap(s) >= alpha for s in q)
    f_nonempty = [s for s in forbidden if s != 0]
    # Dual of minimization (-alpha), <= rows, nonnegative primal variables.
    for j in range(2*k+1):
        lhs = sum(u[i] * (F(1) if j == 2*k else
                  (-moments[s][j] if j < k else moments[s][j-k])) for i, s in enumerate(q))
        lhs += v[0] * int(j < k) + v[1] * int(k <= j < 2*k)
        if j < 2*k:
            lhs += sum(v[i+2] * (moments[s][j] if j < k else -moments[s][j-k])
                       for i, s in enumerate(f_nonempty))
        assert lhs <= (-1 if j == 2*k else 0), 'Invalid rational LP dual'
    assert v[0] + v[1] == -alpha, 'LP primal/dual objectives differ'
    return alpha


def cheap_bounds(record, alpha):
    m = record['minimum_expansion']['m']
    g = record['contrast_at_minimum']['gap']
    best_m = record['expansion_at_maximum_contrast']['m']
    lower_m = (alpha.denominator + alpha.numerator - 1) // alpha.numerator
    return {'minimum': m == lower_m,
            'fixed_gap': g == (alpha * m).__floor__(),
            'at_alpha': best_m == alpha.denominator}


def integer_obligation(record, alpha, mode, directory, timeout):
    subsets, q, forbidden = structure(record)
    n = record['n']
    all_rows = frozenset(range(n))
    values = {s: z3.Int(f'zero_{s}') for s in q}
    solver = z3.Solver()
    solver.set(timeout=timeout*1000)
    # Independent coordinates: zero-pattern differences on qualified sets.
    # All forbidden coordinates, including the empty one, are zero.
    d = []
    for t in range(2 ** n):
        complement = all_rows - subsets[t]
        d.append(z3.Sum([(-1 if (len(subsets[s])-len(complement)) % 2 else 1) * values[s]
                         for s in q if complement <= subsets[s]]))
    length = z3.Sum([z3.If(x > 0, x, 0) for x in d])
    if mode == 'minimum':
        bound = record['minimum_expansion']['m'] - 1
        solver.add(length <= bound)
        solver.add([x >= 1 for x in values.values()])
    elif mode == 'fixed_gap':
        bound = record['minimum_expansion']['m']
        solver.add(length <= bound)
        solver.add([x >= record['contrast_at_minimum']['gap'] + 1 for x in values.values()])
    else:
        m = z3.Int('actual_expansion')
        solver.add(m >= 1, m < record['expansion_at_maximum_contrast']['m'], length <= m)
        solver.add([alpha.denominator*x >= alpha.numerator*m for x in values.values()])
    path = directory / f"{record['id']}-{mode}.smt2"
    path.write_text(solver.to_smt2())
    start = time.monotonic()
    result = solver.check()
    response = {'result': str(result), 'seconds': time.monotonic()-start,
                'query': str(path), 'command': f'z3 {path}'}
    if result == z3.sat:
        response['countermodel'] = str(solver.model())
    elif result == z3.unknown:
        response['reason'] = solver.reason_unknown()
    return response


def local_checks(records):
    for r in records:
        alpha = check_lp(r)
        for field in ('minimum_expansion', 'contrast_at_minimum', 'expansion_at_maximum_contrast'):
            check_witness(r, r[field])
        m = r['minimum_expansion']['m']
        assert r['contrast_at_minimum']['m'] == m
        best = r['expansion_at_maximum_contrast']
        assert F(best['gap'], best['m']) == alpha
        assert F(r['contrast_at_minimum']['gap'], m) <= alpha


def negative_controls(records, max_n):
    passed = []
    for mutation in ('dual', 'column', 'objective', 'coverage'):
        bad = deepcopy(records)
        if mutation == 'dual':
            bad[0]['lp']['dual_equality'][0] = '12345'
        elif mutation == 'column':
            bad[0]['minimum_expansion']['white'][0] += 1
        elif mutation == 'objective':
            bad[0]['expansion_at_maximum_contrast']['gap'] += 1
        else:
            bad.pop()
        try:
            if mutation == 'coverage':
                verify_coverage(bad, max_n)
            else:
                local_checks(bad)
        except AssertionError:
            passed.append(mutation)
        else:
            raise AssertionError(f'Negative control accepted: {mutation}')
    return passed


def verify(data, directory, timeout):
    records = data['records']
    max_n = max(r['n'] for r in records)
    counts = verify_coverage(records, max_n)
    local_checks(records)
    negative = negative_controls(records, max_n)
    outcomes = []
    for r in records:
        alpha = F(r['lp']['alpha'])
        cheap = cheap_bounds(r, alpha)
        results = {}
        for mode, proven in cheap.items():
            results[mode] = {'result': 'exact-bound', 'kind': 'LP plus integrality/divisibility'} if proven else integer_obligation(r, alpha, mode, directory, timeout)
        outcomes.append({'id': r['id'], 'obligations': results,
                         'collection_minimum_certified': cheap['minimum'],
                         'collection_fixed_gap_certified': cheap['minimum'] and cheap['fixed_gap'],
                         'collection_at_alpha_certified': cheap['at_alpha']})
        if not all(x['result'] in ('unsat', 'exact-bound') for x in results.values()):
            print('UNRESOLVED', r['id'], results, flush=True)
    certified = all(x['result'] in ('unsat', 'exact-bound') for o in outcomes for x in o['obligations'].values())
    return {'schema': 'vcs-independent-verification-1', 'command': ' '.join(sys.argv),
            'python': platform.python_version(), 'z3': z3.get_version_string(),
            'certified': certified, 'coverage': counts, 'negative_controls_rejected': negative,
            'exact_lp_certificates': len(records), 'integer_witnesses': 3*len(records),
            'outcomes': outcomes}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--queries', type=Path, required=True)
    p.add_argument('--timeout', type=int, default=60)
    args = p.parse_args()
    args.queries.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    result = verify(json.loads(args.input.read_text()), args.queries, args.timeout)
    result['seconds'] = time.monotonic() - started
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'outcomes'}, indent=2))
    sys.exit(0 if result['certified'] else 1)
