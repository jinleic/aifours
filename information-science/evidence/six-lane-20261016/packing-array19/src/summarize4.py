#!/usr/bin/env python3
"""summarize4 = summarize3 with: full (untruncated) open lists; *_r2.json and *_exact.json
subcase reruns accepted; ms00 block recomputed from the cycle-1 result files; optional
binding report cycle2/binding-pass1.json (from bind_check.py) included. Output STATUS4.json.
Original docstring: Final aggregation (read-only over result files) -> STATUS3.json.

Per A2 case (ms01..ms09, 5577 cases), M1 is decided UNSAT if ANY of:
  (a) pass-1 UNSAT + cycle-1 stored-proof check ok (cases19skel/proofcheck/<tag>.json);
  (b) pass-1 UNSAT + cycle-2 streamed proof check ok (cycle2/proofstream/<tag>.json);
  (c) direct run UNSAT with checked proof and CNF SHA equal to pass 1 (cycle2/hard/<tag>.json);
  (d) A3 full split: every full skeleton covered by a checked UNSAT f*.json or f*_r2.json;
  (e) A3'/A3'' split: every placement covered by a checked UNSAT single subcase f*.json /
      f*_r2.json or a checked UNSAT batch batch_*.json / batch_*_r2.json (indices listed).
M2 is decided UNSAT for the matched gen_skel_b case if (f) cycle2/m2skel_v2 or cycle2/m2skel
holds a checked UNSAT, or (g) every placement of cycle2/m2part/<case> is covered by checked
UNSAT f*.json / batch_*.json results. Any SAT result anywhere is listed.
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


def ok(r):
    return bool(r) and r.get("status") == "UNSAT" and bool(r.get("checked"))


def covered_split(d, n, key="full"):
    """indices covered by checked UNSAT results in split directory d (n subcases)."""
    cov = set()
    sat = False
    for f in glob.glob(os.path.join(d, "f*.json")):
        m = re.match(r".*/f(\d+)(_r2|_exact)?\.json$", f)
        if not m:
            continue
        r = jl(f)
        if r and r.get("status") == "SAT":
            sat = True
        if ok(r):
            cov.add(int(m.group(1)))
    for f in glob.glob(os.path.join(d, "batch_*.json")):
        r = jl(f)
        if r and r.get("status") == "SAT":
            sat = True
        if ok(r):
            idx = r.get("indices")
            if idx and len(idx) == 2 and isinstance(idx[0], int) and "multiset" in r:
                idx = list(range(idx[0], idx[1] + 1))  # M2 batches store [first, last]
            if idx:
                cov.update(idx)
    return cov, sat


def main():
    idx = json.load(open(os.path.join(LANE, "cases19skel", "index.json")))
    maps = {}
    for mi in range(1, 10):
        m = jl(os.path.join(LANE, "cycle2", "skel-b", "compare-map-ms%02d.json" % mi))
        maps[mi] = m["a_to_b"] if m and m.get("bijection") else None
    per = {}
    open_m1, open_m2, sats = [], [], []
    for c in idx["cases"]:
        tag, mi, si = c["tag"], c["multiset"], c["skel"]
        p1 = jl(os.path.join(LANE, "cases19skel", "results", tag + ".json"))
        how = None
        if p1 and p1["status"] == "UNSAT" and (jl(os.path.join(LANE, "cases19skel", "proofcheck", tag + ".json")) or {}).get("ok"):
            how = "a"
        elif p1 and p1["status"] == "UNSAT" and (jl(os.path.join(LANE, "cycle2", "proofstream", tag + ".json")) or {}).get("ok"):
            how = "b"
        else:
            dr = jl(os.path.join(LANE, "cycle2", "hard", tag + ".json"))
            if ok(dr) and dr.get("cnf_matches_pass1_sha"):
                how = "c"
            if dr and dr.get("status") == "SAT":
                sats.append(("direct", tag))
            for kind, sub, key in (("d", "a3", "full"), ("e", "part", "full")):
                if how:
                    break
                d = os.path.join(LANE, "cycle2", sub, tag)
                E = jl(os.path.join(d, "ext.json"))
                if E:
                    n = E.get("num_full")
                    cov, sat = covered_split(d, n)
                    if sat:
                        sats.append((sub, tag))
                    if n is not None and len(cov & set(range(n))) == n:
                        how = kind
        m2 = None
        if maps.get(mi) is not None:
            bi = maps[mi][si]
            for sub in ("m2skel_v2", "m2skel"):
                r = jl(os.path.join(LANE, "cycle2", sub, "ms%02d_b%05d.json" % (mi, bi)))
                if r and r.get("status") == "SAT":
                    sats.append((sub, tag))
                if ok(r):
                    m2 = sub
                    break
            if m2 is None:
                d = os.path.join(LANE, "cycle2", "m2part", "ms%02d_b%05d" % (mi, bi))
                E = jl(os.path.join(d, "ext.json"))
                if E:
                    n = E.get("num_placements")
                    cov, sat = covered_split(d, n)
                    if sat:
                        sats.append(("m2part", tag))
                    if n is not None and len(cov & set(range(n))) == n:
                        m2 = "m2part"
        p = per.setdefault("ms%02d" % mi, {"cases": 0, "M1_decided": 0, "M2_decided": 0, "both": 0, "M1_how": {}})
        p["cases"] += 1
        if how:
            p["M1_decided"] += 1
            p["M1_how"][how] = p["M1_how"].get(how, 0) + 1
        else:
            open_m1.append(tag)
        if m2:
            p["M2_decided"] += 1
        else:
            open_m2.append(tag)
        if how and m2:
            p["both"] += 1
    q0 = [jl(f) for f in glob.glob(os.path.join(LANE, "cases19q0", "results", "g*.json")) if not f.endswith(".check.json")]
    q0c = [jl(f) for f in glob.glob(os.path.join(LANE, "cases19q0", "results", "*.check.json"))]
    m2q = [jl(f) for f in glob.glob(os.path.join(LANE, "m2q0b", "results", "g*.json"))]
    e0 = {"graphs": 486, "M1_results": len(q0), "M1_unsat": sum(1 for r in q0 if r and r.get("status") == "UNSAT"),
          "M1_drat_lrat_ok": sum(1 for c in q0c if c and c.get("ok")), "M2_results": len(m2q),
          "M2_unsat_lrat_ok": sum(1 for r in m2q if r and r.get("status") == "UNSAT" and r.get("lrat_verified"))}
    binding = jl(os.path.join(LANE, "cycle2", "binding-pass1.json"))
    out = {"E0_ms00": e0, "binding_pass1": (binding or {}).get("summary"), "per_multiset": per, "M1_open": len(open_m1), "M2_open": len(open_m2),
           "sat_results": sats, "M1_open_tags": open_m1, "M2_open_tags": open_m2}
    json.dump(out, open(os.path.join(LANE, "STATUS4.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if not k.endswith("_tags")}, indent=1))


if __name__ == "__main__":
    main()
