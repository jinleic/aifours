#!/usr/bin/env python3
"""large_t_lex3.py: engine v3 for structured exclusion of (t, e). Lane ame46-support.

v3 is a new file. Engine v2 (large_t_lex.py, cde05b00...) and its outputs stay untouched. v3 imports v2's guard,
solver wrapper, stream checker, lex-leader generators and in-memory completion CNF, and the frozen engine's CNF builder
and per-solution checks. It changes only the following:
 1. PRE-FILTER (before any N-CNF). A profile is skipped, with status EXCLUDED-BY-LEMMA, if
    (a) Lemma 17 (officer counting, written) gives f(alpha) < 0 for some alpha in 0..4; or, with
        --officer-prefilter,
    (b) the profile-level officer-placement CNF of Lemma 18 (code/profile_officer_cnf.py: C1 every non-hole-type
        line has exactly one officer, C2 at most one officer per line in V_j x V_k, C3 exactly |V_k| - d_{j,a}
        officer-carrying lines (a, b in V_k)) is UNSAT. In proof mode that needs a gzip LRAT stream verified by both
        checkers; its CNF SHA-256 and stream SHA-256 are stored.
    Skipping is sound because either condition proves that no AME state has the profile, for every e.
 2. STORED CERTIFICATES, as the parent required at 13:2x:
    - every phase exclusion stores the explicit certificate (code/phase_cert.py format) and its verification;
    - every moduli exclusion stores the verified Stiemke vector;
    - every completion exclusion stores N, the SHA-256 of the in-memory completion CNF and the SHA-256 of the
      proof stream;
    - every final enumeration stores the SHA-256 of the exact CNF text given to the solver.
 3. RUN-WIDE FREE-SPACE FLOOR. The run does not start if the filesystem has fewer than --free-floor bytes free
    (default 12,000,000,000). The watchdog trips if free space drops below the floor during the run, then sends
    SIGTERM with a bounded wait. The case is then UNKNOWN.
Everything else (pre-bounds, RSS watchdog, exact disk accounting, solution cap, time limit, UNKNOWN semantics, I/O)
is v2's (review/ENGINE_V2_GUARD.r1.md).
"""
import argparse
import hashlib
import json
import os
import subprocess
import time

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import phase_cert as pcert
import phase_check as pc
import profile_officer_cnf as poc

LANE, OUT = v2.LANE, os.path.join(v2.LANE, "explore", "large_t_lex3")


def free_bytes():
    out = subprocess.run(["df", "-k", LANE], capture_output=True, text=True).stdout.splitlines()
    return int(out[1].split()[3]) * 1024


class Guard3(v2.Guard):
    def __init__(self, rss_cap, disk_budget, free_floor):
        self.free_floor = free_floor
        self.min_free = None
        super().__init__(rss_cap, disk_budget)

    def _watch(self):
        while not self._stop:
            total = self._rss(os.getpid())
            ch = self.child
            if ch is not None and ch.poll() is None:
                total += self._rss(ch.pid)
            self.peak_rss = max(self.peak_rss, total)
            if total > self.rss_cap:
                self.trip("RSS %d B > cap %d B" % (total, self.rss_cap))
            s = self.stream
            if s is not None and os.path.exists(s) and self.written + os.path.getsize(s) > self.disk_budget:
                self.trip("disk: %d B written + growing stream %d B > budget %d B" %
                          (self.written, os.path.getsize(s), self.disk_budget))
            fb = free_bytes()
            self.min_free = fb if self.min_free is None else min(self.min_free, fb)
            if fb < self.free_floor:
                self.trip("filesystem free %d B < floor %d B" % (fb, self.free_floor))
            if self.tripped is not None:
                self.terminate_child()
            time.sleep(1.0)


