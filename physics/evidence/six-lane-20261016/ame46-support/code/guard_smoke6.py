#!/usr/bin/env python3
"""guard_smoke6.py: controls for engine v6 (code/large_t_joint6.py) and checker-2 (code/lratcheck_py2.py).
Lane ame46-support. Controls are not proof.

 L1 Pandya positive (base + J + W with all v6 assertions): SAT with N fixed. The mutated N is UNSAT.
 L2 M2: Guard6.settle() joins the watchdog thread. A trip before settling (1-byte RSS cap) is reported; after settling
    the thread is dead.
 L3 m1: a correctly sized W family for profile {2,2,2}^4 (2,592 clauses) with one clause replaced by
    ¬3333 ¬4333 ¬3344 ¬5344 ¬4443 ¬5443 (doubled pairs {3,4}, {3,5}, {4,5}) is rejected by v6 build. The same family
    passes v5 build, which shows the gap is closed.
 L4 m2: a solver model with the wrong cardinality (an injected empty model) makes the profile UNKNOWN; nothing is
    blocked.
 L5 m3: an exception from the stream checker makes the profile UNKNOWN; the engine does not abort. A W generator
    returning a four-literal clause gives UNKNOWN (a build failure), not an IndexError abort.
 L6 m4: checker-2 rejects a proof line with a missing hint terminator, also under PYTHONOPTIMIZE=2.
 L7 Regression: v6 proof mode on the certified (30,0) gives EXCLUDED, with both streams verified by C and by checker-2.
Summary: evidence/guard_smoke6.json.
"""
import itertools
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine_control as ec
import exp_triangle
import large_t_e0 as lte
import large_t_joint5 as v5
import large_t_joint6 as v6
import large_t_lex as v2
import pandya_control as pcn


def sat(S, units):
    p = subprocess.run(["cadical", "-q", "-t", "1200"], input=v2.dimacs(S.nv, S.cl + units), capture_output=True,
                       text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "status %d" % p.returncode)


def run_engine(args, out):
    p = subprocess.run([sys.executable, "-B", os.path.join(HERE, "large_t_joint6.py")] + args + ["--out", out],
                       capture_output=True, text=True, cwd=HERE, env=dict(os.environ, OMP_NUM_THREADS="1"))
    return json.load(open(out)), p


class A:
    pass


