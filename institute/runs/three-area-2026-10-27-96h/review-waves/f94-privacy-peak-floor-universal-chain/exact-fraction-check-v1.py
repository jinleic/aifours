#!/usr/bin/env python3
"""Independent exact Fraction checks for f94; no author scripts or replays."""
from fractions import Fraction as F
from math import factorial

def diamond_abs_monomial(i, j):
    # Four reflected copies of the unit simplex beta integral.
    return 4 * F(factorial(i) * factorial(j), factorial(i + j + 2))

area = diamond_abs_monomial(0, 0)
euclidean = diamond_abs_monomial(2, 0) + diamond_abs_monomial(0, 2)
l1sq = diamond_abs_monomial(2, 0) + 2 * diamond_abs_monomial(1, 1) + diamond_abs_monomial(0, 2)
l1 = diamond_abs_monomial(1, 0) + diamond_abs_monomial(0, 1)
assert (area, euclidean, l1sq, l1) == (2, F(2, 3), 1, F(4, 3))
print('D integrals: area=%s, |x|_2^2=%s, |x|_1^2=%s, |x|_1=%s' % (area, euclidean, l1sq, l1))

# A monomial c*pi^p*(sqrt(3))^r, reduced exactly using (sqrt(3))^2=3.
class T:
    def __init__(self, c, p=0, r=0):
        q, r = divmod(r, 2)
        self.c = F(c) * (F(3) ** q)
        self.p, self.r = p, r
    def __mul__(self, other):
        other = other if isinstance(other, T) else T(other)
        return T(self.c * other.c, self.p + other.p, self.r + other.r)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, T) else T(other)
        return T(self.c / other.c, self.p - other.p, self.r - other.r)
    def __eq__(self, other):
        other = other if isinstance(other, T) else T(other)
        return (self.c, self.p, self.r) == (other.c, other.p, other.r)
    def __repr__(self):
        return '%s*pi^%d*sqrt(3)^%d' % (self.c, self.p, self.r)

pi = T(1, 1, 0)
sqrt3 = T(1, 0, 1)
A0 = pi
A1 = T(F(2, 3)) * pi / sqrt3
Ahalf = T(F(4, 3)) * pi / sqrt3
assert Ahalf / 2 == A1
C0sq = 2 * T(F(2, 3)) / A0
C1sq = 2 * T(F(5, 3)) / A1
Chalfsq = 2 * T(F(5, 6)) / Ahalf
assert C0sq == T(F(4, 3), -1)
assert C1sq == 5 * sqrt3 / pi
assert Chalfsq == T(F(5, 4)) * sqrt3 / pi
assert 2 * T(1) / T(2) == T(1)  # pure squared-l1 endpoint
print('A_0=pi; A_(lambda=1)=2*pi/(3*sqrt(3)); A_(theta=1/2)=4*pi/(3*sqrt(3)); A_(theta=1)=2')
print('C_0^2=4/(3*pi); C_(lambda=1)^2=5*sqrt(3)/pi; C_(theta=1/2)^2=5*sqrt(3)/(4*pi); C_(theta=1)^2=1')
print('C_D(lambda)=2/3+lambda; C_D(theta)=(2+theta)/3; theta samples:', [(str(t), str((2+t)/3)) for t in (F(0), F(1,2), F(1))])
# Positive-root equality of y0*C_D=C/2, checked after squaring.
y0sq = T(F(3,4), -1)
assert y0sq * T(F(2,3)) * T(F(2,3)) == C0sq / 4
assert y0sq * pi == T(F(3,4))
assert y0sq * 4 * pi == T(3)
print('lambda=0: pi*y0^2=3/4; pi*(y0*C_D)^2=1/3; pi*(2*y0)^2=3; y0*C_D=C/2')

# First-norm stationary point: C^3=2, y0^3=1/32,
# (y0*C^2)^3=1/8; positivity makes 2*y0*C^2=1.
Ccube, ycube = F(2), F(1,32)
assert ycube * Ccube**2 == F(1,8)
assert (F(4,3) * F(1,4), F(2,3)) == (F(1,3), F(2,3))
print('first norm: C^3=2; y0^3=1/32; 2*y0*C^2=1; floor/core fractions=1/3,2/3')

# Translation G(a)-G(0)=4 integral_0^a (a-u)(1-u) du, 0<=a<=1.
for a in (F(0), F(1,4), F(1,2), F(1)):
    integral = 4*(a*a - (a+1)*a*a/2 + a*a*a/3)
    assert integral == 2*a*a - F(2,3)*a*a*a
    assert integral >= 0 and (a == 0 or integral > 0)
assert 2*F(1) - F(2,3) == 2*F(1)**2 - F(2,3)*F(1)**3
print('diamond translated-first-norm G(a)-G(0): exact polynomial and endpoint checked')

# Independent geometric law: factorial moments E K=m, E K(K-1)=2m^2,
# E K(K-1)(K-2)=6m^3, K>=0 geometric with P(K=k)=(1-b)b^k.
def moments(q, m):
    e1, e2, e3 = m, m+2*m*m, m+6*m*m+6*m*m*m
    return (q*q+2*q*e1+e2, q**3+3*q*q*e1+3*q*e2+e3)
b, q = F(1,16), F(1,4)
m = b/(1-b)
M2, M3 = moments(q, m)
N = 8
S2 = sum((1-b)*b**k*(q+k)**2 for k in range(N+1)) + b**(N+1)*moments(q+N+1,m)[0]
S3 = sum((1-b)*b**k*(q+k)**3 for k in range(N+1)) + b**(N+1)*moments(q+N+1,m)[1]
assert (S2,S3) == (M2,M3)
print('geometric diamond-shell M2,M3 at rational b=1/16,q=1/4:', M2, M3, 'cost=', F(2,3)*M3/M2)

# All exponents are rational; smaller b means a larger exponent is lower order.
assert F(1,8)+F(1,4) == F(3,8) > F(1,3)
assert F(1,12)+F(1,4) == F(1,3)
assert F(1,8)-F(1,6) == F(-1,24)
assert F(1,3)-F(5,18) == F(1,18)
assert -F(1,2)+2*F(5,18) == F(1,18)
assert F(1,18)+F(5,18) == F(1,3)
assert F(1,18)-2*F(5,18) == -F(1,2)
assert F(5,18)-F(1,4) == F(1,36)
assert 3*F(5,18) == F(5,6) < 1
assert 2*F(1,3)-F(1,2) == F(1,6)
for k in (24,48,96):
    w = F(1, 2**(k//8))
    relative = F(1, 2**(k//24))
    ratio = F(2**(k//24))
    assert w * 2**(k//6) == ratio
    print('counterexample k=%d: weight=%s relative_contamination=%s ratio_to_b^(1/6)=%s' % (k,w,relative,ratio))
for k in (36,72,144):
    w = F(1, k * 2**(k//18))
    ratio = F(2**(k//6-k//18), k)
    assert w * 2**(k//6) == ratio
    print('sharp k=%d: weight=%s relative_contamination=%s ratio_to_b^(1/6)=%s' % (k,w,F(1,k),ratio))
print('exponents: square core=1/4; mean core=1/3; overlap=1/18; intermediate radius=5/18; radius ratio=1/36; critical mix=1/18+5/18=1/3')
print('ALL EXACT FRACTION ASSERTIONS PASSED (not a proof of trigonometric identities or asymptotic estimates)')
