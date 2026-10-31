#!/usr/bin/env python3
"""Bounded physical check of a hidden-noise E1 endpoint example.

The randomly revealed input is E1 but not E2 by the written proof. For its
piecewise-constant adapted discretization x1 and output energies are integrated
exactly on every time cell; x2 is the exact Ito sum for that discretization.
"""
import json
import math
import random


def main():
    n, steps, seed = 10000, 96, 20261028
    rng = random.Random(seed)
    dt = 1.0 / steps
    a = 1.2
    tau_step = steps // 2
    exp1 = math.exp(-a * dt)
    int1 = (1.0 - exp1) / a
    int2 = (1.0 - exp1 * exp1) / (2.0 * a)
    max_relative_residual = max_output_over_input = 0.0
    input_norm_sum = output_norm_sum = hidden_abs_sum = 0.0
    strict_count = 0
    for _ in range(n):
        W = x1 = x2 = 0.0
        Wtau = y = alpha = None
        input_energy = output_energy = state1_energy = 0.0
        for j in range(steps):
            if j == tau_step:
                Wtau = W
                # W_tau/sqrt(tau) is standard normal; upper tail is uniform.
                upper = math.erfc(Wtau / math.sqrt(2.0 * (tau_step * dt))) / 2.0
                if upper <= 0.0:
                    raise RuntimeError("normal-tail underflow")
                y = 1.0 / math.sqrt(upper)
                alpha = y / (1.0 + y)
            w = 0.0 if j < tau_step else y * (1.0 + alpha * (W - Wtau))
            const = w / a
            delta = x1 - const
            out_at_start = w - a * x1
            input_energy += w*w*dt
            output_energy += out_at_start*out_at_start*int2
            state1_energy += const*const*dt + 2.0*const*delta*int1 + delta*delta*int2
            x1 = const + delta * exp1
            dw = rng.gauss(0.0, math.sqrt(dt))
            x2 += w * dw
            W += dw
        right = a*x1*x1 + a*a*state1_energy
        difference = input_energy-output_energy
        max_relative_residual = max(max_relative_residual,
                                    abs(difference-right)/(1.0+input_energy))
        if input_energy > 0 and output_energy < input_energy:
            strict_count += 1
        if input_energy > 0:
            max_output_over_input = max(max_output_over_input,
                                        math.sqrt(output_energy/input_energy))
        input_norm_sum += math.sqrt(input_energy)
        output_norm_sum += math.sqrt(output_energy)
        hidden_abs_sum += abs(x2)
    if strict_count != n or max_relative_residual > 1e-9:
        raise RuntimeError("physical energy identity/strictness check failed")
    print(json.dumps({
        "physical_model": "h=0,T=1,u=w; dx1=(-a*x1+w)dt, dx2=w dW; z=w-a*x1; zero state",
        "input": "Y*(1+Y/(1+Y)*(W_t-W_tau)) after tau=0.5; zero before",
        "parameters": {"a": a, "paths": n, "steps": steps, "seed": seed},
        "pathwise_identity": "||w||^2-||z||^2=a*x1(T)^2+a^2*integral x1^2",
        "max_scaled_identity_residual": max_relative_residual,
        "strict_path_count": strict_count,
        "maximum_sample_path_output_input_ratio": max_output_over_input,
        "sample_mean_input_path_norm": input_norm_sum / n,
        "sample_mean_output_path_norm": output_norm_sum / n,
        "sample_mean_abs_hidden_noise_state": hidden_abs_sum / n,
        "limits": "Piecewise-constant-input numeric test only; finite samples do not prove E2 divergence or all-input strictness."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
