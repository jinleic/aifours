#!/usr/bin/env python3
"""Bounded actual-SDE check of the L2 adjoint endpoint normal equation.

The finite grid checks a stochastic perturbation of a known deterministic
Volterra attainer. It is not evidence that an E1-only attainer exists.
"""
import json
import math
import random


def main():
    n, steps, seed = 10000, 120, 20261028
    dt = 1.0 / steps
    k = math.pi / 2.0
    gamma = 1.0 / k
    u_norm = math.sqrt(0.5)
    p = [math.sin(k * j * dt) / u_norm for j in range(steps + 1)]
    q_true = [gamma * math.cos(k * j * dt) / u_norm for j in range(steps)]
    q_discrete = [0.0] * steps
    running = 0.0
    for j in range(steps - 1, -1, -1):
        running += p[j + 1] * dt
        q_discrete[j] = running
    rng = random.Random(seed)
    lhs_sum = rhs_grid_sum = rhs_cont_sum = state2_sq_sum = 0.0
    max_grid_fubini_error = 0.0
    for _ in range(n):
        W = x1 = x2 = lhs = rhs_grid = rhs_cont = 0.0
        for j in range(steps):
            v = W * W
            dw = rng.gauss(0.0, math.sqrt(dt))
            x1 += v * dt
            x2 += v * dw
            lhs += p[j + 1] * x1 * dt
            rhs_grid += q_discrete[j] * v * dt
            rhs_cont += q_true[j] * v * dt
            W += dw
        lhs_sum += lhs
        rhs_grid_sum += rhs_grid
        rhs_cont_sum += rhs_cont
        state2_sq_sum += x2 * x2
        max_grid_fubini_error = max(max_grid_fubini_error, abs(lhs-rhs_grid))
    # E[W_s^2]=s and integral_0^1 s*cos(k*s) ds
    exact_mean = gamma / u_norm * (math.sin(k) / k + (math.cos(k)-1) / (k*k))
    result = {
        "model": "h=0,T=1,u=v,dx1=v dt,dx2=v dW,z=x1,zero state",
        "endpoint_base": "w=cos(pi*t/2), gamma=2/pi, normalized u=w/sqrt(1/2)",
        "test_variation": "v_t=W_t^2; E integral v_t^2 dt=1",
        "theoretical_continuous_mean_pairing": exact_mean,
        "sample_forward_pairing": lhs_sum / n,
        "sample_discrete_adjoint_pairing": rhs_grid_sum / n,
        "sample_continuous_adjoint_pairing": rhs_cont_sum / n,
        "max_pathwise_discrete_fubini_residual": max_grid_fubini_error,
        "max_grid_vs_continuous_adjoint_coefficient_error": max(abs(a-b) for a,b in zip(q_discrete,q_true)),
        "sample_hidden_noisy_state_second_moment": state2_sq_sum / n,
        "exact_hidden_noisy_state_second_moment": 1.0,
        "paths": n, "steps": steps, "seed": seed,
        "limits": "Finite quadrature/Monte Carlo; baseline is E2-attaining and is not a strict-E2 endpoint counterexample."
    }
    if max_grid_fubini_error > 1e-9:
        raise RuntimeError("discrete forward/adjoint identity failed")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
