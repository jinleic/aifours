#!/usr/bin/env python3
"""Bounded exact six-type P7 feasibility, without assuming subgroup existence."""

from itertools import combinations
from math import comb, gcd, lcm


def search(types, choices, selected):
    if not types:
        return selected
    j, *rest = types
    for u, value in choices[j]:
        index = lcm(7, value)
        if all(gcd(index, old_index) == 7 for _, _, old_index in selected):
            result = search(rest, choices, selected + [(j, u, index)])
            if result is not None:
                return result
    return None


for r in (419, 421, 431, 439):
    choices = {1: [(0, r+1)]}
    for j in range(2, 9):
        choices[j] = [(u, comb(r+j, u)) for u in range(1, j+1)]
    ds = [(r+j)//gcd(r+j, lcm(*range(1, j+1))) for j in range(1, 9)]
    if min(ds) <= 7:
        print(f"r={r} skipped: some d_j <=7, d={ds}")
        continue
    witness = None
    for subset in combinations(range(1, 9), 6):
        witness = search(list(subset), choices, [])
        if witness is not None:
            break
    print(f"r={r}, d={ds}, six-type integer witness={witness}")
print("Exact finite search only; a witness does not imply any subgroup exists")
