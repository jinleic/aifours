#!/usr/bin/env python3
"""large_t_gen.py: structured exclusion of (t, e) for large t and any e >= 0 (lane ame46-support).

As large_t_e0.py, but for general e (review/LEMMAS; README 0.2):
 1. Profiles: positive deficits d_{i,a} >= 2 summing to h = 36 - t, with max_a d_{i,a} <= min_{j != i} |V_j|.
 2. N-only CNF on prod V_i:
    - every line meets N in 0 or >= 2 points;
    - in slice (i, a), the number of hole lines (a, b) equals d_{i,a};
    - |N| = 2h + e;
    - combinatorial orthogonality for rows and for columns of each reshaping (Lemma 5).
    No phase clauses. All solutions are enumerated up to the CNF's symmetry group by orbit blocking, and the final
    UNSAT is proved with CaDiCaL --lrat and checked by code/lratcheck.
 3. Each orbit representative is tested with exact necessary conditions, in order; any failure excludes the orbit,
    with the reason recorded:
    (a) components: each connected component of each reshaping restricted to N must be square with at least 2 rows,
        every row and column must have >= 2 entries, e_K must not be 1, and the component must be fully
        indecomposable (no k' rows supported inside k' columns, 0 < k' < k; Lemma 6 applied to a unitary block);
    (b) moduli: an exact rational LP (sympy) must admit m > 0 with every hole-line sum equal to 1 (Lemma 1);
    (c) 2x2 phases: the congruences of Lemma 10 on the 2x2 components must be consistent over R/2piZ (exact HNF);
    (d) classical completion: T avoids the hole lines and meets every other line exactly once; CaDiCaL --lrat,
        checked.
    A representative that passes (a)-(c) and has a satisfiable completion is reported as an OPEN CANDIDATE. Its
    unitary realizability with components larger than 2x2 is not decided here.
Output: evidence/large_t_gen_t<t>_e<e>.json.
"""
import argparse
import itertools
import json
import os
import subprocess
import sys

import ame_e0_cnf as base
import large_t_e0 as lte
import phase_check as pc

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "explore", "large_t_gen")


class SmallGen(lte.Small):
    def build_gen(self, e, h):
        V, d = self.V, self.d
        for (i, j) in lte.PAIRS:
            for a in V[i]:
                for b in V[j]:
                    mem = [x for x in self.points if x[i] == a and x[j] == b]
                    ns = [self.var[x] for x in mem]
                    v = self.new()
                    self.hl = getattr(self, "hl", {})
                    self.hl[(i, j, a, b)] = v
                    self.cl.append([-v] + ns)
                    for nx in ns:
                        self.cl.append([-nx, v])
                    for x in mem:
                        self.cl.append([-self.var[x]] + [self.var[y] for y in mem if y != x])
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                P = (min(i, j), max(i, j))
                for a in V[i]:
                    lits = [self.hl[(P[0], P[1], a, b) if P[0] == i else (P[0], P[1], b, a)] for b in V[j]]
                    self.eqk(lits, d[i][a])
        self.eqk([self.var[x] for x in self.points], 2 * h + e)
        for rows, cols in base.RESHAPINGS:
            for A, B in ((rows, cols), (cols, rows)):
                av = list(itertools.product(V[A[0]], V[A[1]]))
                bv = list(itertools.product(V[B[0]], V[B[1]]))

                def el(r, c):
                    x = [0] * 4
                    x[A[0]], x[A[1]] = r
                    x[B[0]], x[B[1]] = c
                    return tuple(x)
                for r1, r2 in itertools.combinations(av, 2):
                    aux = {}
                    for c in bv:
                        a_ = self.new()
                        aux[c] = a_
                        self.cl.append([-a_, self.var[el(r1, c)]])
                        self.cl.append([-a_, self.var[el(r2, c)]])
                    for c in bv:
                        self.cl.append([-self.var[el(r1, c)], -self.var[el(r2, c)]] +
                                       [aux[c2] for c2 in bv if c2 != c])


