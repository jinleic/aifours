#!/usr/bin/env python3
"""Independent exact-rational controls; not a proof of the all-law theorem."""
from fractions import Fraction as Q
from math import comb
import signal

signal.alarm(100)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c * x for x in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def power(p, n):
    out = [Q(1)]
    for _ in range(n):
        out = mul(out, p)
    return out


def compose(p, q):
    out = [Q(0)]
    for i, x in enumerate(p):
        out = add(out, scale(power(q, i), x))
    return out


def integral(p, a, b):
    return sum(c * (b ** (i + 1) - a ** (i + 1)) / (i + 1)
               for i, c in enumerate(p))


def octant_polygon(r):
    # D4 profile t=1: F(y)=3/2-y for y<=1/2, F(y)=1 thereafter.
    # Its outward boundary is nonconcave.  Formula by shoelace, not strip integration.
    v = [(Q(0), Q(0)), (Q(3, 2) + r, Q(0)),
         (Q(1) + r, Q(1, 2)), (Q(1) + r, Q(1)),
         (Q(1) + r / 2, Q(1) + r / 2)]
    twice_area = Q(0)
    twelve_moment = Q(0)
    for (x, y), (xx, yy) in zip(v, v[1:] + v[:1]):
        cross = x * yy - xx * y
        twice_area += cross
        twelve_moment += cross * (x*x + x*xx + xx*xx + y*y + y*yy + yy*yy)
    return 8 * twice_area / 2, 8 * twelve_moment / 12


def geometric_moments(b):
    # Direct index-shift identity for geometric moments, not author code.
    m = b / (1 - b)
    moments = [Q(1)]
    for k in range(1, 5):
        moments.append(m * sum(comb(k, j) * moments[j] for j in range(k)))
    return m, moments


def reject_false(condition, explanation):
    if condition:
        raise AssertionError('negative control unexpectedly passed: ' + explanation)
    print('NEGATIVE REJECTED:', explanation)


A, Q0 = octant_polygon(Q(0))
B = 8 * (integral([Q(9, 4), Q(-3), Q(2)], Q(0), Q(1, 2)) +
         integral([Q(1), Q(0), Q(1)], Q(1, 2), Q(1)))
assert A == 5 and B == 13
for r in [Q(0), Q(1, 2), Q(2, 3), Q(2)]:
    area, moment = octant_polygon(r)
    predicted_area = A + 8*r + 2*r*r
    predicted_moment = Q0 + B*r + (A + 8)*r*r + Q(16, 3)*r**3 + Q(2, 3)*r**4
    assert area == predicted_area and moment == predicted_moment
print('PASS: nonconvex-profile shoelace area and moment at four rational radii')
r = Q(2, 3)
_, true_moment = octant_polygon(r)
wrong_moment = Q0 + B*r + (A + 8)*r*r + Q(16, 3)*r**3 + r**4
assert wrong_moment - true_moment == r**4 / 3
reject_false(wrong_moment == true_moment, 'wrong r^4 coefficient: exact excess r^4/3')

for b in [Q(1, 100), Q(1, 3), Q(2, 3), Q(3, 4), Q(99, 100)]:
    m, M = geometric_moments(b)
    assert M[1] == m
    assert M[2] == m + 2*m*m
    assert M[3] == m + 6*m*m + 6*m**3
    assert M[4] == m + 14*m*m + 36*m**3 + 24*m**4
    # N=1, C={0}: all levels iD. Compare with an N=3 prefix 0,D,2D.
    z1, n1 = 2*M[2], Q(2, 3)*M[4]
    z3 = (1-b)*b*2 + b*b*2*(M[2] + 4*m + 4)
    n3 = (1-b)*b*Q(2, 3) + b*b*Q(2, 3)*(M[4] + 8*M[3] + 24*M[2] + 32*m + 16)
    assert z1 > 0 and n1 > 0 and z1 == z3 and n1 == n3
print('PASS: geometric moments, singleton N=1 positivity, and N=3 normalization')
b = Q(2, 3)
m, M = geometric_moments(b)
z3 = (1-b)*b*2 + b*b*2*(M[2] + 4*m + 4)
wrong_z = (1-b)*b*2 + b*2*(M[2] + 4*m + 4)
assert wrong_z-z3 == (b-b*b)*2*(M[2] + 4*m + 4) > 0
reject_false(wrong_z == z3, 'one missing factor b in tail weight')
reject_false(2*M[2] == 0, 'N=1 singleton has positive tail mass')

# Reconstruct S_i=[-1/2,1/2]^2+iD; m=b/(1-b), z=2m+1.
Z_m = [Q(1), Q(6), Q(4)]
N_m = [Q(1, 6), Q(23, 3), Q(94, 3), Q(40), Q(16)]
z = [Q(0), Q(1)]
m_of_z = [Q(-1, 2), Q(1, 2)]
Z_z, N_z = compose(Z_m, m_of_z), compose(N_m, m_of_z)
assert Z_z == [Q(-1), Q(1), Q(1)]
delta = [Q(-1), Q(5), Q(1)]
assert scale(N_z, 6) == add(scale(mul(power(z, 2), Z_z), 6), scale(delta, -1))
# For z=5+w, w>=0, both relevant comparison polynomials have positive coefficients.
assert compose(add(scale(Z_z, 3), scale(delta, -1)), [Q(5), Q(1)]) == [Q(38), Q(18), Q(2)]
cap_gap = add(add(scale(power(z, 4), 3), scale(power(z, 2), -4)), [Q(-1)])
assert compose(cap_gap, [Q(5), Q(1)]) == [Q(1774), Q(1460), Q(446), Q(60), Q(3)]
assert sum(c * Q(2)**i for i, c in enumerate(Z_m)) == 29
assert sum(c * Q(2)**i for i, c in enumerate(N_m)) == Q(4301, 6)
R = Q(4301, 174)
cap_upper = Q(562500, 23104)
assert R > cap_upper
print('PASS: square-profile exact z-polynomials, uniform cap-gap coefficients, boundary fraction')
reject_false(R <= cap_upper, 'f245 square at b=2/3 is outside even a rigorous upper bound for U')

boundary = (Q(1, 2), Q(1, 2))
assert sum(boundary) == 1 and sum(x*x for x in boundary) == Q(1, 2)
reject_false(sum(boundary) < 1, 'diagonal equality point lies in closed D, not open D')
print('PASS: completed exact controls')
