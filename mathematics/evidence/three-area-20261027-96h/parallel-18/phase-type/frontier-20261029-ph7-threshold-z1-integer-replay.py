#!/usr/bin/env python3
"""Independent standard-library replay of the z1=1753/2000 certificate.

Sparse Fraction polynomials only (no NumPy/SymPy, no floats). Checks the
symbolic-z identities with z as an extra polynomial variable, rebuilds
Qpol(z1)/Hpol(z1) and the residual polynomials from their definitions,
matches coefficient digests, and replays the two six-dimensional covers and
the three-parameter residual cover leaf by leaf.
"""
import hashlib, itertools, json, math
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent
C = json.loads((ROOT / 'frontier-20261029-ph7-threshold-z1-certificate-v1.json').read_text())
Z1 = Q(1753, 2000)

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

# (i) identities with symbolic z (variables r1..r6, x, z)
n = 8; r = [var(i, n) for i in range(6)]; x = var(6, n); z = var(7, n); c = lambda a: cst(a, n)
f = [esym(r, k, n) for k in range(5)]; e7 = [esym(r + [x], k, n) for k in range(5)]
tz = lambda a, b: add(c(a), scale(z, b))           # a + b z
q7 = add(e7[2], scale(e7[1], -4), tz(10, -2))
E4 = add(e7[3], scale(e7[2], -4), mul(tz(10, -2), e7[1]), tz(-20, 12))
E3 = add(e7[4], mul(tz(-6, -2), e7[2]), mul(tz(20, 4), e7[1]), scale(mul(z, z), 3), tz(-45, 6))
A = add(f[2], scale(f[1], -4), tz(10, -2)); B = add(f[3], scale(f[2], -4), mul(tz(10, -2), f[1]), tz(-20, 12))
h1 = add(f[3], mul(tz(-6, -2), f[1]), tz(20, 4)); h0 = add(f[4], mul(tz(-6, -2), f[2]), mul(tz(20, 4), f[1]), scale(mul(z, z), 3), tz(-45, 6))
assert zero(sub(q7, add(A, mul(x, add(f[1], c(-4))))))
assert zero(sub(E4, add(mul(A, x), B))) and zero(sub(E3, add(h0, mul(x, h1))))
S4 = add(*r[:4]); D = sub(h1, mul(A, S4)); E = sub(h0, mul(B, S4))
assert zero(sub(sub(E3, mul(E4, S4)), add(E, mul(x, D))))
assert zero(sub(sub(mul(E, A), mul(B, D)), sub(mul(h0, A), mul(h1, B))))
al = [esym(r[:4], k, n) for k in range(5)]; be1 = add(r[4], r[5]); be2 = mul(r[4], r[5])
K1 = add(al[3], scale(mul(al[1], al[2]), -1), scale(mul(al[1], al[1]), 4), scale(al[1], -16), tz(20, 4))
K2 = add(al[2], scale(mul(al[1], al[1]), -1), scale(al[1], 4), tz(-6, -2))
assert zero(sub(D, add(K1, mul(be1, K2))))
assert zero(sub(A, add(al[2], scale(al[1], -4), tz(10, -2), mul(be1, add(al[1], c(-4))), be2)))
Abar = add(al[2], scale(al[1], -4), tz(10, -2), mul(be1, add(al[1], c(-4))), scale(mul(be1, be1), Q(1, 4)))
Dbar = add(scale(mul(al[1], al[1]), 4), scale(al[1], -16), tz(20, 4), scale(mul(al[1], al[2]), Q(-5, 6)), mul(be1, K2))
d56 = sub(r[4], r[5])
assert zero(sub(sub(Abar, A), scale(mul(d56, d56), Q(1, 4))))
assert zero(sub(sub(Dbar, D), sub(scale(mul(al[1], al[2]), Q(1, 6)), al[3])))
four = sub(c(4), f[1])
assert zero(sub(sub(A, mul(four, four)), add(f[2], scale(f[1], 4), scale(mul(f[1], f[1]), -1), tz(-6, -2))))
# characteristic matching: variables (y, z, e1, e2); T=y((y+1)^2+z)^2 (y^2+p y+q), p=e1-4, q=e2-4e1+10-2z
k4 = 4; Yv = var(0, k4); Zv = var(1, k4); E1v = var(2, k4); E2v = var(3, k4); ck = lambda a_: cst(a_, k4)
pv = add(E1v, ck(-4)); qv = add(E2v, scale(E1v, -4), ck(10), scale(Zv, -2))
quad = add(mul(add(Yv, ck(1)), add(Yv, ck(1))), Zv)
Tpol = mul(mul(Yv, mul(quad, quad)), add(mul(Yv, Yv), mul(pv, Yv), qv))
def ycoef(P, d): return clean({(0,) + k[1:]: v for k, v in P.items() if k[0] == d})
zz_ = lambda a_, b_: add(ck(a_), scale(Zv, b_))
assert zero(sub(ycoef(Tpol, 7), ck(1))) and zero(sub(ycoef(Tpol, 6), E1v)) and zero(sub(ycoef(Tpol, 5), E2v))
assert zero(sub(ycoef(Tpol, 4), add(scale(E2v, 4), mul(zz_(-10, 2), E1v), zz_(20, -12))))
assert zero(sub(ycoef(Tpol, 3), add(mul(zz_(6, 2), E2v), mul(zz_(-20, -4), E1v), scale(mul(Zv, Zv), -3), zz_(45, -6))))
assert Q(6, 7) - 2 * Z1 < 0
print('identities PASS (stdlib, symbolic z, incl. characteristic matching)')

