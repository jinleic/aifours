#!/usr/bin/env python3
"""Falsification search: no warning law may certify UNSAT below a proved SAT density.

If the formula and implementation are correct, the theorem and published
satisfiability lower bounds imply Psi_T >= 0 for every finite law at these
densities. A rigorous negative upper bound here would expose an error.
Not finding one is only a numerical consistency check, not a proof.
"""
from fractions import Fraction
import json
from pathlib import Path
import random
import time

from sat_independent_certificate import certify

CASES = [
    {"k": 3, "alpha": "7/2", "lower_bound_source": "3.52 algorithmic lower bound cited by Vorobyev and Achlioptas-Peres"},
    {"k": 4, "alpha": "79/10", "lower_bound_source": "7.91 lower bound, Achlioptas-Peres Table"},
    {"k": 5, "alpha": "187/10", "lower_bound_source": "18.79 lower bound, Achlioptas-Peres Table"},
]


def rational(value, scale=10000):
    return Fraction(max(1, min(scale - 1, round(value * scale))), scale)


def law(params):
    rates = [rational(x) for x in params[:3]]
    raw = [max(1e-4, x) for x in params[3:]]
    total = sum(raw)
    weights = [rational(x / total) for x in raw[:-1]]
    weights.append(1 - sum(weights))
    if weights[-1] <= 0:
        raise ValueError("invalid weights")
    return [str(r) for r in rates], [str(w) for w in weights]


def evaluate(case, params):
    rates, weights = law(params)
    trial = {"name": "search", "k": case["k"], "alpha": case["alpha"], "rates": rates,
             "weights": weights, "T": 128, "epsilon": "1/1000000000000", "y": 40}
    result = certify(trial)
    return float(Fraction(result["psi_upper_decimal_outward"])), rates, weights


def search(case, seed, starts=10, steps=45):
    generator = random.Random(seed)
    best = None
    evaluations = 0
    for _ in range(starts):
        point = [generator.uniform(0.02, 0.95) for _ in range(3)] + [generator.uniform(0.1, 1) for _ in range(3)]
        try:
            value, rates, weights = evaluate(case, point)
        except ValueError:
            continue
        evaluations += 1
        scale = 0.2
        for _ in range(steps):
            candidate = [min(0.995, max(0.0001, x + generator.gauss(0, scale))) for x in point]
            try:
                trial_value, trial_rates, trial_weights = evaluate(case, candidate)
            except ValueError:
                continue
            evaluations += 1
            if trial_value < value:
                point, value, rates, weights = candidate, trial_value, trial_rates, trial_weights
            else:
                scale = max(0.005, scale * 0.93)
        if best is None or value < best["psi_upper"]:
            best = {"psi_upper": value, "rates": rates, "weights": weights}
    return best, evaluations


def main():
    started = time.monotonic()
    rows = []
    violation = False
    for index, case in enumerate(CASES):
        best, evaluations = search(case, 20261015 + index)
        violation |= best["psi_upper"] < 0
        rows.append({**case, "T": 128, "best_rigorous_psi_upper": best["psi_upper"],
                     "best_law": {"rates": best["rates"], "weights": best["weights"]},
                     "evaluations": evaluations, "violation": best["psi_upper"] < 0})
    result = {"status": "FAIL" if violation else "PASS_NO_VIOLATION_FOUND", "rows": rows,
              "seconds": round(time.monotonic() - started, 1),
              "scope": "Seeded local search over three-atom rational laws; a found negative rigorous upper bound would falsify the implementation or theorem chain, while no violation is not a proof."}
    Path(__file__).with_name("sat-satisfiable-region-control.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if violation:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
