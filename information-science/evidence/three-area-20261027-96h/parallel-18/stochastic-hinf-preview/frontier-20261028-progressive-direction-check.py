#!/usr/bin/env python3
"""Finite simulation for scalar linear-SDE pathwise Cauchy saturation."""
import json
import math
import random


def main():
    n, steps, seed = 10000, 200, 20261028
    T, sigma = 1.0, 0.7
    dt = T/steps
    rng = random.Random(seed)
    energy_sum = terminal_sum = euler_error_sum = 0.0
    max_saturation_residual = 0.0
    for _ in range(n):
        W = x_euler = energy = 0.0
        for j in range(steps):
            t = j*dt
            phi = math.exp(sigma*W - 0.5*sigma*sigma*t)
            w = 1.0/phi
            energy += w*w*dt
            dw = rng.gauss(0.0,math.sqrt(dt))
            x_euler += w*dt + sigma*x_euler*dw
            W += dw
        phi_T = math.exp(sigma*W - 0.5*sigma*sigma*T)
        x_factor = phi_T*energy
        pathwise_bound = phi_T*math.sqrt(energy)*math.sqrt(energy)
        max_saturation_residual=max(max_saturation_residual,abs(x_factor-pathwise_bound))
        energy_sum += energy
        terminal_sum += abs(x_factor)
        euler_error_sum += abs(x_euler-x_factor)
    exponent = 3.0*sigma*sigma
    exact_energy = (math.exp(exponent*T)-1.0)/exponent
    result={
        "physical_model":"h=0,x0=0,u=0,dx=w dt+sigma*x dW,z=x",
        "progressive_input":"w=exp(-sigma*W_t+sigma^2*t/2), not an E1-only input",
        "paths":n,"steps":steps,"seed":seed,"sigma":sigma,"T":T,
        "sample_expected_input_energy":energy_sum/n,
        "exact_expected_input_energy":exact_energy,
        "sample_mean_abs_terminal_state_integrating_factor":terminal_sum/n,
        "sample_mean_abs_euler_vs_factor_difference":euler_error_sum/n,
        "max_discrete_pathwise_Cauchy_saturation_residual":max_saturation_residual,
        "limits":"Finite left-point quadrature and Euler/Monte Carlo; no original literal gain, endpoint maximizer or proof of universal transfer is inferred."
    }
    if max_saturation_residual>1e-8:
        raise RuntimeError("sample saturation identity failed")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
