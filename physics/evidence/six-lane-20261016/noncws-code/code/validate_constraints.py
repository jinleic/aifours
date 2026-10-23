"""Validate the reduced-SDP constraint builder (incl. the NEW partial-trace family) on explicit codes.

Positive controls (must satisfy every constraint they are entitled to):
  steane ((7,2,3)) pure; five-qubit+|00> ((7,2,3)) impure; [[6,4,2]]-subcode+|0> ((7,3,2));
  random 3-dim subcode of [[8,3,3]] ((8,3,3)).
Negative controls: random 3-dim subspace of 7 qubits; perturbed Steane.
Entitlement: ptrace{s} holds whenever s <= d-1 (s=0 always, for any projector).
"""
import json
import sys
import time

import numpy as np

import codes
from code_sdp import build, residuals
from gamma_orbits import orbit_sums
from kl_check import kl_report, kl_report_weight
from pauli_tools import pauli_expectations


def check(name, W, n, K, d_claim, d_true_note):
    t0 = time.time()
    rep = kl_report(W, n, d_claim - 1)
    t = pauli_expectations(W, n)
    Iset, lam, x = orbit_sums(t, n, K)
    Iset_, key, eqs, ineqs, blocks = build(n, K, d_claim, partial_trace_sizes=tuple(range(1, n)),
                                           lp=True, kl=True)
    er, ir, mins = residuals(x, Iset_, key, eqs, ineqs, blocks)
    out = {"name": name, "n": n, "K": K, "d_claim": d_claim, "note": d_true_note,
           "kl_max_dev_upto_d-1": rep["max_dev"], "kl_nonzero_scalars": rep["n_nonzero_scalars"],
           "eq_max_abs_by_family": {k: float(v) for k, v in er.items()},
           "ineq_min_by_family": {k: float(v) for k, v in ir.items()},
           "block_min_eig": float(np.min(mins)), "seconds": round(time.time() - t0, 2)}
    print(json.dumps(out))
    return out


if __name__ == "__main__":
    results = []
    St = codes.steane()
    results.append(check("steane_7_2_3_pure", St, 7, 2, 3, "positive control, d=3"))
    F = codes.tensor_zero(codes.five_qubit(), 2)
    results.append(check("five_plus_00_7_2_3_impure", F, 7, 2, 3, "positive control, impure d=3"))
    B642 = codes.stabilizer_code_basis(["XXXXXX", "ZZZZZZ"], 6)
    W732 = codes.tensor_zero(codes.random_subcode(B642, 3, seed=11), 1)
    results.append(check("sub642_plus_0_7_3_2", W732, 7, 3, 2, "positive control K=3, d=2 only"))
    R = codes.random_subspace(7, 3, seed=5)
    results.append(check("random_7_3_negative", R, 7, 3, 3, "negative control: not a code"))
    rng = np.random.default_rng(7)
    Sp = St + 0.05 * (rng.normal(size=St.shape) + 1j * rng.normal(size=St.shape))
    Sp, _ = np.linalg.qr(Sp)
    results.append(check("steane_perturbed_negative", Sp, 7, 2, 3, "negative control: corrupted Steane"))
    if len(sys.argv) > 1 and sys.argv[1] == "--with8":
        B833 = codes.code_8_3_3()
        print("[[8,3,3]] dim", B833.shape[1], "w<=2 max dev:", kl_report_weight(B833, 8, 1),
              kl_report_weight(B833, 8, 2), "w=3:", kl_report_weight(B833, 8, 3))
        W = codes.random_subcode(B833, 3, seed=3)
        results.append(check("sub833_8_3_3", W, 8, 3, 3, "positive control K=3, d=3 at n=8"))
    json.dump(results, open("../evidence/validate_constraints.json", "w"), indent=1)
