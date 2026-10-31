#!/usr/bin/env python3
"""Finite integer controls for the alternating orbit-induction candidate."""

from math import comb, factorial, gcd, lcm


def prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_power(n):
    if n < 2:
        return False
    for p in range(2, n+1):
        if prime(p) and n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return False


r = 419
assert prime(r)
candidates = []
for d in range(2, 9):
    for q in range(2, r):
        value = sum(q**j for j in range(d))
        if value == r:
            candidates.append((q, d, prime_power(q)))
        if value > r:
            break
assert sum(2**j for j in range(9)) > r
assert candidates == [(418, 2, False)]
assert factorial(r-2) % (r+1) == 0
print("r=419 prime; only geometric-sum candidate q=418,d=2 is not a prime power")

for j in range(1, 7):
    n = r+j
    bound = lcm(*range(1, j+1))
    divisor = n // gcd(n, bound)
    assert divisor > 7
    for u in range(1, j+1):
        assert comb(n, u) % divisor == 0
    print(f"j={j}, n={n}, lcm={bound}, common divisor={divisor}")
print("PASS: selected binomial controls only; no subgroup classification verified")
