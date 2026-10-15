"""Independent numerical checks for scalar-literal-norm.md; not a proof kernel."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad, solve_ivp
from scipy.linalg import eigh


def moment_energy(a: float, sigma: float, horizon: float, input_function):
    c = 2 * a + sigma * sigma

    def rhs(t, y):
        w = input_function(t)
        return [a * y[0] + w, c * y[1] + 2 * w * y[0], y[1]]

    result = solve_ivp(rhs, (0, horizon), [0.0, 0.0, 0.0],
                       rtol=2e-11, atol=1e-12, method="DOP853")
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.y[2, -1])


def kernel_matrix(a: float, sigma: float, horizon: float, size: int):
    nodes, weights = leggauss(size)
    nodes = (nodes + 1) * (horizon / 2)
    weights = weights * (horizon / 2)
    c = 2 * a + sigma * sigma
    remaining = horizon - np.maximum(nodes[:, None], nodes[None, :])
    primitive = remaining if c == 0 else np.expm1(c * remaining) / c
    kernel = np.exp(a * np.abs(nodes[:, None] - nodes[None, :])) * primitive
    return nodes, weights, kernel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    a, sigma, horizon = -1.0, 1.0, 2.0
    results = {"scope": "numerical identities only; deterministic scalar inputs",
               "parameters": {"a": a, "sigma": sigma, "T": horizon}}
    comparisons = []
    for size in (128, 256, 512):
        nodes, weights, kernel = kernel_matrix(a, sigma, horizon, size)
        weighted = np.sqrt(weights[:, None] * weights[None, :]) * kernel
        largest = float(eigh(weighted, subset_by_index=[size - 1, size - 1],
                             eigvals_only=True)[0])
        row = {"quadrature_nodes": size, "mean_square_gain_estimate": math.sqrt(largest),
               "input_identities": []}
        for name, function in (("constant", lambda t: 1.0),
                               ("linear", lambda t: t),
                               ("sine", lambda t: math.sin(2 * t))):
            values = np.array([function(t) for t in nodes]) * weights
            integral = float(values @ kernel @ values)
            ode = moment_energy(a, sigma, horizon, function)
            relative = abs(integral - ode) / max(abs(ode), 1e-30)
            if relative >= 8 / (size * size):
                raise AssertionError((name, size, relative))
            row["input_identities"].append({"input": name, "kernel_energy": integral,
                                            "moment_ode_energy": ode, "relative_error": relative})
        comparisons.append(row)
    results["finite_horizon"] = comparisons
    if not comparisons[-1]["mean_square_gain_estimate"] < math.sqrt(2):
        raise AssertionError("Finite-horizon gain exceeded the proved infinite-horizon bound")

    path_values = []
    for slope in (-2.0, 0.0, 2.0):
        drift = a - sigma * sigma / 2 + sigma * slope

        def output(t):
            return t if drift == 0 else math.expm1(drift * t) / drift

        energy = quad(lambda t: output(t) ** 2, 0, horizon,
                      epsabs=1e-12, epsrel=1e-12)[0]
        path_values.append({"W_path_slope": slope, "output_norm": math.sqrt(energy)})
    if not path_values[0]["output_norm"] < path_values[1]["output_norm"] < path_values[2]["output_norm"]:
        raise AssertionError("Wiener-support monotonicity control failed")
    results["cameron_martin_path_controls"] = path_values

    regimes = []
    for drift in (-1.0, -0.5, -0.25, 0.0):
        c = 2 * drift + 1
        rows = []
        for length in (2.0, 8.0, 32.0, 128.0):
            energy_per_time = moment_energy(drift, 1.0, length, lambda t: 1.0) / length
            rows.append({"block_length": length, "block_mean_square_energy_per_time": energy_per_time})
        if not all(rows[j + 1]["block_mean_square_energy_per_time"] >
                   rows[j]["block_mean_square_energy_per_time"] for j in range(len(rows) - 1)):
            raise AssertionError("Unit-input block averages failed expected monotonicity")
        regime = {"a": drift, "sigma": 1.0, "c": c, "blocks": rows,
                  "proved_infinite_gain": math.sqrt(2 / (drift * c)) if c < 0 else "infinite"}
        regimes.append(regime)
    results["infinite_horizon_block_controls"] = regimes
    results["verified"] = True
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"verified": True, "finite_gain_estimate": comparisons[-1]["mean_square_gain_estimate"],
                      "largest_kernel_moment_relative_error": max(
                          x["relative_error"] for row in comparisons for x in row["input_identities"]),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
