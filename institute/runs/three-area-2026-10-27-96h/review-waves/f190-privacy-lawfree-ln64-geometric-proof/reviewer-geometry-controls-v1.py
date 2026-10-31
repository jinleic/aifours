#!/usr/bin/env python3
"""Independent stdlib-only rational controls derived from geometry; not the author's cell."""
from fractions import Fraction as Q
from itertools import product

# Sparse polynomial ring over Q, implemented here to compare identities coefficientwise.
names = ('m', 't', 'd', 'y', 'z', 'u', 's', 'q', 'g', 'L')
N = len(names)
zero_exp = (0,) * N
class Poly:
    def __init__(self, terms=None):
        self.a = {k: Q(v) for k, v in (terms or {}).items() if v}
    @staticmethod
    def const(c):
        return Poly({zero_exp: Q(c)})
    @staticmethod
    def var(i):
        e = list(zero_exp); e[i] = 1
        return Poly({tuple(e): Q(1)})
    def __add__(self, other):
        if not isinstance(other, Poly): other = Poly.const(other)
        r = dict(self.a)
        for k, v in other.a.items(): r[k] = r.get(k, Q(0)) + v
        return Poly(r)
    __radd__ = __add__
    def __neg__(self): return Poly({k: -v for k, v in self.a.items()})
    def __sub__(self, other): return self + (-other if isinstance(other, Poly) else -Q(other))
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        if not isinstance(other, Poly): other = Poly.const(other)
        r = {}
        for a, x in self.a.items():
            for b, w in other.a.items():
                c = tuple(i+j for i, j in zip(a, b))
                r[c] = r.get(c, Q(0)) + x*w
        return Poly(r)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        r = Poly.const(1)
        for _ in range(n): r = r * self
        return r
    def deriv(self, i):
        r = {}
        for e, v in self.a.items():
            if e[i]:
                f = list(e); f[i] -= 1
                r[tuple(f)] = v * e[i]
        return Poly(r)
    def integral(self, i, lo, hi):
        if not isinstance(lo, Poly): lo = Poly.const(lo)
        if not isinstance(hi, Poly): hi = Poly.const(hi)
        r = Poly.const(0)
        for e, v in self.a.items():
            p = e[i] + 1
            f = list(e); f[i] = 0
            r += Poly({tuple(f): v / p}) * (hi**p - lo**p)
        return r
    def sub(self, i, v):
        if not isinstance(v, Poly): v = Poly.const(v)
        r = Poly.const(0)
        for e, a in self.a.items():
            f = list(e); f[i] = 0
            r += Poly({tuple(f): a}) * v**e[i]
        return r
    def value(self, values):
        ans = Q(0)
        for e, a in self.a.items():
            term = a
            for name, exponent in zip(names, e):
                if exponent: term *= Q(values.get(name, 0))**exponent
            ans += term
        return ans
    def is_zero(self): return not self.a

m,t,d,y,z,u,s,q,g,L = [Poly.var(i) for i in range(N)]
T2 = m + 2*m*m
T3 = m + 6*m*m + 6*m**3
T4 = m + 14*m*m + 36*m**3 + 24*m**4
v = m*(1+m)

def same(label, a, b):
    assert (a-b).is_zero(), label
    print('PASS', label, '(coefficientwise rational identity)')
def rejected(label, predicate):
    assert not predicate, label
    print('PASS negative:', label, '(rejected for stated reason)')

# One-dimensional strictness, including an equality case.
def line_moment(a,b): return (Q(b)**3-Q(a)**3)/3
cost_center = line_moment(-1,1)
cost_displaced = line_moment(-2,-1) + line_moment(1,2)
assert cost_center == Q(2,3) and cost_displaced-cost_center == 4
rejected('strictness when the centered sets agree a.e.', cost_center > cost_center)
print('PASS centered interval strictness (equal length 2, cost gap 4)')

# An isolated null point invalidates blindly replacing Minkowski sums by a.e. representatives.
# Square [-1,1]^2 plus D has x <= 2; the added point (10,0)+D has x >= 9.
assert Q(10)-1 > Q(1)+1
rejected('null singleton is harmless before taking a closed-diamond sum', Q(10)-1 <= Q(1)+1)
print('PASS null-set expansion witness (disjoint extra diamond area 2)')

# Exact phase-mixture integration over threshold intervals, at several values including boundaries.
def phase_integral(b, M, a_value):
    cuts = {b*M, M}
    p = a_value
    while p < M:
        if p > b*M: cuts.add(p)
        p /= b
    ordered = sorted(cuts)
    total = Q(0)
    for left,right in zip(ordered, ordered[1:]):
        mid = (left+right)/2
        n = 0
        while not a_value > mid*b**n: n += 1
        total += (right-left)*b**n
    return total
for yy in (Q(1),Q(1,4),Q(1,32),Q(3,100)):
    assert phase_integral(Q(1,4),Q(1),yy) == Q(3,4)*yy
rejected('phase mixture with missing factor 1-b', phase_integral(Q(1,4),Q(1),Q(1,32)) == Q(1,32))
print('PASS exact phase-mixture sample intervals (including threshold endpoints)')

# Integrate the tail triangle directly before inserting geometric moments.
triangle = ((t+s-q)**2 + (t+q)**2).integral(7,0,s*Q(1,2))
triangle_expected = t*t*s + t*s*s + Q(1,3)*s**3
same('triangle slice', triangle, triangle_expected)
rejected('triangle with missing cubic contribution', (triangle-(t*t*s+t*s*s)).is_zero())

