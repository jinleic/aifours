#!/usr/bin/env python3
"""Exact bounded anisotropic-bound and W-state original-channel spectrum checks."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("bloch_check", ROOT / "frontier-20261028-12-bloch-gap-check.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
e = b.e


def projector(first, second, third, fourth):
    out = e.zero(16)
    out[first][first] = out[second][second] = e.ONE
    out[third][third] = out[fourth][fourth] = e.z(F(1, 2))
    out[third][fourth] = e.z(0, -F(1, 2))
    out[fourth][third] = e.z(0, F(1, 2))
    assert out == e.adjoint(out) and e.matmul(out, out) == out and e.trace(out) == e.z(3)
    return out


def rank_fraction(matrix):
    data = [row[:] for row in matrix]
    n = len(data)
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, n) if data[i][col]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        factor = data[rank][col]
        data[rank] = [x / factor for x in data[rank]]
        for i in range(rank + 1, n):
            factor = data[i][col]
            if factor:
                data[i] = [data[i][j] - factor * data[rank][j] for j in range(n)]
        rank += 1
        if rank == n:
            break
    return rank


def main():
    P0 = projector(0, 15, 3, 12)
    P1 = projector(3, 12, 5, 10)
    product = [e.ZERO] * 16
    product[0] = e.ONE
    W = [e.ZERO] * 16
    for index in (1, 2, 4, 8):
        W[index] = e.z(F(1, 2))
    unequal = [e.ZERO] * 16
    unequal[0], unequal[15] = e.z(F(3, 5)), e.z(F(4, 5))
    phase = unequal[:]
    phase[15] = e.z(0, F(4, 5))
    ghz = e.zero(16)
    for i in (0, 15):
        for j in (0, 15):
            ghz[i][j] = e.z(F(1, 2))
    states = (("product", b.pure_from_vector(product)), ("W", b.pure_from_vector(W)), ("unequal_GHZ", b.pure_from_vector(unequal)), ("complex_unequal_GHZ", b.pure_from_vector(phase)), ("equal_GHZ", ghz))
    parameters = (F(0), F(1, 2), F(2, 3), F(4, 5), F(1), F(6, 5), F(4, 3))
    count = 0
    for _, rho in states:
        assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
        radii = sorted(b.diagonal_radii(rho))
        R = sum(radii)
        L = radii[0] + radii[1] + 3 * radii[2] + 3 * radii[3]
        assert L <= 3 * R
        ts_matrices = e.layers(rho)
        for P in (P0, P1):
            ts = [e.trace(e.matmul(P, matrix)) for matrix in ts_matrices]
            assert all(value[1] == 0 for value in ts)
            x = ts[0][0]
            assert ts[1][0] <= 3 + R / 4
            assert ts[3][0] <= (12 + L) / 16
            assert ts[2][0] <= F(5, 2) - x / 4 + (R + L) / 8
            for p in parameters:
                s = min(p, 2 - p)
                q = 1 - s
                out = e.channel(rho, p)
                tr = e.trace(e.matmul(P, out))
                assert tr[1] == 0
                a, c = 1 - s / 2, s / 2
                reference = a**4 + 2 * a**3 * c
                h = min(q**4, s**2 * q**2 / 4)
                sharp = s * q * (8 * s - (2 - s) * (2 * q * R + s * L)) / 16 + h
                coarse = s * q * (8 * s - R * (4 - s**2)) / 16 + h
                assert sharp - coarse == s**2 * q * (2 - s) * (3 * R - L) / 16 >= 0
                assert reference - tr[0] >= sharp
                count += 1

    rhoW = b.pure_from_vector(W)
    Ptop = e.zero(16)
    Ptop[0][0] = e.ONE
    Ptop = e.add_matrix(Ptop, rhoW)
    weight2 = [i for i in range(16) if i.bit_count() == 2]
    for i in weight2:
        for j in weight2:
            Ptop[i][j] = e.z(F(1, 6))
    assert Ptop == e.adjoint(Ptop) and e.matmul(Ptop, Ptop) == Ptop and e.trace(Ptop) == e.z(3)
    spectrum = ((F(10, 81), 1), (F(8, 81), 1), (F(7, 81), 1), (F(6, 81), 3), (F(5, 81), 3), (F(4, 81), 3), (F(3, 81), 3), (F(2, 81), 1))
    assert sum(mult for _, mult in spectrum) == 16
    rows = []
    for p in (F(2, 3), F(4, 3)):
        out = e.channel(rhoW, p)
        assert out == b.direct_pauli(rhoW, p)
        assert all(cell[1] == 0 for row in out for cell in row)
        for value, multiplicity in spectrum:
            shifted = [[out[i][j][0] - (value if i == j else 0) for j in range(16)] for i in range(16)]
            assert 16 - rank_fraction(shifted) == multiplicity
        actual_P = Ptop if p == F(2, 3) else e.global_spinflip(Ptop)
        assert actual_P == e.adjoint(actual_P) and e.matmul(actual_P, actual_P) == actual_P and e.trace(actual_P) == e.z(3)
        tr = e.trace(e.matmul(actual_P, out))
        assert tr == e.z(F(25, 81))
        reference = F(32, 81)
        assert reference - tr[0] == F(7, 81) >= F(1, 81)
        rows.append({"p": str(p), "actual_physical_top3": str(tr[0]), "product_reference_top3": str(reference), "exact_gap": str(reference - tr[0]), "anisotropic_bound": "1/81", "coarse_predecessor_bound": "-1/81"})
    print(json.dumps({"scope": "exact finite original-channel checks; not universal proof or independent review", "state_projector_parameter_checks": count, "independent_original_Pauli_mixture_matrix_checks": len(rows), "W_exact_spectrum_numerators_over_81": [[int(value * 81), multiplicity] for value, multiplicity in spectrum], "W_top3_rank_checked_rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
