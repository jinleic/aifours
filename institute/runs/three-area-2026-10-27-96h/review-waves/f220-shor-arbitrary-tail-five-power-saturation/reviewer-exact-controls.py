#!/usr/bin/env python3
"""Bounded, exact reviewer controls; this does not import author code."""
from collections import Counter
from itertools import product
from math import gcd

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
fixed = {0: 0, 1: 1, 2: 13, 3: 14, 7: 7}
classes = tuple(product(range(3), range(11)))


def compatible(c1, v1, c2, v2):
    i, j = c1
    k, h = c2
    p, s = v1
    q, t = v2
    return p == q or s == t or (i != k and j != h and s % 5 != t % 5)


anchor_entries = [((y % 3, y % 11), (y % 2, y % 25)) for y in Y]
domains = {
    c: {(p, s) for p in range(2) for s in range(25)
        if all(compatible(c, (p, s), d, v) for d, v in anchor_entries)}
    for c in classes
}
rounds = 0
while True:
    rounds += 1
    removed = 0
    for c in classes:
        for v in tuple(domains[c]):
            if any(not any(compatible(c, v, d, u) for u in domains[d])
                   for d in classes if d != c):
                domains[c].remove(v)
                removed += 1
    assert all(domains.values()), "a necessary-condition domain became empty"
    if not removed:
        break
assert all(p == int(i == 1) and s in Y
           for (i, j), values in domains.items() for p, s in values)
for i, j in classes:
    expected = {fixed[j]} if j in fixed else set(Y)
    assert {s for p, s in domains[i, j]} == expected
for j in range(11):
    for p, s in domains[0, j]:
        for q, t in domains[1, j]:
            assert compatible((0, j), (p, s), (1, j), (q, t)) == (s == t)
print(f"parity/graph: 33 classes, arc-consistency rounds={rounds}, "
      f"remaining values={sum(map(len, domains.values()))}; exact anchored and free domains pass")

# A concrete rule-plus-coverage configuration, NOT a direct tiling, showing
# that dropping tail anchor 14 destroys the parity conclusion.
no14 = {}
for i, j in classes:
    if (i, j) == (0, 0):
        no14[i, j] = (0, 0)
    elif (i, j) in {(1, 1), (1, 7), (1, 2)}:
        no14[i, j] = (1, {1: 1, 7: 7, 2: 13}[j])
    else:
        no14[i, j] = (1, 0)
assert all(compatible(c, no14[c], d, no14[d]) for c in classes for d in classes)
assert all(((y % 3, y % 11), (y % 2, y % 25)) in no14.items()
           for y in (0, 1, 7, 13))
assert any(p == 1 and i != 1 for (i, j), (p, s) in no14.items())
print("negative parity: without anchor 14, a 33-class compatible relaxation has wrong-parity tails")


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divmod_monic(a, b):
    a, b = trim(list(a)), trim(list(b))
    assert b[-1] == 1
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        offset, factor = len(a) - len(b), a[-1]
        q[offset] += factor
        for k, value in enumerate(b):
            a[offset + k] -= factor * value
        trim(a)
    return trim(q), a


for s in (1, 2):
    step = 5 ** (s - 1)
    phi = [0] * (4 * step + 1)
    for r in range(5):
        phi[r * step] = 1
    substituted = [0] * (11 * (len(phi) - 1) + 1)
    for k, value in enumerate(phi):
        substituted[11 * k] = value
    phi_product, remainder = divmod_monic(substituted, phi)
    assert remainder == [0]
    assert len(phi_product) - 1 == 10 * (len(phi) - 1)
    _, diff_remainder = divmod_monic([1, -1], phi)
    assert diff_remainder != [0]
    print(f"cyclotomic polynomial control: Phi_(5^{s}) degree={len(phi)-1}, "
          f"Phi_(11*5^{s}) degree={len(phi_product)-1}, 1-X nonzero modulo Phi")
print("negative field-degree: for noncoprime conductors eta=xi^5 with xi of order 25, "
      "eta is already in Q(xi), so relative degree is 1, not 4")

