#!/usr/bin/env python3
"""Exact original-vector ray distinctness for Fourier10 × explicit BH10,5."""
import importlib.util
from itertools import combinations
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('b',ROOT/'frontier-20261028-butson10-half-matching-v1.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b);b.validate()
n=10
# zeta5=zeta10². A vector is a 10-tuple of exponents modulo10.
def exponent(r,c,t):return (r*t+2*b.K[t][c])%10

def raykey(r,c):
    values=[exponent(r,c,t) for t in range(n)]
    return tuple((x-values[0])%10 for x in values)

keys={(r,c):raykey(r,c) for r in range(n) for c in range(n)}
hist=Counter(keys.values())
print('BH10 exact row and column character checks: PASS')
print('actual vector rays',len(hist),'of100; multiplicity histogram',dict(sorted(Counter(hist.values()).items())))
print('parallel unordered pairs',sum(v*(v-1)//2 for v in hist.values()),'of4950')
# For any two distinct physical rows/cells, verify zero inner-product on row
# or column via exact coefficient sum in Q(zeta10).
coef=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,1,-1,1),
      (-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1),(1,-1,1,-1))
for r in range(n):
    for c,d in combinations(range(n),2):
        v=[sum(coef[(exponent(r,d,t)-exponent(r,c,t))%10][i] for t in range(n)) for i in range(4)]
        assert v==[0]*4
for c in range(n):
    for r,s in combinations(range(n),2):
        v=[sum(coef[(exponent(s,c,t)-exponent(r,c,t))%10][i] for t in range(n)) for i in range(4)]
        assert v==[0]*4
print('all20 actual row/column ONBs exact cyclotomic arithmetic: PASS')
print('no resolution claimed; separately proved transversal gap for this K')
