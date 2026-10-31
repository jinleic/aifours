#!/usr/bin/env python3
"""Independent complement-head and set-based replay of n2640 P10 branch."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
L={x for x in P if x%5==2};R={x for x in P if x%5==4};assert len(L)==len(R)==12
hist=Counter();bad=0
for omitR in combinations(sorted(R),10):
 for omitL in combinations(sorted(L),10):
  S=(L-set(omitL))|(R-set(omitR))|set(A)
  if any(gcd(a-b,n) in GY for a,b in combinations(S,2)):bad+=1;continue
  hist[tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}))]+=1
assert bad==866 and sum(hist.values())==3490 and len(hist)==210

def quota(C,F):
 C=set(C);adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%3==0},{x for x in C if x%11==2}];need=[88,24];active=set(C)
 for x in (0,13):
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
  nn=[k-int(x in g) for k,g in zip(need,groups)]
  return dfs(active-{x}-adj[x],nn) or dfs(active-{x},need)
 if dfs(active,need):raise AssertionError('unexpected Q quota SAT')
 return stats

stats=Counter();nodes=[];hard=0
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
 if any(sum(x%3==j for x in Q)<88 for j in range(3)):
  stats['mod3_capacity']+=freq;continue
 if any(sum(x%11==j for x in Q)<24 for j in range(11)):
  stats['mod11_capacity']+=freq;continue
 C={x for x in Q if x%3==0 or x%11==2};nodes.append(quota(C,F)['nodes']);hard+=1;stats['quota_unsat']+=freq
assert (stats['mod3_capacity'],stats['mod11_capacity'],stats['quota_unsat'],hard)==(408,2636,446,64)
print(json.dumps({'head_conflicts':bad,'distinct_H':len(hist),'stats':dict(stats),
                  'hard_cases':hard,'max_replay_nodes':max(nodes),
                  'scope':'separate exact n2640 P10 even-tail replay'},indent=2))
