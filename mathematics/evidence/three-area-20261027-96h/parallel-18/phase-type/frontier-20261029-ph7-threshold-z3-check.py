#!/usr/bin/env python3
"""Exact certificate of the y^2/y^1-sharpened infeasibility (Lemma C3) at
z3 = 83/100 = 0.83, with the algebraic identities verified for symbolic z.

(1) SymPy identities for symbolic z (as in the z2 generator) plus the y^1
    coefficient of the target, c2(Y2b)=S3*A, and the endpoint formulas.
(2) Compactified six-cube covers at z3:
    QO : Qpol(z3)>0 outside the excluded cube [11/32,37/64]^6 (rates in
         N=[11/21,37/27]);
    HO : Hpol(z3)>0 outside the excluded cube [7/16,5/8]^6 (rates in
         M=[7/9,5/3]).
(3) Sorted affine covers (labels v1<=...<=v6<=x):
    NB : case (b) points with all six rates in N;
    MC : case (c) points with all six rates in M.
(4) Three-parameter residual cover at z3 (case (d)).
Leaf searches for NB/MC are float-guided; every leaf is verified with exact
integers (no floating arithmetic in any check).
"""
import hashlib, itertools, json, math, sys, time
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S
R = S.Rational
Z3 = R(83, 100)
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
assert S.expand(target.coeff_monomial(yv) - (1 + z) ** 2 * qq) == 0 and target.coeff_monomial(1) == 0
r = S.symbols('r1:7', positive=True); x = S.symbols('x', positive=True)
def esym(vs, k): return sum(S.prod(c) for c in itertools.combinations(vs, k)) if k else S.Integer(1)
f = [S.expand(esym(r, k)) for k in range(7)]; e7 = [S.expand(esym(list(r) + [x], k)) for k in range(7)]
p7 = e7[1] - 4; q7 = e7[2] - 4 * e7[1] + 10 - 2 * z
E4 = e7[3] - ((4 + 4 * z) + (6 + 2 * z) * p7 + 4 * q7)
E3 = e7[4] - ((1 + z) ** 2 + (4 + 4 * z) * p7 + (6 + 2 * z) * q7)
E2 = e7[5] - ((1 + z) ** 2 * p7 + (4 + 4 * z) * q7)
E1 = e7[6] - (1 + z) ** 2 * q7
A = f[2] - 4 * f[1] + 10 - 2 * z; B = f[3] - 4 * f[2] + (10 - 2 * z) * f[1] + 12 * z - 20
h1 = f[3] - (6 + 2 * z) * f[1] + 20 + 4 * z; h0 = f[4] - (6 + 2 * z) * f[2] + (20 + 4 * z) * f[1] + 3 * z ** 2 + 6 * z - 45
assert S.expand(q7 - (A + x * (f[1] - 4))) == 0
assert S.expand(E4 - (A * x + B)) == 0 and S.expand(E3 - (h0 + x * h1)) == 0
S4 = sum(r[:4]); D = h1 - A * S4; E = h0 - B * S4
K = S.expand(E3 - E4 * S4)
assert S.expand(K - (E + x * D)) == 0
assert S.expand((E * A - B * D) - (h0 * A - h1 * B)) == 0
al = [esym(r[:4], k) for k in range(5)]; be1 = r[4] + r[5]
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
assert R(6, 7) - 2 * Z3 < 0
S3 = r[0] + r[1] + r[2]; m2 = esym(r[:4], 2); L4 = r[3] + r[4] + r[5] + x
Y2b = S.Poly(S.expand(E2 - E4 * m2 - S3 * (E3 - E4 * L4)), x); assert Y2b.degree() == 2
c2s, c1s, c0s = [S.expand(Y2b.coeff_monomial(x ** k)) for k in (2, 1, 0)]
assert S.expand(c2s - S3 * A) == 0
s12 = r[0] + r[1]
alpha = esym(r[:4], 3) - s12 * esym([r[3], r[4], r[5], x], 2)
beta = esym(r[:3], 2) - s12 * (r[4] + r[5] + x)
assert S.expand(-beta - (s12 * (r[4] - r[2]) + s12 * x + (s12 * r[5] - r[0] * r[1]))) == 0   # -beta>0 for sorted labels
Y1p = S.Poly(S.expand(E1 - s12 * E2 - E4 * alpha - K * beta + E4 ** 2 / 2), x); assert Y1p.degree() == 2
d2s, d1s, d0s = [S.expand(Y1p.coeff_monomial(x ** k)) for k in (2, 1, 0)]
g2, g1, g0, aa, bb, cc = S.symbols('g2 g1 g0 aa bb cc')
assert S.expand(aa ** 2 * (g2 * (-bb / aa) ** 2 + g1 * (-bb / aa) + g0) - (g2 * bb ** 2 - g1 * aa * bb + g0 * aa ** 2)) == 0
assert S.expand(aa * (2 * g2 * (-bb / aa) + g1) - (-2 * g2 * bb + g1 * aa)) == 0
print('symbolic-z identities PASS (incl. y^1 coefficient, c2=S3*A, -beta decomposition, endpoint formulas)', round(time.time() - T0, 1), 's')

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

