#!/usr/bin/env python3
"""Independent finite arithmetic controls for f248; stdlib only, no source imports."""
from collections import Counter
from itertools import combinations, product
from math import prod
import json


def ch(a, b):
    return -1 if (a & b).bit_count() % 2 else 1


def hadamard(values):
    return tuple(sum(values[x] * ch(s, x) for x in range(len(values)))
                 for s in range(len(values)))


def classify(b):
    w = sum(x != 0 for x in b)
    a = tuple(abs(x) for x in hadamard(b))
    if w == 0:
        assert a == (0, 0, 0, 0)
        return 'O'
    if w == 1:
        assert a == (1, 1, 1, 1)
        return 'F'
    if w == 2:
        if a[0] == 2:
            j = a.index(2, 1)
            assert sorted(a) == [0, 0, 2, 2]
            return f'C{j}'
        j = a.index(0, 1)
        assert a[0] == 0 and sorted(a) == [0, 0, 2, 2]
        return f'D{j}'
    if w == 3:
        assert sorted(a) == [1, 1, 1, 3]
        return 'B' if a[0] == 3 else f'A{a.index(3)}'
    assert w == 4
    if a == (2, 2, 2, 2):
        return 'E'
    assert sorted(a) == [0, 0, 0, 4]
    return 'H' if a[0] == 4 else f'G{a.index(4)}'


def sign_data(points, signs):
    patterns = [tuple(signs[i] * ch(p, x) for i, p in enumerate(points))
                for x in range(64)]
    ratios = Counter(tuple(a * pattern[0] for a in pattern[1:])
                     for pattern in patterns)
    t = tuple(map(sum, patterns))
    return patterns, ratios, t


def expected_reject(label, predicate):
    try:
        assert predicate
    except AssertionError:
        return label
    raise RuntimeError('negative did not fail for intended reason: ' + label)


blocks = Counter(classify(b) for b in product((-1, 0, 1), repeat=4))
expected_blocks = {'O': 1, 'F': 8, 'B': 8, 'E': 8, 'H': 2}
for j in (1, 2, 3):
    expected_blocks.update({f'A{j}': 8, f'C{j}': 4,
                            f'D{j}': 4, f'G{j}': 2})
assert blocks == expected_blocks and sum(blocks.values()) == 81

r5 = [0, 1, 2, 4, 8, 16]
r4w4 = [0, 1, 2, 3, 4, 8]
r4w6 = [0, 1, 2, 4, 8, 15]
rank5_hist, rank4_hist = Counter(), Counter()
for signs in product((-1, 1), repeat=6):
    for shift in (0, 32):
        pat, rat, t = sign_data([p ^ shift for p in r5], signs)
        assert len(rat) == 32 and set(rat.values()) == {2}
        rank5_hist[str(sum(v % 3 == 0 for v in t))] += 1
    for weight, points, relation in ((4, r4w4, (0, 1, 2, 3)),
                                     (6, r4w6, tuple(range(6)))):
        syndrome = 0 if prod(signs[i] for i in relation) == 1 else 1
        for shift in (0, 16):
            pat, rat, t = sign_data([p ^ shift for p in points], signs)
            assert len(rat) == 16 and set(rat.values()) == {4}
            raw = Counter(pat)
            assert (len(raw), set(raw.values())) == ((16, {4}) if shift == 0 else (32, {2}))
            n = sum(v % 3 == 0 for v in t)
            want = {(4, 0): 28, (4, 1): 16,
                    (6, 0): 4, (6, 1): 40}[weight, syndrome]
            assert n == want
            rank4_hist[f'w{weight}_syndrome{syndrome}_N{n}'] += 1
            if weight == 6 and syndrome == 1:
                assert Counter(abs(v) for v in t) == {0: 40, 4: 24}

