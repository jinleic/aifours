#!/usr/bin/env python3
"""README E2b: connected components of a KM exact-cover instance (columns joined by rows) and,
per component, all exact covers (DFS on the component, capped) with their block-type counts.
Writes OUT.json (exclusive create).  Usage: km_components.py GROUP G OUT.json [CAP]"""
import lane_guard  # noqa: F401

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
import groups as grp


def exact_covers(cols, rows, cap):
    """rows: list of (row_id, frozenset(cols)); all exact covers of `cols` (up to cap)."""
    bycol = collections.defaultdict(list)
    for rid, cs in rows:
        for c in cs:
            bycol[c].append((rid, cs))
    out = []

    def rec(uncovered, chosen):
        if len(out) >= cap:
            return
        if not uncovered:
            out.append(list(chosen))
            return
        c = min(uncovered, key=lambda c: sum(1 for _, cs in bycol[c] if cs <= uncovered))
        for rid, cs in bycol[c]:
            if cs <= uncovered:
                chosen.append(rid)
                rec(uncovered - cs, chosen)
                chosen.pop()

    rec(frozenset(cols), [])
    return out


def main():
    group, g, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    cap = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
    spec = grp.build(group, 4, g)
    gof = spec["group_of"]
    km = CQSKM(4 * g, gof, spec["gens"])
    typ = lambda pts: "+".join(str(c) for c in sorted(collections.Counter(gof[int(p)] for p in pts).values(), reverse=True))
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
    for j, (lab, cols) in enumerate(km.rows):
        rows_of[find(cols[0])].append((j, frozenset(cols)))
    res = []
    for root, cols in sorted(comps.items(), key=lambda kv: -len(kv[1])):
        sols = exact_covers(cols, rows_of[root], cap)
        prof = collections.Counter()
        for s in sols:
            cnt = collections.Counter()
            for j in s:
                cnt[typ(km.Q[km.rows[j][0]])] += km.sizeQ[km.rows[j][0]]
            prof[json.dumps(dict(sorted(cnt.items())))] += 1
        res.append({"columns": len(cols), "rows": len(rows_of[root]), "solutions": len(sols),
                    "capped": len(sols) >= cap, "block_type_profiles": dict(prof)})
    rec = {"group": group, "g": g, "km": km.summary(), "components": len(res), "per_component": res}
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({"components": len(res), "sizes": [(r["columns"], r["rows"], r["solutions"]) for r in res][:40]}))


if __name__ == "__main__":
    main()
