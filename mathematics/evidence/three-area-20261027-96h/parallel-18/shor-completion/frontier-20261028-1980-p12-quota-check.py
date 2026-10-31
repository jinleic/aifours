#!/usr/bin/env python3
"""Exact three-quota tail relaxation excluding n1980 P-size12."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
G={gcd(a-b,n) for a,b in combinations(A,2)};assert G=={3,4,5,11}
cand=[x for x in range(n) if (x%5 in (0,4) or x%11==0) and
      all(x==y or gcd(x-y,n) not in G for y in Y)]
assert len(cand)==171
N=len(cand);index={x:i for i,x in enumerate(cand)}
adj=[sum(1<<j for j,y in enumerate(cand) if y!=x and gcd(x-y,n) in G) for x in cand]
groups=[sum(1<<i for i,x in enumerate(cand) if x%5==r) for r in (0,4)]+[sum(1<<i for i,x in enumerate(cand) if x%11==0)]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
av=(1<<N)-1;need=[33,33,15]
for a in (0,14):
 i=index[a];assert av>>i&1;av &= ~(adj[i]|1<<i)
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
if dfs(av,tuple(need)):raise AssertionError('unexpected feasible relaxation')
# A validated 66-residue witness after removing only gcd4.
W=[0,14,30,60,74,104,110,164,165,180,224,270,284,300,314,344,360,390,404,434,440,494,495,510,614,630,644,674,690,720,770,780,825,840,884,924,930,944,960,974,1020,1064,1100,1155,1214,1260,1274,1304,1334,1380,1394,1424,1430,1440,1485,1590,1604,1664,1724,1754,1760,1815,1874,1914,1934,1964]
F=G-{4};assert len(set(W))==len(W)==66 and {0,14}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in F for y in Y) for x in W)
assert all(gcd(a-b,n) not in F for a,b in combinations(W,2))
assert [sum(x%m==r for x in W) for m,r in ((5,0),(5,4),(11,0))]==[33,33,15]
assert any(gcd(a-b,n)==4 for a,b in combinations(W,2))
print(json.dumps({'core_candidates':len(cand),'quotas':[33,33,15],
 'search':stats,'result':'UNSAT','control':'SAT after removing gcd4',
 'scope':'necessary 1980 P-size12 cyclic-border condition only'},indent=2))
