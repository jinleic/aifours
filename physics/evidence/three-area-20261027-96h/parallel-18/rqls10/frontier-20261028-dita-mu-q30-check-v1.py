#!/usr/bin/env python3
"""Independent QLS definition and full transversal search over Q(zeta30)."""
from itertools import combinations
from pathlib import Path
import json
D=json.loads((Path(__file__).resolve().parent/'frontier-20261028-dita-mu-q30-result-v1.json').read_text())
A=D['exponents'];assert D['dimension']==10 and D['normalization']=='1/sqrt(10)'
assert len(A)==10 and all(len(row)==10 for row in A)
assert all(len(v)==10 and all(type(e)==int and 0<=e<30 for e in v) for row in A for v in row)
# Ascending Phi_30, independently identified as Phi_15(-x).
f=[1,1,0,-1,-1,-1,0,1,1]
def rem(p):
    p=p[:]
    for i in range(len(p)-1,7,-1):
        v=p[i]
        for j in range(9):p[i-8+j]-=v*f[j]
    return tuple((p+[0]*8)[:8])
powers=[rem([0]*k+[1]) for k in range(30)]
def orth(x,y):
    return all(sum(powers[(v-u)%30][k] for u,v in zip(x,y))==0 for k in range(8))
def ray(v):return tuple((x-v[0])%30 for x in v)
for r in range(10):
    for c,d in combinations(range(10),2):assert orth(A[r][c],A[r][d])
for c in range(10):
    for r,s in combinations(range(10),2):assert orth(A[r][c],A[s][c])
rays=[ray(v) for row in A for v in row]
assert len(set(rays))==100
for x,y in combinations(rays,2):assert x!=y
print('PASS 100 norms, all20 ONBs, 4950 distinct ray pairs')
valid={(r,s,c):sum(1<<d for d in range(10) if d!=c and orth(A[r][c],A[s][d]))
       for r,s in combinations(range(10),2) for c in range(10)}
nodes=0
def visit(r,used,chosen):
    global nodes
    nodes+=1
    if r==10:return True
    available=1023^used
    for s,c in enumerate(chosen):available &= valid[s,r,c]
    while available:
        bit=available&-available;available-=bit
        if visit(r+1,used|bit,chosen+[bit.bit_length()-1]):return True
    return False
found=visit(0,0,[])
print('transversal_found',found,'complete_backtracking_nodes',nodes)
assert not found
print('PASS complete transversal search for this sample only')
