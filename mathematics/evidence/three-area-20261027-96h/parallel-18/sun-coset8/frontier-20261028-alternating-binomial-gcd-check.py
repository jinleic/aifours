#!/usr/bin/env python3
"""Exact finite controls for a written gcd-of-binomial-coefficients identity."""

from math import comb, factorial, gcd, lcm

checked = 0
for n in range(2, 101):
    running_gcd = 0
    running_lcm = 1
    for t in range(1, n):
        running_gcd = gcd(running_gcd, comb(n, t))
        running_lcm = lcm(running_lcm, t)
        assert running_gcd == n//gcd(n, running_lcm)
        checked += 1

n, r, t = 64, 53, 11
L = lcm(*range(1, t+1))
assert all(r % d for d in range(2, 8)) and n == r+t and t < r
assert n//gcd(n, factorial(t)) == 1
assert n//gcd(n, L) == 8
assert gcd(*(comb(n, u) for u in range(1, t+1))) == 8
print(f"PASS: {checked} finite (n,t) cases; A64 D_factorial=1, D_lcm=8")
print("Exact integers only; Jordan theorem and actual subgroups not checked")
