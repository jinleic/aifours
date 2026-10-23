#!/usr/bin/env python3
"""large_t_joint6.py: engine v6 for structured exclusion of (t, e). Lane ame46-support. New file; v2–v5 and all
their outputs stay untouched. The CNF is identical to v5's: review/V4_PROOF_SCHEMA.r2.md.

v6 is v5 with the fixes of review/ame46-v5-codex-delta-review-v1.note.md:
 - M2: finalization synchronizes with the watchdog. Guard6.settle() stops the watchdog thread and joins it, and only
   then are guard_tripped and the outcome evaluated. A trip at any time before settling gives UNKNOWN.
 - m1: each W clause must have exactly six literals, and its three doubled pairs must share one value pair {a, a'}.
 - m2: every recorded Y must satisfy |Y| = 2h + e, with distinct points, before its blocking clause is added;
   otherwise the profile is UNKNOWN.
 - m3: any exception in build, solve, proof writing or checking (IndexError, checker startup, proof-file errors) makes
   the profile UNKNOWN instead of aborting.
 - m4: the Python worker checker is code/lratcheck_py2.py, which raises explicitly where lratcheck_py.py asserted.
The v5 changes (proof mode requires --joint, phase flags, UNKNOWN precedence, binding assertions) are kept.
"""
import argparse
import hashlib
import itertools
import json
import os
import threading
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
OUT = os.path.join(LANE, "explore", "large_t_joint6")
HERE = os.path.dirname(os.path.abspath(__file__))


class Guard6(v3.Guard3):
    """Guard3 whose watchdog thread handle is kept, so finalization can stop and join it (Codex v5 M2)."""

    def __init__(self, rss_cap, disk_budget, free_floor):
        self.free_floor, self.min_free = free_floor, None
        self.rss_cap, self.disk_budget = rss_cap, disk_budget
        self.written, self.tripped, self.child, self.stream = 0, None, None, None
        self.peak_rss = 0
        self._stop = False
        self._thread = threading.Thread(target=self._watch, daemon=True)
        self._thread.start()

    def settle(self):
        self._stop = True
        self._thread.join(timeout=60)
        if self._thread.is_alive() and self.tripped is None:
            self.tripped = "watchdog did not stop within 60 s"
        return self.tripped


