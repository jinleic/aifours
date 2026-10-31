#!/usr/bin/env python3
"""Exact sample of the P7-specific residual divisor, not subgroup verification."""

from math import comb, gcd, isqrt, lcm


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


n = 2143232
y = n-4
L = 0
while 2*11**(L+1) < y*4**(L+1):
    L += 1
T = 4+(y+25*L*L-1)//(25*L*L)
assert (L, T) == (13, 512)
assert n == 2**10 * 7 * 13 * 23
Q = 2
assert all(n % p == 0 and p <= T for p in (7, 13, 23))
assert 2**9 <= T < 2**10
assert Q <= 7 and 7 % Q != 0 and lcm(7, Q) == 14
r = n-5
while not prime(r):
    r -= 1
t = n-r
assert 3 <= t < T < n//2
assert all(comb(n, u) % Q == 0 for u in range(1, t+1))
print(f"n={n}, L={L}, T={T}, Q={Q}, selected r={r}, t={t}, lcm(7,Q)=14")
print("PASS: one exact integer example only; no source or subgroup theorem verified")
