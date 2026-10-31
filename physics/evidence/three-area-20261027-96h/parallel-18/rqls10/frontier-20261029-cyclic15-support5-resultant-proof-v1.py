#!/usr/bin/env python3
"""Cyclotomic resultant witnesses for 5 distinct supported eigenvalues."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(F(0),)*8;O=(F(1),)+(F(0),)*7;phi=[1,-1,0,1,-1,1,0,-1,1]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 q=[F(0)]*15
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:q[i+j]+=x*y
 for k in range(14,7,-1):
  v=q[k]
  if v:
   for j in range(8):q[k-8+j]-=v*phi[j]
 return tuple(q[:8])
r=(F(0),F(1))+(F(0),)*6;powers=[O]
for _ in range(15):powers.append(mul(powers[-1],r))
assert powers[15]==O and len(set(powers[:15]))==15
C=[add(O,powers[k])for k in range(15)];Inv=[]
for k in range(15):
 q=Z
 for j in range(15):q=add(q,powers[k*j%15]if j%2==0 else neg(powers[k*j%15]))
 q=tuple(x/2 for x in q);assert mul(C[k],q)==O;Inv.append(q)
def conj(x):
 q=Z
 for j,c in enumerate(x):
  if c:q=add(q,tuple(c*y for y in powers[-j%15]))
 return q
g=[conj(mul(C[(2*a)%15],Inv[(7*a)%15]))for a in range(15)];H={}
for a in range(15):
 for b in range(15):
  if a==b:continue
  delta=(b-a)%15;h0=neg(mul(C[(2*delta)%15],Inv[(5*delta)%15]));h1=neg(mul(mul(mul(g[a],conj(g[b])),C[(7*delta)%15]),Inv[(5*delta)%15]));H[a,b]=(h0,h1)
def polyprod(A,B):return(mul(A[0],B[0]),add(mul(A[0],B[1]),mul(A[1],B[0])),mul(A[1],B[1]))
def minors(S):
 q=[]
 for a,b,c,d in itertools.combinations(S,4):
  q.append(tuple(sub(x,y)for x,y in zip(polyprod(H[a,b],H[c,d]),polyprod(H[a,d],H[c,b]))))
  q.append(tuple(sub(x,y)for x,y in zip(polyprod(H[a,c],H[b,d]),polyprod(H[a,d],H[b,c]))))
 return q
def resultant(P,Q):
 c,b,a=P;f,e,d=Q;t=sub(mul(a,f),mul(c,d));return sub(mul(t,t),mul(sub(mul(a,e),mul(b,d)),sub(mul(b,f),mul(c,e))))
units=[u for u in range(1,15)if math.gcd(u,15)==1];remaining={S for S in itertools.combinations(range(15),5)if len({a%3 for a in S})==3};records=[];sizes=collections.Counter()
while remaining:
 S=min(remaining);orbit={tuple(sorted(u*a%15 for a in S))for u in units};assert orbit<=remaining;remaining-=orbit;sizes[len(orbit)]+=1;polys=minors(S);found=None
 for i,j in itertools.combinations(range(len(polys)),2):
  res=resultant(polys[i],polys[j])
  if res!=Z:found=(i,j,res);break
 assert found is not None
 i,j,res=found;records.append({'representative':list(S),'orbit_size':len(orbit),'minor_indices':[i,j],'resultant_phi15_basis':[str(x)for x in res]})
assert len(records)==299 and sum(x['orbit_size']for x in records)==2250
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'support_sets':2250,'unit_group_orbits':len(records),'orbit_sizes':dict(sizes),'records':records,
 'scope':'two off-diagonal rank-one minors have nonzero resultant for every 5-exponent support containing all three U5 classes','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-support5-resultant-proof-v1.json';out.write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'clock_finish':obj['clock_finish'],
 'support_sets':2250,'orbits':len(records),'orbit_sizes':dict(sizes),'status':'PRODUCED_UNREPLAYED'},indent=2))