def component_checks(N):
    """Exact combinatorial necessary conditions (a). Returns (ok, reason)."""
    S = set(N)
    for k, (rows, cols) in enumerate(pc.RESHAPINGS):
        for rs, cs, elems in pc.components(S, rows, cols):
            if len(rs) != len(cs):
                return False, "reshaping %d: component not square %dx%d" % (k, len(rs), len(cs))
            kk = len(rs)
            if kk < 2:
                return False, "reshaping %d: 1x1 component inside N" % k
            rsup = {r: {tuple(x[i] for i in cols) for x in elems if tuple(x[i] for i in rows) == r} for r in rs}
            csup = {c: {tuple(x[i] for i in rows) for x in elems if tuple(x[i] for i in cols) == c} for c in cs}
            if any(len(v) < 2 for v in rsup.values()) or any(len(v) < 2 for v in csup.values()):
                return False, "reshaping %d: line with a single entry" % k
            if len(elems) - 2 * kk == 1:
                return False, "reshaping %d: e_K = 1" % k
            for kp in range(1, kk):
                for sub in itertools.combinations(rs, kp):
                    if len(set().union(*(rsup[r] for r in sub))) <= kp:
                        return False, "reshaping %d: %d rows supported in %d columns (not fully indecomposable)" % (
                            k, kp, kp)
    return True, "ok"


def moduli_lp(N):
    """Exact LP: max eps s.t. hole-line sums of m equal 1 and m_x >= eps. Returns the exact optimum."""
    from sympy import Rational, symbols
    from sympy.solvers.simplex import lpmax
    S = sorted(set(N))
    m = {x: symbols("m%d" % k) for k, x in enumerate(S)}
    eps = symbols("eps")
    cons = []
    for P in lte.PAIRS:
        lines = {}
        for x in S:
            lines.setdefault(tuple(x[i] for i in P), []).append(x)
        for L in lines.values():
            cons.append(sum(m[x] for x in L) <= 1)
            cons.append(sum(m[x] for x in L) >= 1)
    for x in S:
        cons.append(m[x] - eps >= 0)
    cons.append(eps <= 1)
    try:
        opt, sol = lpmax(eps, cons)
    except Exception as exc:          # sympy raises InfeasibleLPError when the equalities have no solution m >= eps
        if type(exc).__name__ == "InfeasibleLPError":
            return -1
        raise
    return opt


def hole_lines(N):
    S = sorted(set(N))
    lines = []
    for P in lte.PAIRS:
        d = {}
        for x in S:
            d.setdefault(tuple(x[i] for i in P), []).append(x)
        lines.extend((P, z, tuple(L)) for z, L in sorted(d.items()))
    return S, lines


def verify_moduli_certificate(N, w):
    """Exact check of a Stiemke certificate against positive moduli. A is the incidence matrix of the hole lines of N
    (rows: lines, columns: points), b = 1 (every hole-line sum of m_x = 36|psi_x|^2 is 1; L42-1, no officer on hole
    lines). Accept iff A^T w >= 0 componentwise, b^T w <= 0, and (A^T w != 0 or b^T w < 0).
    Soundness: for m > 0 (every point of N is in the support) with A m = b, if A^T w != 0 then
    m^T A^T w > 0 >= b^T w = m^T A^T w; if A^T w = 0 then b^T w = m^T A^T w = 0, contradicting b^T w < 0."""
    from fractions import Fraction
    S, lines = hole_lines(N)
    w = [Fraction(v) for v in w]
    ATw = [sum(w[l] for l, (_, _, L) in enumerate(lines) if x in L) for x in S]
    bw = sum(w)
    return all(v >= 0 for v in ATw) and bw <= 0 and (any(v != 0 for v in ATw) or bw < 0)


def moduli_certificate(N):
    """Search (scipy HiGHS, floats) for a Stiemke certificate w, rationalise it, then verify it EXACTLY with
    verify_moduli_certificate. Returns None when no candidate is found (no exclusion)."""
    from fractions import Fraction
    import numpy as np
    from scipy.optimize import linprog
    S, lines = hole_lines(N)
    nL, nx = len(lines), len(S)
    pos = {x: k for k, x in enumerate(S)}
    A = np.zeros((nL, nx))
    for l, (_, _, L) in enumerate(lines):
        for x in L:
            A[l, pos[x]] = 1.0
    # variables w (nL): maximise sum_x (A^T w)_x - b^T w subject to A^T w >= 0, b^T w <= 0, -1 <= w <= 1.
    # The optimum is > 0 iff a certificate exists (the objective is a sum of non-negative terms that are not all 0).
    c = -(A.sum(axis=1) - 1.0)
    A_ub = np.vstack([-A.T, np.ones((1, nL))])
    b_ub = np.zeros(nx + 1)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(-1, 1)] * nL, method="highs")
    if not res.success or -res.fun < 1e-9:
        return None
    w = [Fraction(v).limit_denominator(10 ** 6) for v in res.x]
    return {"verified": bool(verify_moduli_certificate(N, w)), "w": [str(v) for v in w],
            "lines": ["%d%d:%d%d" % (P[0] + 1, P[1] + 1, z[0], z[1]) for P, z, _ in lines]}


