"""Verifier extension for review/PROOF_CHI8.r2.md (items added after the r1 reviews). Exact rationals, big integers,
sympy and python-flint arb. Self-contained; reads nothing from other lanes. Writes ../evidence/verify_chi8_r2.json.

  F  AM04 Section 6 (layout l.440-455): the relaxed maximiser beta = (d/p) alpha_u alpha_v, p = 1 - 2/k + sum alpha^2,
     has marginals (d/p) alpha_u (1 - 2/k + alpha_u); it satisfies AM04's constraints (12) iff alpha_u = sum alpha^2
     on the support. Exact witnesses: (J+I)/2 and M_{2/3} (infeasible); J and I (feasible, positive controls).
  G  KPW layout l.1251 (proof of Lemma 9): "(k-1)^2 + (k-1)^2 exceeds k^2" holds at k = 4 (18 > 16), fails at k = 3.
  H  GSVY identification: U(M) = Phi_1^{B(x)B}(M^{7/8}) (GSVY (15)); GSVY's map (20) sends M^{7/8} to M/4;
     Psi_d(M) = Psi_1^{B(x)B}(M/k) (GSVY (14)/(22)) in the normalisation of D8/CHI8 (constant bookkeeping, general d, k);
     Phi_1 is invariant under scaling R; B = J_4 - I_4 has eigenvalues 3, -1, -1, -1, so B(x)B is not PSD.
  I  Self-contained first moment for 3-colourings of P_{n,8} (weak duality with multipliers c_1 + log r_i):
     exponent algebra; max over class proportions = log(16/27) < 0; polynomial factor; exact-count control n <= 60.
  K  (added for r2 after the Claude v2 review) (i) the pilot/D8_SCREEN multiplier convention
     U_lam = C_d + ((d-1)/4) sum m ln m - (d/4) sum m lam + (1/4) sum_e e^{lam_u+lam_v}, C_d = (1-d/2) ln4 + (d/2) ln d - d/2,
     equals Lemma A's V_mu term by term under lam_u = mu_u + (ln4 - 1)/2 (uses sum m = 4); (ii) arb point values of the
     Proof 2 slack F(u_*) - F(r(x)) - c_row |r(x) - u_*|^2 at the cut points x = 1/4 -+ 1/25 and at x = 31/100, to
     compare with the certified piece slacks (enclosure overestimation).
Run (from code/): OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B verify_chi8_r2.py
"""
import json
import os
from fractions import Fraction as Fr
from math import factorial

import sympy as sp
from flint import arb, ctx

ctx.prec = 256
HERE = os.path.dirname(os.path.abspath(__file__))
CELLS = [(p, q) for p in range(4) for q in range(4)]


def allowed(u, v):
    return u[0] != v[0] and u[1] != v[1]


# ---------------------------------------------------------------------------------------------------------- F
def am04_marginals(M, d=8, k=4):
    """alpha = M/k (Fractions). Returns (sum alpha^2, p, {cell: (relaxed marginal, required d*alpha)})."""
    al = {u: Fr(M[u[0]][u[1]]) / k for u in CELLS}
    s2 = sum(a * a for a in al.values())
    p = 1 - Fr(2, k) + s2
    out = {}
    for u in CELLS:
        marg = sum(Fr(d) / p * al[u] * al[v] for v in CELLS if allowed(u, v))
        out[u] = (marg, d * al[u])
    return s2, p, out


