#!/usr/bin/env python3
"""Reviewer-owned finite arithmetic controls; no author code or inputs imported."""
from functools import lru_cache
from itertools import product
from math import gcd


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def divide_monic(a, b):
    remainder = trim(a)
    b = trim(b)
    assert b[-1] == 1
    quotient = [0] * max(1, len(remainder) - len(b) + 1)
    while len(remainder) >= len(b) and remainder != [0]:
        k = len(remainder) - len(b)
        coefficient = remainder[-1]
        quotient[k] += coefficient
        for j, x in enumerate(b):
            remainder[k + j] -= coefficient * x
        remainder = trim(remainder)
    assert remainder == [0]
    return trim(quotient)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


@lru_cache(None)
def phi(n):
    p = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n)[:-1]:
        p = divide_monic(p, phi(d))
    return tuple(p)


def substitute_power(p, power):
    result = [0] * ((len(p) - 1) * power + 1)
    for i, x in enumerate(p):
        result[i * power] = x
    return trim(result)


def shifted(s, k):
    return frozenset((x + k) % 16 for x in s)


def folded_counts(c, m):
    return [sum(c[r] for r in range(16) if r % m == j) for j in range(m)]


def owns_two_power(c, power):
    modulus = 2 ** power
    counts = folded_counts(c, modulus)
    half = modulus // 2
    return all(counts[j] == counts[j + half] for j in range(half))


# Check the three cyclotomic polynomials independently by exact monic division.
p16, p80, p400 = phi(16), phi(80), phi(400)
rhs = [1] + [0] * 199 + [1]
assert multiply(multiply(p16, p80), p400) == rhs
assert list(p16) == [1] + [0] * 7 + [1]
assert [(i, x) for i, x in enumerate(p80) if x] == [(8 * k, (-1) ** k) for k in range(5)]
assert [(i, x) for i, x in enumerate(p400) if x] == [(40 * k, (-1) ** k) for k in range(5)]
corrupt = list(p80)
corrupt[8] = 1
bad_product = multiply(multiply(p16, corrupt), p400)
assert bad_product != rhs and bad_product[8] == 2
print('cyclotomic 16*80*400 identity exact; negative sign flip gives coefficient x^8=2')

# Sample the fibre-transport identity with nonsquarefree and multiple-prime R.
transport_cases = 0
for i in (2, 3, 4):
    for r in (1, 3, 9, 15, 33):
        lhs = [1]
        for d in divisors(r):
            lhs = multiply(lhs, phi((2 ** i) * d))
        assert lhs == substitute_power(phi(2 ** i), r)
        transport_cases += 1
lhs = multiply(phi(16), phi(32))
assert lhs != substitute_power(phi(16), 2)
print('odd-R transport cases', transport_cases, '; negative even R=2 rejected for extra Phi16')

# Fixed-parity count vectors (entries 0,1,2) satisfying Phi4 and Phi8.
fibre_good = [0, 0]
for parity in (0, 1):
    for v in product(range(3), repeat=8):
        c = [0] * 16
        for r, x in zip(range(parity, 16, 2), v):
            c[r] = x
        if sum(c) and owns_two_power(c, 2) and owns_two_power(c, 3):
            counts8 = folded_counts(c, 8)
            assert len({counts8[r] for r in range(parity, 8, 2)}) == 1
            assert all(counts8[r] > 0 for r in range(parity, 8, 2))
            fibre_good[parity] += 1
bad4 = [0] * 16
bad4[0] = bad4[4] = 1
assert owns_two_power(bad4, 3) and not owns_two_power(bad4, 2)
assert folded_counts(bad4, 8)[2] == 0
bad8 = [0] * 16
bad8[0] = bad8[2] = 1
assert owns_two_power(bad8, 2) and not owns_two_power(bad8, 3)
print('fixed-parity fibre vectors checked', 2 * 3 ** 8, 'nonempty admissible', fibre_good)
print('negative fibres rejected respectively for missing Phi4 and missing Phi8')

# A common bit follows from all five nonempty, distinct mod-5 value supports.
def conflict(masks):
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            if (masks[i] & 1 and masks[j] & 2) or (masks[i] & 2 and masks[j] & 1):
                return (i, j)
    return None

admissible = [m for m in product((1, 2, 3), repeat=5) if conflict(m) is None]
assert admissible == [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2)]
assert conflict((1, 2, 1, 1, 1)) == (0, 1)
assert conflict((3,)) is None
print('five-value bit-support patterns checked', 3 ** 5, 'admissible', len(admissible))
print('negative cross-value opposite bits rejected; one value alone does not force one bit')

# Independently enumerate actual-row pairing from the Phi16 count equation.
paired = 0
for p0, p8, p3, p11 in product(range(0, 16, 2), range(0, 16, 2), range(1, 16, 2), range(1, 16, 2)):
    c = [0] * 16
    for p in (p0, p8, p3, p11):
        c[p] += 1
    if owns_two_power(c, 4):
        assert p8 == (p0 + 8) % 16 and p11 == (p3 + 8) % 16
        paired += 1
