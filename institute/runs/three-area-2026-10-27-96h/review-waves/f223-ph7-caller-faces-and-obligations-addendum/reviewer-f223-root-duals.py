#!/usr/bin/env python3
"""Reviewer-authored finite exact control; no author files imported."""
from fractions import Fraction as F
from math import comb, floor, ceil

class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    @staticmethod
    def coerce(x):
        return x if isinstance(x, Interval) else Interval(x)
    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return Interval(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -self.coerce(other)
    def __rsub__(self, other):
        return self.coerce(other) + -self
    def __mul__(self, other):
        other = self.coerce(other)
        products = (self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi)
        return Interval(min(products), max(products))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = self.coerce(other)
        assert not (other.lo <= 0 <= other.hi), 'division interval contains zero'
        return self * Interval(1/other.hi, 1/other.lo)
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Interval(1)
        for _ in range(n):
            out *= self
        return out
    def maxabs(self):
        return max(abs(self.lo), abs(self.hi))
    def one(self):
        assert self.lo == self.hi
        return self.lo

class AD:
    def __init__(self, value, deriv=None):
        self.value = Interval.coerce(value)
        self.deriv = tuple(Interval.coerce(x) for x in (deriv or (0, 0, 0)))
    @staticmethod
    def coerce(x):
        return x if isinstance(x, AD) else AD(x)
    @staticmethod
    def variable(value, i):
        return AD(value, [int(i == j) for j in range(3)])
    def __add__(self, other):
        other = self.coerce(other)
        return AD(self.value + other.value, [a+b for a,b in zip(self.deriv, other.deriv)])
    __radd__ = __add__
    def __neg__(self):
        return AD(-self.value, [-x for x in self.deriv])
    def __sub__(self, other):
        return self + -self.coerce(other)
    def __rsub__(self, other):
        return self.coerce(other) + -self
    def __mul__(self, other):
        other = self.coerce(other)
        return AD(self.value * other.value,
                  [a*other.value + self.value*b for a,b in zip(self.deriv, other.deriv)])
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = AD(1)
        for _ in range(n):
            out *= self
        return out

def root_system(box):
    u,v,z = [AD.variable(box[i], i) for i in range(3)]
    p = 5*u + 2*v - 4
    q = 10*u*u + 10*u*v - 20*u + v*v - 8*v - 2*z + 10
    def coefficient(j):
        return sum((comb(5,i)*comb(2,j-i)*u**(5-i)*v**(2-(j-i))
                    for i in range(6) if 0 <= j-i <= 2), AD(0))
    P1,P2,P3,P4 = (coefficient(j) for j in (1,2,3,4))
    R1 = P1 - (1+z)**2*q
    R2 = P2 - (4+4*z)*q - (1+z)**2*p
    R3 = P3 - (6+2*z)*q - (4+4*z)*p - (1+z)**2
    R4 = P4 - 4*q - (6+2*z)*p - (4+4*z)
    return (R4, R3, R1 - 2*v*R2)

def inverse(matrix):
    n = len(matrix)
    M = [row[:] + [F(i == j) for j in range(n)] for i,row in enumerate(matrix)]
    for c in range(n):
        pivot = next(i for i in range(c,n) if M[i][c] != 0)
        M[c],M[pivot] = M[pivot],M[c]
        t = M[c][c]
        M[c] = [x/t for x in M[c]]
        for i in range(n):
            if i != c:
                t = M[i][c]
                M[i] = [x-t*y for x,y in zip(M[i],M[c])]
    return [row[n:] for row in M]

def norm_bound(C, J):
    return max(sum((Interval(int(i == k)) - sum((C[i][j]*J[j][k] for j in range(3)), Interval(0))).maxabs()
                   for k in range(3)) for i in range(3))

def elementary(values, upto):
    e = [AD(1)] + [AD(0) for _ in range(upto)]
    for value in values:
        for k in range(upto, 0, -1):
            e[k] = e[k] + value*e[k-1]
    return e

def grouped_duals(box):
    u,v,z = [AD.variable(box[i], i) for i in range(3)]
    e = elementary([v,v,u,u,u,u,u], 6)
    p = e[1] - 4
    q = e[2] - 4*e[1] + 10 - 2*z
    W = e[3] - 4*e[2] + (10-2*z)*e[1] + 12*z - 20
    E3 = e[4] - (6+2*z)*e[2] + (20+4*z)*e[1] + 3*z*z + 6*z - 45
    E2 = e[5] - (1+z)**2*p - (4+4*z)*q
    E1 = e[6] - (1+z)**2*q
    Z = E1 - 2*v*E2
    Wu,Wv = W.deriv[:2]
    Eu,Ev = E3.deriv[:2]
    Zu,Zv = Z.deriv[:2]
    det = Wu*Ev - Eu*Wv
    assert not (det.lo <= 0 <= det.hi), 'D0 determinant not separated from zero'
    a = (-Zu*Ev + Eu*Zv)/det
    b = (-Wu*Zv + Zu*Wv)/det
    # At the actual grouped root these are the candidate's F multipliers.
    s = 2*v.value
    S4 = 2*v.value + 2*u.value
    alpha = (2*v.value*u.value*u.value + 2*u.value*v.value*v.value)
    # e3(v,v,u,u) = 2*v^2*u + 2*v*u^2; e2(u,u,u,u) = 6*u^2.
    alpha = alpha - s*(6*u.value*u.value)
    Bj = v.value*v.value - s*s
    lam = a + alpha + b*S4 - W.value/F(2) - S4*E3.value
    mu = b + Bj - E3.value
    return det,a,b,lam,mu

def outward(i, scale=10**9):
    return f'[{floor(i.lo*scale)}/{scale},{ceil(i.hi*scale)}/{scale}]'

center = [F(334696976789746519,250000000000000000),
          F(208405938226799943,200000000000000000),
          F(410210220392063003,500000000000000000)]
r = F(1,10**16)
old = [F(1338787907,10**9), F(1042029691,10**9), F(820420441,10**9)]
assert all(abs(c-o)+r < F(1,10**7) for c,o in zip(center,old))
points = [Interval(x) for x in center]
box = [Interval(x-r,x+r) for x in center]
F0 = root_system(points)
FX = root_system(box)
J0 = [[entry.one() for entry in row.deriv] for row in F0]
C = inverse(J0)
J = [row.deriv for row in FX]
q = norm_bound(C,J)
res = max(abs(sum(C[i][j]*F0[j].value.one() for j in range(3))) for i in range(3))
assert q < F(1,10**8), 'contraction norm too large'
assert res + q*r < r, 'fixed-point map not nested'
assert res/(1-q) < F(1,10**18), 'root displacement bound too large'
wrong = C[:]
wrong[0],wrong[1] = wrong[1],wrong[0]
assert norm_bound(wrong,J) > 1, 'negative control failed to reject swapped inverse rows'
det,a,b,lam,mu = grouped_duals(box)
assert lam.lo > 0 and mu.lo > 0, 'root multiplier positivity not certified'
assert (a.hi < (-a).lo or (-a).hi < a.lo) and (b.hi < (-b).lo or (-b).hi < b.lo), 'negative control failed to distinguish reversed dual solve'
print('ROOT: interval Jacobian contraction norm < 1e-8; image nested; displacement < 1e-18; box strictly inside adopted root box')
print('D0 determinant:', outward(det))
print('LINKED DUALS a,b:', outward(a), outward(b))
print('ROOT MULTIPLIERS lambda,mu:', outward(lam), outward(mu))
print('NEGATIVES: swapped inverse rows fail contraction; reversed dual signs are disjoint from linked intervals')
print('LIMIT: own enclosures only; no equality or containment check against undisplayed pinned I_a,I_b; no Hessian/global cover run')
