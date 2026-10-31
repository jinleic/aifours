#!/usr/bin/env python3
"""Bounded check of a revealed-event slice for the actual scalar Ito example.

No scientific claim is decided solely by this script. It checks the displayed
moment identities symbolically with integer/rational polynomial arithmetic and
runs a seeded finite Euler/Itô-sum experiment on the stated physical equation.
"""

from fractions import Fraction
from math import erfc, isfinite, log, sqrt
import json
import random


def mul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            k = tuple(i + j for i, j in zip(a, b))
            out[k] = out.get(k, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def gaussian_mean(p):
    """E[B_t^k]=(k-1)!! t^(k/2) for even k; input keys (a,t,B)."""
    out = {}
    for (a_power, t_power, b_power), coefficient in p.items():
        if b_power % 2:
            continue
        moment = 1
        for odd in range(1, b_power, 2):
            moment *= odd
        key = (a_power, t_power + b_power // 2)
        out[key] = out.get(key, Fraction(0)) + coefficient * moment
    return {k: v for k, v in out.items() if v}


def integrate_to_length(p):
    return {(a_power, t_power + 1): c / (t_power + 1)
            for (a_power, t_power), c in p.items()}


def exact_moments():
    # Input divided by Y: 1+a B_t. State divided by Y:
    # B_t + a/2*(B_t^2-t); exponent order is (a,t,B).
    w = {(0, 0, 0): Fraction(1), (1, 0, 1): Fraction(1)}
    x = {(0, 0, 1): Fraction(1), (1, 0, 2): Fraction(1, 2),
         (1, 1, 0): Fraction(-1, 2)}
    got_w = integrate_to_length(gaussian_mean(mul(w, w)))
    got_x = integrate_to_length(gaussian_mean(mul(x, x)))
    want_w = {(0, 1): Fraction(1), (2, 2): Fraction(1, 2)}
    want_x = {(0, 2): Fraction(1, 2), (2, 3): Fraction(1, 6)}
    if got_w != want_w or got_x != want_x:
        raise RuntimeError(f"symbolic mismatch: input={got_w}, output={got_x}")
    return {"input_conditional_energy_over_Y2": "L + a^2 L^2/2",
            "output_conditional_energy_over_Y2": "L^2/2 + a^2 L^3/6",
            "independent_exact_gaussian_polynomial_check": "PASS"}


def experiment(n=12000, steps=64, seed=20261028):
    """t0=1, T=2, h=0, dx=w dW, z=x; A={Y<=3} in F_t0."""
    rng = random.Random(seed)
    dt = 1.0 / steps
    root_dt = sqrt(dt)
    cut = 3.0
    total_y = total_input_norm = total_output_norm = 0.0
    total_y2_cut = total_input_energy_cut = 0.0
    selected = 0
    max_slice_error = max_ito_identity_error = 0.0
    for _ in range(n):
        z0 = rng.gauss(0.0, 1.0)  # W(t0), t0=1
        p = erfc(z0 / sqrt(2.0)) / 2.0  # Uniform(0,1) marginal
        if p <= 0.0:
            raise RuntimeError("finite-precision normal tail underflow")
        y = 1.0 / sqrt(p)
        a = y / (1.0 + y)
        event = y <= cut
        selected += int(event)
        b = qv = x = x_slice = en_w = en_x = 0.0
        for _step in range(steps):
            dw = rng.gauss(0.0, root_dt)
            w = y * (1.0 + a * b)
            en_w += w * w * dt
            x += w * dw
            x_slice += (w if event else 0.0) * dw
            b += dw
            qv += dw * dw
            independent_closed_form = y * (b + a * (b * b - qv) / 2.0)
            max_ito_identity_error = max(max_ito_identity_error,
                                         abs(x - independent_closed_form))
            max_slice_error = max(max_slice_error, abs(x_slice - (x if event else 0.0)))
            en_x += x * x * dt
        if not all(isfinite(v) for v in (y, en_w, en_x)):
            raise RuntimeError("nonfinite simulation value")
        total_y += y
        total_input_norm += sqrt(en_w)
        total_output_norm += sqrt(en_x)
        if event:
            total_y2_cut += y * y
            total_input_energy_cut += en_w
    return {
        "seed": seed, "paths": n, "steps_per_unit_interval": steps,
        "physical_model": "h=0; t0=1,T=2; x0=0; u=w; dx=u dW; z=x",
        "disturbance": "w=0 before t0; Y*(1+Y/(1+Y)*(W_t-W_t0)) after t0",
        "slice": "A={Y<=3} is F_t0 measurable; same u=w and same Brownian path",
        "sample_P_A": selected / n, "exact_P_A": 1.0 - 1.0 / cut**2,
        "sample_E_Y": total_y / n, "exact_E_Y": 2.0,
        "sample_E_input_path_norm": total_input_norm / n,
        "sample_E_output_path_norm": total_output_norm / n,
        "sample_E_Y2_indicator_A": total_y2_cut / n,
        "exact_E_Y2_indicator_A": 2.0 * log(cut),
        "sample_E_slice_input_energy": total_input_energy_cut / n,
        "analytic_slice_energy_upper": 1.5 * 2.0 * log(cut),
        "max_pathwise_slice_output_difference": max_slice_error,
        "max_discrete_ito_identity_absolute_error": max_ito_identity_error,
        "warning": "Finite simulation is not a proof of endpoint attainment or infinite second moment."
    }


if __name__ == "__main__":
    print(json.dumps({"exact_symbolic": exact_moments(), "bounded_experiment": experiment()},
                     indent=2, sort_keys=True))
