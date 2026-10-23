#!/usr/bin/env python3
"""large_t_joint4.py: engine v4 for structured exclusion of (t, e). Lane ame46-support. New file: v2 (large_t_lex.py)
and v3 (large_t_lex3.py) and all their outputs stay untouched.

v4 = v3 (guards, free-space floor, Lemma 17 pre-filter, stored certificates, gzip LRAT streams), plus two clause
families. Both are written and proved in review/ENGINE_V4.r1.md:
 J (--joint): the officer-placement constraints of Lemma 19 (code/profile_officer_cnf.py, over [6]^4), linked to the
    N-only CNF. For every line (a, b) ∈ V_i × V_j, the hole indicator holds iff the line holds no officer. Valid for
    every AME state and every e: a line meets N iff it holds no officer (L42-2(a), L42-4).
 W (--triangles, e = 0 only): the doubled-triangle clauses of Lemma 20 (code/exp_triangle.triangle_clauses).
Lex-leader constraints act on the N point variables only, with v2's generators (the realizable-support argument of
review/SUPPORT_LOWER48.r2.md §3 covers it: the officers of g·ψ form g(T)). Each found N is blocked individually.
In the joint model every found N has an officer completion. For any N that passes components, moduli and phase, v4
also reconstructs and exactly checks the state (code/reconstruct_e0.exact_unitarity; e = 0 only), and stores N, T
and θ. Such an N is reported as CANDIDATE; the case outcome is then NOT EXCLUDED.
Exploration by default; --proof writes and checks gzip LRAT streams for every final UNSAT.
"""
import argparse
import hashlib
import itertools
import json
import os
import time

import exp_joint
import exp_triangle
import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import large_t_lex3 as v3
import phase_cert as pcert
import phase_check as pc
import reconstruct_e0 as rc

LANE = v2.LANE
OUT = os.path.join(LANE, "explore", "large_t_joint4")


def officer_set(S, model, prof):
    """Officers of a joint-model solution: officer point variables are base + 1 + (index in [6]^4 product order)."""
    pts = list(itertools.product(range(6), repeat=4))
    base = S._officer_base
    return [x for n, x in enumerate(pts) if (n + 1 + base) in model]


def build(prof, e, h, joint, triangles):
    if joint:
        S = exp_joint.build_joint(prof, e, h)
        # build_joint appends the officer CNF after the N-only CNF; its point variables start at the N-only nv
        S0 = ltg.SmallGen(prof)
        S0.build_gen(e, h)
        S._officer_base = S0.nv
    else:
        S = ltg.SmallGen(prof)
        S.build_gen(e, h)
        S._officer_base = None
    ntri = 0
    if triangles:
        if e != 0:
            raise ValueError("triangle clauses are valid only for e = 0")
        tri = exp_triangle.triangle_clauses(S)
        S.cl += tri
        ntri = len(tri)
    return S, ntri


