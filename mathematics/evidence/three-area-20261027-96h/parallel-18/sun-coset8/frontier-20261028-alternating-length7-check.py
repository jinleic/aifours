#!/usr/bin/env python3
"""Finite mod-72 controls for length-7 binomial parity/3 conflicts."""

from itertools import combinations
from math import comb, gcd

checked = odd_cases = 0
for a in range(1, 72):
    if gcd(a, 6) != 1:
        continue
    r = 72+a
    for endpoints in combinations(range(7, 42), 4):
        if len({j % 8 for j in endpoints}) != 1:
            continue
        checked += 1
        values = [comb(r+j, 7) for j in endpoints]
        if all(v % 2 for v in values):
            odd_cases += 1
            assert sum(v % 3 == 0 for v in values) >= 2
print(f"PASS: {checked} residue/endpoint cases, {odd_cases} all-odd cases checked")
print("Exact integer controls only; no global subgroup or P7 conclusion")
