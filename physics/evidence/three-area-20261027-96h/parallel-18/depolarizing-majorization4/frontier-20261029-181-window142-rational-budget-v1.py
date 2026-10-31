#!/usr/bin/env python3
"""Exact scalar budget of packet 180; not a checker of the universal theorem.

Standard-library Fraction arithmetic only. No author helper imports, state
search, eigenvalue calculations, file reads/writes, or floating-point values.
"""
import json
from fractions import Fraction as F


def main():
    c, r = F(1, 142), F(19, 80)
    v, s = F(4, 25), F(2, 25)
    w, b, q, o = F(204, 25), F(1, 25), F(41, 5), F(21, 5)
    g, e, d = F(199, 200), F(137, 100), F(81, 20)
    delta = 2 * r**2
    cubic = F(26, 25) * (d * (2*s)**3 / 6 + v * (2*s)**2 / 2 + w * (2*s))
    error = 3*e*r + 3*b*r**2 + 3*o**2*r**2/g
    slacks = {
        'parseval': v*v - 512*c*c,
        'D_norm': d - (4 + 6*c + 4*c*c + c**3),
        'B_norm': b - 3*v*s,
        'Q_norm': q - (w + 3*v*s),
        'off_Q_norm': o - (4 + v + 3*v*s),
        'exponential_bound': F(26, 25) - 1/(1 - 2*r*s),
        'cubic_remainder': e - cubic,
        'two_block_separations': 2 - 2*(r*v + r*r*q) - g,
        'normalized_residual': 4 - error,
        'gap_t_eta_squared_over_2000': 4 - error - F(16, 2000),
        'far_boundary': delta - 16*c,
        'far_square_root': 441 - (429 + 78*delta),
        'far_monotonicity': 1 - F(39, 20)*c,
        'weight_two_quarter_factor': 2 - 2*c*c - c**3,
        'weight_three_quarter_margin': F(15, 32)*(1-c) - F(1, 4),
        'weight_four_quarter_margin': 1 - 2*c**6 - F(1, 4),
    }
    failed = [name for name, value in slacks.items() if value <= 0]
    if failed:
        raise ArithmeticError('Nonpositive scalar proof margin: ' + ', '.join(failed))
    report = {
        'scope': 'Exact scalar constants only; not the all-variable channel proof',
        'parameter_radius': str(c),
        'tube_radius': str(r),
        'cubic_coefficient': str(cubic),
        'full_adverse_coefficient': str(error),
        'positive_slacks': {k: str(val) for k, val in slacks.items()},
        'all_displayed_scalar_margins_positive': True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
