#!/usr/bin/env python3
"""Exact certificate of the y^2-sharpened infeasibility (Lemma C2) at
z2 = 17/20 = 0.85, with all algebraic identities verified for symbolic z.

(1) SymPy identities for symbolic z: characteristic matching constants
    (including the y^2 coefficient), seventh-rate splitting, K=E+xD,
    EA-BD=h0A-h1B, residual decomposition, case-(a) bound, and the
    leading coefficient c2=S3*A of the sharpened quadratic Y2b(x).
(2) Integer six-dimensional Bernstein covers at z2:
    H : Hpol(z2) > 0 on the open six-orthant (compactified);
    O : outer cover, every compactified leaf has Qpol(z2) > 0 or lies in
        the cube [3/8,9/16]^6, i.e. all six rates in N=[3/5,9/7];
    N : affine cover of N^6 in sorted labels v1<=...<=v6 with selectors
        F (4-f1>0), A (A>0), Q (Qpol>0), E4v6 (A<0, E4(v6)<0),
        Y2v6 (A<0, Y2b(v6)<0, Y2b'(v6)<=0), Disc (A<0, disc(Y2b)<0),
        or the box misses the sorted cone.
(3) Integer three-parameter residual selector cover at z2.
Search for the N cover is guided by floating Bernstein bounds; every leaf is
then verified with exact integers (no floating arithmetic in any check).
"""
import hashlib, itertools, json, math, sys, time
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S
R = S.Rational
Z2 = R(17, 20)
NLO, NHI = R(3, 5), R(9, 7)          # N = [3/5, 9/7]; compactified [3/8, 9/16]
z = S.symbols('z', positive=True)
T0 = time.time()

# ---------- (1) identities for symbolic z ----------
yv, pp, qq = S.symbols('y p q')
target = S.Poly(S.expand(yv * ((yv + 1) ** 2 + z) ** 2 * (yv ** 2 + pp * yv + qq)), yv)
assert S.expand(target.coeff_monomial(yv ** 6) - (pp + 4)) == 0
assert S.expand(target.coeff_monomial(yv ** 5) - (qq + 4 * pp + 6 + 2 * z)) == 0
assert S.expand(target.coeff_monomial(yv ** 4) - ((4 + 4 * z) + (6 + 2 * z) * pp + 4 * qq)) == 0
assert S.expand(target.coeff_monomial(yv ** 3) - ((1 + z) ** 2 + (4 + 4 * z) * pp + (6 + 2 * z) * qq)) == 0
assert S.expand(target.coeff_monomial(yv ** 2) - ((1 + z) ** 2 * pp + (4 + 4 * z) * qq)) == 0
r = S.symbols('r1:7', positive=True); x = S.symbols('x', positive=True)
def esym(vs, k): return sum(S.prod(c) for c in itertools.combinations(vs, k)) if k else S.Integer(1)
f = [S.expand(esym(r, k)) for k in range(6)]; e7 = [S.expand(esym(list(r) + [x], k)) for k in range(6)]
p7 = e7[1] - 4; q7 = e7[2] - 4 * e7[1] + 10 - 2 * z
E4 = e7[3] - ((4 + 4 * z) + (6 + 2 * z) * p7 + 4 * q7)
E3 = e7[4] - ((1 + z) ** 2 + (4 + 4 * z) * p7 + (6 + 2 * z) * q7)
E2 = e7[5] - ((1 + z) ** 2 * p7 + (4 + 4 * z) * q7)
assert S.expand(E4 - (e7[3] - 4 * e7[2] + (10 - 2 * z) * e7[1] + 12 * z - 20)) == 0
assert S.expand(E3 - (e7[4] - (6 + 2 * z) * e7[2] + (20 + 4 * z) * e7[1] + 3 * z ** 2 + 6 * z - 45)) == 0
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
Abar = (al[2] - 4 * al[1] + 10 - 2 * z) + be1 * (al[1] - 4) + be1 ** 2 / 4
Dbar = 4 * al[1] ** 2 - 16 * al[1] + 20 + 4 * z - R(5, 6) * al[1] * al[2] + be1 * K2
assert S.expand((Abar - A) - (r[4] - r[5]) ** 2 / 4) == 0
assert S.expand((Dbar - D) - (al[1] * al[2] / 6 - al[3])) == 0
s1 = S.symbols('s1')
assert S.expand(A - (4 - f[1]) ** 2 - (f[2] + 4 * f[1] - f[1] ** 2 - 6 - 2 * z)) == 0
assert S.expand((-R(7, 12) * s1 ** 2 + 4 * s1 - 6 - 2 * z) - (R(6, 7) - 2 * z - R(7, 12) * (s1 - R(24, 7)) ** 2)) == 0
assert R(6, 7) - 2 * Z2 < 0
# sharpened quadratic in sorted labels r1<=...<=r6<=x
S3 = r[0] + r[1] + r[2]; m2 = esym(r[:4], 2); L4 = r[3] + r[4] + r[5] + x
Y2b = S.Poly(S.expand(E2 - E4 * m2 - S3 * (E3 - E4 * L4)), x)
assert Y2b.degree() == 2
c2s, c1s, c0s = [S.expand(Y2b.coeff_monomial(x ** k)) for k in (2, 1, 0)]
assert S.expand(c2s - S3 * A) == 0
print('symbolic-z identities PASS (incl. y^2 coefficient and c2=S3*A)', round(time.time() - T0, 1), 's')

