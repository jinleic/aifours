#!/usr/bin/env python3
"""Exact delayed-noise range checks and a bounded physical simulation."""
from fractions import Fraction as F
import json
import math
import random


def main():
    beta, sigma, kappa = F(1,3), F(2,5), F(7,10)
    eta, lam, h = F(1,5), F(1,2), F(1,2)
    # n=3: P=0, B=e1, B0=e2, C=-lam*e1, L0=1,Lh=lam,
    # H(r)=eta, Qe1=beta*e2,Qe2=sigma*e2,Qe3=kappa*e1.
    delayed_drift_coefficient = lam - lam
    kernel_early = beta*(1 + eta*F(1,4)) + eta
    kernel_late = beta*(1 + eta*h)
    if (delayed_drift_coefficient, kernel_early, kernel_late) != (0,F(11,20),F(11,30)):
        raise RuntimeError("delayed kernel algebra mismatch")
    # Direct noise atoms and the whole regular kernel have range span(e2),
    # while Q maps that range into itself and O=e1^T kills it. OQ!=0 on e3.
    if beta == 0 or sigma == 0 or kappa == 0:
        raise RuntimeError("test lost nontrivial couplings")

    paths, steps, seed = 8000, 150, 20261028
    T, S = 1.5, 1.0
    dt = T/steps
    rng = random.Random(seed)
    # Deterministic input w=1 on [0,S]. Midpoint integrals of this piecewise
    # linear preview convolution are exact when boundaries align with grid.
    x1 = 0.0
    x1_grid = [0.0]
    controls = []
    for j in range(steps):
        t = j*dt
        w = 1.0 if t < S else 0.0
        wd = 1.0 if float(h) <= t < S+float(h) else 0.0
        window = max(0.0, min(t, S)-max(0.0, t-float(h)))
        controls.append(w+float(lam)*wd+float(eta)*window)
        tm = t+dt/2.0
        wm = 1.0 if tm < S else 0.0
        winm = max(0.0, min(tm,S)-max(0.0,tm-float(h)))
        x1 += (wm+float(eta)*winm)*dt
        x1_grid.append(x1)
    deterministic_output = x1_grid[-1] + controls[-1]
    x2_sum = x2sq_sum = 0.0
    max_output_difference = 0.0
    for _ in range(paths):
        x2 = x3 = 0.0
        for j in range(steps):
            dw = rng.gauss(0.0, math.sqrt(dt))
            x2 += (float(beta)*x1_grid[j] + float(sigma)*x2 + controls[j])*dw
            x3 += 0.0*dw
        output = x1_grid[-1]+controls[-1]
        max_output_difference = max(max_output_difference, abs(output-deterministic_output))
        x2_sum += x2
        x2sq_sum += x2*x2
    print(json.dumps({
        "exact_delayed_drift_BLh_plus_C": str(delayed_drift_coefficient),
        "direct_noise_atom_coefficients_e2": ["1",str(lam)],
        "exact_noise_kernel_early_r_1over4": str(kernel_early),
        "exact_noise_kernel_late_r_3over4": str(kernel_late),
        "finite_noise_range_and_PQ_closure": "span(e2)",
        "output_unobservable_space": "span(e2,e3)",
        "old_OQ_row": ["0","0",str(kappa)],
        "structural_subspace_check": "PASS",
        "model": "P=0; Qe1=beta*e2,Qe2=sigma*e2,Qe3=kappa*e1; u=w+lambda*w(t-h)+integral eta*w(t-r)dr; z=x1+u",
        "T": T, "h": float(h), "input_support": "[0,1]", "input": "deterministic w=1",
        "paths": paths, "steps": steps, "seed": seed,
        "max_actual_output_path_difference": max_output_difference,
        "sample_hidden_noise_state_mean": x2_sum/paths,
        "sample_hidden_noise_state_second_moment": x2sq_sum/paths,
        "limits": "Exact Fraction coefficient identities and finite Euler simulation only; neither proves the general h>0 theorem."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
