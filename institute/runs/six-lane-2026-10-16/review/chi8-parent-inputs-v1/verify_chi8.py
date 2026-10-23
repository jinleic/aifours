"""Verifier for review/PROOF_CHI8.r1.md (chi(G_{n,8}) = 4 a.a.s.), lane random8reg-colour.
Exact rationals, big integers, sympy and python-flint arb (256 bits). Self-contained; reads nothing from other lanes.

Sections (keys of ../evidence/verify_chi8.json):
  A  (k,d) = (4,8) arithmetic: (H1), series ratio, SSC numbers, (1.2)-(1.3), E(Y^2) constant, EY growth,
     simple-graph limits, KPW threshold arithmetic, Molloy-Reed, Theorem 10 parameters (k', residues, l, counts).
  B  Lemma A exponent algebra, Proposition B, Theorem C identities (sympy); 7 < e^2 (exact rational);
     D-SC alpha at |X| = 4; constants a, kappa, C_8 (arb).
  C  Row inequality, Proof 2: arb subdivision of both two-value families + Taylor neighbourhoods (c = 1/40).
  D  Controls: the route's condition fails at d = 9; mutations; KPW's relaxed phi_8 > phi_8(J) but U < U(J) at
     (J+I)/2; Theorem C at explicit rational doubly stochastic points.
  E  Lemma A exponent control at M = I: exact |T(I)|/|P_{4t,8}| for t <= 30 against U(I) = 4 ln 3 - 6 ln 2.
  S  Float sanity (NOT evidence): U - Psi_8 >= 0 on random doubly stochastic matrices; decay ratios.
Run (from code/): OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B verify_chi8.py
"""
import json
import math
import os
from fractions import Fraction as Fr
from math import factorial

import numpy as np
import sympy as sp
from flint import arb, ctx

ctx.prec = 256
HERE = os.path.dirname(os.path.abspath(__file__))


def A_(x):
    if isinstance(x, Fr):
        return arb(x.numerator) / arb(x.denominator)
    return arb(x)


def certain_pos(v):
    return bool(v > 0)


