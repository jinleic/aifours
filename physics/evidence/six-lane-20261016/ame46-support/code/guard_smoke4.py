#!/usr/bin/env python3
"""guard_smoke4.py: controls for engine v4 (code/large_t_joint4.py). Lane ame46-support.

 C1 Positive. Pandya's 60-term AME(4,6) state (t = 12, e = 0, profile {6,6,3,3,3,3}^4), relabelled into normal form
    by engine_control.SIGMA. The v4 joint CNF with triangle clauses, with N fixed by unit clauses, must be SAT. With
    N and Pandya's T both fixed it must also be SAT. This is a positive control for the J and W families on a genuine
    state.
 C2 Negative. Pandya's N with one point moved, as in engine_control: UNSAT.
 C3 Direct triangle count. Pandya's N contains no doubled triangle, for any coordinate and value pair.
 C4 Agreement. v4 (--joint --triangles) on (30,0) and (28,0), in exploration mode, gives EXCLUDED-EXPLORATION.
 C5 Guards. --rss-cap 20 MiB gives UNKNOWN (RSS trip); --free-floor 10^15 gives UNKNOWN at start; --profiles gives
    the PARTIAL label.
Summary: evidence/guard_smoke4.json.
"""
import itertools
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine_control as ec
import exp_triangle
import large_t_joint4 as v4
import large_t_lex as v2
import pandya_control as pcn


def sat(S, units):
    p = subprocess.run(["cadical", "-q", "-t", "1200"], input=v2.dimacs(S.nv, S.cl + units), capture_output=True,
                       text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "status %d" % p.returncode)


def main():
    res = {}
    W = pcn.build()
    N = sorted({tuple(ec.SIGMA[c] for c in x) for x, v in W.items() if v != pcn.R2})
    T = sorted({tuple(ec.SIGMA[c] for c in x) for x, v in W.items() if v == pcn.R2})
    prof = [(6, 6, 3, 3, 3, 3)] * 4
    S, ntri = v4.build(prof, 0, 24, True, True)
    res["pandya_triangle_clauses"] = ntri
    unitsN = [[S.var[x]] if x in set(N) else [-S.var[x]] for x in S.points]
    res["C1_pandya_N_fixed"] = sat(S, unitsN)
    pts = list(itertools.product(range(6), repeat=4))
    unitsT = [[S._officer_base + 1 + n] if x in set(T) else [-(S._officer_base + 1 + n)] for n, x in enumerate(pts)]
    res["C1_pandya_N_and_T_fixed"] = sat(S, unitsN + unitsT)
    x0 = N[0]
    y0 = next(y for y in S.points if y not in set(N) and y[0] == x0[0] and y[1] == x0[1])
    Nm = (set(N) - {x0}) | {y0}
    res["C2_mutated_N"] = sat(S, [[S.var[x]] if x in Nm else [-S.var[x]] for x in S.points])
    Nset = set(N)
    viol = 0
    inv = {S.var[x]: x for x in S.points}
    for c in exp_triangle.triangle_clauses(S):
        if all(inv[-l] in Nset for l in c):
            viol += 1
    res["C3_pandya_doubled_triangles"] = viol
    runs = {}
    for name, args in (("C4_t30e0", ["--t", "30", "--e", "0", "--joint", "--triangles"]),
                       ("C4_t28e0", ["--t", "28", "--e", "0", "--joint", "--triangles"]),
                       ("C5_rss", ["--t", "30", "--e", "0", "--joint", "--triangles", "--rss-cap", str(20 * 2 ** 20)]),
                       ("C5_floor", ["--t", "30", "--e", "0", "--joint", "--free-floor", str(10 ** 15)]),
                       ("C5_partial", ["--t", "28", "--e", "0", "--joint", "--triangles", "--profiles", "0"])):
        out = os.path.join(LANE, "explore", "large_t_joint4", "smoke_%s.json" % name)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        p = subprocess.run([sys.executable, "-B", os.path.join(HERE, "large_t_joint4.py")] + args + ["--out", out],
                           capture_output=True, text=True, cwd=HERE, env=dict(os.environ, OMP_NUM_THREADS="1"))
        rep = json.load(open(out))
        runs[name] = {"outcome": rep["outcome"], "guard": rep["guard_tripped"], "exit": p.returncode}
    res["runs"] = runs
    res["all_required_true"] = bool(
        res["C1_pandya_N_fixed"] == "SAT" and res["C1_pandya_N_and_T_fixed"] == "SAT" and
        res["C2_mutated_N"] == "UNSAT" and res["C3_pandya_doubled_triangles"] == 0 and
        runs["C4_t30e0"]["outcome"].startswith("EXCLUDED-EXPLORATION") and
        runs["C4_t28e0"]["outcome"].startswith("EXCLUDED-EXPLORATION") and
        runs["C5_rss"]["outcome"] == "UNKNOWN" and (runs["C5_rss"]["guard"] or "").startswith("RSS") and
        runs["C5_floor"]["outcome"] == "UNKNOWN" and "PARTIAL" in runs["C5_partial"]["outcome"])
    with open(os.path.join(LANE, "evidence", "guard_smoke4.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
