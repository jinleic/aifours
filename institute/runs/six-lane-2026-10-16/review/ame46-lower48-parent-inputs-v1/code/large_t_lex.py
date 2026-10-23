#!/usr/bin/env python3
"""large_t_lex.py: engine v2 for structured exclusion of (t, e), with resource guards. Lane ame46-support.

The frozen engine large_t_gen.py (28c0c1f9...) and its 18 certificate inputs stay untouched. v2 only IMPORTS from
large_t_gen.py, large_t_e0.py and phase_check.py: the CNF builder SmallGen.build_gen, component_checks,
moduli_certificate, profiles, completion_cnf's constraint logic and the exact phase check. What v2 changes:

1. ENUMERATION (no orbit materialisation). It adds lex-leader constraints X <=_lex g(X) for a generating set of H
   (adjacent transpositions of values inside each d-class of V_i, and adjacent transpositions of coordinates with
   equal partitions), and blocks each found solution individually.
   Soundness: every H-orbit of solutions contains its lexicographically least member X*, and X* <=_lex g(X*) for
   every g in H, in particular for the generators. When the loop ends with UNSAT (CNF + lex constraints + blocking
   clauses), every orbit's least member has been found. Hence every solution is in the H-orbit of a found solution,
   and analysing each found solution covers the orbits. Exclusion transfers along H as in large_t_gen.py.
2. I/O WITHOUT LARGE FILES. CNFs are generated in memory and passed to CaDiCaL on stdin. In proof mode CaDiCaL
   writes a gzip-compressed text LRAT stream (<tag>.lrat.gz). The two independent checkers read the CNF from a FIFO
   fed by a Python thread, and the proof from `gzip -dc` through a pipe, so no uncompressed proof bytes are stored.
3. RESOURCE GUARD (a hit means a cooperative stop and UNKNOWN; never a proof, never a partial result):
   - pre-bounds before any group or CNF generation: product-space size, group order |H| (by formula, not
     materialised), estimated clause and literal counts and in-memory CNF bytes; above a bound the profile is UNKNOWN
     without being attempted;
   - RSS watchdog, sampling every 1 s the resident set of this process plus the live solver or checker child (ps).
     Above the cap (default 6 GiB) the child gets SIGTERM with a bounded wait (30 s), never SIGKILL;
   - exact disk accounting against the lane cap: at start, budget = min(--disk-budget, 10 GiB - 256 MiB - du(lane)).
     Every byte this run writes is counted (compressed proofs and the report). The watchdog also checks the size of a
     growing .gz proof stream every second;
   - solution cap per profile and CaDiCaL's native time limit (-t) per call.
   An UNKNOWN profile makes the case UNKNOWN (excluded = false).
Modes: --proof (certification: compressed LRAT streams checked by both checkers); default proof-free exploration,
whose outcome is never a certificate.
"""
import argparse
import itertools
import json
import math
import os
import signal
import subprocess
import sys
import threading
import time

import large_t_e0 as lte
import large_t_gen as ltg
import phase_check as pc

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "explore", "large_t_lex")
CAP = 10 * 2 ** 30
HEADROOM = 256 * 2 ** 20


def lane_bytes():
    du = int(subprocess.run(["du", "-sk", LANE], capture_output=True, text=True).stdout.split()[0]) * 1024
    app = 0
    for d, _, fs in os.walk(LANE):
        for f in fs:
            p = os.path.join(d, f)
            if os.path.isfile(p) and not os.path.islink(p):
                app += os.path.getsize(p)
    return max(du, app)


