"""Exact controls (sympy, no floating point): conventions, P9, SWAP, identity, thesis U(theta), U_s(2pi/3),
duality/objective mutations.  Run: python -B controls_exact.py  -> writes ../evidence/controls_exact.json
"""
import itertools
import json
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402

N = 9
I9 = sp.eye(N)


def M(L):
    return sp.Matrix(L)


def R(U):
    return M(g.realign(U.tolist()))


def G(U):
    return M(g.ptrans(U.tolist()))


def is_zero(A):
    return all(sp.simplify(x) == 0 for x in A)


def E_of(X):
    """1 - Tr(X X^dag)^2 / 81 for X = U^R or U^Gamma (source eq. 10, d=3)."""
    H = X * X.H
    return sp.nsimplify(sp.simplify(1 - (H * H).trace() / 81))


def ep(U, ES=sp.Rational(8, 9)):
    EU = sp.simplify(1 - ((R(U) * R(U).H) ** 2).trace() / 81)
    EUS = sp.simplify(1 - ((G(U) * G(U).H) ** 2).trace() / 81)
    return sp.simplify((EU + EUS - sp.Rational(8, 9)) / ES), sp.simplify(EU), sp.simplify(EUS)


def props(U):
    return {
        "unitary": is_zero(U * U.H - I9),
        "dual": is_zero(R(U) * R(U).H - I9),
        "tdual": is_zero(G(U) * G(U).H - I9),
    }


def main():
    out = {}
    S = M(g.swap())
    P = M(g.P9())
    Id = I9

    # --- identity checks of the conventions on a generic symbolic matrix ---
    X = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"x{i}_{j}"))
    # (U S)^R = U^Gamma S  (survey/PRR relation used for the T-dual corollary)
    out["identity_(XS)^R == X^G S"] = bool((R(X * S) - G(X) * S) == sp.zeros(N, N))
    # X^R^R = X, X^G^G = X
    out["identity_R_involution"] = bool(R(R(X)) == X)
    out["identity_G_involution"] = bool(G(G(X)) == X)
    # thesis Gamma_1 equals transpose of source Gamma (same singular values)
    out["identity_G1 == (G)^T"] = bool(M(g.ptrans1(X.tolist())) == G(X).T)

    # --- P9, swap, identity ---
    for name, U in [("P9", P), ("SWAP", S), ("identity", Id)]:
        e, EU, EUS = ep(U)
        out[name] = {**props(U), "E(U)": str(EU), "E(US)": str(EUS), "e_p": str(e)}

    # --- P9 S in O9? search local permutations (p1 x p2) P9 (p3 x p4) == P9 S ---
    perms = list(itertools.permutations(range(3)))

    def pm(p):
        A = sp.zeros(3, 3)
        for i in range(3):
            A[p[i], i] = 1
        return A

    target = P * S
    found = None
    for p1, p2, p3, p4 in itertools.product(perms, repeat=4):
        if sp.kronecker_product(pm(p1), pm(p2)) * P * sp.kronecker_product(pm(p3), pm(p4)) == target:
            found = (p1, p2, p3, p4)
            break
    out["P9*S_in_O9_by_local_perms"] = {"found": found is not None, "perms(p1,p2,p3,p4)": found}

    # --- thesis U(theta) symbolic ---
    th = sp.Symbol("theta", real=True)
    c, s = sp.cos(th), sp.sin(th)
    Ut = M(g.U36(c, s))
    out["U36_unitary"] = is_zero(sp.simplify(Ut * Ut.T - I9))
    out["U36_G1_selfadjoint (U^G1 == U)"] = bool(sp.simplify(M(g.ptrans1(Ut.tolist())) - Ut) == sp.zeros(N, N))
    out["U36_tdual"] = is_zero(sp.simplify(G(Ut) * G(Ut).T - I9))
    e_t, EU_t, EUS_t = ep(Ut)
    thesis = sp.Rational(1, 18) * (54 + 59 * c + 22 * sp.cos(2 * th) + 9 * sp.cos(3 * th)) * sp.sin(th / 2) ** 2
    out["U36_ep_symbolic"] = str(sp.simplify(sp.expand_trig(e_t)))
    out["U36_ep_matches_thesis_(3.37)"] = bool(sp.simplify(sp.expand_trig(e_t - thesis)) == 0)

    # --- U_s(2pi/3) := S U(2pi/3) (and U(2pi/3) S) exactly in Q(sqrt3) ---
    c0, s0 = sp.Rational(-1, 2), sp.sqrt(3) / 2
    U0 = M(g.U36(c0, s0))
    for name, U in [("U_s(2pi/3)=S*U36", S * U0), ("U36*S", U0 * S), ("U36(2pi/3)", U0)]:
        e, EU, EUS = ep(U)
        GG = G(U)
        RR = R(U)
        rec = {**props(U), "E(U)": str(EU), "E(US)": str(EUS), "e_p": str(e),
               "rank U^G": int(GG.rank(simplify=True)), "rank U^R": int(RR.rank(simplify=True)),
               "real_orthogonal": bool(all(x.is_real for x in U)) and is_zero(U * U.T - I9)}
        if props(U)["dual"]:
            Gm = GG * GG.H
            rec["eig U^G U^G^dag"] = {str(k): v for k, v in Gm.eigenvals().items()}
            rec["identity 1-e_p == ||GG^dag-I||^2/72"] = bool(
                sp.simplify(1 - e - ((Gm - I9) * (Gm - I9).H).trace() / 72) == 0)
        out[name] = rec
    Us = S * U0
    out["U_s(2pi/3)_self_dual_check (Us^R2 == Us, i.e. realign(Us) relation)"] = {
        "Us^R == Us": bool(sp.simplify(R(Us) - Us) == sp.zeros(N, N)),
        "Us^R == Us^T": bool(sp.simplify(R(Us) - Us.T) == sp.zeros(N, N)),
    }
    out["U_s(2pi/3)_exact_entries"] = [[str(x) for x in row] for row in Us.tolist()]

    # --- mutations ---
    Umut = Us.copy()
    Umut[0, 0] = Umut[0, 0] + sp.Rational(1, 10)
    out["mutation_entry(0,0)+1/10"] = props(Umut)
    # swap two columns of the realignment-irrelevant kind: break duality by a non-local 2x2 rotation on |00>,|01>
    Wrot = sp.eye(N)
    Wrot[0, 0], Wrot[0, 1], Wrot[1, 0], Wrot[1, 1] = sp.Rational(3, 5), -sp.Rational(4, 5), sp.Rational(4, 5), sp.Rational(3, 5)
    Umut2 = Wrot * Us
    e2, _, _ = ep(Umut2)
    out["mutation_left_rotation_00_01"] = {**props(Umut2), "e_p(formula, meaningless off D)": str(e2)}
    e_bad, _, _ = ep(Us, ES=1)
    out["mutation_normalisation_E(S)->1"] = {"e_p": str(e_bad), "differs_from_15/16": bool(e_bad != sp.Rational(15, 16))}
    e_badP, _, _ = ep(P, ES=1)
    out["mutation_normalisation_E(S)->1_on_P9"] = {"e_p": str(e_badP), "flags_P9_not_1": bool(e_badP != 1)}

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "controls_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
