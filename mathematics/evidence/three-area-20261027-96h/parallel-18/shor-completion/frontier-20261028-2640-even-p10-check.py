#!/usr/bin/env python3
"""Exact partial-head and tail-quota certificate for n2640 P10/Q264."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
c2=sorted(x for x in P if x%5==2);c4=sorted(x for x in P if x%5==4)
assert len(c2)==len(c4)==12
hist=Counter();bad=0
for a in combinations(c2,2):
 for b in combinations(c4,2):
  S=set(a+b)|A
  if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
  hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}))]+=1
assert bad==866 and sum(hist.values())==3490 and len(hist)==210

def quota(C,F):
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%3==0),sum(1<<i for i,x in enumerate(C) if x%11==2)]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
 av=(1<<N)-1;need=[88,24]
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
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;nn=need.copy()
  for j in mem[i]:nn[j]-=1
  if dfs(av&~(adj[i]|b),tuple(nn)) or dfs(av&~b,tuple(need)):return True
  cache.add(key);return False
 if dfs(av,tuple(need)):raise AssertionError('unexpected Q quota witness')
 return stats

stats=Counter();hard=[]
for H,freq in sorted(hist.items()):
 F=set(H)
 assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
 if any(sum(x%3==j for x in Q)<88 for j in range(3)):
  stats['mod3_capacity']+=freq;continue
 if any(sum(x%11==j for x in Q)<24 for j in range(11)):
  stats['mod11_capacity']+=freq;continue
 C=[x for x in Q if x%3==0 or x%11==2]
 hard.append({'H':H,'frequency':freq,'core':len(C),'search':quota(C,F)});stats['quota_unsat']+=freq
assert (stats['mod3_capacity'],stats['mod11_capacity'],stats['quota_unsat'])==(408,2636,446) and len(hard)==64
W=[0,13,30,60,75,120,180,225,240,270,277,299,300,315,330,343,360,375,450,510,541,555,570,600,615,629,630,660,673,690,705,720,780,840,855,871,900,915,930,945,960,990,1003,1020,1035,1050,1095,1170,1185,1201,1230,1245,1260,1275,1290,1320,1333,1335,1380,1425,1440,1500,1515,1531,1560,1575,1597,1620,1650,1665,1680,1710,1755,1770,1815,1861,1890,1905,1920,1927,1949,1950,1980,1995,2010,2040,2055,2100,2145,2160,2220,2235,2250,2257,2279,2280,2295,2340,2370,2385,2430,2475,2490,2535,2565,2580]
assert len(W)==len(set(W))==106 and {0,13}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in GA for y in Y) for x in W)
assert all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert sum(x%3==0 for x in W)==88 and sum(x%11==2 for x in W)==24
print(json.dumps({'head_pair_choices':4356,'head_conflicts':bad,'distinct_H':len(hist),
 'stats':dict(stats),'hard_cases':len(hard),'max_quota_nodes':max(x['search']['nodes'] for x in hard),
 'control':'SAT when forced-head gcd restrictions omitted','scope':'n2640 P10 even-Q branch'},indent=2))
