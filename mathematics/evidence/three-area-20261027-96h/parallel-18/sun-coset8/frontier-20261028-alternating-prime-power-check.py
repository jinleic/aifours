#!/usr/bin/env python3
"""Exact finite controls for the prime-power-degree written candidate."""

from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


tested = twin_cases = 0
for p in range(11, 301):
    if not prime(p):
        continue
    n = p
    while n <= 300:
        if n >= 17:
            candidates = [r for r in range((n//2)+1, n) if prime(r)]
            assert candidates
            r = candidates[-1]
            t = n-r
            assert r > 7 and 2 <= t < r and t % 2 == 0
            if t == 2:
                twin_cases += 1
                q = n-1
                assert q & (q-1) != 0
            assert all(comb(n, u) % p == 0 for u in range(1, t+1))
            tested += 1
        n *= p
print(f"PASS: {tested} prime-power degrees <=300, including {twin_cases} two-fixed-point cases")
print("Finite arithmetic only; Bertrand, Jordan/Jones and subgroup claims not checked")
