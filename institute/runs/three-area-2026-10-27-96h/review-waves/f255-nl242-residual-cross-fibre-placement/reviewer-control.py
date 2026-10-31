#!/usr/bin/env python3
"""Reviewer-owned exact controls for the frozen f255 cross-fibre scope."""
import hashlib
import itertools
import os
import subprocess
import time
from collections import Counter


def native_clock():
    return subprocess.run(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def xor_all(values):
    out = 0
    for value in values:
        out ^= value
    return out


def intersection_size(support, translate, target):
    return sum((x ^ translate) in target for x in support)


def aligned_flat(support, negatives):
    result = []
    for c in range(64):
        signs = [(-1 if x in negatives else 1) * (-1 if parity[x & c] else 1)
                 for x in support]
        if len(set(signs)) == 1:
            result.append(c)
    return set(result)


def mismatch(negative2, negative3, t):
    shifted2 = {x ^ t for x in negative2}
    return len(negative3) - len(shifted2), xor_all(shifted2 ^ negative3)


start = time.monotonic()
print('native_start:', native_clock(), flush=True)
with open(os.path.realpath(__file__), 'rb') as source:
    print('reviewer_control_sha256:', hashlib.sha256(source.read()).hexdigest(), flush=True)

# Atom coordinates are p,q,b1,b2,b3,b4 (low to high bit). Block coordinates
# use the dual basis with the same bit order; H* is even parity in bits 2..5.
parity = [bin(x).count('1') % 2 for x in range(64)]
weight4 = [bin(x).count('1') for x in range(16)]
A3 = {0, 1, 2, 3, 4, 8, 16, 32}
outer = {4, 8, 16, 32}
n = xor_all(A3)
d = 60
B = {c for c in range(64)
     if ((c & 3) != 0 and weight4[c >> 2] == 2)
     or ((c & 3) == 0 and weight4[c >> 2] in (1, 4))}
H = {c for c in range(64) if parity[c & d] == 0}
require(n == 60 and len(B) == 23 and len(B & H) == 19, 'B3 normal form')

# All nontrivial characters and all affine hyperplanes.
coefficients = {}
hyperplanes = []
for normal in range(1, 64):
    coef = sum(-1 if parity[normal & c] else 1 for c in B)
    coefficients[normal] = coef
    for bit in (0, 1):
        occupancy = sum(parity[normal & c] == bit for c in B)
        hyperplanes.append((normal, bit, occupancy))
require([(a, v) for a, v in coefficients.items() if abs(v) >= 11] == [(d, 15)],
        'unique large Fourier coefficient')
require([(a, b) for a, b, k in hyperplanes if k >= 17] == [(d, 0)],
        'unique hyperplane with at least 17 points')
require(max(k for _, _, k in hyperplanes) == 19, 'maximum hyperplane occupancy')

# Every affine three-flat of H*: classify all intersections, including the
# crucial asserted two-point direction and nonexistence of a disjoint flat.
directions = set()
nonzero_h = sorted(H - {0})
for basis in itertools.combinations(nonzero_h, 3):
    span = {0}
    for vector in basis:
        span |= {x ^ vector for x in tuple(span)}
    if len(span) == 8:
        directions.add(tuple(sorted(span)))
require(len(directions) == 155, 'number of three-dimensional directions in H*')
flats = {tuple(sorted(a ^ x for x in direction))
         for direction in directions for a in H}
require(len(flats) == 620, 'number of affine three-flats in H*')
flat_histogram = Counter()
for flat in flats:
    hit = set(flat) & B
    flat_histogram[len(hit)] += 1
    require(len(hit) != 0, 'unexpected B3-disjoint flat in H*')
    if len(hit) == 2:
        require(xor_all(hit) == d, 'two-point intersection direction')

# Exhaust every four-point support of XOR n, all signs with product +1, and
# all translations of those supports admitting |F2 intersect B3|=2. Global
# sign flips preserve F2, so four even ratio patterns represent eight signs.
support_count = qualified_supports = qualified_signings = 0
ratio_patterns = (0, 3, 5, 6)
max_overlap = 0
for x, y, z in itertools.combinations(range(64), 3):
    w = x ^ y ^ z ^ n
    if w <= z:
        continue
    support = (x, y, z, w)
    support_count += 1
    bins = [0] * 8
    for c in B:
        pattern = (parity[(y ^ x) & c]
                   | (parity[(z ^ x) & c] << 1)
                   | (parity[(w ^ x) & c] << 2))
        bins[pattern] += 1
    qualifying = sum(bins[pattern] == 2 for pattern in ratio_patterns)
    if qualifying:
        qualified_supports += 1
        qualified_signings += 2 * qualifying
        local_max = max(intersection_size(support, t, A3) for t in range(64))
        max_overlap = max(max_overlap, local_max)
        require(local_max <= 2, 'counterexample to all-translation intersection bound: '
                + repr(support))
require(support_count == 9920 and qualified_supports > 0 and max_overlap == 2,
        'complete support enumeration or nonvacuity')

# The author's specific formal placement and all 64 sign translations.
A2 = (0, 1, 14, 51)
negative2 = {14, 51, 4, 57}
F2 = aligned_flat(A2, negative2)
require(xor_all(A2) == n and len(set(A2) & A3) == 2, 'formal support XOR/overlap')
require(len(set(A2) & negative2) == 2 and len(F2) == 8, 'formal signs/rank')
require(F2 <= H and F2 & B == {14, 50}, 'formal F2 intersection')
require(max(intersection_size(A2, t, A3) for t in range(64)) == 2,
        'formal all-translation intersection bound')
require(all(mismatch(negative2, set(), t) == (-4, 0) for t in range(64)),
        'formal all-translation mismatch condition')
w2_zero = 64 - 2 * len(negative2)
t2_zero = sum(-1 if x in negative2 else 1 for x in A2)
w3_zero, t3_zero = 64, 8
require((w2_zero, t2_zero, w3_zero, t3_zero) == (56, 0, 64, 8),
        'formal transform values at zero')
require((3 * w2_zero - 2 * t2_zero) % 16 != 0
        and (3 * w3_zero - 2 * t3_zero) // 16 == 11,
        'formal local ternary failures')

# Intended-reason negatives: these are deliberately outside the complete
# hypotheses, never counterexamples to the conditional theorem.
outer_flat = aligned_flat(tuple(sorted(outer)), set())
require(len(outer & A3) == 4 and len(outer_flat & B) == 1,
        'negative: outer complement must fail the two-point F2 premise')
plane = (0, 1, 2, 3)
require(xor_all(plane) == 0 and len(aligned_flat(plane, set())) == 16,
        'negative: affine-rank-two plane must fail rank/nonzero XOR')
odd_outer_flat = aligned_flat(tuple(sorted(outer)), {4})
require(all(c not in H for c in odd_outer_flat),
        'negative: odd atom-sign product must land outside H*')
shifted_outer = tuple(x ^ 1 for x in sorted(outer))
require(intersection_size(shifted_outer, 0, A3) == 0
        and intersection_size(shifted_outer, 1, A3) == 4,
        'negative: unshifted overlap alone does not imply all translations')
require(mismatch({1, 2, 3}, set(), 0) == (-3, 0),
        'negative: mod-4 sum must fail independently of XOR')
require(mismatch({0, 1, 2, 4}, set(), 0) == (-4, 7),
        'negative: XOR must fail independently of mod-4 sum')
require(mismatch({0}, {0}, 0) == (0, 0)
        and mismatch({0}, {0}, 1) == (0, 1),
        'negative: t=0 mismatch does not imply all translations')

print('B3/hyperplanes: 23 points; 63 characters; 126 affine hyperplanes; unique >=17 H*', flush=True)
print('H* affine three-flats:', len(flats), 'intersection histogram:', dict(sorted(flat_histogram.items())), flush=True)
print('four-atom supports:', support_count, 'qualified supports:', qualified_supports,
      'qualified signed supports:', qualified_signings, 'max translated overlap:', max_overlap, flush=True)
print('formal example: F2∩B3={14,50}; 64 translations pass C and S; U2=21/2, U3=11', flush=True)
print('seven intended-reason negatives: passed', flush=True)
print('native_end:', native_clock(), flush=True)
print('elapsed_monotonic_seconds:', round(time.monotonic() - start, 6), flush=True)
