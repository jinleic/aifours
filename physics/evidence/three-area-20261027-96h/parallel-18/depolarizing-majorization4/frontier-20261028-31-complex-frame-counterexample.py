#!/usr/bin/env python3
"""Exact complex-rational subspace witness against auxiliary lambda_3 <= 2."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("dicke", ROOT / "frontier-20261028-26-dicke-pauli-counterexample.py")
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
b, e = d.b, d.e


def inverse_complex(z):
    den = z[0] * z[0] + z[1] * z[1]
    assert den
    return z[0] / den, -z[1] / den


def sub(a, c):
    return e.add(a, e.scale(c, -1))


def gram(W, M):
    out = [[e.ZERO for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for c in range(3):
            value = e.ZERO
            for i in range(16):
                for j in range(16):
                    if W[i][a] != e.ZERO and M[i][j] != e.ZERO and W[j][c] != e.ZERO:
                        value = e.add(value, e.mul(e.mul(e.conj(W[i][a]), M[i][j]), W[j][c]))
            out[a][c] = value
    return out


def det3(M):
    first = e.mul(M[0][0], sub(e.mul(M[1][1], M[2][2]), e.mul(M[1][2], M[2][1])))
    second = e.mul(M[0][1], sub(e.mul(M[1][0], M[2][2]), e.mul(M[1][2], M[2][0])))
    third = e.mul(M[0][2], sub(e.mul(M[1][0], M[2][1]), e.mul(M[1][1], M[2][0])))
    return e.add(sub(first, second), third)


def positive_minors(M):
    first = M[0][0]
    second = sub(e.mul(M[0][0], M[1][1]), e.mul(M[0][1], M[1][0]))
    third = det3(M)
    assert all(z[1] == 0 and z[0] > 0 for z in (first, second, third))
    return first[0], second[0], third[0]


def inverse3(M):
    data = [row[:] + [e.ONE if i == j else e.ZERO for j in range(3)] for i, row in enumerate(M)]
    for k in range(3):
        pivot = next(i for i in range(k, 3) if data[i][k] != e.ZERO)
        data[k], data[pivot] = data[pivot], data[k]
        reciprocal = inverse_complex(data[k][k])
        data[k] = [e.mul(entry, reciprocal) for entry in data[k]]
        for i in range(3):
            if i != k:
                factor = data[i][k]
                data[i] = [sub(data[i][j], e.mul(factor, data[k][j])) for j in range(6)]
    return [row[3:] for row in data]


def positive_definite_ldl(M):
    work = [row[:] for row in M]
    pivots = []
    for k in range(16):
        pivot = work[k][k]
        assert pivot[1] == 0 and pivot[0] > 0
        pivots.append(pivot[0])
        for i in range(k + 1, 16):
            for j in range(k + 1, 16):
                work[i][j] = sub(work[i][j], e.scale(e.mul(work[i][k], work[k][j]), 1 / pivot[0]))
    return pivots


def main():
    support = [2, 3, 5, 8, 9, 10, 12, 13, 14, 15]
    phases = [(0, -1), (0, -1), (0, -1), (0, -1), (0, 1), (-1, 0), (-1, 0), (1, 0), (0, 1), (0, 1)]
    v = [e.ZERO] * 16
    for index, (real, imag) in zip(support, phases):
        v[index] = e.z(real, imag)
    rho = [[e.scale(e.mul(v[i], e.conj(v[j])), F(1, 10)) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    frame = d.local_pauli_frame(rho)
    t1 = e.zero(16)
    for site in range(4):
        t1 = e.add_matrix(t1, e.one_erasure(rho, site))
    assert frame == e.add_matrix(e.scale_matrix(t1, 4), e.scale_matrix(rho, -4))
    raw = [
        [(0, 0), (-2, 0), (-1, 0)], [(3, 0), (-1, 0), (2, 0)], [(0, 0), (0, 2), (0, 5)], [(0, -2), (0, -1), (0, 3)],
        [(0, 2), (0, 1), (0, 2)], [(0, 0), (0, -3), (0, -2)], [(2, 0), (2, 0), (1, 0)], [(3, 0), (3, 0), (1, 0)],
        [(0, -3), (0, 4), (0, -3)], [(0, 0), (0, -1), (0, 3)], [(-2, 0), (5, 0), (1, 0)], [(-4, 0), (0, 0), (0, 0)],
        [(1, 0), (3, 0), (-4, 0)], [(-5, 0), (1, 0), (4, 0)], [(0, -3), (0, -3), (0, -1)], [(0, 1), (0, 2), (0, 0)],
    ]
    W = [[e.z(real, imag) for real, imag in row] for row in raw]
    identity = e.zero(16)
    for i in range(16):
        identity[i][i] = e.ONE
    score = e.add_matrix(frame, e.scale_matrix(identity, -F(9, 4)))
    minors = positive_minors(gram(W, score))
    Wgram = gram(W, identity)
    positive_minors(Wgram)
    Winv = inverse3(Wgram)
    P = e.zero(16)
    for i in range(16):
        for j in range(16):
            value = e.ZERO
            for a in range(3):
                for c in range(3):
                    value = e.add(value, e.mul(e.mul(W[i][a], Winv[a][c]), e.conj(W[j][c])))
            P[i][j] = value
    assert P == e.adjoint(P) and e.matmul(P, P) == P and e.trace(P) == e.z(3)
    frame_trace = e.trace(e.matmul(P, frame))
    assert frame_trace[1] == 0 and frame_trace[0] > F(27, 4)

    originals = []
    for p in (F(2, 3), F(4, 3)):
        out = e.channel(rho, p)
        assert out == b.direct_pauli(rho, p)
        assert len(positive_definite_ldl(out)) == 16
        bound_matrix = e.add_matrix(e.scale_matrix(identity, F(1, 8)), e.scale_matrix(out, -1))
        pivots = positive_definite_ldl(bound_matrix)
        assert len(pivots) == 16
        s = min(p, 2 - p)
        a, c = 1 - s / 2, s / 2
        ref = a**4 + 2 * a**3 * c
        assert F(3, 8) < ref
        same_pair = e.trace(e.matmul(P, out))
        assert same_pair[1] == 0 and same_pair[0] < F(3, 8)
        numeric = np.array([[complex(float(z[0]), float(z[1])) for z in row] for row in out])
        eig = np.linalg.eigvalsh(numeric)[::-1]
        originals.append({"p": str(p), "direct_original_Pauli_matches_sequential_exact": True, "exact_positive_ldl_pivots": len(pivots), "exact_output_positive_ldl_pivots": 16, "certified_original_top3_upper": "3/8", "product_reference_top3": str(ref), "certified_reference_margin_lower": str(ref - F(3, 8)), "same_actual_projector_trace": str(same_pair[0]), "numerical_top3_eigenvalues": [float(x) for x in eig[:3]], "numerical_top3_sum": float(sum(eig[:3]))})
    print(json.dumps({"scope": "one exact physical counterexample to auxiliary lambda3<=2, not an original-channel violation", "state_support": support, "integer_amplitudes_before_sqrt10": [[a, c] for a, c in phases], "state_rank": 1, "physical_projector_rank": 3, "strict_frame_threshold": "9/4", "exact_positive_gram_leading_minors": [str(v) for v in minors], "actual_rank3_frame_trace": str(frame_trace[0]), "original_channel_checks": originals}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
