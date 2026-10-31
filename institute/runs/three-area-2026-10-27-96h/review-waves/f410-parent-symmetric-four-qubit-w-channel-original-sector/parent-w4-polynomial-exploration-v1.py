#!/usr/bin/env python3
"""Exact finite polynomial exploration for the parent W4 author duty.

This checks spectra conditional on the separately derived block formula. It
never constructs the physical channel and is not an independent verifier.
No file/network/subprocess access. It prints a complete compact JSON receipt.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from time import monotonic
import json
import sys

START = monotonic()
DEADLINE = START + 50.0


def guard():
    if monotonic() > DEADLINE:
        raise TimeoutError('cooperative calculation deadline')


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(*ps):
    out = [F(0)] * max(map(len, ps))
    for p in ps:
        for i, value in enumerate(p):
            out[i] += value
    return trim(out)


def scale(p, scalar):
    return trim([scalar * x for x in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def power(p, n):
    out = (F(1),)
    for _ in range(n):
        out = mul(out, p)
    return out


def value(p, t):
    return sum(c * t ** i for i, c in enumerate(p))


def drop_positive_endpoint_factors(p):
    p = trim(p)
    at_zero = 0
    at_one = 0
    while len(p) > 1 and p[0] == 0:
        p = trim(p[1:])
        at_zero += 1
    while len(p) > 1 and sum(p) == 0:
        q = [p[0]]
        for j in range(1, len(p) - 1):
            q.append(p[j] + q[-1])
        if p[-1] + q[-1] != 0:
            raise ValueError('invalid (1-t) factorization')
        p = trim(q)
        at_one += 1
    return p, at_zero, at_one


def bernstein(p, left, right):
    n = len(p) - 1
    q = [F(0)] * (n + 1)
    width = right - left
    for j in range(n + 1):
        q[j] = sum(p[i] * comb(i, j) * left ** (i - j) * width ** j
                   for i in range(j, n + 1))
    return tuple(sum(q[j] * F(comb(k, j), comb(n, j))
                     for j in range(k + 1)) for k in range(n + 1))


def certify_nonnegative(p, max_depth=12):
    core, z, o = drop_positive_endpoint_factors(p)
    if core == (0,):
        return {'kind': 'identically_zero', 'zero_factor': z, 'one_factor': o}
    intervals = [(F(0), F(1), 0)]
    max_seen = 0
    certified = 0
    while intervals:
        guard()
        left, right, depth = intervals.pop()
        max_seen = max(max_seen, depth)
        bs = bernstein(core, left, right)
        if min(bs) >= 0:
            certified += 1
            continue
        if max(bs) < 0:
            return {'kind': 'negative_interval', 'interval': [str(left), str(right)],
                    'core': list(map(str, core)), 'bernstein': list(map(str, bs))}
        if depth >= max_depth:
            return {'kind': 'unresolved', 'interval': [str(left), str(right)],
                    'core': list(map(str, core)), 'bernstein': list(map(str, bs))}
        middle = (left + right) / 2
        intervals.append((left, middle, depth + 1))
        intervals.append((middle, right, depth + 1))
    return {'kind': 'bernstein_nonnegative', 'zero_factor': z, 'one_factor': o,
            'max_subdivision_depth': max_seen, 'certified_intervals': certified}


def main():
    a, b, t = (F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2)), (F(0), F(1))
    aa, bb, tt, ab = power(a, 2), power(b, 2), power(t, 2), mul(a, b)
    d1 = scale(add(power(a, 4), scale(mul(aa, bb), 3)), F(1, 4))
    d2 = scale(mul(ab, add(aa, bb)), F(1, 2))
    d3 = scale(add(scale(mul(aa, bb), 3), power(b, 4)), F(1, 4))
    g1, g2, g3 = (scale(mul(tt, aa), F(1, 4)),
                   scale(mul(tt, ab), F(1, 4)),
                   scale(mul(tt, bb), F(1, 4)))
    types = [
        ('weight0', mul(power(a, 3), b), 1),
        ('weight1_plus', add(d1, scale(g1, 3)), 1),
        ('weight1_minus', add(d1, scale(g1, -1)), 3),
        ('weight2_plus', add(d2, scale(g2, 4)), 1),
        ('weight2_zero', d2, 3),
        ('weight2_minus', add(d2, scale(g2, -2)), 2),
        ('weight3_plus', add(d3, scale(g3, 3)), 1),
        ('weight3_minus', add(d3, scale(g3, -1)), 3),
        ('weight4', mul(a, power(b, 3)), 1),
    ]
    ref = [power(a, 4)] + [mul(power(a, 3), b)] * 4 + [mul(aa, bb)] * 6 + [mul(a, power(b, 3))] * 4 + [power(b, 4)]
    total = add(*(scale(poly, mult) for _, poly, mult in types))
    if total != (F(1),) or add(*ref) != (F(1),):
        raise ValueError('spectrum trace polynomial mismatch')
    refs = [(F(0),)]
    for item in ref:
        refs.append(add(refs[-1], item))
    polynomials = {}
    combinations_checked = 0
    for counts in product(*(range(mult + 1) for _, _, mult in types)):
        guard()
        k = sum(counts)
        if k == 0:
            candidate = (F(0),)
        else:
            candidate = add(*(scale(poly, count) for (_, poly, _), count in zip(types, counts)))
        gap = add(refs[k], scale(candidate, -1))
        polynomials.setdefault((k, gap), counts)
        combinations_checked += 1
    statuses = Counter()
    unresolved = []
    max_depth = 0
    positive_intervals = 0
    for (k, poly), counts in polynomials.items():
        proof = certify_nonnegative(poly)
        statuses[proof['kind']] += 1
        max_depth = max(max_depth, proof.get('max_subdivision_depth', 0))
        positive_intervals += proof.get('certified_intervals', 0)
        if proof['kind'] not in ('identically_zero', 'bernstein_nonnegative'):
            unresolved.append({'k': k, 'counts': counts, 'gap': list(map(str, poly)), 'proof': proof})
    samples = []
    for t0 in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
        ordered = sorted(((value(poly, t0), name, mult) for name, poly, mult in types), reverse=True)
        samples.append({'t': str(t0), 'ordered_groups': [[name, str(v), mult] for v, name, mult in ordered]})
    result = {
        'kind': 'PARENT_EXACT_FINITE_POLYNOMIAL_EXPLORATION',
        'spectrum_provenance': 'Conditional on parent-derived W4 Hamming-block/Johnson adjacency spectrum; not an independent physical-channel calculation.',
        'types': [{'name': name, 'coefficients_ascending': list(map(str, poly)), 'multiplicity': mult} for name, poly, mult in types],
        'reference_coefficients_ascending': [list(map(str, poly)) for poly in ref],
        'multiset_count_vectors': combinations_checked,
        'distinct_k_gap_polynomials': len(polynomials),
        'exact_gap_certification_counts': dict(statuses),
        'max_bernstein_subdivision_depth': max_depth,
        'certified_intervals': positive_intervals,
        'unresolved_or_negative': unresolved,
        'selected_rational_spectrum_orderings': samples,
        'elapsed_seconds': monotonic() - START,
        'limitations': ['Conditional spectrum only; physical-channel derivation needs independent verification.',
                        'No numerical sampled ordering is a substitute for exact polynomial certificate.',
                        'No unrestricted all-density conclusion, novelty, human or kernel assurance.'],
    }
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    return 0 if not unresolved else 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(json.dumps({'kind': 'ERROR_NOT_PASS', 'type': type(exc).__name__, 'reason': str(exc)}))
        sys.exit(2)
