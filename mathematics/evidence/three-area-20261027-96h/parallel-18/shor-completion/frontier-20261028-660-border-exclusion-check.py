#!/usr/bin/env python3
"""Finite gcd/residue certificates for Shor-border order660 obstruction."""
from itertools import combinations
from math import gcd
import json
n=660;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
assert GA=={3,4,5,11} and GY=={1,2,6,12}
PC={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
assert len(PC)==42 and sum(x%3==1 for x in PC)==6 and sum(x%5==2 for x in PC)==2
assert [x for x in sorted(PC) if x%11==1]==[188,243]
# P10: four heads forced by 5-uniformity, generating classes55 and132.
c2=sorted(x for x in PC if x%5==2);c4=sorted(x for x in PC if x%5==4)
assert c2==[132,407] and c4==[264,539]
assert gcd(132-407,n)==55 and gcd(132-0,n)==132
G10=GA|{55,132}
Q10={x for x in range(n) if all(x==y or gcd(x-y,n) not in G10 for y in Y)}
assert not any(x%6==4 for x in Q10)
slots={(x%11,x%4) for x in Q10 if x%3==1}
assert len(slots)==18 and all(r in (1,3) for _,r in slots)
# P12: 4-uniformity forces all candidates in mod4 classes1,2.
f1=sorted(x for x in PC if x%4==1);f2=sorted(x for x in PC if x%4==2)
assert f1==[33,253,473] and f2==[198,418,638]
F=set(f1+f2);assert {55,165,220}<={gcd(a-b,n) for a,b in combinations(F,2)}
G12=GA|{55,165,220}
Q12={x for x in range(n) if all(x==y or gcd(x-y,n) not in G12 for y in Y)}
L=sorted(x for x in Q12 if x%11==0 and x!=0);R=sorted(x for x in Q12 if x%11==3 and x!=14)
assert L==[44,110,264,374,594,627] and R==[47,80,300,410,564,630]
matching=[(110,47),(264,80),(594,410),(627,564),(374,630),(44,300)]
assert {a for a,b in matching}==set(L) and {b for a,b in matching}==set(R)
assert all(gcd(a-b,n) in G12 for a,b in matching)
# P22: 11-uniformity forces 188,243 and their gcd55.
assert gcd(188-243,n)==55
G22=GA|{55}
Q22={x for x in range(n) if all(x==y or gcd(x-y,n) not in G22 for y in Y)}
assert not any(x%5 in (0,4) and x%3==1 for x in Q22)
extra=sorted(x for x in Q22 if x%5 in (1,2,3) and x%3!=1)
assert extra==[47,627]
print(json.dumps({'P_candidates':len(PC),'P_mod3_1_capacity':6,'P_mod5_2_capacity':2,
 'P10_Q1_slots':len(slots),'P12_matching':matching,'P22_extra_non1':extra,
 'scope':'exact finite anchor and gcd-class identities, not an all-order completion'},indent=2))
