#!/usr/bin/env python3
"""Check non-Shor positive controls for all 12 proposed border cardinalities."""
from itertools import combinations
from math import gcd
import json
n=1320;choices=(12,15,20,22,24,30,33,40,44,55,60,66)
rows=[]
for d in choices:
    q=n//d;P=[i*q for i in range(d)];Q=list(range(q))
    sums=[(p+x)%n for p in P for x in Q]
    assert len(sums)==len(set(sums))==n
    GP={gcd(a-b,n) for a,b in combinations(P,2)}
    GQ={gcd(a-b,n) for a,b in combinations(Q,2)}
    assert not GP&GQ
    for prime in (3,5,11):
        vec=P if d%prime==0 else Q
        assert len(vec)%prime==0 and all(sum(x%prime==i for x in vec)==len(vec)//prime for i in range(prime))
    for k in (1,2,3):
        mod=2**k;half=mod//2
        balanced=lambda vec: all(sum(x%mod==r for x in vec)==sum(x%mod==r+half for x in vec) for r in range(half))
        assert balanced(P) or balanced(Q)
    rows.append({'P':d,'Q':q,'status':'valid non-Shor factorization'})
print(json.dumps({'controls':rows,'scope':'test of cardinality, gcd-class and Fourier constraints without Shor anchors'},indent=2))
