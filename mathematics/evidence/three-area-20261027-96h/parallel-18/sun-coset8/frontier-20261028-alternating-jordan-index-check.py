#!/usr/bin/env python3
"""Finite exact binomial/index controls; no subgroup classification performed."""

from math import comb, factorial, gcd, isqrt

for r, t in ((13, 3), (19, 4), (431, 41)):
    assert all(r % d for d in range(2, isqrt(r)+1)) and 3 <= t < r
    n = r+t
    common = n//gcd(n, factorial(t))
    assert common > 7
    assert all(comb(n, u) % common == 0 for u in range(1, t+1))
    print(f"r={r}, t={t}, n={n}, common-divisor={common}")

model = (93961, 42398181, 10857619219552, 1762351955, 16435111, 51032359)
assert all(value % 59 != 0 for value in model)
print("A472 relaxation: all six previously displayed r-free numbers fail divisibility by 59")
print("PASS: finite integer checks only; Jordan's theorem and subgroup existence not checked")
