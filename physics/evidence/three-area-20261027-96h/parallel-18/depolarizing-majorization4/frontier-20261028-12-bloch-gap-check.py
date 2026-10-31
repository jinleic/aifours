#!/usr/bin/env python3
"""Exact finite actual-channel tests of the pure-input Bloch-radius bound."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("exact_check", ROOT / "frontier-20261028-09-exact-one-uniform-check.py")
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)


def pure_from_vector(vector):
    return [[e.mul(vector[i], e.conj(vector[j])) for j in range(16)] for i in range(16)]


def kron(a, b):
    n, m = len(a), len(b)
    out = e.zero(n * m)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                for l in range(m):
                    out[i * m + k][j * m + l] = e.mul(a[i][j], b[k][l])
    return out


def direct_pauli(a, p):
    I = [[e.ONE, e.ZERO], [e.ZERO, e.ONE]]
    X = [[e.ZERO, e.ONE], [e.ONE, e.ZERO]]
    Y = [[e.ZERO, e.z(0, -1)], [e.IMAG, e.ZERO]]
    Z = [[e.ONE, e.ZERO], [e.ZERO, e.z(-1)]]
    paulis = (I, X, Y, Z)
    weights = (1 - 3 * p / 4, p / 4, p / 4, p / 4)
    assert all(weight >= 0 for weight in weights) and sum(weights) == 1
    result = e.zero(16)
    for labels in itertools.product(range(4), repeat=4):
        weight = F(1)
        unitary = [[e.ONE]]
        for label in labels:
            weight *= weights[label]
            unitary = kron(unitary, paulis[label])
        if weight:
            term = e.matmul(e.matmul(unitary, a), e.adjoint(unitary))
            result = e.add_matrix(result, e.scale_matrix(term, weight))
    return result


def diagonal_radii(rho):
    radii = []
    for site in range(4):
        local = e.local_marginal(rho, site)
        assert local[0][1] == local[1][0] == e.ZERO
        assert local[0][0][1] == local[1][1][1] == 0
        radii.append(abs(local[0][0][0] - local[1][1][0]))
    return radii


def main():
    P = e.zero(16)
    P[0][0] = P[15][15] = e.ONE
    P[3][3] = P[12][12] = e.z(F(1, 2))
    P[3][12] = e.z(0, -F(1, 2))
    P[12][3] = e.z(0, F(1, 2))
    assert P == e.adjoint(P) and e.matmul(P, P) == P and e.trace(P) == e.z(3)

    product = [e.ZERO] * 16
    product[0] = e.ONE
    W = [e.ZERO] * 16
    for index in (1, 2, 4, 8):
        W[index] = e.z(F(1, 2))
    unequal = [e.ZERO] * 16
    unequal[0], unequal[15] = e.z(F(3, 5)), e.z(F(4, 5))
    ghz = e.zero(16)
    for i in (0, 15):
        for j in (0, 15):
            ghz[i][j] = e.z(F(1, 2))
    states = (("product", pure_from_vector(product)), ("W", pure_from_vector(W)), ("unequal_GHZ_3_4", pure_from_vector(unequal)), ("equal_GHZ", ghz))
    parameters = (F(0), F(1, 2), F(2, 3), F(1), F(4, 3))
    result = []
    comparisons = 0
    for name, rho in states:
        assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
        radii = diagonal_radii(rho)
        R = sum(radii)
        layers = e.layers(rho)
        ts = [e.trace(e.matmul(P, layer)) for layer in layers]
        assert all(x[1] == 0 for x in ts)
        assert ts[1][0] <= 3 + R / 4
        assert ts[2][0] <= F(5, 2) + R / 2
        assert ts[3][0] <= (12 + 3 * R) / 16
        for p in parameters:
            out = e.channel(rho, p)
            if name == "unequal_GHZ_3_4" and p in (F(2, 3), F(4, 3)):
                assert out == direct_pauli(rho, p)
            tr = e.trace(e.matmul(P, out))
            assert tr[1] == 0
            s = min(p, 2 - p)
            a, b = 1 - s / 2, s / 2
            reference = a**4 + 2 * a**3 * b
            lower = s * (1 - s) * (8 * s - R * (4 - s**2)) / 16
            assert reference - tr[0] >= lower
            comparisons += 1
            if p in (F(2, 3), F(4, 3)):
                result.append({"state": name, "p": str(p), "R": str(R), "trace_actual_same_complex_P": str(tr[0]), "reference_top3": str(reference), "actual_trace_gap": str(reference - tr[0]), "bound_lower": str(lower), "strict_positive_bound": lower > 0})
    print(json.dumps({"scope": "exact finite physical examples only; no universal or independent proof", "states": len(states), "rational_parameter_checks": comparisons, "independent_full_Pauli_mixture_checks": 2, "rows": result}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
