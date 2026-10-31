#!/usr/bin/env python3
"""Independent controls for f112; no author code or prior candidate is imported.

Exact rational/algebraic checks are separated from exploratory mpmath quadrature.
The finite grid check is a diagnostic, not a proof of continuous privacy.
"""
from fractions import Fraction as F
import mpmath as mp


def lin_product_integral(a, b, c, d, lo, hi):
    # Integral of (a*x+b)*(c*x+d) dx, with exact rational coefficients.
    a, b, c, d, lo, hi = map(F, (a, b, c, d, lo, hi))
    return (a*c*(hi**3-lo**3)/3 + (a*d+b*c)*(hi**2-lo**2)/2
            + b*d*(hi-lo))


def diamond_one_coordinate_abs(t):
    t = abs(F(t))
    if t >= 1:
        return 2*t
    return 2*(lin_product_integral(1, 1, -1, -t, -1, -t)
              + lin_product_integral(1, 1, 1, t, -t, 0)
              + lin_product_integral(-1, 1, 1, t, 0, 1))


def q(t):
    t = abs(F(t))
    return 2*t*t-F(2, 3)*t**3 if t <= 1 else 2*t-F(2, 3)


# Diamond marginals: density 2*(1-|x|) for unnormalised area measure.
one_norm = 4*(F(1, 2)-F(1, 3))
one_square = 4*(F(1, 3)-F(1, 4))
assert one_norm == F(2, 3) and one_square == F(1, 3)
assert 2*one_norm == F(4, 3) and 2*one_square == F(2, 3)
for t in [F(0), F(1, 4), F(3, 4), F(1), F(3, 2), F(10)]:
    assert diamond_one_coordinate_abs(t)-one_norm == q(t)
    assert 0 <= q(t) <= 2*t*t
for beta in [F(0), F(1, 10), F(1, 2)]:
    for x, y in [(F(0), F(0)), (F(1, 3), F(2, 3)),
                 (F(5, 4), F(-7, 3))]:
        r2 = x*x+y*y
        floor = F(2, 3)+2*r2-beta*(F(4, 3)+q(x)+q(y))
        assert floor >= F(2, 3)+r2-beta*F(4, 3)
print('EXACT diamond moments, translated norm polynomial, and negative-floor samples: OK')

# K_-a consists of four disks with disjoint interiors when a>=2*sqrt(tau).
# Treat tau symbolically via pi*tau^2=1/3 and coefficient arithmetic.
assert 4*F(1, 2)*F(1, 3) == F(2, 3)  # four integrals (pi/2)*tau^2
assert F(2, 3)*F(3, 4) == F(1, 2)    # (2/3)/A = tau/2; A=4/(3*tau)
assert F(1, 2)+F(1, 2) == 1          # disk core variance + macroscopic floor
assert F(2, 3)*F(3, 2) == 1          # theta=0: floor = tau, A=2/(3*tau)
print('EXACT separated disks and theta=0 core/floor coefficients: OK')

# At T=0, theta=-a, use q(phi)=cos(phi)+sin(phi). Store alpha*pi+beta.
q2 = (F(1, 2), F(1))                 # integral q^2 = pi/2+1
q4 = (F(3, 4), F(2))                 # integral q^4 = 3*pi/4+2
assert tuple(2*v for v in q2) == (F(1), F(2))        # area/a^2
assert tuple(F(4, 3)*v for v in q4) == (F(1), F(8, 3))  # L-moment/a^3
assert tuple(v/3 for v in q4) == (F(1, 4), F(2, 3))  # G/a^4
# Thus the hole-closing threshold obeys a^4=8/(3*pi+8).
# At a=1, G(-1/4,-1)=pi/8<2/3<G(0,-1), so K has a hole,
# crosses the coordinate axes, and excludes the origin.
assert F(11, 28) < F(2, 3)             # using pi < 22/7
print('EXACT T=0 polar area, first moment, and G coefficients: OK')

