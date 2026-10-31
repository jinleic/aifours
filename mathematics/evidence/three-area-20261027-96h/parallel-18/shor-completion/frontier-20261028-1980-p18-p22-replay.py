#!/usr/bin/env python3
"""Separate set-based 1980 P18/P22 forced-class quota replay."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def replay(old,bans,spec,anchors):
 C={x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==a or gcd(x-a,n) not in bans for a in old)}
 adj={x:{y for y in C if x!=y and gcd(x-y,n) in bans} for x in C}
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
 if dfs(active,need):raise AssertionError('unexpected quota SAT')
 return {'candidates':len(C),'search':stats,'result':'UNSAT'}
cases=[('P18',A,GY|{660},[(9,j,2) for j in (1,4,7)],()),
 ('Q18',Y,GA|{660},[(11,1,10),(11,2,10)],(1,13)),
 ('P22',A,GY|{180},[(11,j,2) for j in (6,7,9,2)],()),
 ('Q22',Y,GA|{180},[(5,4,18),(9,6,10),(9,3,10),(5,3,18),(9,8,10)],(13,14))]
out={name:replay(old,F,spec,anch) for name,old,F,spec,anch in cases}
assert [out[k]['candidates'] for k in ('P18','Q18','P22','Q22')]==[18,52,24,178]
print(json.dumps({'cases':out,'scope':'independent exact 1980 P18/P22 replay'},indent=2))
