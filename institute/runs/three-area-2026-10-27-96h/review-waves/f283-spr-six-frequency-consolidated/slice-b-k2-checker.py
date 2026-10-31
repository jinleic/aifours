#!/usr/bin/env python3
"""Slice B independent K2 checker for wave f283-spr-six-frequency-consolidated.

Definition-first derivation of the eight cleared-denominator integer polynomials
N_{x,m} = Vdm * D_x * J_{3-m} of S1 line 71, from:
  * the Lagrange extreme-ray weights of S1 lines 42-44
    w_i^{(k)} = e_{3-k}(u_hat_i) / (u_i O_i(u_i) H'(u_i)),
  * the ray F-pairing sum  S = sum_i w_i^{(k)} E_i(u_i) F(u_i)  (S1 line 46),
  * phase-C first-gap case (S1 lines 61-63): F(t) = -t(b-t)(e-t), worst even
    lower envelope E(t) = (x-t)(c-t)(d-t), worst odd endpoints (O+,O+,O-,O-)
    with unit envelopes O+^0=(b-t)(c-t)(f-t), O-^0=(a-t)(d-t)(e-t), a=1,
  * the nine-gap parametrization b=1+B, u1=b+U, c=u1+V, u2=c+X, u3=u2+Y,
    d=u3+Z, u4=d+P, e=u4+W, f=e+R (S1 line 71).

Derived here by exact algebra (verified symbolically and pointwise below):
  term_i = e_m(u_hat_i) * [E(u)F(u)/(u*O^0(u))] / H'(u_i)
         = e_m(u_hat_i) * g_{sigma_i}(u_i) / H'(u_i),
  g at nodes 1,2 (sigma=+): u(d-u)(e-u)/(f-u)  [x=0],  (u-1)(d-u)(e-u)/(f-u)  [x=1]
  g at nodes 3,4 (sigma=-): -u(b-u)(c-u)/(u-1) [x=0],  -(b-u)(c-u)            [x=1]
  H'(u_i) = prod_{j!=i}(u_i-u_j); Vdm = prod_{i<j}(u_j-u_i) = (-1)^{4-i} H'(u_i) Vdm(u_hat_i)
  D_0=(f-u1)(f-u2)(u3-1)(u4-1), D_1=(f-u1)(f-u2) clear the remaining denominators.
So N_{x,m} = sum_i (-1)^{4-i} e_m(u_hat_i) Vdm(u_hat_i) * [D_x factors after
cancelling g's denominator] * [g numerator] is exactly the polynomial equal to
Vdm*D_x*J_{3-m}; positivity of every nonzero coefficient certifies J>0 for all
positive gaps.

The author kernel frontier-20261029-phase-c-gap-positive-polynomials-kernel-v1.py
was never read/imported/executed (metadata only). Standard library only; exact
integer/Fraction arithmetic; single core; single process (well under 120 s in
pre-freeze benchmarks of the same engine).
"""
import sys, os, json, time, hashlib, platform, datetime, resource
from fractions import Fraction as F
from itertools import combinations

T0 = time.time()
WAVE = os.path.dirname(os.path.abspath(__file__))
SELFPATH = os.path.abspath(__file__)

# ---------------- exact multivariate polynomial engine (packed-int exponents) --
NV = 9
def pk(e):
    k = 0
    for i in range(NV): k |= e[i] << (4 * i)
    return k
def unpack(k):
    return tuple((k >> (4 * i)) & 15 for i in range(NV))
ZERO = pk((0,) * NV)
def const(c): return {ZERO: c} if c else {}
_varcache = {}
def var(i):
    if i not in _varcache:
        _varcache[i] = {pk(tuple(1 if j == i else 0 for j in range(NV))): 1}
    return _varcache[i]
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        nv = r.get(k, 0) + v
        if nv: r[k] = nv
        elif k in r: del r[k]
    return r
