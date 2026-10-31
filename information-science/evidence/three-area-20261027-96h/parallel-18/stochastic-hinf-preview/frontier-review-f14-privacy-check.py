#!/usr/bin/env python3
"""Independent bounded rational checks for f14; no claim of a full proof."""

from collections import Counter
from fractions import Fraction as F
import json


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def main():
    # Independently integrate 2*(1-u) on [0,1] and its second moment.
    mass_1d = 2 * (F(1) - F(1, 2))
    variance_1d = 2 * (F(1, 3) - F(1, 4))
    variance_2d = 2 * variance_1d
    derivative_l1 = F(2)
    if (mass_1d, variance_2d, derivative_l1) != (F(1), F(1, 3), F(2)):
        raise RuntimeError("triangular kernel check failed")

    # Check the paired-strip primitive on different rational inputs than author.
    jump = F(5, 37)
    lip = F(11, 7)
    radius = jump / (2 * lip)
    paired = jump * radius - lip * radius * radius
    tv_lower = paired / 2
    if tv_lower != jump * jump / (8 * lip):
        raise RuntimeError("paired strip check failed")

    # Synthetic square core plus a diamond: exact squared side lengths.
    a, j = F(2, 7), F(5, 3)
    vertices = [(a + j, a), (a, a + j), (-a, a + j), (-a - j, a),
                (-a - j, -a), (-a, -a - j), (a, -a - j), (a + j, -a)]
    side_sq = []
    for first, second in zip(vertices, vertices[1:] + vertices[:1]):
        side_sq.append((first[0] - second[0])**2 + (first[1] - second[1])**2)
    if Counter(side_sq) != Counter({(2 * a)**2: 4, 2 * j*j: 4}):
        raise RuntimeError("synthetic perimeter check failed")

    # Rational finite quadrature of a SYNTHETIC diamond-core staircase.
    # Every grid summand is evaluated independently at x and x+(1,0).
    b, t, x1, x2, grid = F(2, 3), F(1, 3), F(4), F(5), 20
    us = [F(2 * i + 1, grid) - 1 for i in range(grid)]
    weights = [(1 - abs(u)) * F(2, grid) for u in us]
    if sum(weights) != 1:
        raise RuntimeError("finite quadrature kernel not normalized")
    q0 = q1 = F(0)
    for u, wu in zip(us, weights):
        for v, wv in zip(us, weights):
            y1, y2 = x1 - t * u, x2 - t * v
            if y1 <= 1 or y2 <= 1:
                raise RuntimeError("synthetic far-quadrant premise failed")
            n0 = ceil_fraction(y1 + y2 - 1)
            n1 = ceil_fraction(y1 + 1 + y2 - 1)
            q0 += wu * wv * b**n0
            q1 += wu * wv * b**n1
    if q1 != b * q0:
        raise RuntimeError("finite quadrature shift identity failed")

    print(json.dumps({
        "triangular_mass_1d": str(mass_1d),
        "triangular_variance_total_2d": str(variance_2d),
        "triangular_derivative_L1_each_axis": str(derivative_l1),
        "synthetic_jump": str(jump), "synthetic_lipschitz_bound": str(lip),
        "paired_integral": str(paired), "total_variation_lower": str(tv_lower),
        "independent_pair_identity": "PASS",
        "synthetic_square_halfside": str(a), "diamond_radius": str(j),
        "polygon_side_squared_multiplicities": {str(k): v for k, v in Counter(side_sq).items()},
        "perimeter_identity": "four lengths 2a plus four lengths sqrt(2)*j: 8a+4sqrt(2)j",
        "synthetic_grid_points": grid * grid,
        "synthetic_b": str(b), "quadrature_q0_unnormalized": str(q0),
        "quadrature_shifted_q1_unnormalized": str(q1),
        "exact_quadrature_q0_over_q1": str(q0 / q1),
        "quadrature_shift_identity": "PASS",
        "limitations": "Synthetic finite quadrature is not the actual optimum, an exact continuous integral, a proof of the theorem, or novelty evidence."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
