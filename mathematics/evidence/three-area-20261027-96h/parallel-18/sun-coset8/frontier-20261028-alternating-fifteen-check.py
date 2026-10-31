#!/usr/bin/env python3
"""Small exact parity/3 controls for a fifteen-step residue-class argument."""

from functools import lru_cache
from itertools import combinations
from math import comb, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def prime_power(n):
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1 and prime(p)
    return prime(n)


def eligible(r):
    if not prime(r) or prime_power(r-1):
        return False
    d = 3
    while (1 << d)-1 <= r:
        for q in range(2, isqrt(r)+2):
            value = sum(q**j for j in range(d))
            if value > r:
                break
            if value == r and prime_power(q):
                return False
        d += 1
    return True


def no_point_packing(r):
    options = {i: [] for i in range(1, 16)}

    @lru_cache(None)
    def factors(cells):
        if not cells:
            return (1,)
        start = cells[0]
        out = []
        for length in range(1, len(cells)+1):
            if cells[:length] != tuple(range(start, start+length)):
                break
            out.extend(comb(r+start+length-1, length)*v for v in factors(cells[length:]))
        return tuple(out)

    for size in (2, 3, 4, 5):
        for cells in combinations(range(1, 16), size):
            mask = sum(1 << (x-1) for x in cells)
            options[cells[0]].extend((mask, v) for v in factors(cells))

    @lru_cache(None)
    def find(mask, count, evens, threes):
        if count == 0:
            return True
        if mask.bit_count() < 2*count:
            return False
        first = (mask & -mask).bit_length()
        if mask.bit_count() > 2*count and find(mask & ~(1 << (first-1)), count, evens, threes):
            return True
        for used, val in options[first]:
            e, z = evens+int(val % 2 == 0), threes+int(val % 3 == 0)
            if used & mask == used and e <= 1 and z <= 1 and find(mask & ~used, count-1, e, z):
                return True
        return False
    return find((1 << 15)-1, 6, 0, 0)


def point_packing(r):
    assert (r+15) % 7 == 0
    edges = [(j-1, j) for j in range(2, 15) if comb(r+j, 2) % 2]
    for chosen in combinations(edges, 3):
        cells = [x for edge in chosen for x in edge]
        if len(set(cells)) != 6:
            continue
        even_left = [x for x in range(2, 15, 2) if x not in cells]
        if len(even_left) != 4:
            continue
        a, b, c, d = even_left
        for pairs in (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))):
            vals = [comb(r+j, 2) for _, j in chosen]
            vals += [(r+i)*(r+j) for i, j in pairs]
            if sum(v % 3 == 0 for v in vals) <= 1:
                return True
    return False


for r in (139, 223, 439, 463):
    assert eligible(r) and r % 12 == 7 and not no_point_packing(r)
    if (r+15) % 7 == 0:
        assert not point_packing(r)
    print(f"r={r}: no-point relaxation excluded; point tested={((r+15)%7 == 0)}")
print("PASS: four selected exact controls below the theorem size bound; no subgroups enumerated")
