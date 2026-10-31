#!/usr/bin/env python3
"""Exact rational check of the (1,1,n) source, full ideal and lowering formulas.

This bounded experiment checks, rather than proves, selected r,s,n values.
The companion written proof carries all positive integer quantifiers.
"""
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lift_exact', ROOT / 'frontier-20261028-lift-exact.py')
lift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lift)


def ad3(letter, n):
    v = lift.letter(letter)
    for _ in range(n):
        v = lift.bracket(lift.letter(3), v)
    return v


def chain(n):
    return [lift.bracket(ad3(1, k), ad3(2, n - k)) for k in range(n + 1)]


def plus(*terms):
    out = {}
    for scalar, vector in terms:
        for w, c in vector.items():
            out[w] = out.get(w, Fraction(0)) + scalar * c
    return {w: c for w, c in out.items() if c}


def span(vectors):
    result = lift.Span()
    for v in vectors:
        result.add(v)
    return result


def same_span(a, b):
    return len(a) == len(b) and all(not b.reduce(v) for v in a.rows.values())


def actual_ideal_at(spaces, degree):
    return spaces.get(tuple(degree), lift.Span())


def verify_case(n, r, s):
    matrix = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    degree = (1, 1, n)
    v = chain(n)
    u = chain(n - 1)
    source = span(v)
    assert len(source) == n + 1
    assert same_span(source, span([x for _, x in lift.lie_basis(degree)]))
    actual = lift.ideal_bases(degree, matrix)
    ideal = actual_ideal_at(actual, degree)
    predicted = span([v[k] for k in range(n + 1) if k >= r + 1 or n - k >= s + 1])
    assert same_span(ideal, predicted), ('source ideal', n, r, s)
    target3 = actual_ideal_at(actual, (1, 1, n - 1))
    predicted3 = span([u[k] for k in range(n) if k >= r + 1 or n - 1 - k >= s + 1])
    assert same_span(target3, predicted3), ('target3 ideal', n, r, s)
    target1 = actual_ideal_at(actual, (0, 1, n))
    assert len(target1) == (1 if s < n else 0)
    for k in range(n + 1):
        expected3 = plus(
            (k * (r - k + 1), u[k - 1] if k > 0 else {}),
            ((n - k) * (s - n + k + 1), u[k] if k < n else {}),
        )
        assert lift.clean(lift.lowering(v[k], 2, matrix)) == lift.clean(expected3), ('f3', n, r, s, k)
        expected1 = plus((n + 1 if k == 0 else -1 if k == 1 else 0, ad3(2, n)))
        assert lift.clean(lift.lowering(v[k], 0, matrix)) == lift.clean(expected1), ('f1', n, r, s, k)
        expected2 = plus((1 if k == n - 1 else -(n + 1) if k == n else 0, ad3(1, n)))
        assert lift.clean(lift.lowering(v[k], 1, matrix)) == lift.clean(expected2), ('f2', n, r, s, k)
    result = lift.run_case(degree, r, s)
    assert result['lift_obstruction_dim'] == 0, result
    assert result['quotient_kernel_dim'] == 0, result
    return {
        'n': n, 'r': r, 's': s,
        'source_dim': result['source_dim'],
        'ideal_dim': result['ideal_dim'],
        'target_ideal_dim': result['target_ideal_dim'],
        'delta_ideal_rank': result['delta_ideal_rank'],
        'lift_obstruction_dim': result['lift_obstruction_dim'],
        'quotient_kernel_dim': result['quotient_kernel_dim'],
    }


def main():
    # Fixed, bounded audit: no claim that these checks replace the all-n proof.
    results = [verify_case(n, r, s) for n in range(1, 5)
               for r in range(1, 7) for s in range(1, 7)]
    path = ROOT / 'frontier-20261028-chain-check-results-v1.json'
    if path.exists():
        raise FileExistsError(f'refusing to overwrite {path}')
    report = {
        'method': 'exact fractions; direct bracket-word identities and full six-seed ideal generation compared against analytic spans',
        'tested_ranges': {'n': [1, 4], 'r': [1, 6], 's': [1, 6]},
        'tested_case_count': len(results),
        'all_source_and_target_spans_and_lowering_identities_verified': True,
        'all_tested_lift_obstructions_and_quotient_kernels_zero': True,
        'not_a_proof_for_unbounded_parameters': True,
        'cases': results,
    }
    path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(results)} exact cases; source/ideal/lowering identities and both obstruction dimensions; {path.name}')


if __name__ == '__main__':
    main()
