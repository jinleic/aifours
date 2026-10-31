#!/usr/bin/env python3
"""Finite integer controls for the 35-step 7-cell extension."""

from math import comb, gcd

worst = 0
for a in range(1, 15):
    if gcd(a, 15) != 1:
        continue
    r = 1500+a
    for t in range(1, 36):
        upper = 1 + sum((r+k) % 3 != 0 and (r+k) % 5 != 0 for k in range(2, t+1, 2))
        worst = max(worst, upper)
        assert upper <= 10
assert comb(420, 2) > 7*(419+35)
assert (419-2)*(419-3) > 7*(419+35)

for r in (419, 421, 431):
    for t in range(1, 36):
        cells = [h for h in range(1, t+1) if (r+h) % 7 == 0]
        assert len(cells) <= 5
        for left in range(1, t+1):
            for right in range(left, t+1):
                if any(h in cells for h in range(left, right+1)):
                    continue
                length = right-left+1
                assert length <= 6 and comb(r+right, length) % 7 != 0
    print(f"r={r}: every t<=35 seven-cell/window check PASS")
print(f"PASS: 8 mod-15 classes, t<=35, possible-prime upper bound={worst}")
print("Finite integer controls only; no actual subgroup classification verified")
