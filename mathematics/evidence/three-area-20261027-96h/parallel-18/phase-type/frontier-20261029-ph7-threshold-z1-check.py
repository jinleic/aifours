#!/usr/bin/env python3
"""Exact certificate of the crude four-condition infeasibility (Lemma C) at
z1 = 1753/2000 = 0.8765, with all identities verified for symbolic z.

(1) SymPy identities for a symbolic ratio z: characteristic matching constants,
    seventh-rate splitting, K=E+xD, EA-BD=h0A-h1B, the residual decomposition
    D=K1(z)+beta1*K2(z) (beta2 cancels), Abar-A, Dbar-D, and the case-(a) bound.
(2) Integer six-dimensional Bernstein covers proving Qpol(z1)>0 and Hpol(z1)>0
    on the open positive six-orthant (compactified, NumPy object integers).
(3) Integer three-parameter residual selector cover at z1.
No floating arithmetic in any check.
"""
import hashlib, itertools, json, math, sys
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S
R = S.Rational
Z1 = R(1753, 2000)
z = S.symbols('z', positive=True)

# ---------- (1) identities for symbolic z ----------
yv, pp, qq, W, CW, C4 = S.symbols('y p q W CW C4')
ee = S.symbols('e1:5')
target = S.Poly(S.expand(yv * ((yv + 1) ** 2 + z) ** 2 * (yv ** 2 + pp * yv + qq)), yv)
sol = S.solve([S.Eq(ee[0], target.coeff_monomial(yv ** 6)), S.Eq(ee[1], target.coeff_monomial(yv ** 5))], [pp, qq], dict=True)[0]
assert S.expand(sol[pp] - (ee[0] - 4)) == 0
assert S.expand(sol[qq] - (ee[1] - 4 * ee[0] + 10 - 2 * z)) == 0
Wsol = S.solve(S.Eq(ee[2] - W, target.coeff_monomial(yv ** 4).subs(sol)), W)[0]
assert S.expand(Wsol - (ee[2] - 4 * ee[1] + (10 - 2 * z) * ee[0] + 12 * z - 20)) == 0
CWsol = S.solve(S.Eq(ee[3] - CW - C4, target.coeff_monomial(yv ** 3).subs(sol)), CW)[0]
assert S.expand(CWsol + C4 - (ee[3] - (6 + 2 * z) * ee[1] + (20 + 4 * z) * ee[0] + 3 * z ** 2 + 6 * z - 45)) == 0
r = S.symbols('r1:7', positive=True); x = S.symbols('x', positive=True)
def esym(vs, k): return sum(S.prod(c) for c in itertools.combinations(vs, k)) if k else S.Integer(1)
f = [esym(r, k) for k in range(5)]; e7 = [esym(list(r) + [x], k) for k in range(5)]
q7 = e7[2] - 4 * e7[1] + 10 - 2 * z
E4 = e7[3] - 4 * e7[2] + (10 - 2 * z) * e7[1] + 12 * z - 20
E3 = e7[4] - (6 + 2 * z) * e7[2] + (20 + 4 * z) * e7[1] + 3 * z ** 2 + 6 * z - 45
A = f[2] - 4 * f[1] + 10 - 2 * z; B = f[3] - 4 * f[2] + (10 - 2 * z) * f[1] + 12 * z - 20
h1 = f[3] - (6 + 2 * z) * f[1] + 20 + 4 * z; h0 = f[4] - (6 + 2 * z) * f[2] + (20 + 4 * z) * f[1] + 3 * z ** 2 + 6 * z - 45
assert S.expand(q7 - (A + x * (f[1] - 4))) == 0
assert S.expand(E4 - (A * x + B)) == 0 and S.expand(E3 - (h0 + x * h1)) == 0
S4 = sum(r[:4]); D = h1 - A * S4; E = h0 - B * S4
assert S.expand((E3 - E4 * S4) - (E + x * D)) == 0
assert S.expand((E * A - B * D) - (h0 * A - h1 * B)) == 0
al = [esym(r[:4], k) for k in range(5)]; be1 = r[4] + r[5]; be2 = r[4] * r[5]
K1 = al[3] - al[1] * al[2] + 4 * al[1] ** 2 - 16 * al[1] + 20 + 4 * z
K2 = al[2] - al[1] ** 2 + 4 * al[1] - 6 - 2 * z
assert S.expand(D - (K1 + be1 * K2)) == 0
assert S.expand(A - ((al[2] - 4 * al[1] + 10 - 2 * z) + be1 * (al[1] - 4) + be2)) == 0
Abar = (al[2] - 4 * al[1] + 10 - 2 * z) + be1 * (al[1] - 4) + be1 ** 2 / 4
Dbar = 4 * al[1] ** 2 - 16 * al[1] + 20 + 4 * z - R(5, 6) * al[1] * al[2] + be1 * K2
assert S.expand((Abar - A) - (r[4] - r[5]) ** 2 / 4) == 0
assert S.expand((Dbar - D) - (al[1] * al[2] / 6 - al[3])) == 0
s1 = S.symbols('s1')
assert S.expand(A - (4 - f[1]) ** 2 - (f[2] + 4 * f[1] - f[1] ** 2 - 6 - 2 * z)) == 0
assert S.expand((-R(7, 12) * s1 ** 2 + 4 * s1 - 6 - 2 * z) - (R(6, 7) - 2 * z - R(7, 12) * (s1 - R(24, 7)) ** 2)) == 0
assert R(6, 7) - 2 * Z1 < 0
print('symbolic-z identities PASS; case (a) bound negative at z1')

