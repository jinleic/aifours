#!/usr/bin/env python3
"""Independent bounded rational controls for the f250 review; not author code."""
from fractions import Fraction as F
from math import comb
import signal

signal.alarm(120)


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    print('PASS', label)


def polygon_for_parallel(knots, radius):
    # Exact D4 boundary from an independently specified octant, counterclockwise.
    t = knots[-1][0]
    arc = [(f + radius, y) for y, f in knots]
    if radius:
        arc.append((t + radius / 2, t + radius / 2))
    arc += [(y, x) for x, y in reversed(arc[:-1])]
    points = []
    for k in range(4):
        for x, y in arc[:-1]:
            for _ in range(k):
                x, y = -y, x
            if not points or (x, y) != points[-1]:
                points.append((x, y))
    return points


def polygon_integrals(points):
    cross_sum = F(0)
    moment_sum = F(0)
    for (x, y), (u, v) in zip(points, points[1:] + points[:1]):
        cross = x*v - u*y
        cross_sum += cross
        moment_sum += cross*(x*x + x*u + u*u + y*y + y*v + v*v)
    return cross_sum/2, moment_sum/12


def coefficient_b(knots):
    answer = F(0)
    for (a, fa), (c, fc) in zip(knots, knots[1:]):
        answer += (c-a)*(fa*fa + fa*fc + fc*fc)/3 + (c**3-a**3)/3
    return 8*answer


def geom_moments(b):
    # Recurrence from shifting sum_j j^k b^j, not the author's symbolic cell.
    m = b/(1-b)
    result = [F(1)]
    for k in range(1, 5):
        result.append(m*sum(comb(k, a)*result[a] for a in range(k)))
    return result


def interval_moments_for_offset(base, g):
    # E[(base+G)^2], E[(base+G)^4] from the binomial theorem.
    return tuple(sum(comb(k, j)*base**(k-j)*g[j] for j in range(k+1))
                 for k in (2, 4))


def diamond_cost(base, g):
    second, fourth = interval_moments_for_offset(base, g)
    return fourth/(3*second)


square = [(F(0), F(1, 2)), (F(1, 2), F(1, 2))]
nonconvex = [(F(0), F(3, 2)), (F(1, 4), F(5, 4)),
             (F(3, 4), F(5, 4)), (F(1), F(1))]
point = [(F(0), F(0))]

for name, knots in [('square', square), ('nonconvex', nonconvex), ('point', point)]:
    t = knots[-1][0]
    area, moment = polygon_integrals(polygon_for_parallel(knots, F(0)))
    linear_moment = coefficient_b(knots)
    for r in (F(0), F(1, 3), F(1, 2), F(1), F(2)):
        measured_a, measured_q = polygon_integrals(polygon_for_parallel(knots, r))
        predicted_a = area + 8*t*r + 2*r*r
        predicted_q = (moment + linear_moment*r + (area+8*t*t)*r*r
                       + F(16, 3)*t*r**3 + F(2, 3)*r**4)
        check((measured_a, measured_q) == (predicted_a, predicted_q),
              f'{name} polygon area/moment at r={r}')
        if r == 1:
            check(measured_a != area + 8*t*r,
                  f'NEGATIVE {name}: omitting outer-triangle area is detected')
            check(measured_q != predicted_q - F(2, 3)*r**4,
                  f'NEGATIVE {name}: omitting quartic moment is detected')

pts = polygon_for_parallel(nonconvex, F(0))
turns = []
for i in range(len(pts)):
    a, c, d = pts[i-1], pts[i], pts[(i+1) % len(pts)]
    turns.append((c[0]-a[0])*(d[1]-c[1])-(c[1]-a[1])*(d[0]-c[0]))
check(any(z < 0 for z in turns) and any(z > 0 for z in turns),
      'nonconvex profile has both signed turn orientations')
check(polygon_integrals(polygon_for_parallel(square, F(0))) == (F(1), F(1, 6))
      and coefficient_b(square) == F(4, 3), 'square core exact polygon invariants')

