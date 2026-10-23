#!/usr/bin/env python3
"""Cycle-2 status: per multiset and per A2 case, the M1 decision (pass-1 verdict plus a
checked proof from cycle 1, the cycle-2 streamed proof pass, the A3 split or the direct
CaDiCaL-LRAT run) and the M2 decision (gen_skel_b case matched by isomorphism, encode_skel_b
+ CaDiCaL-LRAT). Writes STATUS2.json. Read-only over results.
"""
import collections
import json
import os

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def jl(p):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return None


def main():
    idx = json.load(open(os.path.join(LANE, "cases19skel", "index.json")))
    per = collections.defaultdict(lambda: collections.Counter())
    undecided_m1, undecided_m2, sat = [], [], []
    maps = {}
    for mi in range(1, 10):
        m = jl(os.path.join(LANE, "cycle2", "skel-b", "compare-map-ms%02d.json" % mi))
        maps[mi] = m["a_to_b"] if m and m.get("bijection") else None
    for c in idx["cases"]:
        tag, mi, si = c["tag"], c["multiset"], c["skel"]
        p1 = jl(os.path.join(LANE, "cases19skel", "results", tag + ".json"))
        pc1 = jl(os.path.join(LANE, "cases19skel", "proofcheck", tag + ".json"))
        ps2 = jl(os.path.join(LANE, "cycle2", "proofstream", tag + ".json"))
        dr = jl(os.path.join(LANE, "cycle2", "hard", tag + ".json"))
        a3 = jl(os.path.join(LANE, "cycle2", "a3", tag, "summary.json"))
        m1 = "UNKNOWN"
        if p1 and p1["status"] == "UNSAT" and ((pc1 and pc1.get("ok")) or (ps2 and ps2.get("ok"))):
            m1 = "UNSAT_checked"
        elif dr and dr["status"] == "UNSAT" and dr.get("checked") and dr.get("cnf_matches_pass1_sha"):
            m1 = "UNSAT_checked"
        elif a3 and a3.get("decided_unsat"):
            m1 = "UNSAT_checked"
        elif (dr and dr["status"] == "SAT") or (a3 and a3.get("SAT")):
            m1 = "SAT"
        elif p1 and p1["status"] == "UNSAT":
            m1 = "UNSAT_unchecked"
        m2 = "UNKNOWN"
        if maps.get(mi) is not None:
            bi = maps[mi][si]
            r2 = jl(os.path.join(LANE, "cycle2", "m2skel", "ms%02d_b%05d.json" % (mi, bi)))
            if r2:
                m2 = "UNSAT_checked" if (r2["status"] == "UNSAT" and r2["checked"]) else r2["status"]
        per["ms%02d" % mi]["cases"] += 1
        per["ms%02d" % mi]["M1_" + m1] += 1
        per["ms%02d" % mi]["M2_" + m2] += 1
        both = m1 == "UNSAT_checked" and m2 == "UNSAT_checked"
        per["ms%02d" % mi]["both_checked_unsat"] += both
        if m1 != "UNSAT_checked":
            undecided_m1.append(tag)
        if m2 != "UNSAT_checked":
            undecided_m2.append(tag)
        if "SAT" in (m1, m2):
            sat.append(tag)
    e0 = jl(os.path.join(LANE, "STATUS.json"))["E0_ms00"]
    out = {"E0_ms00": e0, "per_multiset": {k: dict(v) for k, v in sorted(per.items())},
           "m1_not_checked_unsat": len(undecided_m1), "m2_not_checked_unsat": len(undecided_m2),
           "sat_cases": sat, "m1_open_tags": undecided_m1[:400], "m2_open_tags": undecided_m2[:400]}
    json.dump(out, open(os.path.join(LANE, "STATUS2.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if not k.endswith("_tags")}, indent=1))


if __name__ == "__main__":
    main()
