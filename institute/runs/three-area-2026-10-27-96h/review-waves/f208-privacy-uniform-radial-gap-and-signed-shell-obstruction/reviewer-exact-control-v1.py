#!/usr/bin/env python3
"""Independent rational controls for the frozen f208 written review."""
from fractions import Fraction as Q
from math import comb, factorial

# Stirling recurrence, then E[(G)_j] = j! m^j for geometric G.
S = [[0] * 5 for _ in range(5)]
S[0][0] = 1
for n in range(1, 5):
    for j in range(1, n + 1):
        S[n][j] = j * S[n - 1][j] + S[n - 1][j - 1]


def translated_moment(p):
    # Dictionary (s-degree, m-degree) for E[(1+s+G)^p].
    d = {}
    for k in range(p + 1):
        for j in range(k + 1):
            for a in range(p - k + 1):
                key = (a, j)
                d[key] = d.get(key, 0) + comb(p, k) * comb(p - k, a) * S[k][j] * factorial(j)
    return {k: v for k, v in d.items() if v}


def derivative_s(poly):
    return {(a - 1, j): a * v for (a, j), v in poly.items() if a}


def product(left, right):
    out = {}
    for (a, j), v in left.items():
        for (c, k), w in right.items():
            key = (a + c, j + k)
            out[key] = out.get(key, 0) + v * w
    return {key: value for key, value in out.items() if value}


def difference(left, right):
    keys = left.keys() | right.keys()
    return {k: left.get(k, 0) - right.get(k, 0) for k in keys if left.get(k, 0) != right.get(k, 0)}


def geom_sum(z, start, p):
    # Sum z^i (start+i)^p; no finite truncation or float arithmetic.
    m = z / (1 - z)
    expectation = Q(0)
    for k in range(p + 1):
        gm = sum(Q(S[k][j] * factorial(j)) * m**j for j in range(k + 1))
        expectation += comb(p, k) * start**(p - k) * gm
    return expectation / (1 - z)


def cost_from_sums(s2, s4):
    return s4 / (3 * s2)


def shell_cost(start, b):
    return cost_from_sums(geom_sum(b, start, 2), geom_sum(b, start, 4))


def reject(predicate, label):
    assert not predicate, 'negative control unexpectedly accepted: ' + label
    print('NEGATIVE REJECTED:', label)


m2 = translated_moment(2)
m4 = translated_moment(4)
lhs = difference(product(derivative_s(m4), m2), product(m4, derivative_s(m2)))
p = {(k, 0): comb(5, k) for k in range(6)}
for j, row in [(1, [4, 21, 34, 22, 5]), (2, [5, 28, 36, 12]), (3, [2, 12, 12])]:
    for k, value in enumerate(row):
        p[k, j] = value
assert lhs == {k: 2 * v for k, v in p.items()}
assert all(v > 0 for v in p.values())
print('DERIVATIVE: complete exact polynomial identity and strictly positive coefficients')
wrong = dict(p)
wrong[1, 2] += 1
reject(lhs == {k: 2 * v for k, v in wrong.items()}, 'perturbed m^2*s coefficient breaks derivative identity')

b = Q(1, 2)
g = Q(1, 2)
delta = Q(1, 10)
lower = (4 * b / (1 + 2 * b)) * (Q(1, 4) + 2 * b / (1 - b)**2)
upper = shell_cost(g, b)
old, new = g + 1, g + 1 + delta
first_a = Q(2, 3) * (new**4 - old**4)
first_b = 2 * (new**2 - old**2)
first_at_lower = first_a - first_b * lower
assert lower == Q(17, 4) and upper == Q(1697, 204)
assert first_a == Q(14911, 15000) and first_b == Q(31, 50)
assert first_at_lower == -Q(12307, 7500)

def excess_sum(p):
    return geom_sum(b, g + delta, p) - geom_sum(b, g, p) - ((g + delta)**p - g**p)

sum_a, sum_b = Q(2, 3) * excess_sum(4), 2 * excess_sum(2)
assert sum_a == Q(50517, 5000) and sum_b == Q(51, 50)
assert sum_a - sum_b * upper == Q(2023, 1250)
assert Q(2023, 1250) - b * first_at_lower == Q(36583, 15000)
print('OBSTRUCTION:', 'L=', lower, 'U=', upper, 'first(L)=', first_at_lower,
      'total(U)=', sum_a - sum_b * upper, 'tail bound=', Q(36583, 15000))