def run(t, e):
    h = 36 - t
    os.makedirs(OUT, exist_ok=True)
    report = {"t": t, "e": e, "h": h, "profiles": []}
    for prof in lte.profiles(h):
        if sum(len(p) for p in prof) == 0:
            continue
        tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)
        S = SmallGen(prof)
        if 2 * h + e > len(S.points):
            report["profiles"].append({"profile": [list(p) for p in prof], "skipped": "2h+e exceeds product space",
                                       "orbits": 0, "final_unsat_lrat_verified": True, "reps": []})
            continue
        S.build_gen(e, h)
        G = S.group()
        blocks, reps = [], []
        while True:
            path = os.path.join(OUT, tag + ".cnf")
            S.write(path, blocks)
            st, model = lte.solve(path)
            if st == 20:
                lrat = os.path.join(OUT, tag + ".final.lrat")
                lte.solve(path, lrat)
                ok, msg = lte.lrat_check(path, lrat)
                break
            if st != 10:
                raise RuntimeError("solver status %d" % st)
            N = [x for x in S.points if S.var[x] in model]
            orbit = {frozenset(S.apply(g, x) for x in N) for g in G}
            for img in orbit:
                blocks.append([-S.var[x] for x in sorted(img)])
            reps.append({"N": N, "orbit_size": len(orbit)})
        prof_rep = {"profile": [list(p) for p in prof], "orbits": len(reps), "group_order": len(G),
                    "final_unsat_lrat_verified": ok, "lrat_msg": msg, "reps": []}
        for k, rep in enumerate(reps):
            N = rep["N"]
            entry = {"N": ["".join(map(str, x)) for x in N], "orbit_size": rep["orbit_size"]}
            okc, why = component_checks(N)
            entry["components_ok"], entry["components_reason"] = okc, why
            if okc:
                # Moduli: exclusion only by an exactly verified certificate w (rational) with A^T w >= 0,
                # b^T w <= 0, not all zero (A = hole-line incidence, b = 1). Soundness: for m > 0 with A m = b,
                # 0 >= b^T w = m^T (A^T w) >= 0 forces A^T w = 0 and b^T w = 0. (The sympy LP is not used: sympy 1.14
                # lpmax returned a wrong optimum on a test LP at 12:13 PDT.)
                cert = moduli_certificate(N)
                entry["moduli_certificate"] = cert
                entry["moduli_excluded"] = bool(cert is not None and cert["verified"])
                if not entry["moduli_excluded"]:
                    eqs = pc.block_equations(set(N))
                    elems = sorted({x for _, tt in eqs for x, _ in tt})
                    ph = pc.phase_consistency(eqs, elems)
                    entry["phase_complex_consistent"] = ph["complex_consistent"]
                    entry["phase_obstruction_verified"] = ph.get("obstruction_verified")
                    if ph["complex_consistent"]:
                        cpath = os.path.join(OUT, tag + "_rep%d_completion.cnf" % k)
                        entry["completion_allowed_points"] = lte.completion_cnf(N, cpath)
                        clrat = cpath.replace(".cnf", ".lrat")
                        st, model = lte.solve(cpath, clrat)
                        entry["completion_status"] = {10: "SAT", 20: "UNSAT"}.get(st, str(st))
                        if st == 20:
                            entry["completion_lrat_verified"], entry["completion_lrat_msg"] = lte.lrat_check(cpath, clrat)
            excluded = (not entry["components_ok"]) or entry.get("moduli_excluded", False) or \
                (entry.get("phase_complex_consistent") is False and entry.get("phase_obstruction_verified")) or \
                (entry.get("completion_status") == "UNSAT" and entry.get("completion_lrat_verified"))
            entry["excluded"] = bool(excluded)
            prof_rep["reps"].append(entry)
        report["profiles"].append(prof_rep)
        print(json.dumps({k: v for k, v in prof_rep.items() if k != "reps"} |
                         {"excluded_reps": sum(r["excluded"] for r in prof_rep["reps"])}), flush=True)
    report["excluded"] = all(p["final_unsat_lrat_verified"] and all(r["excluded"] for r in p["reps"])
                             for p in report["profiles"])
    with open(os.path.join(HERE, "..", "evidence", "large_t_gen_t%d_e%d.json" % (t, e)), "w") as fh:
        json.dump(report, fh, indent=1)
    print("t=%d e=%d excluded: %s" % (t, e, report["excluded"]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    a = ap.parse_args()
    run(a.t, a.e)
