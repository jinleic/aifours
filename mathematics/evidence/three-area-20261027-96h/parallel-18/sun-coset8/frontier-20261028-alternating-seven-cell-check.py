#!/usr/bin/env python3
"""Finite integer controls for the 7-cell and small-block quotient claims."""

from math import comb, factorial

for r in (419, 421, 431):
    for t in range(1, 34):
        cells = [h for h in range(1, t+1) if (r+h) % 7 == 0]
        assert len(cells) <= 5
        for left in range(1, t+1):
            for right in range(left, t+1):
                window = range(left, right+1)
                if any(h in cells for h in window):
                    continue
                length = right-left+1
                assert length <= 6
                assert factorial(length) % 7 != 0
                assert comb(r+right, length) % 7 != 0
    print(f"r={r}: all t<=33 seven-cell and 7-free-window checks PASS")

m = 8
for u in range(2, 10):
    n = m+u
    group = factorial(n)//2
    big = factorial(m)//2
    small = factorial(u)//2
    block = factorial(m)*factorial(u)//2
    for h, c in ((block, 1), (big*small, 2), (big, factorial(u))):
        assert group % h == 0
        assert group//h == comb(n,u)*c and factorial(u) % c == 0
print("u=2..9: exact full-block, alternating-block and pointwise-block index examples PASS")
print("Finite integer controls only; no arbitrary subgroup enumeration or proof")
