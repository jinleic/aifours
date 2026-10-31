#!/usr/bin/env python3
"""Exact relaxed quota certificates for 1980 P18 and P22 branches."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def solve(old,bans,spec,anchors):
 C=[x for x in range(n) if any(x%m==r for m,r,k in spec) and all(x==a or gcd(x-a,n) not in bans for a in old)]
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if y!=x and gcd(x-y,n) in bans) for x in C]
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
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;n2=need.copy()
  for j in mem[i]:n2[j]-=1
  if dfs(av&~(adj[i]|b),tuple(n2)) or dfs(av&~b,tuple(need)):return True
  cache.add(key);return False
 if dfs(av,tuple(need)):raise AssertionError('unexpected relaxed SAT')
 return {'candidates':N,'search':stats}

cases=[('P18',A,GY,660,[(9,j,2) for j in (1,4,7)],(),[253,415,418,1408,88,1078]),
 ('Q18',Y,GA,660,[(11,1,10),(11,2,10)],(1,13),[1,13,67,133,167,211,387,397,541,607,727,793,871,1057,1201,1387,1453,1531,1717,1861]),
 ('P22',A,GY,180,[(11,j,2) for j in (6,7,9,2)],(),[183,303,695,908,1476,1503,1868,1923]),
 ('Q22',Y,GA,180,[(5,4,18),(9,6,10),(9,3,10),(5,3,18),(9,8,10)],(13,14),[13,14,60,62,74,120,133,170,193,240,300,343,350,374,384,434,463,494,523,554,624,660,673,674,780,793,840,853,890,924,960,1003,1020,1070,1094,1123,1154,1183,1272,1274,1320,1333,1334,1380,1430,1453,1500,1513,1560,1610,1663,1680,1694,1704,1783,1790,1814,1843,1874,1932])]
out={}
for name,old,bans,g,spec,anchors,W in cases:
 out[name]=solve(old,bans|{g},spec,anchors)
 assert len(W)==len(set(W)) and set(anchors)<=set(W)
 assert all(all(x==a or gcd(x-a,n) not in bans for a in old) for x in W)
 assert all(gcd(a-b,n) not in bans for a,b in combinations(W,2))
 assert all(sum(x%m==r for x in W)==k for m,r,k in spec)
 assert any(gcd(a-b,n)==g for a,b in combinations(W,2))
assert [out[x]['candidates'] for x in ('P18','Q18','P22','Q22')]==[18,52,24,178]
print(json.dumps({'cases':out,'result':'ALL UNSAT','controls':'SAT after removing designated gcd',
                  'scope':'1980 P-size18 and22 branches only'},indent=2))
