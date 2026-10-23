#!/usr/bin/env python3
"""[Base strict aggregation for guard revision14: accept11/12/13/14 under the identical predicate; retired10 remains excluded. Output STATUS14_BASE.json.]
summarize11 = summarize10 with revision-13 records accepted under the SAME full predicate as revisions 11/12
(checked, drat_trim_verified, s lines exactly ['s VERIFIED'], replay_ok, reader_ok, no admission_denied, no
aborted_by_sigterm); revision-10 records are never counted (retired). Output STATUS11.json.
summarize10 text: summarize10 = summarize9 with revision-12 records accepted under the revision-11 predicate (stream_check12
only adds an admission re-check before the checker spawn). Output STATUS10.json.
summarize9 text: summarize9 = summarize8 plus revision-11 records (stream_check11: certified iff checked, drat_trim_verified,
s lines exactly ['s VERIFIED'], replay_ok, reader_ok, no admission_denied/aborted). Output STATUS9.json.
summarize8 text: summarize8 = summarize7 plus staged revision-10 records (stream_check10: certified iff checked,
drat_trim_verified, s lines exactly ['s VERIFIED'] and replay_sha256_matches). Output STATUS8.json.
summarize7 text: summarize7 (parent route A): like summarize6, but lratstrict records (stream_check revision 6,
cycle2/m2skel_strict, cycle2/m2part_strict) are NOT counted; revision-9 records count only with
drat_trim_verified and drat-trim 's ' lines exactly ['s VERIFIED']. Output STATUS7.json.
summarize6 text: summarize6 = summarize5 plus the strict LRAT pipeline (stream_check revision 6,
cadical_lrat_strict: certified iff checked and lratstrict_verified) and the M2 result trees
cycle2/m2skel_strict and cycle2/m2part_strict. Output STATUS6.json.
summarize5 docstring: aggregation with the lrat-check finding applied (read-only) -> STATUS5.json.

A result certifies UNSAT only if drat-trim verified it (own exit, rc 0, 's VERIFIED'):
  * cycle-1 stored-proof checks (cases19skel/proofcheck, cases19q0 .check.json): 'ok' requires
    drat_trim_verified;
  * stream_check rev 1-4 kissat results: require drat_trim_verified (their lrat flag is ignored);
  * stream_check rev 5 results (kissat_drat / cadical_drat): 'checked' (drat-trim only).
UNCERTIFIED (listed, never used): CaDiCaL-LRAT results (cycle2/hard/*.json with a cadical
solver, *_r2.json, m2q0b/), any result whose acceptance rested on lrat-check alone.
M1 paths per A2 case: (a) pass-1 UNSAT + cycle-1 check; (b) pass-1 UNSAT + cycle-2 streamed
check; (c5) cycle2/hard5 kissat/cadical DRAT result with CNF SHA = pass 1; (d) A3 full split
covered by f/_exact/_r3 results; (e) A3'/A3'' covered by f/batch/_r3 results.
M2 per case (matched by compare-map): cycle2/m2skel_drat result, or cycle2/m2part_drat batches
covering all extend_b placements. E0: M1 cycle-1 checks; M2 m2q0c (rev 5).
SAT outcomes in any path are listed. Open lists are complete.
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


def certified(r):
    if not r or r.get("status") != "UNSAT":
        return False
    if "lratstrict_verified" in r:
        return False
    if r.get("stream_check_revision") == 8:
        return False
    if r.get("stream_check_revision") in (11, 12, 13, 14):
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified")) and \
            (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"] and r.get("replay_ok") is True and \
            r.get("reader_ok") is True and not r.get("admission_denied") and not r.get("aborted_by_sigterm")
    if r.get("stream_check_revision") == 10:
        return False  # rev-10 records were retired (archive/rev10-superseded-20261017T160921); never counted
    if r.get("stream_check_revision") == 9:
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified")) and \
            (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"]
    if r.get("stream_check_revision") == 5:
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified"))
    return bool(r.get("drat_trim_verified")) and bool(r.get("checked"))


def split_cover(d, n, sats, label):
    cov = set()
    for f in glob.glob(os.path.join(d, "f*.json")):
        m = re.match(r".*/f(\d+)(_exact|_r2|_r3)?\.json$", f)
        if not m:
            continue
        r = jl(f)
        if r and r.get("status") == "SAT":
            sats.append((label, os.path.relpath(f, LANE)))
        if m.group(2) == "_r2":
            continue
        if certified(r):
            cov.add(int(m.group(1)))
    for f in glob.glob(os.path.join(d, "batch_*.json")):
        r = jl(f)
        if r and r.get("status") == "SAT":
            sats.append((label, os.path.relpath(f, LANE)))
        if f.endswith("_r2.json"):
            continue
        if certified(r):
            idx = r.get("indices") or []
            if "multiset" in r and len(idx) == 2:
                idx = list(range(idx[0], idx[1] + 1))
            cov.update(idx)
    return cov


def main():
    idx = json.load(open(os.path.join(LANE, "cases19skel", "index.json")))
    maps = {}
    for mi in range(1, 10):
        m = jl(os.path.join(LANE, "cycle2", "skel-b", "compare-map-ms%02d.json" % mi))
        maps[mi] = m["a_to_b"] if m and m.get("bijection") else None
    per, open_m1, open_m2, sats, uncert = {}, [], [], [], []
    for c in idx["cases"]:
        tag, mi, si = c["tag"], c["multiset"], c["skel"]
        p1 = jl(os.path.join(LANE, "cases19skel", "results", tag + ".json"))
        if p1 and p1["status"] == "SAT":
            sats.append(("pass1", tag))
        how = None
        pc = jl(os.path.join(LANE, "cases19skel", "proofcheck", tag + ".json"))
        ps = jl(os.path.join(LANE, "cycle2", "proofstream", tag + ".json"))
        if p1 and p1["status"] == "UNSAT" and pc and pc.get("ok") and pc.get("drat_trim_verified"):
            how = "a"
        elif p1 and p1["status"] == "UNSAT" and ps and ps.get("ok") and ps.get("drat_trim_verified") \
                and ps.get("cnf_matches_pass1_sha"):
            how = "b"
        if ps and ps.get("status") == "SAT":
            sats.append(("proofstream", tag))
        old = jl(os.path.join(LANE, "cycle2", "hard", tag + ".json"))
        if old:
            if old.get("status") == "SAT":
                sats.append(("hard", tag))
            if "cadical" in (old.get("solver") or ""):
                uncert.append(("cycle2/hard (CaDiCaL LRAT + lrat-check)", tag))
        h5 = jl(os.path.join(LANE, "cycle2", "hard5", tag + ".json"))
        if h5 and h5.get("status") == "SAT":
            sats.append(("hard5", tag))
        if not how and certified(h5) and h5.get("cnf_matches_pass1_sha"):
            how = "c5"
        for kind, sub in (("d", "a3"), ("e", "part")):
            d = os.path.join(LANE, "cycle2", sub, tag)
            E = jl(os.path.join(d, "ext.json"))
            if not E:
                continue
            n = E.get("num_full")
            cov = split_cover(d, n, sats, sub)
            if not how and n is not None and len(cov & set(range(n))) == n:
                how = kind
            for f in glob.glob(os.path.join(d, "*_r2.json")):
                uncert.append(("r2 (CaDiCaL LRAT + lrat-check)", os.path.relpath(f, LANE)))
        m2 = None
        if maps.get(mi) is not None:
            bi = maps[mi][si]
            for sub in ("m2skel_drat",):
                r = jl(os.path.join(LANE, "cycle2", sub, "ms%02d_b%05d.json" % (mi, bi)))
                if r and r.get("status") == "SAT":
                    sats.append((sub, tag))
                if not m2 and certified(r):
                    m2 = "direct-" + sub.split("_")[1]
            for sub in ("m2part_drat",):
                d = os.path.join(LANE, "cycle2", sub, "ms%02d_b%05d" % (mi, bi))
                E = jl(os.path.join(d, "ext.json"))
                if E:
                    n = E.get("num_placements")
                    cov = split_cover(d, n, sats, sub)
                    if not m2 and n is not None and len(cov & set(range(n))) == n:
                        m2 = "partbatch-" + sub.split("_")[1]
        p = per.setdefault("ms%02d" % mi, {"cases": 0, "M1_certified": 0, "M2_certified": 0, "both": 0, "M1_how": {}, "M2_how": {}})
        p["cases"] += 1
        if how:
            p["M1_certified"] += 1
            p["M1_how"][how] = p["M1_how"].get(how, 0) + 1
        else:
            open_m1.append(tag)
        if m2:
            p["M2_certified"] += 1
            p["M2_how"][m2] = p["M2_how"].get(m2, 0) + 1
        else:
            open_m2.append(tag)
        if how and m2:
            p["both"] += 1
    q0 = [jl(f) for f in glob.glob(os.path.join(LANE, "cases19q0", "results", "g*.json")) if not f.endswith(".check.json")]
    q0c = [jl(f) for f in glob.glob(os.path.join(LANE, "cases19q0", "results", "*.check.json"))]
    m2c = [jl(f) for f in glob.glob(os.path.join(LANE, "m2q0c", "results", "g*.json"))]
    for r in q0 + m2c:
        if r and r.get("status") == "SAT":
            sats.append(("E0", r.get("tag") or r.get("graph_index")))
    e0 = {"graphs": 486,
          "M1_drat_trim_checked": sum(1 for c in q0c if c and c.get("ok") and c.get("drat_trim_verified")),
          "M2_rev5_certified": sum(1 for r in m2c if certified(r)), "M2_rev5_results": len(m2c),
          "M2_cycle1_m2q0b": "UNCERTIFIED (lrat-check)"}
    out = {"E0_ms00": e0, "per_multiset": per, "M1_open": len(open_m1), "M2_open": len(open_m2),
           "sat_results": sats, "uncertified_records": len(uncert), "binding_pass1": (jl(os.path.join(LANE, "cycle2", "binding-pass1.json")) or {}).get("summary"),
           "M1_open_tags": open_m1, "M2_open_tags": open_m2, "uncertified_list": uncert}
    json.dump(out, open(os.path.join(LANE, "STATUS14_BASE.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if not k.endswith("_tags") and k != "uncertified_list"}, indent=1))


if __name__ == "__main__":
    main()
