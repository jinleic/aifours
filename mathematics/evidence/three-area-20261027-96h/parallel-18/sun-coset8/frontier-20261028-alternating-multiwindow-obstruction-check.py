#!/usr/bin/env python3
"""Finite controls for a formal multiwindow arithmetic obstruction at t=41."""

from math import comb, factorial, gcd, prod

windows = (((2, 3),), ((10, 10), (7, 8)), ((12, 17),),
           ((21, 24),), ((30, 32),), ((38, 38), (35, 36)))
modulus = 8*9*25*49*prod((11, 13, 17, 19, 23, 29, 31))


def numbers(r):
    return [7*r] + [prod(comb(r+b, b-a+1) for a, b in group) for group in windows]


def check(r):
    values = numbers(r)
    assert all(gcd(a, b) == 7 for i, a in enumerate(values) for b in values[i+1:])
    assert all(gcd(r, value) == 1 for value in values[1:])
    cells = [h for group in windows for a, b in group for h in range(a, b+1)]
    assert len(cells) == len(set(cells))
    for group in windows:
        seven = [h for a, b in group for h in range(a, b+1) if (r+h) % 7 == 0]
        assert len(seven) == 1
        assert group[-1][1]-group[-1][0]+1 >= 2
        for (_, high), (low_start, low_end) in zip(group, group[1:]):
            assert low_end <= high-2 and low_start <= low_end
    return values


r = 431
sample = check(r)
group_order = factorial(r+41)//2
assert all(group_order % value == 0 and value >= r+41 for value in sample)
check(r+modulus)
print(f"r={r}, values={sample}")
print(f"modulus={modulus}; representative and one translate satisfy exact arithmetic")
print("PASS: integer relaxation only; no actual subgroup, coset or all-prime theorem verified")
