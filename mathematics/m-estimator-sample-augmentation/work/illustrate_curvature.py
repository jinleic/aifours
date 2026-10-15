#!/usr/bin/env python3
"""Seeded illustration of Theorem 9; simulations are not its proof.
Run: uv run --with numpy==2.5.4 python work/illustrate_curvature.py
"""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"

from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261015
RNG = np.random.default_rng(SEED)




def fit(x, y):
    # For this axis-aligned design and odd psi, the coordinate equation is
    # sum psi(beta_j - x_ij*y_i)=0. No objective-value comparison is needed.
    assert np.all(np.sum(np.abs(x), axis=1) == 1)
    beta = np.zeros(2)
    maximum_iterations = 0
    for coordinate in range(2):
        selected = x[:, coordinate] != 0
        signed = x[selected, coordinate]*y[selected]
        locations, counts = np.unique(signed, return_counts=True)
        total = int(counts.sum())
        lower, upper = float(locations[0]), float(locations[-1])
        for iteration in range(80):
            midpoint = (lower+upper)/2
            displacement = midpoint-locations
            score = float(counts@(displacement+np.tanh(displacement)))
            if abs(score)/total < 1e-12:
                beta[coordinate] = midpoint
                maximum_iterations = max(maximum_iterations, iteration)
                break
            if score > 0:
                upper = midpoint
            else:
                lower = midpoint
        else:
            raise RuntimeError("Scalar score bisection did not converge")
    residual = y-x@beta
    gradient = -x.T@(residual+np.tanh(residual))
    gradient_residual = float(np.linalg.norm(gradient)/len(y))
    assert gradient_residual < 1e-11
    return beta, gradient_residual, maximum_iterations


def main():
    cycle = np.array([[1., 0.], [-1., 0.], [0., 1.], [0., -1.]])
    results = []
    trials = 400
    maximum_gradient = 0.
    maximum_iterations = 0
    for n in (16, 17, 64, 65, 256, 1024):
        x = cycle[np.arange(n)%4]
        xx = np.vstack((x, x))
        # The 0/2 equiprobable population criterion is this finite objective / 2.
        theta, residual, iterations = fit(xx, np.concatenate((np.zeros(n), np.full(n, 2.))))
        if n%4 == 0:
            assert np.linalg.norm(theta) < 1e-10
        maximum_gradient = max(maximum_gradient, residual)
        maximum_iterations = max(maximum_iterations, iterations)
        original_squared, pooled_squared = [], []
        original, pooled = [], []
        for _ in range(trials):
            errors = 2*RNG.integers(0, 2, size=(2, n))
            first, residual1, iterations1 = fit(x, errors[0])
            both, residual2, iterations2 = fit(xx, errors.ravel())
            maximum_gradient = max(maximum_gradient, residual1, residual2)
            maximum_iterations = max(maximum_iterations, iterations1, iterations2)
            original_squared.append(float(np.sum((first-theta)**2)))
            pooled_squared.append(float(np.sum((both-theta)**2)))
            original.append(first)
            pooled.append(both)
        smallest = float(np.linalg.eigvalsh(x.T@x)[0])
        results.append({"n": n, "trials": trials,
            "population_minimizer": theta.tolist(), "smallest_gram_eigenvalue": smallest,
            "original_mean": np.mean(original, axis=0).tolist(),
            "pooled_mean": np.mean(pooled, axis=0).tolist(),
            "original_mse_about_population": float(np.mean(original_squared)),
            "pooled_mse_about_population": float(np.mean(pooled_squared)),
            "theorem_original_mse_upper_bound": 8/smallest,
            "theorem_pooled_mse_upper_bound": 4/smallest})
    assert maximum_gradient < 1e-11
    output = {"scope": "illustration only, not proof", "seed": SEED, "numpy": np.__version__,
              "loss": "r^2/2 + log(cosh(r))", "curvature_bounds": [1, 2],
              "error_law": {"values": [0, 2], "probabilities": [.5, .5], "variance": 1},
              "score_mean_at_truth": float(1+.5*np.tanh(2)),
              "thread_cap": 1, "solver": "coordinate monotone-score bisection",
              "maximum_normalized_gradient_residual": maximum_gradient,
              "maximum_bisection_iterations": maximum_iterations,
              "records": results,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'evidence/curvature-monte-carlo.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
