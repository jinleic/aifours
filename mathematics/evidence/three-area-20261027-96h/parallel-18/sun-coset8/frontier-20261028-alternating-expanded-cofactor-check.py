#!/usr/bin/env python3
"""Exact sample controls for the 3500-cofactor Jordan/Dusart family."""

from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


assert 11**12 < 396738*4**12
for p, a, m in ((2, 10, 875), (3, 6, 1166), (5, 5, 700),
                (7, 6, 500), (100003, 1, 3500)):
    assert prime(p)
    n = m*p**a
    power = p
    k = 1
    while power <= 7:
        power *= p
        k += 1
    assert n >= 500000 and m*p**(k-1) <= 3500
    assert 3600*(n-4) >= 3601*396738 and 101*n > 50400000
    r = n-5
    while not prime(r):
        r -= 1
    t = n-r
    assert 3601*r > 3600*(n-4) and r < n-4 and 3500*t < n
    assert r > 7 and 3 <= t < r
    assert all(comb(n, u) % power == 0 for u in range(1, t+1))
    print(f"n={n}, p={p}, m={m}, r={r}, t={t}, common-power={power}")
print("PASS: five exact controls; no external theorem or subgroup classification verified")
