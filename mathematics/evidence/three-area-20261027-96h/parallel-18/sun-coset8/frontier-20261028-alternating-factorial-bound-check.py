#!/usr/bin/env python3
"""Finite residue controls for a written factorial-terminal exclusion."""

from math import comb, gcd

classes = [a for a in range(1, 15) if gcd(a, 15) == 1]
worst = 0
for a in classes:
    r = 1500+a
    for t in range(1, 34):
        offsets = range(2, t+1, 2)
        possible = 1 + sum((r+k) % 3 != 0 and (r+k) % 5 != 0 for k in offsets)
        worst = max(worst, possible)
        assert possible <= 10
    print(f"r mod 15={a:02d}, t<=33 upper bound PASS")
assert comb(420, 2) > 7*(419+33)
assert (419-2)*(419-3) > 7*(419+33)
print(f"PASS: 8 residue classes, t=1..33, worst possible-prime bound={worst}")
print("Residue arithmetic only; no actual subgroup or primality constellation asserted")
