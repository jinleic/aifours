#!/usr/bin/env python3
"""Exact sample controls for the degree-only Jordan/Dusart criterion."""

from math import comb, gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def factor(n):
    result = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            result.append((d, e))
        d += 1
    if n > 1:
        result.append((n, 1))
    return result


def criterion(n):
    y = n-4
    L = 0
    while 2*11**(L+1) < y*4**(L+1):
        L += 1
    den = 25*L*L
    T = 4+(y+den-1)//den
    D = 1
    for p, a in factor(n):
        exponent = 0
        power = p
        while power <= T:
            exponent += 1
            power *= p
        D *= p**max(0, a-exponent)
    return L, T, D


for n in (500000, 896000, 4000*100003):
    L, T, D = criterion(n)
    assert L >= 12 and 3599*(n-4) > 3600*396738
    r = n-5
    while not prime(r):
        r -= 1
    t = n-r
    assert 3 <= t < T < n//2 and D > 7
    assert all(comb(n, u) % D == 0 for u in range(1, t+1))
    print(f"n={n}, L={L}, T={T}, D={D}, selected r={r}, t={t}")
assert prime(100003) and criterion(4000*100003)[2] == 100003
print("PASS: three selected exact controls; no external theorem or subgroup result verified")
