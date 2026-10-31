#!/usr/bin/env python3
"""Exact n=10 formal uniform-overlap incidence identities.

This checks only M*, not existence of any physical rank-one-projector lift.
"""
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('published',ROOT/'frontier-20261028-ols10-switch-v1.py')
published=importlib.util.module_from_spec(spec)
spec.loader.exec_module(published)
published.check_table()
n=10
cells=[(r,c) for r in range(n) for c in range(n)]


def shares(x,y):
    r,c=x; s,d=y
    return r==s or c==d or published.TABLE[r][c][1]==published.TABLE[s][d][1]


# B=(n-2)M*: integer diagonal8, forced zeros, all other entries1.
B=[[n-2 if x==y else 0 if shares(x,y) else 1 for y in cells] for x in cells]
assert all(sum(row)==n*(n-2) for row in B)
for i in range(n*n):
    for j in range(n*n):
        left=sum(B[i][k]*B[k][j] for k in range(n*n))
        right=n*B[i][j]+(n-2)*(n-3)
        assert left==right,(i,j,left,right)
forced=[sum(1 for j,y in enumerate(cells) if j!=i and shares(x,y)) for i,x in enumerate(cells)]
assert set(forced)=={3*(n-1)}
numerator=n*n*(n-2); denominator=2*n-3
minimum=(numerator+denominator-1)//denominator
print('exact OLS incidence: PASS; 100 cells, 3 partitions, 27 forced-zero neighbors per cell')
print('exact integer identity: B^2=10B+56J, B1=80*1; PASS for all 10000 entries')
print('formal M* eigenvalues: 10 (1), 5/4 (72), 0 (27); follows from identity and trace')
print('conditional physical hyperplane support bound ceil(800/17)=',minimum)
print('formal M* is NOT evidence of a physical lift')
