#!/usr/bin/env python3
"""Independent direct definition check for Parker13-oriented float arrays."""
import json
from itertools import combinations
from pathlib import Path
import sys
import numpy as np

root=Path(__file__).resolve().parent
L=json.loads((root/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']['labels']
v=np.load(sys.argv[1],allow_pickle=False)
n=10
assert v.shape==(n,n*n) and np.isfinite(v).all()
assert all(set(row)==set(range(n)) for row in L)
assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
blocks=[[(r,c) for c in range(n)] for r in range(n)]
blocks += [[(r,c) for r in range(n)] for c in range(n)]
blocks += [[(r,c) for r in range(n) for c in range(n) if L[r][c]==t] for t in range(n)]
assert len(blocks)==30 and all(len(b)==n for b in blocks)
norm=max(float(abs(np.vdot(v[:,x],v[:,x])-1)) for x in range(100))
worst=(0.0,None)
for b,block in enumerate(blocks):
    for (r,c),(s,d) in combinations(block,2):
        val=float(abs(np.vdot(v[:,10*r+c],v[:,10*s+d])))
        if val>worst[0]:worst=(val,(b,(r,c),(s,d)))
near=0; max_pair=0.0
for x,y in combinations(range(100),2):
    denom=np.linalg.norm(v[:,x])*np.linalg.norm(v[:,y])
    val=float(abs(np.vdot(v[:,x],v[:,y]))/denom)
    max_pair=max(max_pair,val)
    if val>=1-1e-8:near+=1
print('all100 max norm error',norm)
print('all30 blocks worst offdiagonal',worst)
print('all4950 pairs max normalized overlap',max_pair,'near-parallel tolerance1e-8',near)
print('numerically feasible at1e-10',norm<1e-10 and worst[0]<1e-10 and near==0)
print('floating-point exploratory check only, not exact/rigorous certification')
