#!/usr/bin/env python3
"""Exact bounded controls for the twisted-E6 degree-18 argument."""
from math import gcd


def factor(n):
    out = []
    d = 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            out.append((d,e))
        d = 3 if d == 2 else d+2
    if n > 1:
        out.append((n,1))
    return out


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


f=[1,0,0,-1,0,0,1]
if poly_mul([1,0,0,1],f) != [1]+[0]*8+[1]:
    raise SystemExit("FAIL polynomial factorization")
print("x9_plus_1_factorization: PASS")
for x in range(2,101):
    value=x**6-x**3+1
    if value % 2 == 0 or value % 9 == 0:
        raise SystemExit("FAIL nonprimitive prime bound")
print("v2_zero_and_v3_at_most_one_x2_to_100: PASS")
for p in (2,3,5,7,11):
    value=p**6-p**3+1
    fs=factor(value)
    for r,_ in fs:
        if r==3:
            continue
        if pow(p,18,r)!=1 or pow(p,9,r)==1 or pow(p,6,r)==1:
            raise SystemExit("FAIL primitive order18")
    choices=[(r,e) for r,e in fs if r!=3 and (r>19 or e>1)]
    if p==2 and fs==[(3,1),(19,1)]:
        result="source quadratic-residue exception"
    elif choices:
        result=f"source threshold {choices[0]}"
    else:
        raise SystemExit("FAIL no source alternative")
    print(f"p={p}, Phi18={value}, factors={fs}, result={result}")
print("PASS: bounded twisted-E6 primitive-source alternatives")
