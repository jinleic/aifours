#!/usr/bin/env python3
"""Finite no-point parity/3 window controls for fourteen steps."""

from functools import lru_cache
from itertools import combinations
from math import comb, factorial, isqrt


def prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def prime_power(n):
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        return n == 1
    for p in range(3, isqrt(n)+1, 2):
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


def find_prime(residue3):
    r = 7*factorial(14)+1
    while True:
        if r % 4 == 3 and r % 3 == residue3 and prime(r) and not excluded(r):
            return r
        r += 2


def packing(r):
    options = {i: [] for i in range(1, 15)}

    @lru_cache(None)
    def decompose(cells):
        if not cells:
            return (1,)
        start = cells[0]
        out = []
        for length in range(1, len(cells)+1):
            if cells[:length] != tuple(range(start, start+length)):
                break
            out.extend(comb(r+start+length-1, length)*v for v in decompose(cells[length:]))
        return tuple(out)

    for size in (2, 3, 4):
        for cells in combinations(range(1, 15), size):
            mask = sum(1 << (x-1) for x in cells)
            options[cells[0]].extend((mask, v) for v in decompose(cells))

    @lru_cache(None)
    def find(mask, remaining, evens, threes):
        if not remaining:
            return True
        if mask.bit_count() < 2*remaining:
            return False
        first = (mask & -mask).bit_length()
        if mask.bit_count() > 2*remaining and find(mask & ~(1 << (first-1)), remaining, evens, threes):
            return True
        for used, value in options[first]:
            e, z = evens+int(value % 2 == 0), threes+int(value % 3 == 0)
            if used & mask == used and e <= 1 and z <= 1 and find(mask & ~used, remaining-1, e, z):
                return True
        return False
    return find((1 << 14)-1, 6, 0, 0)


for b in (1, 2):
    r = find_prime(b)
    assert r+1 > 7*factorial(14) and (r+14) % 7 != 0 and not packing(r)
    print(f"r={r}, mod4=3, mod3={b}: necessary integer packing excluded")
print("PASS: two selected exact controls; no subgroup classification verified")
