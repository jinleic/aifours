#!/usr/bin/env python3
"""Exhaustive enumeration of all Kramer–Mesner exact covers (all G-invariant CQS(g^4:0)) for a
named group with a small KM matrix (Algorithm X over code/cqs_km.py rows; no SAT solver).
Writes OUT.json (exclusive create).  Usage: km_enumerate.py GROUP OUT.json [G] [MAXSOL]"""
import lane_guard  # noqa: F401

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from lanelib import closure
from cqs_km import CQSKM
import groups as grp


def main():
    name, out = sys.argv[1], sys.argv[2]
    g = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    maxsol = int(sys.argv[4]) if len(sys.argv) > 4 else 10**6
    spec = grp.build(name, 4, g)
    v = 4 * g
    km = CQSKM(v, spec["group_of"], spec["gens"])
    cols = range(len(km.tcols))
    rows = [frozenset(c) for _, c in km.rows]
    bycol = {c: [i for i, rs in enumerate(rows) if c in rs] for c in cols}
    sols = []

    def search(active, chosen):
        if len(sols) >= maxsol:
            return
        if not active:
            sols.append(sorted(chosen))
            return
        c = min(active, key=lambda cc: sum(1 for i in bycol[cc] if rows[i] <= active))
        for i in bycol[c]:
            if rows[i] <= active:
                chosen.append(i)
                search(active - rows[i], chosen)
                chosen.pop()

    search(frozenset(cols), [])
    rec = {"group": name, "g": g, "group_order": len(closure(spec["gens"], v)), "km": km.summary(),
           "solutions": len(sols), "capped": len(sols) >= maxsol,
           "solution_rows": sols,
           "solution_row_orbit_sizes": [sorted(km.sizeQ[km.rows[i][0]] for i in s) for s in sols],
           "row_representatives": [[int(x) for x in km.Q[lab]] for lab, _ in km.rows]}
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("group", "group_order", "solutions", "capped", "solution_row_orbit_sizes")}))


if __name__ == "__main__":
    main()