def pneg(a): return {k: -v for k, v in a.items()}
def psub(a, b): return padd(a, pneg(b))
def pmul(a, b):
    if len(a) > len(b): a, b = b, a
    r = {}
    g = r.get
    for ea, ca in a.items():
        for eb, cb in b.items():
            k = ea + eb
            nv = g(k, 0) + ca * cb
            if nv: r[k] = nv
            elif k in r: del r[k]
            g = r.get
    return r
def pmul_seq(factors):
    acc = {ZERO: 1}
    for f in sorted(factors, key=len): acc = pmul(acc, f)
    return acc
def peval(a, vals):
    s = F(0)
    for k, c in a.items():
        e = unpack(k); t = F(c)
        for i in range(NV):
            if e[i]: t *= vals[i] ** e[i]
        s += t
    return s

B, U, V, X, Y, Z, P, W, R = (var(i) for i in range(NV))
ONE = {ZERO: 1}
b_ = padd(ONE, B); u1 = padd(b_, U); c_ = padd(u1, V); u2 = padd(c_, X)
u3 = padd(u2, Y); d_ = padd(u3, Z); u4 = padd(d_, P); e_ = padd(u4, W); f_ = padd(e_, R)
NODES = [u1, u2, u3, u4]
OTHERS = {1: [u2, u3, u4], 2: [u1, u3, u4], 3: [u1, u2, u4], 4: [u1, u2, u3]}
SGN = {1: -1, 2: 1, 3: -1, 4: 1}   # (-1)^{4-i} = sign(Vdm/H'(u_i))

def efun(polys, m):
    acc = {}
    for comb in combinations(range(len(polys)), m):
        t = {ZERO: 1}
        for j in comb: t = pmul(t, polys[j])
        acc = padd(acc, t)
    return acc
def vdm3(o):
    return pmul_seq([psub(o[1], o[0]), psub(o[2], o[0]), psub(o[2], o[1])])

def term_factors(x, i):
    """([remaining D_x factors after cancelling g's denominator], [g numerator factors])"""
    if x == 0:
        if i == 1: return [psub(f_, u2), psub(u3, ONE), psub(u4, ONE)], [u1, psub(d_, u1), psub(e_, u1)]
        if i == 2: return [psub(f_, u1), psub(u3, ONE), psub(u4, ONE)], [u2, psub(d_, u2), psub(e_, u2)]
        if i == 3: return [psub(f_, u1), psub(f_, u2), psub(u4, ONE)], [pneg(u3), psub(b_, u3), psub(c_, u3)]
        return [psub(f_, u1), psub(f_, u2), psub(u3, ONE)], [pneg(u4), psub(b_, u4), psub(c_, u4)]
    else:
        if i == 1: return [psub(f_, u2)], [psub(u1, ONE), psub(d_, u1), psub(e_, u1)]
        if i == 2: return [psub(f_, u1)], [psub(u2, ONE), psub(d_, u2), psub(e_, u2)]
        if i == 3: return [psub(f_, u1), psub(f_, u2)], [{ZERO: -1}, psub(b_, u3), psub(c_, u3)]
        return [psub(f_, u1), psub(f_, u2)], [{ZERO: -1}, psub(b_, u4), psub(c_, u4)]

def build_N(x, m, mut=None):
    """mut: None | 'sign' (flip H'(u1) orientation sign at node 1)
             | 'term' (omit node-4 term) | 'em' (e_m -> e_{m+1} if m<3 else e_{m-1})
             | 'den' (omit (u3-1),(u4-1) clearing factors at nodes 3,4)"""
    N = {}
    for i in (1, 2, 3, 4):
        if mut == "term" and i == 4: continue
        o = OTHERS[i]
        rest, gn = term_factors(x, i)
        if mut == "den" and i in (3, 4):
            drops = [psub(u3, ONE), psub(u4, ONE)]
            rest = [q for q in rest if q not in drops]
        mm = m
        if mut == "em": mm = m + 1 if m < 3 else m - 1
        s = SGN[i]
        if mut == "sign" and i == 1: s = -s
        T = pmul_seq([efun(o, mm), vdm3(o)] + rest + gn)
        N = padd(N, T if s > 0 else pneg(T))
    return N

