#!/usr/bin/env python3
"""Bounded exact checks for the same-projector sharpened Bloch-radius bound."""

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
    result = e.zero(16)
    result[first][first] = result[second][second] = e.ONE
    result[third][third] = result[fourth][fourth] = e.z(F(1, 2))
    result[third][fourth] = e.z(0, -F(1, 2))
    result[fourth][third] = e.z(0, F(1, 2))
    assert result == e.adjoint(result) and e.matmul(result, result) == result and e.trace(result) == e.z(3)
    return result


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
    total = 0
    pauli_checks = 0
    rows = []
    for name, rho in states:
        assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
        R = sum(b.diagonal_radii(rho))
        rho_layers = e.layers(rho)
        tilde = e.global_spinflip(rho)
        for label, P in (("P0", P0), ("P1", P1)):
            ts = [e.trace(e.matmul(P, layer)) for layer in rho_layers]
            assert all(value[1] == 0 for value in ts)
            x = ts[0][0]
            y = e.trace(e.matmul(P, tilde))
            assert y[1] == 0 and 0 <= x <= 1 and 0 <= y[0] <= 1
            assert 4 * ts[2][0] == y[0] - x + 2 * ts[1][0] + 8 * ts[3][0] - 3
            assert ts[2][0] <= F(5, 2) - x / 4 + R / 2
            for p in parameters:
                out = e.channel(rho, p)
                if name == "complex_unequal_GHZ" and label == "P0" and p in (F(1, 2), F(6, 5), F(4, 3)):
                    assert out == b.direct_pauli(rho, p)
                    pauli_checks += 1
                tr = e.trace(e.matmul(P, out))
                assert tr[1] == 0
                s = min(p, 2 - p)
                q = 1 - s
                a, c = 1 - s / 2, s / 2
                reference = a**4 + 2 * a**3 * c
                old_lower = s * q * (8 * s - R * (4 - s**2)) / 16
                gain = min(q**4, s**2 * q**2 / 4)
                lower = old_lower + gain
                assert reference - tr[0] >= lower
                total += 1
                if name in ("complex_unequal_GHZ", "W") and p in (F(1, 2), F(4, 5), F(6, 5), F(4, 3)):
                    rows.append({"state": name, "projector": label, "p": str(p), "R": str(R), "same_pair_overlap": str(x), "reference_top3": str(reference), "actual_same_P_trace": str(tr[0]), "actual_trace_gap": str(reference - tr[0]), "old_lower": str(old_lower), "additional_gain": str(gain), "sharpened_lower": str(lower)})
    print(json.dumps({"scope": "exact finite actual-pair checks, not a universal proof or independent review", "states": len(states), "complex_projectors": 2, "rational_parameters": len(parameters), "state_projector_parameter_checks": total, "independent_full_Pauli_channel_checks": pauli_checks, "rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