# Rank-three supports exhaust all six-point subsets of an affine 3-space
# and all signs. Each value has multiplicity eight on the ambient six-space.
r3_hist = Counter()
r3_n40_shapes = Counter()
for support in combinations(range(8), 6):
    for signs in product((-1, 1), repeat=6):
        v = [0] * 8
        for i, p in enumerate(support):
            v[p] = signs[i]
        w = hadamard(v)
        assert sum(z * z for z in w) == 48
        assert all(z % 2 == 0 and abs(z) <= 6 for z in w)
        n = 8 * sum(z % 3 == 0 for z in w)
        r3_hist[str(n)] += 1
        if n == 40:
            shape = tuple(sorted(Counter(abs(z) for z in w).items()))
            r3_n40_shapes[str(shape)] += 1
            assert Counter(abs(z) for z in w) == {0: 4, 2: 3, 6: 1}

# The excluded no-|6| alternative: for every choice of three frequencies
# and signs of their coefficients, the inverse is nonintegral everywhere.
inverse_half_integer_cases = 0
for positions in combinations(range(8), 3):
    for signs in product((-1, 1), repeat=3):
        for x in range(8):
            numerator = sum(4 * signs[i] * ch(s, x)
                            for i, s in enumerate(positions))
            assert numerator % 8 == 4
            inverse_half_integer_cases += 1

# Independently enumerate scalar class equations rather than evaluating (5).
triples = set()
for y in (1, 3):
    for h in range(3):
        for c2 in range(11):
            c3 = 10 - 4 * h - c2
            d1 = 29 - 4 * y - c2
            if min(c3, d1) < 0:
                continue
            for g in range(65):
                o = 48 - c2 - c3 - d1 - y - g - h
                if o < 0:
                    continue
                weight = 48 + 2 * (c2 + c3 + d1) + 4 * (y + g + h)
                u3sq = 16 + 4 * (c3 + d1) + 16 * g
                if weight == 114 and u3sq == 124:
                    assert (c3, c2, d1, o) == (
                        4 + 2*y - 2*g - 2*h,
                        6 - 2*y + 2*g - 2*h,
                        23 - 2*y - 2*g + 2*h,
                        15 + y + g + h)
                    triples.add((y, g, h))
expected = {
    (1,0,0),(1,1,0),(1,2,0),(1,3,0),(1,0,1),(1,1,1),(1,2,1),(1,0,2),(1,1,2),
    (3,0,0),(3,1,0),(3,1,1),(3,2,0),(3,2,1),(3,2,2),
    (3,3,0),(3,3,1),(3,3,2),(3,4,0),(3,4,1),(3,5,0),
}
assert triples == expected and len(triples) == 21

# Arithmetic product controls use only congruence and the y=7 magnitudes.
rank4_product = 16*4 - 8 + 7*16
rank3_product = 16*(-2) + 4 + 7*(-8)
assert rank4_product == 168 and rank3_product == -84
assert r3_n40_shapes

# Each false proposition is rejected for the named, inspected reason.
pat0, rat0, _ = sign_data(r4w4, (1,) * 6)
rejected = [
    expected_reject('five independent rank-four ratios: observed 16, not 32', len(rat0) == 32),
    expected_reject('individual raw patterns twice: fixed-base witness occurs four times', set(Counter(pat0).values()) == {2}),
    expected_reject('N=34 at ranks 3,4,5: absent from all exact histograms',
                    '34' in r3_hist or '34' in rank5_hist or
                    any(k.endswith('_N34') for k in rank4_hist)),
    expected_reject('y=7 weight-six branch equals signed identity 24: actual 168', rank4_product == 24),
    expected_reject('y=7 rank-three branch equals signed identity 24: actual -84', rank3_product == 24),
    expected_reject('extra (3,0,1) class triple: violates nonnegative C2', (3,0,1) in triples),
    expected_reject('omitting (1,0,0) preserves the literal list', triples - {(1,0,0)} == expected),
]

print(json.dumps({'block_shapes': dict(sorted(blocks.items())),
                  'rank5_counts': dict(rank5_hist),
                  'rank4_counts': dict(sorted(rank4_hist.items())),
                  'rank3_counts': dict(sorted(r3_hist.items(), key=lambda x: int(x[0]))),
                  'rank3_N40_shapes': dict(r3_n40_shapes),
                  'rank3_no_six_half_integer_checks': inverse_half_integer_cases,
                  'class_triples': sorted(triples),
                  'y7_products': {'rank4': rank4_product, 'rank3': rank3_product, 'identity': 24},
                  'intended_reason_negatives': rejected}, sort_keys=True, indent=2))
