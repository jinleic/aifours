#!/usr/bin/env python3
"""Independent finite exact sanity controls, not an exclusion proof."""
from fractions import Fraction as F
from itertools import combinations

Z = (F(0), F(0))
O = (F(1), F(0))

def g(a=0, b=0):
    return (F(a), F(b))

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def conj(x):
    return (x[0], -x[1])

def inner(v, w):
    result = Z
    for a, b in zip(v, w):
        result = add(result, mul(conj(a), b))
    return result

def same_line(v, w):
    assert len(v) == len(w) == 2
    return mul(v[0], w[1]) == mul(v[1], w[0])

def gf_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 8:
            a ^= 0b1011
        b >>= 1
    return result

# In GF(8) with x^3+x+1, four distinct nonzero slopes give four
# classical squares. Apply an exact complex unitary to Q's labels.
cells = [(r, c) for r in range(8) for c in range(8)]
slopes = [1, 2, 4, 3]
squares = [{(r, c): r ^ gf_mul(s, c) for r, c in cells} for s in slopes]
for square in squares:
    for k in range(8):
        assert len({square[r, k] for r in range(8)}) == 8
        assert len({square[k, c] for c in range(8)}) == 8
for i, j in combinations(range(4), 2):
    assert len({(squares[i][z], squares[j][z]) for z in cells}) == 64

qvec = []
for label in range(8):
    vector = [Z for _ in range(8)]
    base = label - label % 2
    vector[label] = g(F(3, 5))
    vector[base + 1 - label % 2] = g(0, F(4, 5))
    qvec.append(vector)
for i in range(8):
    for j in range(8):
        assert inner(qvec[i], qvec[j]) == (O if i == j else Z)

Q = squares[0]
W = {0, 1, 2, 3}
Wcells = [z for z in cells if Q[z] in W]
assert len(Wcells) == 32
assert all(sum(Q[r, c] in W for c in range(8)) == 4 for r in range(8))
assert all(sum(Q[r, c] in W for r in range(8)) == 4 for c in range(8))
assert all(sum(Q[z] == t for z in Wcells) == 8 for t in W)

for y in Wcells:
    u = Q[y]
    mate_supports = []
    for mate in squares[1:]:
        weighted = [z for z in cells if mate[z] == mate[y]]
        # Exact partial contraction: one Q label of each kind.
        assert all(sum(Q[z] == t for z in weighted) == 1 for t in range(8))
        off = {z for z in weighted if z != y}
        assert all(z[0] != y[0] and z[1] != y[1] and Q[z] != u for z in off)
        mate_supports.append(off)
    assert all(a.isdisjoint(b) for a, b in combinations(mate_supports, 2))
    for t in W - {u}:
        from_mates = sum(sum(Q[z] == t for z in support) for support in mate_supports)
        from_lines = sum(Q[z] == t and z != y and (z[0] == y[0] or z[1] == y[1]) for z in Wcells)
        full_star = sum(Q[z] == t for z in Wcells)
        assert (from_mates, from_lines, full_star) == (3, 2, 8)

print('GF8 positive: 4 squares, 6 orthogonal pairs, 32 W cells, all 32 choices of y checked')
print('complex positive: Q label basis is an exact Gaussian-rational unitary basis')
print('STAR positive: for each W-star direction the 3 mate + 2 line contribution is 5; full star is 8')
print('NEG missing mate: only 2 mate + 2 line contribution = 4, so the 5 bound is not established')
assert 2 + 2 == 4 < 5
print('NEG no GAP3/intrinsic: W is a reducible union of four one-ray components; each ray has multiplicity 8')
assert all(sum(Q[z] == t for z in cells) == 8 > 3 for t in W)

# The following directions and buckets are abstract checks of the plane
# argument, not a proposed tight frame, component, or four-MOQLS witness.
x = (O, Z)
xp = (Z, O)
v = (g(F(3, 5)), g(0, F(4, 5)))
vp = (g(0, F(4, 5)), g(F(3, 5)))
assert all(inner(t, t) == O for t in (x, xp, v, vp))
assert inner(x, xp) == Z and inner(v, vp) == Z
assert inner(v, x) != Z and inner(v, xp) != Z
actual = (x, xp, v)
targets = (xp, x, vp)
assert all(not same_line(a, b) for a, b in combinations(targets, 2))
assert all(not same_line(v, t) for t in targets)
buckets = [(targets[0], 5), (targets[1], 5), (targets[2], 5), (v, 1)]
assert all(sum(weight for ray, weight in buckets if same_line(ray, t)) == 5 for t in targets)
assert sum(weight for _, weight in buckets) == 16
assert sum(weight for _, weight in buckets) + 1 == 17 > 16
print('plane positive: three complex target directions are disjoint; 5+5+5+1=16')
print('NEG repeated third: 5+5+5+2=17 exceeds 16')
assert same_line(targets[0], targets[0])
print('NEG duplicate ray indices: their target directions coincide, so disjointness must use distinct rays')

assert all(8 + 2*m <= 14 for m in (1, 2, 3))
counts_m4 = [3, 3, 3, 3, 1, 1, 1, 0]
assert sum(counts_m4) == 15 and max(counts_m4[4:]) == 1
print('row positive: m<=3 gives at most 14; NEG m=4 abstract row counts can reach 15 without a double-star row')

# D = span(q0, q1, (3*q2+4i*q3)/5) in Q-label coordinates.
masses = [F(1), F(1), F(9, 25), F(16, 25)]
degrees = [1, 1, 2, 2]  # actual Q-rays in D are q0,q1
assert sum(masses) == 3
lhs = 10 * 2
middle = 8 * sum(m*d for m, d in zip(masses, degrees))
rhs = 3 * 8 * sum(masses)
assert (lhs, middle, rhs) == (20, 32, 72)
assert 10 * 7 <= 72 < 10 * 8
print('capacity positive: complex D has 10N=20 <= exact double count 32 <= 72; N<=7 arithmetic checked')
# Four distinct plane directions all perpendicular to an out-of-plane axis.
four = (x, xp, v, vp)
assert all(not same_line(a, b) for a, b in combinations(four, 2))
e3 = (Z, Z, O)
assert all(inner((ray[0], ray[1], Z), e3) == Z for ray in four)
print('NEG no plane cap: four distinct plane directions have perpendicular degree 4, not <=3')
print('all exact controls completed; none is an exclusion proof')
