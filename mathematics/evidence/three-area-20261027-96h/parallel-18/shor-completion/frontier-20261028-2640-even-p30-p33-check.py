#!/usr/bin/env python3
"""Exact head candidate/block checks for n2640 P30 and P33 branches."""
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
V={x for x in P if x%3==1};T={x for x in V if x%5!=3};Z=V-T
assert len(V)==24 and len(T)==8 and len(Z)==16
assert len({x for x in V if x%11!=0})==8 and all(x%11==0 for x in Z)
# Four disjoint two-vertex blocker pairs; every Z has one full pair as
# a forbidden-gcd neighborhood, and no pair occurs for more than two Zs
# with exactly two blockers. Four-blocker vertices need >=4 omissions.
pairs=[{916,2236},{1075,2395},{256,1576},{415,1735}]
assert set.union(*pairs)==T and sum(map(len,pairs))==len(T)
blocks={z:{t for t in T if gcd(z-t,n) in GY} for z in Z}
assert all(len(b) in (2,4) for b in blocks.values())
assert all(b in pairs for b in blocks.values() if len(b)==2)
assert all(sum(b==p for b in blocks.values())==2 for p in pairs)
# Exhaustive 2^8 subsets independently verifies the resulting P30 capacity.
maximum=0
for size in range(9):
 for t in combinations(sorted(T),size):
  allowed=sum(not(blocks[z]&set(t)) for z in Z)
  maximum=max(maximum,size+min(4,allowed))
assert maximum==8
print(json.dumps({'P_mod3_1_candidates':len(V),'T':len(T),'Z':len(Z),
 'P33_upper_with_one_Z':len(T)+1,'P30_upper_with_four_Z':maximum,
 'scope':'n2640 even-Q P30/P33'},indent=2))
