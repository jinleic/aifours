#!/usr/bin/env python3
"""Exact uniform support-graph counts and cyclotomic automorphism checks.

The graph is from Parker's published OLS table. It is not a physical lift.
"""
from collections import Counter
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
n=10
L=[[int(oa.PARKER_B[r][c]) for c in range(n)] for r in range(n)]
assert all(set(row)==set(range(n)) for row in L)
assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
cells=[(r,c) for r in range(n) for c in range(n)]

def adjacent(x,y):
    return x!=y and x[0]!=y[0] and x[1]!=y[1] and L[x[0]][x[1]]!=L[y[0]][y[1]]

neighbors={x:{y for y in cells if adjacent(x,y)} for x in cells}
assert {len(v) for v in neighbors.values()}=={72}
hist=Counter()
for x,y in combinations(cells,2):
    shared=len(neighbors[x]&neighbors[y])
    hist[(adjacent(x,y),shared)]+=1
assert hist=={(True,50):3600,(False,56):1350}
print('exact 100-cell support graph:',dict(sorted(hist.items())))
print('every nonzero Gram edge has 50 common triangle neighbors: PASS')

for q in range(1,257):
    N=lcm(q,8)
    candidates=[a for a in range(1,N+1) if gcd(a,N)==1 and a%q==1%q and a%8 in (3,5)]
    assert bool(candidates)==(q%8!=0),(q,candidates)
print('CRT automorphism existence checked q=1..256; iff 8 does not divide q: PASS')
print('Finite checks are corroboration; general field obstruction requires the written proof.')