class Guard:
    def __init__(self, rss_cap, disk_budget):
        self.rss_cap, self.disk_budget = rss_cap, disk_budget
        self.written, self.tripped, self.child, self.stream = 0, None, None, None
        self.peak_rss = 0
        self._stop = False
        threading.Thread(target=self._watch, daemon=True).start()

    @staticmethod
    def _rss(pid):
        r = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True)
        v = r.stdout.strip()
        return int(v) * 1024 if v.isdigit() else 0

    def trip(self, why):
        if self.tripped is None:
            self.tripped = why
            self.terminate_child()

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
            if self.tripped is not None:
                self.terminate_child()            # also stops any child started after the trip
            time.sleep(1.0)

    def terminate_child(self):
        ch = self.child
        if ch is not None and ch.poll() is None:
            ch.send_signal(signal.SIGTERM)
            for _ in range(30):                       # bounded wait; never SIGKILL
                if ch.poll() is not None:
                    break
                time.sleep(1.0)

    def account(self, path):
        if os.path.exists(path):
            self.written += os.path.getsize(path)
        if self.written > self.disk_budget:
            self.trip("disk: written %d B > budget %d B" % (self.written, self.disk_budget))

    def stop(self):
        self._stop = True


def dimacs(nv, clauses):
    return "p cnf %d %d\n" % (nv, len(clauses)) + "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)


def solve(G, text, tlimit, proof_path=None):
    """Returns (returncode, model). A tripped guard means no solver call (returncode -1)."""
    if G.tripped is not None:
        return -1, set()
    cmd = ["cadical", "-q", "-t", str(tlimit)]
    if proof_path:
        cmd += ["--lrat", "--binary=false", "-", proof_path]
        G.stream = proof_path
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    G.child = p
    try:
        out, _ = p.communicate(input=text)
    except BrokenPipeError:
        out = ""
        p.wait()
    G.child, G.stream = None, None
    if proof_path:
        G.account(proof_path)
    model = set()
    for line in out.splitlines():
        if line.startswith("v "):
            for tok in line.split()[1:]:
                v = int(tok)
                if v > 0:
                    model.add(v)
    return p.returncode, model


def check_stream(G, text, gz_path):
    """Both checkers. The CNF comes through a FIFO fed by a thread, the proof through `gzip -dc`; nothing large is
    stored."""
    res = {}
    if G.tripped is not None:
        return {"C": {"verified": False, "msg": "guard tripped; not checked"},
                "py": {"verified": False, "msg": "guard tripped; not checked"}}
    fifo = gz_path + ".cnf.fifo"
    if not os.path.exists(fifo):
        os.mkfifo(fifo)
    for name, cmd in (("C", [os.path.join(HERE, "lratcheck"), fifo, "/dev/stdin"]),
                      ("py", [sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), fifo, "/dev/stdin",
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
        res[name] = {"verified": p.returncode == 0 and "s VERIFIED" in out,
                     "msg": " | ".join(out.strip().splitlines()) or err.strip()}
    return res


def group_order(prof):
    sig = [tuple(p) for p in prof]
    order = 1
    for s in set(sig):
        order *= math.factorial(sig.count(s))
    for p in prof:
        for part in set(p):
            order *= math.factorial(p.count(part))
    return order


def pre_bounds(prof, h, e):
    sizes = [len(p) for p in prof]
    P = sizes[0] * sizes[1] * sizes[2] * sizes[3]
    lines = sum(sizes[i] * sizes[j] for i, j in itertools.combinations(range(4), 2))
    aux = 0
    for (a, b), (c, d) in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))):
        R, C = sizes[a] * sizes[b], sizes[c] * sizes[d]
        aux += R * (R - 1) // 2 * C + C * (C - 1) // 2 * R
    lits = aux * (3 + max(sizes[0] * sizes[1], 1)) + lines * 40 + P * 400
    return {"product_space": P, "group_order": group_order(prof), "est_literals": lits,
            "est_memory_bytes": lits * 80, "fits": 2 * h + e <= P}


def generators(S):
    gens = []
    sig = [tuple(p) for p in S.prof]
    for i in range(3):
        if sig[i] == sig[i + 1]:
            gens.append({x: tuple(x[i + 1] if k == i else x[i] if k == i + 1 else x[k] for k in range(4))
                         for x in S.points})
    for i in range(4):
        classes = {}
        for a in S.V[i]:
            classes.setdefault(S.d[i][a], []).append(a)
        for cl in classes.values():
            for a, b in zip(cl, cl[1:]):
                gens.append({x: tuple((b if x[k] == a else a if x[k] == b else x[k]) if k == i else x[k]
                                      for k in range(4)) for x in S.points})
    return gens


