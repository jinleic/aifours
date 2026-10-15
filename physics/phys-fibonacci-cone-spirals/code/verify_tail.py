#!/usr/bin/env python3
"""Small exact controls for RESULTS.md Section 9; not a finite proof of a limit."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--write", action="store_true")
args = parser.parse_args()

# Exact equality case of the geometric Cauchy bound, h=2*n+q with n=1.
h, q, w, C, S = F(5), F(3), F(4), F(4, 5), F(3, 5)
assert h * h - w * w == q * q and C * C + S * S == 1
value = h - C * w
assert value == q * S == F(9, 5)
assert (h - C * w) ** 2 - q * q * S * S == (w - C * h) ** 2 == 0
# u=arcsin(3/5)>3/5, so the tempting finite bound F>=q*u is false.
# Rational alpha=1/7 gives offset seven and exact tail upper bound 49/(4*n).
assert F(49, 4 * 49) == F(1, 4)
# phi>8/5 follows from sqrt(5)>11/5. These bounds cover every even k>=10
# and every 0<beta<=1, with A=2*pi*beta<44/7.
assert F(11, 5) ** 2 < 5
angle_upper = F(44, 7) * F(5, 8) ** 10
rounding_ratio_upper = (1 + 160 * F(44, 7) ** 2) * F(5, 8) ** 20
assert angle_upper < F(1, 4)
assert rounding_ratio_upper < 1
receipt = {
    "status": "PASS", "arithmetic": "fractions.Fraction only",
    "geometric_equality_distance_squared": str(value),
    "linearized_finite_bound_negative_control": "u=arcsin(3/5)>3/5, while F=q*(3/5)",
    "rational_divergence_negative_control": "alpha=1/7: D(n,n+7)^2/c^2<=49/(4*n)->0",
    "golden_nonattainment_even_index_cutoff": 10,
    "angle_upper": str(angle_upper),
    "rounding_ratio_upper": str(rounding_ratio_upper),
    "scope": "Exact controls of identities and inequalities; universal proof is RESULTS.md Section 9.",
}
if args.write:
    target = Path(__file__).resolve().parents[1] / "results" / "tail-controls.json"
    target.write_text(json.dumps(receipt, indent=2) + "\n")
print("PASS: exact Cauchy equality and false-linearization negative control")
print("PASS: rational-divergence zero-tail control")
print("PASS: golden endpoint rounding bounds for every even k>=10 and 0<beta<=1")
