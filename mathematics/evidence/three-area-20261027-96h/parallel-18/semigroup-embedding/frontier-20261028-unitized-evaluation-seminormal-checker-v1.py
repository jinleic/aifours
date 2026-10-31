#!/usr/bin/env python3
"""Exhaust seminormality of a nonrectangular regular-base evaluation band."""
from itertools import product
B=tuple(product(range(2),range(2)));G=range(2)
def bm(a,b):return(a[0],a[1]&b[1])
def act(g,a):return(a[0]^g,a[1])
def bp(a,b):return b if a is None else a if b is None else bm(a,b)
K=tuple(x for x in B if all(bm(bm(a,x),a)==a for a in B));assert set(K)=={(0,1),(1,1)}
P=((None,None),(None,((1,1),1)));rows=tuple(product(range(2),G));cols=tuple(product(range(2),G))
T=tuple((r,b,c) for r in rows for b in B for c in cols)+tuple((r,None,c) for r in rows for c in cols if r[1]==c[1]);ix={x:i for i,x in enumerate(T)}
def H(c,r):
 l,t=c;j,u=r;p=P[l][j]
 if t==u:return None
 return act(t,p[0]) if p is not None and p[1]==(t^u) else K[0]
def tm(a,b):return(a[0],bp(bp(a[1],H(a[2],b[0])),b[1]),b[2])
M=tuple(tuple(ix[tm(a,b)] for b in T) for a in T);n=len(T)
assert n==72 and all(M[x][x]==x for x in range(n))
assert all(M[M[x][y]][z]==M[x][M[y][z]] for x,y,z in product(range(n),repeat=3))
for x in range(n):
 for y in range(n):
  a=M[x][y]
  for z in range(n):
   b=M[a][z];c=M[M[b][x]][z]
   for w in range(n):
    assert M[M[b][w]][x]==M[M[c][w]][x]
print('PASS T=72 nonrectangular regular base, all72^4=26873856 seminormal identities and all band laws')
print('LIMIT finite check; universal property requires separate written proof')
