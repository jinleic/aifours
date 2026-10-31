#!/usr/bin/env python3
"""Independently check actual rational vectors/labels in a JSON certificate.

Accepts the coordinate-search JSON's `partial_witness` object. All arithmetic
is integer; exact orthogonality and projective nonparallelism are checked.
"""
import json
from itertools import combinations
from pathlib import Path
import sys

p=Path(sys.argv[1]) if len(sys.argv)>1 else Path('frontier-20261028-coordinate-switch-result-v1.json')
data=json.loads(p.read_text())['partial_witness']
if data is None:
    raise ValueError('no partial witness in certificate')
arr=data['array']
labels=data['labels']
den=data['denominator']
n=10
assert isinstance(den,int) and den>0
assert len(arr)==len(labels)==n and all(len(row)==n for row in arr+labels)
for row in arr:
    for v in row:
        assert len(v)==n and all(isinstance(x,int) for x in v)
        assert sum(x*x for x in v)==den*den
expected=set(range(n))
assert all(set(row)==expected for row in labels)
assert all({labels[r][c] for r in range(n)}==expected for c in range(n))
blocks=[[(r,c) for c in range(n)] for r in range(n)]
blocks += [[(r,c) for r in range(n)] for c in range(n)]
blocks += [[(r,c) for r in range(n) for c in range(n) if labels[r][c]==t] for t in range(n)]
assert len(blocks)==30
for block in blocks:
    assert len(block)==10
    for (r,c),(s,d) in combinations(block,2):
        assert sum(x*y for x,y in zip(arr[r][c],arr[s][d]))==0
cells=[(r,c) for r in range(n) for c in range(n)]

def parallel(v,w):
    return all(v[i]*w[j]==v[j]*w[i] for i in range(n) for j in range(i+1,n))

# Pairwise exact, with no dependence on the creator's canonicalization logic.
classes=[]
for r,c in cells:
    v=arr[r][c]
    if not any(parallel(v,w) for w in classes):
        classes.append(v)
parallel_pair_count=sum(parallel(arr[r][c],arr[s][d]) for (r,c),(s,d) in combinations(cells,2))
assert len(classes)==data['ray_count']
print('exact norm check: 100/100, denominator',den)
print('exact orthogonality: 30/30 original row/column/transversal blocks')
print('label incidence: 10 disjoint row/column transversals')
print('exact distinct projective rays:',len(classes),'of 100')
print('exact parallel unordered cell pairs:',parallel_pair_count,'of 4950')
print('is maximal cardinality:',len(classes)==100)
