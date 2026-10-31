#!/usr/bin/env python3
"""Reviewer-authored finite controls; no author code or global verifier."""
from fractions import Fraction as F
from itertools import combinations, product
from math import floor

# Q=A^2-(f1-4)B: direct sparse-polynomial degree argument for compactification.
N = 7  # six rates plus z
class Poly:
    def __init__(self, terms=None):
        self.t = {k:v for k,v in (terms or {}).items() if v}
    @classmethod
    def constant(cls, value):
        return cls({(0,)*N:F(value)})
    @classmethod
    def variable(cls, i):
        e = [0]*N; e[i] = 1
        return cls({tuple(e):F(1)})
    @classmethod
    def convert(cls, x):
        return x if isinstance(x, cls) else cls.constant(x)
    def __add__(self, other):
        out = dict(self.t)
        for k,v in self.convert(other).t.items(): out[k] = out.get(k,F(0)) + v
        return Poly(out)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-v for k,v in self.t.items()})
    def __sub__(self, other): return self + -self.convert(other)
    def __rsub__(self, other): return self.convert(other) - self
    def __mul__(self, other):
        out = {}
        for k,a in self.t.items():
            for l,b in self.convert(other).t.items():
                exp = tuple(x+y for x,y in zip(k,l))
                out[exp] = out.get(exp,F(0)) + a*b
        return Poly(out)
    __rmul__ = __mul__

def ep(xs,k):
    return sum((prod(xs[i] for i in indices) for indices in combinations(range(len(xs)),k)), Poly.constant(0))
def prod(xs):
    out = 1
    for x in xs: out = out*x
    return out

r = [Poly.variable(i) for i in range(6)]
z = Poly.variable(6)
f1,f2,f3,f4 = (ep(r,k) for k in (1,2,3,4))
A = f2 - 4*f1 + 10 - 2*z
B = f3 - 4*f2 + (10-2*z)*f1 + 12*z - 20
h1 = f3 - (6+2*z)*f1 + 20+4*z
h0 = f4 - (6+2*z)*f2 + (20+4*z)*f1 + 3*z*z+6*z-45
Q = A*A - (f1-4)*B
H = -(h0*A-h1*B)
assert max(sum(e[:6]) for e in Q.t) <= 4
assert max(sum(e[:6]) for e in H.t) <= 6
assert all(max(e[:6]) <= 2 for e in Q.t.keys() | H.t.keys())
assert not any(e[0] == e[1] == e[2] == 2 for e in Q.t)
assert not any(e[0] == e[1] == e[2] == e[3] == 2 for e in H.t)
print('POLYNOMIAL DEGREES: each rate <=2; Q total-rate degree <=4, H <=6')
print('CLOSED-FACE NEGATIVE: compactified Q vanishes identically where s1=s2=s3=1; H where s1=s2=s3=s4=1')

# Face predicate example, all z-coefficients identical, degree one in each s_i.
# Leaf [0,1/2]^6, P=s1: the only globally open-cube vertex has P=1/2.
vertices = list(product((F(0),F(1,2)), repeat=6))
inside = [v for v in vertices if all(0 < x < 1 for x in v)]
assert len(inside) == 1 and inside[0][0] == F(1,2)
assert all(v[0] >= 0 for v in vertices)
assert any(v[0] == 0 for v in vertices)
print('FACE NEGATIVE: P=s1 passes interior-vertex rule on [0,1/2]^6 but has infimum 0 and no positive closed-cell lower bound')
# P=t1 on [1/2,1]^6 has admissible interior vertex with zero value.
assert F(1,2) > 0 and F(1,2) < 1 and F(0) == 0
print('FACE REJECTION: local P=t1 on [1/2,1]^6 has zero at an admissible vertex, so vertex rule rejects it')

# Full binary path tree and closed sibling-face examples.
def complete(paths):
    if len(set(paths)) != len(paths) or not paths or any(set(p)-{'0','1'} for p in paths):
        return False
    pathset = set(paths)
    def visit(prefix):
        if prefix in pathset:
            return not any(p != prefix and p.startswith(prefix) for p in paths)
        if not any(p.startswith(prefix) for p in paths):
            return False
        return visit(prefix+'0') and visit(prefix+'1')
    return visit('')
assert complete(['00','01','1'])
assert not complete(['00','1'])
assert not complete(['0','0','1'])
assert not complete(['0','00','1'])
assert not complete(['0','2'])
assert 0 <= F(1,2) <= F(1,2) and F(1,2) <= F(1,2) <= 1
print('PATH NEGATIVES: missing child, duplicate, ancestor conflict, malformed path all rejected; shared half belongs to both cells')