# ---------- (2) compactified outer covers ----------
uu = S.symbols('u0:6', real=True); G = [S.expand(esym(uu, k)) for k in range(5)]
Ag = G[2] - 4 * G[1] + 10 - 2 * Z3; Bg = G[3] - 4 * G[2] + (10 - 2 * Z3) * G[1] + 12 * Z3 - 20
h1g = G[3] - (6 + 2 * Z3) * G[1] + 20 + 4 * Z3; h0g = G[4] - (6 + 2 * Z3) * G[2] + (20 + 4 * Z3) * G[1] + 3 * Z3 ** 2 + 6 * Z3 - 45
Qp, LQ = integerize(Ag * Ag - (G[1] - 4) * Bg, uu)
Hp, LH = integerize(-(h0g * Ag - h1g * Bg), uu)
assert [Qp.degree(v) for v in uu] == [2] * 6 and [Hp.degree(v) for v in uu] == [2] * 6
def cover_compact(P, nbox):
    stack = [('', compact_grid(P, [2] * 6), tuple((Fr(0), Fr(1)) for _ in range(6)))]; leaves = []
    while stack:
        path, Aa, bounds = stack.pop(); depth = len(path)
        if all(nbox[0] <= lo and hi <= nbox[1] for lo, hi in bounds):
            leaves.append([path, 'R']); continue
        if depth >= 6 and min(Aa.flat) >= 0 and interior_ok(Aa, bounds):
            leaves.append([path, 'pos']); continue
        assert depth < 90, path
        axis = depth % 6; Lt, Rt = split(Aa, axis); lo, hi = bounds[axis]; mid = (lo + hi) / 2
        for bit, child, interval in [('1', Rt, (mid, hi)), ('0', Lt, (lo, mid))]:
            bb_ = list(bounds); bb_[axis] = interval; stack.append((path + bit, child, tuple(bb_)))
    return sorted(leaves)
NCUBE = (Fr(11, 32), Fr(37, 64)); MCUBE = (Fr(7, 16), Fr(5, 8))
NLO, NHI = NCUBE[0] / (1 - NCUBE[0]), NCUBE[1] / (1 - NCUBE[1])
MLO, MHI = MCUBE[0] / (1 - MCUBE[0]), MCUBE[1] / (1 - MCUBE[1])
assert (NLO, NHI) == (Fr(11, 21), Fr(37, 27)) and (MLO, MHI) == (Fr(7, 9), Fr(5, 3))
QO = cover_compact(Qp, NCUBE)
print('QO leaves', len(QO), {lab: sum(1 for _, l in QO if l == lab) for lab in ('pos', 'R')}, round(time.time() - T0, 1), 's')
HO = cover_compact(Hp, MCUBE)
print('HO leaves', len(HO), {lab: sum(1 for _, l in HO if l == lab) for lab in ('pos', 'R')}, round(time.time() - T0, 1), 's')