reject(first_at_lower >= 0, 'first signed annulus is negative at all-law lower bound')
reject(sum_a - sum_b * upper <= 0, 'full weighted excess is positive at feasible-law upper bound')
reject(first_b == new**2 - old**2, 'omitting factor 2 in diamond-area difference')

# A finite two-gap example, using an exact geometric tail from the second gap onward.
def two_gap_cost(d0, d1):
    r0 = g
    r1 = g + 1 + d0
    r2 = r1 + 1 + d1
    def power_sum(p):
        return r0**p + b * r1**p + b**2 * geom_sum(b, r2, p)
    return cost_from_sums(power_sum(2), power_sum(4))

cost_two = two_gap_cost(Q(1, 10), Q(1, 5))
cost_one = two_gap_cost(Q(1, 10), Q(0))
cost_zero = two_gap_cost(Q(0), Q(0))
assert cost_two > cost_one > cost_zero == upper
print('FINITE GAPS: two-gap > one-gap > minimal, exact rational comparison')
reject(cost_two <= cost_one, 'reversing last-gap removal changes strict ordering')

# Infinite positive gaps: R_i=i+c(1-q^i), g=0. Expand exactly into geometric sums.
c, q = Q(1, 5), Q(1, 2)
def infinite_moment(p):
    return sum(Q(comb(p, j)) * (-c)**j * geom_sum(b * q**j, c, p - j) for j in range(p + 1))

inf_cost = cost_from_sums(infinite_moment(2), infinite_moment(4))
first_delta = c * (1 - q)
def one_gap_moment(p):
    return geom_sum(b, first_delta, p) - first_delta**p
one_zero_prefix = cost_from_sums(one_gap_moment(2), one_gap_moment(4))
minimal_zero_prefix = shell_cost(Q(0), b)
assert inf_cost > one_zero_prefix > minimal_zero_prefix
print('INFINITE GAPS:', 'J(infinite)=', inf_cost, 'J(first gap)=', one_zero_prefix,
      'J(minimal)=', minimal_zero_prefix)
reject(one_zero_prefix <= minimal_zero_prefix, 'zero-area-prefix first gap is still strictly costly')

# Evaluate the trial polynomial independently from the geometric factorial moments.
def moment_coefficients(p, x):
    out = [Q(0) for _ in range(p + 1)]
    for k in range(p + 1):
        for j in range(k + 1):
            out[j] += Q(comb(p, k) * S[k][j] * factorial(j)) * x**(p - k)
    return out

u = moment_coefficients(4, g)
v = moment_coefficients(2, g)
dpoly = [u[j] - Q(3, 2) * (v[j] if j < len(v) else 0) for j in range(5)]
assert dpoly == [-Q(5, 16), Q(2), Q(26), Q(48), Q(24)]
def dval(x):
    return sum(coef * x**j for j, coef in enumerate(dpoly))
assert dval(Q(1, 14)) == -Q(725, 38416)
assert dval(Q(1, 13)) == Q(8171, 456976)
assert shell_cost(g, Q(1, 15)) == Q(22501, 46452)
series = sum(Q(14, 5)**k / factorial(k) for k in range(6))
assert series == Q(720653, 46875) > 15 and Q(14, 5)**2 < 8
print('TRIAL:', 'Delta(1/14)=', dval(Q(1, 14)), 'Delta(1/13)=', dval(Q(1, 13)),
      'J(b=1/15)=', shell_cost(g, Q(1, 15)), 'exp lower=', series)
reject(dval(Q(1, 13)) < 0, 'm=1/13 is outside this trial\'s strict-negative region')

# Exact square+D inradius endpoint check at t=1/2; minimum, not maximum.
t = Q(1, 2)
axis_sq = (1 + t)**2
diagonal_sq = (1 + 2 * t)**2 / 2
assert min(axis_sq, diagonal_sq) == 2 and axis_sq == Q(9, 4)
print('SQUARE SUPPORT: axis^2=', axis_sq, 'diagonal^2=', diagonal_sq, 'inradius^2=', min(axis_sq, diagonal_sq))
reject(max(axis_sq, diagonal_sq) == min(axis_sq, diagonal_sq), 'maximum support endpoint overstates inradius')
print('COMPLETE: bounded exact controls only; universal proofs require written arguments')
