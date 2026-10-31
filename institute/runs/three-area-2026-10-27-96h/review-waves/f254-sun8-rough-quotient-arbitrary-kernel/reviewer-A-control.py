#!/usr/bin/env python3
"""Finite sanity control for review A; not a proof of the universal theorem."""
from math import gcd

P, Q = 23, 11
assert pow(2, Q, P) == 1 and pow(2, 1, P) != 1

def mul(g, h):
    e, x, y = g
    f, u, v = h
    return ((e + f) % 2, (x + pow(2, y, P) * u) % P, (y + v) % Q)

def inv(g):
    e, x, y = g
    return (e, (-pow(2, (-y) % Q, P) * x) % P, (-y) % Q)

def left_coset(g, subgroup):
    return {mul(g, h) for h in subgroup}

def project(s):
    return {(x, y) for _, x, y in s}

identity = (0, 0, 0)
N = {(e, 0, 0) for e in range(2)}
U1 = {(0, 0, y) for y in range(Q)}
U2 = {(0, x, 0) for x in range(P)}
G = {(e, x, y) for e in range(2) for x in range(P) for y in range(Q)}
assert len(G) == 506 and len(U1) == 11 and len(U2) == 23
for U in (U1, U2):
    assert identity in U
    assert all(mul(a, b) in U for a in U for b in U)
    assert all(inv(a) in U for a in U)
conjugator, h = (0, 1, 0), (0, 0, 1)
conjugate_h = mul(mul(conjugator, h), inv(conjugator))
assert conjugate_h == (0, 22, 1) and conjugate_h not in U1
assert gcd(253, 2*3*5*7) == 1

C1 = left_coset((0, 4, 2), U1)
C2 = left_coset((1, 7, 5), U2)
A1, A2 = project(C1), project(C2)
assert len(C1) == 11 and len(C2) == 23 and not (C1 & C2)
assert len(A1) == 11 and len(A2) == 23 and A1 & A2 == {(4, 5)}
assert (506 // len(U1), 506 // len(U2)) == (46, 22)
assert (253 // len(A1), 253 // len(A2)) == (23, 11)
assert gcd(46, 22) == 2 and gcd(23, 11) == 1
assert U1 & N == U2 & N == {identity}
assert (len(N) // len(U1 & N), len(N) // len(U2 & N)) == (2, 2)
for T in (2, 7):
    assert gcd(46, 22) <= T
    assert all(253 % p for p in range(2, T + 1))

# Enumerate every tuple of the 23 actual left cosets of U1's image and
# the 11 actual left cosets of U2's image, not merely chosen representatives.
for x0 in range(P):
    for y0 in range(Q):
        B1 = project(left_coset((0, x0, 0), U1))
        B2 = project(left_coset((0, 0, y0), U2))
        assert B1 & B2 == {(x0, y0)}

q = (4, 5)
t = (0, *q)
fiber = {g for g in G if g[1:] == q}
translated = [{mul(g, inv(t)) for g in C & fiber} for C in (C1, C2)]
assert translated == [{(0, 0, 0)}, {(1, 0, 0)}]
assert all(part <= N for part in translated) and not (translated[0] & translated[1])
for C, U, part in zip((C1, C2), (U1, U2), translated):
    xi = next(iter(C & fiber))
    K = U & N
    tKt_inverse = {mul(mul(t, k), inv(t)) for k in K}
    assert part == left_coset(mul(xi, inv(t)), tKt_inverse)

# Intended-reason negative: actual disjointness need not descend to the quotient.
assert not (C1 & C2) and A1 & A2
# Intended-reason negative: pairwise intersection without coprime indices is
# insufficient for a simultaneous intersection, even for cosets of a group.
plane = {(x, y) for x in range(2) for y in range(2)}
lines = [{(x, y) for x, y in plane if x == 0},
         {(x, y) for x, y in plane if y == 0},
         {(x, y) for x, y in plane if (x + y) % 2 == 1}]
assert all(lines[i] & lines[j] for i in range(3) for j in range(i+1, 3))
assert not set.intersection(*lines) and all(len(plane)//len(line) == 2 for line in lines)

print('PASS finite control: |G|=506, |Q|=253, U1 nonnormal, indices n=(46,22), a=(23,11), b=(2,2)')
print('PASS all 253 pairs of actual quotient cosets intersect once')
print('PASS r=1, T=2 and T=7 bad-family fibre mechanics; B_T(N)<=1 premise intentionally fails')
print('PASS common right translation gives distinct actual N-cosets with preserved gcd 2')
print('NEGATIVE AS INTENDED: disjoint original cosets have intersecting quotient images')
print('NEGATIVE AS INTENDED: pairwise-intersecting index-2 cosets have empty triple intersection')
