#!/usr/bin/env python3
"""Independently ordered set-based 2310 tail quota replay."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=2310;A=(0,3,8,11);Y=(0,1,7,13,14)
F={gcd(a-b,n) for a,b in combinations(A,2)}
def run(spec,anchors):
 C={x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==y or gcd(x-y,n) not in F for y in Y)}
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
cases=[('10',[(3,0,77),(11,2,21)],(0,13)),
 ('14',[(3,2,55),(11,3,15),(5,3,33)],(13,14)),
 ('15',[(11,3,14),(11,0,14)],(0,14)),('22',[(3,2,35),(3,0,35)],(0,14))]
out={name:run(spec,anchors) for name,spec,anchors in cases}
assert [out[j]['candidates'] for j in ('10','14','15','22')]==[116,184,74,178]
print(json.dumps({'cases':out,'scope':'independent 2310 tail quota replay'},indent=2))