# ---------- (3) sorted affine covers ----------
vv = S.symbols('v1:7', real=True)
rep = dict(zip(r, vv)); rep[z] = Z3
sub = lambda e: S.expand(e.xreplace(rep))
FN = [S.expand(esym(vv, k)) for k in range(5)]
AN = FN[2] - 4 * FN[1] + 10 - 2 * Z3; BN = FN[3] - 4 * FN[2] + (10 - 2 * Z3) * FN[1] + 12 * Z3 - 20
DN, EN = sub(D), sub(E); F1m4 = FN[1] - 4; QN = AN * AN - F1m4 * BN
c2N, c1N, c0N = sub(c2s), sub(c1s), sub(c0s)
d2N, d1N, d0N = sub(d2s), sub(d1s), sub(d0s)
v6 = vv[5]
GQ = c2N * AN ** 2 - c1N * AN * F1m4 + c0N * F1m4 ** 2
GPQ = -2 * c2N * AN + c1N * F1m4
NB_POLYS = {
    'F': -F1m4, 'A': AN, 'Q': QN, 'mA': -AN, 'Fm': F1m4,
    'mE46': -(AN * v6 + BN),
    'mG6': -(c2N * v6 ** 2 + c1N * v6 + c0N), 'mD6': -(2 * c2N * v6 + c1N),
    'mDl': -(c1N ** 2 - 4 * c2N * c0N),
    'mGq': -GQ, 'T2': AN * GQ + GPQ * QN,
    'mGE': -(c2N * BN ** 2 - c1N * AN * BN + c0N * AN ** 2), 'mDE': 2 * c2N * BN - c1N * AN,
}
NB_NEED = {'unsorted': (), 'F': ('F',), 'A': ('A',), 'Q': ('Q',), 'E4v6': ('mA', 'mE46'), 'Y2v6': ('mA', 'mG6', 'mD6'),
           'Y2tan': ('mA', 'Fm', 'mGq', 'T2'), 'Y2E': ('mA', 'mGE', 'mDE'), 'Disc': ('mA', 'mDl')}
NB_ORDER = ('F', 'A', 'Q', 'E4v6', 'Y2v6', 'Y2tan', 'Y2E', 'Disc')
def nb_ok(lab, bs):
    pos = lambda k: min(bs[k].flat) > 0; nn = lambda k: min(bs[k].flat) >= 0
    return {'F': lambda: pos('F'), 'A': lambda: pos('A'), 'Q': lambda: pos('Q'),
            'E4v6': lambda: pos('mA') and pos('mE46'), 'Y2v6': lambda: pos('mA') and pos('mG6') and nn('mD6'),
            'Y2tan': lambda: pos('mA') and pos('Fm') and pos('mGq') and pos('T2'),
            'Y2E': lambda: pos('mA') and pos('mGE') and nn('mDE'), 'Disc': lambda: pos('mA') and pos('mDl')}[lab]()
MC_POLYS = {
    'mA': -AN, 'D': DN, 'H': -(sub(h0) * AN - sub(h1) * BN), 'A': AN, 'mD': -DN, 'c2': d2N,
    'mendL': -(d2N * BN ** 2 - d1N * AN * BN + d0N * AN ** 2),
    'mendH': -(d2N * EN ** 2 - d1N * DN * EN + d0N * DN ** 2),
}
MC_NEED = {'unsorted': (), 'mA': ('mA',), 'D': ('D',), 'H': ('H',), 'Y1end': ('A', 'mD', 'c2', 'mendL', 'mendH')}
MC_ORDER = ('mA', 'D', 'H', 'Y1end')
def mc_ok(lab, bs):
    pos = lambda k: min(bs[k].flat) > 0
    return {'mA': lambda: pos('mA'), 'D': lambda: pos('D'), 'H': lambda: pos('H'),
            'Y1end': lambda: pos('A') and pos('mD') and pos('c2') and pos('mendL') and pos('mendH')}[lab]()
