#!/usr/bin/env python3
"""Exact three-point LP search and certificates; no floating-point arithmetic."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

SUPPORT = [F(-1), F(0), F(1)]
MASS = F(1, 3)


def convex_order(left, right):
    """Equal atom masses; calls are piecewise linear between these knots."""
    if sum(left) != sum(right):
        return False
    knots = sorted(set(left + right))
    return all(sum(max(x - k, F(0)) for x in left) <=
               sum(max(x - k, F(0)) for x in right) for k in knots)


def system(f, g):
    rows, rhs, names = [], [], []
    for i in range(3):
        rows.append([F(int(k // 3 == i)) for k in range(9)])
        rhs.append(MASS)
        names.append(f'row_mass_{i}')
    for j in range(3):
        rows.append([F(int(k % 3 == j)) for k in range(9)])
        rhs.append(MASS)
        names.append(f'col_mass_{j}')
    for i in range(3):
        rows.append([SUPPORT[k % 3] if k // 3 == i else F(0)
                     for k in range(9)])
        rhs.append(MASS * f[i])
        names.append(f'row_moment_{i}')
    for j in range(3):
        rows.append([SUPPORT[k // 3] if k % 3 == j else F(0)
                     for k in range(9)])
        rhs.append(MASS * g[j])
        names.append(f'col_moment_{j}')
    return rows, rhs, names


def solve_one_free_lp(a, b):
    """RREF over Q, then intersect all nonnegative half-lines exactly."""
    matrix = [row[:] + [value] for row, value in zip(a, b)]
    n = len(a[0])
    pivots = []
    for col in range(n):
        row = next((j for j in range(len(pivots), len(matrix))
                    if matrix[j][col]), None)
        if row is None:
            continue
        pivot_index = len(pivots)
        matrix[pivot_index], matrix[row] = matrix[row], matrix[pivot_index]
        factor = matrix[pivot_index][col]
        matrix[pivot_index] = [x / factor for x in matrix[pivot_index]]
        for j in range(len(matrix)):
            if j != pivot_index and matrix[j][col]:
                factor = matrix[j][col]
                matrix[j] = [x - factor * y for x, y in
                             zip(matrix[j], matrix[pivot_index])]
        pivots.append(col)
    if any(not any(row[:n]) and row[-1] for row in matrix):
        return {'feasible': False, 'reason': 'inconsistent_equalities'}
    free = [j for j in range(n) if j not in pivots]
    assert len(free) == 1, 'This verifier is deliberately scoped to this 3x3 family.'
    particular, direction = [F(0)] * n, [F(0)] * n
    direction[free[0]] = F(1)
    for i, col in enumerate(pivots):
        particular[col] = matrix[i][-1]
        direction[col] = -matrix[i][free[0]]
    lower, upper = None, None
    for p, d in zip(particular, direction):
        if d == 0:
            if p < 0:
                return {'feasible': False, 'reason': 'negative_fixed_coordinate',
                        'value': p, 'rank': len(pivots)}
        elif d > 0:
            bound = -p / d
            lower = bound if lower is None else max(lower, bound)
        else:
            bound = -p / d
            upper = bound if upper is None else min(upper, bound)
    feasible = lower is None or upper is None or lower <= upper
    result = {'feasible': feasible, 'rank': len(pivots),
              'free_coordinate': free[0], 'lower': lower, 'upper': upper}
    if feasible:
        parameter = lower if lower is not None else upper if upper is not None else F(0)
        witness = [p + parameter * d for p, d in zip(particular, direction)]
        assert all(x >= 0 for x in witness)
        assert all(sum(x * y for x, y in zip(row, witness)) == rhs
                   for row, rhs in zip(a, b))
        result['witness'] = [witness[i:i + 3] for i in (0, 3, 6)]
    return result


def main():
    search = []
    for r in sorted({F(k, 8) for k in range(9)} | {F(2, 3)}):
        f, g = [F(0), -r, r], [-r / 2, F(0), r / 2]
        a, b, names = system(f, g)
        cx1, cx2 = convex_order(f, SUPPORT), convex_order(g, SUPPORT)
        cross1 = sum(x * y for x, y in zip(SUPPORT, f)) * MASS
        cross2 = sum(x * y for x, y in zip(SUPPORT, g)) * MASS
        assert cx1 and cx2 and cross1 == cross2
        result = solve_one_free_lp(a, b)
        assert result['feasible'] == (r <= F(2, 3))
        search.append({'r': r, 'IF_convex_order': cx1, 'GD_convex_order': cx2,
                       'cross_moment': cross1, 'lp': result})

    r = F(3, 4)
    a, b, names = system([F(0), -r, r], [-r / 2, F(0), r / 2])
    indices = [names.index(name) for name in
               ('col_mass_0', 'col_moment_0', 'row_moment_1')]
    dual_a = [sum(a[i][j] for i in indices) for j in range(9)]
    dual_b = sum(b[i] for i in indices)
    expected = [F(0)] * 9
    expected[5], expected[6] = F(1), F(2)
    assert dual_a == expected and dual_b == -F(1, 24)
    robust_upper = dual_b + 2 * F(1, 32) / 3
    assert robust_upper == -F(1, 48)

    gd_upper = F(112 * 468, 3 * 128**3)
    gd_lower = F(55, 4096)
    assert gd_upper == F(273, 32768)
    assert gd_upper < gd_lower
    assert (F(34) - 36) / (F(25) - 24) == -2
    return {
        'arithmetic': 'fractions.Fraction only; no float or numerical LP solver',
        'search_family': 'uniform {-1,0,1}; f=(0,-r,r), g=(-r/2,0,r/2)',
        'search': search,
        'farkas_certificate': {'row_names': [names[i] for i in indices],
                               'multipliers': [1, 1, 1],
                               'combined_coefficients': dual_a,
                               'combined_rhs': dual_b},
        'continuous_counterexample_epsilon': F(1, 32),
        'continuous_certificate_upper': robust_upper,
        'GD_Jensen_upper': gd_upper,
        'GD_Jensen_lower': gd_lower,
        'GD_gap': gd_lower - gd_upper,
        'negative_IF_at_zero': -2,
        'limitations': ['Algebraic checks only; Fourier analytic proofs are written in proof.md.',
                       'The counterexample data are NOT claimed Fourier-realizable.',
                       'This does not classify literal-density existence for signals.'],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(main(), indent=2, default=str) + '\n'
    if args.output is not None:
        args.output.write_text(text)
    else:
        print(text, end='')
