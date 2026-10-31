#!/usr/bin/env python3
"""Bounded physical check of the endpoint variation/angle identity.

Model: h=0, T=1, x_1'=w, dx_2=w dW, u=w, z=x_1.  The deterministic
base input cos(pi*t/2) attains the pathwise Volterra bound 2/pi.  The test
uses a revealed event A={W_tau>0} and changes only the input tail on A.
"""

import json
import math
import random


def main():
    T = 1.0
    k = math.pi / 2.0
    tau = 0.4
    g = 1.0 / k
    sin_tau = math.sin(k * tau)
    tail_energy = (T - tau) / 2.0 - math.sin(2.0 * k * tau) / (4.0 * k)
    input_energy = T / 2.0
    output_energy = T / (2.0 * k * k)
    output_inner = tail_energy / (k * k)
    tail_output_energy = ((T - tau) * (0.5 + sin_tau * sin_tau)
                          - 3.0 * math.sin(2.0 * k * tau) / (4.0 * k)) / (k * k)
    if min(tail_energy, input_energy, output_energy, tail_output_energy) <= 0:
        raise RuntimeError("inconsistent analytic energy")

    input_norm = math.sqrt(input_energy)
    output_norm = math.sqrt(output_energy)
    tail_norm = math.sqrt(tail_energy)
    tail_output_norm = math.sqrt(tail_output_energy)
    input_direction = tail_energy / input_norm
    output_direction = output_inner / output_norm
    a = tail_norm - input_direction
    b = tail_output_norm - output_direction
    deficit = g * tail_norm - tail_output_norm

    def expected_ratio(eps):
        # P(A)=1/2; original deterministic base plus revealed tail on A.
        in_active = math.sqrt(input_energy + (2.0 * eps + eps * eps) * tail_energy)
        out_active = math.sqrt(output_energy + 2.0 * eps * output_inner
                               + eps * eps * tail_output_energy)
        return (0.5 * output_norm + 0.5 * out_active) / (0.5 * input_norm + 0.5 * in_active)

    n = 12000
    steps = 100
    tau_step = 40
    dt = T / steps
    rng = random.Random(20261028)
    count_a = 0
    mean_x2 = 0.0
    mean_x2_sq = 0.0
    for _ in range(n):
        brownian = 0.0
        x2 = 0.0
        w_at_tau = None
        for j in range(steps):
            dw = rng.gauss(0.0, math.sqrt(dt))
            x2 += math.cos(k * (j * dt)) * dw
            brownian += dw
            if j + 1 == tau_step:
                w_at_tau = brownian
        count_a += int(w_at_tau > 0.0)
        mean_x2 += x2
        mean_x2_sq += x2 * x2

    eps = 1.0e-4
    result = {
        "model": "T=1,h=0,u=w; dx1=w dt, dx2=w dW; z=x1; x0=0",
        "base": "w=cos(pi*t/2), gamma=2/pi; actual pathwise Volterra extremizer",
        "variation": "alpha=1_{W_tau>0}*1_{t>=tau}, tau=0.4",
        "gamma": g,
        "normal_identity_residual": g * input_direction - output_direction,
        "input_angle_A": a,
        "output_angle_B": b,
        "tail_deficit": deficit,
        "angle_budget_residual": deficit - (g * a - b),
        "finite_difference_ratio_derivative": (expected_ratio(eps) - expected_ratio(-eps)) / (2.0 * eps),
        "ratio_at_base": expected_ratio(0.0),
        "ratio_at_positive_perturbation": expected_ratio(eps),
        "ratio_at_negative_perturbation": expected_ratio(-eps),
        "brownian_seed": 20261028,
        "brownian_paths": n,
        "brownian_steps": steps,
        "sample_probability_A": count_a / n,
        "exact_probability_A": 0.5,
        "sample_mean_hidden_noisy_state_x2": mean_x2 / n,
        "sample_second_moment_hidden_noisy_state_x2": mean_x2_sq / n,
        "exact_continuous_second_moment_x2": 0.5,
        "limitations": "Finite floating-point/Monte Carlo check; not a proof of universal endpoint transfer."
    }
    if abs(result["normal_identity_residual"]) > 1e-12:
        raise RuntimeError("normal identity check failed")
    if abs(result["angle_budget_residual"]) > 1e-12:
        raise RuntimeError("angle budget check failed")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
