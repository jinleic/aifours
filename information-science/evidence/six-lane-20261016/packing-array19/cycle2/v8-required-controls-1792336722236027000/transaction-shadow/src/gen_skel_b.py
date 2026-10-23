#!/usr/bin/env python3
"""Independent second generator (M2) for the A2 P0-quad skeletons; shares no code with
gen_skel.py beyond the profile list (recomputed here independently).

Representation: a skeleton is a bicoloured graph, first class = rows lying in >= 2 P0
quads (degree 2..tmax), second class = the c0 P0 quads (degree <= 4); two quads share <= 1
row (genbg -Z1 on the second class). nauty genbg enumerates these up to isomorphism
preserving the two classes, for every number h of first-class vertices (0 <= h <= 2*c0).
Rows in exactly one quad (4 - degree per quad) and rows in no quad complete the 19 rows.
Filters (same necessary conditions as README A2, re-derived): rows in >= 3 quads lie in a
size-<=2 block of a special column, so their number is <= hmax; total rows <= 19; with one
special column its multiset of e = size - 3 must be assignable to rows with
0 <= 2 - |T| - e <= L (checked here by brute-force bipartite matching).
Output: skeletons-b-msXX.json with each skeleton as a list of row types (sorted tuples).
Usage (research venv): gen_skel_b.py MS_INDEX OUTDIR
"""
import itertools
import json
import os
import subprocess
import sys

import networkx as nx

GENBG = "/opt/homebrew/bin/genbg"


def partitions19():
    out = []

    def rec(n, k, mx, acc):
        if k == 0:
            if n == 0:
                out.append(tuple(acc))
            return
        for x in range(min(n, mx), -1, -1):
            rec(n - x, k - 1, x, acc + [x])

    rec(19, 6, 19, [])
    return out


def kap(p):
    return sum(x * (x - 1) // 2 for x in p)


def multisets():
    parts = [p for p in partitions19()]
    kmin = min(kap(p) for p in parts)
    budget = 171 - 8 * kmin
    profs = [p for p in parts if kap(p) - kmin <= budget]
    profs.sort(key=lambda p: (kap(p), [-x for x in p]))
    res = []
    for combo in itertools.combinations_with_replacement(range(len(profs)), 8):
        ex = sum(kap(profs[i]) - kmin for i in combo)
        if ex <= budget:
            res.append(([profs[i] for i in combo], budget - ex))
    return res, kmin


def matchable(tsizes, evals, L):
    # bipartite matching rows -> e-values with 0 <= 2 - t - e <= L (Kuhn's algorithm)
    n = len(tsizes)
    adj = [[j for j, e in enumerate(evals) if 0 <= 2 - t - e <= L] for t in tsizes]
    match = [-1] * len(evals)

    def aug(i, seen):
        for j in adj[i]:
            if not seen[j]:
                seen[j] = True
                if match[j] < 0 or aug(match[j], seen):
                    match[j] = i
                    return True
        return False

    return all(aug(i, [False] * len(evals)) for i in range(n))


def main():
    mi, outdir = int(sys.argv[1]), sys.argv[2]
    ms, kmin = multisets()
    profs, L = ms[mi]
    P0 = (4, 3, 3, 3, 3, 3)
    c0 = sum(1 for p in profs if p == P0)
    X = [p for p in profs if p != P0]
    wmin = sum(min(x - 3 for x in p) for p in X)
    tmax = min(c0, 2 - wmin)
    hmax = sum(x for p in X for x in p if x <= 2)
    evals = [x - 3 for x in X[0] for _ in range(x)] if len(X) == 1 else None
    out = []
    counts = {}
    for h in range(0, 2 * c0 + 1):
        if h == 0:
            graphs = [None]
        else:
            cmd = [GENBG, "-q", "-Z1", "-d2:0", "-D%d:4" % tmax, str(h), str(c0)]
            graphs = subprocess.run(cmd, capture_output=True, text=True).stdout.split()
        kept = 0
        for g6 in graphs:
            if g6 is None:
                types = []
            else:
                G = nx.from_graph6_bytes(g6.encode())
                types = [tuple(sorted(v - h for v in G.neighbors(r))) for r in range(h)]
            deg = [0] * c0
            for t in types:
                for v in t:
                    deg[v] += 1
            if any(d > 4 for d in deg):
                continue
            big = sum(1 for t in types if len(t) >= 3)
            if big > hmax:
                continue
            nrows = len(types) + sum(4 - d for d in deg)
            if nrows > 19:
                continue
            empty = 19 - nrows
            tsizes = [len(t) for t in types] + [1] * sum(4 - d for d in deg) + [0] * empty
            if evals is not None and not matchable(tsizes, evals, L):
                continue
            out.append({"types": sorted(types), "empty": empty})
            kept += 1
        counts[h] = [len(graphs), kept]
    os.makedirs(outdir, exist_ok=True)
    json.dump({"multiset_index": mi, "profiles": [list(p) for p in profs], "c0": c0, "L": L,
               "tmax": tmax, "hmax": hmax, "per_h": counts, "num_skeletons": len(out), "skeletons": out},
              open(os.path.join(outdir, "skeletons-b-ms%02d.json" % mi), "w"))
    print(json.dumps({"multiset_index": mi, "c0": c0, "L": L, "tmax": tmax, "hmax": hmax,
                      "num_skeletons": len(out)}))


if __name__ == "__main__":
    main()
