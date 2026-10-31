#!/usr/bin/env python3
"""Small exact alternating-family order controls, not subgroup classifications."""

from math import comb, factorial


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


for r in (11, 13, 19):
    assert prime(r)
    block_index = factorial(2*r) // (2*factorial(r)**2)
    assert block_index == comb(2*r, r)//2 and block_index > 7
    square_index = factorial(r*r) // (factorial(r)**r * factorial(r))
    assert square_index > 7
    print(f"r={r}, degree 2r wreath index={block_index}, square index positive")

r = 19
candidates = []
for d in range(2, 5):
    for q in range(2, r):
        total = sum(q**j for j in range(d))
        if total == r:
            candidates.append((q, d, prime_power(q)))
assert candidates == [(18, 2, False)]
assert sum(2**j for j in range(5)) > r
assert factorial(r)//(r*(r-1)) == factorial(r-2)
print("r=19: only integer geometric-sum candidate q=18,d=2 is not a prime power")
print("PASS: finite integer identities only; alternating subgroup theorem not checked")