# Strip integration of an independent shell mixture; E G^j are Tj.
strip_raw = (z**3+3*m*z*z+3*T2*z+T3-y**3)*Q(1,3) + y*y*(z-y+m)
strip_expanded = T2*z + m*(z*z+y*y) + z**3*Q(1,3) + y*y*z - Q(4,3)*y**3 + T3*Q(1,3)
same('strip moment integrand',strip_raw,strip_expanded)

# Substitute the full diamond profile and integrate, keeping the triangle contribution.
F = 2*t-y
zform = 8*(F-y).integral(3,0,t)+8*t*m+2*T2
nform = Q(2,3)*T4+Q(16,3)*t*T3+4*t*t*T2 + 8*(T2*F+m*(F*F+y*y)+F**3*Q(1,3)+y*y*F-Q(4,3)*y**3).integral(3,0,t)
M2 = g*g+2*m*g+T2
M4 = g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4
same('diamond total mass',zform,2*M2.sub(8,2*t))
same('diamond total moment',nform,Q(2,3)*M4.sub(8,2*t))
rejected('diamond mass with omitted triangle area', (zform-2*T2-2*M2.sub(8,2*t)).is_zero())

# Obtain B by differentiating the F-independent terms plus the moving endpoint G(t,t).
base = Q(2,3)*T4+Q(16,3)*t*T3+4*t*t*T2-L*(8*t*m+2*T2)
base += 8*(m*y*y-Q(4,3)*y**3+L*y).integral(3,0,t)
G = z**3*Q(1,3)+m*z*z+(T2+y*y-L)*z
B_independent = base.deriv(1) + 8*G.sub(4,t).sub(3,t)
B_expected = Q(16,3)*T3+16*t*T2+16*m*t*t-8*L*m
same('moving endpoint B', B_independent, B_expected)
# On the upper-clipped strip, differentiate F=2t-y.  Replace y by t-u,
# then impose its junction equation only after integrating.
partial_z = G.deriv(4)
upper_integrand = partial_z.sub(4,2*t-y).sub(3,t-u)
upper = 16*upper_integrand.integral(5,0,d)
junction = 2*t*t+2*d*d+2*m*(t+d)+T2
actual = (B_independent+upper).sub(9,junction)
C0 = m*Q(1,3)+Q(3,2)*m*m+m**3
P3 = Q(4,3)*d**3+2*m*d*d+m*m*d
expected = 16*(C0+t*v-P3)
same('rounded derivative from Leibniz integration',actual,expected)
same('rounded curvature factor',P3.deriv(2),(2*d+m)**2)
rejected('rounded derivative with upper facet boundary motion omitted', (B_independent.sub(9,junction)-expected).is_zero())
assert (C0+t*v).value({'m':Q(1,63),'t':Q(1,5)}) > 0
print('PASS positive d=0 matching derivative at rational test point')

P = g**5+5*m*g**4+(2*m+12*m*m)*g**3+(12*m**3-2*m)*g*g-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m)
same('diamond derivative numerator',M4.deriv(8)*M2-M4*M2.deriv(8),2*P)
rejected('diamond derivative with the g^2 term omitted', (M4.deriv(8)*M2-M4*M2.deriv(8)-2*(P-(12*m**3-2*m)*g*g)).is_zero())

# Small exact arithmetic spot checks; NOT the separate transcendental interval certificate.
mm = Q(1,63)
lo = Q(163006627735070347894185905345794,10**33)
hi = lo+Q(1,10**33)
t2 = mm+2*mm**2; t3=mm+6*mm**2+6*mm**3
assert t2<Q(1,50)<Q(4,25)<lo<hi<Q(1,2)
assert Q(16,3)*t3-8*hi*mm > 0
x = Q(3761763123,10**10); x2 = x+Q(1,10**10)
assert P.value({'m':mm,'g':0})>0 and P.value({'m':mm,'g':x})<0 and P.value({'m':mm,'g':x2})>0 and P.value({'m':mm,'g':1})>0
rejected('diamond derivative alleged positive at the left bracket', P.value({'m':mm,'g':x})>0)
rejected('lower-clip constant with its sign reversed', -(Q(16,3)*t3-8*hi*mm)>0)
print('PASS rational regime-domain and derivative-sign samples; no interval value proof')

# Distance-shell closed-shift diagnostic on an exact rational grid for a square core.
def ceilq(x): return -((-x.numerator)//x.denominator)
def dist(x,y): return max(abs(x)-Q(1,4),0)+max(abs(y)-Q(1,4),0)
grid=[Q(i,4) for i in range(-6,7)]
shifts=[(a,b) for a,b in product(grid,repeat=2) if abs(a)+abs(b)<=1]
count=0
for xx,yy in product(grid,repeat=2):
    k=ceilq(dist(xx,yy))
    for aa,bb in shifts:
        assert abs(k-ceilq(dist(xx+aa,yy+bb)))<=1
        count+=1
assert ceilq(2*dist(Q(5,4),0))-ceilq(2*dist(Q(1,4),0))==2
rejected('doubling shell exponent preserves every unit shift', abs(ceilq(2*dist(Q(5,4),0))-ceilq(2*dist(Q(1,4),0)))<=1)
print('PASS square-core shell finite-grid closed-shift diagnostic:',count,'pairs; not an all-shifts proof')
print('ALL CONTROL CHECKS COMPLETED; transcendental interval predicates remain conditional')
