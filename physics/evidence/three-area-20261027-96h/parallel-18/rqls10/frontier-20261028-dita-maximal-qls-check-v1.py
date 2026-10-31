#!/usr/bin/env python3
"""Independent original-vector verifier plus exact exhaustive transversal search."""
from itertools import combinations
from pathlib import Path
import json
D=json.loads((Path(__file__).resolve().parent/'frontier-20261028-dita-maximal-qls-result-v1.json').read_text())
A=D['exponents'];n=10
assert D['dimension']==10 and D['normalization']=='1/sqrt(10)'
assert len(A)==10 and all(len(row)==10 for row in A)
assert all(len(x)==10 and all(type(z)==int and 0<=z<10 for z in x) for row in A for x in row)

def inner_zero(x,y):
    cnt=[0]*10
    for u,v in zip(x,y):cnt[(v-u)%10]+=1
    q=[cnt[k]-cnt[k+5] for k in range(5)]
    return q[0]==-q[1]==q[2]==-q[3]==q[4]

def ray(x):return tuple((z-x[0])%10 for z in x)
for r in range(10):
    for c,d in combinations(range(10),2):assert inner_zero(A[r][c],A[r][d])
for c in range(10):
    for r,s in combinations(range(10),2):assert inner_zero(A[r][c],A[s][c])
R=[ray(A[r][c]) for r in range(10) for c in range(10)]
assert len(set(R))==100
for x,y in combinations(R,2):assert x!=y
print('PASS exact 100 unit vectors, all20 row/column ONBs, all4950 ray pairs distinct')

# A transversal is a clique taking one column per row. Search every row0
# column explicitly: no symmetry or claimed resolution is assumed.
valid={}
for r,s in combinations(range(10),2):
    for c in range(10):
        valid[r,s,c]=sum((1<<d) for d in range(10) if d!=c and inner_zero(A[r][c],A[s][d]))
nodes=0

def visit(r,used,choices):
    global nodes
    nodes+=1
    if r==10:return True
    allowed=((1<<10)-1)^used
    for s,c in enumerate(choices):allowed &= valid[s,r,c]
    while allowed:
        bit=allowed&-allowed;allowed-=bit
        if visit(r+1,used|bit,choices+[bit.bit_length()-1]):return True
    return False
found=visit(0,0,[])
print('transversal_found',found,'complete_backtracking_nodes',nodes)
assert not found
print('PASS complete exact original-vector transversal search for this one example only')
