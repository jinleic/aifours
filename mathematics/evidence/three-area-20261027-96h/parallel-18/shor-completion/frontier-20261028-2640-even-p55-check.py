#!/usr/bin/env python3
"""Exact old-anchor matching obstruction for n2640 P55/Q48."""
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
L={x for x in P if x%5==2};R={x for x in P if x%5==4}
match=[(872,459),(2192,1779),(987,344),(2307,1664)]
assert len(L)==len(R)==12 and len({x for p in match for x in p})==8
assert all(a in L and b in R and gcd(a-b,n) in GY for a,b in match)
print(json.dumps({'class2_candidates':len(L),'class4_candidates':len(R),
                  'disjoint_conflict_pairs':match,'scope':'n2640 P55 even-Q branch'},indent=2))
