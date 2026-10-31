#!/usr/bin/env python3
"""Finite checks of typed alternatives, not a subgroup enumeration."""

from itertools import combinations, product
from math import comb, gcd, lcm

for r in (419, 421, 431):
    options = {1: [r+1]}
    for j in range(2, 6):
        options[j] = [comb(r+j, u) for u in range(1, j+1)]
    checked = 0
    for types in combinations(range(1, 6), 4):
        for values in product(*(options[j] for j in types)):
            checked += 1
            assert any(gcd(7*a, 7*b) > 7
                       for i, a in enumerate(values) for b in values[i+1:])
    d7 = (r+7) // gcd(r+7, lcm(*range(1, 8)))
    assert d7 > 7
    print(f"r={r}, tested={checked} first-five-type choices, d7={d7}")
print("PASS: selected exact binomial controls only; no subgroup or source theorem checked")
