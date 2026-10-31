#!/usr/bin/env python3
"""Direct exact Q(i sqrt 7) verifier of the two-ONB fragment JSON."""
import json
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'frontier-20261028-gf9-conference-result-v1.json').read_text())
A=D['basis1']; B=D['basis2']; den=8
assert len(A)==len(B)==10 and all(len(v)==10 for v in A+B)

def mul(x,y):
    a,b=x; c,d=y
    return (a*c-7*b*d,a*d+b*c)

def subtract(x,y): return (x[0]-y[0],x[1]-y[1])

def conj(x): return (x[0],-x[1])

def dot(v,w):
    vals=[mul(conj(x),y) for x,y in zip(v,w)]
    return (sum(x[0] for x in vals),sum(x[1] for x in vals))

def parallel(v,w):
    return all(subtract(mul(v[i],w[j]),mul(v[j],w[i]))==(0,0)
               for i,j in combinations(range(10),2))

for basis in (A,B):
    for i,x in enumerate(basis):
        for j,y in enumerate(basis):
            assert dot(x,y)==((den**2,0) if i==j else (0,0))
assert parallel(A[0],B[0])
for i in range(10):
    for j in range(1,10):
        x,y=dot(A[i],B[j])
        squared=x*x+7*y*y
        assert squared==(0 if i==0 or i==j else den**4//8)
rays=A+B[1:]
assert len(rays)==19
assert all(not parallel(x,y) for x,y in combinations(rays,2))
print('exact field check: Q(i sqrt 7) using integer-pair arithmetic')
print('two ONBs: all 200 ordered inner products exact; one shared basis ray')
print('cross basis: two zero coordinates and eight squared overlaps 1/8 each')
print('all 171 distinct-ray pairs nonparallel: PASS; actual rays 19')
print('scope: 2 ONB blocks only; NOT a 100-ray resolvable QLS')
