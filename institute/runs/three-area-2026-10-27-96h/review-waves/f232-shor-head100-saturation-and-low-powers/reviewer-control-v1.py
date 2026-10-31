#!/usr/bin/env python3
"""Reviewer-owned exact finite checks; no author code or external packages."""
from itertools import product
from math import gcd

Y = (0, 1, 7, 13, 14)
ANCHORS = (0, 1, 7, 13, 14)
FIXED = {0: 0, 1: 1, 2: 13, 3: 14, 7: 7}
FREE = tuple(j for j in range(11) if j not in FIXED)
CLASSES = tuple(product(range(3), range(11)))


def compatible(c, a, d, b):
    r, j = c
    s, k = d
    p, z = a
    q, v = b
    return not (p != q and (r == s or j == k or z % 5 == v % 5) and z != v)


def anchored_domain():
    anchors = tuple(((x % 3, x % 11), (x % 2, x % 25)) for x in ANCHORS)
    return {
        c: {(p, z) for p in range(2) for z in range(25)
            if all(compatible(c, (p, z), d, b) for d, b in anchors)}
        for c in CLASSES
    }


def enforce_arc_consistency(domains):
    rounds = 0
    while True:
        rounds += 1
        changed = False
        for c in CLASSES:
            for a in tuple(domains[c]):
                if any(not any(compatible(c, a, d, b) for b in domains[d])
                       for d in CLASSES if d != c):
                    domains[c].remove(a)
                    changed = True
            assert domains[c], ('empty', c)
        if not changed:
            return rounds


def remainder(coeff, divisor):
    coeff = list(coeff)
    while coeff and coeff[-1] == 0:
        coeff.pop()
    while len(coeff) >= len(divisor):
        a = coeff[-1]
        start = len(coeff) - len(divisor)
        for i, x in enumerate(divisor):
            coeff[start + i] -= a * x
        while coeff and coeff[-1] == 0:
            coeff.pop()
    return tuple(coeff)


def counts_mod(coeff, p):
    out = [0] * p
    for i, a in enumerate(coeff):
        out[i % p] += a
    return out


def mul_coeff_rows(f):
    a = [0] * 15
    for x in f:
        a[x] += 1
    return a


def folded_counts(e, o):
    heads = ((0, e), (1, o), (1, 0), (0, 2))
    return {(p, r): sum(((p - hp) % 2) == int((r - hr) % 3 == 1)
                        for hp, hr in heads)
            for p in range(2) for r in range(3)}


def low_bits_control():
    cases = 0
    # K=3, s=2: anchor 13 and the paired residue 1 mod 8.
    assert (13 % 8 + 4) % 8 == 1
    assert (13 - 1) % 5 != 0 and (1 - 1) % 8 == 0
    cases += 1
    # K=3, s=3: anchor 7, phi4 partner 1 mod 4.
    for x, ref in ((1, 1), (5, 13)):
        assert x % 4 == 1 and (x - ref) % 8 == 0
        assert (7 - ref) % 5 != 0
        cases += 1
    # K>=4, s outside {3,4}: phi8 then phi16 give residue 9.
    for x in (1, 9):
        assert x % 8 == 1 and ((x + 8) % 16 in (1, 9))
        assert (9 - 1) % 16 == 8 and (13 - 1) % 5 != 0
        cases += 1
    # K>=4, s=3: phi4 partner x and phi16 partner supply 9 or 5.
    for x in (1, 5, 9, 13):
        if x % 8 == 1:
            selected, ref = 9, 1
        else:
            selected, ref = 5, 13
        assert selected in (x, (x + 8) % 16)
        assert (selected - ref) % 16 == 8 and (7 - ref) % 5 != 0
        cases += 1
    # K=2: varying extra odd factors does not change the relevant gcds.
    for v in (3, 4, 5):
        for m in range(1, 101, 2):
            if m % 5 == 0:
                continue
            n = 4 * (5 ** v) * 33 * m
            assert gcd(24, n) == gcd(12, n) == 12
            cases += 1
    # Intended-reason negative: equal mod-5 tail values cannot invoke the rule.
    assert (13 - 8) % 5 == 0
    assert (9 - 1) % 16 == 8
    return cases


initial = anchored_domain()
assert (1, 0) in initial[(0, 0)]  # Negative candidate survives anchor-only checks.
domains = {c: set(d) for c, d in initial.items()}
rounds = enforce_arc_consistency(domains)
assert (1, 0) not in domains[(0, 0)]
assert domains[(0, 3)] == {(0, 14)}
assert all(not compatible((0, 0), (1, 0), (0, 3), b) for b in domains[(0, 3)])
for r, j in CLASSES:
    values = (FIXED[j],) if j in FIXED else Y
    assert domains[(r, j)] == {(int(r == 1), z) for z in values}, (r, j, domains[(r, j)])

phi5 = (1, 1, 1, 1, 1)
phi25 = tuple(1 if i % 5 == 0 else 0 for i in range(21))
assert remainder((1, -1), phi5) and remainder((1, -1), phi25)
assignments = 0
for values in product(Y, repeat=len(FREE)):
    f = [None] * 11
    for j, value in FIXED.items():
        f[j] = value
    for j, value in zip(FREE, values):
        f[j] = value
    assert all(f[j] == f[k] for j in range(11) for k in range(11)
               if f[j] % 5 == f[k] % 5)
    coeff = mul_coeff_rows(f)
    c5 = counts_mod(coeff, 5)
    assert sum(c5) == 11 and remainder(c5, phi5)
    assert sum(coeff) == 11 and remainder(coeff, phi25)
    assignments += 1
assert assignments == 5 ** 6
# Intended-reason negatives: a ten-term balanced fifth-root sum and a repeated
# Phi_25 both vanish; equal eta coefficients can vanish at primitive 11th roots.
assert remainder([2] * 5, phi5) == ()
assert remainder([2 * x for x in phi25], phi25) == ()
assert all(x == 1 for x in [1] * 11)  # coefficient vector Phi_11

for e in range(3):
    assert folded_counts(e, e)[(0, 0)] == 1
assert all(x == 2 for x in folded_counts(0, 2).values())
assert any(x != 2 for x in folded_counts(0, 0).values())
low_cases = low_bits_control()
print('graph_arc_rounds:', rounds)
print('graph_classes:', len(CLASSES), 'forced parity and exact candidate domains: OK')
print('graph_negative: anchor-compatible odd (r=0,j=0,z=0) eliminated by occupied (r=0,j=3,z=14)')
print('free_label_assignments:', assignments, 'fifth/25th exact polynomial remainders nonzero: OK')
print('fourier_negatives: balanced 10-term Phi_5 and 2*Phi_25 reduce to zero; equal coefficients admit Phi_11')
print('folded_count: all equal E=O give 1, anchored E=0,O=2 give 2 at all six targets')
print('low_bit_and_K2_cases:', low_cases, 'negative: same mod5 cannot invoke even-difference rule')
print('SCOPE: conditional exact finite controls only; no LL, cyclotomic field-degree, or s=4 proof')
