"""Consolidated, re-runnable record of the reduced-SDP experiments (floating point, Clarabel).

tau* (max over the region of the uniform block margin) ~ 0 (|tau| < 1e-7): numerically feasible;
tau* clearly negative: numerically infeasible (a PROPOSAL only; no exact certificate produced here).
"""
import json
import time

from sdp_linear_obj import objective_coeffs, optimize
from sdp_run import solve

CASES = [
    # (label, n, K, d, sizes, lp, pure, expectation)
    ("ctrl_steane_exists", 7, 2, 3, (1, 2), True, False, "feasible (Steane exists)"),
    ("ctrl_833_exists", 8, 8, 3, (1, 2), True, False, "feasible ([[8,3,3]] exists)"),
    ("ctrl_833_K3_exists", 8, 3, 3, (1, 2), True, False, "feasible (subcode of [[8,3,3]])"),
    ("ctrl_743_LP_excluded", 7, 4, 3, (), False, False, "infeasible (LP-excluded)"),
    ("ctrl_893_AMH_excluded", 8, 9, 3, (), False, False, "infeasible (AMH SDP exclusion, LP feasible)"),
    ("ctrl_623_pure_excluded", 6, 2, 3, (), True, True, "infeasible (AMH: ((6,2,3)) must be impure)"),
    ("ctrl_623_general_exists", 6, 2, 3, (), True, False, "feasible (impure ((6,2,3)) exist)"),
    ("target_733_AMH", 7, 3, 3, (), False, False, "AMH Table 1: not excluded"),
    ("target_733_AMH_LP_ptrace12", 7, 3, 3, (1, 2), True, False, "NEW constraints added"),
    ("target_733_pure_AMH_LP_ptrace12", 7, 3, 3, (1, 2), True, True, "NEW constraints, pure codes"),
]

if __name__ == "__main__":
    out = {"cases": [], "ranges": []}
    for lab, n, K, d, sizes, lp, pure, exp in CASES:
        r = solve(n, K, d, sizes, lp, pure)
        r.pop("x", None)
        r.update({"label": lab, "expectation": exp})
        out["cases"].append(r)
        print(json.dumps(r))
    for pure in (False, True):
        for name in ("S0", "S1", "A1", "A2", "A3", "A4", "A5"):
            if pure and name in ("A1", "A2"):
                continue
            c = objective_coeffs(name, 7, 3)
            lo = optimize(7, 3, 3, (1, 2), True, pure, c, "min")
            hi = optimize(7, 3, 3, (1, 2), True, pure, c, "max")
            rec = {"pure": pure, "obj": name, "min": lo[1], "max": hi[1], "status": [lo[0], hi[0]]}
            out["ranges"].append(rec)
            print(json.dumps(rec))
    out["generated"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(out, open("../evidence/sdp_suite.json", "w"), indent=1)
