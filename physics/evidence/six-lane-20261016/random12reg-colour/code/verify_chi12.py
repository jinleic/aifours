"""Verifier for review/PROOF_CHI12.r1.md (chi(G_{n,12}) = 5 a.a.s.), lane random12reg-colour.

General-k code. Main case (k, d) = (5, 12). Controls: (k, d) = (4, 8) must reproduce the constants of the accepted
chi8 proof; (k, d) = (5, 13) must fail the route's hypercontractive condition (nothing is claimed at d = 13).
Exact rationals, big integers, sympy and python-flint arb (256 bits). Self-contained: reads nothing from other lanes.

Sections (keys of ../evidence/verify_chi12.json):
  A  arith(k, d): KPW / SSC / residue / lower-bound arithmetic, Lemma 6(a) eigenvalues, Lemma 8 constants, Lemma 9,
     S_1 Hessian H (exact eigenvalues and determinant), Proposition 2 constants, polynomial factor and S_2/S_1 degree.
  B  Lemma A, Proposition B and Theorem C identities (sympy) at k = 5; hypercontractive condition by exact rationals;
     constants a, a^2 - rho^2, kappa, E(J), C (arb).
  C  Supplementary interval check of the k = 5 row inequality with c_row = 1/40 (not needed for Theorem C).
  D  Controls: (4, 8) reproduces chi8's constants and counts; (5, 13) fails the condition; B (x) B not PSD at k = 5;
     GSVY identification U = Phi_1^{B(x)B}(M^beta) (general d, k).
  E  Exact-count control at M = I (the first moment E Y) for k = 5, n = 5t, t <= 20; k = 4 cross-check against chi8.
  F  Theorem C at explicit rational doubly stochastic 5x5 matrices (consistency, not proof).
  G  Self-contained first moment for proper 4-colourings of P_{n,12} (weak duality) plus an exact control, n <= 10.
  S  Float sanity (NOT evidence): decay ratios; weak duality U >= Psi_12 on random doubly stochastic matrices.
Run (from code/): OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B verify_chi12.py
"""
import json
import math
import os
from fractions import Fraction as Fr
from math import comb, factorial

import numpy as np
import sympy as sp
from flint import arb, ctx

ctx.prec = 256
HERE = os.path.dirname(os.path.abspath(__file__))
CHI8_KAPPA = "0.0234376440031617555786917914263469857546398238268746954546660373722778008724"
CHI8_C8 = "0.0147314817863750198010094808542165963469314119713589933613203967483337785331"
CHI8_RATE_N120 = 0.18083321333111818          # chi8 verify_chi8.json section E, t = 30 (floats display)


def A_(x):
    if isinstance(x, Fr):
        return arb(x.numerator) / arb(x.denominator)
    return arb(x)


def dfact(m):
    """(m)!! for odd m >= -1 (m = -1 gives 1)."""
    r = 1
    while m > 1:
        r *= m
        m -= 2
    return r


def cells(k):
    return [(p, q) for p in range(k) for q in range(k)]


def allowed(u, v):
    return u[0] != v[0] and u[1] != v[1]


def eig_check(Mat, claimed):
    """Exact check that a symmetric rational matrix has exactly the claimed eigenvalues with multiplicities."""
    n = Mat.shape[0]
    if sum(claimed.values()) != n:
        return False
    for lam, mult in claimed.items():
        if n - (Mat - lam * sp.eye(n)).rank() != mult:
            return False
    return True


def exp_partial_lower(x, target):
    """Smallest N with sum_{j<N} x^j/j! > target (exact; all omitted terms positive). Returns (N, partial sum)."""
    s, N = Fr(0), 0
    while s <= target:
        s += Fr(x ** N, factorial(N))
        N += 1
    return N, s


def exp_upper(x, N):
    """Exact rational upper bound for e^x (x > 0 integer): partial sum to N-1 plus geometric tail bound (N + 1 > x)."""
    assert N + 1 > x
    s = sum(Fr(x ** j, factorial(j)) for j in range(N))
    term = Fr(x ** N, factorial(N))
    return s + term / (1 - Fr(x, N + 1))


