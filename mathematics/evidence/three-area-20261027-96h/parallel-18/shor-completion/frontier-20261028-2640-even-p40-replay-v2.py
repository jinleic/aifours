#!/usr/bin/env python3
"""Set-based n2640 P40 replay with slack branching; v1 timed out."""
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
F={gcd(a-b,n) for a,b in combinations(A,2)}|{4,16,660,1320}
C={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)};assert len(C)==457
adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%3==r} for r in range(3)]+[{x for x in C if x%11==r} for r in range(11)]
need=[22]*3+[6]*11;active=set(C)
for x in sorted(Y):
 assert x in active;active.remove(x);active-=adj[x]
 for j,g in enumerate(groups):need[j]-=int(x in g)
stats={'nodes':0,'prunes':0,'memo_hits':0};cache=set()
def dfs(active,need):
 stats['nodes']+=1
 if any(k<0 for k in need):return False
 active=set(active)
 for g,k in zip(groups,need):
  if k==0:active-=g
 if any(len(active&g)<k for g,k in zip(groups,need)):
  stats['prunes']+=1;return False
 if all(k==0 for k in need):return True
 key=(frozenset(active),tuple(need))
 if key in cache:stats['memo_hits']+=1;return False
 j=min((j for j,k in enumerate(need) if k),key=lambda j:(len(active&groups[j])-need[j],len(active&groups[j])))
 x=max(sorted(active&groups[j]),key=lambda x:(len(adj[x]&active),sum(x in g for g in groups)))
 nxt=[k-int(x in g) for k,g in zip(need,groups)]
 if dfs(active-{x}-adj[x],nxt) or dfs(active-{x},need):return True
 cache.add(key);return False
if dfs(active,need):raise AssertionError('unexpected Q quota witness')
print(json.dumps({'Q_candidates':len(C),'search':stats,'result':'UNSAT',
 'v1':'separate earlier set replay timed out after35s',
 'scope':'n2640 P40 even-Q tail replay'},indent=2))