def section_F():
    out = {}
    k, d = 4, 8
    # symbolic: generic doubly stochastic M (9 free entries); alpha = M/4
    a = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}"))
    M = sp.zeros(4, 4)
    for i in range(3):
        for j in range(3):
            M[i, j] = a[i, j]
        M[i, 3] = 1 - sum(a[i, j] for j in range(3))
    for j in range(4):
        M[3, j] = 1 - sum(M[i, j] for i in range(3))
    al = M / 4
    s2 = sum(al[i, j] ** 2 for i in range(4) for j in range(4))
    ok_nbr = True
    for (i, j) in CELLS:
        nb = sum(al[r, s] for (r, s) in CELLS if r != i and s != j)
        ok_nbr &= sp.expand(nb - (1 - sp.Rational(2, k) + al[i, j])) == 0
    out["generic DS M, alpha = M/4: sum over allowed partners of alpha_v == 1 - 2/k + alpha_u (all 16 cells)"] = ok_nbr
    pp = 1 - sp.Rational(2, k) + s2
    ok_marg = True
    for (i, j) in CELLS:
        marg = sum(d / pp * al[i, j] * al[r, s] for (r, s) in CELLS if r != i and s != j)
        target = d / pp * al[i, j] * (1 - sp.Rational(2, k) + al[i, j])
        ok_marg &= sp.simplify(marg - target) == 0
    out["relaxed maximiser marginal == (d/p) alpha_u (1 - 2/k + alpha_u) (all 16 cells)"] = ok_marg
    x, S = sp.symbols("x S", positive=True)
    expr = sp.Integer(d) / (1 - sp.Rational(2, k) + S) * x * (1 - sp.Rational(2, k) + x) - d * x
    out["(d/p) x (1 - 2/k + x) - d x == d x (x - S)/p (so feasibility <=> x = S for x > 0)"] = sp.simplify(
        expr - d * x * (x - S) / (1 - sp.Rational(2, k) + S)) == 0
    wit = {}

    def mat(diag, off):
        return [[diag if p == q else off for q in range(4)] for p in range(4)]

    cases = {"(J+I)/2": mat(Fr(5, 8), Fr(1, 8)), "M_{2/3}": mat(Fr(3, 4), Fr(1, 12)),
             "J (control: feasible)": mat(Fr(1, 4), Fr(1, 4)), "I (control: feasible)": mat(Fr(1), Fr(0))}
    feas = {}
    for name, Mx in cases.items():
        s2v, pv, mg = am04_marginals(Mx)
        diag = mg[(0, 0)]
        offd = mg[(0, 1)]
        feasible = all(m == r for (m, r) in mg.values())
        feas[name] = feasible
        wit[name] = {"sum alpha^2": str(s2v), "p": str(pv),
                     "diagonal cell: relaxed marginal, required d alpha": [str(diag[0]), str(diag[1])],
                     "off-diagonal cell: relaxed marginal, required d alpha": [str(offd[0]), str(offd[1])],
                     "sum of relaxed marginals": str(sum(m for (m, _) in mg.values())),
                     "relaxed maximiser satisfies all 16 constraints (12)": feasible}
    out["exact witnesses"] = wit
    out["(J+I)/2: sum alpha^2 = 7/64, p = 39/64, marginals 35/26 vs 5/4 and 17/78 vs 1/4"] = (
        wit["(J+I)/2"]["sum alpha^2"] == "7/64" and wit["(J+I)/2"]["p"] == "39/64"
        and wit["(J+I)/2"]["diagonal cell: relaxed marginal, required d alpha"] == ["35/26", "5/4"]
        and wit["(J+I)/2"]["off-diagonal cell: relaxed marginal, required d alpha"] == ["17/78", "1/4"])
    out["infeasible at (J+I)/2 and M_{2/3}; feasible at J and I"] = (
        (not feas["(J+I)/2"]) and (not feas["M_{2/3}"]) and feas["J (control: feasible)"] and feas["I (control: feasible)"])
    out["relaxation strictly lossy at (J+I)/2: phi_8 - phi_8(J) > 0 (13^32 > 2^56 3^32 5^5) while U - U(J) < 0"] = True if (
        13 ** 32 > 2 ** 56 * 3 ** 32 * 5 ** 5) else False
    # U((J+I)/2) - U(J) < 0 in arb (independent recomputation)
    e78 = arb(7) / 8
    Mh = cases["(J+I)/2"]
    E = arb(0)
    for i, u in enumerate(CELLS):
        for v in CELLS[i + 1:]:
            if allowed(u, v):
                E += (arb(Mh[u[0]][u[1]].numerator) / Mh[u[0]][u[1]].denominator
                      * arb(Mh[v[0]][v[1]].numerator) / Mh[v[0]][v[1]].denominator) ** e78
    dU = 4 * (E / (9 / arb(2).sqrt())).log()
    out["U((J+I)/2) - U(J) (arb)"] = str(dU)
    out["U((J+I)/2) - U(J) < 0 (certain)"] = bool(dU < 0)
    # KPW's relaxed exponent phi_8 (KPW (3.8) at k = 4): phi_8(M) = -(1/4) sum m ln m + 4 ln(1/2 + sum m^2/16)
    def phi8(Mx):
        ent = arb(0)
        s2m = arb(0)
        for u in CELLS:
            mv = Mx[u[0]][u[1]]
            if mv != 0:
                am = arb(mv.numerator) / mv.denominator
                ent += am * am.log()
                s2m += am * am
        return -ent / 4 + 4 * (arb(1) / 2 + s2m / 16).log()
    dphi = phi8(Mh) - phi8(cases["J (control: feasible)"])
    closed = arb(2).log() - arb(5) / 8 * arb(5).log() + 4 * (arb(13) / 12).log()
    out["phi_8((J+I)/2) - phi_8(J) (arb, from the definition)"] = str(dphi)
    out["equals log 2 - (5/8) log 5 + 4 log(13/12) (contains 0 difference)"] = bool(abs(dphi - closed) < arb("1e-60"))
    out["phi_8((J+I)/2) - phi_8(J) > 0 (certain)"] = bool(dphi > 0)
    out["relaxation overestimate at (J+I)/2: [ln4 + phi_8(M)] - U(M) = dphi - dU > 0.036 (certain)"] = bool(dphi - dU > arb("0.036"))
    out["overestimate value (arb)"] = str(dphi - dU)
    out["F ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


# ---------------------------------------------------------------------------------------------------------- G
def section_G():
    out = {"k = 4: (k-1)^2 + (k-1)^2 = 18 > 16 = k^2": 2 * 3 ** 2 > 4 ** 2 and 2 * 3 ** 2 == 18,
           "k = 3: (k-1)^2 + (k-1)^2 = 8 < 9 = k^2 (the l.1251 sentence fails at k = 3)": 2 * 2 ** 2 < 3 ** 2,
           "k = 5: 32 > 25": 2 * 4 ** 2 > 5 ** 2}
    out["G ok"] = all(out.values())
    return out


# ---------------------------------------------------------------------------------------------------------- H
def section_H():
    out = {}
    E, d, k = sp.symbols("E d k", positive=True)
    # Phi_1(R) = (d/2) ln(sum_{u,v} A_uv R_u R_v) - (d-1) ln(sum_u R_u^{d/(d-1)}), with R = m^{(d-1)/d}:
    #   sum_{u,v} A_uv R_u R_v = 2 E_beta(M) (ordered pairs), sum_u R_u^{d/(d-1)} = sum m = k
    Phi = d / 2 * sp.log(2 * E) - (d - 1) * sp.log(k)
    U = (1 - d) * sp.log(k) + d / 2 * sp.log(2 * E)
    out["Phi_1^{B(x)B}(M^beta) == U(M) = (1-d) ln k + (d/2) ln(2 E_beta) (general d, k)"] = sp.simplify(Phi - U) == 0
    out["at (k, d) = (4, 8): U = -10 ln 2 + 4 ln E"] = sp.simplify(
        sp.expand_log(U.subs({k: 4, d: 8}) - (-10 * sp.log(2) + 4 * sp.log(E)), force=True)) == 0
    t = sp.symbols("t", positive=True)
    R = sp.symbols("R0:16", positive=True)
    Q = sum(R[i] * R[j] for i in range(16) for j in range(16) if allowed(CELLS[i], CELLS[j]))
    dd = sp.Integer(8)
    phi = dd / 2 * sp.log(Q) - (dd - 1) * sp.log(sum(r ** (dd / (dd - 1)) for r in R))
    phit = dd / 2 * sp.log(Q.subs({r: t * r for r in R}, simultaneous=True)) - (dd - 1) * sp.log(
        sum((t * r) ** (dd / (dd - 1)) for r in R))
    out["Phi_1 is invariant under R -> tR (d = 8)"] = sp.simplify(sp.expand_log(phit - phi, force=True)) == 0
    m = sp.symbols("m0:16", positive=True)
    Rm = [mm ** sp.Rational(7, 8) for mm in m]
    tot = sum(r ** sp.Rational(8, 7) for r in Rm)
    out["GSVY map (20): alpha_u = R_u^{8/7}/sum R^{8/7} == m_u/sum m (= m_u/4 on DS M)"] = all(
        sp.simplify(Rm[i] ** sp.Rational(8, 7) / tot - m[i] / sum(m)) == 0 for i in range(16))
    # constant bookkeeping: Psi_d(M) = (1-d/2) ln k + (d/2) ln d + ((d-1)/k) sum m ln m - (1/k) min sum_e l ln l,
    # with m = k gamma, l_e = d k y_e (unordered e; y symmetric on ordered pairs, sum_ordered y = 1):
    #   sum_e l ln l = (dk/2)(S_y + ln(dk)),  S_y = sum_ordered y ln y;
    #   GSVY: Psi_1^{B(x)B}(gamma) = (d-1) sum gamma ln gamma - (d/2) min S_y.
    G1, Sy = sp.symbols("G1 S_y")   # G1 = sum gamma ln gamma
    ours = (1 - d / 2) * sp.log(k) + d / 2 * sp.log(d) + (d - 1) * (G1 + sp.log(k)) - (d / 2) * (Sy + sp.log(d * k))
    gsvy = (d - 1) * G1 - d / 2 * Sy
    out["Psi_d(M) == Psi_1^{B(x)B}(M/k) (constant bookkeeping; uses sum gamma = 1, sum_ordered y = 1)"] = sp.simplify(
        sp.expand_log(ours - gsvy, force=True)) == 0
    B = sp.ones(4, 4) - sp.eye(4)
    ev = B.eigenvals()
    out["eigenvalues of B = J_4 - I_4"] = {str(kk): vv for kk, vv in ev.items()}
    BB = sp.kronecker_product(B, B) if hasattr(sp, "kronecker_product") else sp.Matrix(sp.tensorproduct(B, B))
    evBB = BB.eigenvals()
    out["eigenvalues of B(x)B"] = {str(kk): vv for kk, vv in evBB.items()}
    out["B(x)B has a negative eigenvalue (not PSD; GSVY (18) unavailable)"] = bool(min(evBB.keys()) < 0)
    out["H ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


# ---------------------------------------------------------------------------------------------------------- I
def section_I():
    out = {}
    d = sp.Integer(8)
    r = sp.symbols("r0:3", positive=True)
    w, P, G = sp.symbols("w P G", positive=True)   # w = e^{2c-1} > 0, P = sum_{i<j} r_i r_j > 0, G = sum r ln r
    H = -sum(ri * sp.log(ri) for ri in r)
    s2 = sum(ri ** 2 for ri in r)
    # exponent before duality: (d-1) sum r ln r + (d/2) ln d - sum_{i<j} beta_ij ln beta_ij, sum_{j!=i} beta_ij = d r_i.
    # multipliers mu_i = c + ln r_i, i.e. c = (1 + ln w)/2:
    #   -sum beta ln beta <= sum_{i<j} e^{mu_i+mu_j-1} - sum_i mu_i d r_i = w P - d (1 + ln w)/2 - d G   (uses sum r = 1)
    lin = sum(((1 + sp.log(w)) / 2 + sp.log(ri)) * d * ri for ri in r)
    out["sum_i mu_i d r_i == d(1 + ln w)/2 + d sum r ln r when sum r = 1"] = sp.simplify(
        sp.expand(lin - (d * (1 + sp.log(w)) / 2 + d * sum(ri * sp.log(ri) for ri in r))).subs(r[2], 1 - r[0] - r[1])) == 0
    V = (d - 1) * G + d / 2 * sp.log(d) + w * P - d * (1 + sp.log(w)) / 2 - d * G
    wst = sp.solve(sp.diff(V, w), w)
    ok = (len(wst) == 1 and sp.simplify(wst[0] - d / (2 * P)) == 0 and sp.simplify(sp.diff(V, w, 2) - d / (2 * w ** 2)) == 0
          and sp.simplify(sp.expand_log(V.subs(w, wst[0]) - (-G + d / 2 * sp.log(2 * P)), force=True)) == 0)
    out["weak duality, optimised over w = e^{2c-1} > 0 (strictly convex): exponent == -sum r ln r + (d/2) ln(2P)"] = ok
    pairs = sum(r[i] * r[j] for i in range(3) for j in range(i + 1, 3))
    out["identity sum_{i<j} r_i r_j == (1 - sum r^2)/2 when sum r = 1"] = sp.simplify(
        (pairs - (1 - s2) / 2).subs(r[2], 1 - r[0] - r[1])) == 0
    # exact exponent at the balanced point equals the bound (tightness at r = 1/3)
    bal = sp.log(3) + 4 * sp.log(sp.Rational(2, 3))
    out["max over r: H <= ln 3 and sum r^2 >= 1/3 (both at r uniform) => bound = ln 3 + 4 ln(2/3) = ln(16/27)"] = sp.simplify(
        sp.expand_log(bal - sp.log(sp.Rational(16, 27)), force=True)) == 0
    out["16/27 < 1 (exact)"] = Fr(16, 27) < 1
    # exact-count control: E Z_3 for P_{n,8} by the exact matching count, n <= 60
    rows, allok = [], True
    l1627 = arb(16) .log() - arb(27).log()
    for n in range(3, 61):
        N = 8 * n
        dfact = factorial(N) // (factorial(N // 2) * 2 ** (N // 2))   # (N-1)!!
        tot = 0
        for n1 in range(n + 1):
            for n2 in range(n - n1 + 1):
                n3 = n - n1 - n2
                ns = (n1, n2, n3)
                if max(ns) * 2 > n:
                    continue
                s = [8 * x for x in ns]
                b12 = (s[0] + s[1] - s[2]) // 2
                b13 = (s[0] + s[2] - s[1]) // 2
                b23 = (s[1] + s[2] - s[0]) // 2
                Ms = factorial(s[0]) * factorial(s[1]) * factorial(s[2]) // (factorial(b12) * factorial(b13) * factorial(b23))
                tot += factorial(n) // (factorial(n1) * factorial(n2) * factorial(n3)) * Ms
        # E Z_3 = tot / dfact
        rate = (arb(tot).log() - arb(dfact).log()) / n
        logP = (2 * arb(n + 1).log() + 4 + arb(3) / 2 * arb(8 * n + 1).log() + arb(7) / 2 * arb(4 * n + 1).log()) / n
        okn = bool(rate <= l1627 + logP)
        allok &= okn
        if n in (3, 6, 12, 24, 36, 48, 60):
            rows.append({"n": n, "(1/n) ln E Z_3": float(rate.mid()), "ln(16/27)": float(l1627.mid()),
                         "bound ln(16/27) + (1/n) ln P3(n)": float((l1627 + logP).mid())})
    out["exact E Z_3 for P_{n,8}, 3 <= n <= 60: (1/n) ln E Z_3 <= ln(16/27) + (1/n) ln P3(n) (certain)"] = allok
    out["table"] = rows
    out["note: polynomial factor (hand derivation, tested by the exact-count control above)"] = (
        "P3(n) = (n+1)^2 e^4 (8n+1)^{3/2} (4n+1)^{7/2}: points e^3 (dn+1)^{3/2}, tuples (dn/2+1)^3, "
        "pairings e (dn/2+1)^{1/2}, at most (n+1)^2 class-size vectors")
    out["I ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


# ---------------------------------------------------------------------------------------------------------- K
def section_K():
    out = {}
    d, G, X, Mm = sp.symbols("d G X Mm", real=True)          # G = sum m ln m, X = sum_e e^{mu_u+mu_v}, Mm = sum mu m
    s = (sp.log(4) - 1) / 2
    Cd = (1 - d / 2) * sp.log(4) + d / 2 * sp.log(d) - d / 2
    U_lam = Cd + (d - 1) / 4 * G - d / 4 * (Mm + 4 * s) + sp.Rational(1, 4) * sp.exp(2 * s) * X   # lam = mu + s, sum m = 4
    V_mu = (d - 1) / 4 * G + (1 - d) * sp.log(4) + d / 2 * sp.log(d) + sp.exp(-1) * X - d / 4 * Mm
    out["U_lam(lam = mu + (ln4-1)/2) == V_mu identically (general d; uses sum m = 4)"] = sp.simplify(
        sp.expand_log(sp.expand(U_lam - V_mu), force=True)) == 0
    out["(1/4) e^{2s} == e^{-1} for s = (ln4-1)/2"] = sp.simplify(sp.Rational(1, 4) * sp.exp(2 * s) - sp.exp(-1)) == 0
    # status-line form lam_u = ln C + (7/8) ln m_u  <=>  mu_u = c_0 + (7/8) ln m_u with c_0 = ln C - (ln4 - 1)/2
    out["note: convention map"] = "lam_u = ln C + (7/8) ln m_u (pilot) <=> mu_u = c_0 + (7/8) ln m_u, c_0 = ln C - (ln 4 - 1)/2"
    # (ii) Proof 2 slack point values (c_row = 1/40)
    c = arb(1) / 40
    FU = 9 / (4 * arb(2).sqrt())
    e78, e74 = arb(7) / 8, arb(7) / 4
    q = arb(1) / 4

    def slack(fam, x):
        X0 = arb(x.numerator) / x.denominator
        if fam == 1:
            Y = (1 - X0) / 3
            S = X0 ** e78 + 3 * Y ** e78
            Q = X0 ** e74 + 3 * Y ** e74
            D = (X0 - q) ** 2 + 3 * (Y - q) ** 2
        else:
            Y = arb(1) / 2 - X0
            S = 2 * X0 ** e78 + 2 * Y ** e78
            Q = 2 * X0 ** e74 + 2 * Y ** e74
            D = 2 * (X0 - q) ** 2 + 2 * (Y - q) ** 2
        return FU - (S * S + Q / 2) - c * D, FU - (S * S + Q / 2), c * D
    pts = {}
    ok = True
    for fam in (1, 2):
        for x in (Fr(29, 100), Fr(21, 100), Fr(31, 100)):
            sl, gapF, cd = slack(fam, x)
            pts[f"family {fam}, x = {x}"] = {"slack F(u*) - F - c_row|r-u*|^2": str(sl), "F(u*) - F": str(gapF),
                                            "c_row |r-u*|^2": str(cd), "slack > 0 (certain)": bool(sl > 0)}
            ok &= bool(sl > 0)
    out["Proof 2 slack at sample points (arb point values; certified piece slacks are lower bounds)"] = pts
    out["all sample slacks positive (certain)"] = ok
    # (iii) KPW's Gaussian matrix at (k, d) = (4, 8): H = ((k^2-2k-d+2)/(k^2-2k+2)) (J_3 + I_3)^{(x)2} = (1/5)(J_3 + I_3)^{(x)2}
    k, dd = 4, 8
    cH = sp.Rational(k * k - 2 * k - dd + 2, k * k - 2 * k + 2)
    A3 = sp.ones(3, 3) + sp.eye(3)
    H = cH * sp.kronecker_product(A3, A3)
    evH = H.eigenvals()
    out["H coefficient (k^2-2k-d+2)/(k^2-2k+2) at (4,8)"] = str(cH)
    out["eigenvalues of H at (4,8)"] = {str(kk): vv for kk, vv in evH.items()}
    out["H eigenvalues are 1/5 (x4), 4/5 (x4), 16/5 (x1)"] = (
        evH == {sp.Rational(1, 5): 4, sp.Rational(4, 5): 4, sp.Rational(16, 5): 1})
    out["det H == k^{2k-2} ((k^2-2k-d+2)/(k^2-2k+2))^{(k-1)^2} == 4^6 5^-9 (KPW (3.13))"] = (
        H.det() == sp.Integer(4) ** 6 * sp.Rational(1, 5) ** 9 == sp.Integer(k) ** (2 * k - 2) * cH ** ((k - 1) ** 2))
    out["K ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out

def main():
    out = {"note": "r2 extension verifier; exact/sympy/arb only"}
    out["F"] = section_F()
    out["G"] = section_G()
    out["H"] = section_H()
    out["I"] = section_I()
    out["K"] = section_K()
    out["all_required_true"] = bool(out["F"]["F ok"] and out["G"]["G ok"] and out["H"]["H ok"] and out["I"]["I ok"]
                                    and out["K"]["K ok"])
    path = os.path.join(HERE, "..", "evidence", "verify_chi8_r2.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
