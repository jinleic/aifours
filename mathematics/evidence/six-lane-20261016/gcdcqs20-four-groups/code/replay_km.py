#!/usr/bin/env python3
"""Producer replay of the E1 Kramer–Mesner samples (README E1): rebuild the A4 x C20 KM model,
write km_0.cnf (base) and km_1.cnf (base + blocking clause of sample 0), solve them with kissat
seeds 0 and 1 exactly as code/pipeline.py did, and compare CNF sha256 and the selected rows with
the recorded run.  Writes OUTDIR/summary.json in the pipeline format (usable by
pipeline2.py --rows-from OUTDIR/summary.json:1).  All writes exclusive-create.
Usage: replay_km.py RECORDED_SUMMARY.json OUTDIR NSAMPLES"""
import lane_guard  # noqa: F401

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import fresh_dir, xopen
from lanelib import kissat
from cqs_km import CQSKM
import groups as grp


def main():
    rec_path, out, nsamp = sys.argv[1], sys.argv[2], int(sys.argv[3])
    fresh_dir(out)
    recorded = json.load(open(rec_path))
    spec = grp.build("A4xC", 4, 20)
    km = CQSKM(80, spec["group_of"], spec["gens"])
    cnf, rv = km.cnf()
    summ = {"group": "A4xC", "g": 20, "replay_of": rec_path, "samples": []}
    for i in range(nsamp):
        p = os.path.join(out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, 600, seed=i, log=p + ".log")
        sel = [j for j, x in enumerate(rv) if x in model]
        r0 = recorded["samples"][i]
        rec = {"sample": i, "km_seed": i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3),
               "rows": sel, "cnf_matches_record": sha == r0["km_cnf_sha256"], "rows_match_record": sel == r0["rows"]}
        summ["samples"].append(rec)
        print(json.dumps({k: rec[k] for k in rec if k != "rows"}), flush=True)
        if st != "SAT":
            break
        cnf.add([-rv[j] for j in sel])
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(summ, fh)


if __name__ == "__main__":
    main()
