#!/usr/bin/env python3
"""Seeded illustrations, not proofs. Run from the target directory with
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  uv run --with numpy --with scipy python work/illustrate.py
"""
import json
import os
from pathlib import Path

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"

import numpy as np
import scipy
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261014
RNG = np.random.default_rng(SEED)
FORMS = np.array([[2, 0, -2, 0], [-2, 0, -2, 0], [0, 2, -2, 2],
                  [0, -2, -2, 2], [0, 0, .5, 0], [0, 0, .5, -.5]], dtype=float)


def rho(value):
    return 10 * abs(value) + max(value - 1, 0)


def fit_triangle(m, high_errors, positive_counts):
    """Full finite-sample rho objective, aggregated by identical row/error.

    Each low epigraph variable is divided by d, an exact conditioning change.
    Its right side retains ALL three rho pieces, not only the local limit.
    """
    d = .2 / m
    entries = []
    for errors in high_errors:
        for coordinate, error in enumerate(errors):
            row = np.zeros(4)
            row[coordinate] = 1
            entries.append((row, int(error), 1., 1.))
    copies = len(high_errors)
    for r, form in enumerate(FORMS):
        plus = int(positive_counts[r])
        for error, count in ((1, plus), (-1, copies * m - plus)):
            if count:
                entries.append((-d * form, error, float(count), d))
    width = 4 + len(entries)
    cost = np.zeros(width)
    rows, rhs = [], []
    for index, (design, error, count, scale) in enumerate(entries):
        cost[4 + index] = count * scale
        for slope, intercept in ((-10., 0.), (10., 0.), (11., -1.)):
            row = np.zeros(width)
            row[:4] = -slope * design / scale
            row[4 + index] = -1
            rows.append(row)
            rhs.append((-slope * error - intercept + rho(error)) / scale)
    matrix, bound = np.array(rows), np.array(rhs)
    result = linprog(cost, A_ub=matrix, b_ub=bound, bounds=[(None, None)] * width,
                     method="highs-ds", options={"threads": 1,
                         "primal_feasibility_tolerance": 1e-8,
                         "dual_feasibility_tolerance": 1e-8})
    if not result.success:
        raise RuntimeError(result.message)
    primal = max(0., float(np.max(matrix @ result.x - bound)))
    dual = result.ineqlin.marginals
    stationarity = float(np.max(np.abs(matrix.T @ dual - cost)))
    dual_sign = max(0., float(np.max(dual)))
    gap = abs(float(cost @ result.x - bound @ dual))
    if max(primal, stationarity, dual_sign, gap) > 1e-6:
        raise AssertionError((primal, stationarity, dual_sign, gap))
    return result.x[:4], max(primal, stationarity, dual_sign, gap)


def triangular_trials(trials=200):
    records = []
    for m in (30, 1000, 30000, 1000000):
        errors = []
        original_bad = pooled_bad = asymptotic_bad = 0
        max_residual = 0.
        for _ in range(trials):
            high = RNG.choice([-1, 1], size=(2, 2))
            counts = RNG.binomial(m, .5, size=(2, 6))
            original, residual = fit_triangle(m, high[:1], counts[0])
            pooled, residual2 = fit_triangle(m, high, counts.sum(axis=0))
            max_residual = max(max_residual, residual, residual2)
            s = np.where(high[0] == high[1], high[0], 0)
            predicted_v = abs(s[0]) - abs(s[1])
            original_bad += abs(original[3]) > .5
            pooled_bad += abs(pooled[3]) > .5
            asymptotic_bad += abs(predicted_v) > .5
            errors.append(abs(pooled[3] - predicted_v))
        records.append({"m": m, "n": 6*m+2, "trials": trials,
            "original_v_bad_fraction": original_bad/trials,
            "pooled_v_bad_fraction": pooled_bad/trials,
            "same_draw_limit_bad_fraction": asymptotic_bad/trials,
            "pooled_v_mean_error_to_limit": float(np.mean(errors)),
            "max_lp_primal_dual_residual": max_residual})
    return records


def sliding_path(last_block=9):
    last_index = 4 ** (last_block+1)
    eps = RNG.choice(np.array([-1, 1], dtype=np.int8), size=2*last_index+1)
    records = []
    for j in range(1, last_block+1):
        powers = 4 ** np.arange(1, j+1, dtype=np.int64)
        first = float(np.mean(eps[powers]))
        n_values = np.arange(4**j, 4**(j+1), dtype=np.int64)
        sums = np.zeros(len(n_values), dtype=np.int16)
        for index in powers:
            sums += eps[n_values+index]
        minimum, maximum = int(sums.min()), int(sums.max())
        records.append({"j": j, "n_range": [int(n_values[0]), int(n_values[-1])],
            "prefix_estimate": first, "second_block_min": minimum/j,
            "second_block_max": maximum/j,
            "pooled_min": (first+minimum/j)/2,
            "pooled_max": (first+maximum/j)/2,
            "all_plus_windows": int(np.sum(sums == j)),
            "all_minus_windows": int(np.sum(sums == -j))})
    return records


def pointwise_trials(trials=20000):
    records = []
    for j in (4, 16, 64, 256):
        first = (2*RNG.binomial(j, .5, trials)-j)/j
        second = (2*RNG.binomial(j, .5, trials)-j)/j
        pooled = (first+second)/2
        records.append({"informative_rows": j, "trials": trials,
            "prefix_mse": float(np.mean(first**2)),
            "pooled_mse": float(np.mean(pooled**2)),
            "theory_prefix_mse": 1/j, "theory_pooled_mse": 1/(2*j)})
    return records


def bounded_gram_trials(trials=400, maximum_n=4096):
    errors = RNG.choice([-1, 0, 1], size=(trials, maximum_n), p=[.25, .5, .25])
    weights = 1 / np.arange(1, maximum_n+1)
    right = np.cumsum(((errors <= 0)*2-1)*weights, axis=1)
    left = np.cumsum(((errors < 0)*2-1)*weights, axis=1)
    uniform = RNG.uniform(-1, 1, size=(trials, maximum_n))
    lower = np.maximum.accumulate((uniform-1)/weights, axis=1)
    upper = np.minimum.accumulate((uniform+1)/weights, axis=1)
    return [{"n": n, "trials": trials, "gram": float(np.sum(weights[:n]**2)),
             "lad_unique_truth_fraction": float(np.mean((left[:, n-1] < 0) & (right[:, n-1] > 0))),
             "flat_loss_mean_argmin_diameter": float(np.mean(upper[:, n-1]-lower[:, n-1]))}
            for n in (16, 64, 256, 1024, 4096)]


def main():
    result = {"kind": "seeded illustrations, not proofs", "seed": SEED,
              "numpy": np.__version__, "scipy": scipy.__version__, "thread_cap": 1,
              "triangular": triangular_trials(), "sliding_path": sliding_path(),
              "pointwise": pointwise_trials(), "bounded_gram": bounded_gram_trials()}
    target = ROOT / "evidence/monte-carlo.json"
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
