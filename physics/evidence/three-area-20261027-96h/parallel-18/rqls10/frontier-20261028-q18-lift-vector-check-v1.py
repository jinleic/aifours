#!/usr/bin/env python3
"""Independent exact q90 original-vector and full transversal verification."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text());A=D['K_exponents']
assert len(A)==10 and all(len(row)==10 for row in A) and all(type(x)==int and 0<=x<18 for row in A for x in row)
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
f=phi(90);degree=len(f)-1;assert degree==24
powers=[]
for k in range(90):
 a=[0]*k+[1]
 for j in range(len(a)-1,degree-1,-1):
  v=a[j]
  for i,c in enumerate(f):a[j-degree+i]-=v*c
 powers.append(tuple((a+[0]*degree)[:degree]))
def orth(x,y):
 exp=[(b-a)%90 for a,b in zip(x,y)]
 return all(sum(powers[z][j] for z in exp)==0 for j in range(degree))
V=[[[ (9*r*t+5*A[t][c])%90 for t in range(10)] for c in range(10)] for r in range(10)]
for r in range(10):
 for c,d in combinations(range(10),2):assert orth(V[r][c],V[r][d])
for c in range(10):
 for r,s in combinations(range(10),2):assert orth(V[r][c],V[s][c])
rays=[tuple((v-vs[0])%90 for v in vs) for row in V for vs in row]
assert len(set(rays))==100
for a,b in combinations(rays,2):assert a!=b
R=D['rows'];C=D['columns'];r=R[0];s=next(x for x in range(10) if x not in R);c=C[0];d=next(x for x in range(10) if x not in C)
cross=(A[r][c]+A[s][d]-A[r][d]-A[s][c])%18
assert cross%3!=0
print('PASS exact 100 norms,20 original row/column ONBs,4950 distinct ray pairs')
print('PASS gauge-invariant q18 crossratio exponent',cross,'not a sixth root')
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
print('PASS all actual transversals excluded for this explicit sample only')
