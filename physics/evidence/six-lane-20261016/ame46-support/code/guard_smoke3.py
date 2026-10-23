#!/usr/bin/env python3
"""guard_smoke3.py: smoke tests for engine v3 (code/large_t_lex3.py). Lane ame46-support.

Engine runs (separate processes):
 T1 (30,0) exploration, no pre-filter effect expected on {2,2,2}^4 -> EXCLUDED-EXPLORATION; profile {3,3}{2,2,2}^3
    is EXCLUDED-BY-LEMMA (Lemma 17, f(1) = -3)
 T2 (28,0) --proof -> EXCLUDED; stored phase certificates verify; final CNF SHA recorded; streams verified by both
    checkers
 T3 (29,3) --proof -> EXCLUDED with no search (the single profile is excluded by Lemma 17)
 T4 --rss-cap 20 MiB -> UNKNOWN (RSS trip), excluded = false
 T5 --proof --disk-budget 1000 -> UNKNOWN (disk trip)
 T6 --free-floor 10^15 -> UNKNOWN (free-space floor at start), nothing attempted
 T7 --max-solutions 0 on (28,0) -> UNKNOWN (solution cap)
 T8 (28,2) --proof --officer-prefilter -> EXCLUDED; at least one profile EXCLUDED-BY-LEMMA via Lemma 18, with its
    officer-CNF stream verified by both checkers
Unit checks (in process):
 U1 the officer-placement CNF of profile {4,4}{2,2,2,2}^3 at t = 28 is UNSAT, while its Lemma 17 values are all >= 0
    (the parent's binary-code argument excludes the same profile in writing)
 U2 phase-certificate verifier negative controls (drop, flip, duplicate, re-reshape, corner outside N) are rejected
Summary: evidence/guard_smoke3.json.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUTD = os.path.join(LANE, "explore", "guard_smoke3")
PY = sys.executable

RUNS = [
    ("T1", 30, 0, [], "EXCLUDED-EXPLORATION", False, False),
    ("T2", 28, 0, ["--proof"], "EXCLUDED", False, True),
    ("T3", 29, 3, ["--proof"], "EXCLUDED", False, True),
    ("T4", 30, 0, ["--rss-cap", str(20 * 2 ** 20)], "UNKNOWN", True, False),
    ("T5", 30, 0, ["--proof", "--disk-budget", "1000"], "UNKNOWN", True, False),
    ("T6", 30, 0, ["--free-floor", str(10 ** 15)], "UNKNOWN", True, False),
    ("T7", 28, 0, ["--max-solutions", "0"], "UNKNOWN", False, False),
    ("T8", 28, 2, ["--proof", "--officer-prefilter"], "EXCLUDED", False, True),
]


def main():
    os.makedirs(OUTD, exist_ok=True)
    res, allok = [], True
    for name, t, e, args, want, want_trip, want_excl in RUNS:
        out = os.path.join(OUTD, name + ".json")
        t0 = time.time()
        p = subprocess.run([PY, "-B", os.path.join(HERE, "large_t_lex3.py"), "--t", str(t), "--e", str(e),
                            "--out", out] + args, capture_output=True, text=True, cwd=HERE,
                           env=dict(os.environ, OMP_NUM_THREADS="1"))
        rep = json.load(open(out))
        got = {"outcome": rep["outcome"], "guard": rep["guard_tripped"], "excluded": rep["excluded"],
               "statuses": [pr.get("status") for pr in rep["profiles"]], "seconds": round(time.time() - t0, 1)}
        match = (got["outcome"].startswith(want) and (rep["guard_tripped"] is not None) == want_trip and
                 rep["excluded"] == want_excl and p.returncode == 0)
        if name == "T1":
            match &= got["statuses"][0] == "EXCLUDED-BY-LEMMA"
        if name == "T2":
            certs, finals = [], []
            for pr in rep["profiles"]:
                if pr.get("status") == "ENUMERATED":
                    finals.append(bool(pr["final_proof"]["C"]["verified"] and pr["final_proof"]["py"]["verified"]
                                       and pr.get("final_cnf_sha256")))
                    for r in pr["reps"]:
                        if r.get("phase_certificate") is not None:
                            certs.append(r.get("phase_certificate_check") == "ok")
            got["phase_certificates"] = len(certs)
            got["all_final_streams_verified_and_cnf_sha"] = all(finals) and bool(finals)
            match &= all(certs) and got["all_final_streams_verified_and_cnf_sha"]
        if name == "T3":
            match &= all(s == "EXCLUDED-BY-LEMMA" for s in got["statuses"])
        allok &= match
        res.append({"run": name, "t": t, "e": e, "args": args, "got": got, "match": match,
                    "report": os.path.relpath(out, LANE), "exit": p.returncode,
                    "stderr_tail": p.stderr.strip().splitlines()[-3:] if p.stderr else []})
        print(name, "match" if match else "MISMATCH", got["outcome"], "| guard:", got["guard"], flush=True)
    sys.path.insert(0, HERE)
    import large_t_lex3 as v3
    import large_t_lex as v2
    import profile_officer_cnf as poc
    prof = [(4, 4), (2, 2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2)]
    F = poc.build(prof)
    st = poc.solve(F, 60)
    fam = v3.alpha_family(prof, 28, 8)
    u1 = bool(st == 20 and min(fam) >= 0)
    res.append({"run": "U1", "officer_cnf_status": st, "lemma17_f": fam, "match": u1})
    print("U1", "match" if u1 else "MISMATCH", st, fam, flush=True)
    t8 = json.load(open(os.path.join(OUTD, "T8.json")))
    l18 = [pr for pr in t8["profiles"] if pr.get("lemma", "").startswith("Lemma 18")]
    u3 = bool(l18) and all(pr["officer_proof"]["C"]["verified"] and pr["officer_proof"]["py"]["verified"]
                           for pr in l18)
    res.append({"run": "T8-detail", "lemma18_profiles": [pr["profile"] for pr in l18], "match": u3})
    print("T8-detail", "match" if u3 else "MISMATCH", [pr["profile"] for pr in l18], flush=True)
    allok &= u3
    t2 = json.load(open(os.path.join(OUTD, "T2.json")))
    N = cert = None
    for pr in t2["profiles"]:
        for r in pr.get("reps", []):
            if r.get("phase_certificate"):
                N, cert = r["N"], r["phase_certificate"]
                break
        if cert:
            break
    import v2_receipt_r2 as rr
    ctl = rr.cert_controls(N, cert) if cert else []
    u2 = bool(ctl) and all(c["rejected"] for c in ctl)
    res.append({"run": "U2", "controls": ctl, "match": u2})
    print("U2", "match" if u2 else "MISMATCH", [c["mutation"] + ":" + c["reason"] for c in ctl], flush=True)
    allok &= u1 and u2
    summary = {"runs": res, "all_required_true": bool(allok), "python": sys.version.split()[0]}
    with open(os.path.join(LANE, "evidence", "guard_smoke3.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print("all_required_true:", allok)
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