free = tuple(j for j in range(11) if j not in fixed)
assert len(free) == 6
count = 0
histograms = set()
for values in product(Y, repeat=len(free)):
    f = dict(fixed)
    f.update(zip(free, values))
    assert f[0] == 0 and f[1] == 1 and max(f.values()) <= 14
    hist = tuple(sum(f[j] % 5 == r for j in range(11)) for r in range(5))
    assert sum(hist) == 11 and min(hist) >= 1 and len(set(hist)) > 1
    histograms.add(hist)
    count += 1
assert count == 5 ** 6
phi5 = [1] * 5
assert divmod_monic([2] * 5, phi5)[1] == [0]
print(f"arbitrary f: {count} assignments, {len(histograms)} residue histograms; "
      "order-5 nonzero and order-25 degree bound pass")
print("negative order-5: 10 terms with each residue occurring twice give 2*Phi_5 and vanish")
print("negative eta: if all eleven coefficients are 1, the polynomial is Phi_11 and vanishes")

phi3 = [1, 1, 1]
assert divmod_monic([1, -1, 1], phi3)[1] == [0, -2]
assert divmod_monic([1, 1, 1], phi3)[1] == [0]
print("prefactor: 1-X+X^2 = -2X mod Phi_3; negative 1+X+X^2 vanishes")

buckets = {(a % 2, a % 11) for a in A}
assert len(buckets) == 4 and 25 * len(buckets) == 100
assert len({(a % 2, a % 11) for a in (0, 3, 8)}) == 3
print("saturation count: four anchored buckets require 100; negative three anchors force only 75")

signed = {}
for e, o in product(range(3), repeat=2):
    vector = tuple(int(e == k) - int(o == k) for k in range(3))
    signed.setdefault(vector, []).append((e, o))
assert signed[(0, 0, 0)] == [(0, 0), (1, 1), (2, 2)]
assert all(len(pairs) == 1 for v, pairs in signed.items() if v != (0, 0, 0))


def folded_target00(e, o):
    # (head parity, head mod 3); the Q parity is 1 iff Q mod 3 is 1.
    rows = ((0, e), (1, o), (1, 0), (0, 2))
    return sum(int(((0 - hp) % 2) == int(((0 - hi) % 3) == 1))
               for hp, hi in rows)


assert [folded_target00(k, k) for k in range(3)] == [1, 1, 1]
assert folded_target00(0, 2) == 2
assert tuple(int(0 == k) - int(2 == k) for k in range(3)) != tuple(
    int(1 == k) - int(2 == k) for k in range(3))
print("signed/folded: zero difference gives w instead of 2w in all 3 cases; E=0,O=2 gives 2w")
print("negative signed: changing E while O=2 changes the signed vector, so constancy is essential")

moduli = (2, 3, 11, 25)
M = 1650


def crt(residues):
    return sum(r * (M // m) * pow(M // m, -1, m)
               for r, m in zip(residues, moduli)) % M


P0 = {crt((a % 2, a % 3, a % 11, s)) for a in A for s in range(25)}
Q0 = {crt((int(i == 1), i, j, fixed.get(j, 0))) for i, j in classes}
assert len(P0) == 100 and len(Q0) == 33
assert set(A) <= P0 and set(Y) <= Q0
assert Counter(x % 66 for x in P0) == Counter({a: 25 for a in A})
expected_table = {
    (0, 0): {(0, 0), (11, 1)}, (0, 1): {(3, 1), (8, 2)},
    (0, 2): {(0, 2), (8, 0)}, (1, 0): {(3, 0), (8, 1)},
    (1, 1): {(0, 1), (11, 2)}, (1, 2): {(3, 2), (11, 0)},
}
for ep, target in product(range(2), range(3)):
    pairs = {(a, i) for a in A for i in range(3)
             if (a % 2 + int(i == 1)) % 2 == ep and (a % 3 + i) % 3 == target}
    assert pairs == expected_table[ep, target]
cover = Counter((p + q) % M for p in P0 for q in Q0)
assert len(cover) == M and set(cover.values()) == {2}
weighted = Counter({x: 5 * count for x, count in cover.items()})
assert set(weighted.values()) == {10}
assert any(count != 1 for count in cover.values())
print("CRT quotient: both anchors, six exact table cells, 1650 residues each multiplicity 2; "
      "w=5 weighted profile has multiplicity 10")
print("negative quotient: the same cover is not onefold, hence is not a direct tiling")
print("ALL EXACT CONTROLS PASSED")
