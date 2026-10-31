#!/usr/bin/env python3
"""Exact checks for the universal no-two-cycle reduction at z=8/9.

1. SymPy polynomial identities: seventh-rate splitting of q, E4, E3; the
   slack K=E3-E4*S4=E+x*D with E*A-B*D=h0*A-h1*B; the beta2-cancellation in D;
   the bounds A<=Abar, D<=Dbar; and the elementary inequality used when f1<4.
2. Recomputes the girth-four Qpol/Hpol coefficient digests and compares them
   with the pinned girth-four certificate (the only imported computer check).
3. A complete exact integer Bernstein selector cover of the three-parameter
   residual statement NOT(Abar>0 and Dbar>0 and f1>=4).
No floating arithmetic is used in any check.
"""
import hashlib, itertools, json, math, sys
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S

R = S.Rational
# ---------- 1. identities ----------
r = S.symbols('r1:7', positive=True); x = S.symbols('x', positive=True)
def esym(vs, k): return sum(S.prod(c) for c in itertools.combinations(vs, k)) if k else S.Integer(1)
f = [esym(r, k) for k in range(5)]
e7 = [esym(list(r) + [x], k) for k in range(5)]
for k in range(1, 5): assert S.expand(e7[k] - (f[k] + x * f[k - 1])) == 0
p7 = e7[1] - 4
q7 = e7[2] - 4 * e7[1] + R(74, 9)
E4 = e7[3] - 4 * e7[2] + R(74, 9) * e7[1] - R(28, 3)
E3 = e7[4] - R(70, 9) * e7[2] + R(212, 9) * e7[1] - R(1007, 27)
A = f[2] - 4 * f[1] + R(74, 9); B = f[3] - 4 * f[2] + R(74, 9) * f[1] - R(28, 3)
h0 = f[4] - R(70, 9) * f[2] + R(212, 9) * f[1] - R(1007, 27); h1 = f[3] - R(70, 9) * f[1] + R(212, 9)
assert S.expand(q7 - (A + x * (f[1] - 4))) == 0
assert S.expand(E4 - (A * x + B)) == 0
assert S.expand(E3 - (h0 + x * h1)) == 0
S4 = sum(r[:4])
D = h1 - A * S4; E = h0 - B * S4
assert S.expand((E3 - E4 * S4) - (E + x * D)) == 0
assert S.expand((E * A - B * D) - (h0 * A - h1 * B)) == 0
# characteristic matching with D(y)Q(y), z=8/9
yv, pp, qq, W, CW, C4 = S.symbols('y p q W CW C4')
target = S.Poly(S.expand(yv * ((yv + 1) ** 2 + R(8, 9)) ** 2 * (yv ** 2 + pp * yv + qq)), yv)
ee = S.symbols('e1:5')
char_hi = {6: ee[0], 5: ee[1], 4: ee[2] - W, 3: ee[3] - CW - C4}
sol = S.solve([S.Eq(char_hi[6], target.coeff_monomial(yv ** 6)), S.Eq(char_hi[5], target.coeff_monomial(yv ** 5))], [pp, qq], dict=True)[0]
assert S.expand(sol[pp] - (ee[0] - 4)) == 0 and S.expand(sol[qq] - (ee[1] - 4 * ee[0] + R(74, 9))) == 0
Wsol = S.solve(S.Eq(char_hi[4], target.coeff_monomial(yv ** 4).subs(sol)), W)[0]
assert S.expand(Wsol - (ee[2] - 4 * ee[1] + R(74, 9) * ee[0] - R(28, 3))) == 0
CWsol = S.solve(S.Eq(char_hi[3], target.coeff_monomial(yv ** 3).subs(sol)), CW)[0]
assert S.expand(CWsol + C4 - (ee[3] - R(70, 9) * ee[1] + R(212, 9) * ee[0] - R(1007, 27))) == 0
# two-group split of the six rates: a = r1..r4 (four smallest), r5,r6 (two largest)
al = [esym(r[:4], k) for k in range(5)]
be1 = r[4] + r[5]; be2 = r[4] * r[5]
K1 = al[3] - al[1] * al[2] + 4 * al[1] ** 2 - 16 * al[1] + R(212, 9)
K2 = al[2] - al[1] ** 2 + 4 * al[1] - R(70, 9)
assert S.expand(D - (K1 + be1 * K2)) == 0          # beta2 cancels
assert S.expand(A - ((al[2] - 4 * al[1] + R(74, 9)) + be1 * (al[1] - 4) + be2)) == 0
Abar_al = (al[2] - 4 * al[1] + R(74, 9)) + be1 * (al[1] - 4) + be1 ** 2 / 4
Dbar_al = 4 * al[1] ** 2 - 16 * al[1] + R(212, 9) - R(5, 6) * al[1] * al[2] + be1 * (al[2] - al[1] ** 2 + 4 * al[1] - R(70, 9))
assert S.expand((Abar_al - A) - (r[4] - r[5]) ** 2 / 4) == 0
assert S.expand((Dbar_al - D) - (al[1] * al[2] / 6 - al[3])) == 0
# Maclaurin witnesses used in the written proof (sums of nonnegative terms):
mac3 = S.expand(al[1] * al[2] - 6 * al[3])      # = sum_{i!=j} a_i^2 a_j - 3 sum_{i<j<k} ... checked below as positive-coefficient form
a = r[:4]
mac3_form = S.expand(sum(a[i] * (a[j] - a[k]) ** 2 for i in range(4) for j in range(4) for k in range(j + 1, 4) if i not in (j, k)) / 2)
assert S.expand(mac3 - mac3_form) == 0
assert S.expand(3 * al[1] ** 2 - 8 * al[2] - sum((a[i] - a[j]) ** 2 for i in range(4) for j in range(i + 1, 4))) == 0
assert S.expand(5 * f[1] ** 2 - 12 * f[2] - sum((r[i] - r[j]) ** 2 for i in range(6) for j in range(i + 1, 6))) == 0
# elementary case f1<4: A-(4-f1)^2 = f2+4f1-f1^2-70/9 <= -(7/12)f1^2+4f1-70/9 <= -58/63
assert S.expand(A - (4 - f[1]) ** 2 - (f[2] + 4 * f[1] - f[1] ** 2 - R(70, 9))) == 0
s1 = S.symbols('s1')
assert S.expand(-R(7, 12) * s1 ** 2 + 4 * s1 - R(70, 9) + R(58, 63) + R(7, 12) * (s1 - R(24, 7)) ** 2) == 0
print('identities PASS')

