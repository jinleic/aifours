#!/usr/bin/env python3
"""Exact rational finite checks of the one-uniform candidate and channel algebra.

Checks only the named Pauli basis and the displayed GHZ/complex-projector pair;
this is not a proof over all states, projectors, or parameters.
"""

import itertools
import json
import math
from fractions import Fraction as F

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IMAG = (F(0), F(1))


def z(real=0, imag=0):
    return (F(real), F(imag))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def scale(x, q):
    return (x[0] * q, x[1] * q)


def conj(x):
    return (x[0], -x[1])


def zero(n):
    return [[ZERO for _ in range(n)] for _ in range(n)]


def add_matrix(a, b):
    return [[add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale_matrix(a, q):
    return [[scale(x, q) for x in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def adjoint(a):
    return [[conj(x) for x in row] for row in transpose(a)]


def matmul(a, b):
    n = len(a)
    out = zero(n)
    for i in range(n):
        for k in range(n):
            if a[i][k] == ZERO:
                continue
            for j in range(n):
                if b[k][j] != ZERO:
                    out[i][j] = add(out[i][j], mul(a[i][k], b[k][j]))
    return out


def trace(a):
    result = ZERO
    for i in range(len(a)):
        result = add(result, a[i][i])
    return result


def one_erasure(a, site):
    bit = 1 << (3 - site)
    out = zero(16)
    for i in range(16):
        for j in range(16):
            if bool(i & bit) == bool(j & bit):
                out[i][j] = scale(add(a[i & ~bit][j & ~bit], a[i | bit][j | bit]), F(1, 2))
    return out


def layers(a):
    output = []
    for m in range(5):
        total = zero(16)
        for subset in itertools.combinations(range(4), m):
            current = a
            for site in subset:
                current = one_erasure(current, site)
            total = add_matrix(total, current)
        output.append(total)
    return output


def channel(a, p):
    out = a
    for site in range(4):
        out = add_matrix(scale_matrix(out, 1 - p), scale_matrix(one_erasure(out, site), p))
    return out


def global_spinflip(a):
    out = zero(16)
    for i in range(16):
        for j in range(16):
            sign = (-1) ** (i.bit_count() + j.bit_count())
            out[i][j] = scale(a[15 - j][15 - i], sign)
    return out


def local_marginal(a, site):
    bit = 1 << (3 - site)
    out = zero(2)
    for i in range(2):
        for j in range(2):
            for other in range(16):
                if other & bit:
                    continue
                out[i][j] = add(out[i][j], a[other | (i * bit)][other | (j * bit)])
    return out


def fraction_string(q):
    return str(q)


def main():
    I = [[ONE, ZERO], [ZERO, ONE]]
    X = [[ZERO, ONE], [ONE, ZERO]]
    Y = [[ZERO, z(0, -1)], [IMAG, ZERO]]
    Z = [[ONE, ZERO], [ZERO, z(-1)]]
    for pauli, sign in ((I, 1), (X, -1), (Y, -1), (Z, -1)):
        assert matmul(matmul(Y, transpose(pauli)), Y) == scale_matrix(pauli, sign)
    for choices in itertools.product(range(4), repeat=4):
        weight = sum(label != 0 for label in choices)
        from_layers = sum((-1) ** (4 - m) * 2**m * math.comb(4 - weight, m) for m in range(5) if m <= 4 - weight)
        assert from_layers == (-1) ** weight

    rho = zero(16)
    for i in (0, 15):
        for j in (0, 15):
            rho[i][j] = z(F(1, 2))
    P = zero(16)
    P[0][0] = P[15][15] = ONE
    P[3][3] = P[12][12] = z(F(1, 2))
    P[3][12] = z(0, -F(1, 2))
    P[12][3] = z(0, F(1, 2))
    assert rho == adjoint(rho) and matmul(rho, rho) == rho and trace(rho) == ONE
    assert P == adjoint(P) and matmul(P, P) == P and trace(P) == z(3)
    for site in range(4):
        assert local_marginal(rho, site) == [[z(F(1, 2)), ZERO], [ZERO, z(F(1, 2))]]

    rho_layers = layers(rho)
    for matrix in (rho, P):
        mats = layers(matrix)
        rhs = zero(16)
        for m, matrix_m in enumerate(mats):
            rhs = add_matrix(rhs, scale_matrix(matrix_m, (-1) ** (4 - m) * 2**m))
        assert rhs == global_spinflip(matrix)
    exact_t = [trace(matmul(P, layer)) for layer in rho_layers]
    assert exact_t == [z(1), z(2), z(F(7, 4)), z(F(3, 4)), z(F(3, 16))]

    rows = []
    for p in (F(0), F(1, 2), F(1), F(4, 3)):
        output = channel(rho, p)
        by_layers = zero(16)
        for m, matrix_m in enumerate(rho_layers):
            by_layers = add_matrix(by_layers, scale_matrix(matrix_m, (1 - p) ** (4 - m) * p**m))
        assert output == by_layers
        q = abs(1 - p)
        a, b = (1 + q) / 2, (1 - q) / 2
        d0 = (a**4 + b**4) / 2
        d1 = (a**3 * b + a * b**3) / 2
        d2 = a**2 * b**2
        for i in range(16):
            for j in range(16):
                if i == j:
                    h = i.bit_count()
                    expected = d0 if h in (0, 4) else d1 if h in (1, 3) else d2
                    assert output[i][j] == z(expected)
                elif (i, j) in ((0, 15), (15, 0)):
                    assert output[i][j] == z(q**4 / 2)
                else:
                    assert output[i][j] == ZERO
        assert d0 + q**4 / 2 >= d0 - q**4 / 2 >= d1 >= d2
        ghz_top3 = 2 * d0 + d1
        reference = a**4 + 2 * a**3 * b
        s = min(p, 2 - p)
        claimed_gap = s**2 * (1 - s) / 2
        assert reference - ghz_top3 == q * (1 - q) * (q**2 + q + 4) / 8
        assert reference - ghz_top3 >= claimed_gap
        value = trace(matmul(P, output))
        assert value[1] == 0 and value[0] <= ghz_top3
        rows.append({"p": fraction_string(p), "exact_same_projector_trace": fraction_string(value[0]), "exact_original_channel_top3": fraction_string(ghz_top3), "exact_reference_top3": fraction_string(reference), "exact_spectral_gap": fraction_string(reference - ghz_top3), "proved_lower_gap": fraction_string(claimed_gap)})
    print(json.dumps({"scope": "exact finite checks, not universal proof or independent review", "one_qubit_pauli_basis_checked": 4, "four_qubit_pauli_strings_layer_identity_checked": 256, "complex_matrix_operator_identity_checks": 2, "physical_state": "GHZ density; all four marginals exactly I/2", "physical_projector": "rank 3; range |0000>, |1111>, (|0011>+i|1100>)/sqrt(2)", "exact_t0_to_t4": [fraction_string(x[0]) for x in exact_t], "rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
