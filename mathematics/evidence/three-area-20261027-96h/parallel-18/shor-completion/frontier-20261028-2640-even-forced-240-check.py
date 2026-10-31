#!/usr/bin/env python3
"""Exact P quota relaxation forcing gcd240 at order2640."""
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
F=GY|{240};rs=(2,10,9,7,3)
C=[x for x in range(n) if x%11 in rs and all(x==a or gcd(x-a,n) not in F for a in A)]
assert len(C)==63
N=len(C);idx={x:i for i,x in enumerate(C)}
adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
groups=[sum(1<<i for i,x in enumerate(C) if x%11==r) for r in rs]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
av=(1<<N)-1;need=[2]*5;i=idx[3];av &= ~(adj[i]|1<<i)
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
if dfs(av,tuple(need)):raise AssertionError('unexpected head quota witness')
W=[3,35,68,128,183,395,428,515,548,608]
assert len(W)==len(set(W))==10 and 3 in W
assert all(all(x==a or gcd(x-a,n) not in GY for a in A) for x in W)
assert all(gcd(a-b,n) not in GY for a,b in combinations(W,2))
assert all(sum(x%11==r for x in W)==2 for r in rs)
assert any(gcd(a-b,n)==240 for a,b in combinations(W,2))
print(json.dumps({'P_core':N,'search':stats,'result':'UNSAT','forced_gcd':240,
 'control':'SAT after removing240','scope':'any P with >=2 heads in each named mod11 class'},indent=2))
