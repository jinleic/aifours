#!/usr/bin/env python3
"""Independent standard-library replay of the z3=83/100 certificate.

Sparse Fraction polynomials and flat integer lists only (no NumPy/SymPy, no
floats). Re-derives the symbolic-z identities (z as a polynomial variable),
rebuilds every certified polynomial from its definition, matches the recorded
digests, and replays the two compactified outer covers, the two sorted affine
covers (case (b) on N^6, case (c) on M^6, with label-driven pruning) and the
residual cover leaf by leaf.
"""
import hashlib, itertools, json, math, random, sys
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent
C = json.loads((ROOT / 'frontier-20261029-ph7-threshold-z3-certificate-v1.json').read_text())
Z3 = Q(83, 100)

def clean(a): return {k: v for k, v in a.items() if v != 0}
def add(*ps):
    o = {}
    for p in ps:
        for k, v in p.items(): o[k] = o.get(k, Q(0)) + v
    return clean(o)
def scale(a, c): return clean({k: v * c for k, v in a.items()})
def sub(a, b): return add(a, scale(b, -1))
def mul(a, b):
    o = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x + y for x, y in zip(k1, k2)); o[k] = o.get(k, Q(0)) + v1 * v2
    return clean(o)
def var(i, n): e = [0] * n; e[i] = 1; return {tuple(e): Q(1)}
def cst(c, n): return {tuple([0] * n): Q(c)} if c else {}
def esym(vs, k, n):
    if k == 0: return cst(1, n)
    o = {}
    for cmb in itertools.combinations(vs, k):
        t = cst(1, n)
        for v in cmb: t = mul(t, v)
        o = add(o, t)
    return o
def zero(p): return not clean(p)
def coef_in(P, i, d): return clean({k[:i] + (0,) + k[i + 1:]: v for k, v in P.items() if k[i] == d})

