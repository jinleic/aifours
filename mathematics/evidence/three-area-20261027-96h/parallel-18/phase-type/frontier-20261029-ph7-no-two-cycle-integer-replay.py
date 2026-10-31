#!/usr/bin/env python3
"""Independent standard-library replay for the no-two-cycle reduction at z=8/9.

Uses only fractions/itertools/json/hashlib/math. Sparse polynomials are dicts
{exponent tuple: Fraction}. It (i) re-derives every algebraic identity used by
the written proof, (ii) recomputes the girth-four Qpol/Hpol coefficient digests
and compares them with the pinned girth-four certificate, (iii) rebuilds the
three residual polynomials from their defining formulas, compares digests, and
replays the complete binary selector cover with exact Fraction de Casteljau
midpoint subdivision. No NumPy, SymPy or floating arithmetic.
"""
import hashlib, itertools, json, math
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def clean(p): return {k: v for k, v in p.items() if v != 0}
def add(*ps):
    o = {}
    for p in ps:
        for k, v in p.items(): o[k] = o.get(k, Q(0)) + v
    return clean(o)
def scale(p, c): return clean({k: v * c for k, v in p.items()})
def mul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2)); o[k] = o.get(k, Q(0)) + v1 * v2
    return clean(o)
def sub(p, q): return add(p, scale(q, -1))
def var(i, n): e = [0] * n; e[i] = 1; return {tuple(e): Q(1)}
def const(c, n): return {tuple([0] * n): Q(c)} if c else {}
def esym(vs, k, n):
    if k == 0: return const(1, n)
    o = {}
    for comb_ in itertools.combinations(vs, k):
        t = const(1, n)
        for v in comb_: t = mul(t, v)
        o = add(o, t)
    return o
def zero(p): return len(clean(p)) == 0

# ---------- (i) identities, 7 variables r1..r6, x ----------
n = 7; r = [var(i, n) for i in range(6)]; x = var(6, n)
f = [esym(r, k, n) for k in range(5)]
e7 = [esym(r + [x], k, n) for k in range(5)]
for k in range(1, 5): assert zero(sub(e7[k], add(f[k], mul(x, f[k - 1]))))
c = lambda a: const(a, n)
q7 = add(e7[2], scale(e7[1], -4), c(Q(74, 9)))
E4 = add(e7[3], scale(e7[2], -4), scale(e7[1], Q(74, 9)), c(Q(-28, 3)))
E3 = add(e7[4], scale(e7[2], Q(-70, 9)), scale(e7[1], Q(212, 9)), c(Q(-1007, 27)))
A = add(f[2], scale(f[1], -4), c(Q(74, 9)))
B = add(f[3], scale(f[2], -4), scale(f[1], Q(74, 9)), c(Q(-28, 3)))
h0 = add(f[4], scale(f[2], Q(-70, 9)), scale(f[1], Q(212, 9)), c(Q(-1007, 27)))
h1 = add(f[3], scale(f[1], Q(-70, 9)), c(Q(212, 9)))
assert zero(sub(q7, add(A, mul(x, add(f[1], c(-4))))))
assert zero(sub(E4, add(mul(A, x), B)))
assert zero(sub(E3, add(h0, mul(x, h1))))
S4 = add(*r[:4])
D = sub(h1, mul(A, S4)); E = sub(h0, mul(B, S4))
assert zero(sub(sub(E3, mul(E4, S4)), add(E, mul(x, D))))
assert zero(sub(sub(mul(E, A), mul(B, D)), sub(mul(h0, A), mul(h1, B))))
al = [esym(r[:4], k, n) for k in range(5)]
be1 = add(r[4], r[5]); be2 = mul(r[4], r[5])
K1 = add(al[3], scale(mul(al[1], al[2]), -1), scale(mul(al[1], al[1]), 4), scale(al[1], -16), c(Q(212, 9)))
K2 = add(al[2], scale(mul(al[1], al[1]), -1), scale(al[1], 4), c(Q(-70, 9)))
assert zero(sub(D, add(K1, mul(be1, K2))))
A_split = add(al[2], scale(al[1], -4), c(Q(74, 9)), mul(be1, add(al[1], c(-4))), be2)
assert zero(sub(A, A_split))
Abar = add(al[2], scale(al[1], -4), c(Q(74, 9)), mul(be1, add(al[1], c(-4))), scale(mul(be1, be1), Q(1, 4)))
Dbar = add(scale(mul(al[1], al[1]), 4), scale(al[1], -16), c(Q(212, 9)), scale(mul(al[1], al[2]), Q(-5, 6)),
           mul(be1, add(al[2], scale(mul(al[1], al[1]), -1), scale(al[1], 4), c(Q(-70, 9)))))
