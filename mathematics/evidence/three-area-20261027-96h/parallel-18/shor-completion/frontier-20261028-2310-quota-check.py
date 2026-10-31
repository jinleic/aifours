#!/usr/bin/env python3
"""Exact tail quota relaxations for 2310 P sizes10,14,15,22."""
from itertools import combinations
from math import gcd
import json
n=2310;A={0,3,8,11};Y={0,1,7,13,14};GA={gcd(a-b,n) for a,b in combinations(A,2)}
assert GA=={2,3,5,11}
def solve(spec,anchors):
 C=[x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==y or gcd(x-y,n) not in GA for y in Y)]
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in GA) for x in C]
 gr=[sum(1<<i for i,x in enumerate(C) if x%m==r) for m,r,k in spec]
 mem=[tuple(j for j,g in enumerate(gr) if g>>i&1) for i in range(N)];av=(1<<N)-1;need=[k for m,r,k in spec]
 for a in anchors:
  i=idx[a];assert av>>i&1;av &= ~(adj[i]|1<<i)
  for j in mem[i]:need[j]-=1
 stats={'nodes':0,'prunes':0};cache=set()
 def dfs(av,need):
  stats['nodes']+=1;need=list(need)
  for j,k in enumerate(need):
   if k<0:return False
   if k==0:av &= ~gr[j]
  if any((av&gr[j]).bit_count()<k for j,k in enumerate(need)):stats['prunes']+=1;return False
  if not any(need):return True
  key=(av,tuple(need))
  if key in cache:return False
  j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&gr[j]).bit_count()-need[j],(av&gr[j]).bit_count()))
  bits=av&gr[j];pool=[]
  while bits:
   low=bits&-bits;bits-=low;pool.append(low.bit_length()-1)
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;nn=need.copy()
  for j in mem[i]:nn[j]-=1
  if dfs(av&~(adj[i]|b),tuple(nn)) or dfs(av&~b,tuple(need)):return True
  cache.add(key);return False
 if dfs(av,tuple(need)):raise AssertionError('unexpected relaxed SAT')
 return {'candidates':N,'search':stats}

cases=[('10',[(3,0,77),(11,2,21)],(0,13),[0,13,21,35,42,63,84,105,147,189,231,252,273,294,315,343,357,399,441,462,483,497,504,525,567,609,630,651,673,693,714,728,735,777,805,819,840,861,903,924,945,959,987,1003,1029,1036,1050,1071,1092,1113,1155,1197,1239,1260,1267,1281,1302,1323,1333,1365,1407,1421,1449,1470,1491,1512,1533,1554,1575,1596,1617,1659,1663,1680,1701,1722,1729,1743,1764,1785,1827,1869,1890,1911,1932,1953,1974,1995,2037,2079,2100,2268]),
 ('14',[(3,2,55),(11,3,15),(5,3,33)],(13,14),[13,14,20,44,48,50,56,62,68,74,80,104,110,140,164,170,176,182,224,230,258,284,288,290,314,344,350,374,380,386,392,398,404,410,434,440,468,470,568,608,618,674,728,740,806,818,888,948,1004,1028,1058,1070,1098,1238,1278,1288,1308,1334,1388,1400,1518,1608,1658,1664,1718,1730,1868,1938,2048,2078,2148,2268,2288]),
 ('15',[(11,3,14),(11,0,14)],(0,14),[0,14,55,77,165,245,300,363,377,399,495,539,825,839,847,861,1001,1015,1155,1287,1301,1309,1323,1463,1609,1763,1785,2247]),
 ('22',[(3,2,35),(3,0,35)],(0,14),[0,14,21,35,47,80,84,110,182,189,245,294,392,410,441,455,483,504,602,651,665,714,740,777,812,840,875,903,924,950,1022,1050,1070,1085,1092,1113,1160,1232,1239,1260,1295,1370,1400,1407,1470,1505,1596,1680,1701,1715,1730,1764,1790,1827,1862,1869,1890,1925,1974,2000,2037,2060,2072,2100,2135,2163,2184,2268,2282,2289])]
out={}
for name,spec,anchors,W in cases:
 out[name]=solve(spec,anchors)
 F=GA-{2};assert len(W)==len(set(W)) and set(anchors)<=set(W)
 assert all(all(x==y or gcd(x-y,n) not in F for y in Y) for x in W)
 assert all(gcd(a-b,n) not in F for a,b in combinations(W,2))
 assert all(sum(x%m==r for x in W)==k for m,r,k in spec)
 assert any(gcd(a-b,n)==2 for a,b in combinations(W,2))
assert [out[j]['candidates'] for j in ('10','14','15','22')]==[116,184,74,178]
print(json.dumps({'cases':out,'result':'ALL UNSAT','controls':'SAT after removing gcd2',
                  'scope':'2310 P sizes10,14,15,22 only'},indent=2))
