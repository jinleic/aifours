#!/usr/bin/env python3
"""Exhaust the exact necessary correction-parity coset for source96/normal511."""
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]


def canonical(m):
    return m if m % 8 == 2 else -m


def affine_space(equations, n):
    # Highest-bit pivots, augmented right-hand side kept separately.
    pivots = {}
    for left, right in equations:
        for p in sorted(pivots, reverse=True):
            if left >> p & 1:
                v, r = pivots[p]
                left ^= v
                right ^= r
        if left == 0:
            assert right == 0, 'inconsistent affine system'
            continue
        p = left.bit_length() - 1
        for q, (v, r) in list(pivots.items()):
            if v >> p & 1:
                pivots[q] = (v ^ left, r ^ right)
        pivots[p] = (left, right)
    particular = sum(right << p for p, (left, right) in pivots.items())
    basis = []
    for f in range(n):
        if f in pivots:
            continue
        v = 1 << f
        for p, (left, right) in pivots.items():
            if left >> f & 1:
                v |= 1 << p
        basis.append(v)
    return len(pivots), particular, basis


def main():
    started = time.monotonic()
    raw = (ROOT / 'results/screen.json.gz').read_bytes()
    screen = json.loads(gzip.decompress(raw))
    remaining = [r for r in screen['classes'] if r['class_stage'] == 'UNKNOWN']
    assert len(remaining) == 1
    case = remaining[0]
    assert (case['source'], case['normal']) == (96, 511)
    qs = [q for q in case['quadratic_candidates'] if q['rejected_by'] is None]
    assert len(qs) == 1
    q = qs[0]
    assert q['coefficient_mask'] == 7887107311
    m0 = q['maxima']
    A = q['canonical_maximum_inverse']
    assert all(v % 16 == 0 for v in A)
    budget = (q['square_capacity'] - 65536) // 64
    assert budget == 56
    domains = []
    for upper, domain in zip(m0, q['magnitude_domains']):
        allowed = []
        for m in domain:
            assert (canonical(upper) - canonical(m)) % 16 == 0
            assert (upper * upper - m * m) % 64 == 0
            allowed.append(((canonical(upper) - canonical(m)) // 16, (upper * upper - m * m) // 64, m))
        domains.append(allowed)
    active = [a for a, domain in enumerate(domains) if len(domain) > 1]
    assert len(active) == 166
    assert all(domain == [(0, 0, 2)] for a, domain in enumerate(domains) if a not in active)
    r = [v // 16 - 16 for v in A]
    # Integer Boolean-cube Moebius differences in the inverse input index.
    coefficients = r.copy()
    step = 1
    while step < 256:
        for start in range(0, 256, 2 * step):
            for j in range(step):
                coefficients[start + step + j] -= coefficients[start + j]
        step *= 2
    equations = []
    moments = []
    for s in range(256):
        if s.bit_count() > 4:
            continue
        factor = (-2) ** s.bit_count()
        assert coefficients[s] % factor == 0
        rhs = (coefficients[s] // factor) % 2
        left = sum(1 << i for i, a in enumerate(active) if a & s == s)
        equations.append((left, rhs))
        moments.append({'subset': s, 'mixed_difference': coefficients[s], 'factor': factor, 'parity_rhs': rhs})
    assert len(equations) == 163
    rank, particular, basis = affine_space(equations, len(active))
    assert rank == 147 and len(basis) == 19
    for left, right in equations:
        assert (left & particular).bit_count() % 2 == right
        assert all((left & v).bit_count() % 2 == 0 for v in basis)
    # Each parity-one entry has a local minimum unavoidable energy deficit.
    costs = [min(d for e, d, m in domains[a] if e % 2) for a in active]
    weights = sorted(set(costs))
    masks = {w: sum(1 << i for i, cost in enumerate(costs) if cost == w) for w in weights}
    histogram = Counter()
    least = 10 ** 9
    least_word = None
    word = particular
    for index in range(1 << len(basis)):
        if index:
            bit = (index & -index).bit_length() - 1
            word ^= basis[bit]
        cost = sum(w * (word & mask).bit_count() for w, mask in masks.items())
        histogram[cost] += 1
        if cost < least:
            least, least_word = cost, word
    assert sum(histogram.values()) == 524288 and least == 140 and least > budget
    out = {'status': 'EXCLUDED', 'source': 96, 'normal': 511,
           'screen_sha256': hashlib.sha256(raw).hexdigest(),
           'quadratic_coefficient_mask': q['coefficient_mask'], 'energy_deficit_budget': budget,
           'active_spectral_indices': active, 'local_e_d_m_domains': domains,
           'moment_equations': moments, 'affine_rank': rank,
           'affine_particular': str(particular), 'affine_kernel_basis': [str(v) for v in basis],
           'affine_dimension': len(basis), 'enumerated_parities': sum(histogram.values()),
           'minimum_forced_deficit': least, 'minimum_word': str(least_word),
           'cost_histogram': dict(sorted(histogram.items())),
           'elapsed_seconds': time.monotonic() - started,
           'scope': 'No odd complementary 8-variable half with |G|+|H|<=28; zero condition was not needed.'}
    (ROOT / 'results/final-parity.json').write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps({k: out[k] for k in ('status', 'affine_rank', 'affine_dimension', 'enumerated_parities', 'energy_deficit_budget', 'minimum_forced_deficit', 'elapsed_seconds')}, sort_keys=True))


if __name__ == '__main__':
    main()
