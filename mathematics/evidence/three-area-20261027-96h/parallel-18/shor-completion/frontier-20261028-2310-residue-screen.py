#!/usr/bin/env python3
"""Exact static candidate, matching and parity checks for 2310 borders."""
from itertools import combinations
from math import gcd
import json
n=2310;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
assert GA=={2,3,5,11} and GY=={1,6,7,14}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
assert (len(P),len(Q))==(248,409)
D=[d for d in range(8,len(P)+1) if n%d==0 and n//d<=len(Q)]
filtered=[]
for d in D:
 q=n//d;ok=True
 for p in (2,3,5,7,11):
  vec=P if d%p==0 else Q;old=A if d%p==0 else Y;k=(d if d%p==0 else q)//p
  if min(sum(x%p==r for x in vec) for r in range(p))<k:ok=False
  if max(sum(x%p==r for x in old) for r in range(p))>k:ok=False
 if ok:filtered.append(d)
assert filtered==[10,14,15,21,22,30,33,35,42,55,66,70,77,154]
# If Q is even and 3-divisible, all but these four odd candidates are 1 mod3.
assert sorted(x for x in Q if x%6 in (3,5))==[651,903,1421,1673]
# The mod3=1 head class has 24 vertices and 10 disjoint conflict pairs.
V={x for x in P if x%3==1};assert len(V)==24
edges=[(85,1243),(256,1078),(415,913),(586,1408),(916,88),
       (1405,253),(1735,583),(1906,418),(2065,1573),(2236,748)]
assert len({x for e in edges for x in e})==20 and all(a in V and b in V and gcd(a-b,n) in GY for a,b in edges)
# P33: 11 heads in V; mod11 class0 contains old 0 and11, leaving one slot.
T={x for x in V if x%11!=0};Z=V-T;assert len(T)==10 and len(Z)==14
block={88:586,253:415,418:256,583:85,748:256,913:85,1078:256,1243:85,
       1408:256,1573:85,1738:256,1903:85,2068:256,2233:85}
assert set(block)==Z and all(t in T and gcd(z-t,n) in GY for z,t in block.items())
# P70 forces all candidates in mod5 classes2 and4; one old-tail conflict.
assert sum(x%5==2 for x in P)==sum(x%5==4 for x in P)==14
assert 1977 in P and 1977%5==2 and 344 in P and 344%5==4 and gcd(1977-344,n) in GY
# P154 forces all candidates in mod11 classes1 and6.
assert sum(x%11==1 for x in P)==sum(x%11==6 for x in P)==14
assert 1145 in P and 1145%11==1 and 336 in P and 336%11==6 and gcd(1145-336,n) in GY
print(json.dumps({'P_candidates':len(P),'Q_candidates':len(Q),'prime_filtered':filtered,
 'odd_non1_tail_candidates':4,'P_mod3_1_capacity_bound':14,'P33_blocked_last_slots':len(Z),
 'P70_and_P154_forced_conflicts':'PASS','scope':'static 2310 necessary-border screen only'},indent=2))
