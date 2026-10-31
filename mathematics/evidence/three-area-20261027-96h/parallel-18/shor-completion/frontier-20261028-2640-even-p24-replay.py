#!/usr/bin/env python3
"""Complement-head set-state replay for n2640 P24 T2 branch."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
E={x for x in P if x%3==1 and x%2==0};O={x for x in P if x%3==1 and x%2};assert len(E)==len(O)==12
hist=Counter();bad=0
for omitO in combinations(sorted(O),8):
 for omitE in combinations(sorted(E),8):
  S=(E-set(omitE))|(O-set(omitO))|set(A)
  if any(gcd(a-b,n) in GY for a,b in combinations(S,2)):bad+=1;continue
  hist[tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}))]+=1
assert bad==239696 and sum(hist.values())==5329 and len(hist)==45

def quota(C,F):
 C=set(C);adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%5==0},{x for x in C if x%11==2}];need=[22,10];active=set(C)
 for x in (0,13):
  assert x in active;active.remove(x);active-=adj[x]
  for j,g in enumerate(groups):need[j]-=int(x in g)
 stats={'nodes':0,'prunes':0};cache=set()
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
  if key in cache:return False
  j=min((j for j,k in enumerate(need) if k),key=lambda j:(len(active&groups[j])-need[j],len(active&groups[j])))
  x=max(sorted(active&groups[j]),key=lambda x:(len(adj[x]&active),sum(x in g for g in groups)))
  nxt=[k-int(x in g) for k,g in zip(need,groups)]
  if dfs(active-{x}-adj[x],nxt) or dfs(active-{x},need):return True
  cache.add(key);return False
 if dfs(active,need):raise AssertionError('unexpected Q quota SAT')
 return stats
stats=Counter();nodes=[];hard=0
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
 if any(sum(x%5==j for x in Q)<22 for j in range(5)):
  stats['mod5_capacity']+=freq;continue
 if any(sum(x%11==j for x in Q)<10 for j in range(11)):
  stats['mod11_capacity']+=freq;continue
 C={x for x in Q if x%5==0 or x%11==2};nodes.append(quota(C,F)['nodes']);hard+=1;stats['quota_unsat']+=freq
assert (stats['mod5_capacity'],stats['mod11_capacity'],stats['quota_unsat'],hard)==(0,128,5201,43)
print(json.dumps({'head_conflicts':bad,'distinct_H':len(hist),'stats':dict(stats),'hard_cases':hard,
 'max_replay_nodes':max(nodes),'scope':'set-state n2640 P24 CM-T2 replay'},indent=2))
