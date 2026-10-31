#!/usr/bin/env python3
"""Set-based replay of the n2640 P22 T2/parity quota certificate."""
from collections import Counter
from itertools import combinations,product
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
classes={j:{r:sorted(x for x in P if x%11==j and x%2==r) for r in (0,1)} for j in (1,2)}
assert all(len(classes[j][r])==6 for j in (1,2) for r in (0,1))
hist=Counter();bad=total=0
for e2,o2,e1,o1 in product(classes[2][0],classes[2][1],classes[1][0],classes[1][1]):
 total+=1;S={e2,o2,e1,o1,*A}
 if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
 hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}|{240}))]+=1
assert (total,bad,sum(hist.values()),len(hist))==(1296,272,1024,37)
Q0={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
assert not any(x%6==4 for x in Q0)

def quota(Q,F,a):
 Q=set(Q);adj={x:{y for y in Q if x!=y and gcd(x-y,n) in F} for x in Q}
 groups=[{x for x in Q if x%16==r} for r in range(16)]+[{x for x in Q if x%3==1},{x for x in Q if x%5==1}]
 need=[a if r%2==0 else 15-a for r in range(16)]+[40,24];active=set(Q)
 for x in sorted(Y):
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
 if dfs(active,need):raise AssertionError('unexpected tail quota SAT')
 return stats
stats=Counter();nodes=[];surv=0
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
 if any(sum(x%3==j for x in Q)<40 for j in range(3)) or any(sum(x%5==j for x in Q)<24 for j in range(5)):
  stats['prime_capacity']+=freq;continue
 valid=[a for a in range(1,11) if all(sum(x%16==r for x in Q)>=(a if r%2==0 else 15-a) for r in range(16))]
 if not valid:stats['twoadic_capacity']+=freq;continue
 surv+=1;stats['quota_unsat']+=freq
 for a in valid:nodes.append(quota(Q,F,a)['nodes'])
assert (stats['prime_capacity'],stats['twoadic_capacity'],stats['quota_unsat'],surv,len(nodes))==(64,452,508,24,139)
print(json.dumps({'head_choices':total,'head_conflicts':bad,'distinct_H':len(hist),'stats':dict(stats),
 'surviving_H':surv,'a_cases':len(nodes),'max_nodes':max(nodes),
 'scope':'separate set-state n2640 P22 T2 replay'},indent=2))