# Two disjoint non-origin closed diamonds, each radius 1/4, centered at (+/-3,0).
# All coordinates are integers in units 1/4. n is exactly their D-dilation index.
def n_index(x, y):
    d = min(abs(x-12)+abs(y), abs(x+12)+abs(y))
    return max(0, (d-1+3)//4)

steps = [(u, v) for u in range(-4, 5) for v in range(-4, 5)
         if abs(u)+abs(v) <= 4]
count = 0
for x in range(-16, 17):
    for y in range(-16, 17):
        n0 = n_index(x, y)
        for u, v in steps:
            assert abs(n_index(x+u, y+v)-n0) <= 1
            count += 1
assert n_index(-12, 0) == n_index(12, 0) == 0 and n_index(0, 0) == 3
print(f'EXACT rational-grid disconnected-core shell diagnostic: {count} ordered pairs OK')

# Independent polar numerical quadrature: diagnostics only, not an exact certificate.
mp.mp.dps = 25

def polar_integrals(theta, threshold, only_g=False):
    theta, threshold = mp.mpf(theta), mp.mpf(threshold)
    if threshold <= 0 and theta >= 0:
        return mp.mpf('0') if only_g else (mp.mpf('0'),)*3
    if theta < 0 and threshold <= -theta*theta/2:
        return mp.mpf('0') if only_g else (mp.mpf('0'),)*3
    half = mp.pi/4
    if threshold < 0:
        half = min(half, mp.acos(mp.sqrt(-2*threshold/(theta*theta))))
    def integrands(phi):
        Q = mp.sqrt(2)*mp.cos(phi)
        disc = max(mp.mpf('0'), theta*theta*Q*Q + 4*threshold)
        root = mp.sqrt(disc)
        lo = max(mp.mpf('0'), (-theta*Q-root)/2)
        hi = max(mp.mpf('0'), (-theta*Q+root)/2)
        A = (hi**2-lo**2)/2
        B = Q*(hi**3-lo**3)/3
        G = (threshold*(hi**2-lo**2)/2-(hi**4-lo**4)/4
             -theta*Q*(hi**3-lo**3)/3)
        return A, B, G
    if only_g:
        return 8*mp.quad(lambda p: integrands(p)[2], [0, half])
    return tuple(8*mp.quad(lambda p: integrands(p)[i], [0, half]) for i in range(3))


def threshold(theta):
    theta = mp.mpf(theta)
    low = -theta*theta/2 if theta < 0 else mp.mpf('0')
    high = max(mp.mpf('1'), low+1)
    while polar_integrals(theta, high, only_g=True) < mp.mpf(2)/3:
        high = 2*high+1
    for _ in range(40):
        mid = (low+high)/2
        if polar_integrals(theta, mid, only_g=True) < mp.mpf(2)/3:
            low = mid
        else:
            high = mid
    return (low+high)/2


tau = 1/mp.sqrt(3*mp.pi)
for theta in [-2, -1, 0, 1, 5]:
    t = threshold(theta)
    area, first, g = polar_integrals(theta, t)
    v = first/area
    assert abs(g-mp.mpf(2)/3) < mp.mpf('1e-9')
    if theta == -2:
        assert abs(t-(-2+tau)) < mp.mpf('1e-9') and abs(v-2) < mp.mpf('1e-9')
    if theta == -1:
        assert -mp.mpf(1)/4 < t < 0
    if theta == 0:
        assert abs(t-2*tau) < mp.mpf('1e-9')
        assert abs(v-8*mp.sqrt(2*tau)/(3*mp.pi)) < mp.mpf('1e-9')
    print('NUMERIC theta=%s T=%s area=%s V=%s' %
          (theta, mp.nstr(t, 11), mp.nstr(area, 11), mp.nstr(v, 11)))

# Check implicit derivative in the connected-hole regime and for positive theta.
for theta in [-1, 1]:
    h = mp.mpf('0.0002')
    t = threshold(theta)
    area, first, _ = polar_integrals(theta, t)
    finite_difference = (threshold(theta+h)-threshold(theta-h))/(2*h)
    assert abs(finite_difference-first/area) < mp.mpf('0.00001')
    print('NUMERIC theta=%s derivative=%s moment=%s' %
          (theta, mp.nstr(finite_difference, 10), mp.nstr(first/area, 10)))
print('NUMERIC polar diagnostics: OK (not interval-certified)')
