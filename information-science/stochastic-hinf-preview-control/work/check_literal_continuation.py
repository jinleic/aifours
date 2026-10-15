"""Bounded, non-Monte-Carlo checks for literal_continuation.md.

The inequalities certifying separation use exact Fraction arithmetic only.
SciPy moment ODEs and Gaussian quadrature are separate numerical counterchecks,
not a proof of the universal input/controller quantifiers.
"""
import hashlib
import json
import math
import pathlib
import sys
from fractions import Fraction

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import roots_hermitenorm


def exact_exponential_bracket(order):
    """Taylor lower bound and geometric upper bound for exp(1)."""
    lower = sum((Fraction(1, math.factorial(k)) for k in range(order + 1)), Fraction(0))
    first_omitted = Fraction(1, math.factorial(order + 1))
    # Ratios after the first omitted term are at most 1/(order+2).
    upper = lower + first_omitted / (1 - Fraction(1, order + 2))
    return lower, upper


def moment_rhs(forcing):
    """Itô generator of dx=(-x+forcing)dt+2x dW, plus output energy."""
    def rhs(_time, state):
        mean, second, _energy = state
        return [-mean + forcing, 2 * second + 2 * forcing * mean, second]
    return rhs


def integrate(rhs, interval, initial):
    solution = solve_ivp(rhs, interval, initial, method="DOP853", rtol=5e-12, atol=1e-13)
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution.y[:, -1]


