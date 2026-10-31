#!/usr/bin/env python3
"""Exact Dicke-state counterexample to an auxiliary Pauli-frame eigenvalue premise."""

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("w_checker", ROOT / "frontier-20261028-18-anisotropic-w-check.py")
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)
b, e = w.b, w.e


def local_pauli_frame(rho):
    I = [[e.ONE, e.ZERO], [e.ZERO, e.ONE]]
    X = [[e.ZERO, e.ONE], [e.ONE, e.ZERO]]
    Y = [[e.ZERO, e.z(0, -1)], [e.IMAG, e.ZERO]]
    Z = [[e.ONE, e.ZERO], [e.ZERO, e.z(-1)]]
    total = e.zero(16)
    for site in range(4):
        for pauli in (X, Y, Z):
            unitary = [[e.ONE]]
            for i in range(4):
                unitary = b.kron(unitary, pauli if i == site else I)
            total = e.add_matrix(total, e.matmul(e.matmul(unitary, rho), e.adjoint(unitary)))
    return total


def verify_spectrum(matrix, expected):
    assert all(x[1] == 0 for row in matrix for x in row)
    assert sum(expected.values()) == 16
    for value, multiplicity in expected.items():
        shifted = [[matrix[i][j][0] - (value if i == j else 0) for j in range(16)] for i in range(16)]
        assert 16 - w.rank_fraction(shifted) == multiplicity
    return sorted((value for value, mult in expected.items() for _ in range(mult)), reverse=True)


def original_spectrum(matrix):
    assert all(x[1] == 0 for row in matrix for x in row)
    assert all(matrix[i][j] == e.ZERO for i in range(16) for j in range(16) if i.bit_count() != j.bit_count())
    eig = Counter()
    for k in (0, 4):
        idx = [i for i in range(16) if i.bit_count() == k][0]
        eig[matrix[idx][idx][0]] += 1
    for k in (1, 3):
        idx = [i for i in range(16) if i.bit_count() == k]
        diag = matrix[idx[0]][idx[0]][0]
        other = matrix[idx[0]][idx[1]][0]
        assert all(matrix[i][j][0] == (diag if i == j else other) for i in idx for j in idx)
        eig[diag + 3 * other] += 1
        eig[diag - other] += 3
    idx = [i for i in range(16) if i.bit_count() == 2]
    diag = matrix[idx[0]][idx[0]][0]
    common_one = next(matrix[idx[0]][j][0] for j in idx if (idx[0] & j).bit_count() == 1)
    common_zero = next(matrix[idx[0]][j][0] for j in idx if (idx[0] & j).bit_count() == 0)
    for i in idx:
        for j in idx:
            expected = diag if i == j else common_one if (i & j).bit_count() == 1 else common_zero
            assert matrix[i][j][0] == expected
    eig[diag + 4 * common_one + common_zero] += 1
    eig[diag - common_zero] += 3
    eig[diag - 2 * common_one + common_zero] += 2
    return eig


def main():
    indices = [i for i in range(16) if i.bit_count() == 2]
    rho = e.zero(16)
    for i in indices:
        for j in indices:
            rho[i][j] = e.z(F(1, 6))
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    for site in range(4):
        assert e.local_marginal(rho, site) == [[e.z(F(1, 2)), e.ZERO], [e.ZERO, e.z(F(1, 2))]]
    frame = local_pauli_frame(rho)
    t1 = e.zero(16)
    for site in range(4):
        t1 = e.add_matrix(t1, e.one_erasure(rho, site))
    assert frame == e.add_matrix(e.scale_matrix(t1, 4), e.scale_matrix(rho, -4))
    frame_expected = {F(3): 2, F(4, 3): 3, F(1, 3): 6, F(0): 5}
    frame_eigen = verify_spectrum(frame, frame_expected)
    assert frame_eigen[1] == 3 and sum(frame_eigen[:3]) == F(22, 3)
    P = e.zero(16)
    for weight in (1, 3):
        group = [i for i in range(16) if i.bit_count() == weight]
        for i in group:
            for j in group:
                P[i][j] = e.z(F(1, 4))
    P[3][3] = P[12][12] = e.z(F(1, 2))
    P[3][12] = P[12][3] = e.z(-F(1, 2))
    assert P == e.adjoint(P) and e.matmul(P, P) == P and e.trace(P) == e.z(3)
    assert e.trace(e.matmul(P, frame)) == e.z(F(22, 3))
    Pchannel = e.add_matrix(rho, e.zero(16))
    for weight in (1, 3):
        group = [i for i in range(16) if i.bit_count() == weight]
        for i in group:
            for j in group:
                Pchannel[i][j] = e.z(F(1, 4))
    assert Pchannel == e.adjoint(Pchannel) and e.matmul(Pchannel, Pchannel) == Pchannel and e.trace(Pchannel) == e.z(3)
    originals = []
    for p in (F(2, 3), F(4, 3)):
        out = e.channel(rho, p)
        assert out == b.direct_pauli(rho, p)
        spectrum = original_spectrum(out)
        eigen = verify_spectrum(out, spectrum)
        assert all(value >= 0 for value in eigen)
        s = min(p, 2 - p)
        a, c = 1 - s / 2, s / 2
        ref = a**4 + 2 * a**3 * c
        actual_P_trace = e.trace(e.matmul(Pchannel, out))
        assert actual_P_trace == e.z(sum(eigen[:3]))
        originals.append({"p": str(p), "full_spectrum_descending": [[str(value), spectrum[value]] for value in sorted(spectrum, reverse=True)], "original_channel_top3": str(sum(eigen[:3])), "same_original_projector_trace": str(actual_P_trace[0]), "product_reference_top3": str(ref), "original_gap": str(ref - sum(eigen[:3]))})
    print(json.dumps({"scope": "one exact physical counterexample to auxiliary lambda2<=2; no original-channel violation claimed", "state": "normalized four-qubit Dicke state with exactly two excitations", "input_rank": 1, "all_local_marginals": "I/2", "auxiliary_frame_spectrum": [["3", 2], ["4/3", 3], ["1/3", 6], ["0", 5]], "auxiliary_second_eigenvalue": "3", "actual_rank3_auxiliary_trace": "22/3", "original_channel_checks": originals}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
