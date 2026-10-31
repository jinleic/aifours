#!/usr/bin/env python3
"""Bounded check for an abstract causal-operator endpoint obstruction.

This does not implement a physical controller.  It samples the displayed
Brownian input, verifies path-normalization algebra and contrasts an abstract
ensemble-average output with an actual event-local Itô output.
"""

import json
import math
import random


def main():
    n, steps = 12000, 96
    dt = 1.0 / steps
    tau_step = 48
    c = 1.0 / 3.0
    rng = random.Random(20261028)
    norm_sum = phi_self_sum = phi_v_sum = phi_av_sum = 0.0
    w2_quarter_sum = physical_output_norm = 0.0
    event_count = 0
    max_norming_residual = max_actual_locality_error = 0.0
    for _ in range(n):
        brownian = 0.0
        w_values = []
        dw_values = []
        event = None
        for j in range(steps):
            w_values.append(math.exp(c * brownian * brownian))
            if j == steps // 4:
                w2_quarter_sum += w_values[-1] * w_values[-1]
            dw = rng.gauss(0.0, math.sqrt(dt))
            dw_values.append(dw)
            brownian += dw
            if j + 1 == tau_step:
                event = brownian >= 0.0
        event_count += int(event)
        norm = math.sqrt(sum(w * w * dt for w in w_values))
        if not math.isfinite(norm) or norm == 0.0:
            raise RuntimeError("invalid finite-path input norm")
        direction = [w / norm for w in w_values]
        phi_self = sum(p * w * dt for p, w in zip(direction, w_values))
        max_norming_residual = max(max_norming_residual, abs(phi_self - norm))
        phi_v_path = sum(direction[j] * dt for j in range(tau_step, steps))
        norm_sum += norm
        phi_self_sum += phi_self
        phi_v_sum += phi_v_path
        if event:
            phi_av_sum += phi_v_path
        x = x_v = x_av = out_energy = 0.0
        for j in range(steps):
            x += w_values[j] * dw_values[j]
            if j >= tau_step:
                x_v += dw_values[j]
                x_av += dw_values[j] if event else 0.0
            max_actual_locality_error = max(max_actual_locality_error,
                                             abs(x_av - (x_v if event else 0.0)))
            out_energy += x * x * dt
        physical_output_norm += math.sqrt(out_energy)

    phi_v = phi_v_sum / n
    phi_av = phi_av_sum / n
    p_event = event_count / n
    # The abstract output is constant phi_av on every path; locality would
    # require event*phi_v. This is an ensemble-output contrast, not an SDE.
    estimated_nonlocal_gap = (p_event * abs(phi_av - phi_v)
                              + (1.0 - p_event) * abs(phi_av))
    result = {
        "seed": 20261028,
        "paths": n,
        "steps": steps,
        "input": "w_t=exp(W_t^2/3), 0<=t<=1; h>0 only for abstract output interval",
        "sample_mean_E1_input_norm": norm_sum / n,
        "sample_mean_norming_functional_on_w": phi_self_sum / n,
        "max_pathwise_norming_residual": max_norming_residual,
        "sample_w2_at_t_quarter": w2_quarter_sum / n,
        "exact_w2_mean_at_t_quarter": math.sqrt(1.5),
        "exact_E2_divergence_threshold_t": 0.75,
        "sample_event_probability": p_event,
        "abstract_phi_v": phi_v,
        "abstract_phi_1A_v": phi_av,
        "estimated_abstract_event_locality_gap": estimated_nonlocal_gap,
        "physical_model": "actual h=0,x0=0,u=w,dx=u dW,z=x",
        "sample_physical_output_path_norm": physical_output_norm / n,
        "max_actual_sde_slice_output_difference": max_actual_locality_error,
        "limitations": "Abstract ensemble operator is NOT a realizable original SDE/controller. Monte Carlo proves neither divergence nor strict endpoint transfer."
    }
    if max_norming_residual > 1e-9 or max_actual_locality_error > 1e-9:
        raise RuntimeError("discrete algebra/locality check failed")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
