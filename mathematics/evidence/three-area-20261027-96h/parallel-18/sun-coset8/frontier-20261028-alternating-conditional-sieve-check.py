#!/usr/bin/env python3
"""Exact mod-105 reproduction of parent sieve and seven-cell enlargement."""

from math import comb, gcd

expected = {36: (38, 40), 37: (30, 32), 38: (23, 24)}
classes = [a for a in range(1, 105) if gcd(a, 105) == 1]
assert len(classes) == 48
for t in (36, 37, 38):
    cell_classes = []
    sieve_classes = []
    for a in classes:
        cells = sum((a+h) % 7 == 0 for h in range(1, t+1))
        possible = 1 + sum(all((a+k) % p != 0 for p in (3, 5, 7))
                           for k in range(2, t+1, 2))
        if cells <= 5:
            cell_classes.append(a)
            if possible <= 10:
                sieve_classes.append(a)
    assert (len(sieve_classes), len(cell_classes)) == expected[t]
    extra = sorted(set(cell_classes)-set(sieve_classes))
    print(f"t={t}, parent_joint={len(sieve_classes)}, seven_cell_only={len(cell_classes)}, extra={extra}")
assert comb(420, 2) > 7*(419+38)
assert (419-2)*(419-3) > 7*(419+38)
print("PASS: exact residue/count controls only; no subgroup or prime infinitude proof")
