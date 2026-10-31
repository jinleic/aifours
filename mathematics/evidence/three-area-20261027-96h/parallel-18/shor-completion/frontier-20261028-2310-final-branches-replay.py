#!/usr/bin/env python3
"""Independent set-based and complement-selection replay of 2310 branches."""
from fractions import Fraction
from itertools import combinations,product
from math import gcd
import json
n=2310;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def replay(old,F,spec,anchors):
 C={x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==a or gcd(x-a,n) not in F for a in old)}
 adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%m==r} for m,r,k in spec];need=[k for m,r,k in spec];active=set(C)
 for x in anchors:
  assert x in active;active.remove(x);active-=adj[x]
  for j,g in enumerate(groups):need[j]-=int(x in g)
 stats={'nodes':0,'prunes':0}
 def dfs(active,need):
  stats['nodes']+=1
  if any(k<0 for k in need):return False
  active=set(active)
  for g,k in zip(groups,need):
   if k==0:active-=g
  if any(len(active&g)<k for g,k in zip(groups,need)):
   stats['prunes']+=1;return False
  if all(k==0 for k in need):return True
  j=min((j for j,k in enumerate(need) if k),key=lambda j:(Fraction(len(active&groups[j]),need[j]),-j))
  x=max(active&groups[j],key=lambda x:(len(adj[x]&active),-x))
  nxt=[k-int(x in g) for k,g in zip(need,groups)]
  return dfs(active-{x}-adj[x],nxt) or dfs(active-{x},need)
 if dfs(active,need):raise AssertionError('unexpected quota witness')
 return {'candidates':len(C),'search':stats,'result':'UNSAT'}
cases=[('P21',A,GY|{10},[(3,1,7),(7,2,3)],()),
 ('Q21',Y,GA|{10},[(2,0,55),(5,1,22),(5,3,22)],(0,1,13,14)),
 ('P30',A,GY,[(3,1,10),(5,3,6)],(3,8)),
 ('Q42',Y,GA|{10,35,77},[(11,3,5),(11,0,5),(5,0,11),(11,4,5)],(0,14))]
out={name:replay(old,F,spec,anchors) for name,old,F,spec,anchors in cases}
# Independently enumerate excluded endpoints instead of retained endpoints.
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V={x for x in P if x%3==1}
edges=[(85,1243),(256,1078),(415,913),(586,1408),(916,88),
       (1405,253),(1735,583),(1906,418),(2065,1573),(2236,748)]
singles={1738,1903,2068,2233};assert len(V)==24 and set(sum((list(e) for e in edges),[]))|singles==V
valid=[]
for bits in product((1,0),repeat=10):
 omitted={edges[j][bits[j]] for j in range(10)};keep=V-omitted
 if all(gcd(a-b,n) not in GY for a,b in combinations(keep,2)):valid.append(keep)
assert len(valid)==1 and {10,35,77}<={gcd(a-b,n) for a,b in combinations(valid[0]|set(A),2)}
assert [out[k]['candidates'] for k in ('P21','Q21','P30','Q42')]==[42,218,172,81]
print(json.dumps({'P42_unique_forced_set':len(valid),'cases':out,
                  'scope':'independent exact 2310 last-three replay'},indent=2))