# ---------------- exact rational pointwise reference (independent of engine) ---
PTS = [tuple(F(1) for _ in range(9)),
       (F(2), F(1), F(3), F(1), F(2), F(1), F(4), F(2), F(1)),
       (F(1), F(2), F(1), F(5), F(1), F(1), F(3), F(2), F(5)),
       (F(3), F(1), F(1), F(2), F(5), F(1), F(1), F(4), F(2))]
def efrac(v, m):
    s = F(0)
    for comb in combinations(range(len(v)), m):
        t = F(1)
        for j in comb: t *= v[j]
        s += t
    return s
def gaps_to_nodes(p):
    b = 1 + p[0]; u1v = b + p[1]; cv = u1v + p[2]; u2v = cv + p[3]
    u3v = u2v + p[4]; dv = u3v + p[5]; u4v = dv + p[6]; ev = u4v + p[7]; fv = ev + p[8]
    return b, u1v, cv, u2v, u3v, dv, u4v, ev, fv
def Jpt(x, m, p):
    """J_{3-m} from the written definition sum_i e_m(u_hat_i) g_{sigma_i}(u_i)/H'(u_i),
    with a second independent raw route E*F/(u*O^0) asserted equal per node.
    Returns (J, raw_route_equal_at_all_nodes)."""
    b, u1v, cv, u2v, u3v, dv, u4v, ev, fv = gaps_to_nodes(p)
    u = [u1v, u2v, u3v, u4v]; xv = F(x); tot = F(0); raw_eq = True
    for i in range(4):
        oth = [u[j] for j in range(4) if j != i]; em = efrac(oth, m); t = u[i]
        if i < 2:
            g = ((t if x == 0 else t - 1) * (dv - t) * (ev - t)) / (fv - t)
            Oraw = (b - t) * (cv - t) * (fv - t)
        else:
            g = (-(t * (b - t) * (cv - t)) / (t - 1)) if x == 0 else (-(b - t) * (cv - t))
            Oraw = (1 - t) * (dv - t) * (ev - t)
        E = (xv - t) * (cv - t) * (dv - t); Ff = -t * (b - t) * (ev - t)
        if E * Ff / (t * Oraw) != g: raw_eq = False
        Hp = F(1)
        for j in range(4):
            if j != i: Hp *= (t - u[j])
        tot += em * g / Hp
    return tot, raw_eq
def VDpt(p):
    _, u1v, _, u2v, u3v, _, u4v, _, _ = gaps_to_nodes(p); u = [u1v, u2v, u3v, u4v]
    v = F(1)
    for i in range(4):
        for j in range(i + 1, 4): v *= u[j] - u[i]
    return v
def Dxpt(x, p):
    _, u1v, _, u2v, u3v, _, u4v, _, fv = gaps_to_nodes(p)
    if x == 0: return (fv - u1v) * (fv - u2v) * (u3v - 1) * (u4v - 1)
    return (fv - u1v) * (fv - u2v)

# ---------------- symbolic aux proofs (exact zero-polynomial checks) ----------
aux = {}
# Z1: Vdm = (-1)^{4-i} H'(u_i) Vdm(u_hat_i) for each i (denominator clearing of H')
z1_ok = True
Vdm_full = pmul_seq([psub(NODES[j], NODES[i]) for i in range(4) for j in range(i + 1, 4)])
for i in (1, 2, 3, 4):
    o = OTHERS[i]
    Hp = pmul_seq([psub(NODES[i - 1], NODES[j - 1]) for j in (1, 2, 3, 4) if j != i])
    rhs = Hp if SGN[i] > 0 else pneg(Hp)
    rhs = pmul(rhs, vdm3(o))
    if padd(Vdm_full, pneg(rhs)) != {}: z1_ok = False
aux["Z1_Vdm_factorization_exact"] = z1_ok

