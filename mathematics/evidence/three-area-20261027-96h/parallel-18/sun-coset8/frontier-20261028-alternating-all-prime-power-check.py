#!/usr/bin/env python3
"""Exact small-prime-power controls; not a classification or gap theorem."""

from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


count = 0
for p in (2, 3, 5, 7):
    n = p
    a = 1
    while n < 500000:
        if n >= 17:
            r = n-3
            while not prime(r):
                r -= 1
            t = n-r
            assert r > 7 and 3 <= t < r
            if p == 7:
                assert 7*t < n
                divisor = 49
                print(f"7-power n={n}, exponent={a}, r={r}, t={t}")
            else:
                divisor = p
            assert all(comb(n, u) % divisor == 0 for u in range(1, t+1))
            count += 1
        n *= p
        a += 1
print(f"PASS: {count} selected small prime powers; p=7 close-prime rows explicit")
print("Exact integers only; external prime-gap and permutation theorems not verified")
