#!/usr/bin/env python3
"""Collect headline numbers from ../evidence/*.json into ../evidence/SUMMARY.json."""
import glob
import hashlib
import json
import math
import os

EV = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../evidence"))


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    runs = {}
    for f in sorted(glob.glob(os.path.join(EV, "ic_*.json"))):
        d = json.load(open(f))
        runs[os.path.basename(f)] = {k: d[k] for k in (
            "p", "eta", "Dout", "norm", "perturb", "seed", "r_min", "r_max", "nblocks", "p_excluded",
            "bound_excluded_contribution", "Ic_nats", "Ic_bits", "max_abs_deficit", "max_diag_tail",
            "min_ev_B", "min_ev_RB", "seconds")}
    base = runs["ic_p1_5_D440.json"]["Ic_nats"]
    conv = {k: v["Ic_nats"] - base for k, v in runs.items() if v["p"] == "1/5"}
    val = json.load(open(os.path.join(EV, "validation_small.json")))["summary"]
    prec = json.load(open(os.path.join(EV, "precision_checks.json")))
    cmpw = json.load(open(os.path.join(EV, "compare_worker_sectors.json")))["summary"]
    out = dict(
        statement="Independent NUMERICAL (float64) reproduction plus small-M brute-force validation; "
                  "NOT a rigorous certificate.",
        headline_p_1_5=dict(Ic_nats=base, Ic_bits=base / math.log(2),
                            worker_interval_bits=cmpw["worker_total"], inside=cmpw["mine_inside_total"]),
        sign_controls={k: dict(p=v["p"], Ic_bits=v["Ic_bits"]) for k, v in runs.items() if v["p"] != "1/5"},
        p_1_5_variants_minus_baseline_nats=conv,
        validation_small=val,
        precision=dict(
            B_recursion_max_rel_err=prec["P1_B_recursion_vs_mpmath"]["max_rel_error"],
            coeff_g_max_rel=prec["P2_coefficients_vs_mpmath"]["g_max_rel"],
            coeff_h_max_rel=prec["P2_coefficients_vs_mpmath"]["h_max_rel"],
            block_float_vs_mpmath=[(d["r"], d["abs_err_dS"]) for d in prec["P3_block_float_vs_mpmath"]],
            eigensolver_spread=[(d["r"], d["spread"]) for d in prec["P4_eigensolver"]]),
        worker_comparison=cmpw,
        runs=runs,
        evidence_sha256={os.path.basename(f): sha(f) for f in sorted(glob.glob(os.path.join(EV, "*.json")))
                         if not f.endswith("SUMMARY.json")},
    )
    json.dump(out, open(os.path.join(EV, "SUMMARY.json"), "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("headline_p_1_5", "sign_controls", "p_1_5_variants_minus_baseline_nats")},
                     indent=1))


if __name__ == "__main__":
    main()
