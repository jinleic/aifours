#!/usr/bin/env python3
"""Selected exact controls for the large-prime-power subgroup criterion."""

from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


for p, a in ((2, 19), (3, 12), (5, 9), (7, 7), (11, 6)):
    n = p**a
    assert n >= 500000 and 6*n >= 7*396738
    assert 156*n + 3*175 < 175*n
    r = n-4
    while not prime(r):
        r -= 1
    t = n-r
    assert r > 7 and 7*r > 6*n and t >= 4 and t < r
    power = p
    while power <= 7:
        power *= p
    for u in set((1, 2, 3, t//2, t)):
        if 1 <= u <= t:
            assert comb(n, u) % power == 0
    print(f"n={n}, p={p}, r={r}, t={t}, common-power={power}")
print("PASS: five selected exact controls only; prime-interval and Jordan theorems not verified")