def affine_bern_int(P, lo, hi):
    degs = [P.degree(v) for v in vv]; w = hi - lo
    arr = np.empty([d + 1 for d in degs], dtype=object); arr.fill(Fr(0))
    for key, c in P.as_dict().items(): arr[key] = Fr(int(c))
    for ax, d in enumerate(degs):
        M1 = np.empty((d + 1, d + 1), dtype=object); M1.fill(Fr(0))
        for j in range(d + 1):
            for k in range(j, d + 1): M1[j, k] = math.comb(k, j) * lo ** (k - j) * w ** j
        M2 = np.empty((d + 1, d + 1), dtype=object); M2.fill(Fr(0))
        for j in range(d + 1):
            for i in range(j + 1): M2[j, i] = Fr(math.comb(j, i), math.comb(d, i))
        Mx = M2.dot(M1)
        t = np.moveaxis(arr, ax, 0); sh = t.shape
        t = Mx.dot(t.reshape(sh[0], -1)).reshape(sh); arr = np.moveaxis(t, 0, ax)
    L = 1
    for v in arr.flat: L = math.lcm(L, v.denominator)
    out = np.empty(arr.shape, dtype=object)
    for idx in itertools.product(*[range(s) for s in arr.shape]):
        val = arr[idx] * L; assert val.denominator == 1; out[idx] = int(val)
    return out
def fsplit(Bf, axis):
    Bf = np.moveaxis(Bf, axis, 0); d = Bf.shape[0] - 1; cur = Bf; lefts = [cur[0]]; rights = [cur[-1]]
    for _ in range(d): cur = (cur[:-1] + cur[1:]) / 2; lefts.append(cur[0]); rights.append(cur[-1])
    return np.moveaxis(np.stack(lefts), 0, axis), np.moveaxis(np.stack(rights[::-1]), 0, axis)
def unsorted(bounds): return any(bounds[i][0] > bounds[j][1] for i in range(6) for j in range(i + 1, 6))
def child_bounds(bounds, ax, bit):
    lo, hi = bounds[ax]; mid = (lo + hi) / 2; nb = list(bounds); nb[ax] = (lo, mid) if bit == '0' else (mid, hi); return tuple(nb)
def sorted_cover(polys, lo, hi, need, order, ok, name):
    PI = {k: integerize(e, vv) for k, e in polys.items()}
    BI = {k: affine_bern_int(P, lo, hi) for k, (P, L) in PI.items()}
    print(name, 'tensors', {k: a.shape for k, a in BI.items()}, round(time.time() - T0, 1), 's')
    BF = {k: a.astype(float) / float(max(abs(int(t)) for t in a.flat)) for k, a in BI.items()}
    def flab(bs, bounds):
        if unsorted(bounds): return 'unsorted'
        fb = {k: b for k, b in bs.items()}
        for lab in order:
            req = need[lab]
            pos_ok = True
            for k in req:
                nonneg = (lab, k) in (('Y2v6', 'mD6'), ('Y2E', 'mDE'))
                if (fb[k].min() < 0) if nonneg else (fb[k].min() <= 0): pos_ok = False; break
            if pos_ok: return lab
        return None
    fleaves = {}; stack = [('', BF, tuple((Fr(0), Fr(1)) for _ in range(6)))]
    while stack:
        path, bs, bounds = stack.pop(); lab = flab(bs, bounds)
        if lab: fleaves[path] = lab; continue
        assert len(path) < 90, path
        ax = len(path) % 6; Lb = {}; Rb = {}
        for k, b in bs.items(): Lb[k], Rb[k] = fsplit(b, ax)
        stack.append((path + '1', Rb, child_bounds(bounds, ax, '1'))); stack.append((path + '0', Lb, child_bounds(bounds, ax, '0')))
    print(name, 'float leaves', len(fleaves), round(time.time() - T0, 1), 's')
    need_below = {}
    for pth, lab in fleaves.items():
        for j in range(len(pth) + 1): need_below.setdefault(pth[:j], set()).update(need[lab])
    leaves = []; refined = [0]
    def exact_refine(path, bs, bounds):
        if unsorted(bounds): leaves.append([path, 'unsorted']); return
        for lab in order:
            if ok(lab, bs): leaves.append([path, lab]); return
        refined[0] += 1; assert len(path) < 90, path
        ax = len(path) % 6; halves = {k: split(b, ax) for k, b in bs.items()}
        for i, bit in enumerate('01'): exact_refine(path + bit, {k: h[i] for k, h in halves.items()}, child_bounds(bounds, ax, bit))
    def walk(path, bs, bounds):
        if path in fleaves:
            lab = fleaves[path]
            if lab == 'unsorted' or ok(lab, bs): leaves.append([path, lab]); return
            full = dict(BI); bb_ = tuple((Fr(0), Fr(1)) for _ in range(6))
            for j, ch in enumerate(path):
                full = {k: split(b, j % 6)[0 if ch == '0' else 1] for k, b in full.items()}; bb_ = child_bounds(bb_, j % 6, ch)
            exact_refine(path, full, bb_); return
        ax = len(path) % 6; halves = {k: split(b, ax) for k, b in bs.items()}
        for i, bit in enumerate('01'):
            child = path + bit; keep = need_below.get(child, set())
            walk(child, {k: h[i] for k, h in halves.items() if k in keep}, child_bounds(bounds, ax, bit))
    walk('', {k: b for k, b in BI.items() if k in need_below.get('', set())}, tuple((Fr(0), Fr(1)) for _ in range(6)))
    leaves.sort(); counts = {}
    for _, l in leaves: counts[l] = counts.get(l, 0) + 1
    print(name, 'exact leaves', len(leaves), counts, 'refinements', refined[0], round(time.time() - T0, 1), 's')
    return {'box': [str(lo), str(hi)], 'polynomials': {k: {'scale_lcm': L, 'sha256': digest(P)} for k, (P, L) in PI.items()},
            'leaf_counts': counts, 'leaves': leaves}
