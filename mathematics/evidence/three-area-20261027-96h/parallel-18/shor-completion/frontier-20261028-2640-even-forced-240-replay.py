#!/usr/bin/env python3
"""Set-based independent replay of n2640 forced-240 head quota."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14);F={gcd(a-b,n) for a,b in combinations(Y,2)}|{240}
rs=(2,10,9,7,3);C={x for x in range(n) if x%11 in rs and all(x==a or gcd(x-a,n) not in F for a in A)};assert len(C)==63
adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%11==r} for r in rs];need=[2]*5;active=set(C);active.remove(3);active-=adj[3]
for j,g in enumerate(groups):need[j]-=int(3 in g)
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
 x=max(active&groups[j],key=lambda x:(len(adj[x]&active),-x));nn=[k-int(x in g) for k,g in zip(need,groups)]
 return dfs(active-{x}-adj[x],nn) or dfs(active-{x},need)
if dfs(active,need):raise AssertionError('unexpected head quota witness')
print(json.dumps({'P_core':len(C),'search':stats,'result':'UNSAT','forced_gcd':240,
                  'scope':'independent n2640 forced-240 head replay'},indent=2))
