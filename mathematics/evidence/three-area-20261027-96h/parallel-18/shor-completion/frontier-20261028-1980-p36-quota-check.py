#!/usr/bin/env python3
"""Exact finite certificate excluding the n1980 P-size36 border branch."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
PC=[x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)]
V=[x for x in PC if x%3==1]
assert len(V)==18
independent=[s for s in combinations(V,12) if all(gcd(a-b,n) not in GY for a,b in combinations(s,2))]
assert len(independent)==1
forced=independent[0];assert forced==(88,253,418,583,748,913,1078,1243,1408,1573,1738,1903)
H={165,330,495,660,990};assert H<={gcd(a-b,n) for a,b in combinations(forced,2)}
G=GA|H
cand=[x for x in range(n) if (x%5 in (0,4) or x%11 in (0,3)) and all(x==y or gcd(x-y,n) not in G for y in Y)]
assert len(cand)==170
N=len(cand);idx={x:i for i,x in enumerate(cand)}
adj=[sum(1<<j for j,y in enumerate(cand) if y!=x and gcd(x-y,n) in G) for x in cand]
groups=[sum(1<<i for i,x in enumerate(cand) if x%5==r) for r in (0,4)]+[sum(1<<i for i,x in enumerate(cand) if x%11==r) for r in (0,3)]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
av=(1<<N)-1;need=[11,11,5,5]
for x in (0,14):
 i=idx[x];assert av>>i&1;av &= ~(adj[i]|1<<i)
 for j in mem[i]:need[j]-=1
stats={'nodes':0,'prunes':0};cache=set()
def dfs(av,needs):
 stats['nodes']+=1;needs=list(needs)
 for j,k in enumerate(needs):
  if k<0:return False
  if k==0:av &= ~groups[j]
 if any((av&groups[j]).bit_count()<k for j,k in enumerate(needs)):stats['prunes']+=1;return False
 if not any(needs):return True
 key=(av,tuple(needs))
 if key in cache:return False
 j=min((j for j,k in enumerate(needs) if k),key=lambda j:((av&groups[j]).bit_count()-needs[j],(av&groups[j]).bit_count()))
 bits=av&groups[j];pool=[]
 while bits:
  low=bits&-bits;bits-=low;pool.append(low.bit_length()-1)
 i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;n2=needs.copy()
 for j in mem[i]:n2[j]-=1
 if dfs(av&~(adj[i]|b),tuple(n2)) or dfs(av&~b,tuple(needs)):return True
 cache.add(key);return False
if dfs(av,tuple(need)):raise AssertionError('unexpected quota solution')
W=[0,14,60,120,180,240,264,300,350,360,374,564,600,924,984,1010,1044,1224,1584,1670,1884,1944]
relax=G-{660}
assert len(set(W))==len(W)==22 and {0,14}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in relax for y in Y) for x in W)
assert all(gcd(x-y,n) not in relax for x,y in combinations(W,2))
assert [sum(x%m==r for x in W) for m,r in ((5,0),(5,4),(11,0),(11,3))]==[11,11,5,5]
assert any(gcd(a-b,n)==660 for a,b in combinations(W,2))
print(json.dumps({'P_mod3_1_candidates':len(V),'independent_12_subsets':len(independent),
 'forced':forced,'H':sorted(H),'core_candidates':len(cand),'search':stats,'result':'UNSAT',
 'control':'SAT after removing gcd660','scope':'only 1980 border P-size36'},indent=2))