sys.setrecursionlimit(10000)
NBC = sorted_cover(NB_POLYS, NLO, NHI, NB_NEED, NB_ORDER, nb_ok, 'NB')
MCC = sorted_cover(MC_POLYS, MLO, MHI, MC_NEED, MC_ORDER, mc_ok, 'MC')

# ---------- (4) residual cover at z3 ----------
yy, tau, gam = S.symbols('y tau gam', nonnegative=True)
b1s = yy / 2 + gam; a2s = R(3, 8) * tau * yy ** 2
PA = S.Poly(S.expand(144 * ((a2s - 4 * yy + 10 - 2 * Z3) + b1s * (yy - 4) + b1s ** 2 / 4)), yy, tau, gam)
PD = S.Poly(S.expand(144 * (4 * yy ** 2 - 16 * yy + 20 + 4 * Z3 - R(5, 6) * yy * a2s + b1s * (a2s - yy ** 2 + 4 * yy - 6 - 2 * Z3))), yy, tau, gam)
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
out = ROOT / 'frontier-20261029-ph7-threshold-z3-certificate-v1.json'
out.write_text(json.dumps({
    'z3': '83/100',
    'QO': {'scale_lcm': LQ, 'sha256': digest(Qp), 'excluded_cube': ['11/32', '37/64'], 'leaves': QO},
    'HO': {'scale_lcm': LH, 'sha256': digest(Hp), 'excluded_cube': ['7/16', '5/8'], 'leaves': HO},
    'six_cube': 'u_i=x_i/(1-x_i), times prod(1-x_i)^2; split axis depth mod 6; pos leaf: depth>=6, all coefficients >=0, every interior-domain vertex coefficient >0; R leaf: box inside the excluded cube',
    'NB': dict(NBC, rules={k: list(v) for k, v in NB_NEED.items()}, order=list(NB_ORDER),
               nonstrict=['Y2v6:mD6', 'Y2E:mDE'], meaning='case (b) selectors; all listed coefficient tensors >0 (>=0 where nonstrict)'),
    'MC': dict(MCC, rules={k: list(v) for k, v in MC_NEED.items()}, order=list(MC_ORDER),
               meaning='case (c) selectors; all listed coefficient tensors >0'),
    'affine': 'v_i = lo + (hi-lo) s_i, s in [0,1]^6; split axis depth mod 6; unsorted leaf: some i<j with lo_i>hi_j',
    'residual': {'polynomials': {k: {'expr': str(P.as_expr()), 'sha256': digest(P)} for k, P in polys3.items()},
                 'leaf_counts': counts3, 'leaves': leaves3,
                 'chart': 'y=s/(1-s), gam=g/(1-g), tau in [0,1]; split axis depth mod 3'},
}, indent=0) + '\n')
print('SymPy', S.__version__, 'z3=83/100 exact PASS: QO', len(QO), 'HO', len(HO), 'NB', NBC['leaf_counts'], 'MC', MCC['leaf_counts'], 'residual', counts3, round(time.time() - T0, 1), 's')
print('saved', out)