def main(output_path):
    lo, hi = exact_exponential_bracket(18)
    assert Fraction(8, 3) < lo < hi < Fraction(11, 4)
    literal_upper_squared = 2 * (hi * hi - 1) / (1 - 1 / lo) ** 2
    impulse_end_second_lower = lo * lo / 3 - 1 + 2 / (3 * hi)
    tail_energy_lower = impulse_end_second_lower * (lo ** 6 - 1) / 2
    control_operator_upper_squared = (hi ** 10 - 11) / 4
    all_controller_ms_lower_squared = tail_energy_lower / (1 + control_operator_upper_squared / 10000)
    control_noise_operator_upper_squared = Fraction(10, 3) * (hi ** 15 - 1)
    control_noise_ms_lower_squared = tail_energy_lower / (1 + control_noise_operator_upper_squared / 10**8)
    assert literal_upper_squared < 36
    assert tail_energy_lower > 324
    assert control_operator_upper_squared < 5625
    assert all_controller_ms_lower_squared > 196
    assert control_noise_ms_lower_squared > 289
    assert Fraction(168, 5) < 36  # Elementary e-bracket proof of literal feasibility.

    e = math.e
    # Independent integration in physical plant time: no input before t=1,
    # unit input during [1,2], then three units of free multiplicative evolution.
    after_zero = integrate(moment_rhs(0.0), (0.0, 1.0), [0.0, 0.0, 0.0])
    after_forcing = integrate(moment_rhs(1.0), (1.0, 2.0), after_zero)
    final = integrate(moment_rhs(0.0), (2.0, 5.0), after_forcing)
    second_closed = e * e / 3 - 1 + 2 / (3 * e)
    first_energy_closed = (e * e - 1) / 6 - 1 + 2 * (1 - 1 / e) / 3
    tail_closed = second_closed * (e ** 6 - 1) / 2
    total_closed = first_energy_closed + tail_closed
    comparisons = {
        "unit_forcing_second_moment": (float(after_forcing[1]), second_closed),
        "unit_forcing_energy": (float(after_forcing[2]), first_energy_closed),
        "full_output_energy": (float(final[2]), total_closed),
        "tail_output_energy": (float(final[2] - after_forcing[2]), tail_closed),
    }
    # Independent differential equation for integrated kernel second moment.
    kernel = integrate(lambda _t, y: [2 * y[0] + 1, y[0]], (0.0, 5.0), [0.0, 0.0])
    comparisons["control_kernel_integrated_energy"] = (float(kernel[1]), (e ** 10 - 11) / 4)
    control_noise_kernel = integrate(lambda _t, y: [3 * y[0] + 10], (0.0, 5.0), [0.0])
    comparisons["control_noise_kernel_energy_bound"] = (float(control_noise_kernel[0]), 10 * (e ** 15 - 1) / 3)
    ode_rows = []
    for name, (observed, expected) in comparisons.items():
        relative_error = abs(observed - expected) / max(1.0, abs(expected))
        assert relative_error < 2e-10, (name, observed, expected, relative_error)
        ode_rows.append({"name": name, "ode": observed, "closed_form": expected,
                         "scaled_error": relative_error})

    # A distinct numerical representation of the gated subclass: integrate its
    # lognormal multiplier under Gaussian quadrature, then form both witnesses.
    quadrature_rows = []
    for order in (32, 64):
        nodes, weights = roots_hermitenorm(order)
        weights = weights / math.sqrt(2 * math.pi)
        gain = np.exp(nodes - 0.5)
        first = float(weights @ gain)
        second = float(weights @ (gain * gain))
        literal_witness = float(weights @ (gain + 1)) / 2
        adapted_ms_witness = math.sqrt(float(weights @ ((gain + gain / e) ** 2)) /
                                       (2 * float(weights @ (1 + gain * gain / e ** 2))))
        covariance = np.array([[second, first], [first, 1.0]])
        deterministic_ms = math.sqrt(float(np.linalg.eigvalsh(covariance)[-1]) / 2)
        adapted_formula = math.sqrt((1 + e) / 2)
        deterministic_formula = math.sqrt((e + 1 + math.sqrt((e - 1) ** 2 + 4)) / 4)
        assert abs(first - 1) < 2e-13
        assert abs(second - e) < 2e-12
        assert abs(literal_witness - 1) < 2e-13
        assert abs(adapted_ms_witness - adapted_formula) < 2e-12
        assert abs(deterministic_ms - deterministic_formula) < 2e-12
        assert 1 < deterministic_ms < adapted_ms_witness
        quadrature_rows.append({"order": order, "E_G": first, "E_G_squared": second,
                                "literal_witness_gain": literal_witness,
                                "adapted_ms_witness_gain": adapted_ms_witness,
                                "deterministic_ms_eigenvalue_gain": deterministic_ms})

    proof = pathlib.Path(__file__).with_name("literal_continuation.md")
    result = {
        "status": "PASS",
        "method": "Exact rational separation certificate; independent moment ODEs and Gaussian quadrature",
        "monte_carlo_paths": 0,
        "scope": {"original_model": "finite horizon only; h=1, T=5, all adapted or deterministic disturbances",
                  "constant_plant": "dx=(-x+u+w(t-1))dt+2x dW; z=(x,100u)",
                  "controller_impossibility": "all adapted controls, including nonlinear feedback rules",
                  "subclass": "time-gated scalar theorem L3, not the constant-matrix general problem",
                  "infinite_horizon": "not asserted"},
        "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "exact_certificate": {
            "e_lower": str(lo), "e_upper": str(hi),
            "literal_gain_squared_upper": str(literal_upper_squared),
            "tail_energy_lower": str(tail_energy_lower),
            "control_map_gain_squared_upper": str(control_operator_upper_squared),
            "all_controller_mean_square_gain_squared_lower": str(all_controller_ms_lower_squared),
            "literal_gain_less_than_6": True,
            "all_controller_mean_square_gain_greater_than_14": True,
            "control_noise_map_gain_squared_upper": str(control_noise_operator_upper_squared),
            "control_noise_all_controller_ms_gain_squared_lower": str(control_noise_ms_lower_squared),
            "control_noise_all_controller_ms_gain_greater_than_17": True},
        "decimal_diagnostics_not_proof": {
            "literal_gain_upper": math.sqrt(float(literal_upper_squared)),
            "uncontrolled_tail_rms_lower": math.sqrt(float(tail_energy_lower)),
            "control_map_rms_upper": math.sqrt(float(control_operator_upper_squared)),
            "all_controller_ms_gain_lower": math.sqrt(float(all_controller_ms_lower_squared)),
            "control_noise_all_controller_ms_gain_lower": math.sqrt(float(control_noise_ms_lower_squared))},
        "independent_moment_ode_checks": ode_rows,
        "independent_gaussian_quadrature_checks": quadrature_rows,
        "limitations": "The script checks identities and strict scalar inequalities, not all stochastic laws. Universal claims rest on the written proof and independent referee."}
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], **result["decimal_diagnostics_not_proof"],
                      "max_moment_ode_scaled_error": max(row["scaled_error"] for row in ode_rows),
                      "output": str(output_path)}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_literal_continuation.py OUTPUT.json")
    main(sys.argv[1])
