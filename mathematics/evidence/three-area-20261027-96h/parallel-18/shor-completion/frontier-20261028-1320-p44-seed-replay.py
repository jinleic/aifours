#!/usr/bin/env python3
"""Independent complement-seed replay of the 44-head tail contradiction."""
from itertools import combinations
from math import gcd
import json
N=1320;old=(0,1,7,13,14);head=(0,3,8,11)
H={gcd(a-b,N) for a,b in combinations(head,2)};forbidden=H|{55}
def conflict(a,b):return a!=b and gcd(a-b,N) in forbidden
C={x for x in range(N) if all(not conflict(x,y) for y in old)}
X={x for x in C if x%5 in (1,2,3) and x%3 in (0,2)}
assert len(X)==12 and all(x%3!=1 for x in C if x%5 in (0,4))
base={r:{x for x in C if x%5==r} for r in (0,4)}
count={'omitted':0,'conflict':0,'compatible':0,'balanced_pairs':0,'solutions':0}
for omitted in combinations(sorted(X),4):
    S=X-set(omitted);count['omitted']+=1
    if any(conflict(a,b) for a,b in combinations(S,2)):count['conflict']+=1;continue
    count['compatible']+=1
    a0={x for x in base[0] if all(not conflict(x,s) for s in S)}
    a4={x for x in base[4] if all(not conflict(x,s) for s in S)}
    assert 0 in a0 and 14 in a4
    # Reverse the group order and use sets rather than the producer's tuples.
    def legal_fives(universe,anchor):
        for xs in combinations(sorted(universe-{anchor}),5):
            group={anchor,*xs}
            if all(not conflict(a,b) for a,b in combinations(group,2)):yield group
    left=list(legal_fives(a0,0));right=list(legal_fives(a4,14))
    for B in right:
        for A in left:
            total=S|A|B
            if sum(x%3==0 for x in total)!=10 or sum(x%3==2 for x in total)!=10:continue
            count['balanced_pairs']+=1
            if all(not conflict(a,b) for a in A for b in B):count['solutions']+=1
assert (count['omitted'],count['conflict'],count['compatible'],count['solutions'])==(495,474,21,0)
print(json.dumps({'result':'UNSAT','counts':count,'scope':'separate exact complementary-seed replay'},indent=2))
