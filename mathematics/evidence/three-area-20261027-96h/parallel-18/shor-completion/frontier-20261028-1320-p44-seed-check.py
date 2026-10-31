#!/usr/bin/env python3
"""Exact relaxed seed certificate excluding the 1320 |P|=44 border branch."""
from collections import Counter
from itertools import combinations
from math import comb,gcd
import json
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
PC={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
QC={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
# If P avoids class55, 4-of-6 choices in classes 1,2 mod11 force 155 and816.
C1=sorted(x for x in PC if x%11==1);C2=sorted(x for x in PC if x%11==2)
assert C1==[155,188,243,848,903,936] and C2==[35,68,123,728,783,816]
for vals,required in ((C1,155),(C2,816)):
    choices=[s for s in combinations(vals,4) if all(gcd(a-b,n)!=55 for a,b in combinations(s,2))]
    assert len(choices)==2 and all(required in s for s in choices)
assert gcd(155-816,n)==1 and 1 in GY
# Assume Q avoids 55; filter candidates against its five old anchors.
G=GA|{55}
C={x for x in QC if all(x==y or gcd(x-y,n) not in G for y in Y)}
assert not any(x%5 in (0,4) and x%3==1 for x in C)
extras=sorted(x for x in C if x%5 in (1,2,3) and x%3!=1)
assert extras==[47,363,443,561,627,641,693,707,773,891,971,1287]
base={r:sorted(x for x in C if x%5==r) for r in (0,4)}
assert all(len(base[r])==70 for r in (0,4))

def okay(group):return all(gcd(a-b,n) not in G for a,b in combinations(group,2))
stats=Counter();variants=Counter();witness=None
for seed in combinations(extras,8):
    stats['seeds']+=1
    if not okay(seed):stats['seed_conflicts']+=1;continue
    stats['compatible_seeds']+=1
    avail={r:[x for x in base[r] if all(gcd(x-y,n) not in G for y in seed)] for r in (0,4)}
    def choices(r,anchor):
        assert anchor in avail[r]
        return [(anchor,)+s for s in combinations((x for x in avail[r] if x!=anchor),5)
                if okay((anchor,)+s)]
    left=choices(0,0);right=choices(4,14);variants[(len(left),len(right))]+=1
    for x in left:
        for y in right:
            if any(sum(z%3==r for z in seed+x+y)!=10 for r in (0,2)):continue
            stats['balanced_pairs']+=1
            if all(gcd(a-b,n) not in G for a in x for b in y):witness=(seed,x,y);break
        if witness:break
    if witness:break
assert witness is None
assert (stats['seeds'],stats['seed_conflicts'],stats['compatible_seeds'])==(comb(12,8),474,21)
# Positive control: drop only the extra gcd55 requirement; the retained old
# anchors are treated as present, and all relaxed quotas are checked directly.
W=[0,14,54,68,120,240,288,360,386,600,614,674,716,722,840,936,1004,1052,1058,1224]
assert len(W)==len(set(W))==20 and {0,14}<=set(W)
assert all(x in QC for x in W) and all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert [sum(x%mod==r for x in W) for mod,r in ((5,0),(5,4),(3,0),(3,2))]==[6,6,10,10]
assert any(x!=y and gcd(x-y,n)==55 for x in W for y in Y)
print(json.dumps({'seed_statistics':dict(stats),'variant_histogram':{str(k):v for k,v in sorted(variants.items())},
 'result':'UNSAT','control':'SAT with gcd55 removed','scope':'necessary 1320 cyclic-border constraints'},indent=2))
