#!/usr/bin/env python3
"""Reviewer-owned exact geometric and algebraic controls; no author code."""
from fractions import Fraction as Q
from math import factorial, comb
import signal


def alarm_handler(_signum, _frame):
    print('UNKNOWN: control reached the 120-second wall-clock cap', flush=True)
    raise SystemExit(124)


signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(120)


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def negative(label, reason, operation):
    try:
        operation()
    except ValueError as exc:
        if str(exc) != reason:
            raise
        print('NEGATIVE REJECTED:', label, '->', reason)
    else:
        raise AssertionError('mutation was not rejected: ' + label)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*ps):
    out = [Q(0)] * max(map(len, ps))
    for p in ps:
        for j, x in enumerate(p):
            out[j] += x
    return trim(out)


def scale(p, c):
    return trim([x * c for x in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for j, x in enumerate(p):
        for k, y in enumerate(q):
            out[j + k] += x * y
    return trim(out)


def shift(p, a):
    out = [Q(0)] * len(p)
    for k, x in enumerate(p):
        for j in range(k + 1):
            out[j] += x * comb(k, j) * a ** (k - j)
    return trim(out)


def value(p, x):
    return sum((a * x ** j for j, a in enumerate(p)), Q(0))


def interpolate(samples):
    """Recover a degree-at-most-n polynomial from n+1 exact values."""
    n = len(samples)
    mat = [[Q(i) ** j for j in range(n)] + [samples[i]] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if mat[i][j])
        mat[j], mat[pivot] = mat[pivot], mat[j]
        d = mat[j][j]
        mat[j] = [z / d for z in mat[j]]
        for i in range(n):
            if i != j:
                d = mat[i][j]
                mat[i] = [a - d * b for a, b in zip(mat[i], mat[j])]
    return trim([row[-1] for row in mat])


def simplex(p, q, r):
    # Integral of u^p v^q on {u,v >= 0, u+v <= r}.
    return r ** (p + q + 2) * Q(factorial(p) * factorial(q), factorial(p + q + 2))


c = Q(1, 2)


def square_shell_area(r):
    return 4 * (c * c + 2 * c * r + simplex(0, 0, r))


def square_shell_moment(r):
    base = Q(2, 3) * c ** 4
    strip = c * (r ** 3 / 3 + c * r ** 2 + c * c * r) + c ** 3 * r / 3
    triangle = (simplex(2, 0, r) + simplex(0, 2, r)
                + 2 * c * (simplex(1, 0, r) + simplex(0, 1, r))
                + 2 * c * c * simplex(0, 0, r))
    return 4 * (base + 2 * strip + triangle)


def diamond_area(r):
    return 4 * simplex(0, 0, r)


def diamond_moment(r):
    return 4 * (simplex(2, 0, r) + simplex(0, 2, r))


# Polynomial degree <= 2 for areas and <= 4 for quadratic moments follows
# directly from the simplex/rectangle formulas. Interpolation is exact.
area_s = interpolate([square_shell_area(Q(i)) for i in range(3)])
moment_s = interpolate([square_shell_moment(Q(i)) for i in range(5)])
area_k_positive = interpolate([diamond_area(Q(i + 1)) for i in range(3)])
moment_k_positive = interpolate([diamond_moment(Q(i + 1)) for i in range(5)])
area_delta = add(area_k_positive, scale(area_s, -1))
moment_delta = add(moment_k_positive, scale(moment_s, -1))
require(area_s == [Q(1), Q(4), Q(2)], 'square area polynomial')
require(moment_s == [Q(1, 6), Q(4, 3), Q(3), Q(8, 3), Q(2, 3)], 'square moment polynomial')
require(area_delta == [Q(1)], 'positive-level area difference')
require(moment_delta == [Q(1, 2), Q(4, 3), Q(1)], 'positive-level moment difference')
print('S areas, moments:', area_s, moment_s)
print('K-S for i >= 1, areas, moments:', area_delta, moment_delta)


# Stirling recurrence gives exact geometric moments E[G^k] for
# P(G=i)=(1-b)b^i, m=b/(1-b): E[(G)_j]=j! m^j.
stirling = [[1]]
for k in range(1, 5):
    prev = stirling[-1]
    row = []
    for j in range(k + 1):
        left = prev[j - 1] if 0 <= j - 1 < len(prev) else 0
        right = j * prev[j] if j < len(prev) else 0
        row.append(left + right)
    stirling.append(row)
geom = [[Q(stirling[k][j] * factorial(j)) for j in range(k + 1)] for k in range(5)]


def geometric_average(coefficients):
    return add(*(scale(geom[j], a) for j, a in enumerate(coefficients)))


# Given a positive index, i has distribution 1+G by memorylessness.
def positive_moment(k):
    return add(*(scale(geom[j], Q(comb(k, j))) for j in range(k + 1)))


added_cost = add(*(scale(positive_moment(j), a) for j, a in enumerate(moment_delta)))
z_s = geometric_average(area_s)
n_s = geometric_average(moment_s)
require(added_cost == [Q(17, 6), Q(13, 3), Q(2)], 'conditional added cost')
require(z_s == [Q(1), Q(6), Q(4)], 'square normalizer')
require(n_s == [Q(1, 6), Q(23, 3), Q(94, 3), Q(40), Q(16)], 'square moment normalizer')
print('E[G^k] polynomials:', geom)
print('Z_S(m), N_S(m), T(m):', z_s, n_s, added_cost)


# The all-law lower bound is L=(m+8m^2+8m^3)/(1+2m).
l_num = [Q(0), Q(1), Q(8), Q(8)]
den = [Q(1), Q(2)]
gap6 = scale(add(l_num, scale(mul(den, added_cost), -1)), 6)
gap6_at_2_plus_x = shift(gap6, Q(2))
require(gap6_at_2_plus_x == [Q(3), Q(170), Q(128), Q(24)], 'uniform lower-bound gap')
require(all(a > 0 for a in gap6_at_2_plus_x), 'uniform gap positivity')
# An independent direct comparison of the two phase costs avoids invoking L.
direct_gap = add(n_s, scale(mul(z_s, added_cost), -1))
direct_shift = shift(direct_gap, Q(2))
require(all(a > 0 for a in direct_shift), 'direct phase cost gap')
print('6(1+2m)(L-T) at m=2+x:', gap6_at_2_plus_x)
print('N_S-Z_S*T at m=2+x:', direct_shift)


b = Q(3, 4)
m = b / (1 - b)
z0 = value(z_s, m)
n0 = value(n_s, m)
t = value(added_cost, m)
z1 = z0 + b
n1 = n0 + b * t
j0, j1 = n0 / z0, n1 / z1
lower = value(l_num, m) / value(den, m)
margin = m * (t - lower)
require((z0, n0, z1, n1) == (Q(55), Q(16087, 6), Q(223, 4), Q(64957, 24)), 'rational normalizers')
require((j0, j1, j0 - j1) == (Q(16087, 330), Q(64957, 1338), Q(2461, 12265)), 'rational costs')
require((t, lower, margin) == (Q(203, 6), Q(291, 7), -Q(325, 14)), 'rational signed margin')
print('b=3/4: Z_S,N_S,Z_K,N_K =', z0, n0, z1, n1)
print('b=3/4: J_S,J_K,J_S-J_K =', j0, j1, j0 - j1)
print('b=3/4: T,L, m(T-L) =', t, lower, margin)


# Boundary controls concern the written pointwise level-inclusion argument;
# rejection of an open level is not claimed to disprove privacy a.e.
def check_closed_level(include_boundary):
    x = (Q(1, 2), Q(1, 2))
    h = (Q(1), Q(0))
    y = tuple(a + d for a, d in zip(x, h))
    require(sum(abs(v) for v in x) == 1 and sum(abs(v) for v in h) == 1, 'boundary setup')
    norm = sum(abs(v) for v in y)
    require(norm <= 2 if include_boundary else norm < 2, 'closed-boundary-excluded')


check_closed_level(True)
negative('replace K1=closed 2D with open 2D', 'closed-boundary-excluded', lambda: check_closed_level(False))


def check_initial_core(use_square):
    actual = square_shell_area(Q(0)) if use_square else diamond_area(Q(1))
    require(actual == square_shell_area(Q(0)), 'initial-core-changed')


check_initial_core(True)
negative('replace K0=C by D', 'initial-core-changed', lambda: check_initial_core(False))


def check_triangle(include):
    r = Q(1)
    altered = 4 * (c * c + 2 * c * r + (simplex(0, 0, r) if include else 0))
    require(diamond_area(2 * r) - altered == 1, 'missing-triangle-changed-area')


check_triangle(True)
negative('omit shifted triangle from S1', 'missing-triangle-changed-area', lambda: check_triangle(False))


def check_rectangle(xlo, xhi, yhi):
    require(xlo - c > 1, 'rectangle-enters-S1')
    require(xhi + yhi < 2, 'rectangle-leaves-K1')
    require(xhi - 1 - c < 1 and yhi < c, 'translated-rectangle-leaves-S1')


check_rectangle(Q(7, 4), Q(9, 5), Q(1, 20))
negative('move witness rectangle inside S1', 'rectangle-enters-S1',
         lambda: check_rectangle(Q(5, 4), Q(13, 10), Q(1, 20)))


def check_layer_weight(weight):
    k = Q(2)
    exact = (k + c) ** 2 - (k - c) ** 2
    require(weight == exact, 'layer-cake-integral-weight')


check_layer_weight(Q(4))
negative('use k instead of 2k for layer weight', 'layer-cake-integral-weight', lambda: check_layer_weight(Q(2)))


def check_uniform_lower(lnum):
    p = shift(scale(add(lnum, scale(mul(den, added_cost), -1)), 6), Q(2))
    require(p[0] > 0, 'uniform-gap-fails-at-m=2')


check_uniform_lower(l_num)
negative('reduce all-law lower bound cubic coefficient from 8 to 7', 'uniform-gap-fails-at-m=2',
         lambda: check_uniform_lower([Q(0), Q(1), Q(8), Q(7)]))


def check_signed(sign):
    require(m * (t + sign * lower) < 0, 'signed-aggregate-not-negative')


check_signed(-1)
negative('reverse the lambda term in the signed functional', 'signed-aggregate-not-negative', lambda: check_signed(1))
print('ALL REVIEWER EXACT CONTROLS COMPLETED')
signal.alarm(0)
