#!/usr/bin/env python3
"""Bounded illustration of the event-local causal operator obstruction.

The operator is not asserted to be a physical finite-dimensional SDE. Its
reference Brownian input and a physical event-local Ito response are sampled.
"""

import json
import math
import random


def main():
    seed, paths, steps = 20261028, 24000, 100
    rng = random.Random(seed)
    dt = 1.0 / steps
    sigma = math.sqrt(dt)
    c = 1.0 / 3.0
    tau_step = steps // 2
    count_event = count_low = count_high = 0
    low_sum = high_sum = 0.0
    low_physical_sq = high_physical_sq = 0.0
    max_locality_error = max_attainment_error = 0.0
    norm_sum = local_output_sum = 0.0
    for _ in range(paths):
        W = 0.0
        ws = []
        prefix = [0.0]
        for _j in range(steps):
            ws.append(math.exp(c * W * W))
            W += rng.gauss(0.0, sigma)
            prefix.append(W)
        R = math.sqrt(sum(x * x * dt for x in ws))
        if not math.isfinite(R) or R <= 0.0:
            raise RuntimeError("invalid finite-path norm")
        p = [x / R for x in ws]
        value_v = sum(p[j] * dt for j in range(tau_step, steps))
        value_w = sum(p[j] * ws[j] * dt for j in range(steps))
        A = prefix[tau_step] >= 0.0
        value_Av = sum((p[j] if A else 0.0) * dt for j in range(tau_step, steps))
        count_event += int(A)
        max_locality_error = max(max_locality_error, abs(value_Av - (value_v if A else 0.0)))
        max_attainment_error = max(max_attainment_error, abs(value_w - R))
        norm_sum += R
        local_output_sum += value_w
        before = prefix[:tau_step + 1]
        low = max(abs(x) for x in before) < 0.55
        high = (min(prefix[15:26]) > 0.85 and abs(prefix[tau_step]) < 0.55)
        future_brownian = prefix[-1] - prefix[tau_step]
        if low:
            count_low += 1
            low_sum += value_v
            low_physical_sq += future_brownian * future_brownian
        if high:
            count_high += 1
            high_sum += value_v
            high_physical_sq += future_brownian * future_brownian
    result = {
        "seed": seed, "paths": paths, "time_steps_on_input": steps,
        "reference_input": "exp(W_t^2/3), 0<=t<=1",
        "operator": "pathwise <w*/||w*||,v> times unit output profile after input end",
        "sample_mean_input_E1_norm": norm_sum / paths,
        "sample_mean_output_E1_norm_at_reference": local_output_sum / paths,
        "max_sample_attainment_residual": max_attainment_error,
        "revealed_event": "A={W_0.5>=0}; v=1_[0.5,1]",
        "sample_P_A": count_event / paths,
        "max_pathwise_event_locality_error": max_locality_error,
        "prior_path_groups": "low: sup_[0,0.5]|W|<0.55; high: min_[0.15,0.25]W>0.85 and |W_0.5|<0.55",
        "low_group_count": count_low,
        "high_group_count": count_high,
        "sample_mean_local_output_low": low_sum / count_low if count_low else None,
        "sample_mean_local_output_high": high_sum / count_high if count_high else None,
        "physical_comparison": "actual u=v,dx=u dW,z=x, zero state; final x=W_1-W_0.5 depends on future increments only",
        "sample_physical_x2_low": low_physical_sq / count_low if count_low else None,
        "sample_physical_x2_high": high_physical_sq / count_high if count_high else None,
        "limitations": "Monte Carlo does not prove nonrealizability, E2 divergence or endpoint statements; those require the written arguments."
    }
    if max_locality_error > 1e-9 or max_attainment_error > 1e-9:
        raise RuntimeError("discrete pathwise identity failed")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
