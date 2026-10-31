#!/usr/bin/env python3
"""Exact finite checks of the rank-two spin-flip overlap optimization."""

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
    a, c = math.isqrt(value.numerator), math.isqrt(value.denominator)
    assert a * a == value.numerator and c * c == value.denominator
    return F(a, c)


def projector(first, second, third, fourth):
    out = e.zero(16)
    out[first][first] = out[second][second] = e.ONE
    out[third][third] = out[fourth][fourth] = e.z(F(1, 2))
    out[third][fourth] = e.z(0, -F(1, 2))
    out[fourth][third] = e.z(0, F(1, 2))
    assert out == e.adjoint(out) and e.matmul(out, out) == out and e.trace(out) == e.z(3)
    return out


def above_radical_bound(actual_gap, baseline, A, B, d):
    # actual_gap >= baseline+B+A/2 - sqrt(discriminant)/2, without floats.
    disc = A * A + 4 * B * max(B - A, 0) * d * d
    left = 2 * (actual_gap - baseline - B - A / 2)
    assert left >= 0 or disc >= left * left
    return disc


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
    params = (F(0), F(1, 2), F(2, 3), F(4, 5), F(1), F(6, 5), F(4, 3))
    count = 0
    characteristic_checks = 0
    direct_checks = 0
    rows = []
    for name, rho in states:
        assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
        radii = sorted(b.diagonal_radii(rho))
        R = sum(radii)
        L = radii[0] + radii[1] + 3 * radii[2] + 3 * radii[3]
        tilde = e.global_spinflip(rho)
        c2 = e.trace(e.matmul(rho, tilde))
        assert c2[1] == 0 and 0 <= c2[0] <= 1
        d = rational_sqrt(1 - c2[0])
        for p in params:
            s = min(p, 2 - p)
            q = 1 - s
            A, B = q**4, s**2 * q**2 / 4
            K = e.add_matrix(e.scale_matrix(rho, A - B), e.scale_matrix(tilde, B))
            K2 = e.matmul(K, K)
            K3 = e.matmul(K2, K)
            characteristic = e.add_matrix(e.add_matrix(K3, e.scale_matrix(K2, -A)), e.scale_matrix(K, (A - B) * B * d**2))
            assert characteristic == e.zero(16)
            characteristic_checks += 1
            extra = max(B - A, 0)
            left = A + 2 * d * extra
            disc = A * A + 4 * B * extra * d * d
            if extra:
                assert left * left - disc == 4 * A * extra * d * (1 - d) >= 0
            baseline = s * q * (8 * s - (2 - s) * (2 * q * R + s * L)) / 16
            out = e.channel(rho, p)
            if name == "complex_unequal_GHZ" and p in (F(4, 5), F(6, 5)):
                assert out == b.direct_pauli(rho, p)
                direct_checks += 1
            a, c = 1 - s / 2, s / 2
            reference = a**4 + 2 * a**3 * c
            for label, P in (("P0", P0), ("P1", P1)):
                tr = e.trace(e.matmul(P, out))
                assert tr[1] == 0
                gap = reference - tr[0]
                checked_disc = above_radical_bound(gap, baseline, A, B, d)
                assert checked_disc == disc
                previous = baseline + B - d * extra
                assert gap >= previous
                count += 1
                if name == "complex_unequal_GHZ" and p in (F(4, 5), F(6, 5)):
                    assert A == F(1, 625) and B == F(4, 625) and d == F(7, 25)
                    assert disc == F(2977, 244140625)
                    assert baseline == F(116, 3125) and previous == F(659, 15625)
                    assert 54**2 < 2977 < 55**2
                    rows.append({"state": name, "p": str(p), "projector": label, "d": str(d), "actual_trace_gap": str(gap), "previous_bound": str(previous), "new_bound_exact": "(1385-sqrt(2977))/31250", "new_bound_interval": "(133/3125,1331/31250)"})
    print(json.dumps({"scope": "exact finite actual-pair and rank-two identities, not universal proof or independent review", "state_projector_parameter_checks": count, "rank_two_characteristic_matrix_checks": characteristic_checks, "independent_original_Pauli_matrix_checks": direct_checks, "selected_rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
