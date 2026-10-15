"""Exact rational arithmetic check of the worker's constant-matrix norm separation."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def exp_bounds(x: int, degree: int = 80):
    """Taylor lower bound; next-term geometric majorant is a rigorous upper bound."""
    if x < 0 or degree + 2 <= x:
        raise ValueError("Expected nonnegative x and decreasing tail ratios")
    term = Fraction(1)
    lower = term
    for k in range(1, degree + 1):
        term *= Fraction(x, k)
        lower += term
    next_term = term * Fraction(x, degree + 1)
    upper = lower + next_term / (1 - Fraction(x, degree + 2))
    return lower, upper


def encode(value: Fraction):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator),
            "approximation": float(value)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bounds = {x: exp_bounds(x) for x in (1, 2, 6, 10)}
    e1lo, e1hi = bounds[1]
    e2lo, e2hi = bounds[2]
    e6lo, _ = bounds[6]
    _, e10hi = bounds[10]
    literal_gain_squared_upper = 2 * (e2hi - 1) / (1 - 1 / e1lo) ** 2
    uncontrolled_p1_lower = e2lo / 3 - 1 + Fraction(2, 3) / e1hi
    uncontrolled_energy_lower = uncontrolled_p1_lower * (e6lo - 1) / 2
    control_gain_squared_upper = (e10hi - 11) / 4
    best_control_energy_lower = uncontrolled_energy_lower / (1 + control_gain_squared_upper / 10000)
    checks = {
        "literal_zero_control_gain_strictly_below_6": literal_gain_squared_upper < 36,
        "uncontrolled_mean_square_energy_strictly_above_18_squared": uncontrolled_energy_lower > 324,
        "adapted_control_map_gain_strictly_below_75": control_gain_squared_upper < 5625,
        "every_controller_mean_square_gain_strictly_above_6": best_control_energy_lower > 36,
        "coarse_every_controller_gain_strictly_above_14_4": best_control_energy_lower > Fraction(72, 5) ** 2,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    report = {
        "scope": "exact arithmetic of analytic bounds, not a stochastic proof kernel",
        "plant": {"A": -1, "B": 1, "C": 1, "A0": 2, "B0": 0,
                  "D0": [1, 0], "D1": [0, 100], "h": 1, "T": 5, "x0": 0},
        "gamma": 6,
        "disturbances": "square-integrable adapted processes, zero outside [0,4]",
        "exponential_bounds": {str(x): {"lower": encode(v[0]), "upper": encode(v[1])}
                               for x, v in bounds.items()},
        "literal_gain_squared_upper": encode(literal_gain_squared_upper),
        "uncontrolled_energy_lower": encode(uncontrolled_energy_lower),
        "control_gain_squared_upper": encode(control_gain_squared_upper),
        "every_controller_mean_square_gain_squared_lower": encode(best_control_energy_lower),
        "checks": checks,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "verified": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"verified": True, "checks": checks,
                      "literal_gain_squared_upper": float(literal_gain_squared_upper),
                      "every_controller_mean_square_gain_squared_lower": float(best_control_energy_lower),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
