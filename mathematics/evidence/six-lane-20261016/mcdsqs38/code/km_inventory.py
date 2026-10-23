#!/usr/bin/env python3
"""E0: Kramer–Mesner inventory for SQS(v) under Z_v ⋊ <m> for each multiplier generator m,
plus KM satisfiability (kissat, capped).  Usage: km_inventory.py V OUT.json TIMEOUT m1 m2 ..."""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcdsqs_lib import SQSKM, closure, kissat, mult_perm, shift_perm


def main():
    v, out, to = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    res = []
    for m in [int(x) for x in sys.argv[4:]]:
        M = sorted({g[1] for g in closure([mult_perm(m, v)], v)})
        km = SQSKM(v, [shift_perm(1, v), mult_perm(m, v)])
        cnf, rv = km.cnf()
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "km.cnf")
            sha = cnf.write(p)
            st, model, dt = kissat(p, to, seed=0)
        rec = {"generator": m, "multipliers": M, "group_order": v * len(M), "km": km.summary(),
               "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3)}
        if st == "SAT":
            sel = [j for j, x in enumerate(rv) if x in model]
            rec["sample_row_orbit_sizes"] = sorted(km.sizeQ[km.rows[j][0]] for j in sel)
        print(json.dumps({k: rec[k] for k in ("generator", "group_order", "km_status", "km_seconds")}
                         | {"cols": rec["km"]["triple_orbits"], "rows": rec["km"]["valid_rows"]}), flush=True)
        res.append(rec)
    json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    main()
