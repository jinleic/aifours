#!/usr/bin/env python3
"""Reviewer-owned finite rational illustrations; no author code or search."""
from fractions import Fraction as Q
from itertools import product
from math import comb


def row(a, t):
    t = Q(t)
    e = sum(Q(a[2*r]) * (-t)**r for r in range(4))
    o = sum(Q(a[2*r+1]) * (-t)**r for r in range(4))
    den = (1+t)**7
    return [v for r in range(4)
            for v in ((-t)**r * e / den, t * (-t)**r * o / den)]


def dot(x, y):
    return sum((Q(a)*Q(b) for a, b in zip(x, y)), Q(0))


def eval_i(c, w):
    real = imag = Q(0)
    for coeff in reversed(c):
        real, imag = Q(coeff)-imag*w, real*w
    return real, imag


def direct_pair(a, b, w):
    ar, ai = eval_i(a, w)
    br, bi = eval_i(b, w)
    return ar*br + ai*bi


def multiply(a, b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


lo = [-2, 1, -1, 0, -3, 2, 1]
hi = [1, 4, 2, 3, 0, 5, 4]
b = [2, -3, 4, 1, -2, 5, 7, 3]
vertices = [[hi[j] if mask[j] else lo[j] for j in range(7)] + [1]
            for mask in product((0, 1), repeat=7)]
corners = []
for even_max, odd_max in product((False, True), repeat=2):
    c = []
    for j in range(7):
        parity_max = even_max if j % 2 == 0 else odd_max
        choose_hi = ((j//2) % 2 == 0) == parity_max
        c.append(hi[j] if choose_hi else lo[j])
    corners.append(c + [1])
assert all(c in vertices for c in corners)
for w in [Q(0), Q(1,2), Q(1), Q(2), Q(3)]:
    t = w*w
    all_values = []
    for a in vertices:
        via_row = dot(b, row(a, t)) * (1+t)**7
        assert via_row == direct_pair(a, b, w)
        all_values.append(via_row)
    corner_values = [direct_pair(c, b, w) for c in corners]
    assert min(all_values) == min(corner_values)
    assert max(all_values) == max(corner_values)
print('pairing identity: 640 exact vertex/frequency checks')
print('four actual corners: exact minimum and maximum at 5 frequencies')

stable_a = [comb(7, j) for j in range(8)]  # (s+1)^7
r = row(stable_a, Q(1))
bad = r[:]
bad[1] = -bad[1]
assert dot(b, bad) != dot(b, r)
print('negative control: wrong odd-coordinate sign changes pairing')

nodes = [Q(1), Q(2), Q(3)]
for i, t in enumerate(nodes):
    h = [Q(1)]
    for j, other in enumerate(nodes):
        if j != i:
            h = multiply(h, [other, Q(0), Q(1)])
    odd = [Q(0)] + h
    even = [Q(0), Q(0)] + h
    odd += [Q(0)] * (8-len(odd))
    even += [Q(0)] * (8-len(even))
    assert odd[0] == odd[7] == even[0] == even[7] == 0
    for j, u in enumerate(nodes):
        pairs = (dot(odd, row(stable_a, u)), dot(even, row(stable_a, u)))
        if i == j:
            assert pairs != (0, 0)
        else:
            assert pairs == (0, 0)
wrong_locator = [0, 1, 0, 0, 0, 0, 0, 0]
assert dot(wrong_locator, row(stable_a, nodes[1])) != 0
print('three-node endpoint-vanishing isolators: all exact checks passed')
print('negative control: omitting locator factors fails off-node vanishing')

lower_degree_b = [comb(6, j) for j in range(7)] + [0]  # (s+1)^6
for w in [Q(0), Q(1,2), Q(1), Q(2), Q(3)]:
    t = w*w
    assert direct_pair(stable_a, lower_degree_b, w) == (1+t)**6
    assert dot(lower_degree_b, row(stable_a, t)) == 1/(1+t)
assert lower_degree_b[7] == 0
print('exact-degree negative control: (s+1)^6/(s+1)^7 has positive finite samples but zero limit')

# Deliberately non-Hurwitz box: a_0,...,a_4 fixed zero; a_5,a_6 in [-3000,3000].
# These are its actual parity corners. This is NOT an SPR counterexample.
xs = [-10, 20, -15, 4]
ts = [Q(1), Q(2), Q(3), Q(4)]
weighted_atoms = []
for x, t in zip(xs, ts):
    sign = 1 if x > 0 else -1
    a = [0, 0, 0, 0, 0, sign*3000, -sign*3000, 1]
    weight = Q(abs(x), 3000) * (1+t)**7 / t**3
    weighted_atoms.append((weight, a, t))
aggregate = [sum((weight*row(a, t)[j] for weight, a, t in weighted_atoms), Q(0))
             for j in range(8)]
expected = [Q(-1), Q(-3111,3000), Q(-1), Q(-2711,3000),
            Q(-1), Q(-3831,3000), Q(-1), Q(-431,3000)]
assert aggregate == expected and all(x < 0 for x in aggregate)
weight0, a0, t0 = weighted_atoms[0]
wrong_a0 = a0[:]
wrong_a0[6] = -wrong_a0[6]
wrong_coordinate0 = aggregate[0] + weight0*(row(wrong_a0, t0)[0]-row(a0, t0)[0])
assert wrong_coordinate0 == 19 and wrong_coordinate0 > 0
print('four-atom rational strict certificate (unstable illustration):',
      ', '.join(str(x) for x in aggregate))
print('negative control: flipping first even corner gives coordinate 0 =', wrong_coordinate0)
print('all reviewer controls completed')
