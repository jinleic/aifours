#!/usr/bin/env python3
"""Selected exact controls for the small-cofactor Jordan/Dusart family."""

from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


for p, a, m in ((2, 15, 25), (3, 11, 6), (5, 7, 20),
                (7, 6, 14), (100003, 1, 100)):
    assert prime(p)
    n = m*p**a
    power = p
    k = 1
    while power <= 7:
        power *= p
        k += 1
    assert n >= 500000 and m*p**(k-1) <= 100
    assert 100*(n-4) >= 101*396738 and n > 40000
    r = n-5
    while not prime(r):
        r -= 1
    t = n-r
    assert 101*r > 100*(n-4) and r < n-4 and 100*t < n
    assert r > 7 and 3 <= t < r
    assert all(comb(n, u) % power == 0 for u in range(1, t+1))
    print(f"n={n}, p={p}, m={m}, r={r}, t={t}, common-power={power}")
print("PASS: five selected exact controls; no prime-interval or subgroup theorem verified")
