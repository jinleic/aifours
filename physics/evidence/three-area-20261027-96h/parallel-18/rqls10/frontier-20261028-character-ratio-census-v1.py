#!/usr/bin/env python3
"""Exact small-prime permutation counts; no continuous impossibility claim."""
from itertools import permutations
for p in (3,5):
    affine=[];nonaffine=[]
    for s in permutations(range(p)):
        good=all((s[j]-s[0])%p==((s[1]-s[0])*j)%p for j in range(p))
        (affine if good else nonaffine).append(s)
    print('p',p,'permutations',len(affine)+len(nonaffine),'affine',len(affine),'nonaffine',len(nonaffine))
    assert (len(affine),len(nonaffine))==({3:(6,0),5:(20,100)}[p])
print('PASS permutation census; continuous character-ratio contradiction is written separately')
