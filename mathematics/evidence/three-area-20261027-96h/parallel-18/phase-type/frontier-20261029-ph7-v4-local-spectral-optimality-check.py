#!/usr/bin/env python3
"""Exact local all-topology spectral bound around the adopted v4 endpoint.

Only standard-library Fraction interval arithmetic and second-order automatic
differentiation are used. Root existence is an explicitly imported result;
this checker bounds the two dual constants over its frozen rational root box,
then proves positive comparison multipliers, negative z derivative and uniform
negative v-Hessian via a rational LDL congruence and interval diagonal dominance.
No floating arithmetic, external solver or unbounded search.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
CENTER = (Q(1338787907, 10**9), Q(1042029691, 10**9), Q(820420441, 10**9))
ROOT_RADIUS = Q(1, 10**7)
RHO = Q(sys.argv[1]) if len(sys.argv) > 1 else Q(1, 1000000)
DZ = Q(sys.argv[2]) if len(sys.argv) > 2 else Q(1, 1000000)
ROOT_CERT = ROOT / 'frontier-20261028-ph7-two-cycle-interval-certificate.json'
assert hashlib.sha256(ROOT_CERT.read_bytes()).hexdigest() == '2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88'

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, I): self.lo, self.hi = lo.lo, lo.hi; return
        self.lo = Q(lo); self.hi = self.lo if hi is None else Q(hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        b = I(other); return I(self.lo + b.lo, self.hi + b.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-I(other))
    def __rsub__(self, other): return I(other) - self
    def __mul__(self, other):
        b = I(other); p = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return I(min(p), max(p))
    __rmul__ = __mul__
    def __truediv__(self, other):
        b = I(other); assert b.hi < 0 or b.lo > 0, 'interval divisor contains zero'
        return self * I(1/b.hi, 1/b.lo)
    def __rtruediv__(self, other): return I(other) / self
    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        if k == 0: return I(1)
        out = I(1)
        for _ in range(k): out = out * self
        return out
    def absmax(self): return max(abs(self.lo), abs(self.hi))
    def pair(self): return [str(self.lo), str(self.hi)]

class AD:
    __slots__ = ('v', 'g', 'h', 'n')
    def __init__(self, v, n, g=None, h=None):
        self.v = I(v); self.n = n
        self.g = [I(0) for _ in range(n)] if g is None else g
        self.h = [[I(0) for _ in range(n)] for _ in range(n)] if h is None else h
    @staticmethod
    def variable(v, n, k):
        a = AD(v, n); a.g[k] = I(1); return a
    def lift(self, b):
        if isinstance(b, AD): assert self.n == b.n; return b
        return AD(b, self.n)
    def __add__(self, other):
        b = self.lift(other); n = self.n
        return AD(self.v+b.v, n, [self.g[i]+b.g[i] for i in range(n)], [[self.h[i][j]+b.h[i][j] for j in range(n)] for i in range(n)])
    __radd__ = __add__
    def __neg__(self):
        return AD(-self.v, self.n, [-v for v in self.g], [[-v for v in row] for row in self.h])
    def __sub__(self, other): return self + (-self.lift(other))
    def __rsub__(self, other): return self.lift(other) - self
    def __mul__(self, other):
        b = self.lift(other); n = self.n
        return AD(self.v*b.v, n, [self.g[i]*b.v+self.v*b.g[i] for i in range(n)],
                  [[self.h[i][j]*b.v+self.g[i]*b.g[j]+self.g[j]*b.g[i]+self.v*b.h[i][j] for j in range(n)] for i in range(n)])
    __rmul__ = __mul__
    def __truediv__(self, scalar):
        assert not isinstance(scalar, AD)
        return self * (I(1)/scalar)
    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        out = AD(1, self.n)
        for _ in range(k): out = out*self
        return out

def elementary(vs, maxk):
    one = vs[0]*0+1
    ee = [one]+[vs[0]*0 for _ in range(maxk)]
    for t, v in enumerate(vs):
        for k in range(min(t+1, maxk), 0, -1): ee[k] = ee[k]+v*ee[k-1]
    return ee

def quantities(vs, z):
    e = elementary(vs, 6); p = e[1]-4; q = e[2]-4*e[1]+10-2*z
    W = e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
    E3 = e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
    E2 = e[5]-(1+z)**2*p-(4+4*z)*q
    E1 = e[6]-(1+z)**2*q
    s = vs[0]+vs[1]; Z = E1-s*E2
    return W, E3, E2, E1, Z

def dual_box(root_box):
    u, v, z = [AD.variable(t, 3, k) for k, t in enumerate(root_box)]
    W, E3, _, _, Z = quantities([v, v, u, u, u, u, u], z)
    wu, wv = W.g[:2]; eu, ev = E3.g[:2]; zu, zv = Z.g[:2]
    det = wu*ev-wv*eu
    a = (-zu*ev+zv*eu)/det
    b = (-wu*zv+wv*zu)/det
    return a, b, det

u0, v0, z0 = CENTER
rbox = [I(t-ROOT_RADIUS, t+ROOT_RADIUS) for t in CENTER]
a, b, det = dual_box(rbox)
a0I, b0I, _ = dual_box([I(t) for t in CENTER])
assert a0I.lo == a0I.hi and b0I.lo == b0I.hi
a0, b0 = a0I.lo, b0I.lo

# The unknown exact endpoint belongs to rbox. Use its larger rational superset
# for |v_1,2 - V|<=rho, |v_3..7 - U|<=rho and z in [z*,z*+DZ].
box = [I(v0-ROOT_RADIUS-RHO, v0+ROOT_RADIUS+RHO)]*2 + [I(u0-ROOT_RADIUS-RHO, u0+ROOT_RADIUS+RHO)]*5
zbox = I(z0-ROOT_RADIUS, z0+ROOT_RADIUS+DZ)
assert box[1].hi < box[2].lo and box[0].lo > 0

def evaluate(vbox, zrange, av, bv):
    vs = [AD.variable(t, 8, k) for k, t in enumerate(vbox)]
    z = AD.variable(zrange, 8, 7)
    W, E3, E2, E1, Z = quantities(vs, z)
    s = vs[0]+vs[1]; S4 = sum(vs[:4]); K = E3-W*S4
    alpha = elementary(vs[:4], 3)[3]-s*elementary(vs[3:], 2)[2]
    B = vs[0]*vs[1]-s*s
    F = Z+W*av+E3*bv-E3*E3
    lam = alpha+av+S4*bv-W/2-S4*E3
    mu = B+bv-E3
    return F, lam, mu

F, lam, mu = evaluate(box, zbox, a, b)
assert lam.v.lo > 0 and mu.v.lo > 0, ('multipliers not positive', lam.v.pair(), mu.v.pair())
assert F.g[7].hi < 0, ('F_z not negative', F.g[7].pair())

# Exact point Hessian and exact rational unit-LDL preconditioner.
point_v = [I(v0)]*2+[I(u0)]*5
F0, _, _ = evaluate(point_v, I(z0), I(a0), I(b0))
B0 = [[-F0.h[i][j].lo for j in range(7)] for i in range(7)]
assert all(F0.h[i][j].lo == F0.h[i][j].hi for i in range(7) for j in range(7))
L = [[Q(int(i == j)) for j in range(7)] for i in range(7)]
d = []
for j in range(7):
    dj = B0[j][j]-sum(L[j][k]*L[j][k]*d[k] for k in range(j)); assert dj > 0
    d.append(dj)
    for i in range(j+1, 7): L[i][j] = (B0[i][j]-sum(L[i][k]*L[j][k]*d[k] for k in range(j)))/dj
R = [[Q(0) for _ in range(7)] for _ in range(7)]
for col in range(7):
    for i in range(6, -1, -1): R[i][col] = Q(int(i == col))-sum(L[j][i]*R[j][col] for j in range(i+1, 7))
assert all(sum(L[k][i]*R[k][j] for k in range(7)) == int(i == j) for i in range(7) for j in range(7))
assert all(sum(R[k][i]*B0[k][l]*R[l][j] for k in range(7) for l in range(7)) == (d[i] if i == j else 0) for i in range(7) for j in range(7))
BH = [[-F.h[i][j] for j in range(7)] for i in range(7)]
T = [[sum((BH[k][l]*R[k][i]*R[l][j] for k in range(7) for l in range(7)), I(0)) for j in range(7)] for i in range(7)]
margins = [T[i][i].lo-sum(T[i][j].absmax() for j in range(7) if j != i) for i in range(7)]
assert min(margins) > 0, ('interval congruence not diagonally dominant', [str(t) for t in margins])

# Exact algebraic identities for the comparison and stationary choice are
# written in the proof. Spot controls exercise the interval AD implementation.
xx = AD.variable(I(2, 3), 1, 0); ff = xx*xx*xx
assert ff.v.lo <= 8 <= 27 <= ff.v.hi and ff.g[0].lo <= 12 <= 27 <= ff.g[0].hi and ff.h[0][0].lo <= 12 <= 18 <= ff.h[0][0].hi
pointx = AD.variable(I(Q(7, 5)), 1, 0); pointf = pointx**3
assert pointf.v.lo == pointf.v.hi == Q(343, 125)
assert pointf.g[0].lo == pointf.g[0].hi == Q(147, 25)
assert pointf.h[0][0].lo == pointf.h[0][0].hi == Q(42, 5)

out = ROOT / 'frontier-20261029-ph7-v4-local-spectral-optimality-certificate-v1.json'
assert not out.exists(), 'refusing to overwrite certificate'
result = {
    'scope': 'local spectral optimality only; imported algebraic root existence; no global supremum claim',
    'root_center': [str(t) for t in CENTER], 'root_radius': str(ROOT_RADIUS),
    'root_certificate_sha256': '2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88',
    'spectral_neighborhood_radius': str(RHO), 'z_upper_extension': str(DZ),
    'rational_superset_v_boxes': [t.pair() for t in box], 'rational_superset_z_box': zbox.pair(),
    'dual_a_interval': a.pair(), 'dual_b_interval': b.pair(), 'stationarity_determinant_interval': det.pair(),
    'lambda_interval': lam.v.pair(), 'mu_interval': mu.v.pair(), 'F_z_interval': F.g[7].pair(),
    'rational_center_dual_a': str(a0), 'rational_center_dual_b': str(b0),
    'LDL_positive_pivots': [str(t) for t in d], 'congruence_R': [[str(t) for t in row] for row in R],
    'congruence_diagonal_dominance_margins': [str(t) for t in margins],
    'predicates': ['lambda>0', 'mu>0', 'F_z<0', 'R^T(-H_v F)R strictly positive diagonally dominant'],
}
out.write_text(json.dumps(result, indent=1)+'\n')
print('PASS exact local dual: rho=', RHO, 'delta_z=', DZ)
print('lambda>0, mu>0, F_z<0, uniform negative v-Hessian (rational LDL congruence)')
print('saved', out)
