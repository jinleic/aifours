#!/usr/bin/env python3
"""reconstruct_e0.py: for e = 0 candidate supports N that pass components, moduli and phase consistency, run the
classical completion and, if it is SAT, attempt an exact reconstruction of an AME(4,6) state. Lane ame46-support.
Exploration tool. No claim is made until full raw verification.

Reconstruction, following the parent's instruction of 14:4x:
- |6ψ_x| = 1/√2 on N (at e = 0 every hole line holds exactly two points);
- |6ψ_x| = 1 on the completion T;
- phases on N: the exact rational solution θ of the block congruences over R/2πZ (phase_check.phase_consistency;
  φ = 2πθ), not restricted to signs; phase 0 on T.
Exact unitarity check of all three reshapings U_π = 6ψ:
- write each entry as c·ζ_D^k, with c ∈ {1, 1/√2} and D the common denominator of θ;
- every entry of U U† and of U† U is then (1/2)·Σ ζ_D^{k} over N-pairs plus Σ ζ_D^{k} over T-pairs;
- reduce the polynomial Σ c_k x^k modulo the cyclotomic polynomial Φ_D in Q[x], and test that it equals the
  identity entry (1 on the diagonal, 0 elsewhere).
Every candidate is preserved: its N, its completion status, T if SAT, and its phase solution or obstruction.

Usage: reconstruct_e0.py --t T --profile K --budget SECONDS [--out FILE]. This enumerates the profile's N-only
solutions with v2's lex-leader constraints.
"""
import argparse
import itertools
import json
import os
import subprocess
import time
from fractions import Fraction as Fr

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import phase_check as pc
import phase_cert as pcert

RESH = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def completion(N):
    text, nall = v2.completion_text(N)
    holes = {P: {tuple(x[i] for i in P) for x in N} for P in lte.PAIRS}
    allowed = [x for x in itertools.product(range(6), repeat=4)
               if all(tuple(x[i] for i in P) not in holes[P] for P in lte.PAIRS)]
    p = subprocess.run(["cadical", "-q", "-t", "600"], input=text, capture_output=True, text=True)
    if p.returncode != 10:
        return p.returncode, None
    model = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
             if int(v) > 0}
    T = [x for k, x in enumerate(allowed) if (k + 1) in model]
    return 10, T


def cyclotomic_zero(coeffs, D):
    """coeffs: dict k -> Fraction (k mod D). True iff Σ c_k ζ_D^k = 0 exactly."""
    import sympy
    x = sympy.symbols("x")
    poly = sum(sympy.Rational(c.numerator, c.denominator) * x ** (k % D) for k, c in coeffs.items())
    if poly == 0:
        return True
    rem = sympy.rem(sympy.Poly(poly, x), sympy.Poly(sympy.cyclotomic_poly(D, x), x))
    return rem.is_zero


def exact_unitarity(N, T, theta):
    """Entries: x in N -> (1/√2) ζ^k, x in T -> ζ^0. Returns (ok, details)."""
    D = 1
    for v in theta.values():
        D = D * v.denominator // __import__("math").gcd(D, v.denominator)
    D = max(D, 2)
    expo = {x: int(theta.get(x, Fr(0)) * D) % D for x in N}
    entries = {}
    for x in N:
        entries[x] = ("N", expo[x])
    for x in T:
        entries[x] = ("T", 0)
    details = []
    for k, (rows, cols) in enumerate(RESH):
        R = {}
        for x, val in entries.items():
            r = tuple(x[i] for i in rows)
            c = tuple(x[i] for i in cols)
            R.setdefault(r, {})[c] = val
        Cc = {}
        for x, val in entries.items():
            r = tuple(x[i] for i in rows)
            c = tuple(x[i] for i in cols)
            Cc.setdefault(c, {})[r] = val
        if len(R) != 36 or len(Cc) != 36:
            return False, "reshaping %d: an empty row or column" % k
        for side, M in (("rows", R), ("cols", Cc)):
            keys = sorted(M)
            for a, b in itertools.combinations_with_replacement(keys, 2):
                common = set(M[a]) & set(M[b])
                coeffs = {}
                for z in common:
                    (ta, ka), (tb, kb) = M[a][z], M[b][z]
                    w = (Fr(1, 2) if ta == "N" else Fr(1)) if ta == tb else None
                    if w is None:
                        return False, "reshaping %d: N and T share a line" % k
                    coeffs[(ka - kb) % D] = coeffs.get((ka - kb) % D, Fr(0)) + w
                if a == b:
                    coeffs[0] = coeffs.get(0, Fr(0)) - 1
                if coeffs and not cyclotomic_zero(coeffs, D):
                    return False, "reshaping %d %s %s,%s: inner product not identity" % (k, side, a, b)
        details.append("reshaping %d: U U† = U† U = I exactly" % k)
    return True, details


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--budget", type=float, default=120)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    S = ltg.SmallGen(prof)
    S.build_gen(0, h)
    for g in v2.generators(S):
        v2.add_lex_leader(S, g)
    blocks, t0, cands, counts = [], time.time(), [], {}
    while time.time() - t0 < a.budget:
        p = subprocess.run(["cadical", "-q", "-t", "600"], input=v2.dimacs(S.nv, S.cl + blocks), capture_output=True,
                           text=True)
        if p.returncode == 20:
            counts["ENUMERATION_COMPLETE"] = True
            break
        if p.returncode != 10:
            counts["solver_status"] = p.returncode
            break
        m = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
             if int(v) > 0}
        N = [x for x in S.points if S.var[x] in m]
        blocks.append([-S.var[x] for x in N])
        okc, _ = ltg.component_checks(N)
        if not okc:
            counts["components"] = counts.get("components", 0) + 1
            continue
        mc = ltg.moduli_certificate(N)
        if mc is not None and mc["verified"]:
            counts["moduli"] = counts.get("moduli", 0) + 1
            continue
        eqs = pc.block_equations(set(N))
        elems = sorted({x for _, tt in eqs for x, _ in tt})
        ph = pc.phase_consistency(eqs, elems)
        if not ph["complex_consistent"]:
            counts["phase"] = counts.get("phase", 0) + 1
            continue
        counts["phase_consistent"] = counts.get("phase_consistent", 0) + 1
        st, T = completion(N)
        cand = {"index": len(blocks) - 1, "N": [pcert.pt(x) for x in N], "theta": ph.get("theta"),
                "theta_verified": ph.get("theta_verified"), "completion_status": {10: "SAT", 20: "UNSAT"}.get(st, st)}
        if st == 10:
            theta = {tuple(__import__("ast").literal_eval(k)): Fr(v) for k, v in (ph.get("theta") or {}).items()}
            ok, det = exact_unitarity(N, T, theta)
            cand.update({"T": [pcert.pt(x) for x in T], "support_size": len(N) + len(T),
                         "exact_unitarity": ok, "details": det})
            print("!!! COMPLETION SAT; exact unitarity:", ok, det, flush=True)
        cands.append(cand)
        print("phase-consistent candidate #%d: completion %s" % (len(cands), cand["completion_status"]), flush=True)
    out = {"profile": [list(p) for p in prof], "t": a.t, "e": 0, "solutions_seen": len(blocks), "counts": counts,
           "candidates": cands, "elapsed_s": round(time.time() - t0, 1)}
    path = a.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "explore",
                                 "reconstruct_t%d_p%d.json" % (a.t, a.profile))
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "candidates"}))


if __name__ == "__main__":
    main()