for b in (F(1, 5), F(1, 2), F(2, 3), F(3, 4)):
    g = geom_moments(b)
    m = b/(1-b)
    closed = [F(1), m, m+2*m*m, m+6*m*m+6*m**3,
              m+14*m*m+36*m**3+24*m**4]
    check(g == closed, f'geometric moments at b={b}')
    check(g[4] != m+13*m*m+36*m**3+24*m**4,
          f'NEGATIVE changed fourth-moment coefficient at b={b}')

# N=1 and singleton first core: all positive mass comes from later shells.
g = geom_moments(F(1, 2))
z_point = 2*g[2]
q_point = F(2, 3)*g[4]
check((z_point, q_point, q_point/z_point) == (F(6), F(50), F(25, 3)),
      'N=1 singleton core has nonzero exact tail mass and ratio')

# A nonparallel three-prefix K0=square, K1=2D, K2=3D, tail (3+j)D.
b = F(2, 3)
g = geom_moments(b)
m = g[1]
t2, t3, t4 = g[2:]
t, area, moment, lin = F(3, 2), F(18), F(54), F(72)
z_tail = area + 8*t*m + 2*t2
q_tail = moment + lin*m + (area+8*t*t)*t2 + F(16, 3)*t*t3 + F(2, 3)*t4
z_n = (1-b)*(F(1) + b*F(8)) + b*b*z_tail
q_n = (1-b)*(F(1, 6) + b*F(32, 3)) + b*b*q_tail
z_direct = (1-b) + 2*(t2+2*m+b)
q_direct = (1-b)/6 + F(2, 3)*(t4+4*t3+6*t2+4*m+b)
check((z_n, q_n) == (z_direct, q_direct),
      'N=3 nonparallel prefix normalized tail versus independent index moments')
check(z_n != (1-b)*(F(1)+b*F(8)+b*b*z_tail),
      'NEGATIVE extra (1-b) on tail mass is detected')
check(q_n != (1-b)*(F(1, 6)+b*F(32, 3)+b*b*q_tail),
      'NEGATIVE extra (1-b) on tail moment is detected')

# A closed-boundary equality case, and an intended open-diamond negative.
x, y = F(1, 2), F(1, 2)
check(x+y == 1 and 2*(x*x+y*y) == 1,
      'cutoff equality point lies on both unit diamond and cost-ball boundary')
check(not (x+y < 1), 'NEGATIVE open diamond loses the cutoff boundary point')
# K0=[-1/2,1/2]^2, K1=[-1,1]^2: diagonal radius test alone misses a forced axis point.
check(F(1) >= F(1, 2)+F(1, 2) and F(1, 2)+1 > 1,
      'NEGATIVE diagonal-radius-only inclusion misses forced axis boundary')

# Two distinct self-consistent convex diamond profiles, both below the actual
# product-Laplace bound at b=1/2; the worse cannot be globally optimal.
g = geom_moments(F(1, 2))
q_a, q_b = F(7, 10), F(4, 5)
r_a, r_b = diamond_cost(q_a, g), diamond_cost(q_b, g)
# ln(2)=2*sum_{k>=0} (1/3)^(2k+1)/(2k+1).
# Bound the k>=3 remainder by replacing all its denominators by 7.
log2_upper = 2*(F(1, 3)+F(1, 81)+F(1, 1215)+F(1, 7*3**7)/F(8, 9))
check(log2_upper < F(6932, 10000), 'rational strict upper bound for ln(2)')
check(q_a*q_a < r_a < r_b < 4/(log2_upper*log2_upper) and q_b*q_b < r_b,
      'two B6 candidates under product-Laplace bound have strictly different costs')
print('DIAMOND_B6_COSTS', r_a, r_b, 'LOG2_UPPER', log2_upper)
print('NEGATIVE rationale: radius-4/5 candidate satisfies B6 and the U bound but')
print('is beaten by the radius-7/10 feasible candidate; hence B6+U is not sufficient.')
print('All checks are exact rational arithmetic; geometric constructions are controls, not proofs.')