assert paired == 64
bad = [0] * 16
for p in (0, 0, 3, 11):
    bad[p] += 1
assert not owns_two_power(bad, 4) and bad[0] != bad[8]
print('labelled head residue tuples checked 4096; Phi16-paired', paired)
print('negative head tuple rejected for unequal residues 0 and 8')

# Check both closure routes in mod16; no author enumerator is used.
def odd_vectors():
    for bits in product((0, 1), repeat=8):
        c = [0] * 16
        for r, x in zip(range(1, 16, 2), bits):
            c[r] = x
        yield c

route_a = route_b = 0
for c in odd_vectors():
    if c[13] and owns_two_power(c, 3) and owns_two_power(c, 4):
        assert c[9]
        route_a += 1
    if c[7] and owns_two_power(c, 2) and owns_two_power(c, 4):
        assert c[9] or c[5]
        route_b += 1
bad = [0] * 16
bad[13] = bad[1] = 1
assert owns_two_power(bad, 3) and not owns_two_power(bad, 4) and not bad[9]
bad = [0] * 16
bad[7] = bad[15] = 1
assert owns_two_power(bad, 4) and not owns_two_power(bad, 2) and not (bad[9] or bad[5])
print('mod16 binary anchor-fibre routes Phi8+Phi16 / Phi4+Phi16', route_a, route_b)
print('negative anchor fibres rejected for missing Phi16 / missing Phi4 respectively')

# List the four precise head/tail residue pairings used in the quotient count.
heads = (0, 3, 8, 11)
def compatible(target_parity, target_mod3):
    return [(p, r) for p in heads for r in range(3)
            if (p % 2 + int(r == 1)) % 2 == target_parity
            and (p + r) % 3 == target_mod3]
expected = {
    (0, 2): [(0, 2), (8, 0)],
    (1, 2): [(3, 2), (11, 0)],
    (0, 0): [(0, 0), (11, 1)],
    (1, 0): [(3, 0), (8, 1)],
}
for target, pairs in expected.items():
    assert compatible(*target) == pairs
print('four projected target pairings', expected)

# All even and odd mod16 transversals, with literal tail anchors.
evens = frozenset(range(0, 16, 2))
odds = frozenset(range(1, 16, 2))
def transversals(parity):
    return [frozenset(u + 8 * bit for u, bit in zip(range(parity, 8, 2), bits))
            for bits in product((0, 1), repeat=4)]

Es, Os = transversals(0), transversals(1)
for E in Es:
    assert E.isdisjoint(shifted(E, 8)) and E | shifted(E, 8) == evens
    assert all(shifted(E, t) != E for t in range(2, 16, 2))
assert shifted(evens, 6) == evens and not evens.isdisjoint(shifted(evens, 8))
for O in Os:
    assert O.isdisjoint(shifted(O, 8)) and O | shifted(O, 8) == odds
partition_cases = 0
for E in Es:
    for parity, universe in ((0, evens), (1, odds)):
        for a, b in product(range(parity, 16, 2), repeat=2):
            ea, eb = shifted(E, a), shifted(E, b)
            if ea.isdisjoint(eb) and ea | eb == universe:
                assert b == (a + 8) % 16
                partition_cases += 1
assert partition_cases == 256
anchored = [(E, O) for E in Es for O in Os
            if {0, 14}.issubset(E) and {1, 7, 13}.issubset(O)]
eq1 = [(E, O) for E, O in anchored if shifted(O, 11) == shifted(E, 8)]
eq2 = [(E, O) for E, O in anchored if shifted(O, 8) == shifted(E, 11)]
both = [(E, O) for E, O in eq1 if shifted(O, 8) == shifted(E, 11)]
assert (len(Es), len(Os), len(anchored), len(eq1), len(eq2), len(both)) == (16, 16, 8, 1, 1, 0)
print('transversals E/O', len(Es), len(Os), 'partition offset cases', partition_cases)
print('anchored pairs', len(anchored), 'first/second/both equations', len(eq1), len(eq2), len(both))
print('negative non-transversal even universe is invariant under 6 and fails disjoint +8')

# Literal anchor coverage and the row-constancy shift generator.
qanchors = (0, 1, 7, 13, 14)
assert len({q % 5 for q in qanchors}) == 5
assert {q % 11: q % 25 for q in qanchors} == {0: 0, 1: 1, 7: 7, 2: 13, 3: 14}
assert all((q % 2 == 1) == (q % 3 == 1) for q in qanchors)
assert gcd(14, 25) == 1
orbit = {(14 * k) % 25 for k in range(25)}
assert len(orbit) == 25
broken_row = [0] * 25
broken_row[1] = 8
assert any(broken_row[z] != broken_row[(z - 14) % 25] for z in range(25))
print('all five Q anchors distinct mod5; 14-orbit size', len(orbit))
print('negative nonconstant row violates the 14-shift equality')
print('ALL REVIEWER-OWNED FINITE CONTROLS COMPLETED')