d56 = sub(r[4], r[5])
assert zero(sub(sub(Abar, A), scale(mul(d56, d56), Q(1, 4))))
assert zero(sub(sub(Dbar, D), sub(scale(mul(al[1], al[2]), Q(1, 6)), al[3])))
a = r[:4]
sos3 = {}
for i in range(4):
    for j in range(4):
        for k in range(j + 1, 4):
            if i in (j, k): continue
            dd = sub(a[j], a[k]); sos3 = add(sos3, scale(mul(a[i], mul(dd, dd)), Q(1, 2)))
assert zero(sub(sub(mul(al[1], al[2]), scale(al[3], 6)), sos3))
sos2 = {}
for i in range(4):
    for j in range(i + 1, 4): dd = sub(a[i], a[j]); sos2 = add(sos2, mul(dd, dd))
assert zero(sub(sub(scale(mul(al[1], al[1]), 3), scale(al[2], 8)), sos2))
sos6 = {}
for i in range(6):
    for j in range(i + 1, 6): dd = sub(r[i], r[j]); sos6 = add(sos6, mul(dd, dd))
assert zero(sub(sub(scale(mul(f[1], f[1]), 5), scale(f[2], 12)), sos6))
four = sub(c(4), f[1])
assert zero(sub(sub(A, mul(four, four)), add(f[2], scale(f[1], 4), scale(mul(f[1], f[1]), -1), c(Q(-70, 9)))))
# univariate: -(7/12)s^2+4s-70/9 = -58/63-(7/12)(s-24/7)^2
s_ = var(0, 1); one = {(0,): Q(1)}
lhs = add(scale(mul(s_, s_), Q(-7, 12)), scale(s_, 4), {(0,): Q(-70, 9)})
sh = add(s_, {(0,): Q(-24, 7)})
assert zero(sub(lhs, add({(0,): Q(-58, 63)}, scale(mul(sh, sh), Q(-7, 12)))))
print('identities PASS (stdlib sparse Fraction polynomials)')

# characteristic matching: coefficients of y((y+1)^2+8/9)^2 (y^2+p y+q), in p,q
def upoly_mul(P, R_):
    o = [Q(0)] * (len(P) + len(R_) - 1)
    for i, u in enumerate(P):
        for j, v in enumerate(R_): o[i + j] += u * v
    return o
base = upoly_mul([Q(0), Q(1)], upoly_mul([Q(17, 9), Q(2), Q(1)], [Q(17, 9), Q(2), Q(1)]))  # ascending y-powers
# target coefficient of y^k = base[k-2] + p*base[k-1] + q*base[k] ; represent as (const, p-coef, q-coef)
tgt = {k: ((base[k - 2] if k >= 2 else 0), (base[k - 1] if k >= 1 else 0), (base[k] if k < len(base) else 0)) for k in range(3, 7)}
assert tgt[6] == (Q(4), Q(1), Q(0)) and tgt[5] == (Q(70, 9), Q(4), Q(1))
assert tgt[4] == (Q(68, 9), Q(70, 9), Q(4)) and tgt[3] == (Q(289, 81), Q(68, 9), Q(70, 9))
# with p=e1-4, q=e2-4e1+74/9: e3-W = tgt4 => W = e3-4e2+(74/9)e1-28/3 ; e4-CW-C4 = tgt3 => CW+C4 = e4-(70/9)e2+(212/9)e1-1007/27
cW = Q(68, 9) + Q(70, 9) * (-4) + 4 * Q(74, 9)
assert (cW, Q(70, 9) - 16) == (Q(28, 3), Q(-74, 9))
cCW = Q(289, 81) + Q(68, 9) * (-4) + Q(70, 9) * Q(74, 9)
assert (cCW, Q(68, 9) - 4 * Q(70, 9)) == (Q(1007, 27), Q(-212, 9))
print('characteristic matching constants PASS')