def main():
    res = {}
    os.makedirs(os.path.join(LANE, "explore", "large_t_joint6"), exist_ok=True)
    # L1
    W = pcn.build()
    N = sorted({tuple(ec.SIGMA[c] for c in x) for x, v in W.items() if v != pcn.R2})
    S, _ = v6.build([(6, 6, 3, 3, 3, 3)] * 4, 0, 24, True, True)
    fix = lambda S_, N_: [[S_.var[x]] if x in set(N_) else [-S_.var[x]] for x in S_.points]
    res["L1_pandya_N_fixed"] = sat(S, fix(S, N))
    x0 = N[0]
    y0 = next(y for y in S.points if y not in set(N) and y[0] == x0[0] and y[1] == x0[1])
    res["L1_mutated"] = sat(S, fix(S, (set(N) - {x0}) | {y0}))
    # L2
    G = v6.Guard6(6 * 2 ** 30, 10 ** 9, 0)
    time.sleep(1.2)
    G.settle()
    res["L2_thread_stopped"] = not G._thread.is_alive()
    G2 = v6.Guard6(1, 10 ** 9, 0)
    time.sleep(2.5)
    t2 = G2.settle()
    res["L2_early_trip_reported"] = t2 is not None and t2.startswith("RSS")
    # L3
    prof = [(2, 2, 2)] * 4
    orig = exp_triangle.triangle_clauses

    def bad_family(S_):
        fam = orig(S_)
        pts = ["3333", "4333", "3344", "5344", "4443", "5443"]
        fam[0] = [-S_.var[tuple(int(c) for c in s)] for s in pts]
        return fam
    exp_triangle.triangle_clauses = bad_family
    try:
        try:
            v6.build(prof, 0, 6, False, True)
            res["L3_v6_rejects_mixed_pairs"] = False
        except AssertionError as exc:
            res["L3_v6_rejects_mixed_pairs"] = True
            res["L3_reason"] = str(exc)
        try:
            v5.build(prof, 0, 6, False, True)
            res["L3_v5_accepted_it"] = True
        except AssertionError:
            res["L3_v5_accepted_it"] = False

        def four_lit(S_):
            fam = orig(S_)
            fam[0] = fam[0][:4]
            return fam
        exp_triangle.triangle_clauses = four_lit
        try:
            v6.build(prof, 0, 6, False, True)
            res["L5_four_literal_rejected"] = False
        except AssertionError as exc:
            res["L5_four_literal_rejected"] = True
            res["L5_four_literal_reason"] = str(exc)
    finally:
        exp_triangle.triangle_clauses = orig
    # L4: inject an empty SAT model on the first solver call
    real_solve = v2.solve
    calls = {"n": 0}

    def fake_solve(G_, text, tl, proof_path=None):
        calls["n"] += 1
        if calls["n"] == 1 and proof_path is None:
            return 10, set()
        return real_solve(G_, text, tl, proof_path)
    a = A()
    a.t, a.e, a.proof, a.joint, a.triangles, a.profiles = 30, 0, False, True, True, "1"
    a.rss_cap, a.disk_budget, a.free_floor = 6 * 2 ** 30, 512 * 2 ** 20, 12_000_000_000
    a.max_solutions, a.max_product, a.max_mem, a.time_limit = 5000, 1296, 2 * 2 ** 30, 600
    a.out = os.path.join(LANE, "explore", "large_t_joint6", "smoke_L4.json")
    v6.v2.solve = fake_solve
    try:
        v6.run(a)
    finally:
        v6.v2.solve = real_solve
    rep = json.load(open(a.out))
    res["L4_outcome"] = rep["outcome"]
    res["L4_reason"] = rep["profiles"][0].get("unknown_reason")
    # L5: the stream checker raises
    real_check = v6.check_stream6

    def boom(*args, **kw):
        raise FileNotFoundError("injected checker startup failure")
    a.proof, a.out = True, os.path.join(LANE, "explore", "large_t_joint6", "smoke_L5.json")
    v6.check_stream6 = boom
    try:
        v6.run(a)
    finally:
        v6.check_stream6 = real_check
    rep = json.load(open(a.out))
    res["L5_outcome"] = rep["outcome"]
    res["L5_reason"] = rep["profiles"][0].get("unknown_reason")
    # L6: checker-2 rejects a missing hint terminator, also under PYTHONOPTIMIZE=2
    d = os.path.join(LANE, "explore", "large_t_joint6")
    cnf, prf = os.path.join(d, "L6.cnf"), os.path.join(d, "L6.lrat")
    open(cnf, "w").write("p cnf 1 2\n1 0\n-1 0\n")
    open(prf, "w").write("3 0 1 2\n")
    outs = []
    for env in (dict(os.environ), dict(os.environ, PYTHONOPTIMIZE="2")):
        p = subprocess.run([sys.executable, os.path.join(HERE, "lratcheck_py2.py"), cnf, prf], capture_output=True,
                           text=True, env=env)
        outs.append((p.returncode, (p.stdout + p.stderr).strip()[-120:]))
    res["L6_checker2_runs"] = outs
    res["L6_rejects_both"] = all(rc != 0 and "terminator" in msg for rc, msg in outs)
    # L7
    rep, p = run_engine(["--t", "30", "--e", "0", "--proof", "--joint", "--triangles"],
                        os.path.join(d, "smoke_L7_proof_t30e0.json"))
    res["L7_outcome"] = rep["outcome"]
    res["L7_guard"] = rep["guard_tripped"]
    res["L7_streams_both"] = all(pr["final_proof"]["C"]["verified"] and pr["final_proof"]["py"]["verified"]
                                 for pr in rep["profiles"] if pr["status"] == "ENUMERATED")
    res["all_required_true"] = bool(
        res["L1_pandya_N_fixed"] == "SAT" and res["L1_mutated"] == "UNSAT" and res["L2_thread_stopped"] and
        res["L2_early_trip_reported"] and res["L3_v6_rejects_mixed_pairs"] and res["L3_v5_accepted_it"] and
        res["L5_four_literal_rejected"] and res["L4_outcome"] == "UNKNOWN" and res["L5_outcome"] == "UNKNOWN" and
        res["L6_rejects_both"] and res["L7_outcome"] == "EXCLUDED" and res["L7_guard"] is None and
        res["L7_streams_both"])
    with open(os.path.join(LANE, "evidence", "guard_smoke6.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
