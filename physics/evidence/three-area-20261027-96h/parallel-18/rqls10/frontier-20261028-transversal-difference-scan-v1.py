#!/usr/bin/env python3
"""Exact cyclic difference sets of published Latin resolutions.

This is an incidence scan, not a quantum-vector witness or all-L search.
"""
from collections import Counter
from itertools import combinations
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
n=10
Ls={
 'Weisner1':[[oa.w1.TABLE[r][c][1] for c in range(n)] for r in range(n)],
 'Weisner2':[[int(w[1]) for w in row.split()] for row in oa.w2.ROWS],
 'Weisner3-inferred00':[[int(w[1]) for w in row.split()] for row in oa.w3.ROWS],
 'Parker':[[int(oa.PARKER_B[r][c]) for c in range(n)] for r in range(n)],
 'cyclic-difference':[[(c-r)%n for c in range(n)] for r in range(n)],
}
for name,L in Ls.items():
    assert all(set(row)==set(range(n)) for row in L)
    assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
    counts=Counter()
    for t in range(n):
        block=[(r,c) for r in range(n) for c in range(n) if L[r][c]==t]
        assert len(block)==n
        for (r,c),(s,d) in combinations(block,2):
            counts[((r-s)%n,(c-d)%n)]+=1
            counts[((s-r)%n,(d-c)%n)]+=1
    assert all(a and b for a,b in counts)
    missing=[(a,b) for a in range(1,n) for b in range(1,n) if (a,b) not in counts]
    print(name,'distinct directed differences',len(counts),'of81',
          'min_frequency',min(counts.values()),'max_frequency',max(counts.values()),
          'missing',missing,flush=True)