# Z2: sign orientation / unit reduction: E*F*Gden == t*O^0*Gnum exactly, in 10 vars
def engine10():
    NV10 = 10
    def pk10(e):
        k = 0
        for i in range(NV10): k |= e[i] << (4 * i)
        return k
    def v10(i):
        return {pk10(tuple(1 if j == i else 0 for j in range(NV10))): 1}
    def mul(a, bb):
        r = {}
        g = r.get
        for ea, ca in a.items():
            for eb, cb in bb.items():
                k = ea + eb
                nv = g(k, 0) + ca * cb
                if nv: r[k] = nv
                elif k in r: del r[k]
                g = r.get
        return r
    def seq(fs):
        acc = {pk10((0,) * NV10): 1}
        for f in sorted(fs, key=len): acc = mul(acc, f)
        return acc
    def sub(a, bb):
        r = dict(a)
        for k, val in bb.items():
            nv = r.get(k, 0) - val
            if nv: r[k] = nv
            elif k in r: del r[k]
        return r
    def neg(a): return {k: -v for k, v in a.items()}
    return v10, mul, seq, sub, neg, pk10((0,) * NV10)
v10, mul10, seq10, sub10, neg10, O10 = engine10()
BV, UV, VV, XV, YV, ZV, PV, WV, RV, TV = (v10(i) for i in range(10))
ONE10 = {O10: 1}
b10 = seq10([ONE10, BV]); u110 = seq10([b10, UV]); c10 = seq10([u110, VV]); u210 = seq10([c10, XV])
u310 = seq10([u210, YV]); d10 = seq10([u310, ZV]); u410 = seq10([d10, PV]); e10 = seq10([u410, WV]); f10 = seq10([e10, RV])
z2 = {}
for x in (0, 1):
    xt = ONE10 if x == 1 else {}
    E10 = seq10([sub10(xt, TV), sub10(c10, TV), sub10(d10, TV)])
    F10 = seq10([neg10(seq10([TV, sub10(b10, TV)])), sub10(e10, TV)])       # -t(b-t)(e-t)
    Opos = seq10([sub10(b10, TV), sub10(c10, TV), sub10(f10, TV)])
    Oneg = seq10([sub10(ONE10, TV), sub10(d10, TV), sub10(e10, TV)])
    Gnum_pos = seq10([sub10(TV, xt), sub10(d10, TV), sub10(e10, TV)])
    Gden_pos = sub10(f10, TV)
    lhs_pos = seq10([E10, F10, Gden_pos]); rhs_pos = seq10([TV, Opos, Gnum_pos])
    z2["x=%d_sigma+_E*F*Gden==t*Oplus0*Gnum" % x] = (sub10(lhs_pos, rhs_pos) == {})
    if x == 0:
        Gnum_neg = neg10(seq10([TV, sub10(b10, TV), sub10(c10, TV)]))
        lhs_neg = seq10([E10, F10, sub10(TV, ONE10)])
    else:
        Gnum_neg = neg10(seq10([sub10(b10, TV), sub10(c10, TV)]))
        lhs_neg = seq10([E10, F10])
    rhs_neg = seq10([TV, Oneg, Gnum_neg])
    z2["x=%d_sigma-_E*F*Gden==t*Ominus0*Gnum" % x] = (sub10(lhs_neg, rhs_neg) == {})
aux["Z2_sign_orientation_unit_reduction_exact"] = z2