# ---- (i) identities, z symbolic: variables r1..r6, x, z ----
n = 8; r = [var(i, n) for i in range(6)]; x = var(6, n); z = var(7, n); c = lambda a: cst(a, n)
tz = lambda a, b: add(c(a), scale(z, b))
f = [esym(r, k, n) for k in range(7)]; e7 = [esym(r + [x], k, n) for k in range(7)]
p7 = add(e7[1], c(-4)); q7 = add(e7[2], scale(e7[1], -4), tz(10, -2)); zp1sq = mul(tz(1, 1), tz(1, 1))
E4 = sub(e7[3], add(tz(4, 4), mul(tz(6, 2), p7), scale(q7, 4)))
E3 = sub(e7[4], add(zp1sq, mul(tz(4, 4), p7), mul(tz(6, 2), q7)))
E2 = sub(e7[5], add(mul(zp1sq, p7), mul(tz(4, 4), q7)))
E1 = sub(e7[6], mul(zp1sq, q7))
A = add(f[2], scale(f[1], -4), tz(10, -2)); B = add(f[3], scale(f[2], -4), mul(tz(10, -2), f[1]), tz(-20, 12))
h1 = add(f[3], mul(tz(-6, -2), f[1]), tz(20, 4)); h0 = add(f[4], mul(tz(-6, -2), f[2]), mul(tz(20, 4), f[1]), scale(mul(z, z), 3), tz(-45, 6))
assert zero(sub(q7, add(A, mul(x, add(f[1], c(-4))))))
assert zero(sub(E4, add(mul(A, x), B))) and zero(sub(E3, add(h0, mul(x, h1))))
S4 = add(*r[:4]); D = sub(h1, mul(A, S4)); E = sub(h0, mul(B, S4)); K = sub(E3, mul(E4, S4))
assert zero(sub(K, add(E, mul(x, D))))
assert zero(sub(sub(mul(E, A), mul(B, D)), sub(mul(h0, A), mul(h1, B))))
al = [esym(r[:4], k, n) for k in range(5)]; be1 = add(r[4], r[5])
K1 = add(al[3], scale(mul(al[1], al[2]), -1), scale(mul(al[1], al[1]), 4), scale(al[1], -16), tz(20, 4))
K2 = add(al[2], scale(mul(al[1], al[1]), -1), scale(al[1], 4), tz(-6, -2))
assert zero(sub(D, add(K1, mul(be1, K2))))
Abar = add(al[2], scale(al[1], -4), tz(10, -2), mul(be1, add(al[1], c(-4))), scale(mul(be1, be1), Q(1, 4)))
Dbar = add(scale(mul(al[1], al[1]), 4), scale(al[1], -16), tz(20, 4), scale(mul(al[1], al[2]), Q(-5, 6)), mul(be1, K2))
d56 = sub(r[4], r[5])
assert zero(sub(sub(Abar, A), scale(mul(d56, d56), Q(1, 4))))
assert zero(sub(sub(Dbar, D), sub(scale(mul(al[1], al[2]), Q(1, 6)), al[3])))
four = sub(c(4), f[1])
assert zero(sub(sub(A, mul(four, four)), add(f[2], scale(f[1], 4), scale(mul(f[1], f[1]), -1), tz(-6, -2))))
assert Q(6, 7) - 2 * Z3 < 0
S3 = add(*r[:3]); m2 = esym(r[:4], 2, n); L4 = add(r[3], r[4], r[5], x)
Y2b = sub(sub(E2, mul(E4, m2)), mul(S3, sub(E3, mul(E4, L4))))
assert max(k[6] for k in Y2b) == 2 and zero(sub(coef_in(Y2b, 6, 2), mul(S3, A)))
s12 = add(r[0], r[1])
alpha = sub(esym(r[:4], 3, n), mul(s12, esym([r[3], r[4], r[5], x], 2, n)))
beta = sub(esym(r[:3], 2, n), mul(s12, add(r[4], r[5], x)))
assert zero(add(beta, mul(s12, sub(r[4], r[2])), mul(s12, x), sub(mul(s12, r[5]), mul(r[0], r[1]))))
Y1p = add(sub(E1, mul(s12, E2)), scale(mul(E4, alpha), -1), scale(mul(K, beta), -1), scale(mul(E4, E4), Q(1, 2)))
assert max(k[6] for k in Y1p) == 2
k4 = 5; Yv = var(0, k4); Zv = var(1, k4); E1v = var(2, k4); E2v = var(3, k4); ck = lambda a_: cst(a_, k4)
pv = add(E1v, ck(-4)); qv = add(E2v, scale(E1v, -4), ck(10), scale(Zv, -2))
quad = add(mul(add(Yv, ck(1)), add(Yv, ck(1))), Zv)
Tpol = mul(mul(Yv, mul(quad, quad)), add(mul(Yv, Yv), mul(pv, Yv), qv))
zz_ = lambda a_, b_: add(ck(a_), scale(Zv, b_))
assert zero(sub(coef_in(Tpol, 0, 7), ck(1))) and zero(sub(coef_in(Tpol, 0, 6), E1v)) and zero(sub(coef_in(Tpol, 0, 5), E2v))
assert zero(sub(coef_in(Tpol, 0, 4), add(scale(E2v, 4), mul(zz_(-10, 2), E1v), zz_(20, -12))))
assert zero(sub(coef_in(Tpol, 0, 3), add(mul(zz_(6, 2), E2v), mul(zz_(-20, -4), E1v), scale(mul(Zv, Zv), -3), zz_(45, -6))))
assert zero(sub(coef_in(Tpol, 0, 2), add(mul(mul(zz_(1, 1), zz_(1, 1)), pv), mul(zz_(4, 4), qv))))
assert zero(sub(coef_in(Tpol, 0, 1), mul(mul(zz_(1, 1), zz_(1, 1)), qv))) and zero(coef_in(Tpol, 0, 0))
rng = random.Random(7)
for _ in range(50):     # endpoint substitution formulas, exact rational spot checks of a polynomial identity of degree<=3
    g2, g1, g0, a_, b_ = [Q(rng.randint(-50, 50), rng.randint(1, 9)) for _ in range(5)]
    if a_ == 0: continue
    t_ = -b_ / a_
    assert a_ * a_ * (g2 * t_ * t_ + g1 * t_ + g0) == g2 * b_ * b_ - g1 * a_ * b_ + g0 * a_ * a_
    assert a_ * (2 * g2 * t_ + g1) == -2 * g2 * b_ + g1 * a_
print('identities PASS (stdlib, symbolic z, incl. y^1 coefficient, c2=S3*A, -beta decomposition)')

