#!/usr/bin/env python3
"""Exact integer/rational replay. Does not import the witness generator.

All accept/reject decisions use integers or fractions. Decimal values in the
output are presentation only. The infinite statements have written proofs in
RESULTS.md; their finite algebra controls here are not substitutes for proofs.
"""
import argparse
from fractions import Fraction as F
from itertools import combinations
import json
from math import isqrt
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]


def lift_cartesian(a, b):
    """Return six lifts in coordinates (X,Y) meaning (X/2,sqrt(3)*Y/2)."""
    x, y = 2 * a + b, b
    lifts = []
    for _ in range(6):
        lifts.append((x, y))
        assert (x - 3 * y) % 2 == 0 and (x + y) % 2 == 0
        x, y = (x - 3 * y) // 2, (x + y) // 2
    assert (x, y) == lifts[0]
    return lifts


def verify_centers(centers, lower=100, upper=400, diameter=F(1)):
    lifts = [p for a, b in centers for p in lift_cartesian(a, b)]
    assert len(set(lifts)) == 6 * len(centers), "duplicate center orbit"
    for x, y in lifts:
        assert 4 * lower <= x * x + 3 * y * y <= 4 * upper, "outside annulus"
    minimum4 = min((x - u) ** 2 + 3 * (y - v) ** 2
                   for (x, y), (u, v) in combinations(lifts, 2))
    assert minimum4 >= 4 * diameter * diameter, "overlapping disks"
    return minimum4, lifts


def sqrt_bracket(value, digits=30):
    value = F(value)
    scale = 10 ** digits
    k = isqrt(value.numerator * scale * scale // value.denominator)
    low, high = F(k, scale), F(k + 1, scale)
    assert low * low <= value < high * high
    return low, high


def golden_pair_bound():
    # r_i^2 = 100 + 150*i/91, theta_i = 2*pi*i*(3-sqrt(5))/2.
    a, b = F(9700, 91), F(10900, 91)  # i=4 and i=12, difference 8.
    sqrt5_low, _ = sqrt_bracket(5)
    delta_upper = 9 - 4 * sqrt5_low
    assert 0 < delta_upper < F(3, 50)
    angle_upper = F(22, 7) * delta_upper / 3  # pi < 22/7.
    product_lower, _ = sqrt_bracket(a * b)
    cosine_lower = 1 - angle_upper * angle_upper / 2  # cos(x) >= 1-x^2/2.
    assert cosine_lower > 0
    distance2_upper = a + b - 2 * product_lower * cosine_lower
    assert distance2_upper < F(77, 100) < 1
    return distance2_upper


# Independent exact arithmetic in Q(sqrt(5)), represented by (a,b).
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def power(x, n):
    result = (F(1), F(0))
    for _ in range(n):
        result = mul(result, x)
    return result


def positive(x):
    a, b = x
    if a >= 0 and b >= 0:
        return a > 0 or b > 0
    if a <= 0 and b <= 0:
        return False
    return a * a > 5 * b * b if a > 0 else 5 * b * b > a * a


def fibonacci_controls():
    fib = [0, 1]
    for _ in range(52):
        fib.append(fib[-1] + fib[-2])
    gamma = (F(3, 2), F(-1, 2))
    invphi = (F(-1, 2), F(1, 2))
    phi = (F(1, 2), F(1, 2))
    previous = None
    for k in range(2, 51):
        residual = add(mul((F(fib[k]), F(0)), gamma), (-F(fib[k - 2]), F(0)))
        expected = mul((F((-1) ** k), F(0)), power(invphi, k))
        assert residual == expected
        assert positive(mul((F((-1) ** k), F(0)), residual))
        assert fib[k + 1] ** 2 - fib[k] ** 2 == fib[k - 1] * fib[k + 2]
        threshold = mul(power(phi, 2 * k + 1), (F(fib[k - 1] * fib[k + 2]), F(0)))
        if previous is not None:
            assert positive(add(threshold, (-previous[0], -previous[1])))
        previous = threshold
    return 49


def must_reject(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError("negative control was accepted")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="save the deterministic receipt")
    args = parser.parse_args()
    witness = json.loads((ROOT / "results" / "lattice-witness.json").read_text())
    assert witness["disk_diameter"] == 1
    assert witness["center_radius_squared_bounds"] == [100, 400]
    assert witness["frustum_radius_bounds"] == ["19/2", "41/2"]
    centers = [tuple(p) for p in witness["centers"]]
    assert len(centers) == 183
    minimum4, lifts = verify_centers(centers)
    assert minimum4 == 4
    assert {(x, -y) for x, y in lifts} == set(lifts), "reflection symmetry failed"
    small = [(-3, 0), (-3, 1), (-3, 2), (-2, 0), (-2, 1), (-1, 0)]
    assert verify_centers(small, 1, 9)[0] == 4
    must_reject(lambda: verify_centers(centers + [centers[0]]))
    must_reject(lambda: verify_centers(centers + [(25, 0)]))
    must_reject(lambda: verify_centers(centers, diameter=F(101, 100)))
    bound = golden_pair_bound()
    controls = fibonacci_controls()
    receipt = {
        "status": "PASS",
        "python": platform.python_version(),
        "arithmetic": "integer and fractions.Fraction; no floating acceptance decisions",
        "finite_C1": {
            "N": len(centers), "planar_lifts": len(lifts),
            "lattice_min_distance_squared": "1",
            "golden_pair_indices_zero_based": [4, 12],
            "golden_pair_distance_squared_upper_rational": str(bound),
            "golden_pair_distance_squared_upper_display": float(bound),
            "certified_comparison": "golden pair squared distance < 77/100 < 1",
        },
        "controls": {
            "six_orbit_small_instance": "PASS",
            "reflection_invariance": "PASS",
            "negative_controls_rejected": 3,
            "negative_control_cases": ["repeated orbit", "exterior point (25,0)", "diameter 101/100"],
            "Fibonacci_residual_and_ordered_threshold_identities": controls,
            "identity_index_range": [2, 50],
        },
        "scope": "Finite witness certified; infinite results require RESULTS.md proofs; no elasticity or universal C2 proof.",
    }
    if args.write:
        (ROOT / "results" / "certificate.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: N=183, 1098 planar lifts, exact minimum distance squared=1")
    print(f"PASS: golden pair (4,12) squared distance < 0.77 (rational upper bound approx {float(bound):.12f})")
    print("PASS: 6-orbit control; reflection; 3 rejected negative controls; 49 Fibonacci identities")


if __name__ == "__main__":
    main()
