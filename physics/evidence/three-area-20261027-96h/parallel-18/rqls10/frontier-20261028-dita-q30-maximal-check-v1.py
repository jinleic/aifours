#!/usr/bin/env python3
"""Independent exact cyclotomic original-vector and transversal checker."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
D=json.loads((Path(__file__).resolve().parent/'frontier-20261028-dita-q30-maximal-result-v1.json').read_text())
A=D['exponents']
assert D['dimension']==10 and D['normalization']=='1/sqrt(10)'
assert len(A)==10 and all(len(row)==10 for row in A)
assert all(len(x)==10 and all(type(z)==int and 0<=z<30 for z in x) for row in A for x in row)

def divide(a,b):
    a=a[:];q=[0]*(len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b);v=a[-1];q[k]=v
        for j,u in enumerate(b):a[j+k]-=v*u
        while a and a[-1]==0:a.pop()
    assert not a
    return q
@lru_cache(None)
def phi(n):
    p=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:p=divide(p,phi(d))
    return p
f=phi(30);deg=len(f)-1
assert deg==8 and f[-1]==1

def remainder(p):
    p=p[:]
    for i in range(len(p)-1,deg-1,-1):
        v=p[i]
        for j in range(deg+1):p[i-deg+j]-=v*f[j]
    return tuple((p+[0]*deg)[:deg])
powers=[]
for k in range(30):powers.append(remainder([0]*k+[1]))

def zero(x,y):
    accum=[0]*deg
    for u,v in zip(x,y):
        q=powers[(v-u)%30]
        for j in range(deg):accum[j]+=q[j]
    return all(z==0 for z in accum)

def ray(x):return tuple((z-x[0])%30 for z in x)
for r in range(10):
    for c,d in combinations(range(10),2):assert zero(A[r][c],A[r][d])
for c in range(10):
    for r,s in combinations(range(10),2):assert zero(A[r][c],A[s][c])
R=[ray(A[r][c]) for r in range(10) for c in range(10)]
assert len(set(R))==100
for x,y in combinations(R,2):assert x!=y
print('Phi30 ascending',f)
print('PASS exact original vectors: 100 norms, 20 ONBs, 4950 distinct ray pairs')
valid={}
for r,s in combinations(range(10),2):
    for c in range(10):valid[r,s,c]=sum(1<<d for d in range(10) if d!=c and zero(A[r][c],A[s][d]))
nodes=0
def visit(r,used,chosen):
    global nodes
    nodes+=1
    if r==10:return True
    allowed=((1<<10)-1)^used
    for s,c in enumerate(chosen):allowed &= valid[s,r,c]
    while allowed:
        bit=allowed&-allowed;allowed-=bit
        if visit(r+1,used|bit,chosen+[bit.bit_length()-1]):return True
    return False
found=visit(0,0,[])
print('transversal_found',found,'complete_backtracking_nodes',nodes)
assert not found
print('PASS complete original-vector transversal census for this example only')
