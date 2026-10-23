#!/usr/bin/env python3
"""reconstruct_controls.py: controls for reconstruct_e0.exact_unitarity. Lane ame46-support.

Positive control: Pandya's 60-term AME(4,6) state (pandya_control.TABLE). It has e = 0, t = 12, |6ψ| = 1 on T and
1/√2 on N. Its N, together with the phase solution θ that phase_check.phase_consistency computes from N's block
congruences (not Pandya's own signs), must pass the exact unitarity check of all three reshapings.
Negative controls, each of which must fail:
 (n1) θ shifted by 1/4 at one N point;
 (n2) one officer removed;
 (n3) one N point moved onto an officer line.
Output: evidence/reconstruct_controls.json.
"""
import json
import os
from fractions import Fraction as Fr

import pandya_control as pcn
import phase_check as pc
import reconstruct_e0 as rc

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    W = pcn.build()
    T = sorted(x for x, v in W.items() if v == pcn.R2)
    N = sorted(x for x, v in W.items() if v != pcn.R2)
    eqs = pc.block_equations(set(N))
    elems = sorted({x for _, tt in eqs for x, _ in tt})
    ph = pc.phase_consistency(eqs, elems)
    theta = {tuple(__import__("ast").literal_eval(k)): Fr(v) for k, v in (ph.get("theta") or {}).items()}
    out = {"pandya_t": len(T), "pandya_N": len(N), "phase_consistent": ph["complex_consistent"],
           "theta_verified": ph.get("theta_verified"), "theta_denominators": sorted({v.denominator for v in theta.values()})}
    ok, det = rc.exact_unitarity(N, T, theta)
    out["positive_pandya"] = {"ok": ok, "details": det}
    x0 = N[0]
    th1 = dict(theta)
    th1[x0] = th1.get(x0, Fr(0)) + Fr(1, 4)
    ok1, d1 = rc.exact_unitarity(N, T, th1)
    out["n1_phase_shift"] = {"rejected": not ok1, "reason": d1}
    ok2, d2 = rc.exact_unitarity(N, T[1:], theta)
    out["n2_officer_removed"] = {"rejected": not ok2, "reason": d2}
    t0 = T[0]
    y = (t0[0], t0[1], N[0][2], N[0][3])
    N3 = [z for z in N if z != N[0]] + [y] if y not in set(T) else N
    ok3, d3 = rc.exact_unitarity(N3, T, theta)
    out["n3_point_on_officer_line"] = {"rejected": not ok3, "reason": d3}
    out["all_required_true"] = bool(ok and not ok1 and not ok2 and not ok3)
    with open(os.path.join(HERE, "..", "evidence", "reconstruct_controls.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
