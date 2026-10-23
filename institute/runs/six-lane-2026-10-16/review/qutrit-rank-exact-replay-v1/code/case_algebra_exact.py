"""Exact (sympy) checks of the hand algebra in Propositions A* and B* of review/LEMMA_R_PROOF.md.

Complex conjugates are independent formal symbols ("c" suffix); every check is a polynomial identity or an exact
linear solve with the nonvanishing hypotheses of the text (generic solve = those denominators nonzero).
Index conventions: N_d[b,c], Q_a[b,c], R_c[a,d], T_b[a,d], Omega_ad[b,c]; K = {1,2} -> python 0,1.
Writes ../evidence/case_algebra_exact.json.  Run: python -B case_algebra_exact.py
"""
import itertools
import json
import os

import sympy as sp
from sympy import Matrix, symbols

E = lambda i, j: Matrix(2, 2, lambda r, c: 1 if (r, c) == (i, j) else 0)
J = Matrix([[0, 1], [-1, 0]])


def conj_pair(name):
    return symbols(name), symbols(name + "c")


def gmat(name):
    m = Matrix(2, 2, lambda i, j: symbols("%s%d%d" % (name, i, j)))
    mc = Matrix(2, 2, lambda i, j: symbols("%s%d%dc" % (name, i, j)))
    return m, mc


def is_zero(M):
    return sp.expand(M) == sp.zeros(*M.shape) if hasattr(M, "shape") else sp.expand(M) == 0


