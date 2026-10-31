#!/usr/bin/env python3
"""Check conditional curvature on one actual finite-horizon SDE.

The state and controller are real and physical, but this is a finite numerical
check of a necessary condition at a known E2 attainer, not an endpoint proof.
"""
import json
import math
import random


def main():
    k = math.pi / 2.0
    tau = 0.4
    T = 1.0
    g = 1.0 / k
    st = math.sin(k * tau)
    lt = (T - tau) / 2.0 - math.sin(2.0 * k * tau) / (4.0 * k)
    in0 = math.sqrt(T / 2.0)
    out0 = math.sqrt(T / (2.0 * k * k))
    cross = lt / (k * k)
    outtail2 = ((T - tau) * (0.5 + st * st)
                - 3.0 * math.sin(2.0 * k * tau) / (4.0 * k)) / (k * k)
    cin = (lt - (lt / in0)**2) / in0
    cout = (outtail2 - (cross / out0)**2) / out0

    def deficit(eps):
        # A={W_tau>0}; its exact probability is 1/2. The state x1 is
        # integrated exactly, while x2 is simulated independently below.
        in_active = math.sqrt(in0 * in0 + 2.0 * eps * lt + eps * eps * lt)
        out_active = math.sqrt(out0 * out0 + 2.0 * eps * cross + eps * eps * outtail2)
        return g * (0.5 * in0 + 0.5 * in_active) - (0.5 * out0 + 0.5 * out_active)

    eps = 1e-4
    second_fd = (deficit(eps) + deficit(-eps) - 2.0 * deficit(0.0)) / (eps * eps)
    expected_second = 0.5 * (g * cin - cout)
    n, steps, seed = 12000, 100, 20261028
    rng = random.Random(seed)
    event_n = 0
    x2sq = 0.0
    for _ in range(n):
        W = x2 = 0.0
        Wtau = None
        for j in range(steps):
            dw = rng.gauss(0.0, math.sqrt(T / steps))
            x2 += math.cos(k * j / steps) * dw
            W += dw
            if j + 1 == 40:
                Wtau = W
        event_n += int(Wtau > 0.0)
        x2sq += x2 * x2
    result = {
        "model": "h=0,T=1,u=w,dx1=w dt,dx2=w dW,z=x1; zero state",
        "attainer": "w=cos(pi*t/2), gamma=2/pi; endpoint attained already in E2",
        "tail": "tau=0.4; alpha=1_{W_tau>0}1_{t>=tau}",
        "conditional_input_curvature": cin,
        "conditional_output_curvature": cout,
        "conditional_gamma_input_minus_output": g * cin - cout,
        "symmetric_deficit_second_difference": second_fd,
        "analytic_expected_second_derivative": expected_second,
        "absolute_second_difference_error": abs(second_fd - expected_second),
        "sample_P_A": event_n / n, "exact_P_A": 0.5,
        "sample_E_hidden_X2_squared": x2sq / n,
        "exact_E_hidden_X2_squared": 0.5,
        "paths": n, "steps": steps, "seed": seed,
        "limits": "Finite floating-point/Monte Carlo check, not a proof of an E1-only endpoint attainer."
    }
    if cin < 0 or cout < 0 or expected_second < -1e-12:
        raise RuntimeError("curvature inequality failed in check")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