# ---------- (2) Qpol(z1), Hpol(z1) six-dimensional covers ----------
uu = S.symbols('u0:6', real=True); F1, F2, F3, F4 = [esym(uu, k) for k in (1, 2, 3, 4)]
Ag = F2 - 4 * F1 + 10 - 2 * Z1; Bg = F3 - 4 * F2 + (10 - 2 * Z1) * F1 + 12 * Z1 - 20
h1g = F3 - (6 + 2 * Z1) * F1 + 20 + 4 * Z1; h0g = F4 - (6 + 2 * Z1) * F2 + (20 + 4 * Z1) * F1 + 3 * Z1 ** 2 + 6 * Z1 - 45
def integerize(expr, gens):
    P = S.Poly(S.expand(expr), *gens); L = 1
    for c in P.coeffs(): L = math.lcm(L, int(S.Rational(c).q))
    P = S.Poly(S.expand(expr * L), *gens); assert all(c.q == 1 for c in P.coeffs()); return P, L
Qp, LQ = integerize(Ag * Ag - (F1 - 4) * Bg, uu)
Hp, LH = integerize(-(h0g * Ag - h1g * Bg), uu)
assert [Qp.degree(v) for v in uu] == [2] * 6 and [Hp.degree(v) for v in uu] == [2] * 6
def digest(P):
    rows = [[list(k), str(int(c))] for k, c in sorted(P.as_dict().items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
def grid6(P):
    scale = 2 ** 6; arr = np.zeros((3,) * 6, dtype=object)
    for key, c in P.as_dict().items():
        div = math.prod(math.comb(2, k) for k in key); assert scale % div == 0
        arr[key] = int(c) * (scale // div)
    return arr
def split(Aa, axis):
    Aa = np.moveaxis(Aa, axis, 0); d = Aa.shape[0] - 1; levels = [Aa]
    while levels[-1].shape[0] > 1: levels.append(levels[-1][:-1] + levels[-1][1:])
    left = np.stack([levels[k][0] * (1 << (d - k)) for k in range(d + 1)])
    right = np.stack([levels[d - k][-1] * (1 << k) for k in range(d + 1)])
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)
def cover6(P):
    stack = [('', grid6(P), tuple((Fr(0), Fr(1)) for _ in range(6)))]; leaves = []
    while stack:
        path, Aa, bounds = stack.pop(); depth = len(path)
        if depth >= 6 and min(Aa.flat) >= 0:
            good = True; interior = 0
            for corners in itertools.product((0, 1), repeat=6):
                coord = [bounds[j][corners[j]] for j in range(6)]
                if all(0 < c < 1 for c in coord):
                    interior += 1; idx = tuple(0 if c == 0 else 2 for c in corners)
                    if Aa[idx] <= 0: good = False; break
            if interior and good: leaves.append(path); continue
        assert depth < 60, path
        axis = depth % 6; Lt, Rt = split(Aa, axis); lo, hi = bounds[axis]; mid = (lo + hi) / 2
        for bit, child, interval in [('1', Rt, (mid, hi)), ('0', Lt, (lo, mid))]:
            bb = list(bounds); bb[axis] = interval; stack.append((path + bit, child, tuple(bb)))
    return sorted(leaves)
Qc = cover6(Qp); Hc = cover6(Hp)
print('Qpol(z1) leaves', len(Qc), 'Hpol(z1) leaves', len(Hc))

# ---------- (3) residual cover at z1 ----------
yy, tau, gam = S.symbols('y tau gam', nonnegative=True)
b1s = yy / 2 + gam; a2s = R(3, 8) * tau * yy ** 2
PA = S.Poly(S.expand(144 * ((a2s - 4 * yy + 10 - 2 * Z1) + b1s * (yy - 4) + b1s ** 2 / 4)), yy, tau, gam)
PD = S.Poly(S.expand(144 * (4 * yy ** 2 - 16 * yy + 20 + 4 * Z1 - R(5, 6) * yy * a2s + b1s * (a2s - yy ** 2 + 4 * yy - 6 - 2 * Z1))), yy, tau, gam)
PF = S.Poly(S.expand(2 * (yy + b1s - 4)), yy, tau, gam)
def intpoly(P, gens):
    L = 1
    for c in P.coeffs(): L = math.lcm(L, int(S.Rational(c).q))
    return S.Poly(S.expand(P.as_expr() * L), *gens)
PA, PD, PF = intpoly(PA, (yy, tau, gam)), intpoly(PD, (yy, tau, gam)), intpoly(PF, (yy, tau, gam))
def bern3(P):
    dy, dt, dg = P.degree(yy), P.degree(tau), P.degree(gam); c = {k: Fr(int(v)) for k, v in P.as_dict().items()}; vals = {}
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
polys3 = {'Abar': PA, 'Dbar': PD, 'f1minus4': PF}
stack = [('', {k: bern3(P) for k, P in polys3.items()})]; leaves3 = []
while stack:
    path, arrs = stack.pop()
    if max(arrs['Abar'].flat) <= 0: leaves3.append([path, 'Abar<=0']); continue
    if max(arrs['Dbar'].flat) <= 0: leaves3.append([path, 'Dbar<=0']); continue
    if max(arrs['f1minus4'].flat) < 0: leaves3.append([path, 'f1-4<0']); continue
    assert len(path) < 60, path
    ax = len(path) % 3; Lc = {}; Rc = {}
    for k, Aa in arrs.items():
        if Aa.shape[ax] > 1: Lc[k], Rc[k] = split(Aa, ax)
        else: Lc[k], Rc[k] = Aa, Aa
    stack.append((path + '1', Rc)); stack.append((path + '0', Lc))
leaves3.sort()
counts3 = {lab: sum(1 for _, l in leaves3 if l == lab) for lab in ('Abar<=0', 'Dbar<=0', 'f1-4<0')}
out = ROOT / 'frontier-20261029-ph7-threshold-z1-certificate-v1.json'
out.write_text(json.dumps({
    'z1': '1753/2000',
    'Q': {'scale_lcm': LQ, 'sha256': digest(Qp), 'terms': len(Qp.terms()), 'leaves': Qc},
    'H': {'scale_lcm': LH, 'sha256': digest(Hp), 'terms': len(Hp.terms()), 'leaves': Hc},
    'six_cube': 'u_i=x_i/(1-x_i), times prod(1-x_i)^2; split axis depth mod 6; leaf: depth>=6, all coefficients >=0, every interior-domain vertex coefficient >0',
    'residual': {'polynomials': {k: {'expr': str(P.as_expr()), 'sha256': digest(P)} for k, P in polys3.items()},
                 'leaf_counts': counts3, 'leaves': leaves3,
                 'chart': 'y=s/(1-s), gam=g/(1-g), tau in [0,1]; split axis depth mod 3'},
}, indent=1) + '\n')
print('SymPy', S.__version__, 'z1=1753/2000 exact PASS: Q leaves', len(Qc), 'H leaves', len(Hc), 'residual', counts3)
print('saved', out)
