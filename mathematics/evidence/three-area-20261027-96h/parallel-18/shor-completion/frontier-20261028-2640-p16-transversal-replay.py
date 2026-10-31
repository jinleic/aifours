#!/usr/bin/env python3
"""Independent reverse-order set-based replay of 2640 odd-tail branch."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
heads={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
R=(14,13,10,9,6,5,2,1);choices=[sorted((x for x in heads if x%16==r),reverse=True) for r in R]
assert all(len(x)==3 for x in choices)
hist=Counter()
for chosen in product(*choices):
 S=set(chosen)|set(A);hist[tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}))]+=1
assert sum(hist.values())==6561 and len(hist)==25

def solve(C,F):
 C=set(C);adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%5==r} for r in (0,4)]+[{x for x in C if x%11==0}]
 need=[33,33,15];active=set(C)
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
  nxt=[k-int(x in g) for k,g in zip(need,groups)]
  return dfs(active-{x}-adj[x],nxt) or dfs(active-{x},need)
 if dfs(active,need):raise AssertionError('unexpected quota SAT')
 return {'core':len(C),'search':stats}
stats=Counter();hard=[]
for H,freq in sorted(hist.items()):
 F=set(H)
 if any(gcd(a-b,n) in F for a,b in combinations(Y,2)):stats['anchor_rejected']+=freq;continue
 q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
 if any(sum(x%11==r for x in q)<15 for r in range(11)):
  stats['capacity_rejected']+=freq;continue
 core={x for x in q if x%5 in (0,4) or x%11==0}
 hard.append({'H':H,'choices':freq,'quota':solve(core,F)});stats['quota_rejected']+=freq
assert (stats['anchor_rejected'],stats['capacity_rejected'],stats['quota_rejected'])==(0,6519,42) and len(hard)==8
print(json.dumps({'head_choices':6561,'distinct_H':len(hist),'stats':dict(stats),
                  'hard_cases':hard,'scope':'separate n2640 P16 Q165 replay'},indent=2))
