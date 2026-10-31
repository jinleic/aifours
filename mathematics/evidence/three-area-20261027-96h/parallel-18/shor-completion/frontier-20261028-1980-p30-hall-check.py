#!/usr/bin/env python3
"""Finite two-way Hall certificate for the 1980 P30 branch."""
from collections import Counter
from itertools import combinations
from math import comb,gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V=sorted(x for x in P if x%5==4)
assert V==[264,539,924,1119,1199,1584,1664,1859]
triangles=[(264,924,1584),(539,1199,1859)]
assert all(gcd(a-b,n)==660 for t in triangles for a,b in combinations(t,2))
F=GA|{660}
Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
L=sorted(x for x in Q if x%11==0 and x!=0);R=sorted(x for x in Q if x%11==3 and x!=14)
assert len(L)==len(R)==27

def count(left,right):
 mask={x:sum(1<<j for j,y in enumerate(right) if gcd(x-y,n) in F) for x in left}
 hist=Counter();total=compatible=0
 for S in combinations(left,5):
  total+=1
  if any(gcd(a-b,n) in F for a,b in combinations(S,2)):continue
  compatible+=1;blocked=0
  for x in S:blocked|=mask[x]
  hist[len(right)-blocked.bit_count()]+=1
 assert total==comb(27,5)==80730 and compatible==1458
 assert dict(hist)=={3:1332,4:126}
 return {'total':total,'compatible':compatible,'available_other_side':dict(sorted(hist.items()))}
print(json.dumps({'P_mod5_4_candidates':V,'P_forced_gcd':660,
 'forward':count(L,R),'reverse':count(R,L),
 'scope':'necessary border obstruction at n1980 P-size30'},indent=2))