# ---------- shared integer Bernstein machinery ----------
def digest(P):
    rows = [[list(k), str(int(c))] for k, c in sorted(P.as_dict().items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
def integerize(expr, gens):
    P = S.Poly(S.expand(expr), *gens); L = 1
    for c in P.coeffs(): L = math.lcm(L, int(S.Rational(c).q))
    P = S.Poly(S.expand(expr * L), *gens); assert all(c.q == 1 for c in P.coeffs()); return P, L
def split(Aa, axis):
    Aa = np.moveaxis(Aa, axis, 0); d = Aa.shape[0] - 1; levels = [Aa]
    while levels[-1].shape[0] > 1: levels.append(levels[-1][:-1] + levels[-1][1:])
    left = np.stack([levels[k][0] * (1 << (d - k)) for k in range(d + 1)])
    right = np.stack([levels[d - k][-1] * (1 << k) for k in range(d + 1)])
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)
def compact_grid(P, degs):
    L = 1
    for key in itertools.product(*[range(d + 1) for d in degs]):
        L = math.lcm(L, math.prod(math.comb(degs[j], key[j]) for j in range(len(degs))))
    arr = np.zeros([d + 1 for d in degs], dtype=object)
    for key, c in P.as_dict().items():
        div = math.prod(math.comb(degs[j], key[j]) for j in range(len(degs)))
        arr[key] = int(c) * (L // div)
    return arr
def interior_ok(Aa, bounds):
    m = Aa.ndim; interior = 0
    for corners in itertools.product((0, 1), repeat=m):
        coord = [bounds[j][corners[j]] for j in range(m)]
        if all(0 < c < 1 for c in coord):
            interior += 1; idx = tuple(0 if c == 0 else Aa.shape[j] - 1 for j, c in enumerate(corners))
            if Aa[idx] <= 0: return False
    return interior > 0

# ---------- (2H, 2O) compactified six-cube covers ----------
uu = S.symbols('u0:6', real=True); G = [S.expand(esym(uu, k)) for k in range(5)]
Ag = G[2] - 4 * G[1] + 10 - 2 * Z2; Bg = G[3] - 4 * G[2] + (10 - 2 * Z2) * G[1] + 12 * Z2 - 20
h1g = G[3] - (6 + 2 * Z2) * G[1] + 20 + 4 * Z2; h0g = G[4] - (6 + 2 * Z2) * G[2] + (20 + 4 * Z2) * G[1] + 3 * Z2 ** 2 + 6 * Z2 - 45
Qp, LQ = integerize(Ag * Ag - (G[1] - 4) * Bg, uu)
Hp, LH = integerize(-(h0g * Ag - h1g * Bg), uu)
assert [Qp.degree(v) for v in uu] == [2] * 6 and [Hp.degree(v) for v in uu] == [2] * 6
def cover_compact(P, nbox=None):
    stack = [('', compact_grid(P, [2] * 6), tuple((Fr(0), Fr(1)) for _ in range(6)))]; leaves = []
    while stack:
        path, Aa, bounds = stack.pop(); depth = len(path)
        if nbox and all(nbox[0] <= lo and hi <= nbox[1] for lo, hi in bounds):
            leaves.append([path, 'N']); continue
        if depth >= 6 and min(Aa.flat) >= 0 and interior_ok(Aa, bounds):
            leaves.append([path, 'pos']); continue
        assert depth < 80, path
        axis = depth % 6; Lt, Rt = split(Aa, axis); lo, hi = bounds[axis]; mid = (lo + hi) / 2
        for bit, child, interval in [('1', Rt, (mid, hi)), ('0', Lt, (lo, mid))]:
            bb = list(bounds); bb[axis] = interval; stack.append((path + bit, child, tuple(bb)))
    return sorted(leaves)
Hc = cover_compact(Hp)
print('Hpol(z2) leaves', len(Hc), round(time.time() - T0, 1), 's')
NB = (Fr(3, 8), Fr(9, 16))
assert NB[0] / (1 - NB[0]) == Fr(3, 5) and NB[1] / (1 - NB[1]) == Fr(9, 7)
Oc = cover_compact(Qp, NB)
print('outer Q/N leaves', len(Oc), {lab: sum(1 for _, l in Oc if l == lab) for lab in ('pos', 'N')}, round(time.time() - T0, 1), 's')

# ---------- (2N) sorted affine cover of N^6 ----------
vv = S.symbols('v1:7', real=True); ss = S.symbols('s1:7', real=True)
rep = dict(zip(r, vv)); rep[z] = Z2
c2N, c1N, c0N = [S.expand(c.xreplace(rep)) for c in (c2s, c1s, c0s)]
FN = [S.expand(esym(vv, k)) for k in range(5)]
AN = FN[2] - 4 * FN[1] + 10 - 2 * Z2; BN = FN[3] - 4 * FN[2] + (10 - 2 * Z2) * FN[1] + 12 * Z2 - 20
v6 = vv[5]
NP = {
    'F': 4 - FN[1], 'A': AN, 'Q': AN * AN - (FN[1] - 4) * BN, 'mA': -AN,
    'mE46': -(AN * v6 + BN),
    'mG6': -(c2N * v6 ** 2 + c1N * v6 + c0N),
    'mD6': -(2 * c2N * v6 + c1N),
    'mDl': -(c1N ** 2 - 4 * c2N * c0N),
}
NPI = {}
for k, e in NP.items():
    P, L = integerize(e, vv); NPI[k] = (P, L)
NEED = {'unsorted': (), 'F': ('F',), 'A': ('A',), 'Q': ('Q',), 'E4v6': ('mA', 'mE46'),
        'Y2v6': ('mA', 'mG6', 'mD6'), 'Disc': ('mA', 'mDl')}
def affine_bern_int(P):
    degs = [P.degree(v) for v in vv]
    W = NHI - NLO
    Ps = S.Poly(S.expand(P.as_expr().xreplace({vv[i]: NLO + W * ss[i] for i in range(6)})), *ss)
    arr = np.zeros([d + 1 for d in degs], dtype=object)
    for idx in itertools.product(*[range(d + 1) for d in degs]): arr[idx] = Fr(0)
    for key, c in Ps.as_dict().items(): arr[key] = Fr(int(S.Rational(c).p), int(S.Rational(c).q))
    for ax, d in enumerate(degs):           # monomial -> Bernstein along each axis
        arr = np.moveaxis(arr, ax, 0); new = np.empty_like(arr)
        for j in range(d + 1):
            acc = arr[0] * Fr(1)
            for i in range(1, j + 1): acc = acc + arr[i] * Fr(math.comb(j, i), math.comb(d, i))
            new[j] = acc
        arr = np.moveaxis(new, 0, ax)
    L = 1
    for v in arr.flat: L = math.lcm(L, v.denominator)
    out = np.empty(arr.shape, dtype=object)
    for idx in itertools.product(*[range(s) for s in arr.shape]):
        val = arr[idx] * L; assert val.denominator == 1; out[idx] = int(val)
    return out
BN_int = {k: affine_bern_int(P) for k, (P, L) in NPI.items()}
print('N-box Bernstein tensors', {k: a.shape for k, a in BN_int.items()}, round(time.time() - T0, 1), 's')
def unsorted(bounds): return any(bounds[i][0] > bounds[j][1] for i in range(6) for j in range(i + 1, 6))
def label_ok(lab, bs):
    if lab == 'F': return min(bs['F'].flat) > 0
    if lab == 'A': return min(bs['A'].flat) > 0
    if lab == 'Q': return min(bs['Q'].flat) > 0
    if lab == 'E4v6': return min(bs['mA'].flat) > 0 and min(bs['mE46'].flat) > 0
    if lab == 'Y2v6': return min(bs['mA'].flat) > 0 and min(bs['mG6'].flat) > 0 and min(bs['mD6'].flat) >= 0
    if lab == 'Disc': return min(bs['mA'].flat) > 0 and min(bs['mDl'].flat) > 0
    raise ValueError(lab)
ORDER = ('F', 'A', 'Q', 'E4v6', 'Y2v6', 'Disc')
# floating search for the leaf set (guidance only; every leaf is re-verified exactly)
def fsplit(Bf, axis):
    Bf = np.moveaxis(Bf, axis, 0); d = Bf.shape[0] - 1; cur = Bf; lefts = [cur[0]]; rights = [cur[-1]]
    for _ in range(d): cur = (cur[:-1] + cur[1:]) / 2; lefts.append(cur[0]); rights.append(cur[-1])
    return np.moveaxis(np.stack(lefts), 0, axis), np.moveaxis(np.stack(rights[::-1]), 0, axis)
BN_f = {k: a.astype(float) / float(max(abs(int(t)) for t in a.flat)) for k, a in BN_int.items()}
def flab(bs, bounds):
    if unsorted(bounds): return 'unsorted'
    if bs['F'].min() > 0: return 'F'
    if bs['A'].min() > 0: return 'A'
    if bs['Q'].min() > 0: return 'Q'
    if bs['mA'].min() > 0:
        if bs['mE46'].min() > 0: return 'E4v6'
        if bs['mG6'].min() > 0 and bs['mD6'].min() >= 0: return 'Y2v6'
        if bs['mDl'].min() > 0: return 'Disc'
    return None
fleaves = {}; stack = [('', BN_f, tuple((Fr(0), Fr(1)) for _ in range(6)))]
while stack:
    path, bs, bounds = stack.pop(); lab = flab(bs, bounds)
    if lab: fleaves[path] = lab; continue
    assert len(path) < 80, path
    ax = len(path) % 6; lo, hi = bounds[ax]; mid = (lo + hi) / 2; Lb = {}; Rb = {}
    for k, b in bs.items(): Lb[k], Rb[k] = fsplit(b, ax)
    b0 = list(bounds); b0[ax] = (lo, mid); b1 = list(bounds); b1[ax] = (mid, hi)
    stack.append((path + '1', Rb, tuple(b1))); stack.append((path + '0', Lb, tuple(b0)))
print('float N search leaves', len(fleaves), round(time.time() - T0, 1), 's')
need_below = {}
for pth, lab in fleaves.items():
    for j in range(len(pth) + 1): need_below.setdefault(pth[:j], set()).update(NEED[lab])
Nleaves = []; refined = [0]
def child_bounds(bounds, ax, bit):
    lo, hi = bounds[ax]; mid = (lo + hi) / 2; nb = list(bounds); nb[ax] = (lo, mid) if bit == '0' else (mid, hi); return tuple(nb)
def exact_refine(path, bs, bounds):
    if unsorted(bounds): Nleaves.append([path, 'unsorted']); return
    for lab in ORDER:
        if label_ok(lab, bs): Nleaves.append([path, lab]); return
    refined[0] += 1; assert len(path) < 80, path
    ax = len(path) % 6; halves = {k: split(b, ax) for k, b in bs.items()}
    for i, bit in enumerate('01'):
        exact_refine(path + bit, {k: h[i] for k, h in halves.items()}, child_bounds(bounds, ax, bit))
def walk(path, bs, bounds):
    if path in fleaves:
        lab = fleaves[path]
        if lab == 'unsorted' or label_ok(lab, bs): Nleaves.append([path, lab]); return
        full = dict(BN_int); bb = tuple((Fr(0), Fr(1)) for _ in range(6))
        for j, ch in enumerate(path):
            full = {k: split(b, j % 6)[0 if ch == '0' else 1] for k, b in full.items()}
            bb = child_bounds(bb, j % 6, ch)
        exact_refine(path, full, bb); return
    ax = len(path) % 6; halves = {k: split(b, ax) for k, b in bs.items()}
    for i, bit in enumerate('01'):
        child = path + bit; keep = need_below.get(child, set())
        walk(child, {k: h[i] for k, h in halves.items() if k in keep}, child_bounds(bounds, ax, bit))
sys.setrecursionlimit(10000)
walk('', {k: b for k, b in BN_int.items() if k in need_below.get('', set())}, tuple((Fr(0), Fr(1)) for _ in range(6)))
Nleaves.sort()
Ncounts = {}
for _, l in Nleaves: Ncounts[l] = Ncounts.get(l, 0) + 1
print('exact N cover leaves', len(Nleaves), Ncounts, 'exact refinements', refined[0], round(time.time() - T0, 1), 's')

# ---------- (3) residual cover at z2 ----------
yy, tau, gam = S.symbols('y tau gam', nonnegative=True)
b1s = yy / 2 + gam; a2s = R(3, 8) * tau * yy ** 2
PA = S.Poly(S.expand(144 * ((a2s - 4 * yy + 10 - 2 * Z2) + b1s * (yy - 4) + b1s ** 2 / 4)), yy, tau, gam)
PD = S.Poly(S.expand(144 * (4 * yy ** 2 - 16 * yy + 20 + 4 * Z2 - R(5, 6) * yy * a2s + b1s * (a2s - yy ** 2 + 4 * yy - 6 - 2 * Z2))), yy, tau, gam)
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
out = ROOT / 'frontier-20261029-ph7-threshold-z2-certificate-v1.json'
out.write_text(json.dumps({
    'z2': '17/20',
    'H': {'scale_lcm': LH, 'sha256': digest(Hp), 'leaves': [p for p, _ in Hc]},
    'outer': {'Q_scale_lcm': LQ, 'Q_sha256': digest(Qp), 'N_cube': ['3/8', '9/16'], 'leaves': Oc},
    'six_cube': 'u_i=x_i/(1-x_i), times prod(1-x_i)^2; split axis depth mod 6; pos leaf: depth>=6, all coefficients >=0, every interior-domain vertex coefficient >0; N leaf: box inside [3/8,9/16]^6',
    'N': {'box': ['3/5', '9/7'], 'sorted_labels': 'v1<=v2<=...<=v6 (x is the largest of the seven)',
          'polynomials': {k: {'scale_lcm': L, 'sha256': digest(P)} for k, (P, L) in NPI.items()},
          'rules': {'unsorted': 'some i<j with lo_i>hi_j', 'F': 'all F>0', 'A': 'all A>0', 'Q': 'all Q>0',
                    'E4v6': 'all mA>0 and all mE46>0', 'Y2v6': 'all mA>0, all mG6>0, all mD6>=0', 'Disc': 'all mA>0 and all mDl>0'},
          'leaf_counts': Ncounts, 'leaves': Nleaves},
    'residual': {'polynomials': {k: {'expr': str(P.as_expr()), 'sha256': digest(P)} for k, P in polys3.items()},
                 'leaf_counts': counts3, 'leaves': leaves3,
                 'chart': 'y=s/(1-s), gam=g/(1-g), tau in [0,1]; split axis depth mod 3'},
}, indent=0) + '\n')
print('SymPy', S.__version__, 'z2=17/20 exact PASS: H leaves', len(Hc), 'outer', len(Oc), 'N', Ncounts, 'residual', counts3, round(time.time() - T0, 1), 's')
print('saved', out)