def add_lex_leader(S, gmap):
    """X <=_lex g(X) over the variables in the order S.points; e_k <-> (prefixes equal)."""
    prev = None
    for p in S.points:
        x, y = S.var[p], S.var[gmap[p]]
        if x == y:
            continue
        S.cl.append([-x, y] if prev is None else [-prev, -x, y])
        e = S.new()
        if prev is None:
            S.cl += [[-x, -y, e], [x, y, e]]
        else:
            S.cl += [[-e, prev], [-prev, -x, -y, e], [-prev, x, y, e]]
        S.cl += [[-e, -x, y], [-e, x, -y]]
        prev = e


def completion_text(N):
    """Same constraints as large_t_e0.completion_cnf, generated in memory."""
    import ame_e0_cnf as base
    holes = {P: {tuple(x[i] for i in P) for x in N} for P in lte.PAIRS}
    allowed = [x for x in itertools.product(range(6), repeat=4)
               if all(tuple(x[i] for i in P) not in holes[P] for P in lte.PAIRS)]
    var = {x: k + 1 for k, x in enumerate(allowed)}
    F = base.CNF()
    F.nv = len(allowed)
    for P in lte.PAIRS:
        for z in itertools.product(range(6), repeat=2):
            if z in holes[P]:
                continue
            lits = [var[x] for x in allowed if tuple(x[i] for i in P) == z]
            if not lits:
                F.add([])
                continue
            F.add(lits)
            F.at_most_k(lits, 1)
    return dimacs(F.nv, F.clauses), len(allowed)


