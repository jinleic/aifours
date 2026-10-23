#!/usr/bin/env python3
"""Parent audit sun-core5 v1, part 2: labelled replay under the Claude-review section-3 semantics.

Imports ONLY the parent's own frozen module indep_check_v1.py (same desk; sha256 recorded); no worker code.
Usage: python3 indep_labelled_v1.py OUTDIR LANE_DIR
  1. Direct classification of all 3^10 * 6^2 = 2,125,764 labelled (alpha, E2, E3); first-firing order
     T, K, P(pair then Bonferroni, per vertex), N2, FH1, FH2; every unkilled labelled pattern must
     canonicalise to the S-D orbit (proof-v1.md lines 25-28).
  2. Orbit-weighted counts (orbit size = 120/|stabiliser|) from the orbit enumeration, as a cross-check.
  3. Full rule-hit sets per orbit (independent of first-firing): T, K, P-pair, PB, N2 for all 21,150 orbits;
     FH2 (both H2 alternatives for the same (a,b)) for every orbit that no other rule kills.
  4. For the 20 PB orbits: which of P-pair / PB fire.  For the 22 FH2 orbits: per (a,b) pair, which
     alternatives are refuted (flags any one-case-only certificate pair).
  5. Comparison with the worker's lane checker counts (evidence/check-v2-run1/summary.json read as data).
"""
import hashlib
import importlib.util
import itertools
import json
import os
import sys
import time
from collections import Counter
from itertools import combinations, product

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ic1", os.path.join(HERE, "indep_check_v1.py"))
ic = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ic)

EDGES = ic.EDGES
TRIS = list(combinations(range(5), 3))
TRI_EDGES = [(ic.EIDX[(x, y)], ic.EIDX[(x, z)], ic.EIDX[(y, z)]) for x, y, z in TRIS]


