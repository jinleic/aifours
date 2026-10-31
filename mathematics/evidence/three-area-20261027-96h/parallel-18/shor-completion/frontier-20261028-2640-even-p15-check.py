#!/usr/bin/env python3
"""Exact relaxed head/tail checks for n2640 P15/Q176."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V=sorted(x for x in P if x%3==1);assert len(V)==24
hist=Counter()
for s in combinations(V,5):
 if sum(x%5==3 for x in s)>1:continue
 S=set(s)|A
 if any(gcd(a-b,n) in GY for a,b in combinations(S,2)):continue
 hist[tuple(sorted({gcd(a-b,n) for a,b in combinations(S,2)}))]+=1
assert sum(hist.values())==184 and len(hist)==20

def quota(C,F):
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%16==r) for r in range(16)]+[sum(1<<i for i,x in enumerate(C) if x%11==r) for r in range(11)]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)];av=(1<<N)-1;need=[11]*16+[16]*11
 for a in sorted(Y):
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
 if dfs(av,tuple(need)):raise AssertionError('unexpected quota witness')
 return stats
stats=Counter();hard=[]
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
 if any(sum(x%16==r for x in Q)<11 for r in range(16)):
  stats['mod16_capacity']+=freq;continue
 if any(sum(x%11==r for x in Q)<16 for r in range(11)):
  stats['mod11_capacity']+=freq;continue
 hard.append({'H':H,'freq':freq,'candidates':len(Q),'search':quota(Q,F)});stats['quota_unsat']+=freq
assert (stats['mod16_capacity'],stats['mod11_capacity'],stats['quota_unsat'])==(78,0,106) and len(hard)==9
W=[0,1,7,13,14,73,110,120,127,180,193,217,230,240,247,264,276,277,283,290,300,313,331,337,343,350,374,384,386,403,410,444,457,494,504,523,547,554,564,577,607,613,614,643,660,661,667,673,674,733,770,780,787,840,853,877,890,900,907,924,936,937,943,950,960,973,991,997,1003,1010,1034,1044,1046,1063,1070,1104,1117,1154,1164,1183,1207,1214,1224,1237,1267,1273,1274,1303,1320,1321,1327,1333,1334,1393,1430,1440,1447,1500,1513,1537,1550,1560,1567,1584,1596,1597,1603,1610,1620,1633,1651,1657,1663,1670,1694,1704,1706,1723,1730,1764,1777,1814,1824,1843,1867,1874,1884,1897,1927,1933,1934,1963,1980,1981,1987,1993,1994,2053,2090,2100,2107,2160,2173,2197,2210,2220,2227,2244,2256,2257,2263,2270,2280,2293,2311,2317,2323,2330,2354,2364,2366,2383,2390,2424,2437,2474,2484,2503,2527,2534,2544,2557,2587,2593,2594,2623]
assert len(W)==len(set(W))==176 and Y<=set(W)
assert all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert all(sum(x%16==r for x in W)==11 for r in range(16))
assert all(sum(x%11==r for x in W)==16 for r in range(11))
print(json.dumps({'head_partial_sets':184,'distinct_H':len(hist),'stats':dict(stats),
 'hard_cases':len(hard),'max_nodes':max(x['search']['nodes'] for x in hard),
 'control':'SAT when partial-head gcd classes omitted','scope':'n2640 P15 even-Q'},indent=2))
