#!/usr/bin/env python3
"""Exact parity, matching and quota certificate for 1980 P33 branch."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
# Assuming Q avoids36, quantify its old-anchor-compatible candidates by mod5.
F=GA|{36};CQ={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
for r in (1,2,3):
 vals=[x for x in CQ if x%5==r];ev=[x for x in vals if x%2==0];odd=[x for x in vals if x%2]
 assert len(ev)==4
 if r in (1,3):
  assert all(sum(gcd(e-x,n) not in F for x in odd)<=6 for e in ev)
 else:
  assert all(sum(all(gcd(e-x,n) not in F for e in S) for x in odd)<=6 for S in combinations(ev,3))
# If Q uses36, P avoids36. Under additionally avoiding180, two 3-quotas
# have four candidates each, connected by a perfect 180-matching.
F=GY|{36,180}
p5={x for x in range(n) if x%11==5 and all(x==a or gcd(x-a,n) not in F for a in A)}
p9={x for x in range(n) if x%11==9 and all(x==a or gcd(x-a,n) not in F for a in A)}
assert p5=={423,1028,1688,1743} and p9=={603,1208,1868,1923}
matching=[(423,603),(1028,1208),(1688,1868),(1743,1923)]
assert {a for a,b in matching}==p5 and {b for a,b in matching}==p9
assert all(gcd(a-b,n)==180 for a,b in matching)
# Under avoiding36 and660, class9 has two 660-conflict triples.
F=GY|{36,660};p9={x for x in range(n) if x%11==9 and all(x==a or gcd(x-a,n) not in F for a in A)}
tri=[{548,1208,1868},{603,1263,1923}]
assert set.union(*tri)==p9 and all(gcd(a-b,n)==660 for t in tri for a,b in combinations(t,2))
# Q must then avoid GA,180,660 while meeting all mod4/mod5 quotas.
F=GA|{180,660};C=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
assert len(C)==332
N=len(C);idx={x:i for i,x in enumerate(C)}
adj=[sum(1<<j for j,y in enumerate(C) if y!=x and gcd(x-y,n) in F) for x in C]
groups=[sum(1<<i for i,x in enumerate(C) if x%4==r) for r in range(4)]+[sum(1<<i for i,x in enumerate(C) if x%5==r) for r in range(5)]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
av=(1<<N)-1;need=[15]*4+[12]*5
for x in sorted(Y):
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
 i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;n2=need.copy()
 for j in mem[i]:n2[j]-=1
 if dfs(av&~(adj[i]|b),tuple(n2)) or dfs(av&~b,tuple(need)):return True
 cache.add(key);return False
if dfs(av,tuple(need)):raise AssertionError('unexpected Q quota witness')
# Positive control: a 60-tail Q-only set satisfying all balances when gcd660
# is not forbidden; it deliberately contains gcd36 and gcd660.
W=[0,1,7,13,14,55,62,110,276,288,289,331,337,343,385,386,398,564,612,619,660,661,667,673,674,715,722,770,936,948,949,991,997,1003,1045,1046,1058,1224,1272,1279,1320,1321,1327,1333,1334,1375,1382,1430,1596,1608,1609,1651,1657,1663,1705,1706,1718,1884,1932,1939]
relax=GA|{180}
assert len(W)==len(set(W))==60 and Y<=set(W)
assert all(gcd(a-b,n) not in relax for a,b in combinations(W,2))
assert all(sum(x%4==r for x in W)==15 for r in range(4))
assert all(sum(x%5==r for x in W)==12 for r in range(5))
assert any(gcd(a-b,n)==660 for a,b in combinations(W,2))
print(json.dumps({'Q_forced_gcd':36,'P_forced_gcds':[180,660],
 'Q_core_candidates':N,'search':stats,'result':'UNSAT',
 'relaxed_control':'SAT after removing gcd660','scope':'n1980 P33 border branch'},indent=2))
