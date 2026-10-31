#!/usr/bin/env python3
"""Independent standard-library verification of the v2 PH7 band.

Reconstruct the six-rate family from the written candidate. Sparse rational
polynomials check the whole determinant and actual numerator identities in
(y,z); Bernstein coefficients prove the listed signs on the whole band.
Exact rational linear solves check actual PH row ties and transfer values at
both endpoints and an interior point, for several c. This does not reprove
any historical six-state lower bound or assert novelty.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def scalar(value):
    v = F(value)
    return {(0, 0): v} if v else {}


def add(*polys):
    result = {}
    for poly in polys:
        for degree, value in poly.items():
            result[degree] = result.get(degree, F(0)) + value
    return {degree: value for degree, value in result.items() if value}


def scale(poly, factor):
    factor = F(factor)
    return {degree: value * factor for degree, value in poly.items() if value * factor}


def sub(left, right):
    return add(left, scale(right, -1))


def mul(left, right):
    result = {}
    for (a, b), x in left.items():
        for (c, d), y in right.items():
            key = (a + c, b + d)
            result[key] = result.get(key, F(0)) + x * y
    return {degree: value for degree, value in result.items() if value}


def power(poly, exponent):
    result = scalar(1)
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def determinant(matrix):
    """Sparse recursive Laplace expansion over the actual 7 by 7 matrix."""
    def expand(row, columns):
        if row == len(matrix):
            return scalar(1)
        terms = []
        for offset, column in enumerate(columns):
            if matrix[row][column]:
                rest = columns[:offset] + columns[offset + 1:]
                terms.append(scale(mul(matrix[row][column], expand(row + 1, rest)),
                                   -1 if offset % 2 else 1))
        return add(*terms)
    return expand(0, tuple(range(len(matrix))))


def bernstein_coefficients(poly, lower, upper):
    require(all(ydegree == 0 for ydegree, _ in poly), 'sign polynomial depends on y')
    degree = max((zdegree for _, zdegree in poly), default=0)
    width = upper - lower
    power_coefficients = []
    for j in range(degree + 1):
        power_coefficients.append(sum(
            (poly.get((0, i), F(0)) * comb(i, j) * lower ** (i - j) * width ** j
             for i in range(j, degree + 1)), F(0)))
    return [sum((power_coefficients[j] * F(comb(k, j), comb(degree, j))
                 for j in range(k + 1)), F(0)) for k in range(degree + 1)]


def evaluate_z(poly, z):
    require(all(ydegree == 0 for ydegree, _ in poly), 'numeric coefficient depends on y')
    return sum((value * z ** zdegree for (_, zdegree), value in poly.items()), F(0))


def solve(matrix, rhs):
    """Exact Gauss-Jordan elimination with partial row pivoting."""
    n = len(rhs)
    a = [[F(x) for x in row] + [F(value)] for row, value in zip(matrix, rhs)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        require(pivot is not None, f'singular exact linear system in column {col}')
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [value / divisor for value in a[col]]
        for row in range(n):
            if row != col and a[row][col]:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def main():
    rates = [F(1331, 1000), F(341, 250), F(1339, 1000),
             F(33, 25), F(257, 250), F(132, 125)]
    u1, u2, u3, v1, v2, v3 = rates
    symmetric = [F(1)] + [sum((__import__('functools').reduce(
        lambda a, b: a * b, term, F(1)) for term in combinations(rates, k)), F(0))
        for k in range(1, 7)]
    A, B2, C3, e4, e5, e6 = symmetric[1:]
    h0 = B2 + 4 * A - A * A - 6
    y, z = {(1, 0): F(1)}, {(0, 1): F(1)}
    one = scalar(1)
    L = sub(scalar(B2 - 4 * A + 10), scale(z, 2))
    N = sub(scalar(4 * h0 + 4 - C3 - B2 * (4 - A)), scale(z, 4))
    pnum = N
    qnum = add(scale(N, A - 4), mul(sub(scalar(h0), scale(z, 2)), L))
    wnum = add(N, scale(L, 4 - A))
    bnum = sub(N, scale(L, u1 + u2))
    cnum = sub(sub(qnum, scale(L, u1 * u2)), scale(bnum, u1))
    phinum = sub(add(scale(L, e4), scale(wnum, C3)),
                 add(mul(add(scalar(6), scale(z, 2)), qnum),
                     mul(add(scalar(4), scale(z, 4)), pnum),
                     mul(power(add(one, z), 2), L)))
    r2num = sub(add(scale(L, e5), scale(wnum, e4)),
                add(mul(add(scalar(4), scale(z, 4)), qnum),
                    mul(power(add(one, z), 2), pnum)))
    r1num = sub(add(scale(L, e6), scale(wnum, e5)),
                mul(power(add(one, z), 2), qnum))
    r0num = scale(wnum, e6)
    d1num = sub(r2num, scale(phinum, u1 + u2 + u3))
    d2num = sub(sub(r1num, scale(phinum, u1*u2 + u1*u3 + u2*u3)),
                scale(d1num, v2 + v3))
    d3num = sub(sub(sub(r0num, scale(phinum, u1*u2*u3)),
                    scale(d1num, v2*v3)), scale(d2num, v3))
    coeffs = {'L': L, 'Lp': pnum, 'Lq': qnum, 'Lw': wnum, 'LB': bnum,
              'LC': cnum, 'Lphi': phinum, 'LD1': d1num, 'LD2': d2num, 'LD3': d3num}
    low, high = F(7, 9), F(41, 50)
    minima = {}
    for name, poly in coeffs.items():
        coefficients = bernstein_coefficients(poly, low, high)
        require(all(value > 0 for value in coefficients), f'nonpositive Bernstein coefficient: {name}')
        minima[name] = str(min(coefficients))

    # Multiply precisely rows 4 through 7 of yI-G by L, clearing every
    # rational denominator. Its determinant is L^4 det(yI-G).
    M = [[{} for _ in range(7)] for _ in range(7)]
    for i, rate in enumerate((u1, u2, u3)):
        M[i][i] = add(y, scalar(rate))
        M[i][i + 1] = scalar(-1)
    M[3][3], M[3][4] = add(mul(L, y), wnum), scale(L, -1)
    for row, rate in ((4, v1), (5, v2), (6, v3)):
        M[row][row] = mul(L, add(y, scalar(rate)))
    M[4][0], M[5][0], M[6][0] = scale(d1num, -1), scale(d2num, -1), scale(d3num, -1)
    M[4][5], M[5][6], M[6][3] = scale(L, -1), scale(L, -1), scale(phinum, -1)
    qnumerator = add(mul(L, power(y, 2)), mul(pnum, y), qnum)
    D = mul(y, power(add(power(add(y, one), 2), z), 2))
    det = determinant(M)
    require(det == mul(power(L, 3), mul(D, qnumerator)), 'full determinant identity failed')
    updated = [row[:] for row in M]
    for j, beta_num in enumerate((cnum, bnum, L)):
        updated[6][j] = add(updated[6][j], beta_num)
    require(sub(determinant(updated), det) == mul(power(L, 3), qnumerator),
            'rank-one-update numerator identity failed')

    mutant = [row[:] for row in M]
    mutant[4][0] = add(mutant[4][0], L)
    require(determinant(mutant) != det, 'D1 coefficient mutation was not detected')
    mutant_update = [row[:] for row in updated]
    mutant_update[6][1] = add(mutant_update[6][1], L)
    require(sub(determinant(mutant_update), det) != mul(power(L, 3), qnumerator),
            'initial-vector coefficient mutation was not detected')

    checks = []
    for zz in (low, (low + high) / 2, high):
        lv = evaluate_z(L, zz)
        values = {name: evaluate_z(poly, zz) / lv for name, poly in coeffs.items() if name != 'L'}
        require(lv > 0 and all(v > 0 for v in values.values()), 'physical coefficient sign failed')
        G = [[F(0) for _ in range(7)] for _ in range(7)]
        for i, rate in enumerate((u1, u2, u3, values['Lw'], v1, v2, v3)):
            G[i][i] = -rate
        for i in range(6):
            G[i][i + 1] = F(1)
        G[4][0], G[5][0], G[6][0], G[6][3] = values['LD1'], values['LD2'], values['LD3'], values['Lphi']
        beta = [values['LC'], values['LB'], F(1), F(0), F(0), F(0), F(0)]
        for c in (F(1, 2), F(1), F(2)):
            K = c * ((c + 1) ** 2 + zz) ** 2
            h = solve([[(c if i == j else 0) - G[i][j] for j in range(7)]
                       for i in range(7)], [0, 0, 0, 0, 0, 0, K])
            require(all(x > 0 for x in h), 'normalizer not positive')
            alpha = [beta[i] * h[i] for i in range(7)]
            require(all(x >= 0 for x in alpha) and sum(alpha) == 1, 'initial law invalid')
            T = [[(G[i][j] - (c if i == j else 0)) * h[j] / h[i]
                  for j in range(7)] for i in range(7)]
            require(all(T[i][j] >= 0 for i in range(7) for j in range(7) if i != j),
                    'non-Metzler generator')
            omega = [F(0)] * 7
            omega[6] = K / h[6]
            require(all(-sum(T[i]) == omega[i] for i in range(7)), 'exit row tie failed')
            for s in (F(0), F(1), F(3)):
                x = solve([[(s if i == j else 0) - T[i][j] for j in range(7)]
                           for i in range(7)], omega)
                actual = sum((alpha[i] * x[i] for i in range(7)), F(0))
                expected = K / ((s + c) * (((s + c + 1) ** 2 + zz) ** 2))
                require(actual == expected, 'actual resolvent does not match target')
            checks.append({'z': str(zz), 'c_over_d': str(c), 'laplace_points': 3})
    print(json.dumps({'result': 'PASS', 'arithmetic': 'stdlib Fraction; sparse bivariate polynomial',
                      'whole_interval': [str(low), str(high)],
                      'full_7x7_determinant_identity': 'PASS',
                      'actual_adjugate_numerator_identity': 'PASS',
                      'all_ten_bernstein_lists_positive': minima,
                      'rational_actual_representation_checks': checks,
                      'negative_controls': {'changed_feedback': 'determinant rejected',
                                            'changed_input': 'numerator rejected'},
                      'limits': 'upper construction only; finite row checks are diagnostic; PH6 lower bound is not reproved'},
                     indent=2))


if __name__ == '__main__':
    main()
