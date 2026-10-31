#!/usr/bin/env python3
"""Two independently oriented exact Hall counts for the 1320 Q=110 branch."""
from collections import Counter
from itertools import combinations
from math import comb,gcd
import json
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)}
QC={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
L=sorted(x for x in QC if x%11==0 and x!=0)
R=sorted(x for x in QC if x%11==3 and x!=14)
assert len(L)==len(R)==25
for x in R:assert gcd(x-0,n) not in GA
for x in L:assert gcd(x-14,n) not in GA

def neighborhood_counts(left,right,k):
    masks=[sum(1<<j for j,y in enumerate(right) if gcd(x-y,n) in {3,5,8}) for x in left]
    hist=Counter();arg=None;best=len(right)+1;count=0
    for group in combinations(range(len(left)),k):
        bits=0
        for i in group:bits|=masks[i]
        size=bits.bit_count();hist[size]+=1;count+=1
        if size<best:best=size;arg=[left[i] for i in group]
    assert count==comb(len(left),k)
    return {'subset_size':k,'subsets':count,'min_neighbors':best,'minimizers':hist[best],
            'example':arg,'histogram':dict(sorted(hist.items()))}

forward=neighborhood_counts(L,R,9)
reverse=neighborhood_counts(R,L,8)
assert forward['min_neighbors']==18 and forward['minimizers']==11
assert reverse['min_neighbors']==17 and reverse['minimizers']==10
print(json.dumps({'L_size':25,'R_size':25,'forward':forward,'reverse':reverse,
                  'scope':'exact finite two-class gcd-screen; no full completion'},indent=2))
