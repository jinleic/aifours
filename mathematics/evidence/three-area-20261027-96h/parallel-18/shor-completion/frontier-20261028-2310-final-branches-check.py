#!/usr/bin/env python3
"""Exact quota and saturated-head checks for 2310 P21/P30/P42."""
from itertools import combinations,product
from math import gcd
import json
n=2310;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def solve(old,bans,spec,anchors):
 C=[x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==a or gcd(x-a,n) not in bans for a in old)]
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in bans) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%m==r) for m,r,k in spec]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
 av=(1<<N)-1;need=[k for m,r,k in spec]
 for a in anchors:
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
 if dfs(av,tuple(need)):raise AssertionError('unexpected relaxed SAT')
 return {'candidates':N,'search':stats}

# P42: a 10-edge screen cover plus four singles; exactly one maximum 14-set.
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V={x for x in P if x%3==1}
edges=[(85,1243),(256,1078),(415,913),(586,1408),(916,88),
       (1405,253),(1735,583),(1906,418),(2065,1573),(2236,748)]
singles={1738,1903,2068,2233}
assert len(V)==24 and len({x for e in edges for x in e})==20 and set(sum((list(e) for e in edges),[]))|singles==V
assert all(gcd(a-b,n) in GY for a,b in edges)
maxsets=[]
for bits in product((0,1),repeat=10):
 S=singles|{edges[j][bits[j]] for j in range(10)}
 if all(gcd(a-b,n) not in GY for a,b in combinations(S,2)):maxsets.append(S)
assert len(maxsets)==1
S=maxsets[0]|A;H={10,35,77};assert H<={gcd(a-b,n) for a,b in combinations(S,2)}

cases=[('P21',A,GY,10,[(3,1,7),(7,2,3)],(),[256,415,583,586,916,1906,2236]),
 ('Q21',Y,GA,10,[(2,0,55),(5,1,22),(5,3,22)],(0,1,13,14),[0,1,13,14,42,56,84,91,133,140,182,224,252,294,301,331,343,350,392,434,462,504,511,553,560,602,630,644,651,661,673,714,721,728,763,770,812,840,854,903,924,931,973,991,1003,1022,1036,1050,1064,1092,1141,1183,1232,1260,1274,1288,1302,1321,1333,1351,1393,1400,1421,1470,1484,1512,1554,1561,1596,1603,1610,1651,1663,1673,1680,1694,1722,1764,1771,1813,1820,1862,1890,1932,1974,1981,1993,2023,2030,2072,2191,2233,2268]),
 ('P30',A,GY-{6},6,[(3,1,10),(5,3,6)],(3,8),[3,8,85,88,253,256,338,415,586,668,916,1405,1735,2065]),
 ('Q42',Y,GA|{10,35},77,[(11,3,5),(11,0,5),(5,0,11),(11,4,5)],(0,14),[0,14,91,140,224,301,350,553,560,630,763,770,840,847,924,1050,1260,1400,1610,1694])]
out={}
for name,old,bans,g,spec,anchors,W in cases:
 out[name]=solve(old,bans|{g},spec,anchors)
 assert len(W)==len(set(W)) and set(anchors)<=set(W)
 assert all(all(x==a or gcd(x-a,n) not in bans for a in old) for x in W)
 assert all(gcd(a-b,n) not in bans for a,b in combinations(W,2))
 assert all(sum(x%m==r for x in W)==k for m,r,k in spec)
 assert any(gcd(a-b,n)==g for a,b in combinations(W,2)) or any(x!=a and gcd(x-a,n)==g for x in W for a in old)
assert [out[k]['candidates'] for k in ('P21','Q21','P30','Q42')]==[42,218,172,81]
print(json.dumps({'P42_forced_maxsets':len(maxsets),'P42_forced_gcds':sorted(H),'quota_cases':out,
 'result':'ALL UNSAT','controls':'SAT after removing designated gcd','scope':'2310 P21/P30/P42 only'},indent=2))
