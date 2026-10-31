#!/usr/bin/env python3
"""Exact examples for the six-step alternating divisor collision."""

from math import gcd, isqrt, lcm


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n)+1):
        if n % d == 0:
            return False
    return True


def prime_power(n):
    for p in range(2, n+1):
        if prime(p) and n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return False


def divisors(r):
    return [(r+j)//gcd(r+j, lcm(*range(1, j+1))) for j in range(1, 7)]


for r in (419, 421, 431):
    assert prime(r)
    bad = []
    for exponent in range(2, 10):
        q = 2
        while sum(q**j for j in range(exponent)) <= r:
            if sum(q**j for j in range(exponent)) == r and prime_power(q):
                bad.append((q, exponent))
            q += 1
    assert not bad
    ds = divisors(r)
    if r % 4 == 1:
        assert ds[0] % 2 == ds[2] % 2 == 0
    if r % 8 == 3:
        assert ds[0] % 2 == ds[4] % 2 == 0
    print(f"r={r}, residue8={r%8}, d={ds}")

r = 431
ds = divisors(r)
assert all(gcd(a, b) == 1 for i, a in enumerate(ds) for b in ds[i+1:])
integers = [7*r] + [7*d for d in ds]
assert all(gcd(a, b) == 7 for i, a in enumerate(integers) for b in integers[i+1:])
print(f"r=431: integer-only seven-tuple {integers} has every pair gcd 7")
print("PASS: finite integer controls; no subgroup existence inferred")
