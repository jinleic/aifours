#!/usr/bin/env python3
"""Finite parity/3 packing controls for the twelve-step written candidate."""

from functools import lru_cache
from itertools import combinations
from math import comb, factorial, isqrt, prod


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


def find_prime(a, b):
    r = 7*factorial(12)+1
    while True:
        if r % 7 == 2 and r % 4 == a and r % 3 == b and prime(r) and not excluded_repunit(r):
            return r
        r += 2


def no_point_pairing(r):
    @lru_cache(None)
    def find(mask, evens):
        if not mask:
            return True
        i = (mask & -mask).bit_length()
        for j in range(i+1, 13):
            if not mask & (1 << (j-1)):
                continue
            choices = [(r+i)*(r+j)]
            if j == i+1:
                choices.append(comb(r+j, 2))
            for value in choices:
                e = evens + int(value % 2 == 0)
                if e <= 1 and find(mask & ~(1 << (i-1)) & ~(1 << (j-1)), e):
                    return True
        return False
    return find((1 << 12)-1, 0)


def point_packing(r):
    assert (r+12) % 7 == 0 and (r+12) % 2 == 1 and (r+12) % 3 != 0
    options = {i: [] for i in range(1, 12)}
    for k in (2, 3):
        for cells in combinations(range(1, 12), k):
            values = [prod(r+x for x in cells)]
            if k == 2 and cells[1] == cells[0]+1:
                values.append(comb(r+cells[1], 2))
            if k == 3:
                if cells[1] == cells[0]+1:
                    values.append(comb(r+cells[1], 2)*(r+cells[2]))
                if cells[2] == cells[1]+1:
                    values.append((r+cells[0])*comb(r+cells[2], 2))
                if cells[1] == cells[0]+1 and cells[2] == cells[1]+1:
                    values.append(comb(r+cells[2], 3))
            mask = sum(1 << (x-1) for x in cells)
            options[cells[0]].extend((mask, v) for v in values)

    @lru_cache(None)
    def find(mask, remaining, evens, threes):
        if remaining == 0:
            return True
        if mask.bit_count() < 2*remaining:
            return False
        i = (mask & -mask).bit_length()
        if mask.bit_count() > 2*remaining and find(mask & ~(1 << (i-1)), remaining, evens, threes):
            return True
        for used, value in options[i]:
            e, z = evens+int(value % 2 == 0), threes+int(value % 3 == 0)
            if used & mask == used and e <= 1 and z <= 1 and find(mask & ~used, remaining-1, e, z):
                return True
        return False
    return find((1 << 11)-1, 5, 0, 0)


for a, b in ((1, 1), (1, 2), (3, 1), (3, 2)):
    r = find_prime(a, b)
    assert r+1 > 7*factorial(12) and not no_point_pairing(r) and not point_packing(r)
    print(f"r={r}, mod4={a}, mod3={b}: no-point and point integer packings excluded")
print("PASS: four selected finite controls only; no subgroup classification verified")