# ---------- (ii) girth-four digest binding ----------
m = 6; u = [var(i, m) for i in range(m)]
g = [esym(u, k, m) for k in range(5)]
cm = lambda a_: const(a_, m)
Ag = add(g[2], scale(g[1], -4), cm(Q(74, 9))); Bg = add(g[3], scale(g[2], -4), scale(g[1], Q(74, 9)), cm(Q(-28, 3)))
h0g = add(g[4], scale(g[2], Q(-70, 9)), scale(g[1], Q(212, 9)), cm(Q(-1007, 27))); h1g = add(g[3], scale(g[1], Q(-70, 9)), cm(Q(212, 9)))
Qg = scale(sub(mul(Ag, Ag), mul(add(g[1], cm(-4)), Bg)), 81)
Hg = scale(sub(mul(h0g, Ag), mul(h1g, Bg)), -243)
def dig(P):
    assert all(v.denominator == 1 for v in P.values())
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
G4 = json.loads((ROOT / 'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json').read_text())
assert dig(Qg) == G4['Q_coefficients_sha256'] and dig(Hg) == G4['H_coefficients_sha256']
print('girth-four Qpol/Hpol digests reproduced independently')

# ---------- (iii) residual polynomials and cover ----------
C = json.loads((ROOT / 'frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json').read_text())
t = 3; Y = var(0, t); T = var(1, t); G = var(2, t); ct = lambda a_: const(a_, t)
b1 = add(scale(Y, Q(1, 2)), G); a2 = scale(mul(T, mul(Y, Y)), Q(3, 8))
PA = scale(add(a2, scale(Y, -4), ct(Q(74, 9)), mul(b1, add(Y, ct(-4))), scale(mul(b1, b1), Q(1, 4))), 144)
PD = scale(add(scale(mul(Y, Y), 4), scale(Y, -16), ct(Q(212, 9)), scale(mul(Y, a2), Q(-5, 6)),
               mul(b1, add(a2, scale(mul(Y, Y), -1), scale(Y, 4), ct(Q(-70, 9))))), 144)
PF = scale(add(Y, b1, ct(-4)), 2)
polys = {'Abar': PA, 'Dbar': PD, 'f1minus4': PF}
for k_, P in polys.items(): assert dig(P) == C['polynomials'][k_]['sha256'], k_
def degs(P): return [max(e[i] for e in P) for i in range(3)]
def bernstein(P):
    dy, dt, dg = degs(P); B_ = {}
    for i in range(dy + 1):
        for mm in range(dt + 1):
            for k in range(dg + 1):
                v = Q(0)
                for j in range(mm + 1): v += P.get((i, j, k), Q(0)) * Q(math.comb(mm, j), math.comb(dt, j))
                B_[(i, mm, k)] = v / (math.comb(dy, i) * math.comb(dg, k))
    return (dy, dt, dg), B_
def halve(shape, B_, axis, upper):
    d = shape[axis]; out = {}
    others = [range(s + 1) for i, s in enumerate(shape) if i != axis]
    for rest in itertools.product(*others):
        def key(idx):
            kk = list(rest); kk.insert(axis, idx); return tuple(kk)
        row = [B_[key(i)] for i in range(d + 1)]
        tri = [row]
        for _ in range(d): prev = tri[-1]; tri.append([(prev[i] + prev[i + 1]) / 2 for i in range(len(prev) - 1)])
        new = [tri[d - i][-1] for i in range(d + 1)] if upper else [tri[i][0] for i in range(d + 1)]
        for i in range(d + 1): out[key(i)] = new[i]
    return out
leaves = {p: lab for p, lab in C['leaves']}
for p1 in leaves:
    for p2 in leaves: assert p1 == p2 or not p2.startswith(p1), (p1, p2)
start = {k_: bernstein(P) for k_, P in polys.items()}
counts = {}
def walk(path, state):
    if path in leaves:
        lab = leaves[path]
        name, rule = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}[lab]
        vals = state[name][1].values()
        assert (max(vals) <= 0) if rule == 'le' else (max(vals) < 0), (path, lab)
        counts[lab] = counts.get(lab, 0) + 1; return
    assert any(l.startswith(path) for l in leaves), ('uncovered', path)
    ax = len(path) % 3
    for bit in '01':
        new = {}
        for k_, (shape, B_) in state.items():
            new[k_] = (shape, halve(shape, B_, ax, bit == '1') if shape[ax] > 0 else B_)
        walk(path + bit, new)
walk('', start)
assert counts == C['leaf_counts'], counts
print('Independent stdlib Fraction replay PASS: complete binary cover,', sum(counts.values()), 'leaves', counts)
