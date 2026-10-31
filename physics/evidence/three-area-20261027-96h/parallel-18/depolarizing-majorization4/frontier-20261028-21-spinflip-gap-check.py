#!/usr/bin/env python3
"""Exact finite checks of spin-flip-overlap sharpening and GHZ eigenvalues."""

import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("bloch_check", ROOT / "frontier-20261028-12-bloch-gap-check.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
e = b.e


def rational_sqrt(value):
    assert value >= 0
    a, b_ = math.isqrt(value.numerator), math.isqrt(value.denominator)
    assert a * a == value.numerator and b_ * b_ == value.denominator
    return F(a, b_)


def projector(first, second, third, fourth):
    out = e.zero(16)
    out[first][first] = out[second][second] = e.ONE
    out[third][third] = out[fourth][fourth] = e.z(F(1, 2))
    out[third][fourth] = e.z(0, -F(1, 2))
    out[fourth][third] = e.z(0, F(1, 2))
    assert out == e.adjoint(out) and e.matmul(out, out) == out and e.trace(out) == e.z(3)
    return out


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
    direct_checks = 0
    examples = []
    for name, rho in states:
        assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
        radii = sorted(b.diagonal_radii(rho))
        R = sum(radii)
        L = radii[0] + radii[1] + 3 * radii[2] + 3 * radii[3]
        tilde = e.global_spinflip(rho)
        c2 = e.trace(e.matmul(rho, tilde))
        assert c2[1] == 0 and 0 <= c2[0] <= 1
        d = rational_sqrt(1 - c2[0])
        for label, P in (("P0", P0), ("P1", P1)):
            x, y = e.trace(e.matmul(P, rho)), e.trace(e.matmul(P, tilde))
            assert x[1] == y[1] == 0 and y[0] - x[0] <= min(d, 1 - x[0])
            for p in parameters:
                s = min(p, 2 - p)
                q = 1 - s
                out = e.channel(rho, p)
                if name == "complex_unequal_GHZ" and label == "P0" and p in (F(4, 5), F(6, 5)):
                    assert out == b.direct_pauli(rho, p)
                    direct_checks += 1
                tr = e.trace(e.matmul(P, out))
                assert tr[1] == 0
                a, c = 1 - s / 2, s / 2
                reference = a**4 + 2 * a**3 * c
                A, B = q**4, s**2 * q**2 / 4
                base = s * q * (8 * s - (2 - s) * (2 * q * R + s * L)) / 16
                previous = base + min(A, B)
                sharpened = base + B - d * max(B - A, 0)
                assert sharpened - previous == (1 - d) * max(B - A, 0) >= 0
                assert reference - tr[0] >= sharpened
                count += 1
                if name in ("equal_GHZ", "complex_unequal_GHZ") and p in (F(4, 5), F(6, 5)):
                    examples.append({"state": name, "projector": label, "p": str(p), "R": str(R), "L": str(L), "c_squared": str(c2[0]), "d": str(d), "previous_lower": str(previous), "new_lower": str(sharpened), "actual_same_P_trace": str(tr[0]), "reference_top3": str(reference), "actual_trace_gap": str(reference - tr[0])})

    top_projector = e.zero(16)
    for index in (0, 1, 15):
        top_projector[index][index] = e.ONE
    assert top_projector == e.adjoint(top_projector) and e.matmul(top_projector, top_projector) == top_projector and e.trace(top_projector) == e.z(3)
    spectra = []
    for p in (F(4, 5), F(6, 5)):
        out = e.channel(ghz, p)
        assert out == b.direct_pauli(ghz, p)
        direct_checks += 1
        t = abs(1 - p)
        a, c = (1 + t) / 2, (1 - t) / 2
        d0 = (a**4 + c**4) / 2
        d1 = (a**3 * c + a * c**3) / 2
        d2 = a**2 * c**2
        for i in range(16):
            for j in range(16):
                if i == j:
                    weight = i.bit_count()
                    expected = d0 if weight in (0, 4) else d1 if weight in (1, 3) else d2
                    assert out[i][j] == e.z(expected)
                elif (i, j) in ((0, 15), (15, 0)):
                    assert out[i][j] == e.z(t**4 / 2)
                else:
                    assert out[i][j] == e.ZERO
        assert d0 + t**4 / 2 >= d0 - t**4 / 2 >= d1 >= d2
        exact_top3 = 2 * d0 + d1
        actual_P = top_projector if p == F(4, 5) else e.global_spinflip(top_projector)
        assert actual_P == e.adjoint(actual_P) and e.matmul(actual_P, actual_P) == actual_P and e.trace(actual_P) == e.z(3)
        assert e.trace(e.matmul(actual_P, out)) == e.z(exact_top3)
        reference = a**4 + 2 * a**3 * c
        assert exact_top3 == F(136, 625) and reference == F(189, 625)
        assert reference - exact_top3 == F(53, 625) >= F(44, 625)
        spectra.append({"p": str(p), "exact_GHZ_top3": str(exact_top3), "reference_top3": str(reference), "exact_gap": str(reference - exact_top3), "previous_anisotropic_bound": "41/625", "spinflip_bound": "44/625"})
    print(json.dumps({"scope": "finite exact checks, not universal proof or independent review", "state_projector_parameter_checks": count, "full_Pauli_channel_matrix_checks": direct_checks, "exact_GHZ_spectrum_checks": spectra, "selected_rows": examples}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
