"""Exact (symbolic) check that every relation used in review/LEMMA_R_PROOF.md is literally a block of one of the
biunitarity sums (1)-(4) for the maximal-overlap normal form, and that the sector bookkeeping is right.

phi(a,b,c,d) = U[(c,d),(a,b)]; normal form phi(0000)=1 and phi=0 at points != 0000 with a zero pair in
{12,34,13,24}; X_ad[b,c] = phi(a,b,c,d).  Entries and their complex conjugates are independent symbols, so each
check is a polynomial identity.  Writes ../evidence/relations_exact.json.  Run: python -B relations_exact.py
"""
import itertools
import json
import os

import sympy as sp

R3 = range(3)
K = (1, 2)


def free_point(a, b, c, d):
    if (a, b, c, d) == (0, 0, 0, 0):
        return False
    for (i, j) in ((0, 1), (2, 3), (0, 2), (1, 3)):
        if (a, b, c, d)[i] == 0 and (a, b, c, d)[j] == 0:
            return False
    return True


def main():
    z, zc = {}, {}
    for p in itertools.product(R3, repeat=4):
        if free_point(*p):
            z[p] = sp.Symbol("z%d%d%d%d" % p)
            zc[p] = sp.Symbol("w%d%d%d%d" % p)        # formal conjugate

    def phi(p):
        return 1 if p == (0, 0, 0, 0) else z.get(p, 0)

    def phic(p):
        return 1 if p == (0, 0, 0, 0) else zc.get(p, 0)

    X = {(a, d): sp.Matrix(3, 3, lambda b, c: phi((a, b, c, d))) for a in R3 for d in R3}
    Xc = {(a, d): sp.Matrix(3, 3, lambda b, c: phic((a, b, c, d))) for a in R3 for d in R3}   # entrywise conj
    dag = lambda key: Xc[key].T                                                               # X^dagger

    def S1(a, a2):
        return sp.expand(sum((X[(a, d)] * dag((a2, d)) for d in R3), sp.zeros(3, 3)))

    def S2(a2, a):
        return sp.expand(sum((dag((a2, d)) * X[(a, d)] for d in R3), sp.zeros(3, 3)))

    def S3(d, d2):
        return sp.expand(sum((X[(a, d)] * dag((a, d2)) for a in R3), sp.zeros(3, 3)))

    def S4(d2, d):
        return sp.expand(sum((dag((a, d2)) * X[(a, d)] for a in R3), sp.zeros(3, 3)))

    KK = lambda Mx: Mx.extract([1, 2], [1, 2])
    K0 = lambda Mx: Mx.extract([1, 2], [0])
    Z0K = lambda Mx: Mx.extract([0], [1, 2])

    # sector matrices (2x2, index 0->K label 1, 1->K label 2)
    N = [sp.Matrix(2, 2, lambda b, c: phi((0, b + 1, c + 1, d))) for d in R3]
    Nc = [sp.Matrix(2, 2, lambda b, c: phic((0, b + 1, c + 1, d))) for d in R3]
    Q = [sp.Matrix(2, 2, lambda b, c: phi((a, b + 1, c + 1, 0))) for a in R3]
    Qc = [sp.Matrix(2, 2, lambda b, c: phic((a, b + 1, c + 1, 0))) for a in R3]
    Rm = [sp.Matrix(2, 2, lambda a, d: phi((a + 1, 0, c, d + 1))) for c in R3]      # R_c[a,d], R_0 = x
    Rc = [sp.Matrix(2, 2, lambda a, d: phic((a + 1, 0, c, d + 1))) for c in R3]
    Tm = [sp.Matrix(2, 2, lambda a, d: phi((a + 1, b, 0, d + 1))) for b in R3]      # T_b[a,d], T_0 = R_0
    Tc = [sp.Matrix(2, 2, lambda a, d: phic((a + 1, b, 0, d + 1))) for b in R3]
    Om = {(a, d): sp.Matrix(2, 2, lambda b, c: phi((a, b + 1, c + 1, d))) for a in K for d in K}
    Omc = {(a, d): sp.Matrix(2, 2, lambda b, c: phic((a, b + 1, c + 1, d))) for a in K for d in K}
    Omp = {(b, c): sp.Matrix(2, 2, lambda a, d: phi((a + 1, b, c, d + 1))) for b in K for c in K}
    Ompc = {(b, c): sp.Matrix(2, 2, lambda a, d: phic((a + 1, b, c, d + 1))) for b in K for c in K}
    H = lambda M, Mc: Mc.T                      # dagger from conj matrix

    checks = {}

    def eq(name, lhs, rhs):
        checks[name] = bool(sp.expand(lhs - rhs) == sp.zeros(*lhs.shape))

    # zero pattern bookkeeping: X_00 = 1 (+) N_0, X_0d = 0 (+) N_d, X_a0 = 0 (+) Q_a
    checks["X_00 = 1+N_0 block form"] = X[(0, 0)][0, :].tolist() == [[1, 0, 0]] and X[(0, 0)][:, 0].T.tolist() == [[1, 0, 0]]
    checks["X_0d, X_a0 first row/col zero"] = all(
        all(v == 0 for v in list(X[(0, d)][0, :]) + list(X[(0, d)][:, 0]) + list(X[(d, 0)][0, :]) + list(X[(d, 0)][:, 0]))
        for d in K)
    # (U) unitality blocks
    eq("(U) sum N N^dag = KK block of S1(0,0)", KK(S1(0, 0)), sum((N[d] * H(N[d], Nc[d]) for d in R3), sp.zeros(2, 2)))
    eq("(U) sum N^dag N = KK block of S2(0,0)", KK(S2(0, 0)), sum((H(N[d], Nc[d]) * N[d] for d in R3), sp.zeros(2, 2)))
    eq("(U) N0N0^dag+sum QQ^dag = KK of S3(0,0)", KK(S3(0, 0)), sum((Q[a] * H(Q[a], Qc[a]) for a in R3), sp.zeros(2, 2)))
    eq("(U) N0^dagN0+sum Q^dagQ = KK of S4(0,0)", KK(S4(0, 0)), sum((H(Q[a], Qc[a]) * Q[a] for a in R3), sp.zeros(2, 2)))
    S1aa = sp.Matrix(2, 2, lambda i, j: S1(i + 1, j + 1)[0, 0])
    eq("(U) sum_c R_c R_c^dag = [S1(a,a')]_00", S1aa, sum((Rm[c] * H(Rm[c], Rc[c]) for c in R3), sp.zeros(2, 2)))
    S2aa = sp.Matrix(2, 2, lambda i, j: S2(j + 1, i + 1)[0, 0])     # S2(a',a)[0,0] -> entry (a,a')
    eq("(U) sum_b T_b T_b^dag = [S2(a',a)]_00", S2aa, sum((Tm[b] * H(Tm[b], Tc[b]) for b in R3), sp.zeros(2, 2)))
    S3dd = sp.Matrix(2, 2, lambda i, j: S3(i + 1, j + 1)[0, 0])
    eq("(U) sum_c R_c^T conj(R_c) = [S3(d,d')]_00", S3dd, sum((Rm[c].T * Rc[c] for c in R3), sp.zeros(2, 2)))
    S4dd = sp.Matrix(2, 2, lambda i, j: S4(j + 1, i + 1)[0, 0])
    eq("(U) sum_b T_b^T conj(T_b) = [S4(d',d)]_00 (transposed)", S4dd.T, sum((Tc[b].T * Tm[b] for b in R3), sp.zeros(2, 2)).T.T)
    for a in K:
        eq(f"(alpha) a={a}", KK(S1(0, a)), N[0] * H(Q[a], Qc[a]) + sum((N[d] * H(Om[(a, d)], Omc[(a, d)]) for d in K), sp.zeros(2, 2)))
        eq(f"(gamma) a={a}", KK(S2(0, a)), H(N[0], Nc[0]) * Q[a] + sum((H(N[d], Nc[d]) * Om[(a, d)] for d in K), sp.zeros(2, 2)))
        # (O1): sum_d N_d r_ad^dag ; (O3): sum_d N_d^dag t_ad
        O1 = sp.Matrix(2, 1, lambda b, _: sum(N[d][b, c - 1] * Rc[c][a - 1, d - 1] for c in K for d in K))
        eq(f"(O1) a={a}", K0(S1(0, a)), O1)
        O3 = sp.Matrix(2, 1, lambda c, _: sum(Nc[d][b - 1, c] * Tm[b][a - 1, d - 1] for b in K for d in K))
        eq(f"(O3, conj form) a={a}", K0(S2(0, a)), O3)
    for d in K:
        eq(f"(beta) d={d}", KK(S3(d, 0)), N[d] * H(N[0], Nc[0]) + sum((Om[(a, d)] * H(Q[a], Qc[a]) for a in K), sp.zeros(2, 2)))
        eq(f"(delta) d={d}", KK(S4(0, d)), H(N[0], Nc[0]) * N[d] + sum((H(Q[a], Qc[a]) * Om[(a, d)] for a in K), sp.zeros(2, 2)))
        O4 = sp.Matrix(2, 1, lambda b, _: sum(Q[a][b, c - 1] * Rc[c][a - 1, d - 1] for a in K for c in K))
        eq(f"(O4) d={d}", K0(S3(0, d)), O4)
        O2 = sp.Matrix(2, 1, lambda c, _: sum(Qc[a][b - 1, c] * Tm[b][a - 1, d - 1] for a in K for b in K))
        eq(f"(O2, conj form) d={d}", K0(S4(0, d)), O2)
    # (a,d)-analogues
    for b in K:
        lhs = sp.Matrix(2, 2, lambda i, j: K0(S1(i + 1, j + 1))[b - 1, 0])
        rhs = Tm[b] * H(Rm[0], Rc[0]) + sum((Omp[(b, c)] * H(Rm[c], Rc[c]) for c in K), sp.zeros(2, 2))
        eq(f"(a,d)-analogue T_bR0^dag+sum Om'R^dag, b={b}", lhs, rhs)
        lhs2 = sp.Matrix(2, 2, lambda i, j: Z0K(S3(i + 1, j + 1))[0, b - 1])
        rhs2 = (H(Rm[0], Rc[0]) * Tm[b] + sum((H(Rm[c], Rc[c]) * Omp[(b, c)] for c in K), sp.zeros(2, 2)))
        # S3(d,d')_{0,b} = conj((R0^dag T_b + sum R_c^dag Om'_bc)[d,d']) : compare via formal conjugation swap z<->w
        swap = {**{z[p]: zc[p] for p in z}, **{zc[p]: z[p] for p in z}}
        eq(f"(a,d)-analogue R0^dag T_b + sum R^dag Om' (conj), b={b}", lhs2, rhs2.subs(swap, simultaneous=True))
    # mutation controls: deliberately wrong versions must NOT match (the checker is not vacuous)
    ctrl = {}
    a = 1
    ctrl["(alpha) with N_d -> N_d^T"] = bool(sp.expand(KK(S1(0, a)) - (N[0].T * H(Q[a], Qc[a]) + sum(
        (N[d].T * H(Om[(a, d)], Omc[(a, d)]) for d in K), sp.zeros(2, 2)))) == sp.zeros(2, 2))
    O1bad = sp.Matrix(2, 1, lambda b, _: sum(N[d][b, c - 1] * Rm[c][a - 1, d - 1] for c in K for d in K))
    ctrl["(O1) without complex conjugation"] = bool(sp.expand(K0(S1(0, a)) - O1bad) == sp.zeros(2, 1))
    ctrl["(U) S1(0,0) KK block vs sum N^dag N (wrong order)"] = bool(sp.expand(
        KK(S1(0, 0)) - sum((H(N[d], Nc[d]) * N[d] for d in R3), sp.zeros(2, 2))) == sp.zeros(2, 2))
    out = {"checks": checks, "mutation_controls_match (must all be false)": ctrl,
           "all_ok": all(checks.values()) and not any(ctrl.values()), "n_free_entries": len(z)}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "relations_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
