#!/usr/bin/env python3
"""Exact necessary-condition DP for all 480 prime residue classes modulo 1800.

No-point: six groups of at least two cells in 1..15.
Point: cell 15 occupied by the even top-point index; five further groups.
Groups are arbitrary interval decompositions, with 2/3/5 flags.
"""

from functools import lru_cache
from itertools import combinations
from math import comb, gcd


@lru_cache(None)
def decompositions(cells):
    if not cells:
        return ((),)
    start = cells[0]
    result = []
    for length in range(1, len(cells)+1):
        if cells[:length] != tuple(range(start, start+length)):
            break
        for rest in decompositions(cells[length:]):
            result.append(((start+length-1, length),) + rest)
    return tuple(result)


groups = []
for size in range(2, 7):
    for cells in combinations(range(1, 16), size):
        mask = sum(1 << (x-1) for x in cells)
        groups.append((cells[0]-1, mask, decompositions(cells)))


def check(residue):
    r = 1800 + residue
    interval_flags = {}
    for end in range(1, 16):
        for length in range(1, min(end, 6)+1):
            value = comb(r+end, length)
            interval_flags[(end, length)] = sum(
                (1 << i) for i, p in enumerate((2, 3, 5)) if value % p == 0
            )

    option_sets = [set() for _ in range(15)]
    for first, mask, decomps in groups:
        for decomp in decomps:
            flags = 0
            for interval in decomp:
                flags |= interval_flags[interval]
            option_sets[first].add((mask, flags))
    options = [tuple(sorted(group)) for group in option_sets]

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

    no_point = search((1 << 15)-1, 6, 0)
    no_point_states = search.cache_info().currsize
    search.cache_clear()
    point = search((1 << 14)-1, 5, 1)
    point_states = search.cache_info().currsize
    return no_point, point, no_point_states, point_states


classes = [a for a in range(1, 1800) if gcd(a, 30) == 1]
assert len(classes) == 480
states_no_point = states_point = 0
for i, a in enumerate(classes, 1):
    no_point, point, sn, sp = check(a)
    assert not no_point, f"no-point relaxation has witness at r mod 1800 = {a}"
    assert not point, f"point relaxation has witness at r mod 1800 = {a}"
    states_no_point += sn
    states_point += sp
    if i % 60 == 0:
        print(f"classes={i}, no_point_states={states_no_point}, point_states={states_point} PASS")
print(f"PASS: {len(classes)} classes, no-point states={states_no_point}, point states={states_point}; no subgroup enumeration")
