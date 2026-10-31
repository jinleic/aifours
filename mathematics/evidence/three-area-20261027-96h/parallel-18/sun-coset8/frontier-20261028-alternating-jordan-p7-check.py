#!/usr/bin/env python3
"""Selected exact binomial controls for the P7-specific Jordan criterion."""

from math import comb, factorial, gcd, lcm, isqrt

for r, t, expected in ((19, 13, 4), (29, 7, 3)):
    assert r > 7 and all(r % d for d in range(2, isqrt(r)+1)) and 3 <= t < r
    n = r+t
    L = lcm(*range(1, t+1))
    D = n//gcd(n, L)
    assert D == expected and 7 % D != 0 and lcm(7, D) > 7
    assert all(comb(n, u) % D == 0 for u in range(1, t+1))
    print(f"n={n}, r={r}, t={t}, D_lcm={D}, D_factorial={n//gcd(n, factorial(t))}")
print("PASS: two integer examples only; Jordan and subgroup claims not verified")
