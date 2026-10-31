#!/usr/bin/env python3
"""Finite prime-order examples and exact exceptional-group index arithmetic."""

from math import gcd


def factors(n):
    found = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        found.append(n)
    return found


def order(a, r):
    x = 1
    for i in range(1, r):
        x = x * a % r
        if x == 1:
            return i
    raise AssertionError((a, r))


for f in (3, 5, 7):
    for name, p, exponent in (("Suzuki", 2, 4), ("small-Ree", 3, 6),
                               ("large-Ree", 2, 12)):
        q = p**f
        cyclo = {4: q*q + 1, 6: q*q - q + 1,
                 12: q**4 - q*q + 1}[exponent]
        candidates = [r for r in factors(cyclo) if order(p, r) == exponent*f]
        assert candidates
        r = candidates[0]
        assert r > 7 and order(q, r) == exponent
        for k in factors(f):
            assert pow(p, (exponent//2)*f//k, r) != r - 1
        print(f"{name}: f={f} q={q} primitive_r={r}")

tits = 2**11 * 3**3 * 5**2 * 13
psl3_3_times_2 = 2 * 3**3 * (3**3 - 1) * (3**2 - 1)
psl2_25 = 25 * (25**2 - 1) // 2
assert tits % psl3_3_times_2 == tits % psl2_25 == 0
indices = (tits // psl3_3_times_2, tits // psl2_25)
assert indices == (1600, 2304) and gcd(*indices) == 64
print(f"Tits exceptional r=13: overgroup indices={indices}, gcd=64")

psl2_8 = 504
maximal_orders = (56, 18, 14)
indices = tuple(psl2_8 // m for m in maximal_orders)
assert indices == (9, 28, 36) and 9 % 9 == 36 % 9 == 0
print(f"PSL2(8) max indices={indices}, every one divisible by 9 or 28")
print("PASS: integer examples only; maximal-subgroup claims remain source imports")