def t_table():
    """kill[(a_xy, a_xz, a_yz, p2, p3)]: p = position (0,1,2 for x,y,z) of E2/E3 in the triangle, 3 = absent."""
    tab = {}
    for axy, axz, ayz in product((1, 2, 3), repeat=3):
        for p2 in range(4):
            for p3 in range(4):
                def gam(a, opp):
                    if a == 2 and p2 == opp:
                        return 2
                    if a == 3 and p3 == opp:
                        return 3
                    return 1
                tmin = 1
                for a, opp in ((axy, 2), (axz, 1), (ayz, 0)):
                    tmin = ic.lcm(tmin, a // gam(a, opp))
                tmax = min(axy * axz, axy * ayz, axz * ayz)
                tab[(axy, axz, ayz, p2, p3)] = tmin > tmax
    return tab


def main():
    outdir, lane = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        me = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.join(HERE, "indep_check_v1.py"), "rb") as f:
        dep = hashlib.sha256(f.read()).hexdigest()
    S = {"script_sha256": me, "imports_parent_module_indep_check_v1_sha256": dep, "python": sys.version}
    sd_key = (1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 0)
    assert ic.canon((1, 1, 2, 2, 3, 3, 3, 3, 3, 3), 1, 0) == sd_key
    # ---- 1. direct labelled classification
    TT = t_table()
    lab = Counter()
    unkilled = []
    n = 0
    for al in product((1, 2, 3), repeat=10):
        for e2 in (None, 0, 1, 2, 3, 4):
            for e3 in (None, 0, 1, 2, 3, 4):
                n += 1
                killed_T = False
                for (x, y, z), (exy, exz, eyz) in zip(TRIS, TRI_EDGES):
                    p2 = 0 if e2 == x else 1 if e2 == y else 2 if e2 == z else 3
                    p3 = 0 if e3 == x else 1 if e3 == y else 2 if e3 == z else 3
                    if TT[(al[exy], al[exz], al[eyz], p2, p3)]:
                        killed_T = True
                        break
                if killed_T:
                    lab["T"] += 1
                    continue
                c = ic.core_from(al, e2, e3).classify()
                if c is None:
                    lab["UNKILLED"] += 1
                    unkilled.append((al, e2, e3))
                else:
                    assert c[0] != "T"
                    lab[c[0]] += 1
    S["1_labelled_total"] = n
    S["1_labelled_first_rule_counts"] = dict(lab)
    S["1_unkilled_all_in_SD_orbit"] = all(ic.canon(*p) == sd_key for p in unkilled)
    S["1_unkilled_count"] = len(unkilled)
    S["1_seconds"] = round(time.time() - t0, 2)
    # ---- 2. orbit-weighted
    reps, pats = ic.enumerate_universe()
    weighted = Counter()
    orbit_size = {}
    for al, e2, e3 in pats:
        st = 0
        for pi, src in ic.PSRC:
            if tuple(al[src[s]] for s in range(10)) == al and (None if e2 is None else pi[e2]) == e2 and (
                    None if e3 is None else pi[e3]) == e3:
                st += 1
        orbit_size[(al, e2, e3)] = 120 // st
    cls = {}
    for p in pats:
        c = ic.core_from(*p).classify()
        cls[p] = c[0] if c else "UNKILLED"
        weighted[cls[p]] += orbit_size[p]
    S["2_orbit_weighted_counts"] = dict(weighted)
    S["2_orbit_sizes_sum"] = sum(orbit_size.values())
    S["2_SD_orbit_size"] = [orbit_size[p] for p in pats if ic.canon(*p) == sd_key]
    # ---- 3/4. full hit sets per orbit
    hist = Counter()
    pb_detail = []
    fh2_detail = []
    nohit = []
    for p in pats:
        q = ic.core_from(*p)
        h = q.hits(fh=False)
        fired = {r for r, v in h.items() if v}
        if not fired:
            per_pair = []
            for a, b in combinations(range(5), 2):
                if q.a(a, b) != 1 or not q.V2_of(a, b):
                    continue
                V2 = q.V2_of(a, b)
                c1 = not q.fibre_admissible(4, [a, b], {v: 2 for v in V2})
                c2 = not q.fibre_admissible(2, [a, b] + V2, {})
                per_pair.append({"ab": [a, b], "V2": V2, "case_i_refuted": c1, "case_ii_refuted": c2})
            if any(d["case_i_refuted"] and d["case_ii_refuted"] for d in per_pair):
                fired.add("FH2")
            fh2_detail.append({"pattern": [list(p[0]), p[1], p[2]], "pairs": per_pair,
                               "one_case_only_pairs": [d["ab"] for d in per_pair
                                                       if d["case_i_refuted"] != d["case_ii_refuted"]]})
        if cls[p] == "PB":
            pb_detail.append({"pattern": [list(p[0]), p[1], p[2]], "Ppair_fires": h["Ppair"], "PB_fires": h["PB"],
                              "T": h["T"], "K": h["K"]})
        hist[tuple(sorted(fired))] += 1
        if not fired:
            nohit.append([list(p[0]), p[1], p[2]])
    S["3_hitset_histogram"] = {"+".join(k) if k else "NONE": v for k, v in sorted(hist.items())}
    S["3_orbits_with_no_valid_certificate"] = nohit
    S["4_PB_orbits"] = {"n": len(pb_detail), "Ppair_fires": sum(d["Ppair_fires"] for d in pb_detail),
                        "PB_fires": sum(d["PB_fires"] for d in pb_detail), "detail": pb_detail}
    S["4_FH_stage_orbits"] = fh2_detail
    S["4_FH2_one_case_only_pairs_total"] = sum(len(d["one_case_only_pairs"]) for d in fh2_detail)
    # ---- 5. worker v2 counts (data only)
    wpath = os.path.join(lane, "evidence/check-v2-run1/summary.json")
    with open(wpath, "rb") as f:
        wb = f.read()
    w = json.loads(wb)
    S["5_worker_v2_summary_sha256"] = hashlib.sha256(wb).hexdigest()
    S["5_worker_v2_counts"] = w.get("first_rule_counts")
    mine = dict(lab)
    mine_cmp = {k: mine.get(k, 0) for k in ("T", "K", "PB", "Ppair", "N2", "FH1", "FH2")}
    mine_cmp["RSD(unkilled S-D orbit)"] = mine.get("UNKILLED", 0)
    S["5_parent_counts_for_comparison"] = mine_cmp
    wc = w.get("first_rule_counts", {})
    S["5_equal"] = all(mine_cmp[k] == wc.get(k, 0) for k in ("T", "K", "PB", "N2", "FH2")) and \
        mine_cmp["RSD(unkilled S-D orbit)"] == wc.get("RSD", 0) and mine_cmp["Ppair"] == wc.get("Ppair", 0) \
        and mine_cmp["FH1"] == wc.get("FH1", 0)
    S["seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(outdir, "summary.json"), "x") as f:
        json.dump(S, f, indent=1, default=str)
    print(json.dumps({k: S[k] for k in ("1_labelled_total", "1_labelled_first_rule_counts", "1_unkilled_count",
                                         "1_unkilled_all_in_SD_orbit", "2_orbit_weighted_counts", "2_SD_orbit_size",
                                         "3_hitset_histogram", "4_FH2_one_case_only_pairs_total",
                                         "5_worker_v2_counts", "5_equal", "seconds")}, default=str))


if __name__ == "__main__":
    main()
