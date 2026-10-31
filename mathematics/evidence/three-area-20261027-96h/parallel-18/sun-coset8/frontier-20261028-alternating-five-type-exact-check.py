#!/usr/bin/env python3
"""Exact minimal P7 multiples for typed alternatives; no subgroups enumerated."""

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
            minima = [lcm(7, value) for value in values]
            assert any(gcd(a, b) > 7
                       for i, a in enumerate(minima) for b in minima[i+1:])
    print(f"r={r}, exact minimal 7-multiple choices checked={checked}")
print("PASS: exact lcm controls only; no subgroup or general theorem verified")
