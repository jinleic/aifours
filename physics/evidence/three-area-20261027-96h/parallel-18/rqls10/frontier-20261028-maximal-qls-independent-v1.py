#!/usr/bin/env python3
"""Check the generated 100 complex vectors at original QLS definition.

All arithmetic is exact on tenth-root exponent counts and Phi_10. This does
not claim a transversal or 1-resolvability.
"""
import json
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'frontier-20261028-butson-maximal-qls-result-v1.json').read_text())
A=D['exponents'];n=10
assert D['dimension']==n and len(A)==n and all(len(row)==n for row in A)
assert all(len(A[r][c])==n and all(isinstance(x,int) and 0<=x<n for x in A[r][c])
           for r in range(n) for c in range(n))


def inner_zero(x,y):
    counts=[0]*n
    for a,b in zip(x,y):counts[(b-a)%n]+=1
    v=[counts[j]-counts[j+5] for j in range(5)]
    return v[0]==-v[1]==v[2]==-v[3]==v[4]


def canonical(x):return tuple((a-x[0])%n for a in x)

# Each entry has unit magnitude divided by sqrt(10): every vector has norm1.
for r in range(n):
    for c,d in combinations(range(n),2):assert inner_zero(A[r][c],A[r][d])
for c in range(n):
    for r,s in combinations(range(n),2):assert inner_zero(A[r][c],A[s][c])
keys=[canonical(A[r][c]) for r in range(n) for c in range(n)]
assert len(set(keys))==100
for x,y in combinations(keys,2):assert x!=y
print('100 exact unit vectors and all20 row/column ONBs: PASS')
print('all4950 pairs of cells are projectively nonparallel: PASS')
print('actual maximal-cardinality QLS(10): VERIFIED over exact tenth roots')
print('NO 1-resolvability claimed; separate obstruction says no transversal')