def dig_scaled(P, L):
    P = scale(P, L); assert all(v.denominator == 1 for v in P.values())
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest(), P

# ---- (ii) compactified outer covers ----
m = 6; u = [var(i, m) for i in range(m)]; g = [esym(u, k, m) for k in range(5)]; cm = lambda a: cst(a, m)
Ag = add(g[2], scale(g[1], -4), cm(10 - 2 * Z3)); Bg = add(g[3], scale(g[2], -4), scale(g[1], 10 - 2 * Z3), cm(12 * Z3 - 20))
h1g = add(g[3], scale(g[1], -(6 + 2 * Z3)), cm(20 + 4 * Z3)); h0g = add(g[4], scale(g[2], -(6 + 2 * Z3)), scale(g[1], 20 + 4 * Z3), cm(3 * Z3 * Z3 + 6 * Z3 - 45))
dQ, Qg = dig_scaled(sub(mul(Ag, Ag), mul(add(g[1], cm(-4)), Bg)), C['QO']['scale_lcm'])
dH, Hg = dig_scaled(sub(mul(h0g, Ag), mul(h1g, Bg)), -C['HO']['scale_lcm'])
assert dQ == C['QO']['sha256'] and dH == C['HO']['sha256']
def grid(P):
    stride = [3 ** (m - 1 - i) for i in range(m)]; arr = [0] * (3 ** m)
    for key, val in P.items():
        div = math.prod(math.comb(2, key[j]) for j in range(m)); assert 64 % div == 0
        arr[sum(key[j] * stride[j] for j in range(m))] = int(val) * (64 // div)
    return arr
def split_flat(arr, shape, axis):
    d = shape[axis] - 1; stride = math.prod(shape[axis + 1:]); L = [0] * len(arr); Rr = [0] * len(arr)
    other = [range(s) for j, s in enumerate(shape) if j != axis]; ost = [math.prod(shape[j + 1:]) for j in range(len(shape)) if j != axis]
    for coord in itertools.product(*other):
        base = sum(a * b for a, b in zip(coord, ost)); idx = [base + j * stride for j in range(d + 1)]
        lv = [[arr[i] for i in idx]]
        while len(lv[-1]) > 1: lv.append([a + b for a, b in zip(lv[-1], lv[-1][1:])])
        for k in range(d + 1): L[idx[k]] = lv[k][0] * (1 << (d - k)); Rr[idx[k]] = lv[d - k][-1] * (1 << k)
    return L, Rr
sys.setrecursionlimit(20000)
def replay_compact(P, leaves, nbox):
    shape = (3,) * m; lv = {p: lab for p, lab in leaves}; pref = {p[:j] for p in lv for j in range(len(p) + 1)}; seen = {}
    def walk(path, Aa, bounds):
        if path in lv:
            lab = lv[path]; seen[lab] = seen.get(lab, 0) + 1
            if lab == 'R': assert all(nbox[0] <= lo and hi <= nbox[1] for lo, hi in bounds); return
            assert lab == 'pos' and len(path) >= m and min(Aa) >= 0; inter = 0
            for corner in itertools.product((0, 1), repeat=m):
                coords = [bounds[j][corner[j]] for j in range(m)]
                if all(0 < t < 1 for t in coords):
                    inter += 1; assert Aa[sum((0 if corner[j] == 0 else 2) * 3 ** (m - 1 - j) for j in range(m))] > 0
            assert inter > 0; return
        assert path + '0' in pref and path + '1' in pref
        ax = len(path) % m; L, Rr = split_flat(Aa, shape, ax); lo, hi = bounds[ax]; mid = (lo + hi) / 2
        b0 = list(bounds); b0[ax] = (lo, mid); walk(path + '0', L, tuple(b0))
        b1 = list(bounds); b1[ax] = (mid, hi); walk(path + '1', Rr, tuple(b1))
    walk('', grid(P), tuple((Q(0), Q(1)) for _ in range(m))); assert sum(seen.values()) == len(lv)
    return seen
NCUBE = (Q(11, 32), Q(37, 64)); MCUBE = (Q(7, 16), Q(5, 8))
assert [str(t) for t in NCUBE] == C['QO']['excluded_cube'] and [str(t) for t in MCUBE] == C['HO']['excluded_cube']
sQ = replay_compact(Qg, C['QO']['leaves'], NCUBE); sH = replay_compact(Hg, C['HO']['leaves'], MCUBE)
print('compactified covers replayed: QO', sQ, 'HO', sH)

# ---- (iii) sorted affine covers ----
NLO, NHI = NCUBE[0] / (1 - NCUBE[0]), NCUBE[1] / (1 - NCUBE[1]); MLO, MHI = MCUBE[0] / (1 - MCUBE[0]), MCUBE[1] / (1 - MCUBE[1])
assert C['NB']['box'] == [str(NLO), str(NHI)] and C['MC']['box'] == [str(MLO), str(MHI)]
n7 = 7; w = [var(i, n7) for i in range(6)]; X = var(6, n7); c7 = lambda a: cst(a, n7)
e7n = [esym(w + [X], k, n7) for k in range(7)]; fN = [esym(w, k, n7) for k in range(5)]
p7n = add(e7n[1], c7(-4)); q7n = add(e7n[2], scale(e7n[1], -4), c7(10 - 2 * Z3))
E4n = sub(e7n[3], add(c7(4 + 4 * Z3), scale(p7n, 6 + 2 * Z3), scale(q7n, 4)))
E3n = sub(e7n[4], add(c7((1 + Z3) ** 2), scale(p7n, 4 + 4 * Z3), scale(q7n, 6 + 2 * Z3)))
E2n = sub(e7n[5], add(scale(p7n, (1 + Z3) ** 2), scale(q7n, 4 + 4 * Z3)))
E1n = sub(e7n[6], scale(q7n, (1 + Z3) ** 2))
An = add(fN[2], scale(fN[1], -4), c7(10 - 2 * Z3)); Bn = add(fN[3], scale(fN[2], -4), scale(fN[1], 10 - 2 * Z3), c7(12 * Z3 - 20))
h1n = add(fN[3], scale(fN[1], -(6 + 2 * Z3)), c7(20 + 4 * Z3)); h0n = add(fN[4], scale(fN[2], -(6 + 2 * Z3)), scale(fN[1], 20 + 4 * Z3), c7(3 * Z3 * Z3 + 6 * Z3 - 45))
S4n = add(*w[:4]); Dn = sub(h1n, mul(An, S4n)); En = sub(h0n, mul(Bn, S4n)); Kn = sub(E3n, mul(E4n, S4n))
S3n = add(*w[:3]); m2n = esym(w[:4], 2, n7); L4n = add(w[3], w[4], w[5], X)
Y2n = sub(sub(E2n, mul(E4n, m2n)), mul(S3n, sub(E3n, mul(E4n, L4n))))
s12n = add(w[0], w[1])
alphan = sub(esym(w[:4], 3, n7), mul(s12n, esym([w[3], w[4], w[5], X], 2, n7)))
betan = sub(esym(w[:3], 2, n7), mul(s12n, add(w[4], w[5], X)))
Y1n = add(sub(E1n, mul(s12n, E2n)), scale(mul(E4n, alphan), -1), scale(mul(Kn, betan), -1), scale(mul(E4n, E4n), Q(1, 2)))
def drop_x(P): return clean({k[:6]: v for k, v in P.items()})
assert all(k[6] <= 2 for k in Y2n) and all(k[6] <= 2 for k in Y1n)
c2n, c1n, c0n = [drop_x(coef_in(Y2n, 6, d)) for d in (2, 1, 0)]
d2n, d1n, d0n = [drop_x(coef_in(Y1n, 6, d)) for d in (2, 1, 0)]
m6 = 6; vs = [var(i, m6) for i in range(m6)]; c6 = lambda a: cst(a, m6)
d6 = lambda P: drop_x(P)
A6, B6, D6, E6, h06, h16 = d6(An), d6(Bn), d6(Dn), d6(En), d6(h0n), d6(h1n)
F1m4 = add(d6(fN[1]), c6(-4)); Q6 = sub(mul(A6, A6), mul(F1m4, B6)); V6 = vs[5]
GQ = add(mul(c2n, mul(A6, A6)), scale(mul(c1n, mul(A6, F1m4)), -1), mul(c0n, mul(F1m4, F1m4)))
GPQ = add(scale(mul(c2n, A6), -2), mul(c1n, F1m4))
NB = {'F': scale(F1m4, -1), 'A': A6, 'Q': Q6, 'mA': scale(A6, -1), 'Fm': F1m4,
      'mE46': scale(add(mul(A6, V6), B6), -1),
      'mG6': scale(add(mul(c2n, mul(V6, V6)), mul(c1n, V6), c0n), -1), 'mD6': scale(add(scale(mul(c2n, V6), 2), c1n), -1),
      'mDl': scale(sub(mul(c1n, c1n), scale(mul(c2n, c0n), 4)), -1),
      'mGq': scale(GQ, -1), 'T2': add(mul(A6, GQ), mul(GPQ, Q6)),
      'mGE': scale(add(mul(c2n, mul(B6, B6)), scale(mul(c1n, mul(A6, B6)), -1), mul(c0n, mul(A6, A6))), -1),
      'mDE': sub(scale(mul(c2n, B6), 2), mul(c1n, A6))}
MCp = {'mA': scale(A6, -1), 'D': D6, 'H': scale(sub(mul(h06, A6), mul(h16, B6)), -1), 'A': A6, 'mD': scale(D6, -1), 'c2': d2n,
       'mendL': scale(add(mul(d2n, mul(B6, B6)), scale(mul(d1n, mul(A6, B6)), -1), mul(d0n, mul(A6, A6))), -1),
       'mendH': scale(add(mul(d2n, mul(E6, E6)), scale(mul(d1n, mul(D6, E6)), -1), mul(d0n, mul(D6, D6))), -1)}
def affine_bern(P, lo, hi):
    degs = [max(e[j] for e in P) for j in range(m6)]; shape = [d + 1 for d in degs]; W = hi - lo
    T = dict(P)
    for ax in range(m6):
        NT = {}
        for key, val in T.items():
            kk = key[ax]
            for j in range(kk + 1):
                nk = key[:ax] + (j,) + key[ax + 1:]
                NT[nk] = NT.get(nk, Q(0)) + val * math.comb(kk, j) * lo ** (kk - j) * W ** j
        T = clean(NT)
    for ax in range(m6):
        d = degs[ax]; NT = {}
        for key, val in T.items():
            i = key[ax]
            for j in range(i, d + 1):
                nk = key[:ax] + (j,) + key[ax + 1:]
                NT[nk] = NT.get(nk, Q(0)) + val * Q(math.comb(j, i), math.comb(d, i))
        T = clean(NT)
    L = 1
    for v in T.values(): L = math.lcm(L, v.denominator)
    flat = [0] * math.prod(shape); st = [math.prod(shape[j + 1:]) for j in range(m6)]
    for key, val in T.items(): flat[sum(key[j] * st[j] for j in range(m6))] = int(val * L)
    return flat, tuple(shape)
def replay_sorted(polys, cert, lo, hi, nonstrict):
    for k, P in polys.items():
        d_, Pi = dig_scaled(P, cert['polynomials'][k]['scale_lcm']); assert d_ == cert['polynomials'][k]['sha256'], k
        polys[k] = Pi
    rules = {k: tuple(v) for k, v in cert['rules'].items()}
    lv = {p: lab for p, lab in cert['leaves']}
    for p in lv:
        for j in range(len(p)): assert p[:j] not in lv
    need = {}
    for p, lab in lv.items():
        for j in range(len(p) + 1): need.setdefault(p[:j], set()).update(rules[lab])
    BT = {k: affine_bern(polys[k], lo, hi) for k in need['']}
    cnt = {}
    def check(lab, T, bounds):
        if lab == 'unsorted': return any(bounds[i][0] > bounds[j][1] for i in range(6) for j in range(i + 1, 6))
        for k in rules[lab]:
            mn = min(T[k][0])
            if (f'{lab}:{k}' in nonstrict and mn < 0) or (f'{lab}:{k}' not in nonstrict and mn <= 0): return False
        return True
    def walk(path, T, bounds):
        if path in lv:
            lab = lv[path]; assert check(lab, T, bounds), (path, lab); cnt[lab] = cnt.get(lab, 0) + 1; return
        assert path + '0' in need and path + '1' in need, path
        ax = len(path) % 6; lo_, hi_ = bounds[ax]; mid = (lo_ + hi_) / 2
        halves = {k: split_flat(arr, sh, ax) + (sh,) for k, (arr, sh) in T.items()}
        for i, bit in enumerate('01'):
            nb = list(bounds); nb[ax] = (lo_, mid) if bit == '0' else (mid, hi_)
            walk(path + bit, {k: (h[i], h[2]) for k, h in halves.items() if k in need[path + bit]}, tuple(nb))
    walk('', BT, tuple((Q(0), Q(1)) for _ in range(6)))
    assert cnt == cert['leaf_counts'], cnt
    return cnt
cNB = replay_sorted(NB, C['NB'], NLO, NHI, set(C['NB']['nonstrict']))
print('NB cover replayed:', cNB)
cMC = replay_sorted(MCp, C['MC'], MLO, MHI, set())
print('MC cover replayed:', cMC)

# ---- (iv) residual at z3 ----
t = 3; Y = var(0, t); T_ = var(1, t); G_ = var(2, t); ct = lambda a: cst(a, t)
b1 = add(scale(Y, Q(1, 2)), G_); a2 = scale(mul(T_, mul(Y, Y)), Q(3, 8))
PA = scale(add(a2, scale(Y, -4), ct(10 - 2 * Z3), mul(b1, add(Y, ct(-4))), scale(mul(b1, b1), Q(1, 4))), 144)
PD = scale(add(scale(mul(Y, Y), 4), scale(Y, -16), ct(20 + 4 * Z3), scale(mul(Y, a2), Q(-5, 6)),
               mul(b1, add(a2, scale(mul(Y, Y), -1), scale(Y, 4), ct(-6 - 2 * Z3)))), 144)
PF = scale(add(Y, b1, ct(-4)), 2)
def integ(P):
    L = 1
    for v in P.values(): L = math.lcm(L, v.denominator)
    return scale(P, L)
polys = {'Abar': integ(PA), 'Dbar': integ(PD), 'f1minus4': integ(PF)}
for k, P in polys.items():
    d_, _ = dig_scaled(P, 1); assert d_ == C['residual']['polynomials'][k]['sha256'], k
def degs3(P): return [max(e[i] for e in P) for i in range(3)]
def bern(P):
    dy, dt, dg = degs3(P); Bm = {}
    for i in range(dy + 1):
        for mm in range(dt + 1):
            for k in range(dg + 1):
                v = Q(0)
                for j in range(mm + 1): v += P.get((i, j, k), Q(0)) * Q(math.comb(mm, j), math.comb(dt, j))
                Bm[(i, mm, k)] = v / (math.comb(dy, i) * math.comb(dg, k))
    return (dy, dt, dg), Bm
def halve(shape, Bm, axis, upper):
    d = shape[axis]; out = {}
    for rest in itertools.product(*[range(s + 1) for i, s in enumerate(shape) if i != axis]):
        def key(ii):
            kk = list(rest); kk.insert(axis, ii); return tuple(kk)
        tri = [[Bm[key(i)] for i in range(d + 1)]]
        for _ in range(d): pv = tri[-1]; tri.append([(pv[i] + pv[i + 1]) / 2 for i in range(len(pv) - 1)])
        new = [tri[d - i][-1] for i in range(d + 1)] if upper else [tri[i][0] for i in range(d + 1)]
        for i in range(d + 1): out[key(i)] = new[i]
    return out
lv3 = {p: lab for p, lab in C['residual']['leaves']}
for p1 in lv3:
    for j in range(len(p1)): assert p1[:j] not in lv3
pref3 = {p[:j] for p in lv3 for j in range(len(p) + 1)}
cnt3 = {}
def walk3(path, st):
    if path in lv3:
        lab = lv3[path]; name, rule = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}[lab]
        vals = st[name][1].values(); assert (max(vals) <= 0) if rule == 'le' else (max(vals) < 0)
        cnt3[lab] = cnt3.get(lab, 0) + 1; return
    assert path in pref3, path
    ax = len(path) % 3
    for bit in '01':
        walk3(path + bit, {k: (sh, halve(sh, Bm, ax, bit == '1') if sh[ax] > 0 else Bm) for k, (sh, Bm) in st.items()})
walk3('', {k: bern(P) for k, P in polys.items()})
assert cnt3 == C['residual']['leaf_counts'], cnt3
print('Independent stdlib replay PASS at z3=83/100: QO', sQ, 'HO', sH, 'NB', cNB, 'MC', cMC, 'residual', cnt3)
