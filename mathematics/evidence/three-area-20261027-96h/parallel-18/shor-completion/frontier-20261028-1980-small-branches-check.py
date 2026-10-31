#!/usr/bin/env python3
"""Exact screen/matching/quota checks for 1980 P sizes9,10,20,44."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
assert (len(P),len(Q))==(158,380)
# Size9: Q mod11 classes1,2 each require20; 17 disjoint conflict edges.
U={x for x in Q if x%11 in (1,2)};assert len(U)==56
match=[(937,948),(276,793),(398,541),(727,1046),(386,463),
       (1596,1861),(343,1827),(1608,1927),(871,1607),(1387,1706),
       (133,288),(1013,1597),(1718,1783),(1058,1531),(211,936),
       (331,387),(761,1453)]
assert len({v for e in match for v in e})==34 and all(a in U and b in U and gcd(a-b,n) in GA for a,b in match)
# Size20: five P mod4=2 are required, but at most two can lie in mod5=3
# after old anchors3,8 consume two of that class's total quota4.
P2=sorted(x for x in P if x%4==2)
assert len(P2)==11 and [x for x in P2 if x%5!=3]==[1070,1746]
# Size44: 11 P mod4=1 required; only 11 candidates, including an old-Q conflict.
P1=sorted(x for x in P if x%4==1)
assert len(P1)==11 and {33,921}<=set(P1) and gcd(33-921,n)==12 and 12 in GY
# Size10: Q is uniform mod9 and mod11; only quotas r9=8,r11=0 are retained.
C=sorted(x for x in Q if x%11==0 or x%9==8);assert len(C)==56
idx={x:i for i,x in enumerate(C)};N=len(C)
adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in GA) for x in C]
groups=[sum(1<<i for i,x in enumerate(C) if x%mod==r) for mod,r in ((11,0),(9,8))]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
av=(1<<N)-1;need=[18,22];i=idx[0];av &= ~(adj[i]|1<<i)
for j in mem[i]:need[j]-=1
stats={'nodes':0,'prunes':0};cache=set()
def dfs(av,need):
 stats['nodes']+=1;need=list(need)
 for j,k in enumerate(need):
  if k<0:return False
  if k==0:av &= ~groups[j]
 if any((av&groups[j]).bit_count()<k for j,k in enumerate(need)):
  stats['prunes']+=1;return False
 if not any(need):return True
 key=(av,tuple(need))
 if key in cache:return False
 j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&groups[j]).bit_count()-need[j],(av&groups[j]).bit_count()))
 bits=av&groups[j];vs=[]
 while bits:
  low=bits&-bits;bits-=low;vs.append(low.bit_length()-1)
 i=max(vs,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;n2=need.copy()
 for j in mem[i]:n2[j]-=1
 if dfs(av&~(adj[i]|b),tuple(n2)) or dfs(av&~b,tuple(need)):return True
 cache.add(key);return False
if dfs(av,tuple(need)):raise AssertionError('unexpected quota witness')
W=[0,80,89,170,179,231,269,297,330,350,359,377,449,561,620,627,629,660,710,728,800,890,891,957,990,1070,1160,1221,1287,1320,1340,1551,1610,1617,1650,1700,1718,1790,1881,1947]
F=GA-{4};assert len(W)==len(set(W))==40 and 0 in W
assert all(all(x==y or gcd(x-y,n) not in F for y in Y) for x in W)
assert all(gcd(a-b,n) not in F for a,b in combinations(W,2))
assert [sum(x%m==r for x in W) for m,r in ((11,0),(9,8))]==[18,22]
assert any(gcd(a-b,n)==4 for a,b in combinations(W,2))
print(json.dumps({'P_candidates':len(P),'Q_candidates':len(Q),'P9_conflict_matching':len(match),
 'P20_mod4_2_candidates':len(P2),'P44_mod4_1_candidates':len(P1),
 'P10_Q_core':N,'P10_search':stats,'P10_relaxed_control':'SAT after dropping gcd4',
 'scope':'only 1980 P sizes9,10,20,44'},indent=2))
