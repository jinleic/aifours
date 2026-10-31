#!/usr/bin/env python3
"""Finite 7-adic controls for the six-cell saturation boundary."""

from math import comb, factorial


def valuation(n, p=7):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


for r in (419, 421, 431):
    t = 41
    cells = [h for h in range(1, t+1) if (r+h) % 7 == 0]
    assert len(cells) == 6
    checked = 0
    for left in range(1, t+1):
        for right in range(left, t+1):
            local = [h for h in cells if left <= h <= right]
            if len(local) != 1:
                continue
            u = right-left+1
            assert u <= 13 and valuation(factorial(u)) == (1 if u >= 7 else 0)
            assert valuation(comb(r+right, u)) == valuation(r+local[0])-valuation(factorial(u))
            checked += 1
    print(f"r={r}, 7-cells={cells}, single-cell windows checked={checked}")
print("PASS: finite exact 7-adic arithmetic only; no subgroup or existence conclusion")
