#!/usr/bin/env python3
"""Exact seminormal check for K-sandwich Rees band over nonrectangular regular base."""
from itertools import product
B=tuple(product(range(2),range(2)));G=range(2)
def bm(a,b):return(a[0],a[1]&b[1])
def act(g,a):return(a[0]^g,a[1])
K=tuple(p for p in B if all(bm(bm(b,p),b)==b for b in B));assert set(K)=={(0,1),(1,1)}
P=((((0,1),0),((1,1),0)),(((0,1),0),((1,1),1)))
rows=tuple(product(range(2),G));cols=tuple(product(range(2),G));T=tuple(product(rows,B,cols));ix={x:i for i,x in enumerate(T)}
def H(col,row):
 l,t=col;j,u=row;p,q=P[l][j]
 return act(t,p) if q==(t^u) else K[0]
def tm(a,b):return(a[0],bm(bm(a[1],H(a[2],b[0])),b[1]),b[2])
M=tuple(tuple(ix[tm(a,b)] for b in T) for a in T);n=len(T)
assert n==64 and all(M[x][x]==x for x in range(n))
assert all(M[M[x][y]][z]==M[x][M[y][z]] for x,y,z in product(range(n),repeat=3))
for x in range(n):
 for y in range(n):
  a=M[x][y]
  for z in range(n):
   b=M[a][z];c=M[M[b][x]][z]
   for w in range(n):assert M[M[b][w]][x]==M[M[c][w]][x]
print('PASS T=64 over nonrectangular regular B, all64^4=16777216 seminormal identities and band laws')
print('LIMIT finite same-author check; universal K-sandwich argument is symbolic')
