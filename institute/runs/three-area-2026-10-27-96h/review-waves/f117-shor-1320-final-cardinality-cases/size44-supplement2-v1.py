#!/usr/bin/env python3
"""size44-supplement2-v1.py -- f117 reviewer supplement 2 (size-44 branch).

Imports ONLY the reviewer's own module; no author code.
  T1  for each of the 21 G-compatible seeds, count gcd-55 pairs that survive inside the
      seed-filtered availability of class 0 and class 4 (explains why the GA-relaxed
      control restricted to the same 12 extras reproduces every count exactly).
  T2  the extras admitted under GA but not under G = GA u {55}: each must owe its
      exclusion to a gcd-55 difference against some Y anchor (mechanism of the 55-ban).
  T3  class-1-mod-3 residues in mod-5 classes 0/4 admitted under GA but not under G:
      each must have gcd 55 against anchor 0 or 14 (the elementary reason in the review).
  T4  independent re-check of the elementary parity lemma: every Y-screened residue
      x = 1 (mod 3) (under GA alone) is odd.
"""
import importlib.util
import json
import os
import sys
import time
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s44", os.path.join(HERE, "size44-independent-search-v1.py"))
s44 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s44)
gc, N, Y, A = s44.gc, s44.N, s44.Y, s44.A


def main():
    t_start = time.time()
    out = {"program": "size44-supplement2-v1.py", "utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t_start))}
    GA = s44.diff_classes(A)
    G = GA | {55}
    C, X, B0, B4, _ = s44.tail_instance(G)
    C2, X2, B0_2, B4_2, _ = s44.tail_instance(GA)

    # T1
    t1 = []
    for S in combinations(X, 8):
        if not s44.pairwise_free(S, G):
            continue
        av0 = [y for y in B0 if all(gc(s - y) not in G for s in S)]
        av4 = [y for y in B4 if all(gc(s - y) not in G for s in S)]
        p0 = [(a, b) for a, b in combinations(av0, 2) if gc(a - b) == 55]
        p4 = [(a, b) for a, b in combinations(av4, 2) if gc(a - b) == 55]
        t1.append({"seed": list(S), "avail0": av0, "avail4": av4, "gcd55_pairs_in_avail0": p0, "gcd55_pairs_in_avail4": p4})
    out["T1_surviving_gcd55_pairs_per_seed"] = t1
    out["T1_summary"] = {"compatible_seeds": len(t1),
                         "seeds_with_any_surviving_gcd55_pair": sum(1 for r in t1 if r["gcd55_pairs_in_avail0"] or r["gcd55_pairs_in_avail4"])}

    # T2
    removed = sorted(set(X2) - set(X))
    t2 = {str(x): [(y, gc(x - y)) for y in Y if x != y and gc(x - y) == 55] for x in removed}
    out["T2_extras_removed_by_55_ban"] = {"removed": removed, "count": len(removed), "gcd55_vs_Y": t2,
                                          "all_have_gcd55_vs_Y": all(t2[str(x)] for x in removed),
                                          "X12_subset_of_GA_extras": set(X) <= set(X2)}

    # T3
    c1 = [x for x in C2 if x % 5 in (0, 4) and x % 3 == 1]
    t3 = {str(x): [(y, gc(x - y)) for y in (0, 14) if gc(x - y) == 55] for x in c1}
    out["T3_class1_in_04_under_GA"] = {"residues": c1, "gcd55_vs_0_or_14": t3, "all_have_gcd55_vs_0_or_14": all(t3[str(x)] for x in c1),
                                       "all_odd": all(x % 2 == 1 for x in c1)}

    # T4
    ones = [x for x in C2 if x % 3 == 1]
    out["T4_parity_lemma"] = {"class1_screened_under_GA": len(ones), "all_odd": all(x % 2 == 1 for x in ones),
                              "even_exceptions": [x for x in ones if x % 2 == 0]}

    out["seconds_total"] = round(time.time() - t_start, 3)
    out["utc_end"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    text = json.dumps(out, indent=1, default=list) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "x") as fh:
            fh.write(text)
    print(json.dumps({"T1": out["T1_summary"], "T2": {k: v for k, v in out["T2_extras_removed_by_55_ban"].items() if k != "gcd55_vs_Y"},
                      "T3": {k: v for k, v in out["T3_class1_in_04_under_GA"].items() if k != "gcd55_vs_0_or_14"},
                      "T4": out["T4_parity_lemma"], "utc_start": out["utc_start"], "utc_end": out["utc_end"]}, indent=1, default=list))


if __name__ == "__main__":
    main()
