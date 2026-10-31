#!/usr/bin/env python3
"""Independent split-head and set-based replay of 2640 P15 branch."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V={x for x in P if x%3==1};T=sorted(x for x in V if x%5!=3);Z=sorted(V-set(T))
assert (len(T),len(Z))==(8,16)
sets=[set(s) for s in combinations(T,5)]+[set(s)|{z} for s in combinations(T,4) for z in Z]
hist=Counter()
for s in sets:
 S=s|set(A)
 if any(gcd(a-b,n) in GY for a,b in combinations(S,2)):continue
 hist[tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}))]+=1
assert sum(hist.values())==184 and len(hist)==20

def quota(C,F):
 C=set(C);adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%16==r} for r in range(16)]+[{x for x in C if x%11==r} for r in range(11)]
 need=[11]*16+[16]*11;active=set(C)
 for x in sorted(Y):
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
  x=max(active&groups[j],key=lambda x:(len(adj[x]&active),-x));nn=[k-int(x in g) for k,g in zip(need,groups)]
  return dfs(active-{x}-adj[x],nn) or dfs(active-{x},need)
 if dfs(active,need):raise AssertionError('unexpected quota SAT')
 return stats
stats=Counter();hard=[]
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
 if any(sum(x%16==r for x in Q)<11 for r in range(16)):
  stats['mod16_capacity']+=freq;continue
 if any(sum(x%11==r for x in Q)<16 for r in range(11)):
  stats['mod11_capacity']+=freq;continue
 hard.append(quota(Q,F)['nodes']);stats['quota_unsat']+=freq
assert (stats['mod16_capacity'],stats['mod11_capacity'],stats['quota_unsat'])==(78,0,106) and len(hard)==9
print(json.dumps({'head_partial_sets':184,'distinct_H':len(hist),'stats':dict(stats),
 'hard_cases':len(hard),'max_replay_nodes':max(hard),'scope':'independent n2640 P15 even-Q replay'},indent=2))
