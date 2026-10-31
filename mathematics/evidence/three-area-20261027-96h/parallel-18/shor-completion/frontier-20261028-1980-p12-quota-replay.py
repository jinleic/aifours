#!/usr/bin/env python3
"""Set-based, different-order replay of 1980 P12 tail obstruction."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;head=(0,3,8,11);tail=(0,1,7,13,14)
F={gcd(a-b,n) for a,b in combinations(head,2)}
C={x for x in range(n) if (x%5 in (0,4) or x%11==0) and
   all(x==y or gcd(x-y,n) not in F for y in tail)}
assert len(C)==171
adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%5==r} for r in (0,4)]+[{x for x in C if x%11==0}]
active=set(C);need=[33,33,15]
for x in (0,14):
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
    nextneed=[k-int(x in g) for k,g in zip(need,groups)]
    return dfs(active-{x}-adj[x],nextneed) or dfs(active-{x},need)
if dfs(active,need):raise AssertionError('unexpected feasible relaxation')
print(json.dumps({'core':len(C),'search':stats,'result':'UNSAT',
                  'scope':'separate exact 1980 P12 tail-quota replay'},indent=2))
