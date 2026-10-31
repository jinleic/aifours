#!/usr/bin/env python3
"""Exact polynomial identities and bounded E8 primitive-prime controls.

No test establishes the external E8 maximal-overgroup classification.
"""
from math import gcd, isqrt


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def factor(n):
    result = []
    d = 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            result.append((d, e))
        d = 3 if d == 2 else d+2
    if n > 1:
        result.append((n, 1))
    return result


def evalpoly(a, x):
    return sum(c*x**i for i, c in enumerate(a))


phi30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]
phi2 = [1, 1]
phi6 = [1, -1, 1]
phi10 = [1, -1, 1, -1, 1]
rhs = [1]+[0]*14+[1]
if mul(mul(mul(phi2, phi6), phi10), phi30) != rhs:
    raise SystemExit("FAIL Phi30 polynomial factorization")
phi60 = [0]*17
for i, c in enumerate(phi30):
    phi60[2*i] = c
if mul(mul(mul([1,0,1], [1,0,-1,0,1]), [1,0,-1,0,1,0,-1,0,1]), phi60) != [1]+[0]*29+[1]:
    raise SystemExit("FAIL Phi60 polynomial factorization")
print("Phi30_Phi60_factorizations: PASS")
for x in range(2, 101):
    if gcd(evalpoly(phi30,x),30) != 1 or gcd(evalpoly(phi60,x),60) != 1:
        raise SystemExit("FAIL small-prime coprimality control")
print("gcd_controls_x2_to_100: PASS")
for f, ps in ((1,(2,3,5,7)), (2,(2,3,5))):
    for p in ps:
        val = evalpoly(phi30 if f == 1 else phi60, p)
        facts = factor(val)
        if any(pow(p,30*f,r) != 1 or
               any(pow(p,(30*f)//k,r) == 1 for k in (2,3,5))
               for r, _ in facts):
            raise SystemExit("FAIL primitive-order test")
        choices = [(r,e) for r,e in facts if r > 61 or e > 1]
        if not choices:
            raise SystemExit("FAIL E8 source-threshold alternative")
        print(f"f={f}, p={p}, Phi={val}, factors={facts}, source_candidate={choices[0]}")
print("PASS: exact bounded E8 primitive-order and source-threshold controls")
