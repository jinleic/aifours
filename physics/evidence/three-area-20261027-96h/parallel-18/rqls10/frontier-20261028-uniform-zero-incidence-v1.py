#!/usr/bin/env python3
"""Check zero-pattern incidence on two validated Latin resolutions.

This checks symbolic supports required IF a uniform physical lift exists;
it constructs no such lift and is not an exhaustive all-L proof.
"""
from collections import Counter
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)
n=10
Ls={'Weisner1':[[oa.w1.TABLE[r][c][1] for c in range(n)] for r in range(n)],
    'Parker1959':[[int(oa.PARKER_B[r][c]) for c in range(n)] for r in range(n)]}
for name,L in Ls.items():
    assert all(set(row)==set(range(n)) for row in L)
    assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
    partners=Counter()
    for r0 in range(n):
        inverse={L[r0][c]:c for c in range(n)}
        zero={}
        for r in range(n):
            if r==r0: continue
            for c in range(n):
                j=inverse[L[r][c]]
                assert j!=c
                zero[(r,c)]=frozenset((c,j))
        paircounts=Counter(zero.values())
        assert len(paircounts)==45 and set(paircounts.values())=={2}
        for (r,c),zx in zero.items():
            candidates=[(s,d) for (s,d),zy in zero.items()
                        if s!=r and d!=c and L[s][d]!=L[r][c]
                        and len(zx & zy)==1]
            assert len(candidates)>=7
            partners[len(candidates)]+=1
    print(name,'all10 reference rows: every unordered zero pair occurs twice; PASS')
    print(name,'900 nonreference cells, nonsharing one-common-zero partner counts',dict(sorted(partners.items())))
print('Finite checks only: general all-L counting requires the written proof.')
