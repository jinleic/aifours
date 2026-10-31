#!/usr/bin/env python3
"""Bounded independent arithmetic controls; no author code or linked sources."""
from collections import Counter
from itertools import combinations, product
from functools import reduce
from operator import xor
import signal

signal.alarm(110)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def char(a, b):
    return -1 if (a & b).bit_count() % 2 else 1


def atom_transform(atoms, signs, c):
    return sum(sign * char(a, c) for a, sign in zip(atoms, signs))


# Exhaustive local ternary blocks and all four coordinate relabellings.
for block in product((-1, 0, 1), repeat=4):
    u = [sum(block[z] * char(s, z) for z in range(4)) for s in range(4)]
    require(sum(x*x for x in u) == 4*sum(x*x for x in block), 'block Parseval')
    if abs(u[1]) == 3:
        require(all(abs(u[s]) == 1 for s in (0, 2, 3)), 'three-entry shape')
    if u[1] == 0:
        shapes = sorted(abs(x) for x in u)
        require(shapes in ([0, 0, 0, 0], [0, 0, 2, 2], [0, 0, 0, 4]), 'even shape')
    for shift in range(4):
        moved = [block[z ^ shift] for z in range(4)]
        for s in range(4):
            actual = sum(moved[z] * char(s, z) for z in range(4))
            require(actual == char(s, shift)*u[s], 'coordinate shear')
print('local blocks=81; block shifts=324; block Parseval and shapes=OK')

# Four atoms: independent-affine and plane cases, all signed patterns.
for atoms in ((0, 1, 2, 4), (0, 1, 2, 3)):
    for signs in product((-1, 1), repeat=4):
        ts = [atom_transform(atoms, signs, c) for c in range(64)]
        counts = Counter(abs(t) for t in ts)
        if atoms[-1] == 4:
            require(counts == {0: 24, 2: 32, 4: 8}, 'independent four atoms')
        elif signs[0]*signs[1]*signs[2]*signs[3] == 1:
            require(counts == {0: 48, 4: 16}, 'even plane syndrome')
        else:
            require(counts == {2: 64}, 'odd plane syndrome')
print('four-atom sign patterns=32; rank-three and two plane alternatives=OK')

# Eight-atom zero set, nontrivial Fourier spectrum, and all affine 3-flats of H*.
B = set()
for u in range(4):
    for v in range(16):
        weight = v.bit_count()
        if (u != 0 and weight == 2) or (u == 0 and weight in (1, 4)):
            B.add(u | (v << 2))
H = {c for c in range(64) if (c >> 2).bit_count() % 2 == 0}
require(len(B) == 23 and len(B & H) == 19, 'B and H sizes')
coeff = {a: sum(char(a, c) for c in B) for a in range(64)}
require([(a, coeff[a]) for a in range(1, 64) if abs(coeff[a]) >= 11] == [(60, 15)], 'unique large B coefficient')
nonzero = sorted(H - {0})
directions = set()
for a, b, c in combinations(nonzero, 3):
    span = frozenset((0, a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c))
    if len(span) == 8:
        directions.add(tuple(sorted(span)))
require(len(directions) == 155, 'number of three-dimensional directions')
flats = set()
for direction in directions:
    for origin in H:
        flats.add(tuple(sorted(origin ^ d for d in direction)))
require(len(flats) == 620, 'number of affine three-flats')
histogram = Counter()
for flat in flats:
    intersection = sorted(set(flat) & B)
    histogram[len(intersection)] += 1
    if len(intersection) == 2:
        require(intersection[0] ^ intersection[1] == 60, 'two-point direction')
print('B size=23; H intersection=19; unique large Fourier coefficient=(60,15)')
print('H affine 3-flats=620; intersection histogram=' + str(dict(sorted(histogram.items()))))
print('every two-point intersection direction=60')

# Reconstruct the stated placement and sign extension, including all 64 translations.
p, q, b1, b2, b3, b4 = (1, 2, 4, 8, 16, 32)
a3 = (0, p, q, p ^ q, b1, b2, b3, b4)
a2 = (0, p, q ^ b1 ^ b2, p ^ q ^ b3 ^ b4)
eps2 = (1, 1, -1, -1)
neg2 = {a2[2], a2[3], b1, p ^ b2 ^ b3 ^ b4}
require(len(set(a2)) == 4 and len(set(a3)) == 8 and len(neg2) == 4, 'distinct placement')
require(reduce(xor, a2) == reduce(xor, a3) == 60, 'common nonzero XOR')
require(eps2[0]*eps2[1]*eps2[2]*eps2[3] == 1, 'common sign product')
t2 = [atom_transform(a2, eps2, c) for c in range(64)]
f2 = {c for c in range(64) if abs(t2[c]) == 4}
h2 = {c for c in range(64) if t2[c] % 4 == 0}
require(h2 == H and len(f2 & B) == 2 and len((h2 - f2) & B) == 17, 'formal geometry')
for t in range(64):
    require(len({a ^ t for a in a2} & set(a3)) <= 2, 'all translations support')
    disagreement = {a ^ t for a in neg2}
    require(len(disagreement) == 4 and reduce(xor, disagreement) == 0, 'all translations sign')