# ---------- 2. bind the imported girth-four certificate ----------
uu = S.symbols('u0:6', real=True); F1, F2, F3, F4 = S.symbols('f1 f2 f3 f4', real=True)
Ag = F2 - 4 * F1 + R(74, 9); Bg = F3 - 4 * F2 + R(74, 9) * F1 - R(28, 3)
qnum = S.expand(Ag * Ag - (F1 - 4) * Bg)
h0g = F4 - R(70, 9) * F2 + R(212, 9) * F1 - R(1007, 27); h1g = F3 - R(70, 9) * F1 + R(212, 9)
hnum = S.expand(h0g * Ag - h1g * Bg)
subs = dict(zip((F1, F2, F3, F4), [esym(uu, k) for k in (1, 2, 3, 4)]))
Qp = S.Poly(S.expand((81 * qnum).subs(subs)), *uu); Hp = S.Poly(S.expand((-243 * hnum).subs(subs)), *uu)
def digest(P):
    rows = [[list(k), str(int(c))] for k, c in sorted(P.as_dict().items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
G4 = json.loads((ROOT / 'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json').read_text())
assert digest(Qp) == G4['Q_coefficients_sha256'] and digest(Hp) == G4['H_coefficients_sha256']
assert (len(G4['Q_positive_compactified_binary_leaf_paths']), len(G4['H_positive_compactified_binary_leaf_paths'])) == (5332, 5334)
print('girth-four Qpol/Hpol digests match pinned certificate')

# ---------- 3. three-parameter residual certificate ----------
y, tau, gam = S.symbols('y tau gam', nonnegative=True)
be1s = y / 2 + gam; al2s = R(3, 8) * tau * y ** 2
PA = S.Poly(S.expand(144 * ((al2s - 4 * y + R(74, 9)) + be1s * (y - 4) + be1s ** 2 / 4)), y, tau, gam)
PD = S.Poly(S.expand(144 * (4 * y ** 2 - 16 * y + R(212, 9) - R(5, 6) * y * al2s + be1s * (al2s - y ** 2 + 4 * y - R(70, 9)))), y, tau, gam)
PF = S.Poly(S.expand(2 * (y + be1s - 4)), y, tau, gam)
polys = {'Abar': PA, 'Dbar': PD, 'f1minus4': PF}
assert all(c.q == 1 for P in polys.values() for c in P.coeffs())
def bern(P):
    dy, dt, dg = P.degree(y), P.degree(tau), P.degree(gam)
    c = {k: Fr(int(v)) for k, v in P.as_dict().items()}
    vals = {}
    for i in range(dy + 1):
        for m in range(dt + 1):
            for k in range(dg + 1):
                v = sum((c.get((i, j, k), 0) * Fr(math.comb(m, j), math.comb(dt, j)) for j in range(m + 1)), Fr(0))
                vals[(i, m, k)] = v / (math.comb(dy, i) * math.comb(dg, k))
    L = 1
    for v in vals.values(): L = math.lcm(L, v.denominator)
    arr = np.empty((dy + 1, dt + 1, dg + 1), dtype=object)
    for key, v in vals.items(): arr[key] = int(v * L)
    return arr
def split(Aa, axis):
    Aa = np.moveaxis(Aa, axis, 0); d = Aa.shape[0] - 1; levels = [Aa]
    while levels[-1].shape[0] > 1: levels.append(levels[-1][:-1] + levels[-1][1:])
    left = np.stack([levels[k][0] * (1 << (d - k)) for k in range(d + 1)])
    right = np.stack([levels[d - k][-1] * (1 << k) for k in range(d + 1)])
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)
start = {k: bern(P) for k, P in polys.items()}
stack = [('', start)]; leaves = []
while stack:
    path, arrs = stack.pop()
    if max(arrs['Abar'].flat) <= 0: leaves.append([path, 'Abar<=0']); continue
    if max(arrs['Dbar'].flat) <= 0: leaves.append([path, 'Dbar<=0']); continue
    if max(arrs['f1minus4'].flat) < 0: leaves.append([path, 'f1-4<0']); continue
    assert len(path) < 60, path
    ax = len(path) % 3; L = {}; Rr = {}
    for k, Aa in arrs.items():
        if Aa.shape[ax] > 1: L[k], Rr[k] = split(Aa, ax)
        else: L[k], Rr[k] = Aa, Aa
    stack.append((path + '1', Rr)); stack.append((path + '0', L))
leaves.sort()
counts = {lab: sum(1 for _, l in leaves if l == lab) for lab in ('Abar<=0', 'Dbar<=0', 'f1-4<0')}
def pdig(P):
    rows = [[list(k), str(int(c))] for k, c in sorted(P.as_dict().items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
out = ROOT / 'frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json'
out.write_text(json.dumps({
    'z': '8/9',
    'variables': 'y=alpha1 in (0,inf), tau in [0,1] with alpha2=(3/8)*tau*y^2, gam=beta1-y/2 in [0,inf)',
    'compactification': 'y=s/(1-s), gam=g/(1-g), times (1-s)^deg_y (1-g)^deg_gam; tau kept on [0,1]',
    'polynomials': {k: {'expr': str(P.as_expr()), 'degrees': [P.degree(y), P.degree(tau), P.degree(gam)], 'sha256': pdig(P)} for k, P in polys.items()},
    'split_axis': 'path depth modulo 3 (0=s,1=tau,2=g); bit 0=lower half, 1=upper half',
    'selectors': 'Abar<=0: all Bernstein coefficients <=0; Dbar<=0: all <=0; f1-4<0: all <0',
    'leaf_counts': counts, 'leaves': leaves,
    'imported': {'girth4_certificate_sha256_Q': G4['Q_coefficients_sha256'], 'girth4_certificate_sha256_H': G4['H_coefficients_sha256']},
}, indent=1) + '\n')
print('SymPy', S.__version__, 'exact 3D residual selector cover PASS; leaves', len(leaves), counts)
print('saved', out)
