#!/usr/bin/env python3
"""Bounded exact arithmetic controls; no actual subgroup classification."""

from math import comb, factorial, gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


pairs = 0
for n in range(14, 201):
    t = (n-1)//2
    for i in range(3, t+1):
        a = comb(n, i)
        assert a > 7
        for j in range(i+1, t+1):
            b = comb(n, j)
            c = comb(j, i)
            assert a*comb(n-i, j-i) == b*c
            assert a > 7*c and gcd(a, b) > 7
            pairs += 1

for n in (14, 15, 16):
    r = 11
    assert prime(r) and r > n//2 and 3 <= n-r < r

for e in (5, 7):
    q = 2**e
    assert prime(e) and prime(q-1)
    n = q+1
    order = factorial(n)//2
    assert all(order % (d*q*(q*q-1)) == 0 for d in (1, e))
    print(f"q={q}, r={q-1}, n={n}: both source-allowed order overbounds divide |A_n|")

for n in range(5, 14):
    other_primes = [p for p in range(2, n+1) if p != 7 and prime(p)]
    assert len(other_primes) <= 5
print(f"PASS: {pairs} binomial pairs, n=14..16 prime cycles, n<=13 support bounds")
print("Finite integer controls only; no Jordan/Jones/Sylow-overgroup theorem verified")
