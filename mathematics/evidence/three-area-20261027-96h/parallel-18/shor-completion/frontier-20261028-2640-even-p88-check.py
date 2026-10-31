#!/usr/bin/env python3
"""Exact forced-gcd and relaxed slot proof for n2640 P88/Q30."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
def heads(j,H):return {x for x in range(n) if x%11==j and all(x==a or gcd(x-a,n) not in GY|H for a in A)}
# Avoiding 4: classes1,4 each have exactly8, forcing a gcd1 conflict.
L=heads(1,{4});R=heads(4,{4});assert len(L)==len(R)==8 and 155 in L and 576 in R and gcd(155-576,n)==1
# Avoiding55: omitting 456 or35 leaves 11 candidates, four disjoint 55-pairs,
# hence at most7 selected in the relevant class, below the quota8.
for j,forced,pairs in [(5,456,[(368,423),(1028,1083),(1688,1743),(2348,2403)]),
                       (2,35,[(68,123),(728,783),(1388,1443),(2048,2103)])]:
 S=heads(j,{55});assert len(S)==12 and forced in S
 assert len({x for p in pairs for x in p})==8 and all(a in S and b in S and gcd(a-b,n)==55 for a,b in pairs)
assert gcd(456-35,n)==1
# Avoiding240: two 10-candidate classes must provide 8 each, but five
# disjoint forbidden cross pairs permit at most15 of their20 endpoints.
L=heads(2,{240});R=heads(10,{240});assert len(L)==len(R)==10
pairs=[(35,1176),(68,1748),(123,1803),(783,2463),(816,395)]
assert len({x for p in pairs for x in p})==10 and all(a in L and b in R and gcd(a-b,n) in GY|{240} for a,b in pairs)
# Q must avoid the three forced P gcd classes and old head classes.
F=GA|{4,55,240};C={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
assert not any(x%5 in (0,4) and x%3==1 for x in C)
assert all(x%2 for x in C if x%5 in (1,2,3) and x%3==1)
N=sorted(x for x in C if x%5 in (1,2,3) and x%3!=1);assert len(N)==16
slots={}
for x in C:
 if x%5 in (1,2,3) and x%3==1:slots.setdefault((x%5,x%16),[]).append(x)
assert len(slots)==24
stats=Counter()
for S in combinations(N,8):
 stats['seeds']+=1
 if any(gcd(a-b,n) in F for a,b in combinations(S,2)):
  stats['internal_conflicts']+=1;continue
 if any(sum(x%5==r for x in S)>6 for r in (1,2,3)):
  stats['group_excess']+=1;continue
 opens={r:sum(any(all(gcd(x-y,n) not in F for y in S) for x in vals)
              for (r0,m16),vals in slots.items() if r0==r) for r in (1,2,3)}
 if any(opens[r]<6-sum(x%5==r for x in S) for r in (1,2,3)):
  stats['slot_shortage']+=1;continue
 stats['residual']+=1
assert (stats['seeds'],stats['internal_conflicts'],stats['group_excess'],stats['slot_shortage'],stats['residual'])==(12870,12657,33,180,0)
W=[1,7,13,33,231,241,247,481,493,627,721,733,973,1287,1367,1947,2343,2541]
R=GA|{4,55};assert len(W)==len(set(W))==18 and {1,7,13}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in R for y in Y) for x in W)
assert all(gcd(a-b,n) not in R for a,b in combinations(W,2))
assert all(sum(x%5==r for x in W)==6 for r in (1,2,3)) and sum(x%3==1 for x in W)==10
assert any(gcd(a-b,n)==240 for a,b in combinations(W,2))
print(json.dumps({'P_forced':[4,55,240],'Q_non1_candidates':len(N),'Q1_slots':len(slots),
 'seed_stats':dict(stats),'control':'SAT after removing 240','scope':'n2640 P88/Q30 only'},indent=2))
