"""EXPLORATORY (not a frozen target, no claim): general-k form of the chi8 route, with the case (k, d) = (5, 12).
Checks only identities and constants; no solver search. Writes ./check_general_k.json.

General k (cells [k]^2, allowed pairs p != r and q != s, doubly stochastic M with sum m = k):
  * Lemma A analogue: V_mu = ((d-1)/k) sum m ln m + (1-d) ln k + (d/2) ln d + sum_e e^(mu_u+mu_v-1) - (d/k) sum mu m.
  * beta = (d-1)/d cancels the entropy; optimising c gives U = (1-d) ln k + (d/2) ln(2 E_beta), E_beta = sum (m_u m_v)^beta.
  * Row reduction: 2E = (sum f)^2 - sum R^2 - sum C^2 + sum f^2 <= (k-2) sum R^2 + sum f^2.
  * Row function F_k = ((k-2)/2) S^2 + Q/2 = (k (k-1)^2 / 2) ||T_(1/(k-1)) g||^2 on the uniform k-point space.
  * D-SC: alpha = (1 - 2/k)/ln(k-1); with t = ln(k-1), 4 alpha t = 4 - 8/k; condition d - 1 <= e^(4 - 8/k).
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


def identities():
    out = {}
    for k in (3, 4, 5, 6):
        F = sp.Matrix(k, k, lambda i, j: sp.Symbol(f"f{i}_{j}"))
        E2 = sum(F[p, q] * F[r, s] for p in range(k) for q in range(k) for r in range(k) for s in range(k) if p != r and q != s)
        tot = sum(F)
        R = [sum(F[p, :]) for p in range(k)]
        C = [sum(F[:, q]) for q in range(k)]
        ie = tot ** 2 - sum(x ** 2 for x in R) - sum(x ** 2 for x in C) + sum(x ** 2 for x in F)
        cert = (sum(x ** 2 for x in C) - tot ** 2 / k) + sp.Rational(k - 1, k) * (k * sum(x ** 2 for x in R) - sum(R) ** 2)
        g = sp.symbols(f"g0:{k}")
        Eg = sum(g) / k
        T = [Eg + sp.Rational(1, k - 1) * (gi - Eg) for gi in g]
        Fk = sp.Rational(k - 2, 2) * sum(g) ** 2 + sum(gi ** 2 for gi in g) / 2
        out[f"k={k}"] = {
            "inclusion-exclusion 2E == (sum f)^2 - sum R^2 - sum C^2 + sum f^2": sp.expand(E2 - ie) == 0,
            "certificate (k-2) sum R^2 + sum f^2 - 2E == [sum C^2 - (sum f)^2/k] + ((k-1)/k)[k sum R^2 - (sum R)^2]":
                sp.expand((k - 2) * sum(x ** 2 for x in R) + sum(x ** 2 for x in F) - ie - cert) == 0,
            "F_k == (k (k-1)^2/2) ||T_(1/(k-1)) g||^2": sp.expand(Fk - sp.Rational(k * (k - 1) ** 2, 2) * sum(t ** 2 for t in T) / k) == 0,
        }
    d, k, E, c = sp.symbols("d k E c", positive=True)
    V = (1 - d) * sp.log(k) + d / 2 * sp.log(d) + sp.exp(2 * c - 1) * E - d * c
    cst = sp.solve(sp.diff(V, c), c)[0]
    out["general: min_c V == (1-d) ln k + (d/2) ln(2E)"] = sp.simplify(
        sp.expand_log(V.subs(c, cst) - ((1 - d) * sp.log(k) + d / 2 * sp.log(2 * E)), force=True)) == 0
    beta = (d - 1) / d
    EJ = k ** 2 * (k - 1) ** 2 / 2 * k ** (-2 * beta)
    UJ = (1 - d) * sp.log(k) + d / 2 * sp.log(2 * EJ)
    out["general: U(J) == (2-d) ln k + d ln(k-1) (exponent of (EY)^2)"] = sp.simplify(
        sp.expand_log(UJ - ((2 - d) * sp.log(k) + d * sp.log(k - 1)), force=True)) == 0
    alpha = (1 - 2 / k) / sp.log(k - 1)
    out["general: 4 alpha ln(k-1) == 4 - 8/k"] = sp.simplify(4 * alpha * sp.log(k - 1) - (4 - 8 / k)) == 0
    out["general: entropy cancellation (d-1)/k == (d/k) beta"] = sp.simplify((d - 1) / k - d / k * beta) == 0
    return out


def case_5_12():
    k, d = 5, 12
    out = {"label": "[INFERENCE] exploratory; not a frozen target"}
    beta = Fr(d - 1, d)
    out["beta"] = str(beta)
    out["(H1) k^2-2k-d+2"] = k * k - 2 * k - d + 2
    out["series ratio (d-1)/(k-1)^2"] = str(Fr(d - 1, (k - 1) ** 2))
    out["EY growth k(1-1/k)^(d/2)"] = str(Fr(k) * Fr(k - 1, k) ** (d // 2))
    out["Molloy-Reed q = 4: 4 (3/4)^6"] = str(4 * Fr(3, 4) ** 6)
    out["exact checks"] = {
        "(H1) > 0": k * k - 2 * k - d + 2 > 0,
        "series ratio < 1": Fr(d - 1, (k - 1) ** 2) < 1,
        "EY growth > 1": Fr(k) * Fr(k - 1, k) ** (d // 2) > 1,
        "Molloy-Reed 729/1024 < 1": 4 * Fr(3, 4) ** 6 == Fr(729, 1024) and Fr(729, 1024) < 1,
    }
    # hypercontractive condition: 11 <= e^(12/5) <=> 11^5 <= e^12; exact lower bound for e^12 by a partial sum
    N = 0
    s = Fr(0)
    while s <= 11 ** 5:
        s += Fr(12 ** N, factorial(N))
        N += 1
    out["exact: partial sum of e^12 = sum_{j<N} 12^j/j! exceeds 11^5 = 161051 at N"] = N
    out["exact: e^12 > 11^5 (so ln 11 < 12/5)"] = s > 11 ** 5
    l4, l11 = arb(4).log(), arb(11).log()
    a = (-(arb(5) * l4 / 12) * l11).exp()
    gap = a * a - arb(1) / 16
    kappa = arb(121) / 18 * gap
    E0 = 200 * (-(arb(11) / 6) * arb(5).log()).exp()
    C12 = 6 * kappa / E0
    out["alpha_LS = 3/(5 ln 4)"] = str(arb(3) / (5 * l4))
    out["a = 11^(-5 ln4/12)"] = str(a)
    out["a > 1/4 (certain)"] = bool(a > arb(1) / 4)
    out["a^2 - 1/16"] = str(gap)
    out["kappa = (121/18)(a^2 - 1/16)"] = str(kappa)
    out["E0 = E_beta(J) = 200 * 5^(-11/6)"] = str(E0)
    out["C_12 = 6 kappa / E0"] = str(C12)
    out["C_12 > 0 (certain)"] = bool(C12 > 0)
    out["kappa algebra: ((k-1)^2/2) beta^2 == 121/18"] = Fr((k - 1) ** 2, 2) * beta ** 2 == Fr(121, 18)
    # KPW / NPG arithmetic at d = 12
    l5 = arb(5).log()
    out["KPW at d = 12: 8 ln4 < 12 < 10 ln5 (KPW's k = 6, window {5,6})"] = bool(8 * l4 < 12) and bool(12 < 10 * l5)
    out["KPW exact clause d > 9 ln5 fails (9 ln5 > 12)"] = bool(9 * l5 > 12)
    lk = 2 * arb(4) ** 3 / (5 * 3) * l4
    out["NPG l_5 = 2*4^3 ln4/15"] = str(lk)
    out["NPG l_5 < 12 (d = 12 outside NPG/AN(12))"] = bool(lk < 12)
    # control: d = 13 fails the route's condition: 12 > e^(12/5)
    out["control d = 13: e^(12/5) < 12 (certain), condition fails"] = bool((arb(12) / 5).exp() < 12)
    return out


def table():
    rows = []
    for k in range(3, 13):
        Dk = 1 + (4 - arb(8) / k).exp()
        dmax = int(math.floor(float(Dk.mid())))
        # certify floor: dmax <= Dk < dmax + 1
        cert = bool(Dk >= dmax) and bool(Dk < dmax + 1)
        kpw = 2 * (k - 1) * arb(k - 1).log()
        npg = 2 * arb(k - 1) ** 3 / (k * (k - 2)) * arb(k - 1).log() if k >= 3 else None
        rows.append({"k": k, "1 + e^(4-8/k)": float(Dk.mid()), "route reaches d <=": dmax, "floor certified": cert,
                     "KPW/AN range d < 2(k-1)ln(k-1)": float(kpw.mid()), "NPG l_k": float(npg.mid()),
                     "route extends beyond NPG": bool(dmax > npg)})
    return rows


def float_sanity_k5():
    rng = np.random.default_rng(512)
    k, beta = 5, 11 / 12
    cells = [(p, q) for p in range(k) for q in range(k)]
    adj = np.array([[1.0 if (u[0] != v[0] and u[1] != v[1]) else 0.0 for v in cells] for u in cells])
    J = np.full((k, k), 1 / k)
    yJ = J.reshape(-1) ** beta
    EJ = 0.5 * yJ @ (adj @ yJ)
    worst = -1e9
    for _ in range(3000):
        M = np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(k, k)))
        for _ in range(500):
            M = M / M.sum(axis=1, keepdims=True)
            M = M / M.sum(axis=0, keepdims=True)
        y = M.reshape(-1) ** beta
        worst = max(worst, (0.5 * y @ (adj @ y) - EJ) / np.sum((M - J) ** 2))
    for t in np.linspace(0.01, 1, 100):
        M = (1 - t) * J + t * np.eye(k)
        y = M.reshape(-1) ** beta
        worst = max(worst, (0.5 * y @ (adj @ y) - EJ) / np.sum((M - J) ** 2))
    return {"note": "floats; not evidence", "E0 (float)": EJ,
            "max (E_beta(M) - E_beta(J))/|M-J|^2 over 3000 random 5x5 DS + (1-t)J + tI (theory: <= -kappa ~ -0.00104)": worst}


def main():
    out = {"note": "[INFERENCE] exploratory general-k check; no claim; identities exact, constants arb, sanity floats"}
    out["identities"] = identities()
    out["case (k,d) = (5,12)"] = case_5_12()
    out["route range by k (rigorous floor)"] = table()
    out["float sanity k = 5, d = 12"] = float_sanity_k5()
    with open(os.path.join(HERE, "check_general_k.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
