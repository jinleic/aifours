#!/usr/bin/env python3
"""Exact 96-class P7 necessary-condition DP; no group enumeration.

Every option is any disjoint interval decomposition of 2..4 positions.
Flags record divisibility of its binomial product by 2, 3 and 5.
A successful search would be six disjoint options with no repeated flag.
"""

from functools import lru_cache
from itertools import combinations
from math import comb, gcd


def check(residue):
    r = 360 + residue
    options = [set() for _ in range(14)]

    @lru_cache(None)
    def products(cells):
        if not cells:
            return (1,)
        start = cells[0]
        out = []
        for length in range(1, len(cells)+1):
            if cells[:length] != tuple(range(start, start+length)):
                break
            factor = comb(r+start+length-1, length)
            out.extend(factor*v for v in products(cells[length:]))
        return tuple(out)

    for size in (2, 3, 4):
        for cells in combinations(range(1, 15), size):
            mask = sum(1 << (x-1) for x in cells)
            for value in products(cells):
                flags = sum((1 << i) for i, p in enumerate((2, 3, 5)) if value % p == 0)
                options[cells[0]-1].add((mask, flags))
    options = [tuple(sorted(group)) for group in options]

    @lru_cache(None)
    def search(available, remaining, used_flags):
        if remaining == 0:
            return True
        if available.bit_count() < 2*remaining:
            return False
        first = (available & -available).bit_length()-1
        if available.bit_count() > 2*remaining:
            if search(available & ~(1 << first), remaining, used_flags):
                return True
        for used, flags in options[first]:
            if used & available == used and not flags & used_flags:
                if search(available & ~used, remaining-1, used_flags | flags):
                    return True
        return False

    witness = search((1 << 14)-1, 6, 0)
    return witness, search.cache_info().currsize


classes = [a for a in range(1, 360) if gcd(a, 30) == 1]
assert len(classes) == 96
states = 0
for a in classes:
    witness, seen = check(a)
    assert not witness, f"arithmetic relaxation has a six-label witness at r mod 360 = {a}"
    states += seen
    print(f"residue={a:03d} states={seen} PASS")
print(f"PASS: 96 residue classes, {states} memoized search states; no subgroup enumeration")
