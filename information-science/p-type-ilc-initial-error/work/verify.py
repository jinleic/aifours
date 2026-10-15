"""Reproduce exact identities and bounded nonlinear ILC illustrations.

Run from the target root: <venv>/bin/python work/verify.py
No plots, external services, parameter fitting, or large computation are used.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import mpmath as mp
import numpy as np
from exact_checks import certificates

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
COMMAND = f"{sys.executable} work/verify.py"
TRIALS = 200
GAMMA = 0.7
EPS0, EPSETA, EPSXI = 0.02, 0.01, 0.005


def profile(t, params):
    a, b, p, r = params
    return 0.6 * a * np.sin(2 * np.pi * t + p) + 0.4 * b * np.cos(6 * np.pi * t + r)


def integrated_profile(t, params, order):
    a, b, p, r = params
    def exp_integral(omega, phase):
        w = 1j * omega
        remainder = np.exp(w * t)
        for k in range(order):
            remainder = remainder - (w * t) ** k / math.factorial(k)
        return np.exp(1j * phase) * remainder / w ** order
    return 0.6 * a * exp_integral(2 * np.pi, p).imag + 0.4 * b * exp_integral(6 * np.pi, r).real


def random_data(q):
    rng = np.random.default_rng(20261014 + q)
    initials = rng.uniform(-1, 1, (TRIALS, q))
    params = rng.uniform(-1, 1, (TRIALS, q + 1, 4))
    params[:, :, 2:] *= np.pi
    return initials, params


def drift(x, q):
    if q == 1:
        return 0.3 * math.sin(x[0])
    return 0.3 * math.sin(x[0]) + 0.2 * math.sin(x[1])


def physical_trial(q, nsteps, initial, eta_grid, xi, input_grid, cancel):
    """Physical nonlinear RK4; eta_grid includes half-step values."""
    h = 1.0 / nsteps
    x = np.array(initial, dtype=float)
    output = np.empty(nsteps + 1)
    physical_input = np.empty(nsteps + 1)
    output[0] = x[0] + xi[0]

    def rhs(state, applied, disturbance):
        nonlinear = drift(state, q)
        actual = applied - nonlinear if cancel else applied
        if q == 1:
            return np.array([nonlinear + actual + disturbance[0]])
        return np.array([state[1] + disturbance[0], nonlinear + actual + disturbance[1]])

    for j in range(nsteps):
        left, right = input_grid[j], input_grid[j + 1]
        middle = 0.5 * (left + right)
        physical_input[j] = left - drift(x, q) if cancel else left
        k1 = rhs(x, left, eta_grid[:, 2 * j])
        k2 = rhs(x + 0.5 * h * k1, middle, eta_grid[:, 2 * j + 1])
        k3 = rhs(x + 0.5 * h * k2, middle, eta_grid[:, 2 * j + 1])
        k4 = rhs(x + h * k3, right, eta_grid[:, 2 * j + 2])
        x += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        output[j + 1] = x[0] + xi[j + 1]
    physical_input[-1] = input_grid[-1] - drift(x, q) if cancel else input_grid[-1]
    return output, physical_input


def simulation(q, nsteps, scale, method):
    t = np.linspace(0, 1, nsteps + 1)
    t_half = np.linspace(0, 1, 2 * nsteps + 1)
    psi = t ** q
    reference = psi
    gram = 1 / (2 * q + 1)
    kappa = (2 * q + 1) / (q + 1)
    delta = scale * (EPS0 * sum(1 / math.factorial(j) for j in range(q))
                     + EPSETA * sum(1 / math.factorial(j) for j in range(1, q + 1)) + EPSXI)
    initials, params = random_data(q)
    theta = 0.0
    u = np.zeros_like(t)
    rows = []
    max_analytic_discrepancy = 0.0
    for i in range(TRIALS):
        initial = scale * EPS0 * initials[i]
        eta = np.array([scale * EPSETA * profile(t_half, params[i, j]) for j in range(q)])
        xi = scale * EPSXI * profile(t, params[i, q])
        if method == "filtered":
            u.fill(math.factorial(q) * theta)
        y, physical_input = physical_trial(q, nsteps, initial, eta, xi, u, method == "filtered")
        error = reference - y
        bound = (1 - GAMMA) ** i + (1 + kappa) * delta
        analytic_difference = None
        if method == "filtered":
            analytic = theta * psi + xi
            for j in range(q):
                analytic += initial[j] * t ** j / math.factorial(j)
                analytic += scale * EPSETA * integrated_profile(t, params[i, j], j + 1)
            analytic_difference = float(np.max(np.abs(y - analytic)))
            max_analytic_discrepancy = max(max_analytic_discrepancy, analytic_difference)
            assert analytic_difference < 1e-8, (q, nsteps, i, analytic_difference)
            assert np.max(np.abs(error)) <= bound + 1e-5, (q, i, bound, np.max(np.abs(error)))
            theta += GAMMA * np.trapezoid(psi * error, t) / gram
        else:
            u += error  # Exact book P0 law with ell=1; no hidden derivative/feedback.
        rows.append({
            "q": q, "steps": nsteps, "scale": scale, "method": method, "trial": i,
            "sup_error": float(np.max(np.abs(error))),
            "rms_error": float(np.sqrt(np.trapezoid(error ** 2, t))),
            "input_at_zero": float(physical_input[0]),
            "max_input": float(np.max(np.abs(physical_input))),
            "theorem_bound": bound if method == "filtered" else None,
            "analytic_discrepancy": analytic_difference,
        })
    summary = {
        "q": q, "steps": nsteps, "scale": scale, "method": method,
        "first_sup_error": rows[0]["sup_error"], "last_sup_error": rows[-1]["sup_error"],
        "last50_max_error": max(r["sup_error"] for r in rows[-50:]),
        "max_all_error": max(r["sup_error"] for r in rows),
        "max_input": max(r["max_input"] for r in rows),
        "last_input_at_zero": rows[-1]["input_at_zero"],
        "kappa_exact": f"{2*q+1}/{q+1}", "delta": delta,
        "asymptotic_bound": (1 + kappa) * delta if method == "filtered" else None,
        "max_analytic_discrepancy": max_analytic_discrepancy if method == "filtered" else None,
    }
    return rows, summary


def laguerre_growth():
    previous, current = 1.0, 0.0  # L_0(1), L_1(1)
    absolute_sum = 2.0
    records = []
    for n in range(2, 100001):
        following = ((2 * n - 2) * current - (n - 1) * previous) / n
        absolute_sum += abs(following - current)
        previous, current = current, following
        if n in (100, 1000, 10000, 100000):
            records.append({"horizon": n, "absolute_impulse_sum": absolute_sum})
    return records


def generating_checks():
    mp.mp.dps = 80
    rows = []
    z = mp.mpc("0.1", "0.1")
    for q in range(1, 6):
        coefficients = [mp.mpf(1)]
        for n in range(1, 120):
            coefficients.append(mp.fsum(
                (-1) ** k * mp.binomial(n - 1, k - 1) / mp.factorial(q * k)
                for k in range(1, n + 1)))
        power_sum = mp.fsum(c * z ** n for n, c in enumerate(coefficients))
        argument = -z / (1 - z)
        root = argument ** (mp.mpf(1) / q)
        roots_expression = mp.fsum(mp.exp(root * mp.exp(2j * mp.pi * j / q)) for j in range(q)) / q
        discrepancy = abs(power_sum - roots_expression)
        assert discrepancy < mp.mpf("1e-65"), (q, discrepancy)
        rows.append({"q": q, "z": "0.1+0.1i", "terms": 120,
                     "absolute_discrepancy": mp.nstr(discrepancy, 10)})
    return rows


def main():
    start = time.monotonic()
    exact = certificates()
    (OUT / "exact-certificates.json").write_text(json.dumps({"command": COMMAND, **exact}, indent=2) + "\n")
    rows, summaries = [], []
    for q in (1, 2):
        for steps in (400, 800):
            for method, scale in (("pure-P", 1.0), ("filtered", 1.0),
                                  ("filtered", 0.5), ("filtered", 0.0)):
                result, summary = simulation(q, steps, scale, method)
                rows.extend(result)
                summaries.append(summary)
    with (OUT / "simulation-trials.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    refinements = []
    for q in (1, 2):
        for method, scale in (("pure-P", 1.0), ("filtered", 1.0),
                              ("filtered", 0.5), ("filtered", 0.0)):
            coarse = [r["sup_error"] for r in rows if r["q"] == q and r["method"] == method
                      and r["scale"] == scale and r["steps"] == 400]
            fine = [r["sup_error"] for r in rows if r["q"] == q and r["method"] == method
                    and r["scale"] == scale and r["steps"] == 800]
            refinements.append({"q": q, "method": method, "scale": scale,
                                "max_trial_sup_error_difference": float(np.max(np.abs(np.array(coarse)-fine)))})
    output = {
        "command": COMMAND, "date_pt": "2026-10-14", "seed_base": 20261014,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__},
        "protocol": "work/verification_protocol.md", "evidence_label": "Empirical evidence (numerics); Certification (rational identities only)",
        "trials": TRIALS, "gamma": GAMMA,
        "epsilon0": EPS0, "epsilon_eta": EPSETA, "epsilon_xi": EPSXI,
        "generating_function_checks": generating_checks(),
        "laguerre_growth": laguerre_growth(), "summaries": summaries,
        "grid_refinements": refinements,
        "constant_initial_input_identity": "u_i(0)=-i*a for ell=1; input divergence alone is not output divergence",
        "seconds": time.monotonic() - start,
        "script_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (ROOT / "work/verify.py", ROOT / "work/exact_checks.py", ROOT / "work/requirements.txt")},
    }
    (OUT / "verification.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