def run(a):
    t, e, h = a.t, a.e, 36 - a.t
    os.makedirs(OUT, exist_ok=True)
    start_bytes = lane_bytes()
    budget = min(int(a.disk_budget), CAP - HEADROOM - start_bytes)
    G = Guard(int(a.rss_cap), budget)
    report = {"engine": "large_t_lex v2", "t": t, "e": e, "h": h, "mode": "proof" if a.proof else "exploration",
              "caps": {"rss_cap_bytes": int(a.rss_cap), "disk_budget_bytes": budget, "max_solutions": a.max_solutions,
                       "max_product_space": a.max_product, "max_group_order": a.max_group,
                       "max_est_memory_bytes": a.max_mem, "solver_time_limit_s": a.time_limit},
              "lane_bytes_at_start": start_bytes, "lane_cap_bytes": CAP, "headroom_bytes": HEADROOM, "profiles": []}
    if budget <= 0:
        G.trip("no disk budget left under the lane cap")
    for prof in lte.profiles(h):
        if G.tripped:
            break
        pb = pre_bounds(prof, h, e)
        entry = {"profile": [list(p) for p in prof], "pre_bounds": pb, "reps": []}
        report["profiles"].append(entry)
        if not pb["fits"]:
            entry.update({"status": "EMPTY", "note": "2h+e exceeds product space", "solutions": 0})
            continue
        if pb["product_space"] > a.max_product or pb["group_order"] > a.max_group or pb["est_memory_bytes"] > a.max_mem:
            entry.update({"status": "UNKNOWN", "unknown_reason": "pre-bounds exceeded (not attempted)"})
            continue
        tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)
        S = ltg.SmallGen(prof)
        S.build_gen(e, h)
        gens = generators(S)
        for g in gens:
            add_lex_leader(S, g)
        blocks, sols, status = [], [], None
        lrat_info = None
        while True:
            if G.tripped:
                status = "UNKNOWN"
                break
            text = dimacs(S.nv, S.cl + blocks)
            st, model = solve(G, text, a.time_limit)
            if G.tripped:
                status = "UNKNOWN"
                break
            if st == 20:
                if a.proof:
                    gzp = os.path.join(OUT, tag + ".final.lrat.gz")
                    st2, _ = solve(G, text, a.time_limit, gzp)
                    if G.tripped or st2 != 20:
                        status = "UNKNOWN"
                        break
                    lrat_info = check_stream(G, text, gzp)
                    lrat_info["proof"] = os.path.relpath(gzp, LANE)
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
        entry.update({"status": status, "solutions": len(sols), "generators": len(gens), "final_proof": lrat_info})
        if status == "ENUMERATED":
            for k, N in enumerate(sols):
                if G.tripped:
                    entry["status"] = "UNKNOWN"
                    break
                r = {"N": ["".join(map(str, x)) for x in N]}
                okc, why = ltg.component_checks(N)
                r["components_ok"], r["components_reason"] = okc, why
                if okc:
                    cert = ltg.moduli_certificate(N)
                    r["moduli_excluded"] = bool(cert is not None and cert["verified"])
                    if not r["moduli_excluded"]:
                        eqs = pc.block_equations(set(N))
                        elems = sorted({x for _, tt in eqs for x, _ in tt})
                        ph = pc.phase_consistency(eqs, elems)
                        r["phase_complex_consistent"] = ph["complex_consistent"]
                        r["phase_obstruction_verified"] = ph.get("obstruction_verified")
                        if ph["complex_consistent"]:
                            ctext, nall = completion_text(N)
                            r["completion_allowed_points"] = nall
                            if a.proof:
                                gzp = os.path.join(OUT, tag + "_sol%d_completion.lrat.gz" % k)
                                st, _ = solve(G, ctext, a.time_limit, gzp)
                                if st == 20 and not G.tripped:
                                    r["completion_proof"] = check_stream(G, ctext, gzp)
                                    r["completion_proof"]["proof"] = os.path.relpath(gzp, LANE)
                            else:
                                st, _ = solve(G, ctext, a.time_limit)
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
        print(json.dumps({k: v for k, v in entry.items() if k != "reps"}), flush=True)
    unknown = G.tripped is not None or any(p.get("status") == "UNKNOWN" for p in report["profiles"])
    if unknown:
        outcome = "UNKNOWN"
    else:
        ok = all(p["status"] == "EMPTY" or (all(r["excluded"] for r in p["reps"]) and
                                            (not a.proof or (p["final_proof"]["C"]["verified"] and
                                                             p["final_proof"]["py"]["verified"])))
                 for p in report["profiles"])
        outcome = ("EXCLUDED" if a.proof else "EXCLUDED-EXPLORATION (no proofs; not a certificate)") if ok else \
            "NOT EXCLUDED (open candidates)"
    report.update({"outcome": outcome, "excluded": outcome == "EXCLUDED", "guard_tripped": G.tripped,
                   "peak_rss_bytes_sampled": G.peak_rss, "bytes_written_before_report": G.written})
    G.stop()
    path = a.out or os.path.join(LANE, "evidence", "large_t_lex_t%d_e%d%s.json" % (t, e, "" if a.proof else "_explore"))
    with open(path, "w") as fh:
        json.dump(report, fh, indent=1)
    print("t=%d e=%d outcome: %s | guard: %s | peak RSS sampled %d MiB | written %d B" % (
        t, e, outcome, G.tripped, G.peak_rss // 2 ** 20, G.written))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--rss-cap", type=float, default=6 * 2 ** 30, help="bytes")
    ap.add_argument("--disk-budget", type=float, default=512 * 2 ** 20, help="bytes")
    ap.add_argument("--max-solutions", type=int, default=5000)
    ap.add_argument("--max-product", type=int, default=1296)
    ap.add_argument("--max-group", type=int, default=10 ** 15)
    ap.add_argument("--max-mem", type=float, default=2 * 2 ** 30, help="bytes, estimated in-memory CNF")
    ap.add_argument("--time-limit", type=int, default=600)
    ap.add_argument("--out", default=None)
    run(ap.parse_args())