# ---------------------------------------------------------------------------------------------------------- A
def arith(k, d):
    out = {}
    H1 = k * k - 2 * k - d + 2
    out["(H1) k^2 - 2k - d + 2"] = H1
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
    out["delta_1 = -1 and |delta_i| <= 1/(k-1) for 2 <= i < 60"] = all(
        abs(Fr((-1) ** i, (k - 1) ** (i - 1))) <= Fr(1, k - 1) for i in range(2, 60))
    m = sp.symbols("m", integer=True, positive=True)
    lam = sp.Integer(d - 1) ** m / (2 * m)
    dl = (-1) ** m / sp.Integer(k - 1) ** (m - 1)
    target = sp.Rational((k - 1) ** 2, 2) * sp.Rational(d - 1, (k - 1) ** 2) ** m / m
    out["lambda_m delta_m^2 == ((k-1)^2/2) ((d-1)/(k-1)^2)^m / m"] = sp.simplify(lam * dl ** 2 - target) == 0
    ssum = sp.Rational((k - 1) ** 2, 2) * sp.summation(sp.Rational(d - 1, (k - 1) ** 2) ** m / m, (m, 1, sp.oo))
    kpw12 = sp.Integer(k - 1) ** 2 * sp.log(sp.Integer(k - 1) / sp.sqrt(H1))
    out["sum lambda delta^2 (closed form)"] = str(sp.nsimplify(sp.simplify(ssum)))
    out["sum lambda delta^2 == KPW (1.2) (k-1)^2 log((k-1)/sqrt(H1))"] = sp.simplify(
        sp.expand_log(ssum - kpw12, force=True)) == 0
    pi = sp.pi
    C1 = sp.Integer(k) ** sp.Rational(k, 2) * (sp.Integer(k - 1) / (2 * pi * (k - 2))) ** sp.Rational(k - 1, 2)
    C2 = sp.Integer(k) ** k * sp.Integer(k - 1) ** (k * (k - 1)) / (
        sp.Integer(H1) ** sp.Rational((k - 1) ** 2, 2) * (2 * pi * (k - 2)) ** (k - 1))
    r13 = (sp.Integer(k - 1) / sp.sqrt(H1)) ** ((k - 1) ** 2)
    out["Prop 2: C2/C1^2 == ((k-1)/sqrt(H1))^((k-1)^2) == exp(sum lambda delta^2) (KPW (1.3))"] = (
        sp.simplify(C2 / C1 ** 2 - r13) == 0 and sp.simplify(sp.expand_log(sp.log(r13) - ssum, force=True)) == 0)
    out["Prop 2 constants C1, C2 (sympy)"] = [str(sp.simplify(C1)), str(sp.simplify(C2))]
    # KPW threshold arithmetic: KPW's k at this d (smallest K with d < 2(K-1) log(K-1))
    Kk = None
    for K in range(3, 30):
        val = 2 * (K - 1) * arb(K - 1).log()
        if bool(arb(d) < val):
            Kk = K
            break
        assert bool(arb(d) > val), "undecided comparison"
    out["KPW's k at this d (smallest K with d < 2(K-1)log(K-1))"] = Kk
    out["KPW window {K-1, K}"] = [Kk - 1, Kk]
    out["KPW exact-value clause d > (2K-3) log(K-1) fails"] = bool(arb(d) < (2 * Kk - 3) * arb(Kk - 1).log())
    q = k - 1
    mr = Fr(q) * Fr(q - 1, q) ** (d // 2)
    out["Molloy-Reed at q = k-1: q(1-1/q)^(d/2)"] = str(mr)
    out["Molloy-Reed < 1 (chi > k-1)"] = mr < 1
    out["KPW weak form (2q-1) log q < d at q = k-1"] = bool((2 * q - 1) * arb(q).log() < d)
    # residues
    kprime = 2 * k if (d * k) % 2 else k
    res = [r for r in range(1, kprime) if (d * r) % 2 == 0]
    out["k' (2k if dk odd, else k)"] = kprime
    out["residues r (0 < r < k', dr even)"] = res
    out["l = dr/2"] = [d * r // 2 for r in res]
    out["preimage counts multinomial(dr; d, ..., d)"] = {str(r): factorial(d * r) // factorial(d) ** r for r in res}
    out["choices (dr-1)!! (dr/2)! of (eta, order) per G"] = {str(r): dfact(d * r - 1) * factorial(d * r // 2) for r in res}
    # Lemma 9 and Lemma 6(a)
    out["Lemma 9: 2(k-1)^2 > k^2"] = 2 * (k - 1) ** 2 > k * k
    out["Lemma 9 values [2(k-1)^2, k^2]"] = [2 * (k - 1) ** 2, k * k]
    Jk = sp.ones(k, k)
    L6 = sp.kronecker_product(Jk - sp.eye(k), Jk - sp.eye(k)) + (k - 1) ** 2 * sp.eye(k * k)
    claimed6 = {sp.Integer(k * k - 2 * k + 2): (k - 1) ** 2, sp.Integer((k - 1) * (k - 2)): 2 * (k - 1),
                sp.Integer(2 * (k - 1) ** 2): 1}
    out["Lemma 6(a) eigenvalues {k^2-2k+2: (k-1)^2, (k-1)(k-2): 2(k-1), 2(k-1)^2: 1} (exact rank check)"] = eig_check(L6, claimed6)
    out["Lemma 6(a) eigenvalue values"] = {str(kk): vv for kk, vv in claimed6.items()}
    # Lemma 8 constants
    dd, kk, eps = sp.symbols("d k epsilon", positive=True)
    coef = dd * kk ** 2 * (kk - 1) ** 4 / (2 * (kk ** 2 - 2 * kk + 2))      # eps' <= coef * eps^2
    bound = dd / (16 * kk ** 2 * (kk - 1) ** 2)                            # need eps' < bound
    cond = sp.simplify(bound / coef)
    out["Lemma 8: eps'-condition eps^2 < bound/coef is free of d"] = (sp.diff(cond, dd) == 0)
    out["Lemma 8: eps^2 < (k^2-2k+2)/(8 k^4 (k-1)^6) (general form)"] = sp.simplify(
        cond - (kk ** 2 - 2 * kk + 2) / (8 * kk ** 4 * (kk - 1) ** 6)) == 0
    out["Lemma 8 at (k,d): c_KPW = d/(2k^2(k-1)^2)"] = str(Fr(d, 2 * k * k * (k - 1) ** 2))
    out["Lemma 8 at (k,d): eps' coefficient, bound, eps^2 threshold"] = [
        str(Fr(d * k * k * (k - 1) ** 4, 2 * (k * k - 2 * k + 2))), str(Fr(d, 16 * k * k * (k - 1) ** 2)),
        str(Fr(k * k - 2 * k + 2, 8 * k ** 4 * (k - 1) ** 6))]
    # S_1 Hessian
    cH = sp.Rational(H1, k * k - 2 * k + 2)
    Ak = sp.ones(k - 1, k - 1) + sp.eye(k - 1)
    H = cH * sp.kronecker_product(Ak, Ak)
    claimedH = {cH * k * k: 1, cH * k: 2 * (k - 2), cH: (k - 2) ** 2}
    out["S_1 Hessian H = (H1/(k^2-2k+2)) (J_{k-1}+I_{k-1})^(x)2: coefficient"] = str(cH)
    out["H eigenvalues {c k^2: 1, c k: 2(k-2), c: (k-2)^2} (exact rank check)"] = eig_check(H, claimedH)
    out["H eigenvalue values"] = {str(kk_): vv for kk_, vv in claimedH.items()}
    detH = H.det()
    out["det H"] = str(detH)
    out["det H == k^(2k-2) c^((k-1)^2) (KPW (3.13))"] = detH == sp.Integer(k) ** (2 * k - 2) * cH ** ((k - 1) ** 2)
    # polynomial factor and degree
    npairs = sum(1 for u in cells(k) for v in cells(k) if allowed(u, v)) // 2
    out["number of unordered allowed pairs"] = npairs
    out["unordered allowed pairs == k^2 (k-1)^2 / 2"] = npairs == k * k * (k - 1) ** 2 // 2
    eP = (k * k + 1, Fr(k * k, 2), Fr(k * k * (k - 1) ** 2 + 1, 2))
    out["P_d(n) = e^a (dn+1)^b (dn/2+1)^c with (a, b, c)"] = [str(x) for x in eP]
    deg = k * k + eP[1] + eP[2] + (k - 1)
    out["S_2/S_1 polynomial degree k^2 + b + c + (k-1)"] = str(deg)
    out["first-moment exponent log k + (d/2) log(1-1/k)"] = str(arb(k).log() + A_(Fr(d, 2)) * (arb(k - 1).log() - arb(k).log()))
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["A ok"] = all(bools)
    return out


# ---------------------------------------------------------------------------------------------------------- B
def constants(k, d):
    """Route constants in arb: alpha, a, rho, a^2 - rho^2, kappa, E(J), F(u*), C; plus exact admissibility data."""
    out = {}
    beta = Fr(d - 1, d)
    rho = Fr(1, k - 1)
    lk1, ld1 = arb(k - 1).log(), arb(d - 1).log()
    alpha = (1 - arb(2) / k) / lk1
    a = (-(ld1 / (4 * alpha))).exp()
    gap = a * a - A_(rho) ** 2
    kappa = A_(Fr((k - 1) ** 2, 2) * beta * beta) * gap
    E0 = A_(Fr(k * k * (k - 1) ** 2, 2)) * (-(2 * A_(beta)) * arb(k).log()).exp()
    FU = E0 / k
    C = A_(Fr(d, 2)) * kappa / E0
    out["beta"] = str(beta)
    out["rho = 1/(k-1)"] = str(rho)
    out["alpha (D-SC A.1) = (1 - 2/k)/log(k-1)"] = str(alpha)
    out["a = (d-1)^(-1/(4 alpha))"] = str(a)
    out["a^2 - rho^2"] = str(gap)
    out["kappa = ((k-1)^2/2) beta^2 (a^2 - rho^2)"] = str(kappa)
    out["kappa coefficient ((k-1)^2/2) beta^2"] = str(Fr((k - 1) ** 2, 2) * beta * beta)
    out["E(J) = (k^2(k-1)^2/2) k^(-2 beta)"] = str(E0)
    out["F(u*) = E(J)/k"] = str(FU)
    out["C = (d/2) kappa / E(J)"] = str(C)
    out["margin (4 - 8/k) - log(d-1)"] = str(4 - arb(8) / k - ld1)
    out["admissible: rho < a (certain)"] = bool(A_(rho) < a)
    out["a^2 - rho^2 > 0 (certain)"] = bool(gap > 0)
    out["C > 0 (certain)"] = bool(C > 0)
    out["_arb"] = {"a": a, "kappa": kappa, "E0": E0, "C": C, "gap": gap}
    return out


def section_B():
    k, d = 5, 12
    out = {}
    beta = sp.Rational(d - 1, d)
    out["entropy cancellation (d-1)/k == (d/k) beta"] = sp.Rational(d - 1, k) == sp.Rational(d, k) * beta
    # Lemma A exponent algebra at k = 5 (25 cell variables, sum m = 5)
    ms = sp.symbols("m0:25", positive=True)
    dS = sp.Integer(d)
    Hk = -sum(mm / k * sp.log(mm / k) for mm in ms)
    T2 = sum(dS * mm / k * sp.log(dS * mm / k) for mm in ms)
    lhs = Hk + T2 - dS / 2 * sp.log(dS)
    rhs = (dS - 1) / k * sum(mm * sp.log(mm) for mm in ms) + (1 - dS) * sp.log(k) + dS / 2 * sp.log(dS)
    diff = sp.expand(sp.expand_log(lhs - rhs, force=True))
    diff = sp.expand(sp.expand_log(diff.subs(ms[24], k - sum(ms[:24])), force=True))
    out["Lemma A exponent at k = 5: H_5 + sum (dm/5) log(dm/5) - (d/2) log d == ((d-1)/5) sum m log m + (1-d) log 5 + (d/2) log d"] = (
        sp.simplify(diff) == 0)
    # Proposition B (general d, k): min over w = e^{2c_0 - 1} > 0
    E_, w, dd, kk = sp.symbols("E w d k", positive=True)
    V = (1 - dd) * sp.log(kk) + dd / 2 * sp.log(dd) + w * E_ - dd / 2 * (1 + sp.log(w))
    wst = sp.solve(sp.diff(V, w), w)
    out["Prop B (general d, k): argmin w = d/(2E); min = (1-d) log k + (d/2) log(2E); strictly convex"] = (
        len(wst) == 1 and sp.simplify(wst[0] - dd / (2 * E_)) == 0
        and sp.simplify(sp.expand_log(V.subs(w, wst[0]) - ((1 - dd) * sp.log(kk) + dd / 2 * sp.log(2 * E_)), force=True)) == 0
        and sp.simplify(sp.diff(V, w, 2) - dd / (2 * w ** 2)) == 0)
    c0 = sp.symbols("c_0", real=True)
    lin = sp.Rational(d, k) * (c0 * k + beta * sp.Symbol("G"))     # (d/k) sum mu m with sum m = k, G = sum m log m
    out["(d/k) sum mu_u m_u == d c_0 + ((d-1)/k) sum m log m for mu = c_0 + beta log m"] = sp.simplify(
        lin - (d * c0 + sp.Rational(d - 1, k) * sp.Symbol("G"))) == 0
    EJ = sp.Rational(k * k * (k - 1) ** 2, 2) * sp.Integer(k) ** (-2 * beta)
    out["E(J) == 200 * 5^(-11/6)"] = sp.simplify(EJ - 200 * sp.Integer(5) ** sp.Rational(-11, 6)) == 0
    UJ = (1 - d) * sp.log(k) + sp.Rational(d, 2) * sp.log(2 * EJ)
    out["U(J) == (2-d) log k + d log(k-1) == 24 log 2 - 10 log 5 (exponent of (EY)^2)"] = (
        sp.simplify(sp.expand_log(UJ - ((2 - d) * sp.log(k) + d * sp.log(k - 1)), force=True)) == 0
        and sp.simplify(sp.expand_log(UJ - (24 * sp.log(2) - 10 * sp.log(5)), force=True)) == 0)
    EI = sp.Rational(k * (k - 1), 2)
    UI = (1 - d) * sp.log(k) + sp.Rational(d, 2) * sp.log(2 * EI)
    out["U(I) == log 5 + 6 log(4/5) == 12 log 2 - 5 log 5 (exponent of EY)"] = sp.simplify(
        sp.expand_log(UI - (sp.log(5) + 6 * sp.log(sp.Rational(4, 5))), force=True)) == 0
    # generic doubly stochastic 5x5: sum over allowed unordered pairs of m_u m_v == (k^2 - 2k + ||M||^2)/2
    aa = sp.symbols("a0:16")
    Mds = sp.zeros(k, k)
    for i in range(k - 1):
        for j in range(k - 1):
            Mds[i, j] = aa[i * (k - 1) + j]
        Mds[i, k - 1] = 1 - sum(Mds[i, j] for j in range(k - 1))
    for j in range(k):
        Mds[k - 1, j] = 1 - sum(Mds[i, j] for i in range(k - 1))
    cl = cells(k)
    Eds = sum(Mds[u] * Mds[v] for u in cl for v in cl if allowed(u, v)) / 2
    out["generic DS 5x5: sum_{allowed unordered} m_u m_v == (15 + ||M||^2)/2 (so E(M) >= 8 on DS M)"] = (
        sp.expand(Eds - (k * k - 2 * k + sum(Mds[u] ** 2 for u in cl)) / 2) == 0)
    # row reduction at k = 5 (generic non-negative array)
    F = sp.Matrix(k, k, lambda i, j: sp.Symbol(f"f{i}_{j}"))
    E2 = sum(F[u] * F[v] for u in cl for v in cl if allowed(u, v))
    tot = sum(F)
    R = [sum(F[p, :]) for p in range(k)]
    Cc = [sum(F[:, q]) for q in range(k)]
    ie = tot ** 2 - sum(x ** 2 for x in R) - sum(x ** 2 for x in Cc) + sum(x ** 2 for x in F)
    out["k = 5 inclusion-exclusion: 2E == (sum f)^2 - sum R^2 - sum C^2 + sum f^2"] = sp.expand(E2 - ie) == 0
    cert = (sum(x ** 2 for x in Cc) - tot ** 2 / k) + sp.Rational(k - 1, k) * (k * sum(x ** 2 for x in R) - sum(R) ** 2)
    out["k = 5 certificate: 3 sum R^2 + sum f^2 - 2E == [sum C^2 - (sum f)^2/5] + (4/5)[5 sum R^2 - (sum R)^2]"] = (
        sp.expand((k - 2) * sum(x ** 2 for x in R) + sum(x ** 2 for x in F) - ie - cert) == 0)
    # row function identity at k = 5
    g = sp.symbols("g0:5")
    Eg = sum(g) / k
    rho = sp.Rational(1, k - 1)
    T = [Eg + rho * (gi - Eg) for gi in g]
    F5 = sp.Rational(k - 2, 2) * sum(g) ** 2 + sum(gi ** 2 for gi in g) / 2
    out["F_5 = (3/2) S^2 + Q/2 == 40 ||T_(1/4) g||_2^2"] = sp.expand(F5 - 40 * sum(t ** 2 for t in T) / k) == 0
    rr = sp.symbols("rho", positive=True)
    Tr = [Eg + rr * (gi - Eg) for gi in g]
    VarG = sum((gi - Eg) ** 2 for gi in g) / k
    out["||T_rho g||_2^2 == (Eg)^2 + rho^2 Var g (k = 5)"] = sp.expand(sum(t ** 2 for t in Tr) / k - (Eg ** 2 + rr ** 2 * VarG)) == 0
    out["Var g == (1/(2k^2)) sum_{i,j} (g_i - g_j)^2 (k = 5)"] = sp.expand(
        VarG - sum((gi - gj) ** 2 for gi in g for gj in g) / (2 * k * k)) == 0
    r = sp.symbols("r0:5", positive=True)
    p = 1 / beta
    normp = (sum((ri ** beta) ** p for ri in r) / k) ** (1 / p)
    out["||r^(11/12)||_(12/11) == ((sum r)/5)^(11/12)"] = sp.simplify(normp - (sum(r) / k) ** beta) == 0
    FU = sp.Rational(k - 2, 2) * (k * sp.Integer(k) ** (-beta)) ** 2 + k * sp.Integer(k) ** (-2 * beta) / 2
    out["F(u*) == 8 * 5^(-5/6) == 40 * 5^(-11/6) and 5 F(u*) == E(J)"] = (
        sp.simplify(FU - 8 * sp.Integer(5) ** sp.Rational(-5, 6)) == 0
        and sp.simplify(FU - 40 * sp.Integer(5) ** sp.Rational(-11, 6)) == 0 and sp.simplify(k * FU - EJ) == 0)
    out["kappa algebra: 40 * (121/144) / 5 == 121/18"] = sp.Rational(40) * beta ** 2 / k == sp.Rational(121, 18)
    out["note: C_12"] = "C_12 = (d/2) kappa / E(J) = 6 kappa / E(J); E(M) >= (15 + ||M||^2)/2 >= 8 > 0 on DS M"
    alpha = (1 - sp.Rational(2, k)) / sp.log(k - 1)
    out["D-SC Thm A.1 at |X| = 5: alpha == 3/(5 log 4); 1/(4 alpha) == 5 log 4/12"] = (
        sp.simplify(alpha - 3 / (5 * sp.log(4))) == 0 and sp.simplify(1 / (4 * alpha) - 5 * sp.log(4) / 12) == 0)
    out["4 alpha log(k-1) == 4 - 8/k == 12/5"] = sp.simplify(4 * alpha * sp.log(k - 1) - sp.Rational(12, 5)) == 0
    # exact rational proof of 11^5 < e^12 (equivalently log 11 < 12/5, i.e. rho = 1/4 < a)
    N, s = exp_partial_lower(12, 11 ** 5)
    out["exact: smallest N with sum_{j<N} 12^j/j! > 11^5 = 161051"] = N
    out["exact: sum_{j<22} 12^j/j! > 161051 (all omitted terms positive, so e^12 > 11^5)"] = (
        sum(Fr(12 ** j, factorial(j)) for j in range(22)) > 11 ** 5)
    out["exact partial sum value (float display)"] = float(s)
    out["arb: 11 < e^(12/5)"] = bool(arb(11) < (arb(12) / 5).exp())
    cs = constants(k, d)
    for key, val in cs.items():
        if key != "_arb":
            out[key] = val
    arbs = cs["_arb"]
    out["a > 1/4 (certain)"] = bool(arbs["a"] > arb(1) / 4)
    out["a in (0.2503, 0.2504) (certain)"] = bool(arbs["a"] > arb("0.2503")) and bool(arbs["a"] < arb("0.2504"))
    out["kappa in (1.0228e-3, 1.0229e-3) (certain)"] = bool(arbs["kappa"] > arb("0.0010228")) and bool(arbs["kappa"] < arb("0.0010229"))
    out["C_12 in (5.866e-4, 5.867e-4) (certain)"] = bool(arbs["C"] > arb("0.0005866")) and bool(arbs["C"] < arb("0.0005867"))
    out["E(J) arb == 200 * 5^(-11/6)"] = bool(abs(arbs["E0"] - 200 * (-(arb(11) / 6) * arb(5).log()).exp()) < arb("1e-60"))
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["B ok"] = all(bools)
    return out


# ---------------------------------------------------------------------------------------------------------- C
K5, BETA5 = 5, arb(11) / 12


def fam_vals(m, X, c):
    """Family m: r = (x * m copies, y * (5-m) copies), y = (1 - m x)/(5 - m). Returns G, G', G'' in arb on ball X."""
    k, b = K5, BETA5
    km = k - m
    Y = (1 - m * X) / km
    q = arb(1) / k
    S = m * X ** b + km * Y ** b
    Sp = m * b * (X ** (b - 1) - Y ** (b - 1))
    Spp = m * b * (b - 1) * (X ** (b - 2) + (arb(m) / km) * Y ** (b - 2))
    Q = m * X ** (2 * b) + km * Y ** (2 * b)
    Qp = 2 * m * b * (X ** (2 * b - 1) - Y ** (2 * b - 1))
    Qpp = 2 * m * b * (2 * b - 1) * (X ** (2 * b - 2) + (arb(m) / km) * Y ** (2 * b - 2))
    D = m * (X - q) ** 2 + km * (Y - q) ** 2
    Dp = 2 * m * (X - Y)
    Dpp = arb(2 * m * k) / km
    F = arb(k - 2) / 2 * S * S + Q / 2
    Fp = (k - 2) * S * Sp + Qp / 2
    Fpp = (k - 2) * (Sp * Sp + S * Spp) + Qpp / 2
    return F + c * D, Fp + c * Dp, Fpp + c * Dpp


def pw(x, e):
    return arb(0) if x == 0 else A_(x) ** e


def crude_upper(m, lo, hi, c):
    k, b = K5, BETA5
    km = k - m
    yhi = (1 - m * lo) / km
    S = m * pw(hi, b) + km * pw(yhi, b)
    Q = m * pw(hi, 2 * b) + km * pw(yhi, 2 * b)
    q = arb(1) / k
    d1 = m * (A_(lo) - q) ** 2 + km * (A_((1 - m * lo) / km) - q) ** 2
    d2 = m * (A_(hi) - q) ** 2 + km * (A_((1 - m * hi) / km) - q) ** 2
    dmax = ((d1 + d2 + abs(d1 - d2)) / 2).upper()
    return arb(k - 2) / 2 * S * S + Q / 2 + c * dmax


def section_C():
    c = arb(1) / 40
    FU = 8 * (-(arb(5) / 6) * arb(5).log()).exp()
    eta = Fr(1, 25)
    out = {"c_row": "1/40", "cut": "|x - 1/5| < 1/25 handled by the Taylor neighbourhood"}
    allok = True
    for m, hi0 in ((1, Fr(1)), (2, Fr(1, 2))):
        ok, worst, centred = True, None, 0
        for a0, b0 in ((Fr(0), Fr(1, 5) - eta), (Fr(1, 5) + eta, hi0)):
            npc = 4000
            for i in range(npc):
                lo = a0 + (b0 - a0) * Fr(i, npc)
                hi = a0 + (b0 - a0) * Fr(i + 1, npc)
                slack = FU - crude_upper(m, lo, hi, c)
                if not bool(slack > 0):
                    mid = (lo + hi) / 2
                    rad = float(hi - lo) / 2 * 1.000001 + 1e-30
                    Gm, _, _ = fam_vals(m, A_(mid), c)
                    _, Gp, _ = fam_vals(m, A_(mid) + arb(0, rad), c)
                    slack = FU - (Gm + Gp * arb(0, rad))
                    centred += 1
                    if not bool(slack > 0):
                        ok = False
                v = float(slack.mid()) - float(slack.rad())
                if worst is None or v < worst[0]:
                    worst = (v, str(lo), str(hi))
        tok, tworst = True, None
        nb = 400
        for i in range(nb):
            lo = Fr(1, 5) - eta + 2 * eta * Fr(i, nb)
            hi = Fr(1, 5) - eta + 2 * eta * Fr(i + 1, nb)
            mid = (lo + hi) / 2
            rad = float(hi - lo) / 2 * 1.000001 + 1e-30
            _, _, Gpp = fam_vals(m, A_(mid) + arb(0, rad), c)
            if not bool(Gpp < 0):
                tok = False
            fv = float(Gpp.mid()) + float(Gpp.rad())
            if tworst is None or fv > tworst:
                tworst = fv
        out[f"family m = {m}"] = {"pieces": 8000, "pieces needing the centred form": centred,
                                  "G < F(u*) certainly on every piece with |x - 1/5| >= 1/25": ok,
                                  "smallest certified slack (float display)": worst,
                                  "G'' < 0 certainly on 400 balls covering |x - 1/5| <= 1/25": tok,
                                  "largest G'' upper bound (float display)": tworst}
        allok &= ok and tok
    x = sp.symbols("x", positive=True)
    b = sp.Rational(11, 12)
    FUs = 8 * sp.Integer(5) ** sp.Rational(-5, 6)
    exact = {}
    for m in (1, 2):
        y = (1 - m * x) / (5 - m)
        Fx = sp.Rational(3, 2) * (m * x ** b + (5 - m) * y ** b) ** 2 + (m * x ** (2 * b) + (5 - m) * y ** (2 * b)) / 2
        exact[f"m = {m}"] = (sp.simplify(Fx.subs(x, sp.Rational(1, 5)) - FUs) == 0
                             and sp.simplify(sp.diff(Fx, x).subs(x, sp.Rational(1, 5))) == 0)
    out["exact: F(1/5) == F(u*) and F'(1/5) == 0 on both families (distance term: value and slope 0)"] = exact
    # two-value lemma: t^{13/12} psi'(t) = -(11/48) S + (55/72) t^{11/12} + 2 c t^{13/12} (strictly increasing in t)
    t, S, cc = sp.symbols("t S c", positive=True)
    psi = sp.Rational(11, 4) * S * t ** sp.Rational(-1, 12) + sp.Rational(11, 12) * t ** sp.Rational(5, 6) + 2 * cc * t
    expr = sp.simplify(t ** sp.Rational(13, 12) * sp.diff(psi, t))
    out["two-value lemma: t^(13/12) psi'(t) == -(11/48) S + (55/72) t^(11/12) + 2 c t^(13/12)"] = sp.simplify(
        expr - (-sp.Rational(11, 48) * S + sp.Rational(55, 72) * t ** sp.Rational(11, 12) + 2 * cc * t ** sp.Rational(13, 12))) == 0
    out["psi is dG/dr_j + c_row (2/5): dG/dr_j == (3/2)*2S*(11/12) r^(-1/12) + (1/2)(11/6) r^(5/6) + 2c(r - 1/5)"] = True if sp.simplify(
        sp.Rational(3, 2) * 2 * S * b * t ** (b - 1) + sp.Rational(1, 2) * 2 * b * t ** (2 * b - 1) + 2 * cc * (t - sp.Rational(1, 5))
        - (psi - 2 * cc * sp.Rational(1, 5))) == 0 else False
    # arb point values of the slack F(u*) - G(r(x)) (certified piece slacks above are lower bounds)
    pts = {}
    for m, xs in ((1, (Fr(4, 25), Fr(6, 25), Fr(257, 1000), Fr(804, 1000))), (2, (Fr(4, 25), Fr(6, 25), Fr(3, 10)))):
        for xv in xs:
            Gv, _, _ = fam_vals(m, A_(xv), c)
            sl = FU - Gv
            pts[f"family m = {m}, x = {xv}"] = {"slack F(u*) - G": str(sl), "slack > 0 (certain)": bool(sl > 0)}
    out["point values of the slack (arb)"] = pts
    out["all point slacks positive (certain)"] = all(v["slack > 0 (certain)"] for v in pts.values())
    out["C ok"] = allok and all(exact.values()) and out["two-value lemma: t^(13/12) psi'(t) == -(11/48) S + (55/72) t^(11/12) + 2 c t^(13/12)"] \
        and out["psi is dG/dr_j + c_row (2/5): dG/dr_j == (3/2)*2S*(11/12) r^(-1/12) + (1/2)(11/6) r^(5/6) + 2c(r - 1/5)"] \
        and out["all point slacks positive (certain)"]
    return out


# ---------------------------------------------------------------------------------------------------------- D
def section_D():
    out = {}
    # (4, 8) control: same general code must reproduce chi8
    c48 = constants(4, 8)
    arb48 = c48["_arb"]
    out["(4,8) kappa equals chi8 kappa (|diff| < 1e-70)"] = bool(abs(arb48["kappa"] - arb(CHI8_KAPPA)) < arb("1e-70"))
    out["(4,8) C equals chi8 C_8 (|diff| < 1e-70)"] = bool(abs(arb48["C"] - arb(CHI8_C8)) < arb("1e-70"))
    out["(4,8) E(J) == 9/sqrt2"] = bool(abs(arb48["E0"] - 9 / arb(2).sqrt()) < arb("1e-70"))
    out["(4,8) a == 7^(-log 3/2)"] = bool(abs(arb48["a"] - (-(arb(3).log() * arb(7).log()) / 2).exp()) < arb("1e-70"))
    out["(4,8) kappa coefficient 441/128"] = c48["kappa coefficient ((k-1)^2/2) beta^2"] == "441/128"
    a48 = arith(4, 8)
    out["(4,8) arith: (H1) 2, ratio 7/9, growth 81/64, Molloy-Reed 16/27"] = (
        a48["(H1) k^2 - 2k - d + 2"] == 2 and a48["series ratio (d-1)/(k-1)^2"] == "7/9"
        and a48["EY growth k(1-1/k)^(d/2)"] == "81/64" and a48["Molloy-Reed at q = k-1: q(1-1/q)^(d/2)"] == "16/27")
    out["(4,8) arith: residues 1,2,3 with counts 1, 12870, 9465511770"] = (
        a48["residues r (0 < r < k', dr even)"] == [1, 2, 3]
        and a48["preimage counts multinomial(dr; d, ..., d)"] == {"1": 1, "2": 12870, "3": 9465511770})
    out["(4,8) arith: H eigenvalues 16/5, 4/5, 1/5 and det 4^6 5^-9"] = (
        a48["H eigenvalues {c k^2: 1, c k: 2(k-2), c: (k-2)^2} (exact rank check)"]
        and a48["det H"] == str(sp.Integer(4) ** 6 * sp.Rational(1, 5) ** 9))
    out["(4,8) arith: P exponents (17, 8, 145/2) and degree 199/2"] = (
        a48["P_d(n) = e^a (dn+1)^b (dn/2+1)^c with (a, b, c)"] == ["17", "8", "145/2"]
        and a48["S_2/S_1 polynomial degree k^2 + b + c + (k-1)"] == "199/2")
    out["(4,8) arith A ok"] = a48["A ok"]
    N8, _ = exp_partial_lower(8, 7 ** 4)
    out["(4,8) exact: e^8 > 7^4 (partial sum, smallest N)"] = N8
    out["(4,8) exact (chi8 form): sum_{j<=5} 2^j/j! == 109/15 > 7"] = sum(Fr(2 ** j, factorial(j)) for j in range(6)) == Fr(109, 15)
    # (5, 13): condition fails
    ub = exp_upper(12, 40)
    out["(5,13) exact: e^12 < 12^5 = 248832 (partial sum to 39 + geometric tail)"] = ub < 12 ** 5
    out["(5,13) exact upper bound for e^12 (float display)"] = float(ub)
    c513 = constants(5, 13)
    out["(5,13) admissible rho < a ? (must be False)"] = c513["admissible: rho < a (certain)"]
    out["(5,13) a < 1/4 (certain)"] = bool(c513["_arb"]["a"] < arb(1) / 4)
    out["(5,13) margin (4 - 8/k) - log(d-1) (negative)"] = c513["margin (4 - 8/k) - log(d-1)"]
    # B (x) B not PSD at k = 5
    B = sp.ones(5, 5) - sp.eye(5)
    BB = sp.kronecker_product(B, B)
    out["B = J_5 - I_5 eigenvalues {4: 1, -1: 4} (exact rank check)"] = eig_check(B, {sp.Integer(4): 1, sp.Integer(-1): 4})
    out["B (x) B eigenvalues {16: 1, -4: 8, 1: 16}: not PSD (exact rank check)"] = eig_check(
        BB, {sp.Integer(16): 1, sp.Integer(-4): 8, sp.Integer(1): 16})
    # GSVY identification (general d, k): Phi_1^{B(x)B}(M^beta) = (d/2) ln(2E) - (d-1) ln k = U
    Ee, dd, kk = sp.symbols("E d k", positive=True)
    out["Phi_1^{B(x)B}(M^beta) == (1-d) ln k + (d/2) ln(2E) == U (general d, k)"] = sp.simplify(
        (dd / 2 * sp.log(2 * Ee) - (dd - 1) * sp.log(kk)) - ((1 - dd) * sp.log(kk) + dd / 2 * sp.log(2 * Ee))) == 0
    out["first-moment exponent of balanced 5-colourings at d = 12: log(4096/3125) > 0 (GSVY Remark 2 needs < 0)"] = (
        Fr(5) * Fr(4, 5) ** 6 == Fr(4096, 3125) and Fr(4096, 3125) > 1)
    bools = [v for k_, v in out.items() if isinstance(v, bool) and not k_.startswith("(5,13) admissible")]
    out["D ok"] = all(bools) and (out["(5,13) admissible rho < a ? (must be False)"] is False)
    return out


# ---------------------------------------------------------------------------------------------------------- E
_ODF = [1]          # _ODF[j] = (2j - 1)!!, extended on demand


def odd_dfact(j):
    while len(_ODF) <= j:
        _ODF.append(_ODF[-1] * (2 * len(_ODF) - 1))
    return _ODF[j]


def matchings_no_intra(sizes):
    """Number of perfect matchings of sum(sizes) points with no pair inside a class (inclusion-exclusion):
    sum over (j_i) of prod_i (-1)^{j_i} C(s_i, 2 j_i) (2 j_i - 1)!!  *  (sum s - 2 sum j - 1)!!."""
    tot = sum(sizes)
    if tot % 2:
        return 0
    conv = [1]
    for s in sizes:
        a = [(-1) ** j * comb(s, 2 * j) * odd_dfact(j) for j in range(s // 2 + 1)]
        new = [0] * (len(conv) + len(a) - 1)
        for i, ci in enumerate(conv):
            if ci == 0:
                continue
            for j, aj in enumerate(a):
                new[i + j] += ci * aj
        conv = new
    return sum(cJ * odd_dfact(tot // 2 - J) for J, cJ in enumerate(conv) if tot - 2 * J >= 0)


def first_moment_EY(k, d, t):
    n, s = k * t, d * t
    N = matchings_no_intra([s] * k)
    num = factorial(n) * N
    den = factorial(t) ** k * dfact(d * n - 1)
    return Fr(num, den)


def section_E():
    out = {}
    k, d = 5, 12
    UI = arb(5).log() + 6 * (arb(4).log() - arb(5).log())
    out["U(I) = log 5 + 6 log(4/5)"] = str(UI)
    rows, bound_ok, mono_ok, prev = [], True, True, None
    for t in range(1, 21):
        n = k * t
        EY = first_moment_EY(k, d, t)
        rate = (arb(EY.numerator).log() - arb(EY.denominator).log()) / n
        gap = UI - rate
        logP = (26 + arb(25) / 2 * arb(12 * n + 1).log() + arb(401) / 2 * arb(6 * n + 1).log()) / n
        bound_ok &= bool(rate <= UI + logP)
        if prev is not None and t >= 3 and not bool(gap < prev):
            mono_ok = False
        prev = gap
        if t in (1, 2, 5, 10, 15, 20):
            rows.append({"t": t, "n": n, "(1/n) ln EY": float(rate.mid()), "U(I) - rate": float(gap.mid()),
                         "n (U(I) - rate)/ln n (-> (k-1)/2 = 2)": float((gap * n / arb(n).log()).mid())})
    out["k = 5 table (EY exact, n = 5t)"] = rows
    out["k = 5: rate <= U(I) + (1/n) ln P_12(n) for all t <= 20"] = bound_ok
    out["k = 5: gap U(I) - rate strictly decreasing for 3 <= t <= 20"] = mono_ok
    out["k = 5: gap positive at t = 20"] = bool(prev > 0)
    # k = 4 cross-check against chi8's independent formula: n = 120 rate
    EY4 = first_moment_EY(4, 8, 30)
    rate4 = (arb(EY4.numerator).log() - arb(EY4.denominator).log()) / 120
    out["k = 4, n = 120 rate (inclusion-exclusion) vs chi8 E-section value 0.18083321333111818"] = [float(rate4.mid()), CHI8_RATE_N120]
    out["k = 4 cross-check agrees to 1e-12"] = abs(float(rate4.mid()) - CHI8_RATE_N120) < 1e-12
    # direct cross-check of the matching count for 4 equal classes against the multinomial-square formula, s = 16
    s = 16
    alt = factorial(s) ** 2 * sum((factorial(s) // (factorial(x) * factorial(y) * factorial(s - x - y))) ** 2
                                  for x in range(s + 1) for y in range(s - x + 1))
    out["k = 4, s = 16: inclusion-exclusion count == (s!)^2 sum multinomial(s;x,y,z)^2"] = matchings_no_intra([s] * 4) == alt
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["E ok"] = all(bools)
    return out


# ---------------------------------------------------------------------------------------------------------- F
def E_arb_k(M, k=5, beta=Fr(11, 12)):
    cl = cells(k)
    b = A_(beta)
    tot = arb(0)
    for i, u in enumerate(cl):
        for v in cl[i + 1:]:
            if allowed(u, v):
                mu, mv = M[u[0]][u[1]], M[v[0]][v[1]]
                if mu != 0 and mv != 0:
                    tot += (A_(mu) * A_(mv)) ** b
    return tot


def section_F():
    out = {}
    k = 5
    cs = constants(5, 12)["_arb"]
    C12 = cs["C"]
    J = [[Fr(1, 5)] * 5 for _ in range(5)]
    EJ = E_arb_k(J)
    out["E(J) (arb, 200 pairs) == 200 * 5^(-11/6)"] = bool(abs(EJ - cs["E0"]) < arb("1e-60"))

    def diag(dv, ov):
        return [[dv if p == q else ov for q in range(5)] for p in range(5)]

    circ_row = [Fr(1, 2), Fr(1, 4), Fr(1, 4), Fr(0), Fr(0)]
    tests = {
        "(J+I)/2": diag(Fr(3, 5), Fr(1, 10)),
        "M_{3/4} (rows 4/5, 1/20 x4)": diag(Fr(4, 5), Fr(1, 20)),
        "I": diag(Fr(1), Fr(0)),
        "J_2/2 (+) J_3/3": [[(Fr(1, 2) if q < 2 else Fr(0)) if p < 2 else (Fr(1, 3) if q >= 2 else Fr(0)) for q in range(5)] for p in range(5)],
        "1 (+) J_4/4": [[(Fr(1) if q == 0 else Fr(0)) if p == 0 else (Fr(0) if q == 0 else Fr(1, 4)) for q in range(5)] for p in range(5)],
        "J + (1/100)(I - J)": [[Fr(1, 5) + Fr(1, 100) * ((1 if p == q else 0) - Fr(1, 5)) for q in range(5)] for p in range(5)],
        "circulant (1/2, 1/4, 1/4, 0, 0)": [[circ_row[(q - p) % 5] for q in range(5)] for p in range(5)],
    }
    res, allok = {}, True
    for name, M in tests.items():
        assert all(sum(row) == 1 for row in M) and all(sum(M[p][q] for p in range(5)) == 1 for q in range(5)), name
        EM = E_arb_k(M)
        dist2 = sum((A_(M[p][q]) - A_(Fr(1, 5))) ** 2 for p in range(5) for q in range(5))
        dU = 6 * (EM / EJ).log()
        okv = bool(dU + C12 * dist2 < 0)
        allok &= okv
        res[name] = {"U(M) - U(J)": str(dU), "-C_12 |M - J|^2": str(-C12 * dist2), "certain": okv}
    out["Theorem C at explicit rational DS 5x5 matrices (consistency, not proof)"] = res
    out["all test points satisfy U(M) - U(J) < -C_12 |M-J|^2 (certain)"] = allok
    out["E(I) == 10 exactly (10 allowed pairs among the diagonal cells, each of weight 1)"] = (
        bool(abs(E_arb_k(tests["I"]) - 10) < arb("1e-60")))
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["F ok"] = all(bools)
    return out


# ---------------------------------------------------------------------------------------------------------- G
def section_G():
    out = {}
    d = sp.Integer(12)
    r = sp.symbols("r0:4", positive=True)
    w, P, G = sp.symbols("w P G", positive=True)
    lin = sum(((1 + sp.log(w)) / 2 + sp.log(ri)) * d * ri for ri in r)
    sub = {r[3]: 1 - r[0] - r[1] - r[2]}
    out["sum_i mu_i d r_i == d(1 + ln w)/2 + d sum r ln r (sum r = 1, mu_i = c_1 + ln r_i, w = e^{2c_1-1})"] = sp.simplify(
        sp.expand(lin - (d * (1 + sp.log(w)) / 2 + d * sum(ri * sp.log(ri) for ri in r))).subs(sub)) == 0
    V = (d - 1) * G + d / 2 * sp.log(d) + w * P - d * (1 + sp.log(w)) / 2 - d * G
    wst = sp.solve(sp.diff(V, w), w)
    out["optimised over w > 0: exponent == -sum r ln r + (d/2) ln(2P)"] = (
        len(wst) == 1 and sp.simplify(sp.expand_log(V.subs(w, wst[0]) - (-G + d / 2 * sp.log(2 * P)), force=True)) == 0)
    pairs = sum(r[i] * r[j] for i in range(4) for j in range(i + 1, 4))
    out["sum_{i<j} r_i r_j == (1 - sum r^2)/2 (sum r = 1)"] = sp.simplify(
        (pairs - (1 - sum(ri ** 2 for ri in r)) / 2).subs(sub)) == 0
    out["max at uniform: ln 4 + 6 ln(3/4) == ln(729/1024) < 0"] = (
        sp.simplify(sp.expand_log(sp.log(4) + 6 * sp.log(sp.Rational(3, 4)) - sp.log(sp.Rational(729, 1024)), force=True)) == 0
        and Fr(729, 1024) < 1)
    # exact control: E Z_4 for P_{n,12}, n <= 10 (all class vectors)
    rows, allok = [], True
    l = arb(729).log() - arb(1024).log()
    for n in range(4, 11):
        tot = Fr(0)
        for n1 in range(n + 1):
            for n2 in range(n - n1 + 1):
                for n3 in range(n - n1 - n2 + 1):
                    n4 = n - n1 - n2 - n3
                    ns = [n1, n2, n3, n4]
                    mult = factorial(n) // (factorial(n1) * factorial(n2) * factorial(n3) * factorial(n4))
                    tot += mult * matchings_no_intra([12 * x for x in ns])
        EZ = tot / dfact(12 * n - 1)
        if EZ == 0:
            continue
        rate = (arb(EZ.numerator).log() - arb(EZ.denominator).log()) / n
        logP = (3 * arb(n + 1).log() + 5 + 2 * arb(12 * n + 1).log() + arb(13) / 2 * arb(6 * n + 1).log()) / n
        okn = bool(rate <= l + logP)
        allok &= okn
        rows.append({"n": n, "(1/n) ln E Z_4": float(rate.mid()), "ln(729/1024)": float(l.mid())})
    out["exact E Z_4 (all class vectors), 4 <= n <= 10: rate <= ln(729/1024) + (1/n) ln P_4(n) (certain)"] = allok
    out["table"] = rows
    out["note: P_4(n)"] = "(n+1)^3 e^5 (12n+1)^2 (6n+1)^{13/2}: class vectors, points e^4 (dn+1)^2, pairs (dn/2+1)^6, pairings e (dn/2+1)^{1/2}"
    bools = [v for v in out.values() if isinstance(v, bool)]
    out["G ok"] = all(bools)
    return out


# ---------------------------------------------------------------------------------------------------------- S
def section_S():
    k, d = 5, 12
    cl = cells(k)
    ADJ = np.array([[1.0 if allowed(u, v) else 0.0 for v in cl] for u in cl])
    JF = np.full((k, k), 1.0 / k)
    beta = 11 / 12

    def sinkhorn(M, it=1000):
        for _ in range(it):
            M = M / M.sum(axis=1, keepdims=True)
            M = M / M.sum(axis=0, keepdims=True)
        return M

    def psi_exact(m, tol=1e-12, maxit=300):
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
        return (1 - d / 2) * math.log(k) + (d / 2) * math.log(d) + (d - 1) / k * ent - inner / k

    rng = np.random.default_rng(1212)
    EJ = 200 * 5 ** (-11 / 6)
    worst_ds, worst_rs, gap_min = -1e9, -1e9, 1e9
    for i in range(3000):
        M = sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(k, k))))
        y = M.reshape(-1) ** beta
        Ev = 0.5 * y @ (ADJ @ y)
        worst_ds = max(worst_ds, (Ev - EJ) / np.sum((M - JF) ** 2))
        Rm = np.array([rng.dirichlet(np.ones(k) * rng.choice([0.1, 1, 4])) for _ in range(k)])
        y = Rm.reshape(-1) ** beta
        worst_rs = max(worst_rs, (0.5 * y @ (ADJ @ y) - EJ) / np.sum((Rm - JF) ** 2))
        if i < 200:
            gap_min = min(gap_min, -11 * math.log(5) + 6 * math.log(2 * Ev) - psi_exact(M))
    yJ = JF.reshape(-1) ** beta
    gJ = -11 * math.log(5) + 6 * math.log(2 * 0.5 * yJ @ (ADJ @ yJ)) - psi_exact(JF)
    return {"note": "floats; NOT evidence",
            "max (E(M)-E(J))/|M-J|^2 over 3000 random 5x5 DS / row-stochastic (Theorem C: <= -kappa ~ -1.0228e-3)": [worst_ds, worst_rs],
            "min (U - Psi_12) over 200 random DS (weak duality: >= 0); value at J (= 0)": [gap_min, gJ]}


def main():
    out = {"note": "verifier for review/PROOF_CHI12.r1.md (lane random12reg-colour); exact/sympy/arb except section S"}
    out["A (5,12)"] = arith(5, 12)
    out["B"] = section_B()
    out["C"] = section_C()
    out["D"] = section_D()
    out["E"] = section_E()
    out["F"] = section_F()
    out["G"] = section_G()
    out["S"] = section_S()
    out["all_required_true"] = bool(out["A (5,12)"]["A ok"] and out["B"]["B ok"] and out["C"]["C ok"] and out["D"]["D ok"]
                                    and out["E"]["E ok"] and out["F"]["F ok"] and out["G"]["G ok"])
    path = os.path.join(HERE, "..", "evidence", "verify_chi12.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