# S+ closed form (S1|71): S_+ = [q2*(u2-x)*h(u2) - q1*(u1-x)*h(u1)]/(u2-u1)
def Spoint(x, m, p):
    b, u1v, cv, u2v, u3v, dv, u4v, ev, fv = gaps_to_nodes(p)
    Splus = F(0)
    for i in (0, 1):
        oth = [[u2v, u3v, u4v], [u1v, u3v, u4v]][i]
        t = [u1v, u2v][i]
        g = ((t if x == 0 else t - 1) * (dv - t) * (ev - t)) / (fv - t)
        Hp = (t - u2v) * (t - u3v) * (t - u4v) if i == 0 else (t - u1v) * (t - u3v) * (t - u4v)
        Splus += efrac(oth, m) * g / Hp
    q1 = efrac([u2v, u3v, u4v], m); q2 = efrac([u1v, u3v, u4v], m)
    def h(t): return (dv - t) * (ev - t) / ((u3v - t) * (u4v - t) * (fv - t))
    closed = (q2 * (u2v - x) * h(u2v) - q1 * (u1v - x) * h(u1v)) / (u2v - u1v)
    qdiff_id = (q2 * (u2v - x) - q1 * (u1v - x)
                == (u2v - u1v) * (efrac([u3v, u4v], m)
                                  - x * (efrac([u3v, u4v], m - 1) if m >= 1 else F(0))))
    return Splus, closed, qdiff_id
sp = {}
for x in (0, 1):
    for m in range(4):
        oks = []
        for p in PTS:
            s, cl, qd = Spoint(x, m, p)
            oks.append(s == cl and qd and s > 0)
        sp["x=%d,m=%d" % (x, m)] = all(oks)
aux["Splus_closed_form_and_qdiff_identities_and_positivity"] = sp

# e_m(u_hat_i) nonincreasing in i (S1|44 note): deterministic rational points
MONO_PTS = [tuple(F((7 * i * k + 3 * k + 5) % 11 + 1, (k + 2)) for k in range(9)) for i in range(20)]
mono_ok = True
for p in MONO_PTS:
    _, u1v, _, u2v, u3v, _, u4v, _, _ = gaps_to_nodes(p)
    u = [u1v, u2v, u3v, u4v]
    for m in range(4):
        vals = [efrac([u[j] for j in range(4) if j != i], m) for i in range(4)]
        if not (vals[0] >= vals[1] >= vals[2] >= vals[3]): mono_ok = False
aux["e_m_nonincreasing_in_i_at_20_rational_points"] = mono_ok

# ---------------- main expansion of all eight polynomials ---------------------
cases = {}
polyfiles = {}
for x in (0, 1):
    for m in range(4):
        t_start = time.time()
        N = build_N(x, m)
        t_build = time.time() - t_start
        coeffs = sorted((unpack(k), c) for k, c in N.items())
        allpos = all(c > 0 for _, c in coeffs)
        ident_ok = True; raw_ok_all = True; pospts_ok = True
        for p in PTS:
            J, raw_eq = Jpt(x, m, p)
            if not raw_eq: raw_ok_all = False
            if peval(N, p) != VDpt(p) * Dxpt(x, p) * J: ident_ok = False
            if not (J > 0 and peval(N, p) > 0): pospts_ok = False
        # canonical serialization (mine, explicit): lines "e_B,e_U,e_V,e_X,e_Y,e_Z,e_P,e_W,e_R:c"
        # sorted by exponent tuple ascending; file sha256 = digest of this convention
        lines = ["%d,%d,%d,%d,%d,%d,%d,%d,%d:%d" % (e + (c,)) for e, c in coeffs]
        blob = ("\n".join(lines) + "\n").encode()
        digest = hashlib.sha256(blob).hexdigest()
        fn = os.path.join(WAVE, "slice-b-k2-poly-x%d-m%d.txt" % (x, m))
        with open(fn, "w") as fh: fh.write("\n".join(lines) + "\n")
        polyfiles["x%d_m%d" % (x, m)] = os.path.basename(fn)
        # author-digest convention attempts (pre-declared, 2 variants; variable order S3|114-124)
        blobA1 = ("\n".join("%d,%d,%d,%d,%d,%d,%d,%d,%d:%d" % (e + (c,))
                            for e, c in sorted(coeffs, key=lambda t: (sum(t[0]), t[0]))) + "\n").encode()
        blobA2 = ("\n".join("B^%d*U^%d*V^%d*X^%d*Y^%d*Z^%d*P^%d*W^%d*R^%d:%d" % (e + (c,))
                            for e, c in coeffs) + "\n").encode()
        cases["x%d_m%d" % (x, m)] = {
            "monomials": len(N), "coefficient_sum": sum(N.values()),
            "min_coefficient": min(N.values()), "max_coefficient": max(N.values()),
            "all_coefficients_strictly_positive": allpos,
            "pointwise_identity_N_eq_VdmDxJ_4pts": ident_ok,
            "raw_route_eq_g_route_all_nodes": raw_ok_all,
            "J_positive_at_4pts": pospts_ok,
            "canonical_sha256_own_convention": digest,
            "author_digest_attempt_A1_graded_lex_colon": hashlib.sha256(blobA1).hexdigest(),
            "author_digest_attempt_A2_lex_caret": hashlib.sha256(blobA2).hexdigest(),
            "build_seconds": round(t_build, 3),
        }

