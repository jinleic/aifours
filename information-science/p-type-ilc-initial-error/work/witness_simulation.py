"""An initial-error-only nonlinear diagnostic; no parameter search.

This additional check was specified after the main suite: simulate its already
certified finite sign witnesses on nonlinear coordinate versions of integrators.
The original suite and every result are retained. Run from the target root.
"""
import csv
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"


def output(x):
    return x + 0.2 * math.sin(x)


def initial_position(a):
    x = a
    for _ in range(8):
        x -= (output(x) - a) / (1 + 0.2 * math.cos(x))
    assert abs(output(x) - a) < 1e-14
    return x


def trial(q, steps, a, u):
    # g(x)=x+0.2*sin(x), g'>=0.8, so the state transformation is global.
    # q=1: x'=u/g'(x), y=g(x). q=2: x1'=x2/g'(x1), x2'=u.
    # These are actual nonlinear plants, not cancellation inside the controller.
    x = np.zeros(q)
    x[0] = initial_position(a)
    y = np.empty(steps + 1)
    y[0] = output(x[0])
    h = 1 / steps
    def rhs(state, control):
        denominator = 1 + 0.2 * math.cos(state[0])
        if q == 1:
            return np.array([control / denominator])
        return np.array([state[1] / denominator, control])
    for j in range(steps):
        middle = (u[j] + u[j + 1]) / 2
        k1 = rhs(x, u[j])
        k2 = rhs(x + h * k1 / 2, middle)
        k3 = rhs(x + h * k2 / 2, middle)
        k4 = rhs(x + h * k3, u[j + 1])
        x += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        y[j + 1] = output(x[0])
    return y


def main():
    certificates = json.loads((OUT / "exact-certificates.json").read_text())
    witnesses = [w for w in certificates["finite_exact_witnesses"] if w["horizon"] == 128]
    records, summary = [], []
    for witness in witnesses:
        q = witness["relative_degree"]
        expected = witness["output_float"]
        for steps in (400, 800):
            t = np.linspace(0, 1, steps + 1)
            psi = t ** q
            for method in ("pure-P", "filtered"):
                u = np.zeros(steps + 1)
                theta = 0.0
                for i, sign in enumerate(witness["a_signs"]):
                    a = sign * 0.05
                    if method == "filtered":
                        u.fill(math.factorial(q) * theta)
                    y = trial(q, steps, a, u)
                    records.append({"q": q, "steps": steps, "method": method,
                                    "trial": i, "initial_output": a,
                                    "initial_physical_state": initial_position(a),
                                    "output_at_one": float(y[-1]),
                                    "sup_error": float(np.max(np.abs(y))),
                                    "input_at_zero": float(u[0])})
                    if method == "pure-P":
                        u -= y
                    else:
                        theta -= 0.7 * (2*q + 1) * np.trapezoid(psi * y, t)
                        assert np.max(np.abs(y)) <= (1 + (2*q+1)/(q+1)) * 0.05 + 1e-5
                numerical = float(y[-1])
                if method == "pure-P":
                    assert abs(numerical - expected) < 1e-3
                summary.append({"q": q, "steps": steps, "method": method,
                                "output_at_trial128_time1": numerical,
                                "pure_P_exact_output": expected if method == "pure-P" else None,
                                "difference_from_exact": abs(numerical-expected) if method == "pure-P" else None,
                                "sup_error_last_trial": float(np.max(np.abs(y)))})
    with (OUT / "nonlinear-witness-trials.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    report = {"command": f"{sys.executable} work/witness_simulation.py",
              "date_pt": "2026-10-14", "evidence_label": "Empirical evidence",
              "purpose": "Initial-error-only finite witness, not infinite divergence certification",
              "physical_state_bound": "0.05/0.8=0.0625 (actual state magnitudes are also recorded)",
              "controller_information": "The filtered controller exploits the known transformed input-output basis; P0 does not.",
              "summary": summary}
    (OUT / "nonlinear-witness.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
