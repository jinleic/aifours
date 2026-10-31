#!/usr/bin/env python3
"""size44-supplement-v1.py -- f117 reviewer supplement (size-44 branch).

Imports ONLY the reviewer's own module size44-independent-search-v1.py (same directory);
no author code.  Purpose:
  S1  balance-free UNSAT via structure 2: run the quota DFS exhaustively for every
      (zeros, twos) split with zeros+twos = 20 and sum the solutions (expected 0).
  S2  census of gcd-55 pairs inside the relaxed universe U = X12 u B0 u B4 and against Y,
      explaining why dropping 55 while keeping X12 leaves every count unchanged.
  S3  per-compatible-seed margins: availability sizes, |L|,|R|, and the minimum number of
      cross-conflicting (l,r) element pairs over all (L,R) pairs (expected >= 1 everywhere).
  S4  structural facts behind the cross obstruction (parity / mod-3 composition of L,R).
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
    out = {"program": "size44-supplement-v1.py", "utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t_start))}
    GA, GY = s44.diff_classes(A), s44.diff_classes(Y)
    G = GA | {55}
    C, X, B0, B4, info = s44.tail_instance(G)
    assert len(X) == 12 and len(B0) == 70 and len(B4) == 70

    # S1: balance-free exhaustive DFS (structure 2)
    s1 = {}
    total_nodes = 0
    total_sols = 0
    for z in range(0, 21):
        q = s44.quota_dfs(G, X, B0, B4, zeros_target=z, twos_target=20 - z, stop_first=False)
        assert not q["budget_exceeded"]
        s1[f"zeros={z},twos={20 - z}"] = {"nodes": q["nodes"], "solutions": q["solutions"]}
        total_nodes += q["nodes"]
        total_sols += q["solutions"]
    out["S1_balance_free_quota_dfs"] = {"per_split": s1, "total_nodes": total_nodes, "total_solutions": total_sols}

    # S2: gcd-55 census inside the universe
    U = sorted(set(X) | set(B0) | set(B4))
    pairs55 = [(a, b) for a, b in combinations(U, 2) if gc(a - b) == 55]
    vsY55 = [(u, y) for u in U for y in Y if u != y and gc(u - y) == 55]
    out["S2_gcd55_census"] = {"universe_size": len(U), "gcd55_pairs_inside_universe": pairs55,
                              "gcd55_pairs_universe_vs_Y": vsY55,
                              "gcd_class_histogram_inside_universe": {}}
    hist = {}
    for a, b in combinations(U, 2):
        g = gc(a - b)
        hist[g] = hist.get(g, 0) + 1
    out["S2_gcd55_census"]["gcd_class_histogram_inside_universe"] = {str(k): hist[k] for k in sorted(hist)}

    # S3/S4: per-seed margins and structure
    i0, i4 = B0.index(0), B4.index(14)
    conf0 = [s44.mask_of(j for j, y in enumerate(B0) if j != i and gc(x - y) in G) for i, x in enumerate(B0)]
    conf4 = [s44.mask_of(j for j, y in enumerate(B4) if j != i and gc(x - y) in G) for i, x in enumerate(B4)]
    full0, full4 = (1 << 70) - 1, (1 << 70) - 1

    def cliques(conf, avail, anchor, size):
        res = []

        def rec(ch, cand):
            need = size - len(ch)
            if need == 0:
                res.append(tuple(ch))
                return
            if cand.bit_count() < need:
                return
            c = cand
            while c:
                b = c & -c
                i = b.bit_length() - 1
                c ^= b
                rec(ch + [i], c & ~conf[i])

        rec([anchor], avail & ~conf[anchor] & ~(1 << anchor))
        return res

    seeds_info = []
    for S in combinations(X, 8):
        if not s44.pairwise_free(S, G):
            continue
        av0 = full0
        av4 = full4
        for s in S:
            av0 &= ~s44.mask_of(j for j, y in enumerate(B0) if gc(s - y) in G)
            av4 &= ~s44.mask_of(j for j, y in enumerate(B4) if gc(s - y) in G)
        L = cliques(conf0, av0, i0, 6)
        R = cliques(conf4, av4, i4, 6)
        Lv = [[B0[i] for i in l] for l in L]
        Rv = [[B4[j] for j in r] for r in R]
        min_cross = None
        min_pair = None
        for l in Lv:
            for r in Rv:
                k = sum(1 for a in l for b in r if gc(a - b) in G)
                if min_cross is None or k < min_cross:
                    min_cross, min_pair = k, (l, r)

        def profile(sets):
            # composition: (#even, #class0mod3) histogram over sets
            h = {}
            for s in sets:
                key = f"even={sum(1 for x in s if x % 2 == 0)},mod3zero={sum(1 for x in s if x % 3 == 0)}"
                h[key] = h.get(key, 0) + 1
            return h

        seeds_info.append({
            "seed": list(S), "seed_mod3": [s % 3 for s in S], "seed_parity": [s % 2 for s in S],
            "avail0": av0.bit_count(), "avail4": av4.bit_count(), "L": len(L), "R": len(R),
            "min_cross_conflicts_over_all_pairs": min_cross, "argmin_pair": min_pair,
            "L_profile": profile(Lv), "R_profile": profile(Rv),
        })
    out["S3_per_compatible_seed"] = seeds_info
    out["S3_summary"] = {"compatible_seeds": len(seeds_info),
                         "min_cross_conflicts_global": min(s["min_cross_conflicts_over_all_pairs"] for s in seeds_info),
                         "seeds_with_min_cross_1": sum(1 for s in seeds_info if s["min_cross_conflicts_over_all_pairs"] == 1)}

    # S4: structural fact check used in the written explanation:
    #   inside B0 (class 0 mod 5, non-class-1), conflict <=> different mod-3 class AND different parity.
    viol = []
    for a, b in combinations(B0, 2):
        pred = (a % 3 != b % 3) and (a % 2 != b % 2)
        if pred != (gc(a - b) in G):
            viol.append((a, b, gc(a - b)))
    viol4 = []
    for a, b in combinations(B4, 2):
        pred = (a % 3 != b % 3) and (a % 2 != b % 2)
        if pred != (gc(a - b) in G):
            viol4.append((a, b, gc(a - b)))
    out["S4_inside_class_conflict_rule_violations"] = {"B0": viol, "B4": viol4}

    out["seconds_total"] = round(time.time() - t_start, 3)
    out["utc_end"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    text = json.dumps(out, indent=1, default=list) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "x") as fh:
            fh.write(text)
    print(json.dumps({"S1_total_solutions": total_sols, "S1_total_nodes": total_nodes,
                      "S2_gcd55_pairs_inside_universe": len(pairs55), "S2_gcd55_vs_Y": len(vsY55),
                      "S3_summary": out["S3_summary"],
                      "S4_violations": {"B0": len(viol), "B4": len(viol4)},
                      "utc_start": out["utc_start"], "utc_end": out["utc_end"], "seconds": out["seconds_total"]}, indent=1))


if __name__ == "__main__":
    main()