S3_CLAIM = {  # author claims from packet S3|8-112 (compared AFTER computation)
    "x0": {0: (11357, 369600, 1, 837, "21dfbc28fccdfb436ac7d562582bc13df6f128484d713147bb799c9307ee0102"),
           1: (27170, 6384000, 1, 7983, "9a9f4d4684a79da37811f9a022622bc8d529263008d02e5bdca6288c51118943"),
           2: (53462, 32709600, 1, 28620, "f039fa325cfdc0daeafaf8e66b9f64736cfadc4c031e3ea65242d8a6dfb9dcf5"),
           3: (89883, 48384000, 1, 34968, "2eba62731d20117bfcfe90fb9e3a5b4789dc34353e765c01bd0a7c2d772e0b72")},
    "x1": {0: (1292, 8640, 1, 78, "dd3834e2a6101f0e53c1f4ba21668fafc92124841d58e4891be43f1f73cdaa21"),
           1: (4969, 150720, 1, 534, "595e513f1b7c574181835e515b49da0e125fbe05975f32fbb97ca244ed92780d"),
           2: (12719, 780960, 1, 1269, "7e621b63f691e412ea15f69e8d0fee8439bc02290886661de1dc6e69dbb078d5"),
           3: (24167, 1176480, 1, 1320, "4d7bf583f8fd0f45f37a67e801b6cf98f66e751298037162fc5105ddaf616099")}}
for x in (0, 1):
    for m in range(4):
        c = cases["x%d_m%d" % (x, m)]; e = S3_CLAIM["x%d" % x][m]
        c["vs_S3_counts_sum_min_max"] = (c["monomials"] == e[0] and c["coefficient_sum"] == e[1]
                                          and c["min_coefficient"] == e[2] and c["max_coefficient"] == e[3])
        c["vs_S3_sha_any_attempt_match"] = e[4] in (c["canonical_sha256_own_convention"],
                                                    c["author_digest_attempt_A1_graded_lex_colon"],
                                                    c["author_digest_attempt_A2_lex_caret"])

# ---------------- mutations: must fail for their intended reason ---------------
muts = {}
for (x, m, kind, reason) in [
        (0, 0, "sign", "flip H'(u_1) orientation sign at node 1: object no longer equals Vdm*D_x*J (wrong sign orientation)"),
        (1, 3, "sign", "flip H'(u_1) orientation sign at node 1: object no longer equals Vdm*D_x*J (wrong sign orientation)"),
        (0, 0, "em", "e_m replaced by e_{m+1}: wrong Lagrange weight index in the ray"),
        (0, 3, "term", "node-4 term omitted from the ray sum"),
        (0, 3, "den", "omit (u3-1),(u4-1) denominator-clearing factors at nodes 3,4")]:
    Nm = build_N(x, m, mut=kind)
    N0 = build_N(x, m)
    pts = PTS[:2]
    differs = all(peval(Nm, p) != peval(N0, p) for p in pts)
    J0 = [Jpt(x, m, p)[0] for p in pts]
    if kind == "den":
        ident_fail = all(peval(Nm, p) != VDpt(p) * Dxpt(0, p) * J0[k]
                         and peval(Nm, p) != VDpt(p) * Dxpt(1, p) * J0[k]
                         for k, p in enumerate(pts))
    else:
        ident_fail = all(peval(Nm, p) != VDpt(p) * Dxpt(x, p) * J0[k] for k, p in enumerate(pts))
    muts["%s_x%d_m%d" % (kind, x, m)] = {
        "intended_reason": reason,
        "monomials": len(Nm),
        "all_coefficients_strictly_positive": all(v > 0 for v in Nm.values()),
        "differs_from_N_at_2pts": differs,
        "identity_N_eq_VdmDxJ_fails": ident_fail,
        "fails_for_intended_reason": differs and ident_fail,
    }

