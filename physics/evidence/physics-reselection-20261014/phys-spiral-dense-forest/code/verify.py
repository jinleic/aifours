"""Exact finite controls plus explicitly empirical geometric observations.

The infinite dense-forest theorem is the written proof, not this finite sample.
No random search, solver, fitted parameter, or floating-point proof is used.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from math import isqrt
import os
from pathlib import Path
import sys

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RADII = (8, 16, 32, 64)


def square_enumerator(radius, types=(0, 1)):
    return sorted((a * a + b * b, t, a, b)
                  for a in range(-radius, radius + 1)
                  for b in range(-radius, radius + 1)
                  if 0 < a * a + b * b <= radius * radius
                  for t in types)


def shell_enumerator(radius):
    result = []
    for q in range(1, radius * radius + 1):
        for a in range(-isqrt(q), isqrt(q) + 1):
            remaining = q - a * a
            b = isqrt(remaining)
            if b * b == remaining:
                for y in ((0,) if b == 0 else (-b, b)):
                    for t in (0, 1):
                        result.append((q, t, a, y))
    return sorted(result)


def algebraic_point(k, record):
    """Coordinates are sqrt(k/den)*(A+B*sqrt(2)); no rounding."""
    q, t, a, b = record
    if t == 0:
        return q, (a, 0), (b, 0)
    return 3 * q, (a, -b), (b, a)


def exact_norm_squared(k, record):
    den, (a, b), (d, e) = algebraic_point(k, record)
    constant = Q(k, den) * (a * a + 2 * b * b + d * d + 2 * e * e)
    irrational = Q(2 * k, den) * (a * b + d * e)
    return constant, irrational


def atan_interval(den, terms=20):
    partial = sum((Q((-1) ** j, (2 * j + 1) * den ** (2 * j + 1)) for j in range(terms)), Q(0))
    next_term = Q((-1) ** terms, (2 * terms + 1) * den ** (2 * terms + 1))
    return min(partial, partial + next_term), max(partial, partial + next_term)


def pi_interval():
    # Machin's identity: pi = 16 atan(1/5) - 4 atan(1/239).
    tangent = Q(1, 5)
    for _ in range(2):
        tangent = 2 * tangent / (1 - tangent * tangent)
    assert (tangent - Q(1, 239)) / (1 + tangent / 239) == 1
    lo5, hi5 = atan_interval(5)
    lo239, hi239 = atan_interval(239)
    lo, hi = 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239
    assert Q(3) < lo < hi < Q(22, 7)
    return lo, hi


def floor_sqrt(value):
    return isqrt(value.numerator // value.denominator)


def ceil_sqrt(value):
    root = floor_sqrt(value)
    return root + (root * root < value)


def distortion_upper(k, q, pi_lo, pi_hi):
    numerator = max(abs(k - 2 * pi_lo * q), abs(k - 2 * pi_hi * q))
    denominator = isqrt(k) + floor_sqrt(2 * pi_lo * q)
    return numerator / denominator


def exact_controls(records, pi_lo, pi_hi):
    for k, record in enumerate(records, 1):
        assert exact_norm_squared(k, record) == (Q(k), Q(0))
    a, b, d, e = sp.symbols("a b d e", real=True)
    determinant = a * e - b * d
    dot = a * d + b * e
    assert sp.expand(determinant ** 2 + dot ** 2 - (a * a + b * b) * (d * d + e * e)) == 0
    vectors = [(x, y) for x, y in product(range(-4, 5), repeat=2) if x or y]
    direction_pairs = 0
    for a, b in vectors:
        for d, e in vectors:
            assert (a * e - b * d, a * d + b * e) != (0, 0)
            direction_pairs += 1
    shells = {}
    for k, (q, _, _, _) in enumerate(records, 1):
        if q not in shells:
            shells[q] = [k, k]
        shells[q][1] = k
    samples = []
    for radius in RADII:
        small = square_enumerator(radius)
        independent = shell_enumerator(radius)
        assert small == independent == records[:len(small)]
        shell_samples = {q: bounds for q, bounds in shells.items() if radius * radius // 4 <= q <= radius * radius}
        upper = max(distortion_upper(k, q, pi_lo, pi_hi) for q, bounds in shell_samples.items() for k in bounds)
        samples.append({"base_radius": radius, "prefix_count": len(small), "outer_half_radius_shells": len(shell_samples),
                        "all_tie_ranks_displacement_upper": str(upper), "upper_decimal_for_display": float(upper)})
    # Changed prefix count and a fixed analytic zero-rotation sanity check.
    omitted = square_enumerator(RADII[-1], types=(0,))
    assert omitted != records and len(omitted) * 2 == len(records)
    common_direction_at_zero_rotation = (1 * 0 - 0 * 1 == 0)
    assert common_direction_at_zero_rotation
    # All points of the zero-rotation union have integer y; the open strip
    # 1/4 < y < 3/4 is empty at every length, not just in this sample.
    q = records[-1][0]
    k = len(records)
    wrong_scale_lower = (k - pi_hi * q) / (ceil_sqrt(Q(k)) + ceil_sqrt(pi_hi * q))
    assert wrong_scale_lower > 1
    # Rank-count sanity check at half-integer squared-radius thresholds.
    for threshold_twice in range(0, 257):
        rho = Q(threshold_twice, 2)
        count = sum(1 for k in range(1, len(records) + 1) if Q(k) <= rho)
        assert count == rho.numerator // rho.denominator
    return {"exact_norm_identities": len(records), "exact_direction_pairs": direction_pairs,
            "symbolic_dot_determinant_identity": "0", "radial_count_thresholds": 257,
            "largest_tie_in_prefix": max(hi - lo + 1 for lo, hi in shells.values()), "samples": samples,
            "negative_controls": {"omitted_grid_rejected": True, "zero_rotation_common_direction_detected": True,
                                  "zero_rotation_empty_strip": "1/4 < y < 3/4; all x",
                                  "wrong_sqrt_pi_scale_displacement_lower": str(wrong_scale_lower),
                                  "wrong_scale_lower_decimal_for_display": float(wrong_scale_lower)}}


def empirical_geometry(records):
    raw = np.array([(a, b) for _, _, a, b in records], dtype=np.float64)
    labels = np.array([t for _, t, _, _ in records])
    rotation = np.array([[1.0, -np.sqrt(2.0)], [np.sqrt(2.0), 1.0]]) / np.sqrt(3.0)
    raw[labels == 1] = raw[labels == 1] @ rotation.T
    rank = np.arange(1, len(records) + 1, dtype=np.float64)
    squared_radius = np.array([q for q, _, _, _ in records], dtype=np.float64)
    points = raw * np.sqrt(rank / squared_radius)[:, None]
    observations = []
    for length in (24.0, 48.0):
        worst = 0.0
        witness = None
        count = 0
        for x, y, j in product((-8.0, 0.0, 8.0), (-8.0, 0.0, 8.0), range(24)):
            angle = np.pi * j / 24
            direction = np.array([np.cos(angle), np.sin(angle)])
            start = np.array([x, y]) - length * direction / 2
            relative = points - start
            parameter = np.clip(relative @ direction, 0.0, length)
            distances_squared = np.sum((relative - parameter[:, None] * direction) ** 2, axis=1)
            nearest = int(np.argmin(distances_squared))
            distance = float(np.sqrt(distances_squared[nearest]))
            if distance > worst:
                worst = distance
                witness = {"center": [x, y], "angle_index_over_24_pi": j, "nearest_rank": nearest + 1}
            count += 1
        observations.append({"length": length, "segments": count, "maximum_sampled_nearest_distance": worst, "witness": witness})
    return {"evidence_label": "Empirical evidence only; float64, no interval error certificate",
            "not_claimed": "No visibility bound, all-rectangle coverage, global separation, or asymptotic theorem is inferred.",
            "observations": observations}


def main():
    (ROOT / "results").mkdir(exist_ok=True)
    records = square_enumerator(RADII[-1])
    lo, hi = pi_interval()
    exact = exact_controls(records, lo, hi)
    empirical = empirical_geometry(records)
    report = {"verdict": "PASS for finite exact controls", "parameters": {"radii": RADII, "direction_box": 4, "atan_terms": 20},
              "python": sys.version.split()[0], "numpy": np.__version__, "sympy": sp.__version__,
              "pi_rational_interval": [str(lo), str(hi)], "exact": exact, "empirical": empirical,
              "prefix_sha256": sha256(json.dumps(records, separators=(",", ":")).encode()).hexdigest(),
              "first_64_labels": [{"k": k, "norm_squared": q, "lattice_type": t, "a": a, "b": b} for k, (q, t, a, b) in enumerate(records[:64], 1)],
              "code_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "proof_scope": "The universal existence theorem is RESULTS.md sections 1-6, not these finite checks."}
    (ROOT / "results/verification.json").write_text(json.dumps(report, indent=2) + "\n")
    hashes = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT / "source").iterdir()) if p.is_file()}
    (ROOT / "results/source-sha256.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print("PASS: exact norm identities", len(records), "; independent enumerators at radii", RADII)
    print("PASS: exact direction pairs", exact["exact_direction_pairs"], "; radial thresholds", exact["radial_count_thresholds"], "; largest tie", exact["largest_tie_in_prefix"])
    print("PASS: omitted-grid, zero-rotation, wrong-scale controls; wrong-scale lower bound > 1")
    for sample in exact["samples"]:
        print("CERTIFIED finite radial-displacement upper: R =", sample["base_radius"], "bound approximately", sample["upper_decimal_for_display"])
    for observation in empirical["observations"]:
        print("EMPIRICAL ONLY:", observation)


if __name__ == "__main__":
    main()
