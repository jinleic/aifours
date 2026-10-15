"""Claims C3-C4: the literal two-function reading of the conjecture in the class P = D_t + p(D_x).

    (1)  P F.G = 0,  D_x P F.G = 0          (2)  P F.G = 0,  D_y P F.G = 0

One-soliton data: P(k_i) a_i + P(-k_i) b_i = 0 with a_i, b_i the amplitudes of e^{eta_i} in F and G.
For odd p both amplitudes are free; otherwise a soliton is of F type (b_i = 0, w_i = -p(k_i)) or of
G type (a_i = 0, w_i = p(-k_i)).  The generic three-soliton test asks that the recursively determined
exponential polynomial (hirota_ns.two_function_solution) solves the system identically.

Part A  deg p <= 3 passes, symbolically in every parameter (k_i, l_i, amplitudes, c_j):
        A1 p = c1 k + c3 k^3 with two free amplitudes per soliton, for (1) and (2);
        A2 p = c1 k + c2 k^2 + c3 k^3 and p = c1 k + c2 k^2, every F/G type pattern, for (1) and (2).
Part B  abstract lemma: for ANY P and ANY linear odd multiplier M (M = D_x or D_y), solitons 1,2 of F type and
        3 of G type, the n = (2,1,1) residual of the first equation equals
            a1^2 a2 b3 M(k3) Phi / (M(k123) P(-k123) P(-k13)),
            Phi = P(k2-k3) P(k1-k2-k3) P(-k1-k3) + P(k1-k3) P(k2-k1-k3) P(-k2-k3),
        checked with every value P(e.k) an independent symbol (only the dispersion relations imposed).
Part C  monomials p = k^d at (k1, k2, k3) = (1, 2, -4) (types F, F, G): Phi_d = 0 for d = 2, 3 and Phi_d < 0 for
        4 <= d <= 60 (exact integers); all nondegeneracy conditions hold; engine cross-check of the closed
        form for d = 4..9 for (1) and for (2) with l = (1, 3, 7).  (d > 60: inequality in RESULTS.md.)
Part D  lower-order terms do not help (illustration of the scaling lemma; the proof is in RESULTS.md).
Run: python two_function_3ss.py     (deterministic; a few minutes)
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.fields import field

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hirota_ns as H  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "results"


# ------------------------------------------------------------------------------------------- Part A
def part_A(report):
    names = []
    for i in (1, 2, 3):
        names += [f"k{i}", f"l{i}", f"a{i}", f"b{i}"]
    names += ["c1", "c2", "c3"]
    K, *gens = field(",".join(names), QQ)
    g = dict(zip(names, gens))
    c1, c2, c3 = g["c1"], g["c2"], g["c3"]
    out = {}

    def run(pcoef, mult, types):
        P = {(0, 0, 1): K.one}
        for j, cj in pcoef.items():
            P[(j, 0, 0)] = cj
        M = {(0, 1, 0): K.one} if mult == "Dy" else {(1, 0, 0): K.one}
        Bs = [P, H.bmul(M, P)]
        waves, a, b = [], [], []
        for i, typ in zip((1, 2, 3), types):
            k = g[f"k{i}"]
            l = g[f"l{i}"] if mult == "Dy" else K.zero
            pk = sum((cj * k**j for j, cj in pcoef.items()), K.zero)
            pmk = sum((cj * (-k) ** j for j, cj in pcoef.items()), K.zero)
            w = -pk if typ in ("FG", "F") else pmk
            waves.append((k, l, w))
            a.append(g[f"a{i}"] if typ in ("FG", "F") else K.zero)
            b.append(g[f"b{i}"] if typ in ("FG", "G") else K.zero)
        F, G = H.two_function_solution(Bs, waves, a, b)
        res = H.residuals(Bs, waves, F, G)
        return len(res)

    t0 = time.time()
    for mult in ("Dx", "Dy"):
        n = run({1: c1, 3: c3}, mult, ("FG", "FG", "FG"))
        out[f"A1 odd cubic, two amplitudes, {mult}"] = n
        for pat in itertools.product("FG", repeat=3):
            n1 = run({1: c1, 2: c2, 3: c3}, mult, pat)
            n2 = run({1: c1, 2: c2}, mult, pat)
            out[f"A2 c1k+c2k^2+c3k^3 pattern {''.join(pat)}, {mult}"] = n1
            out[f"A2 c1k+c2k^2 pattern {''.join(pat)}, {mult}"] = n2
        # explicit specialisations (guards against hidden denominators vanishing at special c's)
        for lab, pc in (("k^3", {3: 1}), ("k^3-2k", {3: 1, 1: -2}), ("k^2", {2: 1}), ("k^3+k^2", {3: 1, 2: 1}),
                        ("3k^2+k", {2: 3, 1: 1})):
            pcK = {j: K.one * c for j, c in pc.items()}
            pats = [("FG",) * 3] if all(j % 2 for j in pc) else list(itertools.product("FG", repeat=3))
            for pat in pats:
                out[f"A3 p={lab} pattern {''.join(x[0] for x in pat) if len(pats) > 1 else 'two-amp'},"
                    f" {mult}"] = run(pcK, mult, pat)
    bad = {k: v for k, v in out.items() if v != 0}
    print(f"Part A: {len(out)} symbolic three-soliton identities, nonzero residual sets: {bad if bad else 'none'}"
          f"  [{time.time() - t0:.1f}s]")
    report["partA_nonzero_residual_counts"] = out
    return not bad


# ------------------------------------------------------------------------------------------- Part B
def part_B(report):
    """Abstract FFG lemma: every value P(eps.kappa) is an independent symbol."""
    eps_all = [e for e in itertools.product((-1, 0, 1), repeat=3) if any(e)]
    zero_P = {(1, 0, 0), (0, 1, 0), (0, 0, -1)}  # dispersion: P(k1) = P(k2) = 0 (F type), P(-k3) = 0 (G type)
    sym_names = {e: "P_" + "".join({-1: "m", 0: "0", 1: "p"}[x] for x in e) for e in eps_all if e not in zero_P}
    names = list(sym_names.values()) + ["m1", "m2", "m3", "a1", "a2", "b3"]
    K, *gens = field(",".join(names), QQ)
    g = dict(zip(names, gens))
    m = [g["m1"], g["m2"], g["m3"]]

    def eps_of(A, C):
        return tuple((1 if A >> i & 1 else 0) - (1 if C >> i & 1 else 0) for i in range(3))

    def Pval(e):
        if not any(e) or e in zero_P:
            return K.zero
        return g[sym_names[e]]

    def B1(A, C):
        return Pval(eps_of(A, C))

    def B2(A, C):
        e = eps_of(A, C)
        return sum((ei * mi for ei, mi in zip(e, m)), K.zero) * Pval(e)

    dummy = [(K.one, K.one, K.one)] * 3  # kappa table is not used by callable symbols
    a = [g["a1"], g["a2"], K.zero]
    b = [K.zero, K.zero, g["b3"]]
    F, G = H.two_function_solution([B1, B2], dummy, a, b)
    kap = H._kappa_table(dummy)
    r211 = H.coefficient(B1, kap, F, G, (2, 1, 1))
    P = lambda *e: Pval(tuple(e))  # noqa: E731
    Phi = (P(0, 1, -1) * P(1, -1, -1) * P(-1, 0, -1) + P(1, 0, -1) * P(-1, 1, -1) * P(0, -1, -1))
    closed = g["a1"] ** 2 * g["a2"] * g["b3"] * m[2] * Phi / ((m[0] + m[1] + m[2]) * P(-1, -1, -1) * P(-1, 0, -1))
    ok = (r211 - closed) == 0
    # all other residual coefficients with a 2-entry, for the record (they involve M non-trivially)
    res = H.residuals([B1, B2], dummy, F, G)
    print(f"Part B: abstract FFG lemma (n=(2,1,1) residual == closed form): {ok};"
          f" residual coefficient sets present at n = {sorted(res)}")
    report["partB_closed_form_matches"] = ok
    report["partB_nonzero_n"] = [list(n) for n in sorted(res)]
    return ok


# ------------------------------------------------------------------------------------------- Part C
def monomial_values(d, ks=(1, 2, -4), types="FFG"):
    w = []
    for k, typ in zip(ks, types):
        w.append(-(k**d) if typ == "F" else (-k) ** d)

    def P(*e):
        return sum(ei * wi for ei, wi in zip(e, w)) + sum(ei * ki for ei, ki in zip(e, ks)) ** d
    return P


def Phi_d(d):
    P = monomial_values(d)
    return P(0, 1, -1) * P(1, -1, -1) * P(-1, 0, -1) + P(1, 0, -1) * P(-1, 1, -1) * P(0, -1, -1)


def part_C(report):
    rows = {}
    all_ok = True
    for d in range(2, 61):
        P = monomial_values(d)
        phi = Phi_d(d)
        nondeg = all(v != 0 for v in (P(1, 1, 0), P(-1, -1, 0), P(1, 0, 1), P(-1, 0, -1), P(0, 1, 1),
                                         P(0, -1, -1), P(1, 1, 1), P(-1, -1, -1)))
        expected_zero = d in (2, 3)
        ok = nondeg and ((phi == 0) if expected_zero else (phi < 0))
        all_ok &= ok
        if d <= 12:
            rows[d] = str(phi)
    # inequality used for d >= 30 (see RESULTS.md): (1 - 2*0.8^d)^2 >= 2*0.96^d, checked exactly at d = 30
    d0 = 30
    lhs = (1 - 2 * Fr(4, 5) ** d0) ** 2
    rhs = 2 * Fr(24, 25) ** d0
    ineq_ok = lhs >= rhs
    print(f"Part C: Phi_d (d=2..60) zero exactly for d=2,3, negative for 4<=d<=60, nondegenerate: {all_ok};"
          f" tail inequality at d=30: {ineq_ok}")
    print("        Phi_d for d=2..12:", rows)
    report["partC_Phi_d_small"] = rows
    report["partC_all_checks_d_le_60"] = all_ok
    report["partC_tail_inequality_d30"] = ineq_ok

    # engine cross-check of the closed form for (1) and (2)
    Dx, Dy, Dt = H.DX, H.DY, H.DT
    cross = {}
    for d in range(4, 10):
        Pexpr = Dt + Dx**d
        ks = [Fr(1), Fr(2), Fr(-4)]
        ls = [Fr(1), Fr(3), Fr(7)]
        w = [-(ks[0] ** d), -(ks[1] ** d), (-ks[2]) ** d]
        for mult, M in (("(1)", Dx), ("(2)", Dy)):
            Bs = [H.bpoly(Pexpr), H.bpoly(M * Pexpr)]
            lv = ls if mult == "(2)" else [Fr(0)] * 3
            waves = [(ks[i], lv[i], w[i]) for i in range(3)]
            F, G = H.two_function_solution(Bs, waves, [Fr(1), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)])
            kap = H._kappa_table(waves)
            r = H.coefficient(Bs[0], kap, F, G, (2, 1, 1))
            m3 = ks[2] if mult == "(1)" else ls[2]
            m123 = sum(ks) if mult == "(1)" else sum(ls)
            P = monomial_values(d)
            closed = Fr(m3) * Phi_d(d) / (m123 * P(-1, -1, -1) * P(-1, 0, -1))
            cross[f"d={d} {mult}"] = (r == closed and r != 0)
    print("        engine cross-check (closed form == engine residual != 0):", all(cross.values()))
    report["partC_engine_crosscheck"] = cross
    return all_ok and ineq_ok and all(cross.values())


# ------------------------------------------------------------------------------------------- Part D
def part_D(report):
    Dx, Dy, Dt = H.DX, H.DY, H.DT
    out = {}
    for label, pc in (("k^5+k^2", {5: 1, 2: 1}), ("k^4+k^3", {4: 1, 3: 1}), ("k^6-3k^2+k", {6: 1, 2: -3, 1: 1}),
                      ("2k^5-k^3+k", {5: 2, 3: -1, 1: 1}), ("k^7+k^5+k^3", {7: 1, 5: 1, 3: 1})):
        Pexpr = Dt + sum(c * Dx**j for j, c in pc.items())
        for mult, M in (("(1)", Dx), ("(2)", Dy)):
            Bs = [H.bpoly(Pexpr), H.bpoly(M * Pexpr)]
            vals = []
            for s in (1, 2, 5, 20):
                ks = [Fr(s), Fr(2 * s), Fr(-4 * s)]
                w = [-sum(Fr(c) * k**j for j, c in pc.items()) for k in ks[:2]]
                w.append(sum(Fr(c) * (-ks[2]) ** j for j, c in pc.items()))
                lv = [Fr(1), Fr(3), Fr(7)] if mult == "(2)" else [Fr(0)] * 3
                waves = [(ks[i], lv[i], w[i]) for i in range(3)]
                try:
                    F, G = H.two_function_solution(Bs, waves, [Fr(1), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)])
                    res = H.residuals(Bs, waves, F, G)
                    vals.append(len(res))
                except H.DegenerateSystem:
                    vals.append("degenerate")
            out[f"{label} {mult}"] = vals
    print("Part D: number of nonzero residual coefficients at s*(1,2,-4), s = 1,2,5,20:", out)
    report["partD"] = out
    return all(all(v != 0 and v != "degenerate" for v in vals) for vals in out.values())


def main():
    OUT.mkdir(exist_ok=True)
    report = {}
    okA = part_A(report)
    okB = part_B(report)
    okC = part_C(report)
    okD = part_D(report)
    report["summary"] = {"A_cubic_passes": okA, "B_abstract_lemma": okB, "C_monomials_fail_d_ge_4": okC,
                         "D_lower_order_examples_fail": okD}
    print("SUMMARY:", report["summary"])
    (OUT / "two_function_3ss.json").write_text(json.dumps(report, indent=2))
    print("wrote", OUT / "two_function_3ss.json")


if __name__ == "__main__":
    main()
