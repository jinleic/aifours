#!/usr/bin/env python3
"""Finite small-k residue checks for odd P and even Q over 165*2^k."""
from itertools import combinations
from math import gcd
import json
A={0,3,8,11};Y={0,1,7,13,14};rows=[]
for k in range(2,6):
 n=165*(1<<k);GY={gcd(a-b,n) for a,b in combinations(Y,2)}
 P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
 c3=sum(x%3==1 for x in P);c5=sum(x%5==2 for x in P)
 rows.append({'k':k,'n':n,'P_mod3_1_candidates':c3,'P_mod5_2_candidates':c5})
assert [r['P_mod3_1_candidates'] for r in rows]==[6,12,24,48]
assert [r['P_mod5_2_candidates'] for r in rows]==[2,6,12,24]
n=2640;GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
L={x for x in P if x%5==2};R={x for x in P if x%5==4}
pairs=[(872,459),(2192,1779),(987,344),(2307,1664)]
assert len(L)==len(R)==12 and len({x for pair in pairs for x in pair})==8
assert all(a in L and b in R and gcd(a-b,n) in GY for a,b in pairs)
print(json.dumps({'small_k':rows,'P55_k4_conflict_pairs':pairs,
                  'scope':'finite controls for odd-P/even-Q classification'},indent=2))
