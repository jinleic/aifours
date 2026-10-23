#!/usr/bin/env python3
"""Audit step (run only AFTER the independent evaluation): compare our per-sector values with the
worker's per-sector rigorous enclosures (*.sectors.jsonl) and totals.  Writes
../evidence/compare_worker_sectors.json"""
import glob
import hashlib
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PIN = os.path.normpath(os.path.join(HERE, "../../depolarizing-parent-inputs-v1"))
MINE = os.path.join(HERE, "../evidence/ic_p1_5_D440.json")
OUT = os.path.join(HERE, "../evidence/compare_worker_sectors.json")


def main():
    w = json.load(open(os.path.join(PIN, "evidence/cert/witness_g3_M2000_p1_5.json")))
    canon = hashlib.sha256(json.dumps(w, sort_keys=True).encode()).hexdigest()
    tot = json.load(open(os.path.join(PIN, "evidence/cert/M2000_p1_5_TOTAL.json")))
    mine = json.load(open(MINE))
    B = {b["N"]: b for b in mine["blocks"]}
    recs = {}
    for f in sorted(glob.glob(os.path.join(PIN, "evidence/cert/*.sectors.jsonl"))):
        for line in open(f):
            r = json.loads(line)
            recs[r["N"]] = r
    rows = []
    for N, r in sorted(recs.items()):
        v = B[N]["dS"] / math.log(2)
        rows.append(dict(N=N, r=(mine["M"] - N) // 2, worker_lo=r["lo"], worker_hi=r["hi"], mine_bits=v,
                         inside=r["lo"] <= v <= r["hi"], rel_pos=(v - r["lo"]) / (r["hi"] - r["lo"]),
                         pN_worker=r["pN"], p_mine=B[N]["p"], smin=r["smin"], w_tail=r["w_tail"],
                         eps_tail=r["eps_tail"]))
    sel = set(recs)
    rest_mine = math.fsum(b["p"] for b in mine["blocks"] if b["N"] not in sel)
    summ = dict(
        witness_canonical_sha256=canon, total_json_witness_sha256=tot["witness_sha256"],
        same_witness=(canon == tot["witness_sha256"]),
        n_sectors=len(rows), n_inside=sum(r["inside"] for r in rows),
        rel_pos_min=min(r["rel_pos"] for r in rows), rel_pos_max=max(r["rel_pos"] for r in rows),
        max_rel_dev_pN=max(abs(r["pN_worker"] / r["p_mine"] - 1) for r in rows),
        worker_total=[tot["lower"], tot["upper"]], mine_total_bits=mine["Ic_bits"],
        mine_inside_total=tot["lower"] <= mine["Ic_bits"] <= tot["upper"],
        mine_rel_pos_total=(mine["Ic_bits"] - tot["lower"]) / (tot["upper"] - tot["lower"]),
        mine_sum_over_worker_sectors_bits=math.fsum(B[N]["p"] * B[N]["dS"] for N in sel) / math.log(2),
        worker_rest_mass_hi=tot["rest_mass_hi"],
        mine_mass_outside_worker_sectors_within_r121_440=rest_mine,
        effective_ptail_bracket=[max(B[N]["p"] for N in B if N not in sel), min(B[N]["p"] for N in sel)],
    )
    json.dump(dict(summary=summ, rows=rows), open(OUT, "w"), indent=1)
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()
