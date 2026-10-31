#!/usr/bin/env python3
"""Check the universal polynomial identities behind Walsh support parity."""

import argparse
import json
import math
from pathlib import Path

MOD = 512


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def h_coeff(j):
    if j % 2 == 0:
        r = j // 2
        return (-1) ** r * choose(7, r)
    r = (j - 1) // 2
    return 256 * (-1) ** r * choose(6, r)


def check_global_identity(delta=0):
    result = []
    for j in range(257):
        left = sum(h_coeff(k) * (-1) ** ((j - k) // 2) * choose(121, (j - k) // 2)
                   for k in range(15) if j >= k and (j - k) % 2 == 0)
        if j % 2 == 0:
            left += delta * (-1) ** (j // 2) * choose(121, j // 2)
        right = choose(256, j)
        if (left - right) % MOD:
            result.append(j)
    return result


def coeff_b_at_translated_center(t, degree, sign):
    # sign=+1: z=1-u; sign=-1: z=u-1.
    if sign == 1:
        low, exponent = 7 + t, 7 - t
    else:
        low, exponent = 7 - t, 7 + t
    j = degree - low
    return 0 if not 0 <= j <= exponent else (-1) ** j * choose(exponent, j) * (1 << (exponent - j))


def h_at_translated_center(degree, sign):
    # H=(1-z²)^7+256z(1-z²)^6 and z=sign*(1-u).
    r = degree - 7
    first = 0 if not 0 <= r <= 7 else (-1) ** r * choose(7, r) * (1 << (7 - r))
    q = degree - 6
    c0 = 0 if not 0 <= q <= 6 else (-1) ** q * choose(6, q) * (1 << (6 - q))
    q2 = degree - 7
    c1 = 0 if not 0 <= q2 <= 6 else (-1) ** q2 * choose(6, q2) * (1 << (6 - q2))
    return first + 256 * sign * (c0 - c1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mismatch = check_global_identity()
    if mismatch:
        raise RuntimeError(f"global polynomial identity mismatch at {mismatch}")
    control = check_global_identity(delta=1)
    if not control or control[0] != 0:
        raise RuntimeError("mutated polynomial control did not fail at expected degree zero")
    cases = []
    for sign in (1, -1):
        for degree, divisor, modulus in ((6, 256, 2), (7, 128, 4)):
            coefficients = [coeff_b_at_translated_center(t, degree, sign) for t in range(-7, 8)]
            constant = h_at_translated_center(degree, sign)
            if any(c % divisor for c in coefficients) or constant % divisor:
                raise RuntimeError("coefficient not divisible by stated common factor")
            reduced = [(c // divisor) % modulus for c in coefficients]
            reduced_constant = (constant // divisor) % modulus
            expected = [0] * 15
            if degree == 6:
                for t in range(-7, 8):
                    expected[t + 7] = int((t < 0) if sign == 1 else (t > 0))
                expected_constant = 0
            else:
                expected[7] = 1
                expected[3 if sign == 1 else 11] = 2
                expected_constant = 1
            if reduced != expected or reduced_constant != expected_constant:
                raise RuntimeError(f"symbolic coefficient mismatch for sign={sign}, degree={degree}")
            cases.append({"substitution": "z=1-u" if sign == 1 else "z=u-1", "degree": degree,
                          "modulus": modulus, "A_t_coefficients_t_minus7_to_7": reduced,
                          "constant": reduced_constant, "matches_symbolic_statement": True})
    receipt = {"identity_coefficients_checked": 257, "global_identity_mismatches": mismatch,
               "mutated_constant_control": {"first_mismatch_degree": control[0], "rejected": True},
               "translated_coefficient_checks": cases,
               "method": "exact integer polynomial coefficients modulo 512; all 15 formal variables individually"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print("global polynomial identity: all 257 coefficients PASS; mutated constant: degree-0 rejection PASS")
    for case in cases:
        print(f"{case['substitution']} u^{case['degree']} mod {case['modulus']}: PASS")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()
