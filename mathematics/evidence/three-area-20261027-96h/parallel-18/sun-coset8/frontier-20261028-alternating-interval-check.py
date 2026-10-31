#!/usr/bin/env python3
"""Selected exact eligible-prime and interval-packing controls."""

from functools import lru_cache
from math import comb, factorial, gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def prime_power(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1 and prime(p)
    return prime(n)


def excluded_repunit(r):
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


t = 9
r = 7*factorial(t)+1
while not prime(r) or excluded_repunit(r):
    r += 1
assert prime(r) and not excluded_repunit(r) and r+1 > 7*factorial(t)


@lru_cache(None)
def maximum(j, mask, evens):
    if j > t:
        return 0
    best = maximum(j+1, mask, evens)
    for u in ((1,) if j == 1 else range(1, j+1)):
        window = sum(1 << (h-1) for h in range(j-u+1, j+1))
        value = r+1 if j == 1 else comb(r+j, u)
        extra = int(value % 2 == 0)
        if not mask & window and evens + extra <= 1:
            best = max(best, 1+maximum(j+1, mask | window, evens+extra))
    return best


limit = maximum(1, 0, 0)
assert limit <= t//2+1
assert all((r+h)//gcd(r+h, factorial(t)) > 7 for h in range(1, t+1))
print(f"eligible r={r}, t={t}, max_disjoint_windows_with_at_most_one_even={limit}")
print("PASS: one exact integer example only; no subgroup classification verified")