def main():
    out = {}
    # ---------------- B*.1: (O1) with diagonal N, R
    p = symbols("p0:3"); q = symbols("q0:3"); r = symbols("r0:3"); s = symbols("s0:3")
    pc = symbols("p0:3c"); qc = symbols("q0:3c"); rc = symbols("r0:3c"); sc = symbols("s0:3c")
    N = [sp.diag(p[d], q[d]) for d in range(3)]
    R = [sp.diag(r[c], s[c]) for c in range(3)]
    Rcj = [sp.diag(rc[c], sc[c]) for c in range(3)]
    nvec = {0: p, 1: q}; rhoc = {0: rc, 1: sc}
    ok = True
    for a, b in itertools.product(range(2), repeat=2):
        O1 = sum(N[d + 1][b, c] * Rcj[c + 1][a, d] for c in range(2) for d in range(2))
        ok &= is_zero(O1 - nvec[b][a + 1] * rhoc[a][b + 1])
    out["B1 (O1) == n^(b)_a conj(rho^(a)_b)"] = bool(ok)
    # ---------------- B*.1: pattern enumeration over zero/nonzero supports
    pats = set()
    for z in itertools.product([0, 1], repeat=8):       # nonzero flags of p1,p2,q1,q2,r1,r2,s1,s2
        p1, p2, q1, q2, r1, r2, s1, s2 = z
        if not ((p1 or p2) and (q1 or q2) and (r1 or r2) and (s1 or s2)):
            continue
        if p1 * r1 or p2 * s1 or q1 * r2 or q2 * s2:
            continue
        pats.add(z)
    out["B1 surviving support patterns"] = sorted(pats)
    out["B1 only patterns I and II survive"] = pats == {(1, 0, 0, 1, 0, 1, 1, 0), (0, 1, 1, 0, 1, 0, 0, 1)}
    # ---------------- B*.2: (O4), (O3) under pattern I
    Q1, Q1c = gmat("Qa"); Q2, Q2c = gmat("Qb"); Qs = [None, Q1, Q2]
    T1, T1c = gmat("Ta"); T2, T2c = gmat("Tb"); Ts = [None, T1, T2]; Tcs = [None, T1c, T2c]
    patI = {p[2]: 0, q[1]: 0, r[1]: 0, s[2]: 0, pc[2]: 0, qc[1]: 0, rc[1]: 0, sc[2]: 0}
    O4 = {(b, d): sum(Qs[a + 1][b, c] * Rcj[c + 1][a, d] for a in range(2) for c in range(2)).subs(patI)
          for b in range(2) for d in range(2)}
    want4 = {(b, 0): rc[2] * Q1[b, 1] for b in range(2)}
    want4.update({(b, 1): sc[1] * Q2[b, 0] for b in range(2)})
    out["B2 (O4) under pattern I == conj(r2) Q1[b,2], conj(s1) Q2[b,1]"] = all(is_zero(O4[k] - want4[k]) for k in O4)
    Ncj = [sp.diag(pc[d], qc[d]) for d in range(3)]
    O3c = {(a, c): sum(Ncj[d + 1][b, c] * Ts[b + 1][a, d] for b in range(2) for d in range(2)).subs(patI)
           for a in range(2) for c in range(2)}                                   # conjugate form of (O3)
    want3 = {(a, 0): pc[1] * T1[a, 0] for a in range(2)}
    want3.update({(a, 1): qc[2] * T2[a, 1] for a in range(2)})
    out["B2 (O3) under pattern I == conj(p1) T1[a,1], conj(q2) T2[a,2]"] = all(is_zero(O3c[k] - want3[k]) for k in O3c)
    # ---------------- B*.3: (U) expansions for the reduced forms
    al, alc = conj_pair("al"); be, bec = conj_pair("be"); ga, gac = conj_pair("ga"); de, dec = conj_pair("de")
    x1, x1c = conj_pair("x1"); y1, y1c = conj_pair("y1"); x2, x2c = conj_pair("x2"); y2, y2c = conj_pair("y2")
    Qf = [None, al * E(0, 0) + be * E(1, 0), ga * E(0, 1) + de * E(1, 1)]
    Qfc = [None, alc * E(0, 0) + bec * E(1, 0), gac * E(0, 1) + dec * E(1, 1)]
    Tf = [None, x1 * E(0, 1) + y1 * E(1, 1), x2 * E(0, 0) + y2 * E(1, 0)]
    Tfc = [None, x1c * E(0, 1) + y1c * E(1, 1), x2c * E(0, 0) + y2c * E(1, 0)]
    QQd = sum((Qf[a] * Qfc[a].T for a in (1, 2)), sp.zeros(2, 2))
    QdQ = sum((Qfc[a].T * Qf[a] for a in (1, 2)), sp.zeros(2, 2))
    out["B3 sum QQ^dag form"] = is_zero(QQd - Matrix([[al * alc + ga * gac, al * bec + ga * dec], [be * alc + de * gac, be * bec + de * dec]]))
    out["B3 sum Q^dagQ form"] = is_zero(QdQ - sp.diag(al * alc + be * bec, ga * gac + de * dec))
    TTd = sum((Tf[b] * Tfc[b].T for b in (1, 2)), sp.zeros(2, 2))
    TdT = sum((Tfc[b].T * Tf[b] for b in (1, 2)), sp.zeros(2, 2))
    out["B3 sum TT^dag form"] = is_zero(TTd - Matrix([[x1 * x1c + x2 * x2c, x1 * y1c + x2 * y2c], [y1 * x1c + y2 * x2c, y1 * y1c + y2 * y2c]]))
    out["B3 sum T^dagT form"] = is_zero(TdT - sp.diag(x2 * x2c + y2 * y2c, x1 * x1c + y1 * y1c))
    # ---------------- B*.4: (O2) for the reduced forms
    O2 = {(c, d): sp.expand(sum(Qf[a + 1][b, c] * Tfc[b + 1][a, d] for a in range(2) for b in range(2)))
          for c in range(2) for d in range(2)}
    out["B4 (O2) == {be x2c, al x1c, de y2c, ga y1c}"] = (O2[(0, 0)] == be * x2c and O2[(0, 1)] == al * x1c
                                                       and O2[(1, 0)] == de * y2c and O2[(1, 1)] == ga * y1c)
    # ---------------- B*.6: Omega forced to 0 when N0 = 0, N1 = p1 E11, N2 = q2 E22, Q1 = be E21, Q2 = ga E12
    p1, p1c = conj_pair("P1"); q2, q2c = conj_pair("Q2")
    Nn = [sp.zeros(2, 2), p1 * E(0, 0), q2 * E(1, 1)]
    Nnc = [sp.zeros(2, 2), p1c * E(0, 0), q2c * E(1, 1)]
    Qn = [sp.zeros(2, 2), be * E(1, 0), ga * E(0, 1)]
    Qnc = [sp.zeros(2, 2), bec * E(1, 0), gac * E(0, 1)]
    Om = {(a, d): gmat("W%d%d_" % (a, d))[0] for a in (1, 2) for d in (1, 2)}
    unknowns = [Om[k][i, j] for k in Om for i in range(2) for j in range(2)]
    eqs = []
    for a in (1, 2):   # (alpha)^dagger: Q_a N_0^dag + sum_d Om_ad N_d^dag = 0 ; (gamma)
        eqs += list(Qn[a] * Nnc[0].T + sum((Om[(a, d)] * Nnc[d].T for d in (1, 2)), sp.zeros(2, 2)))
        eqs += list(Nnc[0].T * Qn[a] + sum((Nnc[d].T * Om[(a, d)] for d in (1, 2)), sp.zeros(2, 2)))
    for d in (1, 2):   # (beta)^dagger-free forms: N_d N_0^dag + sum_a Om_ad Q_a^dag = 0 ; (delta)
        eqs += list(Nn[d] * Nnc[0].T + sum((Om[(a, d)] * Qnc[a].T for a in (1, 2)), sp.zeros(2, 2)))
        eqs += list(Nnc[0].T * Nn[d] + sum((Qnc[a].T * Om[(a, d)] for a in (1, 2)), sp.zeros(2, 2)))
    sol = sp.linsolve(eqs, unknowns)
    out["B6 Omega = 0 is the unique solution (p1,q2,beta,gamma != 0)"] = sol == sp.FiniteSet(tuple([0] * len(unknowns)))
    sol_ctrl = sp.linsolve([sp.sympify(e).subs({be: 0, bec: 0}) for e in eqs], unknowns)
    out["control B6: with beta = 0, Omega is NOT forced to 0"] = sol_ctrl != sp.FiniteSet(tuple([0] * len(unknowns)))
    # ---------------- B*.5: beta = gamma = 0 -> Omega diagonal (entries (1,2),(2,1) of (alpha)^dag and (gamma))
    p0, p0c = conj_pair("P0"); q0, q0c = conj_pair("Q0")
    Nd = [sp.diag(p0, q0), p1 * E(0, 0), q2 * E(1, 1)]
    Ndc = [sp.diag(p0c, q0c), p1c * E(0, 0), q2c * E(1, 1)]
    Qd = [None, al * E(0, 0), de * E(1, 1)]
    offdiag_zero = True
    for a in (1, 2):
        eqa = []
        A1 = Qd[a] * Ndc[0].T + sum((Om[(a, d)] * Ndc[d].T for d in (1, 2)), sp.zeros(2, 2))
        G1 = Ndc[0].T * Qd[a] + sum((Ndc[d].T * Om[(a, d)] for d in (1, 2)), sp.zeros(2, 2))
        eqa += [A1[0, 1], A1[1, 0], G1[0, 1], G1[1, 0]]
        unk = [Om[(a, 1)][0, 1], Om[(a, 1)][1, 0], Om[(a, 2)][0, 1], Om[(a, 2)][1, 0]]
        offdiag_zero &= sp.linsolve(eqa, unk) == sp.FiniteSet((0, 0, 0, 0))
    out["B5 off-diagonal Omega entries forced 0 (beta=gamma=0, p1,q2 != 0)"] = bool(offdiag_zero)
    # ---------------- B*.6 conclusion: P P^dag and B^dag B are diagonal with entries |coefficient|^2, so unimodular
    # coefficients give unitaries (P rows: vec p1E11, q2E22, beta E21, gamma E12; B columns: s1E22, r2E11, x1E12, y2E21)
    vec = lambda M: Matrix([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    s1, s1c = conj_pair("S1"); r2, r2c = conj_pair("R2")
    Pm = Matrix.hstack(vec(p1 * E(0, 0)), vec(q2 * E(1, 1)), vec(be * E(1, 0)), vec(ga * E(0, 1))).T
    Pmc = Matrix.hstack(vec(p1c * E(0, 0)), vec(q2c * E(1, 1)), vec(bec * E(1, 0)), vec(gac * E(0, 1))).T
    Bm = Matrix.hstack(vec(s1 * E(1, 1)), vec(r2 * E(0, 0)), vec(x1 * E(0, 1)), vec(y2 * E(1, 0)))
    Bmc = Matrix.hstack(vec(s1c * E(1, 1)), vec(r2c * E(0, 0)), vec(x1c * E(0, 1)), vec(y2c * E(1, 0)))
    out["B6 P P^dag = diag(|p1|^2,|q2|^2,|beta|^2,|gamma|^2)"] = is_zero(Pm * Pmc.T - sp.diag(p1 * p1c, q2 * q2c, be * bec, ga * gac))
    out["B6 B B^dag = diag of |s1|^2,|r2|^2,|x1|^2,|y2|^2 (matrix-unit positions)"] = is_zero(
        Bm * Bmc.T - sp.diag(r2 * r2c, x1 * x1c, y2 * y2c, s1 * s1c))
    # ---------------- A*: (O4),(O2) with rank-one symmetric R_c, T_b
    n1 = Matrix(symbols("u1:3")); n2 = Matrix(symbols("v1:3"))           # n^(1)_K, n^(2)_K
    n1c = Matrix(symbols("u1:3c")); n2c = Matrix(symbols("v1:3c"))
    w = {1: J * n1c, 2: J * n2c}; wc = {1: J * n1, 2: J * n2}            # w_b = J conj(n^(b)_K); conj(w_b) = J n^(b)_K
    rh = {1: conj_pair("rho1"), 2: conj_pair("rho2")}; ta = {1: conj_pair("tau1"), 2: conj_pair("tau2")}
    Rr = {c: rh[c][1] * wc[c] * wc[c].T for c in (1, 2)}                 # conj(R_c)
    Tr = {b: ta[b][1] * wc[b] * wc[b].T for b in (1, 2)}                 # conj(T_b)
    QA = {1: gmat("QA")[0], 2: gmat("QB")[0]}
    ok4 = ok2 = True
    for b, d in itertools.product(range(2), repeat=2):
        lhs = sum(QA[a + 1][b, c] * Rr[c + 1][a, d] for a in range(2) for c in range(2))
        rhs = sum(rh[c][1] * wc[c][d] * sum(QA[a + 1][b, c - 1] * wc[c][a] for a in range(2)) for c in (1, 2))
        ok4 &= is_zero(lhs - rhs)
    for c, d in itertools.product(range(2), repeat=2):
        lhs = sum(QA[a + 1][b, c] * Tr[b + 1][a, d] for a in range(2) for b in range(2))
        rhs = sum(ta[b][1] * wc[b][d] * sum(QA[a + 1][b - 1, c] * wc[b][a] for a in range(2)) for b in (1, 2))
        ok2 &= is_zero(lhs - rhs)
    out["A1 (O4) factorisation with R_c = rho_c w_c w_c^T"] = bool(ok4)
    out["A2 (O2) factorisation with T_b = tau_b w_b w_b^T"] = bool(ok2)
    # A3: the 8 equations (star),(star-star) force Q_a[b,c]=0 (b!=c) and Q_a[b,b] = lambda_b n^(b)_a
    eqs = []
    for b, c in itertools.product(range(2), repeat=2):
        eqs.append(sum(QA[a + 1][b, c] * wc[c + 1][a] for a in range(2)))
        eqs.append(sum(QA[a + 1][b, c] * wc[b + 1][a] for a in range(2)))
    unk = [QA[a][i, j] for a in (1, 2) for i in range(2) for j in range(2)]
    sol = list(sp.linsolve(eqs, unk))
    good = len(sol) == 1
    if good:
        S = dict(zip(unk, sol[0]))
        free = set().union(*[sp.sympify(v).free_symbols for v in sol[0]]) & set(unk)
        good &= len(free) == 2                                            # one free parameter per diagonal slot
        good &= all(sp.simplify(S[QA[a][0, 1]]) == 0 and sp.simplify(S[QA[a][1, 0]]) == 0 for a in (1, 2))
        # diagonal (b,b) entries proportional to n^(b)_a: Q_1[b,b] n^(b)_2 - Q_2[b,b] n^(b)_1 == 0
        good &= sp.simplify(S[QA[1][0, 0]] * n1[1] - S[QA[2][0, 0]] * n1[0]) == 0
        good &= sp.simplify(S[QA[1][1, 1]] * n2[1] - S[QA[2][1, 1]] * n2[0]) == 0
    out["A3 Q_a diagonal with (Q_a[b,b])_a parallel to n^(b)_K (generic n^(1), n^(2))"] = bool(good)
    same = {symbols("v1"): symbols("u1"), symbols("v2"): symbols("u2"), symbols("v1c"): symbols("u1c"),
            symbols("v2c"): symbols("u2c")}
    solc = list(sp.linsolve([sp.sympify(e).subs(same) for e in eqs], unk))
    freec = set().union(*[sp.sympify(v).free_symbols for v in solc[0]]) & set(unk) if solc else set()
    out["control A3: with n^(2) = n^(1) (w_1 || w_2) more than 2 free parameters"] = len(freec) > 2
    out["all_ok"] = all(v for k, v in out.items() if isinstance(v, bool))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "case_algebra_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
