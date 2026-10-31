#!/usr/bin/env python3
"""Exact screened-residue certificate for n2640 P48 border branch."""
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
expected={1:{33,913,1793},2:{418,1298,2178},5:{693,1573,2453},9:{473,1353,2233}}
for r,v in expected.items():assert {x for x in P if x%16==r}==v
forced=A|set.union(*expected.values());H={15,30,55,66,660,1320}
assert H<={gcd(a-b,n) for a,b in combinations(forced,2)}
F=GA|H
Q7={x for x in range(n) if x%11==7 and all(x==y or gcd(x-y,n) not in F for y in Y)}
assert Q7=={7,337,997,1657,2317} and gcd(337-997,n)==660
print(json.dumps({'forced_classes':{str(r):sorted(v) for r,v in expected.items()},
 'forced_gcds':sorted(H),'Q_mod11_7':sorted(Q7),'contradiction_gcd':660,
 'scope':'n2640 P-size48 only'},indent=2))