print('formal placement: H2=H*, |F2 intersect B|=2, |(H2-F2) intersect B|=17')
print('formal support and sign restrictions: all 64 translations=OK')

# Intended negatives: parity offset, bad intersection and nonintegral/out-of-range local U.
require((2 // 2) % 2 == 1 and (0 + 0) % 2 == 0, 'short parity negative')
outer = (b1, b2, b3, b4)
outer_f = {c for c in range(64) if abs(atom_transform(outer, (1, 1, 1, 1), c)) == 4}
require(len(set(outer) & set(a3)) == 4 and len(outer_f & B) == 1, 'bad outer-overlap negative')
require(3*56 % 16 == 8 and (3*64 - 2*8) // 16 == 11, 'formal placement non-witness')
print('intended negatives: missing e/2 parity, four-atom overlap, noninteger U2 and U3=11=OK')

# Real Boolean inverse control: balanced m=116, T!=0, deliberately NOT max-Walsh bounded.
sign = [-1 if x & 1 else 1 for x in range(512)]
for i in range(70):
    odd = 2*i + 1
    even = 2*i
    sign[odd ^ (256 if i == 0 else 0)] *= -1
    sign[even] *= -1
require(sum(sign) == 0, 'Boolean balance')
T = reduce(xor, (x for x in range(512) if sign[x] == -1), 0)
require(T == 256, 'Boolean XOR T')
u = [(sign[y] + sign[y ^ T]) // 2 for y in range(256)]
v = [(sign[y] - sign[y ^ T]) // 2 for y in range(256)]
require(sum(x*x for x in u) == 116 and sum(x*x for x in v) == 140, 'Boolean pair counts')
require(all(u[y]*v[y] == 0 and u[y]*u[y] + v[y]*v[y] == 1 for y in range(256)), 'full inverse pairing')
W = [sum(sign[x] * char(a, x) for x in range(512)) for a in range(512)]
require(all(w % 4 == 0 for w in W), 'Boolean W divisible by 4')
k = [w // 4 for w in W]
for a in range(256):
    wu = sum(u[y] * char(a, y) for y in range(256))
    wv = sum(v[y] * char(a, y) for y in range(256))
    require(wu == 2*k[a] and wv == 2*k[a ^ 256], 'both Walsh halves')
    require(k[a] % 2 == 0 and k[a ^ 256] % 2 == 1, 'T parity')
for y in range(256):
    require(sum(k[a] * char(a, y) for a in range(256)) == 128*u[y], 'u inverse')
    require(sum(k[a ^ 256] * char(a, y) for a in range(256)) == 128*v[y], 'v inverse')
for b in range(512):
    require(sum(k[a]*k[a ^ b] for a in range(512)) == (16384 if b == 0 else 0), 'full Boolean caller')
for s in range(4):
    U = [sum(u[c | (z << 6)]*char(s, z) for z in range(4)) for c in range(64)]
    for r in range(64):
        require(sum(U[c]*char(r, c) for c in range(64)) == 2*k[r | (s << 6)], 'shared block transform')
print('balanced Boolean control: T=256, m=116, both inverses and all 512 caller shifts=OK')
print('Boolean control max|W|=' + str(max(abs(w) for w in W)) + '; NOT a <=28 target or witness')

# Symbolic normalization on independent synthetic sign fields and signed atoms.
for atoms, signs in ((a2, eps2), (a3, (1,)*8)):
    sigma = [(-1 if r in neg2 else 1) for r in range(64)] if len(atoms) == 4 else [1]*64
    require(all(sigma[a] == sign for a, sign in zip(atoms, signs)), 'atom signs')
    kf = [2*sigma[r]*(3 - 2*(r in atoms)) for r in range(64)]
    for c in range(64):
        ws = sum(sigma[r]*char(r, c) for r in range(64))
        ts = atom_transform(atoms, signs, c)
        inverse_numerator = sum(2*kf[r]*char(r, c) for r in range(64))
        require(16*inverse_numerator == 64*(3*ws - 2*ts), '16U normalization')
print('16U_s=3 Walsh(sigma_s)-2 t_s: both synthetic fibres, all 64 characters=OK')
print('ALL CONTROLS COMPLETED')
