#!/usr/bin/env python3
"""Selected integer control for the six saturated 7-local windows at t=41."""

from math import comb, gcd, isqrt


def valuation(n, p=7):
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


r = 251
assert all(r % d for d in range(2, isqrt(r)+1)) and r % 49 == 6
windows = [(1+7*i, 7+7*i) for i in range(5)] + [(36, 41)]
indices = []
for i, (left, right) in enumerate(windows):
    u = right-left+1
    cells = [h for h in range(left, right+1) if (r+h) % 7 == 0]
    assert len(cells) == 1 and valuation(r+cells[0]) == 1
    c = 7 if i < 5 else 1
    n = comb(r+right, u)*c
    assert valuation(n) == 1
    indices.append(n)
conflicts = [(i, j, gcd(a, b)) for i, a in enumerate(indices)
             for j, b in enumerate(indices[i+1:], i+1) if gcd(a, b) > 7]
assert conflicts
print(f"r={r}, windows={windows}, all local 7-valuations=1")
print(f"pairs with extra non-7 common factors={len(conflicts)}")
print("PASS: selected 7-local arithmetic only; no global subgroup or P7 realization")
