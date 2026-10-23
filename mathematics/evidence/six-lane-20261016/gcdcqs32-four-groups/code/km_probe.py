#!/usr/bin/env python3
"""README E2b probes: build the KM model of GROUP at G once and solve variants with kissat
(native --time limit), recording status and block-type counts:
  base             the plain KM CNF
  no1111           every 1+1+1+1 row forbidden
  no22             every 2+2 row forbidden
  force211:K       K random 2+1+1 rows forced true (seed 0..), one variant per seed
  colcover211      every 1+1+1 column covered by a 2+1+1 row (all 1+1+1+1 rows forbidden on it) for
                   one column at a time (first 20 columns), reporting which are feasible
Usage: km_probe.py GROUP G OUTDIR TIMEOUT"""
import lane_guard  # noqa: F401

import collections
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import fresh_dir, xopen
from cqs_km import CQSKM
from lanelib import kissat
import groups as grp


def main():
    group, g, out, tl = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    fresh_dir(out)
    spec = grp.build(group, 4, g)
    gof = spec["group_of"]
    km = CQSKM(4 * g, gof, spec["gens"])
    typ = lambda pts: "+".join(str(c) for c in sorted(collections.Counter(gof[int(p)] for p in pts).values(), reverse=True))
    rtype = [typ(km.Q[lab]) for lab, _ in km.rows]
    ctype = [typ(km.T[lab]) for lab in km.tcols]
    base, rv = km.cnf()
    res = []

    def solve(name, extra):
        p = os.path.join(out, name + ".cnf")
        cl = base.clauses
        base.clauses = cl + [list(c) for c in extra]
        base.write(p)
        base.clauses = cl
        st, model, dt = kissat(p, tl, seed=0, log=p + ".log")
        rec = {"variant": name, "status": st, "seconds": round(dt, 3)}
        if st == "SAT":
            sel = [j for j, x in enumerate(rv) if x in model]
            rec["block_types"] = dict(collections.Counter(t for j in sel for t in [rtype[j]] for _ in range(km.sizeQ[km.rows[j][0]])))
        res.append(rec)
        print(json.dumps(rec), flush=True)
        return rec

    solve("base", [])
    solve("no1111", [[-rv[j]] for j, t in enumerate(rtype) if t == "1+1+1+1"])
    solve("no22", [[-rv[j]] for j, t in enumerate(rtype) if t == "2+2"])
    r211 = [j for j, t in enumerate(rtype) if t == "2+1+1"]
    for sd in range(3):
        pick = random.Random(sd).sample(r211, 3)
        solve(f"force211_3_seed{sd}", [[rv[j]] for j in pick])
    cols1111 = [ci for ci, t in enumerate(ctype) if t == "1+1+1"]
    for ci in cols1111[:20]:
        forb = [[-rv[j]] for j, (lab, cols) in enumerate(km.rows) if rtype[j] == "1+1+1+1" and ci in cols]
        solve(f"col{ci}_by211", forb)
    with xopen(os.path.join(out, "probe.json")) as fh:
        json.dump({"group": group, "g": g, "km": km.summary(), "results": res}, fh, indent=1)


if __name__ == "__main__":
    main()
