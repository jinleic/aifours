#!/usr/bin/env python3
"""Check original block constraints and 2-sparse partner argument exactly."""
import json
from itertools import combinations
from pathlib import Path
from collections import Counter
from math import gcd
from functools import reduce

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'frontier-20261028-coordinate-switch-result-v1.json').read_text())['partial_witness']
A=D['array']; L=D['labels']; den=D['denominator']; n=10
blocks=[[(r,c) for c in range(n)] for r in range(n)]
blocks += [[(r,c) for r in range(n)] for c in range(n)]
blocks += [[(r,c) for r in range(n) for c in range(n) if L[r][c]==t] for t in range(n)]
assert len(blocks)==30 and all(len(block)==n for block in blocks)


def ray(v):
    d=reduce(gcd,(abs(x) for x in v if x),0)
    out=tuple(x//d for x in v)
    first=next(x for x in out if x)
    return out if first>0 else tuple(-x for x in out)


def support(v): return tuple(i for i,x in enumerate(v) if x)

s=t=0
for r in range(n):
    for c in range(n):
        v=A[r][c]
        assert sum(x*x for x in v)==den**2
        supp=support(v)
        assert len(supp) in (1,2)
        if len(supp)==1:
            s+=1
            continue
        t+=1
        containing=[block for block in blocks if (r,c) in block]
        assert len(containing)==3
        partners=[]
        for block in containing:
            for x,y in combinations(block,2):
                assert sum(a*b for a,b in zip(A[x[0]][x[1]],A[y[0]][y[1]]))==0
            found=[q for q in block if q!=(r,c) and support(A[q[0]][q[1]])==supp]
            assert len(found)==1
            partners.append(found[0])
        assert len(set(partners))==3
        assert len({ray(A[x][y]) for x,y in partners})==1
rays=Counter(ray(A[r][c]) for r in range(n) for c in range(n))
bound=min(n,s)+t//3
print('actual singleton-support cells',s,'two-support cells',t)
print('every 2-support cell has three distinct parallel partner cells: PASS')
print('ray count',len(rays),'profile bound',bound,'uniform all-array bound',n+n*(n-1)//3)
print('ray multiplicity histogram',dict(sorted(Counter(rays.values()).items())))
assert len(rays)<=bound and bound<=n+n*(n-1)//3
