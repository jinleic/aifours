#!/usr/bin/env python3
"""Exact all-parameter compatibility and gauge-direction rank for one q6 family."""
from itertools import combinations
from fractions import Fraction as Q
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'][0]
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
M=[[[int(t in f['rows'] and c in f['columns']) for c in range(10)]for t in range(10)]for f in D['rectangles']]
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
for r,s in combinations(range(10),2):
 bins={}
 for c in range(10):bins.setdefault(tuple(x[r][c]-x[s][c] for x in M),[]).append(H[r][c]-H[s][c])
 assert all(zero(v) for v in bins.values())
A=[[Q(x[r][c]-x[r][0]-x[0][c]+x[0][0]) for x in M]for r in range(1,10)for c in range(1,10)]
rank=0
for c in range(4):
 pivot=next((r for r in range(rank,len(A)) if A[r][c]),None)
 if pivot is None:continue
 A[rank],A[pivot]=A[pivot],A[rank];v=A[rank][c];A[rank]=[x/v for x in A[rank]]
 for r in range(len(A)):
  if r!=rank:
   v=A[r][c];A[r]=[x-v*y for x,y in zip(A[r],A[rank])]
 rank+=1
assert rank==4
print('PASS all Laurent coefficients of every row pair vanish; four mask signatures have rank',rank)
print('This validates one literal family only; no complete classification claimed.')
