#!/usr/bin/env python3
"""Exact finite transversal/quotas certificate for n2640, P16 Q165."""
from collections import Counter
from itertools import combinations,product
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
R=[r for r in range(16) if r%4 in (1,2)];opts={r:sorted(x for x in P if x%16==r) for r in R}
assert R==[1,2,5,6,9,10,13,14] and all(len(opts[r])==3 for r in R)
hist=Counter()
for values in product(*(opts[r] for r in R)):
 S=set(values)|A;H=tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}));hist[H]+=1
assert sum(hist.values())==3**8 and len(hist)==25

def quota(C,F):
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%5==r) for r in (0,4)]+[sum(1<<i for i,x in enumerate(C) if x%11==0)]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
 av=(1<<N)-1;need=[33,33,15]
 for x in (0,14):
  i=idx[x];assert av>>i&1;av &= ~(adj[i]|1<<i)
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
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;nn=need.copy()
  for j in mem[i]:nn[j]-=1
  if dfs(av&~(adj[i]|b),tuple(nn)) or dfs(av&~b,tuple(need)):return True
  cache.add(key);return False
 if dfs(av,tuple(need)):raise AssertionError('unexpected relaxed SAT')
 return {'core':N,'nodes':stats['nodes'],'prunes':stats['prunes']}

stats=Counter();hard=[]
for H,freq in sorted(hist.items()):
 F=set(H)
 if any(gcd(a-b,n) in F for a,b in combinations(Y,2)):
  stats['anchor_rejected']+=freq;continue
 q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
 if any(sum(x%11==j for x in q)<15 for j in range(11)):
  stats['capacity_rejected']+=freq;continue
 core=[x for x in q if x%5 in (0,4) or x%11==0]
 hard.append({'H':H,'choices':freq,'quota':quota(core,F)});stats['quota_rejected']+=freq
assert (stats['anchor_rejected'],stats['capacity_rejected'],stats['quota_rejected'])==(0,6519,42) and len(hard)==8
W=[0,14,33,50,74,140,164,224,230,231,264,290,314,330,350,363,380,404,470,494,554,561,594,614,620,627,644,660,680,693,710,734,830,884,891,924,944,950,957,974,1010,1070,1094,1160,1214,1274,1287,1334,1340,1400,1424,1490,1550,1604,1664,1670,1730,1754,1790,1814,1820,1880,1934,1994,2030,2054,2060,2084,2120,2144,2150,2210,2270,2294,2324]
assert len(W)==len(set(W))==75 and {0,14}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in GA for y in Y) for x in W)
assert all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert [sum(x%m==r for x in W) for m,r in ((5,0),(5,4),(11,0))]==[33,33,15]
print(json.dumps({'head_choices':3**8,'distinct_H':len(hist),'stats':dict(stats),
 'hard_cases':hard,'control':'SAT after dropping forced-head gcd classes',
 'scope':'n2640 P16 Q165 branch'},indent=2))
