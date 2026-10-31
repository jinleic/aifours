#!/usr/bin/env python3
"""Exact mod-105 seven-cell counts for offsets 39..41."""

from math import gcd

classes = [a for a in range(1, 105) if gcd(a, 105) == 1]
for t, expected in ((39, 16), (40, 8), (41, 0)):
    selected = [a for a in classes
                if sum((a+h) % 7 == 0 for h in range(1, t+1)) <= 5]
    assert len(selected) == expected
    print(f"t={t}, classes={len(selected)}, residues={selected}")
print("PASS: exact residue count only; no group theorem or infinitude checked")