def check_stream6(G, text, gz_path):
    """As large_t_lex.check_stream, with checker-2 (lratcheck_py2.py) as the Python checker."""
    import subprocess
    import sys
    res = {}
    if G.tripped is not None:
        return {"C": {"verified": False, "msg": "guard tripped; not checked"},
                "py": {"verified": False, "msg": "guard tripped; not checked"}}
    fifo = gz_path + ".cnf.fifo"
    if not os.path.exists(fifo):
        os.mkfifo(fifo)
    for name, cmd in (("C", [os.path.join(HERE, "lratcheck"), fifo, "/dev/stdin"]),
                      ("py", [sys.executable, "-B", os.path.join(HERE, "lratcheck_py2.py"), fifo, "/dev/stdin",
                              "--allow-satisfied"])):
        def feed():
            with open(fifo, "w") as fh:
                fh.write(text)
        th = threading.Thread(target=feed, daemon=True)
        th.start()
        gz = subprocess.Popen(["gzip", "-dc", gz_path], stdout=subprocess.PIPE)
        p = subprocess.Popen(cmd, stdin=gz.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        gz.stdout.close()
        G.child = p
        out, err = p.communicate()
        G.child = None
        gz.wait()
        th.join(timeout=5)
        res[name] = {"verified": p.returncode == 0 and "s VERIFIED" in out and gz.returncode == 0,
                     "msg": " | ".join(out.strip().splitlines()) or err.strip()}
    return res


def officer_set(S, model, prof):
    """Officers of a joint-model solution: officer point variables are base + 1 + (index in [6]^4 product order)."""
    pts = list(itertools.product(range(6), repeat=4))
    base = S._officer_base
    return [x for n, x in enumerate(pts) if (n + 1 + base) in model]


def build(prof, e, h, joint, triangles):
    """Builds base [+ J] [+ W] and asserts the bindings of the Claude v4 review (MAJOR-2 a-d, MINOR-3, MINOR-6).
    A failed assertion raises and the profile becomes UNKNOWN; it never excludes."""
    if any(sum(p) != h for p in prof):
        raise AssertionError("profile part sums differ from h")
    S0 = ltg.SmallGen(prof)
    S0.build_gen(e, h)
    nv0, base_cl = S0.nv, len(S0.cl)
    # (b) two-sided hole indicators: v -> OR(line points) and point -> v, for every line of V_i x V_j
    cs = {tuple(c) for c in S0.cl}
    for (i, j, a_, b_), v in S0.hl.items():
        ns = [S0.var[x] for x in S0.points if x[i] == a_ and x[j] == b_]
        if (-v, *ns) not in cs or any((-nx, v) not in cs for nx in ns):
            raise AssertionError("hole indicator not two-sided at %s" % ((i, j, a_, b_),))
    if any(abs(l) > nv0 for c in S0.cl for l in c):
        raise AssertionError("base literal beyond nv0")
    if joint:
        # (a) one convention for V and d: poc.build derives them itself; assert they equal SmallGen's
        Vp = [sorted(set(range(6 - len(p), 6))) for p in prof]
        dp = [{a_: p[k] for k, a_ in enumerate(Vp[i])} for i, p in enumerate(prof)]
        if Vp != [list(v) for v in S0.V] or dp != [dict(d) for d in S0.d]:
            raise AssertionError("V/d conventions of SmallGen and profile_officer_cnf differ")
        # MINOR-6: 0 <= want <= |V_k| for every (j, a, k)
        if any(not (0 <= len(S0.V[k]) - S0.d[j][a_] <= len(S0.V[k]))
               for j in range(4) for a_ in S0.V[j] for k in range(4) if k != j):
            raise AssertionError("C3 count out of range")
        S = exp_joint.build_joint(prof, e, h)
        if S.cl[:base_cl] != S0.cl:
            raise AssertionError("base block differs")
        S._officer_base = nv0
        F = __import__("profile_officer_cnf").build(prof)
        if any(abs(l) > F.nv for c in F.clauses for l in c):
            raise AssertionError("officer CNF literal beyond its own variable count")
        # (c) officer block occupies (nv0, nv0 + F.nv]; no base variable above nv0 (checked above)
        if S.nv != nv0 + F.nv:
            raise AssertionError("joint variable count mismatch")
        for c in S.cl[base_cl:base_cl + len(F.clauses)]:
            if any(not (nv0 < abs(l) <= nv0 + F.nv) for l in c):
                raise AssertionError("officer clause outside the officer block")
        # linking binding: exactly the clauses (¬hl ∨ ¬o) for o in the line, then (hl ∨ Λ), per line, in order
        pts4 = list(itertools.product(range(6), repeat=4))
        expect_link = []
        for (i, j) in lte.PAIRS:
            for a_ in S0.V[i]:
                for b_ in S0.V[j]:
                    hl = S0.hl[(i, j, a_, b_)]
                    lam = [nv0 + 1 + n for n, x in enumerate(pts4) if x[i] == a_ and x[j] == b_]
                    expect_link += [[-hl, -o] for o in lam] + [[hl] + lam]
        if S.cl[base_cl + len(F.clauses):] != expect_link:
            raise AssertionError("linking clauses differ from the written schema")
    else:
        S = S0
        S._officer_base = None
    ntri = 0
    if triangles:
        # (d) W gated in code
        if e != 0:
            raise ValueError("triangle clauses are valid only for e = 0")
        tri = exp_triangle.triangle_clauses(S)
        # MINOR-3: build-time count and shape assertions
        sizes = [len(v) for v in S.V]
        expect = 2
        for q in sizes:
            expect *= q * (q - 1)
        if len(tri) != expect or len({frozenset(c) for c in tri}) != len(tri):
            raise AssertionError("triangle clause count %d != 2*prod q(q-1) = %d, or duplicates" % (len(tri), expect))
        inv = {S.var[x]: x for x in S.points}
        for c in tri:
            if len(c) != 6 or any(l >= 0 or -l not in inv for l in c):
                raise AssertionError("triangle clause is not six negative point literals")
            P = [inv[-l] for l in c]
            pairs = [(P[0], P[1]), (P[2], P[3]), (P[4], P[5])]
            dif = [[k for k in range(4) if u[k] != w[k]] for u, w in pairs]
            if len(set(P)) != 6 or any(len(dd) != 1 for dd in dif) or len({dd[0] for dd in dif}) != 1:
                raise AssertionError("triangle clause shape")
            if len({frozenset((u[dif[0][0]], w[dif[0][0]])) for u, w in pairs}) != 1:
                raise AssertionError("triangle clause pairs do not share one value pair {a, a'}")
            i_ = dif[0][0]
            z = [tuple(u[k] for k in range(4) if k != i_) for u, _ in pairs]
            ag = lambda u, w: [n for n in range(3) if u[n] == w[n]]
            a12, a23, a13 = ag(z[0], z[1]), ag(z[1], z[2]), ag(z[0], z[2])
            if not (len(a12) == len(a23) == len(a13) == 1 and len({a12[0], a23[0], a13[0]}) == 3):
                raise AssertionError("triangle agreement pattern")
        S.cl += tri
        ntri = len(tri)
    S._pre_lex_nv = S.nv
    return S, ntri


def run(a):
    t, e, h = a.t, a.e, 36 - a.t
    os.makedirs(OUT, exist_ok=True)
    start_bytes = v2.lane_bytes()
    budget = min(int(a.disk_budget), v2.CAP - v2.HEADROOM - start_bytes)
    fb0 = v3.free_bytes()
    G = Guard6(int(a.rss_cap), budget, int(a.free_floor))
    report = {"engine": "large_t_joint6 v6", "t": t, "e": e, "h": h, "mode": "proof" if a.proof else "exploration",
              "joint": a.joint, "triangles": a.triangles,
              "caps": {"rss_cap_bytes": int(a.rss_cap), "disk_budget_bytes": budget, "max_solutions": a.max_solutions,
                       "max_product_space": a.max_product, "max_est_memory_bytes": a.max_mem,
                       "solver_time_limit_s": a.time_limit, "free_floor_bytes": int(a.free_floor)},
              "lane_bytes_at_start": start_bytes, "free_bytes_at_start": fb0, "profiles": []}
    if budget <= 0:
        G.trip("no disk budget left under the lane cap")
    if fb0 < int(a.free_floor):
        G.trip("filesystem free %d B < floor %d B at start" % (fb0, int(a.free_floor)))
    if a.proof and not a.joint:
        G.trip("proof mode requires --joint (v5, Codex M1)")
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
        try:
            S, ntri = build(prof, e, h, a.joint, a.triangles)
            gens = v2.generators(S)
            n_before = len(S.cl)
            for g in gens:
                v2.add_lex_leader(S, g)
            P = len(S.points)
            if any(not (abs(l) <= P or abs(l) > S._pre_lex_nv) for c in S.cl[n_before:] for l in c):
                raise AssertionError("lex clause uses a non-point, non-fresh variable")
        except Exception as exc:
            entry.update({"status": "UNKNOWN", "unknown_reason": "build/binding failure: %s: %s" % (
                type(exc).__name__, exc)})
            continue
        entry.update({"triangle_clauses": ntri, "generators": len(gens), "bindings_asserted": True})
        blocks, sols, offs, status, lrat_info, final_sha = [], [], [], None, None, None
        while True:
            if G.tripped:
                status = "UNKNOWN"
                break
            try:
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
                        lrat_info = check_stream6(G, text, gzp)
                        lrat_info["proof"] = os.path.relpath(gzp, LANE)
                        lrat_info["proof_gz_sha256"] = hashlib.sha256(open(gzp, "rb").read()).hexdigest()
                    status = "ENUMERATED"
                    break
                if st != 10:
                    status = "UNKNOWN"
                    entry["unknown_reason"] = "solver status %d (time limit or error)" % st
                    break
                N = [x for x in S.points if S.var[x] in model]
                # v6 (Codex m2): check the recorded cardinality before blocking
                if len(N) != 2 * h + e or len(set(N)) != len(N):
                    status = "UNKNOWN"
                    entry["unknown_reason"] = "recorded Y has %d points, expected 2h+e = %d" % (len(N), 2 * h + e)
                    break
                blocks.append([-S.var[x] for x in N])
                sols.append(N)
                offs.append(officer_set(S, model, prof) if a.joint else None)
                if len(sols) > a.max_solutions:
                    status = "UNKNOWN"
                    entry["unknown_reason"] = "solution cap exceeded"
                    break
            except Exception as exc:
                status = "UNKNOWN"
                entry["unknown_reason"] = "solve/proof/check failure: %s: %s" % (type(exc).__name__, exc)
                break
        entry.update({"status": status, "solutions": len(sols), "final_proof": lrat_info,
                      "final_cnf_sha256": final_sha, "seconds": round(time.time() - t0, 1)})
        if status == "ENUMERATED" or (status == "UNKNOWN" and sols):
            try:
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
                                # v5 (Codex m1): returned flags kept; scope is closed 2x2 components only, so for
                                # e > 0 this is a necessary condition, not phase realizability.
                                r["phase_complex_consistent"] = ph["complex_consistent"]
                                r["phase_obstruction_verified"] = bool(ph.get("obstruction_verified"))
                                r["theta"], r["theta_verified"] = ph.get("theta"), ph.get("theta_verified")
                                r["phase_scope"] = "closed 2x2 components" + ("" if e == 0 else
                                                                              " (e > 0: necessary only)")
                                T = offs[k]
                                if T is None and not a.proof:
                                    # exploration only: completion via the guarded wrapper; never a certificate
                                    ctext, nall = v2.completion_text(N)
                                    stc, cm = v2.solve(G, ctext, a.time_limit)
                                    r["completion_status"] = {10: "SAT", 20: "UNSAT"}.get(stc, "UNKNOWN(%s)" % stc)
                                    r["completion_cnf_sha256"] = hashlib.sha256(ctext.encode()).hexdigest()
                                    if stc == 10:
                                        holes = {P: {tuple(x[i] for i in P) for x in N} for P in lte.PAIRS}
                                        allowed = [x for x in itertools.product(range(6), repeat=4)
                                                   if all(tuple(x[i] for i in P) not in holes[P] for P in lte.PAIRS)]
                                        T = [x for n_, x in enumerate(allowed) if (n_ + 1) in cm]
                                    elif stc != 20:
                                        entry["status"] = "UNKNOWN"
                                        entry["unknown_reason"] = "completion solver status %s" % stc
                                if r["phase_complex_consistent"] and T is not None and e == 0 and r["theta_verified"]:
                                    theta = {tuple(__import__("ast").literal_eval(kk)):
                                             __import__("fractions").Fraction(vv)
                                             for kk, vv in (ph.get("theta") or {}).items()}
                                    ok, det = rc.exact_unitarity(N, T, theta)
                                    r.update({"T": [pcert.pt(x) for x in T], "exact_unitarity": ok,
                                              "unitarity_details": det, "CANDIDATE": True})
                                    print("!!! CANDIDATE profile %d sol %d exact_unitarity %s" % (pidx, k, ok),
                                          flush=True)
                                elif r["phase_complex_consistent"]:
                                    r["CANDIDATE"] = True
                    r["excluded"] = bool((not r["components_ok"]) or r.get("moduli_excluded", False) or
                                         r.get("phase_obstruction_verified", False) or
                                         (r.get("completion_status") == "UNSAT" and not a.proof))
                    entry["reps"].append(r)
            except Exception as exc:
                entry["status"] = "UNKNOWN"
                entry["unknown_reason"] = "per-solution analysis failure: %s: %s" % (type(exc).__name__, exc)
        if a.proof and status == "ENUMERATED" and not (lrat_info and lrat_info["C"]["verified"] and
                                                       lrat_info["py"]["verified"]):
            entry["status"] = "UNKNOWN"
            entry["unknown_reason"] = "final proof not verified by both worker checkers"
        print(json.dumps({k: v for k, v in entry.items() if k != "reps"} |
                         {"excluded_reps": sum(r["excluded"] for r in entry["reps"])}), flush=True)
    # v6 (Codex M2): stop and join the watchdog first, then evaluate its settled state
    G.settle()
    unknown = G.tripped is not None or any(p.get("status") == "UNKNOWN" for p in report["profiles"])
    cands = [(p["index"], k) for p in report["profiles"] for k, r in enumerate(p.get("reps", [])) if r.get("CANDIDATE")]
    report["candidates"] = cands
    if unknown:
        # v5 (Codex m2): UNKNOWN takes precedence; candidates are still listed in report["candidates"]
        outcome = "UNKNOWN"
    elif cands:
        outcome = "NOT EXCLUDED (candidate found; see report['candidates'])"
    else:
        ok = all(p["status"] in ("EMPTY", "EXCLUDED-BY-LEMMA") or all(r["excluded"] for r in p["reps"])
                 for p in report["profiles"])
        outcome = ("EXCLUDED" if a.proof else "EXCLUDED-EXPLORATION (no proofs; not a certificate)") if ok else \
            "NOT EXCLUDED (open candidates)"
    if a.profiles is not None and outcome.startswith("EXCLUDED"):
        outcome += " [PARTIAL: selected profiles only]"
    report.update({"outcome": outcome, "excluded": outcome == "EXCLUDED", "guard_tripped": G.tripped,
                   "peak_rss_bytes_sampled": G.peak_rss, "bytes_written_before_report": G.written,
                   "min_free_bytes_sampled": G.min_free})
    path = a.out or os.path.join(LANE, "evidence", "large_t_joint6_t%d_e%d%s.json" % (
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