internal_ok = (aux["Z1_Vdm_factorization_exact"]
               and all(aux["Z2_sign_orientation_unit_reduction_exact"].values())
               and all(sp.values()) and mono_ok
               and all(c["pointwise_identity_N_eq_VdmDxJ_4pts"] and c["raw_route_eq_g_route_all_nodes"]
                       for c in cases.values())
               and all(v["fails_for_intended_reason"] for v in muts.values()))
receipt = {
    "kind": "slice-B independent K2 exact polynomial expansion receipt",
    "wave": "f283-spr-six-frequency-consolidated",
    "source": os.path.basename(SELFPATH),
    "checker_sha256_at_run": hashlib.sha256(open(SELFPATH, "rb").read()).hexdigest(),
    "python": platform.python_version(), "platform": platform.platform(),
    "argv": sys.argv,
    "clock_start_utc": datetime.datetime.fromtimestamp(T0, datetime.timezone.utc).isoformat(),
    "definitions_only_from": "S1 lines 42-44,46,50,63,71 (packet literal-packet-v1.md)",
    "canonical_digest_convention_own": "lines 'e_B,e_U,e_V,e_X,e_Y,e_Z,e_P,e_W,e_R:c' sorted by exponent tuple ascending, LF-terminated, sha256",
    "author_digest_convention": "not specified in S1/S3 beyond variable order (S3|114-124); two pre-declared attempts A1 (graded-lex sort, colon format) and A2 (lex sort, caret format) reported; mismatch is inconclusive",
    "aux_symbolic_and_rational_checks": aux,
    "cases": cases,
    "mutations": muts,
    "poly_files": polyfiles,
    "internal_all_checks_pass": internal_ok,
    "all_eight_all_coefficients_strictly_positive": all(c["all_coefficients_strictly_positive"] for c in cases.values()),
    "all_eight_vs_S3_counts_sum_min_max": all(c["vs_S3_counts_sum_min_max"] for c in cases.values()),
    "any_S3_digest_match": any(c["vs_S3_sha_any_attempt_match"] for c in cases.values()),
    "author_kernel_read_or_executed": False,
    "slice_A_or_other_review_read": False,
    "peak_rss_kb_observed": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "memory_admission_estimate": "well under 2 GiB (largest object ~90k monomials; observed peak RSS recorded above)",
    "clock_end_utc": datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).isoformat(),
    "wall_seconds": round(time.time() - T0, 3),
}
with open(os.path.join(WAVE, "slice-b-k2-receipt.json"), "w") as fh:
    json.dump(receipt, fh, indent=1)
print("K2: all eight positive:", receipt["all_eight_all_coefficients_strictly_positive"],
      "| vs S3 counts/sums/min/max:", receipt["all_eight_vs_S3_counts_sum_min_max"],
      "| internal:", internal_ok, "| any digest match:", receipt["any_S3_digest_match"])
for k in sorted(cases):
    print(" ", k, cases[k]["monomials"], cases[k]["coefficient_sum"],
          cases[k]["all_coefficients_strictly_positive"], cases[k]["vs_S3_counts_sum_min_max"])
for k, v in muts.items():
    print(" MUT", k, "fails_intended:", v["fails_for_intended_reason"],
          "still_all_positive:", v["all_coefficients_strictly_positive"])
sys.exit(0 if internal_ok else 1)
