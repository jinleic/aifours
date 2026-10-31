#!/usr/bin/env python3
"""Recheck the stated 10th-root odd-sum and F5 complete-map lemmas exactly."""
from itertools import combinations_with_replacement,product
from collections import Counter
for length in (1,3,5):
    zero=0;total=0
    for v in combinations_with_replacement(range(10),length):
        total+=1
        signed=[0]*5
        for k in v:signed[(3*k)%5]+=(-1)**k
        if len(set(signed))==1:
            zero+=1
            assert length==5
            assert len({k%2 for k in v})==1
            assert len({(3*k)%5 for k in v})==5
    print('root-sum length',length,'multisets',total,'zero',zero)
for g in product(range(5),repeat=5):
    good=[d for d in range(5) if len({(g[t]+d*t)%5 for t in range(5)})==5]
    affine=all((g[t]-g[0])%5==((g[1]-g[0])*t)%5 for t in range(5))
    assert len(good)<=1 or affine
print('PASS all3125 functions: two good shifts imply affine')
