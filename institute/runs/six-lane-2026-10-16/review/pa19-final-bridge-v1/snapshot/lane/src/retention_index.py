#!/usr/bin/env python3
"""Per-case proof-retention index (parent route A, 2026-10-17): for every A2 case and every E0
graph, list each certificate record that counts (drat-trim verified; lrat-check-only and
lratstrict-only records are listed as not counted) with: path, CNF SHA-256, solver command /
version / seed, verdict, streamed proof byte count and SHA-256, drat-trim time, and whether the
proof bytes are retained on disk (only cycle-1 stored DRATs: cases19skel/proof/<tag>.drat for
path a, cases19q0/proof/gNNN.drat for E0 M1). Read-only; writes cycle2/proof-retention-index.json.
"""
import glob
import json
import os
import re

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def jl(p):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return None


def rel(p):
    return os.path.relpath(p, LANE)


def counted(r):
    if not r or r.get("status") != "UNSAT":
        return False
    if "lratstrict_verified" in r:
        return False
    return bool(r.get("checked")) and bool(r.get("drat_trim_verified"))


def streamed(path, r, kind):
    return {"record": rel(path), "kind": kind, "status": r.get("status"), "counted": counted(r),
            "cnf_sha256": r.get("cnf_sha256"), "solver": r.get("solver"), "solver_info": r.get("solver_info"),
            "stream_check_revision": r.get("stream_check_revision"), "proof_bytes": r.get("drat_bytes"),
            "proof_sha256": r.get("drat_sha256"), "check_seconds": r.get("check_seconds"),
            "solve_seconds": r.get("solve_seconds"), "proof_retained": False}


def main():
    idx = json.load(open(os.path.join(LANE, "cases19skel", "index.json")))
    out = {"A2": {}, "E0": {}}
    for c in idx["cases"]:
        tag = c["tag"]
        recs = []
        p1 = jl(os.path.join(LANE, "cases19skel", "results", tag + ".json"))
        pc_path = os.path.join(LANE, "cases19skel", "proofcheck", tag + ".json")
        pc = jl(pc_path)
        if pc:
            drat = os.path.join(LANE, "cases19skel", "proof", tag + ".drat")
            recs.append({"record": rel(pc_path), "kind": "M1 path a (cycle-1 stored DRAT, drat-trim)",
                         "status": (p1 or {}).get("status"), "counted": bool(pc.get("ok") and pc.get("drat_trim_verified")),
                         "cnf_sha256": pc.get("cnf_sha256"), "solver": "kissat 4.0.4 -q --seed=1 (cycle-1 run_proofpass.py)",
                         "proof_bytes": pc.get("drat_bytes"), "proof_sha256": pc.get("drat_sha256"),
                         "check_seconds": pc.get("check_seconds"), "proof_retained": os.path.exists(drat),
                         "proof_path": rel(drat) if os.path.exists(drat) else None})
        for sub, kind in (("proofstream", "M1 path b (streamed kissat DRAT)"), ("hard5", "M1 path c5 (streamed DRAT)"),
                          ("hard", "cycle-2 CaDiCaL LRAT + lrat-check (NOT counted)")):
            p = os.path.join(LANE, "cycle2", sub, tag + ".json")
            r = jl(p)
            if r:
                e = streamed(p, r, kind)
                if sub == "hard" and "cadical" in (r.get("solver") or ""):
                    e["counted"] = False
                recs.append(e)
        for sub, kind in (("a3", "M1 path d (A3 subcases)"), ("part", "M1 path e (A3'/A3'' subcases/batches)")):
            d = os.path.join(LANE, "cycle2", sub, tag)
            if os.path.isdir(d):
                files = sorted(glob.glob(os.path.join(d, "f*.json")) + glob.glob(os.path.join(d, "batch_*.json")))
                items = []
                for f in files:
                    if not re.match(r".*/(f\d+(_exact|_r2|_r3)?|batch_\d+_\d+(_r2|_r3)?)\.json$", f):
                        continue
                    r = jl(f)
                    if r:
                        e = streamed(f, r, kind)
                        if f.endswith("_r2.json"):
                            e["counted"] = False
                        items.append(e)
                recs.append({"kind": kind, "dir": rel(d), "n_records": len(items),
                             "n_counted": sum(1 for e in items if e["counted"]), "items": items})
        out["A2"][tag] = recs
    q0 = os.path.join(LANE, "cases19q0", "results")
    for f in sorted(glob.glob(os.path.join(q0, "g*.check.json"))):
        g = os.path.basename(f).split(".")[0]
        ck = jl(f)
        drat = os.path.join(LANE, "cases19q0", "proof", g + ".drat")
        recs = [{"record": rel(f), "kind": "E0 M1 (cycle-1 stored DRAT, drat-trim)",
                 "counted": bool(ck.get("ok") and ck.get("drat_trim_verified")), "cnf_sha256": ck.get("cnf_sha256_now"),
                 "proof_bytes": ck.get("proof_bytes"), "proof_sha256": ck.get("proof_sha256"),
                 "check_seconds": ck.get("drat_trim_seconds"), "proof_retained": os.path.exists(drat),
                 "proof_path": rel(drat) if os.path.exists(drat) else None}]
        p = os.path.join(LANE, "m2q0c", "results", g + ".json")
        r = jl(p)
        if r:
            recs.append(streamed(p, r, "E0 M2' re-cert (CaDiCaL DRAT -> drat-trim)"))
        p = os.path.join(LANE, "m2q0b", "results", g + ".json")
        if os.path.exists(p):
            recs.append({"record": rel(p), "kind": "E0 M2' cycle 1 (CaDiCaL LRAT + lrat-check, NOT counted)", "counted": False})
        out["E0"][g] = recs
    m2 = {}
    for sub in ("m2skel_drat", "m2skel_strict"):
        for f in sorted(glob.glob(os.path.join(LANE, "cycle2", sub, "*.json"))):
            r = jl(f)
            if r:
                m2[rel(f)] = streamed(f, r, "M2 direct (" + sub + ")")
    for f in sorted(glob.glob(os.path.join(LANE, "cycle2", "m2part_drat", "*", "batch_*.json"))):
        r = jl(f)
        if r:
            m2[rel(f)] = streamed(f, r, "M2 partial batch")
    out["M2_records"] = m2
    a2_counted = sum(1 for recs in out["A2"].values() for e in recs if e.get("counted"))
    out["summary"] = {"A2_cases": len(out["A2"]), "E0_graphs": len(out["E0"]),
                      "A2_cases_with_retained_proof": sum(1 for recs in out["A2"].values() if any(e.get("proof_retained") for e in recs)),
                      "E0_graphs_with_retained_M1_proof": sum(1 for recs in out["E0"].values() if recs[0].get("proof_retained")),
                      "M2_records": len(m2), "A2_counted_top_level_records": a2_counted,
                      "note": "proof_retained=false: streamed proof (only its byte count and SHA-256 are recorded); "
                              "re-check by deterministic re-solve with the recorded solver command"}
    json.dump(out, open(os.path.join(LANE, "cycle2", "proof-retention-index.json"), "w"))
    print(json.dumps(out["summary"], indent=1))


if __name__ == "__main__":
    main()
