"""Exact/analytic counterchecks for the mean-square referee's scope corrections.

These finite checks exercise the corrected proof obligations, not the universal
N&S theorem. No Monte Carlo or external solver is used.
"""
from fractions import Fraction as Q
import argparse
import json
import math
from pathlib import Path

import sympy as sp


def tail_controller_expected_energy(input_values, input_length=Q(3), tail_length=Q(1)):
    # The rule acts only after the counted window ends: u=1 iff its observed
    # complete past input energy is zero, otherwise u=0. Plant output is z=u.
    output = input_energies = Q(0)
    for value in input_values:  # equally likely Brownian events A and A^c
        energy = input_length * value * value
        action = Q(int(energy == 0))
        input_energies += energy / 2
        output += tail_length * action * action / 2
    return input_energies, output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    zero_input, zero_output = tail_controller_expected_energy([Q(0), Q(0)])
    assert zero_input == 0 and zero_output == 1
    rows = []
    for epsilon in (Q(1), Q(1, 10), Q(1, 100)):
        deterministic_input, deterministic_output = tail_controller_expected_energy([epsilon, epsilon])
        assert deterministic_input > 0 and deterministic_output == 0
        adapted_input, adapted_output = tail_controller_expected_energy([epsilon, Q(0)])
        gain_squared = adapted_output / adapted_input
        assert gain_squared == 1 / (3 * epsilon ** 2)
        rows.append({'epsilon': str(epsilon), 'adapted_input_energy': str(adapted_input),
                     'adapted_output_energy': str(adapted_output), 'adapted_gain_squared': str(gain_squared)})

    # A genuinely original-detectable/stabilizable plant loses detectability
    # after the feedback substitution that orthogonalizes the output cost.
    # xdot=x+u+w, z=x+u; Sigma=1; transformed xdot=u_tilde+w, z=u_tilde.
    k, s, P, gamma = sp.symbols('k s P gamma', positive=True)
    original_A, B, D0, D1 = map(sp.Integer, (1, 1, 1, 1))
    Sigma = D0 / D1
    transformed_A = original_A - B * Sigma
    transformed_D0 = D0 - D1 * Sigma
    assert transformed_A == transformed_D0 == 0
    assert original_A - 2 * D0 == -1  # original detectability injection
    closed_A = sp.simplify(original_A + B * (-(1 + k)))
    closed_output = sp.simplify(D0 + D1 * (-(1 + k)))
    assert closed_A == -k and closed_output == -k
    transfer = sp.simplify(closed_output / (s - closed_A))
    assert transfer == -k / (s + k)
    gare = sp.factor(2 * transformed_A * P + transformed_D0 ** 2 - P ** 2 + P ** 2 / gamma ** 2)
    assert sp.simplify(gare - (gamma ** -2 - 1) * P ** 2) == 0
    # For gamma>1 only P=0 solves this equation, and its mean matrix is zero,
    # not Hurwitz; but u=-(1+k)x is stable and has induced gain exactly one.
    assert gare.subs(gamma, Q(3, 2)) == -Q(5, 9) * P ** 2

    # Independent scalar stationary-delay discriminant from reviewer R-09.
    q = sp.symbols('q', positive=True)  # q=e^-h
    ch, sh = (q + 1 / q) / 2, (1 / q - q) / 2
    polynomial = sp.Poly((P * ch - sh) ** 2 + gamma ** 2 * (1 - P), P)
    discriminant = sp.factor(sp.discriminant(polynomial.as_expr(), P))
    assert sp.simplify(discriminant - gamma ** 2 * (gamma ** 2 - 2 * (1 + q ** 2))) == 0
    delay_rows = [{'h': h, 'adapted_mean_square_threshold': math.sqrt(2 * (1 + math.exp(-2 * h)))}
                  for h in (0.0, 0.5, 1.0, 2.0)]
    assert delay_rows[0]['adapted_mean_square_threshold'] == 2.0
    assert all(delay_rows[i + 1]['adapted_mean_square_threshold'] < delay_rows[i]['adapted_mean_square_threshold']
               for i in range(len(delay_rows) - 1))
    gamma_value = 1.9
    d = math.sqrt(1 - gamma_value ** 2 / 4)
    escape_time = gamma_value / d * (math.pi / 2 + math.atan(gamma_value / (2 * d)))
    assert math.sqrt(2) < gamma_value < 2 and escape_time < 18

    report = {'verified': True, 'scope': 'Exact event-locality and transformed-data counterexamples; symbolic stationary discriminant; numerical escape-time diagnostic. Not a theorem replay.',
              'zero_input_output_energy': str(zero_output), 'tail_controller': rows,
              'transformed_detectability_counterexample': {
                  'plant': 'xdot=x+u+w, z=x+u', 'Sigma': '1', 'transformed_A': str(transformed_A),
                  'transformed_D0': str(transformed_D0), 'stable_control': 'u=-(1+k)x, k>0',
                  'closed_A': str(closed_A), 'transfer': str(transfer), 'induced_gain': '1',
                  'stationary_gare': str(gare), 'only_P_at_gamma_1_5': '0, whose A_P=0 is not Hurwitz',
                  'conclusion': 'original detectability is insufficient; transformed detectability is a genuine restriction'},
              'delay_discriminant': str(discriminant), 'delay_threshold_diagnostics': delay_rows,
              'gamma_1_9_finite_escape_time': escape_time}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'verified': True, 'event_locality_cases': len(rows),
                      'transformed_detectability_counterexample': True,
                      'finite_escape_time': escape_time, 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
