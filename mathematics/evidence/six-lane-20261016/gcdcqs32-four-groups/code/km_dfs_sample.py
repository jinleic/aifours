#!/usr/bin/env python3
"""README E2c/E3d: random Kramer–Mesner solutions by randomized exact-cover DFS, one component at
a time (components = columns joined by rows; independent), seeds SEED0..SEED0+N-1.  Column
choice: fewest admissible rows, ties broken at random; candidate rows in random order; a node
cap per component restarts the DFS with the next sub-seed; TIME_BUDGET seconds per sample (native
limit; the sample is recorded as UNKNOWN when exceeded).  EXCLUDE = "lemmaS" drops the 2+2 rows
with a pair difference (XOR of the two coordinates) in {1, 2, 3} before sampling (README E3d,
Lemma S; for the group A4xES).  Writes OUTDIR/summary.json in the pipeline format (samples with
`rows` = indices into CQSKM.rows, usable by pipeline2.py --rows-from) after checking that every
column is covered exactly once.  Usage:
km_dfs_sample.py GROUP G OUTDIR N [SEED0] [NODE_CAP] [EXCLUDE] [TIME_BUDGET]"""
import lane_guard  # noqa: F401

import collections
import json
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import fresh_dir, xopen
from cqs_km import CQSKM
import groups as grp


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
    group, g, out, nsamp = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    seed0 = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    cap = int(sys.argv[6]) if len(sys.argv) > 6 else 200000
    exclude = sys.argv[7] if len(sys.argv) > 7 else "none"
    budget = float(sys.argv[8]) if len(sys.argv) > 8 else 3600.0
    assert exclude in ("none", "lemmaS", "lemmaT")
    fresh_dir(out)
    spec = grp.build(group, 4, g)
    gof = spec["group_of"]
    km = CQSKM(4 * g, gof, spec["gens"])
    typ = lambda pts: "+".join(str(c) for c in sorted(collections.Counter(gof[int(p)] for p in pts).values(), reverse=True))

    def lemma_s_bad(lab):
        b = [int(p) for p in km.Q[lab]]
        if typ(b) != "2+2":
            return False
        by = collections.defaultdict(list)
        for p in b:
            by[gof[p]].append(p % g)
        return any((c[0] ^ c[1]) in (1, 2, 3) for c in by.values())

    def lemma_t_bad(lab):
        """gcdcqs32 notes, Lemma T design condition (group A4xET)."""
        b = [int(p) for p in km.Q[lab]]
        if typ(b) != "2+2":
            return False
        by = collections.defaultdict(list)
        for p in b:
            by[gof[p]].append(p % g)
        (i, P), (j, Q2) = sorted(by.items())
        for (a, a2), (bb, bb2) in ((P, Q2), (Q2, P)):
            c = a ^ a2
            if (bb ^ bb2) == 1 and c != 0 and not (c >> 4) & 1:
                if ((a ^ bb) >> 4) & 1:
                    return True
        return False

    bad = {"none": lambda lab: False, "lemmaS": lemma_s_bad, "lemmaT": lemma_t_bad}[exclude]
    allowed = [j for j, (lab, _) in enumerate(km.rows) if not bad(lab)]
    parent = list(range(len(km.tcols)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for j in allowed:
        cols = km.rows[j][1]
        for c in cols[1:]:
            ra, rb = find(cols[0]), find(c)
            if ra != rb:
                parent[ra] = rb
    comps = collections.defaultdict(list)
    for c in range(len(km.tcols)):
        comps[find(c)].append(c)
    rows_of = collections.defaultdict(list)
    for j in allowed:
        rows_of[find(km.rows[j][1][0])].append((j, frozenset(km.rows[j][1])))
    summ = {"group": group, "g": g, "km": km.summary(), "method": "randomized exact-cover DFS per component",
            "node_cap": cap, "exclude": exclude, "rows_allowed": len(allowed), "time_budget": budget,
            "components": sorted((len(c) for c in comps.values()), reverse=True), "samples": []}
    print(json.dumps({k: summ[k] for k in ("rows_allowed", "components")}), flush=True)
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
            rec = {"sample": i, "km_seed": sd, "km_status": "UNKNOWN", "km_method": "DFS", "restarts": restarts,
                   "km_seconds": round(time.time() - t0, 3)}
            summ["samples"].append(rec)
            print(json.dumps(rec), flush=True)
            continue
        rows.sort()
        cover = collections.Counter(c for j in rows for c in km.rows[j][1])
        assert sorted(cover) == list(range(len(km.tcols))) and set(cover.values()) == {1}, "not an exact cover"
        bt = collections.Counter()
        for j in rows:
            bt[typ(km.Q[km.rows[j][0]])] += km.sizeQ[km.rows[j][0]]
        rec = {"sample": i, "km_seed": sd, "km_status": "SAT", "km_method": "DFS", "restarts": restarts,
               "km_seconds": round(time.time() - t0, 3), "block_types": dict(bt), "rows": rows}
        summ["samples"].append(rec)
        print(json.dumps({k: rec[k] for k in rec if k != "rows"}), flush=True)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(summ, fh)


if __name__ == "__main__":
    main()