# (ii) Qpol(z1), Hpol(z1)
m = 6; u = [var(i, m) for i in range(m)]; g = [esym(u, k, m) for k in range(5)]; cm = lambda a: cst(a, m)
Ag = add(g[2], scale(g[1], -4), cm(10 - 2 * Z1)); Bg = add(g[3], scale(g[2], -4), scale(g[1], 10 - 2 * Z1), cm(12 * Z1 - 20))
h1g = add(g[3], scale(g[1], -(6 + 2 * Z1)), cm(20 + 4 * Z1)); h0g = add(g[4], scale(g[2], -(6 + 2 * Z1)), scale(g[1], 20 + 4 * Z1), cm(3 * Z1 * Z1 + 6 * Z1 - 45))
Qg = scale(sub(mul(Ag, Ag), mul(add(g[1], cm(-4)), Bg)), C['Q']['scale_lcm'])
Hg = scale(sub(mul(h0g, Ag), mul(h1g, Bg)), -C['H']['scale_lcm'])
def dig(P):
    assert all(v.denominator == 1 for v in P.values())
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
assert dig(Qg) == C['Q']['sha256'] and dig(Hg) == C['H']['sha256']
def grid(P):
    mm = 3; stride = [mm ** (m - 1 - i) for i in range(m)]; arr = [0] * (mm ** m)
    for key, val in P.items():
        div = math.prod(math.comb(2, key[j]) for j in range(m)); assert 64 % div == 0
        arr[sum(key[j] * stride[j] for j in range(m))] = int(val) * (64 // div)
    return arr, stride
def split6(arr, stride, axis):
    L = [0] * len(arr); Rr = [0] * len(arr); other = [j for j in range(m) if j != axis]
    for coord in itertools.product(range(3), repeat=m - 1):
        base = sum(coord[k] * stride[other[k]] for k in range(m - 1)); idx = [base + j * stride[axis] for j in range(3)]
        lv = [[arr[i] for i in idx]]
        while len(lv[-1]) > 1: lv.append([a + b for a, b in zip(lv[-1], lv[-1][1:])])
        for k in range(3): L[idx[k]] = lv[k][0] * (1 << (2 - k)); Rr[idx[k]] = lv[2 - k][-1] * (1 << k)
    return L, Rr
def replay6(P, leaves):
    leaves = set(leaves); pref = {p[:j] for p in leaves for j in range(len(p) + 1)}; seen = set(); arr, stride = grid(P)
    def walk(path, Aa, bounds):
        d = len(path)
        if path in leaves:
            seen.add(path); assert d >= m and min(Aa) >= 0; inter = 0
            for corner in itertools.product((0, 1), repeat=m):
                coords = [bounds[j][corner[j]] for j in range(m)]
                if all(0 < t < 1 for t in coords):
                    inter += 1; idx = sum((0 if corner[j] == 0 else 2) * stride[j] for j in range(m)); assert Aa[idx] > 0
            assert inter > 0; return
        assert path + '0' in pref and path + '1' in pref
        ax = d % m; L, Rr = split6(Aa, stride, ax); lo, hi = bounds[ax]; mid = (lo + hi) / 2
        b0 = list(bounds); b0[ax] = (lo, mid); walk(path + '0', L, tuple(b0))
        b1 = list(bounds); b1[ax] = (mid, hi); walk(path + '1', Rr, tuple(b1))
    walk('', arr, tuple((Q(0), Q(1)) for _ in range(m))); assert seen == leaves
    return len(seen)
nq = replay6(Qg, C['Q']['leaves']); nh = replay6(Hg, C['H']['leaves'])
print('six-dimensional covers replayed:', nq, nh)

# (iii) residual at z1
t = 3; Y = var(0, t); T = var(1, t); G = var(2, t); ct = lambda a: cst(a, t)
b1 = add(scale(Y, Q(1, 2)), G); a2 = scale(mul(T, mul(Y, Y)), Q(3, 8))
PA = scale(add(a2, scale(Y, -4), ct(10 - 2 * Z1), mul(b1, add(Y, ct(-4))), scale(mul(b1, b1), Q(1, 4))), 144)
PD = scale(add(scale(mul(Y, Y), 4), scale(Y, -16), ct(20 + 4 * Z1), scale(mul(Y, a2), Q(-5, 6)),
               mul(b1, add(a2, scale(mul(Y, Y), -1), scale(Y, 4), ct(-6 - 2 * Z1)))), 144)
PF = scale(add(Y, b1, ct(-4)), 2)
def integ(P):
    L = 1
    for v in P.values(): L = math.lcm(L, v.denominator)
    return scale(P, L)
polys = {'Abar': integ(PA), 'Dbar': integ(PD), 'f1minus4': integ(PF)}
for k, P in polys.items(): assert dig(P) == C['residual']['polynomials'][k]['sha256'], k
def degs(P): return [max(e[i] for e in P) for i in range(3)]
def bern(P):
    dy, dt, dg = degs(P); Bm = {}
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
lv = {p: lab for p, lab in C['residual']['leaves']}
for p1 in lv:
    for p2 in lv: assert p1 == p2 or not p2.startswith(p1)
cnt = {}
def walk3(path, st):
    if path in lv:
        lab = lv[path]; name, rule = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}[lab]
        vals = st[name][1].values(); assert (max(vals) <= 0) if rule == 'le' else (max(vals) < 0)
        cnt[lab] = cnt.get(lab, 0) + 1; return
    assert any(l.startswith(path) for l in lv), path
    ax = len(path) % 3
    for bit in '01':
        walk3(path + bit, {k: (sh, halve(sh, Bm, ax, bit == '1') if sh[ax] > 0 else Bm) for k, (sh, Bm) in st.items()})
walk3('', {k: bern(P) for k, P in polys.items()})
assert cnt == C['residual']['leaf_counts'], cnt
print('Independent stdlib replay PASS at z1=1753/2000: Q/H leaves', nq, nh, 'residual', cnt)
