#!/usr/bin/env python3
"""README A3: random Kramer–Mesner solutions of the cyclic stem model (code/pipeline_s3.py groups: Z_{4g},
groups = residues mod 4, rho swapping the stems, optional multipliers u ≡ 1 mod 4) by randomized exact-cover
DFS, one connected component of the column graph at a time (copied logic of the gcdcqs32 lane's
code/km_dfs_sample.py, sha256 of the source recorded in README): column with fewest admissible rows (random
ties), rows in random order, node cap with restarts, time budget per sample (native limit; UNKNOWN when
exceeded).  The cover is re-checked; summary.json lists `rows` (indices into CQSKMS.rows) for
pipeline_s4.py --rows-from.  Usage: km_dfs_s.py OUTDIR G MULT(comma list or -) N [SEED0] [NODE_CAP] [BUDGET]"""
import lane_guard  # noqa: F401

import collections
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import fresh_dir, xopen  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402

sys.setrecursionlimit(100000)


def random_cover(cols, rows, rng, cap, deadline):
    bycol = collections.defaultdict(list)
    for rid, cs in rows:
        for c in cs:
            bycol[c].append((rid, cs))
    nodes = [0]

    def rec(uncovered, chosen):
        if not uncovered:
            return list(chosen)
        nodes[0] += 1
        if nodes[0] > cap or (nodes[0] % 64 == 0 and time.time() > deadline):
            nodes[0] = cap + 1
            return None
        best, cand = None, None
        for c in uncovered:
            adm = [rc for rc in bycol[c] if rc[1] <= uncovered]
            key = (len(adm), rng.random())
            if best is None or key < best:
                best, cand = key, adm
            if len(adm) <= 1:
                break
        rng.shuffle(cand)
        for rid, cs in cand:
            chosen.append(rid)
            r = rec(uncovered - cs, chosen)
            if r is not None:
                return r
            chosen.pop()
            if nodes[0] > cap:
                return None
        return None

    return rec(frozenset(cols), [])


def main():
    out, g, mult, nsamp = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    seed0 = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    cap = int(sys.argv[6]) if len(sys.argv) > 6 else 200000
    budget = float(sys.argv[7]) if len(sys.argv) > 7 else 600.0
    fresh_dir(out)
    N, v = 4 * g, 4 * g + 2
    group_of = [p % 4 for p in range(N)] + [-1, -1]
    gens = [tuple([(p + 1) % N for p in range(N)] + [N + 1, N])]
    mults = [] if mult == "-" else [int(u) for u in mult.split(",")]
    for u in mults:
        assert u % 4 == 1 and math.gcd(u, N) == 1
        gens.append(tuple([(u * p) % N for p in range(N)] + [N, N + 1]))
    km = CQSKMS(v, group_of, gens)
    parent = list(range(len(km.tcols)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for _, cols in km.rows:
        for c in cols[1:]:
            ra, rb = find(cols[0]), find(c)
            if ra != rb:
                parent[ra] = rb
    comps = collections.defaultdict(list)
    for c in range(len(km.tcols)):
        comps[find(c)].append(c)
    rows_of = collections.defaultdict(list)
    for j, (_, cols) in enumerate(km.rows):
        rows_of[find(cols[0])].append((j, frozenset(cols)))
    summ = {"g": g, "mult": mults, "km": km.summary(), "method": "randomized exact-cover DFS per component",
            "node_cap": cap, "time_budget": budget, "components": sorted((len(c) for c in comps.values()), reverse=True),
            "samples": []}
    print(json.dumps({"km": summ["km"], "components": summ["components"]}), flush=True)
    for i in range(nsamp):
        sd = seed0 + i
        t0 = time.time()
        deadline = t0 + budget
        rows, restarts, ok = [], 0, True
        for root in sorted(comps):
            sub = 0
            while True:
                rng = random.Random(f"{sd}:{root}:{sub}")
                sol = random_cover(comps[root], rows_of[root], rng, cap, deadline)
                if sol is not None or time.time() > deadline:
                    break
                sub += 1
                restarts += 1
            if sol is None:
                ok = False
                break
            rows += sol
        if not ok:
            rec = {"sample": i, "km_seed": sd, "km_status": "UNKNOWN", "restarts": restarts,
                   "km_seconds": round(time.time() - t0, 3)}
        else:
            rows.sort()
            cover = collections.Counter(c for j in rows for c in km.rows[j][1])
            assert sorted(cover) == list(range(len(km.tcols))) and set(cover.values()) == {1}, "not an exact cover"
            rec = {"sample": i, "km_seed": sd, "km_status": "SAT", "restarts": restarts,
                   "km_seconds": round(time.time() - t0, 3), "rows": rows}
        summ["samples"].append(rec)
        print(json.dumps({k: rec[k] for k in rec if k != "rows"}), flush=True)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(summ, fh)


if __name__ == "__main__":
    main()
