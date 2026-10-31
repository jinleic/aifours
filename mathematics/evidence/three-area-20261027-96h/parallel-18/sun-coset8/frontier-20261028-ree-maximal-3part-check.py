#!/usr/bin/env python3
"""Exact bounded arithmetic check of the sourced small-Ree subgroup orders.

This verifies the quoted order arithmetic for six q values; it does not
construct a Ree group or verify maximal-subgroup completeness.
"""


def vp(n, p):
    if n <= 0:
        raise ValueError("nonpositive order")
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def main():
    for m in range(1, 7):
        e = 2*m + 1
        q = 3**e
        root = 3**(m+1)
        order = q**3 * (q**3 + 1) * (q-1)
        b = q**3 * (q-1)
        others = {
            "involution_centralizer": q*(q*q-1),
            "four_group_normalizer": 6*(q+1),
            "torus_minus_normalizer": 6*(q-root+1),
            "torus_plus_normalizer": 6*(q+root+1),
        }
        for d in divisors(e):
            if d != e:
                s = 3**d
                others[f"subfield_3^{d}"] = s**3*(s**3+1)*(s-1)
        if order // b != q**3+1 or order % b or vp(order, 3) != 3*e:
            raise SystemExit("FAIL group/B index or 3-part")
        for name, size in others.items():
            if order % size or vp(size, 3) >= 3*e:
                raise SystemExit(f"FAIL {name} for q={q}")
        wrong_order = q**3 * (q+1) * (q-1)
        if order != wrong_order * (q*q-q+1):
            raise SystemExit("FAIL source-order discrepancy identity")
        print(f"m={m}, q={q}, v3_group={3*e}, v3_B={vp(b,3)}, "
              f"max_v3_other={max(vp(x,3) for x in others.values())}, "
              f"index_B={q**3+1}")
    print("PASS: six q cases match stated 3-part and index comparisons")


if __name__ == "__main__":
    main()
