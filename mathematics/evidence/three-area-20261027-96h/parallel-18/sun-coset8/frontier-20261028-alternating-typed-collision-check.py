#!/usr/bin/env python3
"""Exact selected controls for typed binomial alternatives, not subgroup enumeration."""

from math import comb, gcd

for r in (419, 421, 431):
    b1 = r+1
    b2 = [comb(r+2, u) for u in (1, 2)]
    b3 = [comb(r+3, u) for u in (1, 2, 3)]
    assert b1 % 2 == 0
    assert all(x % (r+2) == 0 for x in b2)
    assert b3[0] % 2 == b3[2] % 2 == 0
    assert b3[1] % (r+2) == 0
    print(f"r={r}, type2={b2}, type3={b3}")

r = 431
d = [432, 433, 217, 145, 109, 437]
old_numbers = [7*r] + [7*x for x in d]
assert all(gcd(x, y) == 7 for i, x in enumerate(old_numbers) for y in old_numbers[i+1:])
bucket3_number = 7*d[2]
assert all(bucket3_number % comb(r+3, u) != 0 for u in (1, 2, 3))
print(f"r=431: old coarse-bucket number {bucket3_number} fails all type3 binomial alternatives")
print("PASS: selected exact integer identities only; no subgroup classifications verified")