# ---------------------------------------------------------------------------------------------------------- A
def section_A():
    k, d = 4, 8
    out = {}
    H1 = k * k - 2 * k - d + 2
    out["(H1) k^2-2k-d+2"] = H1
    out["(H1) > 0"] = H1 > 0
    ratio = Fr(d - 1, (k - 1) ** 2)
    out["series ratio (d-1)/(k-1)^2"] = str(ratio)
    out["series ratio < 1"] = ratio < 1
    growth = Fr(k) * Fr(k - 1, k) ** (d // 2)
    out["EY growth k(1-1/k)^(d/2)"] = str(growth)
    out["EY growth > 1"] = growth > 1
    out["lambda_1 = (d-1)/2"] = str(Fr(d - 1, 2))
    out["lambda_2 = (d-1)^2/4"] = str(Fr((d - 1) ** 2, 4))
    out["P(Simple) exponent (1-d^2)/4"] = str(Fr(1 - d * d, 4))
    out["delta_1 = -1 and |delta_i| <= 1/3 for 2 <= i < 40"] = (Fr(-1, (k - 1) ** 0) == -1) and all(
        abs(Fr((-1) ** i, (k - 1) ** (i - 1))) <= Fr(1, 3) for i in range(2, 40))
    m = sp.symbols("m", integer=True, positive=True)
    lam = sp.Integer(d - 1) ** m / (2 * m)
    dl = (-1) ** m / sp.Integer(k - 1) ** (m - 1)
    term = sp.simplify(lam * dl ** 2)
    out["lambda_m delta_m^2 == (9/2)(7/9)^m/m"] = sp.simplify(term - sp.Rational(9, 2) * sp.Rational(7, 9) ** m / m) == 0
    series = sp.summation(sp.Rational(7, 9) ** m / m, (m, 1, sp.oo))
    out["sum_m (7/9)^m/m == ln(9/2)"] = sp.simplify(series - sp.log(sp.Rational(9, 2))) == 0
    kpw12 = sp.Integer(k - 1) ** 2 * sp.log(sp.Integer(k - 1) / sp.sqrt(H1))
    out["KPW (1.2) value (k-1)^2 log((k-1)/sqrt(H1)) == (9/2) ln(9/2)"] = sp.simplify(
        sp.expand_log(kpw12 - sp.Rational(9, 2) * sp.log(sp.Rational(9, 2)), force=True)) == 0
    lhs13 = (sp.Integer(k - 1) / sp.sqrt(H1)) ** ((k - 1) ** 2)
    out["KPW (1.3): ((k-1)/sqrt(H1))^((k-1)^2) == (3/sqrt2)^9 == exp((9/2) ln(9/2))"] = (
        sp.simplify(lhs13 - (3 / sp.sqrt(2)) ** 9) == 0 and
        sp.simplify(lhs13 - sp.exp(sp.Rational(9, 2) * sp.log(sp.Rational(9, 2)))) == 0)
    pi = sp.pi
    c2 = sp.Integer(k) ** k * sp.Integer(k - 1) ** (k * (k - 1)) / (
        sp.Integer(H1) ** sp.Rational((k - 1) ** 2, 2) * (2 * pi * (k - 2)) ** (k - 1))
    c1 = sp.Integer(k) ** sp.Rational(k, 2) * (sp.Integer(k - 1) / (2 * pi * (k - 2))) ** sp.Rational(k - 1, 2)
    out["Prop 2: C2 / C1^2 == (3/sqrt2)^9 (powers of n cancel: n^-(k-1) vs (n^-(k-1)/2)^2)"] = sp.simplify(
        c2 / c1 ** 2 - (3 / sp.sqrt(2)) ** 9) == 0
    out["E(Y^2) constant at (4,8) == 4^4 3^12 / (2^(9/2) (4 pi)^3)"] = sp.simplify(
        c2 - sp.Integer(4) ** 4 * sp.Integer(3) ** 12 / (2 ** sp.Rational(9, 2) * (4 * pi) ** 3)) == 0
    l3, l4 = arb(3).log(), arb(4).log()
    out["KPW: 6 ln3 < 8 < 8 ln4 (KPW's k = 5 at d = 8)"] = bool(6 * l3 < 8) and bool(8 < 8 * l4)
    out["KPW exact clause d > 7 ln4 fails at d = 8 (7 ln4 > 8)"] = bool(7 * l4 > 8)
    out["Molloy-Reed: 3 (2/3)^4 == 16/27 < 1 (exact)"] = (3 * Fr(2, 3) ** 4 == Fr(16, 27)) and Fr(16, 27) < 1
    out["KPW weak form: (2q-1) log q = 5 ln3 < 8 at q = 3"] = bool(5 * l3 < 8)
    kprime = 2 * k if (d * k) % 2 else k
    out["k' (dk = 32 even)"] = kprime
    res = [r for r in range(1, kprime) if (d * r) % 2 == 0]
    out["residues r with 0 < r < k' and dr even"] = res
    out["l = dr/2 for these r"] = [d * r // 2 for r in res]
    pre = {}
    for r in res:
        multin = factorial(d * r) // factorial(d) ** r
        per_G = 1
        for j in range(d * r - 1, 0, -2):
            per_G *= j
        per_G *= factorial(d * r // 2)
        pre[str(r)] = {"multinomial(8r; 8,...,8)": multin, "(8r-1)!! (4r)! choices of (mu, order) per G": per_G}
    out["reduction counts"] = pre
    out["multinomials: (8;8) = 1, (16;8,8) = 12870, (24;8,8,8) = 9465511770"] = (
        pre["1"]["multinomial(8r; 8,...,8)"] == 1 and pre["2"]["multinomial(8r; 8,...,8)"] == 12870
        and pre["3"]["multinomial(8r; 8,...,8)"] == 9465511770)
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["A ok"] = all(bools) and kprime == 4 and res == [1, 2, 3]
    return out


# ---------------------------------------------------------------------------------------------------------- B
def section_B():
    out = {}
    d = sp.Integer(8)
    out["S1 (d-1)/4 - (d/4)(7/8) == 0"] = sp.simplify((d - 1) / 4 - d / 4 * sp.Rational(7, 8)) == 0
    ms = sp.symbols("m0:16", positive=True)
    H4 = -sum(mm / 4 * sp.log(mm / 4) for mm in ms)
    T2 = sum(d * mm / 4 * sp.log(d * mm / 4) for mm in ms)
    lhs = H4 + T2 - d / 2 * sp.log(d)
    rhs = (d - 1) / 4 * sum(mm * sp.log(mm) for mm in ms) + (1 - d) * sp.log(4) + d / 2 * sp.log(d)
    diff = sp.expand(sp.expand_log(lhs - rhs, force=True))
    diff = sp.expand(diff.subs(ms[15], 4 - sum(ms[:15])))
    diff = sp.expand(sp.expand_log(diff, force=True))
    # after expand_log, the m ln m terms must cancel identically; check the remaining linear part is 0
    out["Lemma A exponent: H_4 + sum (dm/4) ln(dm/4) - (d/2) ln d == ((d-1)/4) sum m ln m + (1-d) ln 4 + (d/2) ln d (sum m = 4)"] = (
        sp.simplify(diff) == 0)
    E_, c = sp.symbols("E c", positive=True)
    V = -7 * sp.log(4) + 4 * sp.log(8) + sp.exp(2 * c - 1) * E_ - 8 * c
    cst = sp.solve(sp.diff(V, c), c)[0]
    out["Prop B: argmin has e^(2c-1) == 4/E"] = sp.simplify(sp.exp(2 * cst - 1) - 4 / E_) == 0
    out["Prop B: min value == -10 ln2 + 4 ln E"] = sp.simplify(
        sp.expand_log(V.subs(c, cst) - (-10 * sp.log(2) + 4 * sp.log(E_)), force=True)) == 0
    out["Prop B: V convex in c"] = sp.simplify(sp.diff(V, c, 2) - 4 * sp.exp(2 * c - 1) * E_) == 0
    EJ = 72 * sp.Rational(1, 4) ** sp.Rational(7, 4)
    out["E(J) == 72 * 4^(-7/4) == 9/sqrt2"] = sp.simplify(EJ - 9 / sp.sqrt(2)) == 0
    UJ = -10 * sp.log(2) + 4 * sp.log(9 / sp.sqrt(2))
    out["U(J) == 2 ln4 + 8 ln(3/4)"] = sp.simplify(sp.expand_log(UJ - (2 * sp.log(4) + 8 * sp.log(sp.Rational(3, 4))), force=True)) == 0
    aa = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}"))
    Mds = sp.zeros(4, 4)
    for i in range(3):
        for j in range(3):
            Mds[i, j] = aa[i, j]
        Mds[i, 3] = 1 - sum(aa[i, j] for j in range(3))
    for j in range(4):
        Mds[3, j] = 1 - sum(Mds[i, j] for i in range(3))
    Eds = sum(Mds[p, q] * Mds[r, s] for p in range(4) for q in range(4) for r in range(4) for s in range(4) if p != r and q != s) / 2
    out["generic doubly stochastic M: sum over allowed unordered pairs of m_u m_v == (8 + ||M||^2)/2"] = (
        sp.expand(Eds - (8 + sum(Mds[p, q] ** 2 for p in range(4) for q in range(4))) / 2) == 0)
    F = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"f{i}{j}"))
    lhs2 = sum(F[p, q] * F[r, s] for p in range(4) for q in range(4) for r in range(4) for s in range(4) if p != r and q != s)
    tot = sum(F)
    R = [sum(F[p, :]) for p in range(4)]
    C = [sum(F[:, q]) for q in range(4)]
    rhs2 = tot ** 2 - sum(x ** 2 for x in R) - sum(x ** 2 for x in C) + sum(x ** 2 for x in F)
    out["S3: sum_{p!=r, q!=s} f_pq f_rs == (sum f)^2 - sum R^2 - sum C^2 + sum f^2"] = sp.expand(lhs2 - rhs2) == 0
    cert = (sum(x ** 2 for x in C) - tot ** 2 / 4) + sp.Rational(3, 4) * (4 * sum(x ** 2 for x in R) - sum(R) ** 2)
    out["row-reduction certificate: 2 sum R^2 + sum f^2 - 2E == [sum C^2 - (sum f)^2/4] + (3/4)[4 sum R^2 - (sum R)^2]"] = (
        sp.expand(2 * sum(x ** 2 for x in R) + sum(x ** 2 for x in F) - rhs2 - cert) == 0)
    g = sp.symbols("g0:4")
    Eg = sum(g) / 4
    T = [Eg + sp.Rational(1, 3) * (gi - Eg) for gi in g]
    out["S4: S^2 + Q/2 == 18 ||T_(1/3) g||_2^2"] = sp.expand(sum(g) ** 2 + sum(gi ** 2 for gi in g) / 2 - 18 * sum(t ** 2 for t in T) / 4) == 0
    rho = sp.symbols("rho", positive=True)
    Tr = [Eg + rho * (gi - Eg) for gi in g]
    VarG = sum((gi - Eg) ** 2 for gi in g) / 4
    out["||T_rho g||_2^2 == (Eg)^2 + rho^2 Var g"] = sp.expand(sum(t ** 2 for t in Tr) / 4 - (Eg ** 2 + rho ** 2 * VarG)) == 0
    r = sp.symbols("r0:4", positive=True)
    p = sp.Rational(8, 7)
    normp = (sum((ri ** sp.Rational(7, 8)) ** p for ri in r) / 4) ** (1 / p)
    out["S5: ||r^(7/8)||_(8/7) == ((sum r)/4)^(7/8)"] = sp.simplify(normp - (sum(r) / 4) ** sp.Rational(7, 8)) == 0
    FU = (4 * sp.Rational(1, 4) ** sp.Rational(7, 8)) ** 2 + 4 * sp.Rational(1, 4) ** sp.Rational(7, 4) / 2
    out["F(U) == 9/(4 sqrt2) == 18 * 4^(-7/4) and 4 F(U) == E(J)"] = (
        sp.simplify(FU - 9 / (4 * sp.sqrt(2))) == 0 and sp.simplify(18 * sp.Rational(1, 4) ** sp.Rational(7, 4) - FU) == 0
        and sp.simplify(4 * FU - EJ) == 0)
    out["kappa algebra: 18 (49/64)(1/4) == 441/128"] = sp.Rational(18) * sp.Rational(49, 64) / 4 == sp.Rational(441, 128)
    out["C_8 = 4 kappa/E(J) == (49 sqrt2/32)(a^2 - 1/9)"] = sp.simplify(4 * sp.Rational(441, 128) / EJ - 49 * sp.sqrt(2) / 32) == 0
    b, th = sp.symbols("b theta", positive=True)
    ex = -b * sp.log(b) + b * th
    bs = sp.solve(sp.diff(ex, b), b)[0]
    out["S6: max_{b>0} (-b ln b + b theta) == e^(theta-1) (concave)"] = (
        sp.simplify(bs - sp.exp(th - 1)) == 0 and sp.simplify(ex.subs(b, bs) - sp.exp(th - 1)) == 0
        and sp.simplify(sp.diff(ex, b, 2) + 1 / b) == 0)
    partial = sum(Fr(2 ** j, factorial(j)) for j in range(6))
    out["exact: sum_{j<=5} 2^j/j! == 109/15 = 7 + 4/15 > 7 (all omitted terms of e^2 positive)"] = partial == Fr(109, 15) and partial > 7
    out["arb: 7 < e^2"] = bool(arb(7) < arb(2).exp())
    alpha = (1 - sp.Rational(2, 4)) / sp.log(4 - 1)
    out["D-SC Thm A.1 at |X| = 4: alpha == 1/(2 ln 3) and 1/(4 alpha) == (ln 3)/2"] = (
        sp.simplify(alpha - 1 / (2 * sp.log(3))) == 0 and sp.simplify(1 / (4 * alpha) - sp.log(3) / 2) == 0)
    ln3, ln7 = arb(3).log(), arb(7).log()
    a2 = (-(ln3 * ln7)).exp()
    a = a2.sqrt()
    gap = a2 - arb(1) / 9
    kappa = arb(441) / 128 * gap
    C8 = 49 * arb(2).sqrt() / 32 * gap
    out["a = 7^(-ln3/2)"] = str(a)
    out["a^2 - 1/9"] = str(gap)
    out["kappa"] = str(kappa)
    out["C_8"] = str(C8)
    out["a > 1/3 (certain)"] = bool(a > arb(1) / 3)
    out["a^2 - 1/9 > 0 (certain)"] = bool(gap > 0)
    out["kappa in (0.0234, 0.0235) (certain)"] = bool(kappa > arb("0.0234")) and bool(kappa < arb("0.0235"))
    out["C_8 in (0.0147, 0.0148) (certain)"] = bool(C8 > arb("0.0147")) and bool(C8 < arb("0.0148"))
    out["B ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


# ---------------------------------------------------------------------------------------------------------- C
def G_and_Gp(fam, X, c):
    a78, a74 = arb(7) / 8, arb(7) / 4
    q = arb(1) / 4
    if fam == 1:
        Y = (1 - X) / 3
        S = X ** a78 + 3 * Y ** a78
        Sp = a78 * (X ** (a78 - 1) - Y ** (a78 - 1))
        Q = X ** a74 + 3 * Y ** a74
        Qp = a74 * (X ** (a74 - 1) - Y ** (a74 - 1))
        D = (X - q) ** 2 + 3 * (Y - q) ** 2
        Dp = 2 * (X - q) - 2 * (Y - q)
    else:
        Y = arb(1) / 2 - X
        S = 2 * X ** a78 + 2 * Y ** a78
        Sp = 2 * a78 * (X ** (a78 - 1) - Y ** (a78 - 1))
        Q = 2 * X ** a74 + 2 * Y ** a74
        Qp = 2 * a74 * (X ** (a74 - 1) - Y ** (a74 - 1))
        D = 2 * (X - q) ** 2 + 2 * (Y - q) ** 2
        Dp = 4 * (X - q) - 4 * (Y - q)
    return S * S + Q / 2 + c * D, 2 * S * Sp + Qp / 2 + c * Dp


def hpp(fam, X, c):
    a78, a74 = arb(7) / 8, arb(7) / 4
    if fam == 1:
        Y = (1 - X) / 3
        S = X ** a78 + 3 * Y ** a78
        Sp = a78 * X ** (a78 - 1) - a78 * Y ** (a78 - 1)
        Spp = a78 * (a78 - 1) * X ** (a78 - 2) + a78 * (a78 - 1) * Y ** (a78 - 2) / 3
        Qpp = a74 * (a74 - 1) * X ** (a74 - 2) + a74 * (a74 - 1) * Y ** (a74 - 2) / 3
        Dpp = arb(8) / 3
    else:
        Y = arb(1) / 2 - X
        S = 2 * X ** a78 + 2 * Y ** a78
        Sp = 2 * a78 * (X ** (a78 - 1) - Y ** (a78 - 1))
        Spp = 2 * a78 * (a78 - 1) * (X ** (a78 - 2) + Y ** (a78 - 2))
        Qpp = 2 * a74 * (a74 - 1) * (X ** (a74 - 2) + Y ** (a74 - 2))
        Dpp = arb(8)
    return 2 * Sp * Sp + 2 * S * Spp + Qpp / 2 + c * Dpp


def pw(x, e):
    return arb(0) if x == 0 else A_(x) ** e


def crude_upper(fam, lo, hi, c):
    """Monotone enclosure: x^(7/8), x^(7/4) increasing; y-part decreasing in x; dist^2 convex (max at an end)."""
    e78, e74 = arb(7) / 8, arb(7) / 4
    q = arb(1) / 4
    if fam == 1:
        yhi = (1 - lo) / 3
        S = pw(hi, e78) + 3 * pw(yhi, e78)
        Q = pw(hi, e74) + 3 * pw(yhi, e74)
        d1 = (A_(lo) - q) ** 2 + 3 * (A_((1 - lo) / 3) - q) ** 2
        d2 = (A_(hi) - q) ** 2 + 3 * (A_((1 - hi) / 3) - q) ** 2
    else:
        yhi = Fr(1, 2) - lo
        S = 2 * pw(hi, e78) + 2 * pw(yhi, e78)
        Q = 2 * pw(hi, e74) + 2 * pw(yhi, e74)
        d1 = 4 * (A_(lo) - q) ** 2
        d2 = 4 * (A_(hi) - q) ** 2
    dmax = ((d1 + d2 + abs(d1 - d2)) / 2).upper()
    return S * S + Q / 2 + c * dmax


def section_C():
    c = arb(1) / 40
    FU = 9 / (4 * arb(2).sqrt())
    eta = Fr(1, 25)
    out = {}
    for fam, lo0, hi0 in ((1, Fr(0), Fr(1)), (2, Fr(0), Fr(1, 2))):
        ok, worst, count, centred = True, None, 0, 0
        for a0, b0 in ((lo0, Fr(1, 4) - eta), (Fr(1, 4) + eta, hi0)):
            m = 4000
            for i in range(m):
                lo = a0 + (b0 - a0) * Fr(i, m)
                hi = a0 + (b0 - a0) * Fr(i + 1, m)
                slack = FU - crude_upper(fam, lo, hi, c)
                count += 1
                if not certain_pos(slack):
                    mid = (lo + hi) / 2
                    rad = float(hi - lo) / 2 * 1.000001 + 1e-30
                    Gm, _ = G_and_Gp(fam, A_(mid), c)
                    _, Gp = G_and_Gp(fam, A_(mid) + arb(0, rad), c)
                    slack = FU - (Gm + Gp * arb(0, rad))
                    centred += 1
                    if not certain_pos(slack):
                        ok = False
                v = float(slack.mid()) - float(slack.rad())
                if worst is None or v < worst[0]:
                    worst = (v, str(lo), str(hi))
        tok, tworst = True, None
        m = 400
        for i in range(m):
            lo = Fr(1, 4) - eta + 2 * eta * Fr(i, m)
            hi = Fr(1, 4) - eta + 2 * eta * Fr(i + 1, m)
            mid = (lo + hi) / 2
            rad = float(hi - lo) / 2 * 1.000001 + 1e-30
            v = hpp(fam, A_(mid) + arb(0, rad), c)
            if not bool(v < 0):
                tok = False
            fv = float(v.mid()) + float(v.rad())
            if tworst is None or fv > tworst:
                tworst = fv
        out[f"family {fam}"] = {
            "pieces": count, "pieces needing the centred form": centred,
            "G < F(U) certainly on every piece with |x - 1/4| >= 1/25": ok,
            "smallest certified slack (float display)": worst,
            "h'' < 0 certainly on 400 balls covering |x - 1/4| <= 1/25": tok,
            "largest h'' upper bound (float display)": tworst,
        }
    x = sp.symbols("x", positive=True)
    F1 = (x ** sp.Rational(7, 8) + 3 * ((1 - x) / 3) ** sp.Rational(7, 8)) ** 2 + (x ** sp.Rational(7, 4) + 3 * ((1 - x) / 3) ** sp.Rational(7, 4)) / 2
    F2 = (2 * x ** sp.Rational(7, 8) + 2 * (sp.Rational(1, 2) - x) ** sp.Rational(7, 8)) ** 2 + (2 * x ** sp.Rational(7, 4) + 2 * (sp.Rational(1, 2) - x) ** sp.Rational(7, 4)) / 2
    FUs = 9 / (4 * sp.sqrt(2))
    ex = {}
    for name, Fs in (("family 1", F1), ("family 2", F2)):
        ex[name] = (sp.simplify(Fs.subs(x, sp.Rational(1, 4)) - FUs) == 0 and sp.simplify(sp.diff(Fs, x).subs(x, sp.Rational(1, 4))) == 0)
    out["exact: F(1/4) == F(U) and F'(1/4) == 0 on both families"] = ex
    out["C ok"] = (all(out[f"family {f}"]["G < F(U) certainly on every piece with |x - 1/4| >= 1/25"] and
                       out[f"family {f}"]["h'' < 0 certainly on 400 balls covering |x - 1/4| <= 1/25"] for f in (1, 2))
                   and all(ex.values()))
    return out


# ---------------------------------------------------------------------------------------------------------- D
CELLS = [(p, q) for p in range(4) for q in range(4)]
PAIRS = [(i, j) for i in range(16) for j in range(i + 1, 16) if CELLS[i][0] != CELLS[j][0] and CELLS[i][1] != CELLS[j][1]]


def E_arb(M):
    mv = [M[p][q] for (p, q) in CELLS]
    e78 = arb(7) / 8
    tot = arb(0)
    for i, j in PAIRS:
        if mv[i] != 0 and mv[j] != 0:
            tot += (A_(mv[i]) * A_(mv[j])) ** e78
    return tot


def section_D():
    out = {}
    out["72 unordered allowed pairs"] = len(PAIRS) == 72
    l8 = arb(8).log()
    a9 = (-(arb(3).log() * l8) / 2).exp()
    out["d = 9: ln 8 > 2 (certain)"] = bool(l8 > 2)
    out["d = 9: 8^(-ln3/2) < 1/3 (certain): rho = 1/3 is outside the hypercontractive range for 9/8 -> 2"] = bool(a9 < arb(1) / 3)
    out["d = 9: entropy cancellation would need beta = 8/9, and 7/8 leaves a nonzero coefficient"] = Fr(9 - 1, 4) - Fr(9, 4) * Fr(7, 8) != 0
    Gm, _ = G_and_Gp(1, A_(Fr(19, 25)), arb(3) / 50)
    FU = 9 / (4 * arb(2).sqrt())
    out["mutation: c = 3/50 violates the row inequality at (19/25, 2/25, 2/25, 2/25) (certain)"] = certain_pos(Gm - FU)
    out["mutation value G - F(U) at c = 3/50"] = str(Gm - FU)
    g = sp.symbols("g0:4")
    Eg = sum(g) / 4
    T = [Eg + sp.Rational(1, 2) * (gi - Eg) for gi in g]
    out["mutation: S^2 + Q/2 == 18 ||T_(1/2) g||^2 is FALSE"] = sp.expand(sum(g) ** 2 + sum(gi ** 2 for gi in g) / 2 - 18 * sum(t ** 2 for t in T) / 4) != 0
    out["KPW relaxed: phi_8((J+I)/2) > phi_8(J) <=> 13^32 > 2^56 3^32 5^5"] = 13 ** 32 > 2 ** 56 * 3 ** 32 * 5 ** 5
    J = [[Fr(1, 4)] * 4 for _ in range(4)]
    EJ = E_arb(J)
    out["E(J) (arb) == 9/sqrt2"] = bool(abs(EJ - 9 / arb(2).sqrt()) < arb("1e-60"))
    a2 = (-(arb(3).log() * arb(7).log())).exp()
    C8 = 49 * arb(2).sqrt() / 32 * (a2 - arb(1) / 9)
    tests = {
        "(J+I)/2": [[Fr(5, 8) if p == q else Fr(1, 8) for q in range(4)] for p in range(4)],
        "M_{2/3}: rows (3/4,1/12,1/12,1/12)": [[Fr(3, 4) if p == q else Fr(1, 12) for q in range(4)] for p in range(4)],
        "I": [[Fr(1) if p == q else Fr(0) for q in range(4)] for p in range(4)],
        "J_2/2 (+) J_2/2": [[Fr(1, 2) if (p // 2 == q // 2) else Fr(0) for q in range(4)] for p in range(4)],
        "1 (+) J_3/3": [[(Fr(1) if p == q else Fr(0)) if (p == 0 or q == 0) else Fr(1, 3) for q in range(4)] for p in range(4)],
        "J + (1/100)(I - J)": [[Fr(1, 4) + Fr(1, 100) * ((1 if p == q else 0) - Fr(1, 4)) for q in range(4)] for p in range(4)],
    }
    res = {}
    allok = True
    for name, M in tests.items():
        assert all(sum(row) == 1 for row in M) and all(sum(M[p][q] for p in range(4)) == 1 for q in range(4))
        EM = E_arb(M)
        dist2 = sum((A_(M[p][q]) - A_(Fr(1, 4))) ** 2 for p in range(4) for q in range(4))
        dU = 4 * (EM / EJ).log()
        okv = bool(dU + C8 * dist2 < 0)
        allok &= okv
        res[name] = {"U(M) - U(J)": str(dU), "-C_8 |M-J|^2": str(-C8 * dist2), "U(M) - U(J) < -C_8 |M-J|^2 (certain)": okv}
    out["Theorem C at explicit rational doubly stochastic points (consistency, not proof)"] = res
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["D ok"] = all(bools) and allok
    return out


# ---------------------------------------------------------------------------------------------------------- E
def section_E():
    """Exact |T(I)|/|P_{n,8}| for n = 4t (diagonal cells hold t vertices = 8t points each; all 6 pairs of diagonal
    cells are allowed; (3.2)-(3.3) force b12 = b34 = x, b13 = b24 = y, b14 = b23 = z with x + y + z = 8t)."""
    out = {}
    U_I = 4 * arb(3).log() - 6 * arb(2).log()
    out["U(I) = -10 ln2 + 4 ln 6 = 4 ln3 - 6 ln2"] = str(U_I)
    rows = []
    bound_ok, mono_ok, prev = True, True, None
    for t in range(1, 31):
        n, D = 4 * t, 8 * t
        fD = factorial(D)
        N = 0
        for x in range(D + 1):
            fx = factorial(x)
            for y in range(D - x + 1):
                mult = fD // (fx * factorial(y) * factorial(D - x - y))
                N += mult * mult
        num = factorial(n) * fD * fD * N * factorial(16 * t) * 2 ** (16 * t)
        den = factorial(t) ** 4 * factorial(32 * t)
        rate = (arb(num).log() - arb(den).log()) / n
        gap = U_I - rate
        logP = (17 + 8 * arb(8 * n + 1).log() + arb(145) / 2 * arb(4 * n + 1).log()) / n
        bound_ok &= bool(rate <= U_I + logP)
        if prev is not None and t >= 5 and not bool(gap < prev):
            mono_ok = False
        prev = gap
        if t in (1, 2, 3, 5, 10, 20, 30):
            rows.append({"t": t, "n": n, "(1/n) ln(|T(I)|/|P|)": float(rate.mid()), "U(I) - rate": float(gap.mid()),
                         "n (U(I) - rate)/ln n": float((gap * n / arb(n).log()).mid())})
    out["table"] = rows
    out["rate <= U(I) + (1/n) ln P_8(n) for all t <= 30, P_8(n) = e^17 (8n+1)^8 (4n+1)^(145/2)"] = bound_ok
    out["gap U(I) - rate strictly decreasing for 5 <= t <= 30"] = mono_ok
    out["gap positive at t = 30"] = bool(prev > 0)
    out["E ok"] = bound_ok and mono_ok and bool(prev > 0)
    return out


# ---------------------------------------------------------------------------------------------------------- S
ADJ = np.array([[1.0 if (u[0] != v[0] and u[1] != v[1]) else 0.0 for v in CELLS] for u in CELLS])
JF = np.full((4, 4), 0.25)


def sinkhorn(M, it=500):
    for _ in range(it):
        M = M / M.sum(axis=1, keepdims=True)
        M = M / M.sum(axis=0, keepdims=True)
    return M


def psi_exact(m, d, tol=1e-13, maxit=200):
    """Exact inner optimum via the concave dual (float; Newton with backtracking)."""
    mv = m.reshape(-1)
    S = np.where(mv > 1e-15)[0]
    A = ADJ[np.ix_(S, S)]
    cc = d * mv[S]
    lam = np.log(np.sqrt(cc / np.maximum(A.sum(axis=1), 1e-300)))
    for _ in range(maxit):
        x = np.exp(lam)
        Ax = A @ x
        grad = cc - x * Ax
        if np.max(np.abs(grad)) < tol:
            break
        H = -(np.diag(x * Ax) + (x[:, None] * A * x[None, :]))
        step = np.linalg.solve(H, -grad)
        g0 = cc @ lam - 0.5 * x @ Ax
        t = 1.0
        while t > 1e-12:
            ln_ = lam + t * step
            xn = np.exp(ln_)
            if cc @ ln_ - 0.5 * xn @ (A @ xn) >= g0 - 1e-15:
                break
            t *= 0.5
        lam = lam + t * step
    ent = sum(v * math.log(v) for v in mv if v > 0)
    inner = float(np.sum(d * mv[S] * lam))
    return (1 - d / 2) * math.log(4) + (d / 2) * math.log(d) + (d - 1) / 4 * ent - inner / 4


def section_S():
    rng = np.random.default_rng(88)
    f = lambda z: np.clip(z, 0, None) ** 0.875
    EJ = 9 / math.sqrt(2)
    worst_ds, worst_rs, gap_min = -1e9, -1e9, 1e9
    for i in range(4000):
        M = sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(4, 4))))
        y = f(M.reshape(-1))
        Ev = 0.5 * y @ (ADJ @ y)
        worst_ds = max(worst_ds, (Ev - EJ) / np.sum((M - JF) ** 2))
        Rm = np.array([rng.dirichlet(np.ones(4) * rng.choice([0.1, 1, 4])) for _ in range(4)])
        y = f(Rm.reshape(-1))
        worst_rs = max(worst_rs, (0.5 * y @ (ADJ @ y) - EJ) / np.sum((Rm - JF) ** 2))
        if i < 300:
            gap_min = min(gap_min, -10 * math.log(2) + 4 * math.log(Ev) - psi_exact(M, 8))
    yJ = f(JF.reshape(-1))
    gJ = -10 * math.log(2) + 4 * math.log(0.5 * yJ @ (ADJ @ yJ)) - psi_exact(JF, 8)
    return {"note": "floats; NOT evidence",
            "max (E(M)-E(J))/|M-J|^2 over 4000 random DS / row-stochastic (Theorem C: <= -kappa = -0.02344)": [worst_ds, worst_rs],
            "min (U - Psi_8) over 300 random DS (weak duality: >= 0); value at J (= 0)": [gap_min, gJ]}


def main():
    out = {"note": "verifier for review/PROOF_CHI8.r1.md (lane random8reg-colour); exact/arb except section S"}
    out["A"] = section_A()
    out["B"] = section_B()
    out["C"] = section_C()
    out["D"] = section_D()
    out["E"] = section_E()
    out["S"] = section_S()
    out["all_required_true"] = bool(out["A"]["A ok"] and out["B"]["B ok"] and out["C"]["C ok"] and out["D"]["D ok"] and out["E"]["E ok"])
    path = os.path.join(HERE, "..", "evidence", "verify_chi8.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
