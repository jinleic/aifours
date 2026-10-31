#!/usr/bin/env python3
"""Exact P24 tail quotas assuming the written CM-T2 parity lemma."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
E=sorted(x for x in P if x%3==1 and x%2==0);O=sorted(x for x in P if x%3==1 and x%2)
assert len(E)==len(O)==12
hist=Counter();bad=0
for a in combinations(E,4):
 for b in combinations(O,4):
  S=set(a+b)|A
  if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
  hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}))]+=1
assert bad==239696 and sum(hist.values())==5329 and len(hist)==45

def quota(C,F):
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%5==0),sum(1<<i for i,x in enumerate(C) if x%11==2)]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)];av=(1<<N)-1;need=[22,10]
 for a in (0,13):
  i=idx[a];assert av>>i&1;av &= ~(adj[i]|1<<i)
  for j in mem[i]:need[j]-=1
 stats={'nodes':0,'prunes':0};cache=set()
 def dfs(av,need):
  stats['nodes']+=1;need=list(need)
  for j,k in enumerate(need):
   if k<0:return False
   if k==0:av &= ~groups[j]
  if any((av&groups[j]).bit_count()<k for j,k in enumerate(need)):stats['prunes']+=1;return False
  if not any(need):return True
  key=(av,tuple(need))
  if key in cache:return False
  j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&groups[j]).bit_count()-need[j],(av&groups[j]).bit_count()))
  bits=av&groups[j];pool=[]
  while bits:
   low=bits&-bits;bits-=low;pool.append(low.bit_length()-1)
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));bit=1<<i;nn=need.copy()
  for j in mem[i]:nn[j]-=1
  if dfs(av&~(adj[i]|bit),tuple(nn)) or dfs(av&~bit,tuple(need)):return True
  cache.add(key);return False
 if dfs(av,tuple(need)):raise AssertionError('unexpected Q quota witness')
 return stats
stats=Counter();nodes=[];hard=0
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
 if any(sum(x%5==j for x in Q)<22 for j in range(5)):
  stats['mod5_capacity']+=freq;continue
 if any(sum(x%11==j for x in Q)<10 for j in range(11)):
  stats['mod11_capacity']+=freq;continue
 C=[x for x in Q if x%5==0 or x%11==2];nodes.append(quota(C,F)['nodes']);hard+=1;stats['quota_unsat']+=freq
assert (stats['mod5_capacity'],stats['mod11_capacity'],stats['quota_unsat'],hard)==(0,128,5201,43)
W=[0,13,30,60,75,120,180,225,240,270,277,299,300,315,330,343,360,375,450,510,915,1245,1575,1905,2235,2565]
assert len(W)==len(set(W))==26 and {0,13}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in GA for y in Y) for x in W)
assert all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert sum(x%5==0 for x in W)==22 and sum(x%11==2 for x in W)==10
print(json.dumps({'head_choices':245025,'head_conflicts':bad,'distinct_H':len(hist),'stats':dict(stats),
 'hard_cases':hard,'max_nodes':max(nodes),'control':'SAT after dropping partial-head gcd classes',
 'scope':'n2640 P24 even-Q, assumes named CM-T2 parity'},indent=2))
