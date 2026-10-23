#!/usr/bin/env python3
"""guard_smoke5.py: controls for engine v5 (code/large_t_joint5.py). Lane ame46-support. Controls are not proof.

 K1 Pandya's 60-term state (t = 12, e = 0) in normal form satisfies v5's base + J + W, with all binding assertions
    active: SAT with N fixed, and SAT with N and T fixed.
 K2 Pandya's N with one point moved: UNSAT.
 K3 Pandya's N contains no doubled triangle.
 K4 W discriminates. An N with a doubled triangle that satisfies base + J (profile {6,6}{2⁶}³, t = 24) is SAT without
    W and UNSAT with W.
 K5 J discriminates. An N that satisfies the base but has no officer placement (the stored phase-consistent,
    completion-UNSAT N of explore/reconstruct_t24_p0.json) is SAT without J and UNSAT with J.
 K6 Guards. RSS trip gives UNKNOWN; free-space floor gives UNKNOWN; --proof without --joint gives UNKNOWN; --profiles
    gives the PARTIAL label.
 K7 The build-time W count assertion rejects the void (15:13) generator, i.e. without the z2 filter.
    --triangles with e ≠ 0 raises.
Summary: evidence/guard_smoke5.json.
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
import large_t_e0 as lte
import large_t_gen as ltg
import large_t_joint5 as v5
import large_t_lex as v2
import pandya_control as pcn
import phase_cert as pcert


def sat(S, units, extra=()):
    p = subprocess.run(["cadical", "-q", "-t", "1200"], input=v2.dimacs(S.nv, S.cl + list(extra) + units),
                       capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "status %d" % p.returncode), p.stdout


def fixN(S, N):
    Ns = set(N)
    return [[S.var[x]] if x in Ns else [-S.var[x]] for x in S.points]


def void_triangle_clauses(S):
    """The 15:13 generator, i.e. the z2 filter replaced by pass. Used only to test that the assertion rejects it."""
    cl = []
    for i in range(4):
        others = [k for k in range(4) if k != i]
        c1, c2, c3 = others
        idx = {k: n for n, k in enumerate(others)}
        for a, a2 in itertools.combinations(S.V[i], 2):
            Z = list(itertools.product(*[S.V[k] for k in others]))

            def pt(val, z):
                x = [0] * 4
                x[i] = val
                for k in others:
                    x[k] = z[idx[k]]
                return tuple(x)
            for z1 in Z:
                for z2 in Z:
                    for z3 in Z:
                        if z3[idx[c2]] != z2[idx[c2]] or z3[idx[c3]] != z1[idx[c3]] or z3[idx[c1]] == z1[idx[c1]]:
                            continue
                        cl.append([-S.var[pt(a, z)] for z in (z1, z2, z3)] + [-S.var[pt(a2, z)] for z in (z1, z2, z3)])
    return cl


def main():
    res = {}
    W = pcn.build()
    N = sorted({tuple(ec.SIGMA[c] for c in x) for x, v in W.items() if v != pcn.R2})
    T = sorted({tuple(ec.SIGMA[c] for c in x) for x, v in W.items() if v == pcn.R2})
    prof = [(6, 6, 3, 3, 3, 3)] * 4
    S, ntri = v5.build(prof, 0, 24, True, True)
    res["K1_triangle_clauses"] = ntri
    res["K1_N_fixed"] = sat(S, fixN(S, N))[0]
    pts = list(itertools.product(range(6), repeat=4))
    uT = [[S._officer_base + 1 + n] if x in set(T) else [-(S._officer_base + 1 + n)] for n, x in enumerate(pts)]
    res["K1_N_T_fixed"] = sat(S, fixN(S, N) + uT)[0]
    x0 = N[0]
    y0 = next(y for y in S.points if y not in set(N) and y[0] == x0[0] and y[1] == x0[1])
    res["K2_mutated"] = sat(S, fixN(S, (set(N) - {x0}) | {y0}))[0]
    inv = {S.var[x]: x for x in S.points}
    res["K3_pandya_doubled_triangles"] = sum(1 for c in exp_triangle.triangle_clauses(S)
                                             if all(inv[-l] in set(N) for l in c))
    # K4: profile 0 at t = 24, base + J without W; search for an N containing a doubled triangle
    p0 = lte.profiles(12)[0]
    SJ, _ = v5.build(p0, 0, 12, True, False)
    tri0 = exp_triangle.triangle_clauses(SJ)
    blocks, found, tries = [], None, 0
    while tries < 60 and found is None:
        st, out = sat(SJ, [], blocks)
        if st != "SAT":
            break
        m = {int(v) for line in out.splitlines() if line.startswith("v ") for v in line.split()[1:] if int(v) > 0}
        Nc = [x for x in SJ.points if SJ.var[x] in m]
        blocks.append([-SJ.var[x] for x in Nc])
        tries += 1
        Ns = set(Nc)
        inv0 = {SJ.var[x]: x for x in SJ.points}
        if any(all(inv0[-l] in Ns for l in c) for c in tri0):
            found = Nc
    res["K4_search_tries"] = tries
    if found is not None:
        res["K4_N"] = [pcert.pt(x) for x in found]
        res["K4_without_W"] = sat(SJ, fixN(SJ, found))[0]
        res["K4_with_W"] = sat(SJ, fixN(SJ, found), tri0)[0]
    # K5: the stored phase-consistent, completion-UNSAT N
    cand = json.load(open(os.path.join(LANE, "explore", "reconstruct_t24_p0.json")))["candidates"][0]
    N5 = [pcert.unpt(s) for s in cand["N"]]
    SB, _ = v5.build(p0, 0, 12, False, False)
    res["K5_completion_status_recorded"] = cand["completion_status"]
    res["K5_without_J"] = sat(SB, fixN(SB, N5))[0]
    res["K5_with_J"] = sat(SJ, fixN(SJ, N5))[0]
    # K7: the void generator must be rejected by the count assertion; W with e != 0 must raise
    orig = exp_triangle.triangle_clauses
    exp_triangle.triangle_clauses = void_triangle_clauses
    try:
        v5.build(p0, 0, 12, False, True)
        res["K7_void_generator_rejected"] = False
    except AssertionError as exc:
        res["K7_void_generator_rejected"] = True
        res["K7_reason"] = str(exc)
    finally:
        exp_triangle.triangle_clauses = orig
    try:
        v5.build(lte.profiles(10)[0], 2, 10, False, True)
        res["K7_W_e_nonzero_raises"] = False
    except ValueError:
        res["K7_W_e_nonzero_raises"] = True
    # K6: guards through the engine
    runs = {}
    for name, args in (("K6_rss", ["--t", "30", "--e", "0", "--joint", "--rss-cap", str(20 * 2 ** 20)]),
                       ("K6_floor", ["--t", "30", "--e", "0", "--joint", "--free-floor", str(10 ** 15)]),
                       ("K6_proof_without_joint", ["--t", "30", "--e", "0", "--proof"]),
                       ("K6_partial", ["--t", "28", "--e", "0", "--joint", "--triangles", "--profiles", "0"]),
                       ("K6_agree_t30e0", ["--t", "30", "--e", "0", "--joint", "--triangles"])):
        out = os.path.join(LANE, "explore", "large_t_joint5", "smoke_%s.json" % name)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        p = subprocess.run([sys.executable, "-B", os.path.join(HERE, "large_t_joint5.py")] + args + ["--out", out],
                           capture_output=True, text=True, cwd=HERE, env=dict(os.environ, OMP_NUM_THREADS="1"))
        rep = json.load(open(out))
        runs[name] = {"outcome": rep["outcome"], "guard": rep["guard_tripped"], "exit": p.returncode}
    res["runs"] = runs
    res["all_required_true"] = bool(
        res["K1_N_fixed"] == "SAT" and res["K1_N_T_fixed"] == "SAT" and res["K2_mutated"] == "UNSAT" and
        res["K3_pandya_doubled_triangles"] == 0 and res.get("K4_without_W") == "SAT" and
        res.get("K4_with_W") == "UNSAT" and res["K5_without_J"] == "SAT" and res["K5_with_J"] == "UNSAT" and
        res["K7_void_generator_rejected"] and res["K7_W_e_nonzero_raises"] and
        runs["K6_rss"]["outcome"] == "UNKNOWN" and runs["K6_floor"]["outcome"] == "UNKNOWN" and
        runs["K6_proof_without_joint"]["outcome"] == "UNKNOWN" and "PARTIAL" in runs["K6_partial"]["outcome"] and
        runs["K6_agree_t30e0"]["outcome"].startswith("EXCLUDED-EXPLORATION"))
    with open(os.path.join(LANE, "evidence", "guard_smoke5.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("K4_N",)}, indent=1))


if __name__ == "__main__":
    main()
