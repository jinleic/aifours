#!/usr/bin/env python3
"""Set-based, differently ordered replay of 1980 P10 tail quota obstruction."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;head=(0,3,8,11);tail=(0,1,7,13,14)
F={gcd(a-b,n) for a,b in combinations(head,2)}
C={x for x in range(n) if (x%11==0 or x%9==8) and all(x==y or gcd(x-y,n) not in F for y in tail)}
assert len(C)==56
adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%11==0},{x for x in C if x%9==8}]
active=set(C);need=[18,22];active.remove(0);active-=adj[0]
for i,g in enumerate(groups):need[i]-=int(0 in g)
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
 i=min((i for i,k in enumerate(need) if k),key=lambda i:(Fraction(len(active&groups[i]),need[i]),-i))
 x=max(active&groups[i],key=lambda x:(len(adj[x]&active),-x))
 nn=[k-int(x in g) for k,g in zip(need,groups)]
 return dfs(active-{x}-adj[x],nn) or dfs(active-{x},need)
if dfs(active,need):raise AssertionError('unexpected quota witness')
print(json.dumps({'core_candidates':len(C),'search':stats,'result':'UNSAT',
                  'scope':'independent n1980 P10 branch replay'},indent=2))
