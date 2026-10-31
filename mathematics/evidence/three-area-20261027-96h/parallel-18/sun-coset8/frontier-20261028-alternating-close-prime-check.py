#!/usr/bin/env python3
"""Exact finite controls for close-prime binomial pair collision."""

from math import comb, factorial, gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


pairs = 0
for n in range(22, 201):
    t = (n-1)//7
    assert n > 7*t
    for i in range(1, t+1):
        a = comb(n, i)
        assert a > 7
        for j in range(i+1, t+1):
            b = comb(n, j)
            bridge = comb(j, i)
            assert a*comb(n-i, j-i) == b*bridge
            assert a > 7*bridge and gcd(a, b) > 7
            pairs += 1

n = 510510
assert n == 2*3*5*7*11*13*17
r = n-4
while not prime(r):
    r -= 1
t = n-r
assert r > 7 and 7*r > 6*n and 3 <= t < r
for i in range(1, t+1):
    for j in range(i+1, t+1):
        assert gcd(comb(n, i), comb(n, j)) > 7
assert gcd(n, factorial(146)) == n
print(f"PASS: {pairs} finite small pairs; smooth example n={n}, r={r}, t={t}, factorial-residual=1")
print("Exact integer controls only; Dusart, Jordan and actual subgroup claims not verified")