def alpha_family(prof, t, h):
    V = [len(p) for p in prof]
    s1 = 6 * sum(V) - 4 * h
    s2 = sum(V[i] * V[j] for i in range(4) for j in range(i + 1, 4)) - 6 * h
    return [s2 - a * s1 + a * (a + 1) // 2 * t for a in range(5)]


def compact_certificate(cert):
    """Parent's integer-coefficient format: [{"w": w, "k": k, "corners": [...]}], zero coefficients omitted. The
    repeated-entry format of phase_cert.py is equivalent: an entry repeated |w| times with sign sign(w)."""
    acc = {}
    for ent in cert:
        key = (ent["k"], tuple(ent["corners"]))
        acc[key] = acc.get(key, 0) + ent["sign"]
    return [{"w": w, "k": k, "corners": list(c)} for (k, c), w in acc.items() if w != 0]


def run(a):
    t, e, h = a.t, a.e, 36 - a.t
    os.makedirs(OUT, exist_ok=True)
    start_bytes = v2.lane_bytes()
    budget = min(int(a.disk_budget), v2.CAP - v2.HEADROOM - start_bytes)
    fb0 = free_bytes()
    G = Guard3(int(a.rss_cap), budget, int(a.free_floor))
    report = {"engine": "large_t_lex3 v3", "t": t, "e": e, "h": h, "mode": "proof" if a.proof else "exploration",
              "caps": {"rss_cap_bytes": int(a.rss_cap), "disk_budget_bytes": budget, "max_solutions": a.max_solutions,
                       "max_product_space": a.max_product, "max_group_order": a.max_group,
                       "max_est_memory_bytes": a.max_mem, "solver_time_limit_s": a.time_limit,
                       "free_floor_bytes": int(a.free_floor), "officer_prefilter": a.officer_prefilter},
              "lane_bytes_at_start": start_bytes, "free_bytes_at_start": fb0, "lane_cap_bytes": v2.CAP,
              "headroom_bytes": v2.HEADROOM, "profiles": []}
    if budget <= 0:
        G.trip("no disk budget left under the lane cap")
    if fb0 < int(a.free_floor):
        G.trip("filesystem free %d B < floor %d B at start" % (fb0, int(a.free_floor)))
    for prof in lte.profiles(h):
        if G.tripped:
            break
        entry = {"profile": [list(p) for p in prof], "reps": []}
        report["profiles"].append(entry)
        fam = alpha_family(prof, t, h)
        entry["lemma17_f"] = fam
        if min(fam) < 0:
            entry.update({"status": "EXCLUDED-BY-LEMMA", "lemma": "Lemma 17 (officer counting)",
                          "alpha": min(range(5), key=lambda k: fam[k])})
            continue
        if a.officer_prefilter:
            F = poc.build(prof)
            otext = v2.dimacs(F.nv, F.clauses)
            ost, _ = v2.solve(G, otext, a.time_limit)
            if G.tripped:
                entry.update({"status": "UNKNOWN", "unknown_reason": "guard tripped in officer pre-filter"})
                break
            entry["officer_cnf_sha256"] = hashlib.sha256(otext.encode()).hexdigest()
            entry["officer_cnf_status"] = {10: "SAT", 20: "UNSAT"}.get(ost, "UNKNOWN(%d)" % ost)
            if ost == 20:
                tag0 = "t%d_" % t + "_".join("-".join(map(str, p)) for p in prof)
                if a.proof:
                    gzp = os.path.join(OUT, tag0 + ".officer.lrat.gz")
                    st2, _ = v2.solve(G, otext, a.time_limit, gzp)
                    if G.tripped or st2 != 20:
                        entry.update({"status": "UNKNOWN", "unknown_reason": "officer pre-filter proof run"})
                        continue
                    chk = v2.check_stream(G, otext, gzp)
                    chk["proof"] = os.path.relpath(gzp, LANE)
                    chk["proof_gz_sha256"] = hashlib.sha256(open(gzp, "rb").read()).hexdigest()
                    entry["officer_proof"] = chk
                    if not (chk["C"]["verified"] and chk["py"]["verified"]):
                        entry.update({"status": "UNKNOWN", "unknown_reason": "officer proof not verified"})
                        continue
                entry.update({"status": "EXCLUDED-BY-LEMMA", "lemma": "Lemma 18 (officer placement CNF UNSAT)"})
                continue
        pb = v2.pre_bounds(prof, h, e)
        entry["pre_bounds"] = pb
        if not pb["fits"]:
            entry.update({"status": "EMPTY", "note": "2h+e exceeds product space", "solutions": 0})
            continue
        if pb["product_space"] > a.max_product or pb["group_order"] > a.max_group or pb["est_memory_bytes"] > a.max_mem:
            entry.update({"status": "UNKNOWN", "unknown_reason": "pre-bounds exceeded (not attempted)"})
            continue
        tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)
        S = ltg.SmallGen(prof)
        S.build_gen(e, h)
        gens = v2.generators(S)
        for g in gens:
            v2.add_lex_leader(S, g)
        blocks, sols, status, lrat_info, final_sha = [], [], None, None, None
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
            if len(sols) > a.max_solutions:
                status = "UNKNOWN"
                entry["unknown_reason"] = "solution cap exceeded"
                break
        entry.update({"status": status, "solutions": len(sols), "generators": len(gens), "final_proof": lrat_info,
                      "final_cnf_sha256": final_sha})
        if status == "ENUMERATED":
            for k, N in enumerate(sols):
                if G.tripped:
                    entry["status"] = "UNKNOWN"
                    break
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
                            r.update({"phase_complex_consistent": False, "phase_certificate": cert,
                                      "phase_certificate_compact": compact_certificate(cert),
                                      "phase_certificate_check": cwhy, "phase_obstruction_verified": cok})
                        else:
                            eqs = pc.block_equations(set(N))
                            elems = sorted({x for _, tt in eqs for x, _ in tt})
                            ph = pc.phase_consistency(eqs, elems)
                            r["phase_complex_consistent"] = ph["complex_consistent"]
                            r["phase_obstruction_verified"] = ph.get("obstruction_verified")
                        if r.get("phase_complex_consistent"):
                            ctext, nall = v2.completion_text(N)
                            r["completion_allowed_points"] = nall
                            r["completion_cnf_sha256"] = hashlib.sha256(ctext.encode()).hexdigest()
                            if a.proof:
                                gzp = os.path.join(OUT, tag + "_sol%d_completion.lrat.gz" % k)
                                st, _ = v2.solve(G, ctext, a.time_limit, gzp)
                                if st == 20 and not G.tripped:
                                    r["completion_proof"] = v2.check_stream(G, ctext, gzp)
                                    r["completion_proof"]["proof"] = os.path.relpath(gzp, LANE)
                                    r["completion_proof"]["proof_gz_sha256"] = hashlib.sha256(
                                        open(gzp, "rb").read()).hexdigest()
                            else:
                                st, _ = v2.solve(G, ctext, a.time_limit)
                            r["completion_status"] = {10: "SAT", 20: "UNSAT"}.get(st, "UNKNOWN(%d)" % st)
                cp = r.get("completion_proof") or {}
                r["excluded"] = bool((not r["components_ok"]) or r.get("moduli_excluded", False) or
                                     (r.get("phase_complex_consistent") is False and r.get("phase_obstruction_verified"))
                                     or (r.get("completion_status") == "UNSAT" and
                                         (not a.proof or (cp.get("C", {}).get("verified") and
                                                          cp.get("py", {}).get("verified")))))
                entry["reps"].append(r)
                if str(r.get("completion_status", "")).startswith("UNKNOWN"):
                    entry["status"] = "UNKNOWN"
                    entry["unknown_reason"] = "completion solver status %s" % r["completion_status"]
        print(json.dumps({k: v for k, v in entry.items() if k not in ("reps", "farkas_certificate")}), flush=True)
    unknown = G.tripped is not None or any(p.get("status") == "UNKNOWN" for p in report["profiles"])
    if unknown:
        outcome = "UNKNOWN"
    else:
        ok = all(p["status"] in ("EMPTY", "EXCLUDED-BY-LEMMA") or
                 (all(r["excluded"] for r in p["reps"]) and
                  (not a.proof or (p["final_proof"]["C"]["verified"] and p["final_proof"]["py"]["verified"])))
                 for p in report["profiles"])
        outcome = ("EXCLUDED" if a.proof else "EXCLUDED-EXPLORATION (no proofs; not a certificate)") if ok else \
            "NOT EXCLUDED (open candidates)"
    report.update({"outcome": outcome, "excluded": outcome == "EXCLUDED", "guard_tripped": G.tripped,
                   "peak_rss_bytes_sampled": G.peak_rss, "bytes_written_before_report": G.written,
                   "min_free_bytes_sampled": G.min_free})
    G.stop()
    path = a.out or os.path.join(LANE, "evidence", "large_t_lex3_t%d_e%d%s.json" % (t, e, "" if a.proof else "_explore"))
    with open(path, "w") as fh:
        json.dump(report, fh, indent=1)
    print("t=%d e=%d outcome: %s | guard: %s | peak RSS sampled %d MiB | written %d B | min free %s B" % (
        t, e, outcome, G.tripped, G.peak_rss // 2 ** 20, G.written, G.min_free))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--officer-prefilter", action="store_true")
    ap.add_argument("--rss-cap", type=float, default=6 * 2 ** 30, help="bytes")
    ap.add_argument("--disk-budget", type=float, default=512 * 2 ** 20, help="bytes")
    ap.add_argument("--free-floor", type=float, default=12_000_000_000, help="bytes free on the filesystem")
    ap.add_argument("--max-solutions", type=int, default=5000)
    ap.add_argument("--max-product", type=int, default=1296)
    ap.add_argument("--max-group", type=int, default=10 ** 15)
    ap.add_argument("--max-mem", type=float, default=2 * 2 ** 30, help="bytes, estimated in-memory CNF")
    ap.add_argument("--time-limit", type=int, default=600)
    ap.add_argument("--out", default=None)
    run(ap.parse_args())