def run(a):
    t, e, h = a.t, a.e, 36 - a.t
    os.makedirs(OUT, exist_ok=True)
    start_bytes = v2.lane_bytes()
    budget = min(int(a.disk_budget), v2.CAP - v2.HEADROOM - start_bytes)
    fb0 = v3.free_bytes()
    G = v3.Guard3(int(a.rss_cap), budget, int(a.free_floor))
    report = {"engine": "large_t_joint4 v4", "t": t, "e": e, "h": h, "mode": "proof" if a.proof else "exploration",
              "joint": a.joint, "triangles": a.triangles,
              "caps": {"rss_cap_bytes": int(a.rss_cap), "disk_budget_bytes": budget, "max_solutions": a.max_solutions,
                       "max_product_space": a.max_product, "max_est_memory_bytes": a.max_mem,
                       "solver_time_limit_s": a.time_limit, "free_floor_bytes": int(a.free_floor)},
              "lane_bytes_at_start": start_bytes, "free_bytes_at_start": fb0, "profiles": []}
    if budget <= 0:
        G.trip("no disk budget left under the lane cap")
    if fb0 < int(a.free_floor):
        G.trip("filesystem free %d B < floor %d B at start" % (fb0, int(a.free_floor)))
    profs = lte.profiles(h)
    sel = range(len(profs)) if a.profiles is None else [int(k) for k in a.profiles.split(",")]
    for pidx in sel:
        prof = profs[pidx]
        if G.tripped:
            break
        entry = {"index": pidx, "profile": [list(p) for p in prof], "reps": []}
        report["profiles"].append(entry)
        fam = v3.alpha_family(prof, t, h)
        entry["lemma17_f"] = fam
        if min(fam) < 0:
            entry.update({"status": "EXCLUDED-BY-LEMMA", "lemma": "Lemma 17 (officer counting)"})
            continue
        pb = v2.pre_bounds(prof, h, e)
        entry["pre_bounds"] = pb
        if not pb["fits"]:
            entry.update({"status": "EMPTY", "solutions": 0})
            continue
        if pb["product_space"] > a.max_product or pb["est_memory_bytes"] > a.max_mem:
            entry.update({"status": "UNKNOWN", "unknown_reason": "pre-bounds exceeded (not attempted)"})
            continue
        tag = "t%d_e%d_p%d" % (t, e, pidx)
        t0 = time.time()
        S, ntri = build(prof, e, h, a.joint, a.triangles)
        gens = v2.generators(S)
        for g in gens:
            v2.add_lex_leader(S, g)
        entry.update({"triangle_clauses": ntri, "generators": len(gens)})
        blocks, sols, offs, status, lrat_info, final_sha = [], [], [], None, None, None
        while True:
            if G.tripped:
                status = "UNKNOWN"
                break
            text = v2.dimacs(S.nv, S.cl + blocks)
            st, model = v2.solve(G, text, a.time_limit)
            if G.tripped:
                status = "UNKNOWN"
                break
            if st == 20:
                final_sha = hashlib.sha256(text.encode()).hexdigest()
                if a.proof:
                    gzp = os.path.join(OUT, tag + ".final.lrat.gz")
                    st2, _ = v2.solve(G, text, a.time_limit, gzp)
                    if G.tripped or st2 != 20:
                        status = "UNKNOWN"
                        break
                    lrat_info = v2.check_stream(G, text, gzp)
                    lrat_info["proof"] = os.path.relpath(gzp, LANE)
                    lrat_info["proof_gz_sha256"] = hashlib.sha256(open(gzp, "rb").read()).hexdigest()
                status = "ENUMERATED"
                break
            if st != 10:
                status = "UNKNOWN"
                entry["unknown_reason"] = "solver status %d (time limit or error)" % st
                break
            N = [x for x in S.points if S.var[x] in model]
            blocks.append([-S.var[x] for x in N])
            sols.append(N)
            offs.append(officer_set(S, model, prof) if a.joint else None)
            if len(sols) > a.max_solutions:
                status = "UNKNOWN"
                entry["unknown_reason"] = "solution cap exceeded"
                break
        entry.update({"status": status, "solutions": len(sols), "final_proof": lrat_info,
                      "final_cnf_sha256": final_sha, "seconds": round(time.time() - t0, 1)})
        if status == "ENUMERATED" or (status == "UNKNOWN" and sols):
            for k, N in enumerate(sols):
                r = {"N": [pcert.pt(x) for x in N]}
                okc, why = ltg.component_checks(N)
                r["components_ok"], r["components_reason"] = okc, why
                if okc:
                    mc = ltg.moduli_certificate(N)
                    r["moduli_excluded"] = bool(mc is not None and mc["verified"])
                    if r["moduli_excluded"]:
                        r["moduli_certificate"] = mc
                    else:
                        cert = pcert.extract_certificate(N)
                        if cert is not None:
                            cok, cwhy = pcert.verify_certificate(N, cert)
                            r.update({"phase_certificate": cert,
                                      "phase_certificate_compact": v3.compact_certificate(cert),
                                      "phase_certificate_check": cwhy, "phase_obstruction_verified": cok})
                        else:
                            eqs = pc.block_equations(set(N))
                            elems = sorted({x for _, tt in eqs for x, _ in tt})
                            ph = pc.phase_consistency(eqs, elems)
                            r["phase_consistent"] = True
                            r["theta"] = ph.get("theta")
                            T = offs[k]
                            if T is None:
                                stc, T = rc.completion(N)
                                r["completion_status"] = {10: "SAT", 20: "UNSAT"}.get(stc, stc)
                            if T is not None and e == 0:
                                theta = {tuple(__import__("ast").literal_eval(kk)): __import__("fractions").Fraction(vv)
                                         for kk, vv in (ph.get("theta") or {}).items()}
                                ok, det = rc.exact_unitarity(N, T, theta)
                                r.update({"T": [pcert.pt(x) for x in T], "exact_unitarity": ok,
                                          "unitarity_details": det, "CANDIDATE": True})
                                print("!!! CANDIDATE profile %d sol %d exact_unitarity %s" % (pidx, k, ok),
                                      flush=True)
                r["excluded"] = bool((not r["components_ok"]) or r.get("moduli_excluded", False) or
                                     r.get("phase_obstruction_verified", False) or
                                     r.get("completion_status") == "UNSAT")
                entry["reps"].append(r)
        print(json.dumps({k: v for k, v in entry.items() if k != "reps"} |
                         {"excluded_reps": sum(r["excluded"] for r in entry["reps"])}), flush=True)
    unknown = G.tripped is not None or any(p.get("status") == "UNKNOWN" for p in report["profiles"])
    cand = any(r.get("CANDIDATE") for p in report["profiles"] for r in p.get("reps", []))
    if cand:
        outcome = "NOT EXCLUDED (candidate found; see reps with CANDIDATE)"
    elif unknown:
        outcome = "UNKNOWN"
    else:
        ok = all(p["status"] in ("EMPTY", "EXCLUDED-BY-LEMMA") or
                 (all(r["excluded"] for r in p["reps"]) and
                  (not a.proof or (p["final_proof"]["C"]["verified"] and p["final_proof"]["py"]["verified"])))
                 for p in report["profiles"])
        outcome = ("EXCLUDED" if a.proof else "EXCLUDED-EXPLORATION (no proofs; not a certificate)") if ok else \
            "NOT EXCLUDED (open candidates)"
    if a.profiles is not None and outcome.startswith("EXCLUDED"):
        outcome += " [PARTIAL: selected profiles only]"
    report.update({"outcome": outcome, "excluded": outcome == "EXCLUDED", "guard_tripped": G.tripped,
                   "peak_rss_bytes_sampled": G.peak_rss, "bytes_written_before_report": G.written,
                   "min_free_bytes_sampled": G.min_free})
    G.stop()
    path = a.out or os.path.join(LANE, "evidence", "large_t_joint4_t%d_e%d%s.json" % (
        t, e, "" if a.proof else "_explore"))
    with open(path, "w") as fh:
        json.dump(report, fh, indent=1)
    print("t=%d e=%d outcome: %s | guard: %s | peak RSS %d MiB | written %d B" % (
        t, e, outcome, G.tripped, G.peak_rss // 2 ** 20, G.written))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--joint", action="store_true")
    ap.add_argument("--triangles", action="store_true")
    ap.add_argument("--profiles", default=None, help="comma-separated profile indices (partial run)")
    ap.add_argument("--rss-cap", type=float, default=6 * 2 ** 30)
    ap.add_argument("--disk-budget", type=float, default=512 * 2 ** 20)
    ap.add_argument("--free-floor", type=float, default=12_000_000_000)
    ap.add_argument("--max-solutions", type=int, default=5000)
    ap.add_argument("--max-product", type=int, default=1296)
    ap.add_argument("--max-mem", type=float, default=2 * 2 ** 30)
    ap.add_argument("--time-limit", type=int, default=1200)
    ap.add_argument("--out", default=None)
    run(ap.parse_args())
