#!/usr/bin/env python3
"""Exact finite interval packing with 2/3 conflicts; no subgroup enumeration."""

from functools import lru_cache
from math import comb, factorial, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def prime_power(n):
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1 and prime(p)
    return prime(n)


def excluded(r):
    if prime_power(r-1):
        return True
    d = 3
    while (1 << d)-1 <= r:
        q = 2
        while True:
            total = sum(q**j for j in range(d))
            if total > r:
                break
            if total == r and prime_power(q):
                return True
            q += 1
        d += 1
    return False


r = 7*factorial(11)+1
while not prime(r) or excluded(r):
    r += 1
assert r+1 > 7*factorial(11)
for t in (10, 11):
    @lru_cache(None)
    def maximum(j, mask, evens, threes):
        if j > t:
            return 0
        best = maximum(j+1, mask, evens, threes)
        for u in ((1,) if j == 1 else range(1, j+1)):
            window = sum(1 << (h-1) for h in range(j-u+1, j+1))
            value = r+1 if j == 1 else comb(r+j, u)
            e, z = int(value % 2 == 0), int(value % 3 == 0)
            if not mask & window and evens+e <= 1 and threes+z <= 1:
                best = max(best, 1+maximum(j+1, mask | window, evens+e, threes+z))
        return best

    answer = maximum(1, 0, 0, 0)
    assert answer <= 5
    print(f"eligible r={r}, t={t}, maximum disjoint typed windows={answer}")
print("PASS: selected exact integer control only; no source or subgroup proof verified")
