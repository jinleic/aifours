#!/usr/bin/env python3
"""Independent exact q630 original-vector/affine-pair verification."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-bh6-two-parameter-lift-result-v1.json').read_text())['candidate']
A=D['K_exponents_mod126'];assert len(A)==10 and all(len(row)==10 for row in A)
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
def mask(f):return [[int(t in f['rows'] and c in f['columns']) for c in range(10)] for t in range(10)]
M,N=mask(D['first']),mask(D['second'])
assert all(A[t][c]==(21*H[t][c]+7*M[t][c]+3*N[t][c])%126 for t in range(10) for c in range(10))
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
for r,s in combinations(range(10),2):
 bins={}
 for c in range(10):bins.setdefault((M[r][c]-M[s][c],N[r][c]-N[s][c]),[]).append((H[r][c]-H[s][c])%6)
 assert all(all(sum(six[x][j] for x in v)==0 for j in range(2)) for v in bins.values())
contrasts=[(M[r][c]-M[r][0]-M[0][c]+M[0][0],N[r][c]-N[r][0]-N[0][c]+N[0][0]) for r in range(1,10) for c in range(1,10)]
assert any(x*v-y*u!=0 for (x,y),(u,v) in combinations(contrasts,2))
def div(a,b):
 a=a[:];q=[0]*(len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);v=a[-1];q[k]=v
  for j,w in enumerate(b):a[j+k]-=v*w
  while a and a[-1]==0:a.pop()
 assert not a;return q
@lru_cache(None)
def phi(n):
 x=[-1]+[0]*(n-1)+[1]
 for d in range(1,n):
  if n%d==0:x=div(x,phi(d))
 return x
f=phi(630);deg=len(f)-1;assert deg==144
pw=[tuple([1]+[0]*(deg-1))]
for k in range(1,630):
 prev=pw[-1];lead=prev[-1]
 pw.append(tuple((-lead*f[j])+(prev[j-1] if j else 0) for j in range(deg)))
def orth(x,y):
 vals=[(b-a)%630 for a,b in zip(x,y)]
 return all(sum(pw[e][j] for e in vals)==0 for j in range(deg))
V=[[[ (63*r*t+5*A[t][c])%630 for t in range(10)] for c in range(10)] for r in range(10)]
for r in range(10):
 for c,d in combinations(range(10),2):assert orth(V[r][c],V[r][d])
for c in range(10):
 for r,s in combinations(range(10),2):assert orth(V[r][c],V[s][c])
rays=[tuple((v-vs[0])%630 for v in vs) for row in V for vs in row]
assert len(set(rays))==100
for a,b in combinations(rays,2):assert a!=b
print('PASS exact all-phase bivariate Hadamard, 2 independent mask directions')
print('PASS q630 exact 100 norms,20 original ONBs,4950 distinct ray pairs')
adj={(r,s,c):sum(1<<d for d in range(10) if d!=c and orth(V[r][c],V[s][d]))
     for r,s in combinations(range(10),2) for c in range(10)}
nodes=0
def search(r,used,chosen):
 global nodes
 nodes+=1
 if r==10:return True
 opt=1023^used
 for s,c in enumerate(chosen):opt &= adj[s,r,c]
 while opt:
  bit=opt&-opt;opt-=bit
  if search(r+1,used|bit,chosen+[bit.bit_length()-1]):return True
 return False
found=search(0,0,[]);print('transversal_found',found,'complete_nodes',nodes)
assert not found
print('PASS no transversal for this explicit q126 sample only')
