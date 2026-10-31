#!/usr/bin/env python3
"""Exact symbolic W4 output via direct tensor-product matrix-unit action.

Author-owned control, not independent scientific verification. Polynomials use
ascending rational coefficients in t. No file/network/subprocess access.
"""
from fractions import Fraction as F
from itertools import product
from time import monotonic
import json
import sys

START = monotonic()


def need(condition, name):
    if monotonic() - START > 50:
        raise TimeoutError('cooperative deadline')
    if not condition:
        raise ValueError(name)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        out[i] += v
    for i, v in enumerate(q):
        out[i] += v
    return trim(out)


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def scale(p, c):
    return trim([c*x for x in p])


def power(p, n):
    out = (F(1),)
    for _ in range(n):
        out = mul(out, p)
    return out


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mscale(a, c):
    return [[c*x for x in row] for row in a]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(n):
    return [[0] * n for _ in range(n)]


def main():
    a, b, t = (F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2)), (F(0), F(1))
    z = (F(0),)
    output = [[z for _ in range(16)] for _ in range(16)]
    basis = (1, 2, 4, 8)
    for i, j in product(basis, repeat=2):
        options = []
        for bit in range(4):
            left, right = (i >> bit) & 1, (j >> bit) & 1
            if left == right == 0:
                options.append(((0, 0, a), (1, 1, b)))
            elif left == right == 1:
                options.append(((0, 0, b), (1, 1, a)))
            else:
                options.append(((left, right, t),))
        for choices in product(*options):
            row = sum(x << bit for bit, (x, _, _) in enumerate(choices))
            col = sum(y << bit for bit, (_, y, _) in enumerate(choices))
            term = (F(1, 4),)
            for _, _, factor in choices:
                term = mul(term, factor)
            output[row][col] = add(output[row][col], term)
    nchecks = 0
    for row, col in product(range(16), repeat=2):
        k, ell = row.bit_count(), col.bit_count()
        expected = z
        if row == col:
            if k == 0:
                expected = mul(power(a, 3), b)
            elif k == 4:
                expected = mul(a, power(b, 3))
            else:
                expected = scale(add(scale(mul(power(a, 5-k), power(b, k-1)), k),
                                     scale(mul(power(a, 3-k), power(b, k+1)), 4-k)), F(1, 4))
        elif k == ell and 1 <= k <= 3 and (row ^ col).bit_count() == 2:
            expected = scale(mul(power(t, 2), mul(power(a, 3-k), power(b, k-1))), F(1, 4))
        need(output[row][col] == expected, 'actual physical block identity')
        nchecks += 1
    need(nchecks == 256, 'all matrix entries')
    need(sum((output[i][i][0] for i in range(16)), F(0)) == 1, 'constant trace')
    for degree in range(1, 5):
        need(sum((output[i][i][degree] if degree < len(output[i][i]) else F(0)
                  for i in range(16)), F(0)) == 0, 'higher trace coefficients')

    block1 = [i for i in range(16) if i.bit_count() == 1]
    block2 = [i for i in range(16) if i.bit_count() == 2]
    A1 = [[int(x != y) for y in block1] for x in block1]
    A2 = [[int((x ^ y).bit_count() == 2) for y in block2] for x in block2]
    need(mm(A1, A1) == madd(mscale(A1, 2), mscale(eye(4), 3)), 'J(4,1) spectrum polynomial')
    need(mm(mm(A2, madd(A2, mscale(eye(6), -4))),
            madd(A2, mscale(eye(6), 2))) == zero(6), 'J(4,2) spectrum polynomial')
    need(sum(A2[i][i] for i in range(6)) == 0, 'J(4,2) trace')
    need(sum(mm(A2, A2)[i][i] for i in range(6)) == 24, 'J(4,2) trace square')
    # Distinct roots 4,0,-2 and these traces force multiplicities 1,3,2.

    controls = []
    wrong_t = scale(mul(t, power(a, 2)), F(1, 4))
    need(output[1][2] != wrong_t, 'mutation missing one coherence t')
    controls.append('missing_one_coherence_t')
    wrong_spectators = scale(mul(power(t, 2), mul(a, b)), F(1, 4))
    need(output[1][2] != wrong_spectators, 'mutation wrong spectator probability')
    controls.append('wrong_spectator_weight')
    need(output[1][2] != scale(output[1][2], -1), 'mutation flipped complex coherence sign')
    controls.append('flipped_coherence_sign')
    mutant = [row[:] for row in A2]
    mutant[0][1] = mutant[1][0] = 1 - mutant[0][1]
    need(mm(mm(mutant, madd(mutant, mscale(eye(6), -4))),
            madd(mutant, mscale(eye(6), 2))) != zero(6), 'mutation removed/added Johnson edge')
    controls.append('changed_johnson_edge')
    print(json.dumps({'status': 'PASS_EXACT_PHYSICAL_W4_BLOCKS',
                      'matrix_entries_checked_as_polynomials': nchecks,
                      'J41_spectrum': {'3': 1, '-1': 3},
                      'J42_spectrum': {'4': 1, '0': 3, '-2': 2},
                      'intended_negative_controls': controls,
                      'elapsed_seconds': monotonic()-START,
                      'scope': 'Actual W4 channel polynomial block identity, t in [0,1]. Not arbitrary inputs, independent proof review, or novelty.'},
                     sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(json.dumps({'status': 'ERROR_OR_FAIL', 'type': type(exc).__name__, 'reason': str(exc)}))
        sys.exit(1)