# Sorting: equal touching boundaries and reversed midpoints cannot discard.
lo1,hi1,lo2,hi2 = F(1),F(2),F(0),F(1)
assert lo1 == hi2 and not lo1 > hi2 and lo1 <= hi2
lo1,hi1,lo2,hi2 = F(1),F(4),F(0),F(3)
assert (lo1+hi1)/2 > (lo2+hi2)/2 and lo1 <= 2 <= hi1 and lo2 <= 2 <= hi2
print('SORTING NEGATIVES: touching equal rates and reversed midpoints both retain a sorted point')

# Common Bernstein basis ratio and exact floor. N=-A and D=Fm.
num = [F(2),F(5)]; den = [F(1),F(3)]
Lq = min(n/d for n,d in zip(num,den))
assert Lq == F(5,3) and all(-n+Lq*d <= 0 for n,d in zip(num,den))
wrong = max(n/d for n,d in zip(num,den))
assert any(-n+wrong*d > 0 for n,d in zip(num,den))
Lv6 = F(7,4)
anchor = F(floor(1024*max(Lq,Lv6)),1024)
assert anchor == F(7,4)
L = 1-F(1,2**55); x = 1-F(1,2**56)
assert L < x < 1 and L > 1-F(1,2**54)
safe = F(floor(1024*L),1024)
assert safe == F(1023,1024) and safe <= x and 1 > x
print('ANCHOR NEGATIVES: max coefficient ratio fails; nearest-rounded 1 exceeds x while exact floor 1023/1024 is safe')

# Independent parameter endpoints are not reducible to a linked diagonal.
def predicate(a,b): return F(1,4)+a-b
assert predicate(F(1,2),F(1,2)) > 0 and predicate(F(0),F(1)) < 0
print('DUAL NEGATIVE: a=b=1/2 gives positive sign but independent corner (0,1) is negative')

# R3 A and D relaxations on rational sorted rates, plus equality case.
def es(xs,k): return sum((prod(xs[i] for i in ind) for ind in combinations(range(len(xs)),k)),F(0))
def r3(values,z):
    first,last = values[:4],values[4:]
    y = sum(first); aa2 = es(first,2); aa3 = es(first,3)
    bb1 = sum(last); bb2 = prod(last)
    f1 = sum(values); f2 = es(values,2); f3 = es(values,3)
    A = f2-4*f1+10-2*z
    h1 = f3-(6+2*z)*f1+20+4*z
    D = h1-A*y
    Ab = aa2-4*y+10-2*z+bb1*(y-4)+bb1*bb1/4
    Db = 4*y*y-16*y+20+4*z-F(5,6)*y*aa2+bb1*(aa2-y*y+4*y-6-2*z)
    assert Ab-A == (last[0]-last[1])**2/4 >= 0
    assert Db-D == y*aa2/6-aa3 >= 0
    return Ab-A,Db-D
z0 = F(410210220392063003,500000000000000000)
assert r3([F(1),F(2),F(3),F(4),F(5),F(6)],z0)[0] > 0
assert r3([F(1)]*6,z0) == (0,0)
# Stronger false e3 <= y*e2/7 fails at equal rates.
assert es([F(1)]*4,3) > sum([F(1)]*4)*es([F(1)]*4,2)/7
print('R3 NEGATIVE: /7 would reject equality case; /6 and beta-square gap reproduce exact relaxations')

# Local finite-difference controls for Y0 cubic and Y2 quadratic identities.
v = [F(1),F(6,5),F(13,10),F(4,3),F(7,5),F(3,2)]
f1,f2,f3 = (es(v,k) for k in (1,2,3))
A = f2-4*f1+10-2*z0
s = v[0]+v[1]; S3 = s+v[2]; S4 = S3+v[3]
def polys(x):
    vv = v+[x]
    e = [F(1)]+[es(vv,k) for k in range(1,8)]
    W = e[3]-4*e[2]+(10-2*z0)*e[1]+12*z0-20
    E3 = e[4]-(6+2*z0)*e[2]+(20+4*z0)*e[1]+3*z0*z0+6*z0-45
    p = e[1]-4; q = e[2]-4*e[1]+10-2*z0
    E2 = e[5]-(1+z0)**2*p-(4+4*z0)*q
    L4 = v[3]+v[4]+v[5]+x
    g = v[0]*v[1]*v[2]-W
    Y0 = e[7]-W*es(v[:4],4)+W*W*x/2-g*(E3-W*L4)
    Y2 = E2-W*es(v[:4],2)-S3*(E3-W*L4)
    return Y0,Y2
values = [polys(F(i)) for i in range(4)]
third = values[3][0]-3*values[2][0]+3*values[1][0]-values[0][0]
second = values[2][1]-2*values[1][1]+values[0][1]
assert third == -3*A*A and third != 3*A*A
assert second == 2*S3*A
print('TAIL NEGATIVE: Y0 third difference is -3A^2, not +3A^2; Y2 second difference is 2*S3*A')
print('LIMIT: finite controls and exact degree identities only; no global tree, leaf, verifier or author code executed')
