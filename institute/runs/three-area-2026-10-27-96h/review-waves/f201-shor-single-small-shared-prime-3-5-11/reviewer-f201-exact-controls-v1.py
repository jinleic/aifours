#!/usr/bin/env python3
"""Independent exact finite controls for f201; not a universal proof."""
from collections import deque
from fractions import Fraction
from functools import cache
from itertools import combinations
from math import gcd, isqrt


def divisors(n):
    return sorted({d for k in range(1, isqrt(n) + 1) if n % k == 0 for d in (k, n // k)})


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def divmonic(a, b):
    a = trim(list(a))
    assert b and b[-1] == 1
    q = [0] * max(0, len(a) - len(b) + 1)
    nz = [(j, v) for j, v in enumerate(b) if v]
    for k in range(len(q) - 1, -1, -1):
        c = a[k + len(b) - 1]
        q[k] = c
        if c:
            for j, v in nz:
                a[k + j] -= c * v
    return trim(q), trim(a)


def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    nz = [(j, y) for j, y in enumerate(b) if y]
    for i, x in enumerate(a):
        if x:
            for j, y in nz:
                r[i + j] += x * y
    return trim(r)


@cache
def cyclo(n):
    f = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n)[:-1]:
        f, rem = divmonic(f, cyclo(d))
        assert not rem
    return tuple(f)


def substituted(f, k):
    ans = [0] * ((len(f) - 1) * k + 1)
    for i, c in enumerate(f):
        ans[i * k] = c
    return ans


def tiles(a, b, n):
    if len(a) * len(b) != n:
        return False
    mask = 0
    for x in a:
        for y in b:
            bit = 1 << ((x + y) % n)
            if mask & bit:
                return False
            mask |= bit
    return mask == (1 << n) - 1


def divisorgcds(a, n):
    return {gcd(x - y, n) for x in a for y in a}


def bfs(r, steps):
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for d in steps:
            v = (u + d) % r
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


# Exhaustive small tilings: validate the group-ring dilation mechanism and
# divisor exclusion, including multipliers noninvertible modulo n.
tiling_count = dilation_count = nonunit_dilation_count = 0
for n in (6, 8, 10, 12):
    for k in divisors(n):
        for a in combinations(range(n), k):
            for b in combinations(range(n), n // k):
                if not tiles(a, b, n):
                    continue
                tiling_count += 1
                assert divisorgcds(a, n) & divisorgcds(b, n) == {n}
                for t in range(1, n + 1):
                    if gcd(t, k) != 1:
                        continue
                    dilation_count += 1
                    nonunit_dilation_count += gcd(t, n) != 1
                    ta = {(t * x) % n for x in a}
                    assert len(ta) == k and tiles(ta, b, n)
assert tiling_count and nonunit_dilation_count
assert tiles({0, 1}, {0, 2, 4}, 6)
assert not tiles({0, 2}, {0, 2, 4}, 6)  # t=2 shares |A|=2.
assert not tiles({0, 1}, {0, 1}, 4)
assert 1 in divisorgcds({0, 1}, 4) & divisorgcds({0, 1}, 4)
print('tilings', tiling_count, 'dilations', dilation_count,
      'nonunit_mod_n_dilations', nonunit_dilation_count,
      'intended_negatives', 2)


# R3 arithmetic over all odd x for the stated finite modulus grid.
witnesses = moduli = 0
for p, q1, q2 in ((3, 5, 11), (5, 3, 11), (11, 3, 5)):
    for r in (q1 * q2, q1 * q1 * q2, q1 * q2 * 13):
        for v in (2, 3):
            for K in (1, 2):
                n = (2 ** K) * (p ** v) * r
                moduli += 1
                for x in range(1, n, 2):
                    if x % q1 and x % q2:
                        continue
                    if x % (p * p) == 0:
                        continue
                    g = gcd(x, n)
                    ell = (q1 if x % q1 == 0 else q2) if x % p else p
                    assert g % ell == 0
                    t = g // ell
                    assert g < n and gcd(t, p * (2 ** K)) == 1
                    assert gcd(t * ell, n) == g
                    witnesses += 1
# The same recipe must not claim an admissible witness when p^2 divides x.
p, q1, q2, r, n, x = 3, 5, 11, 55, 990, 495
g = gcd(x, n)
assert x % (p * p) == 0
assert all(gcd(g // ell, p * 2) != 1 for ell in (p, q1, q2))
print('R3_moduli', moduli, 'odd_difference_witnesses', witnesses,
      'intended_p_squared_negative', 1)


# Exact cardinality of a p^2-coset relative to a putative constant fibre.
cardinality_count = 0
for p in (3, 5, 11):
    for v in range(2, 7):
        for a in range(9):
            for b in range(5):
                ratio = Fraction(p ** (v - 2) * 2 ** (a + b),
                                 p ** (v - 1) * 2 ** b)
                assert ratio == Fraction(2 ** a, p) and ratio.denominator == p
                cardinality_count += 1
# Omitting one p from the fibre count makes the ratio integral, so the
# denominator conclusion cannot be transferred to that different count.
assert Fraction(3 ** 0 * 2 ** 4, 3 ** 0 * 2 ** 1).denominator == 1
print('coset_ratios', cardinality_count, 'wrong_fibre_size_negative', 1)


# Monic integer cyclotomic computations, without external algebra packages.
identities = 0
for p, r in ((3, 55), (5, 33), (11, 15)):
    for s in (p, p * p):
        product = [1]
        for m in divisors(r):
            product = mul(product, cyclo(s * m))
        assert product == substituted(cyclo(s), r)
        identities += 1
# gcd(s,R)=1 is essential: product_{m|3} Phi_{3m} != Phi_3(X^3).
assert mul(cyclo(3), cyclo(9)) != substituted(cyclo(3), 3)
nonzero_remainders = 0
for p in (3, 5, 11):
    for s in (p, p * p):
        for d in (0, 1, p * p - 1):
            f = [0] * (d + 3 * p * p + 1)
            for k in (0, 1, 3):
                f[d + k * p * p] += 1
            assert divmonic(f, cyclo(s))[1]
            nonzero_remainders += 1
        assert not divmonic([], cyclo(s))[1]  # zero weight is different.
print('cyclotomic_identities', identities, 'constant_fibre_remainders',
      nonzero_remainders, 'coprimality_and_empty_negatives', 2)


# Construct six unanchored tilings, independently exercising both choices of s.
# Check actual masks, all m|R, and each fibre; do not infer anchored existence.
examples = fibres = 0
for p, r in ((3, 55), (5, 33), (11, 15)):
    n = 2 * p * p * r
    for s in (p, p * p):
        if s == p:
            a = {p * j for j in range(p)}
            b = {i + p * p * k for i in range(p) for k in range(n // (p * p))}
        else:
            a = set(range(p))
            b = {p * k for k in range(n // p)}
        assert tiles(a, b, n)
        assert not ({0, 3, 8, 11} <= a and {0, 1, 7, 13, 14} <= b)
        mask = [int(x in b) for x in range(n)]
        for m in divisors(r):
            assert not divmonic(mask, cyclo(s * m))[1]
        for u in range(r):
            bu = [x for x in b if x % r == u]
            assert len(bu) == 2 * p
            assert {x % 2 for x in bu} == {0, 1}
            assert len({x % (p * p) for x in bu}) > 1
            f = [0] * (n // r)
            for x in bu:
                f[(x - u) // r] += 1
            assert not divmonic(f, cyclo(s))[1]
            fibres += 1
        examples += 1
# Removing one term from Phi_3 breaks that fibre's divisibility.
assert divmonic([1, 1], cyclo(3))[1]
print('unanchored_tilings', examples, 'fibre_checks', fibres,
      'deleted_term_negative', 1)


# Connectivity, and the negative control where one generator is omitted.
graphs = 0
for q1, q2 in ((5, 11), (3, 11), (3, 5)):
    for r in (q1 * q2, q1 * q1 * q2, q1 * q2 * 13):
        assert len(bfs(r, (q1, q2))) == r
        graphs += 1
    assert len(bfs(q1 * q2, (q1,))) < q1 * q2
# Exhaust all nontrivial partitions of the smallest graph.
r, q1, q2 = 15, 3, 5
partitions = 0
for mask in range(1, (1 << r) - 1):
    assert any(((mask >> u) & 1) != ((mask >> ((u + step) % r)) & 1)
               for u in range(r) for step in (q1, q2))
    partitions += 1
print('connected_graphs', graphs, 'nontrivial_partitions', partitions,
      'one_generator_negatives', 3)
print('ALL_EXACT_CONTROLS_COMPLETED')
