#!/usr/bin/env python3
"""Finite integer controls for the G2 source-conditional candidate."""

from math import gcd


def factors(n):
    found = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            found.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        found.append((n, 1))
    return found


def order(a, r):
    v = 1
    for i in range(1, r):
        v = v*a % r
        if v == 1:
            return i
    raise AssertionError((a, r))


def valuation(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
    a, b = p*p+p+1, p*p-p+1
    fa, fb = factors(a), factors(b)
    assert gcd(a, b) == 1 and valuation(a, 3) <= 1 and valuation(b, 3) <= 1
    assert all(r == 3 or order(p, r) == 3 for r, _ in fa)
    assert all(r == 3 or order(p, r) == 6 for r, _ in fb)
    assert any(r > 13 or (r == 13 and e > 1) for r, e in fa+fb)
    print(f"p={p}, Phi3={fa}, Phi6={fb}")
    c = p**4-p*p+1
    fc = factors(c)
    assert all(order(p, r) == 12 and order(p*p, r) == 6 for r, _ in fc)
    assert any(r > 13 or e > 1 for r, e in fc)

for p, fs in ((2, (3, 4)), (3, (2, 3, 4))):
    for f in fs:
        q = p**f
        candidates = [r for r, _ in factors(q*q-q+1) if order(p, r) == 6*f]
        assert candidates and candidates[0] > 7
        print(f"p={p}, f={f}, primitive={candidates[0]}")

l2_13 = 13*(13**2-1)//2
for q, max_orders, prime, expected in (
    (3, (2*3**3*(3**3-1)*(3**2-1), l2_13), 3, (3, 5)),
    (4, (2*4**3*(4**3+1)*(4**2-1), l2_13), 2, (5, 10)),
):
    g = q**6*(q**6-1)*(q**2-1)
    assert all(g % m == 0 for m in max_orders)
    indices = tuple(g//m for m in max_orders)
    assert tuple(valuation(n, prime) for n in indices) == expected
    print(f"G2({q}) candidate r13 indices={indices}, valuations={expected}")
assert (6048//216, 6048//168, 6048//96) == (28, 36, 63)
print("U3(3) maximal indices 28,36,63 all divisible by 28 or 9")
print("PASS: finite integer controls only; no subgroup classification computed")
