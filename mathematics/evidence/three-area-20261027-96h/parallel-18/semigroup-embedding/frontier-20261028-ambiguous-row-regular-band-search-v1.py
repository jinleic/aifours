#!/usr/bin/env python3
"""Bounded source-host search beyond row-label uniqueness, no all-host inference."""
import importlib.util
from pathlib import Path
from itertools import product
import sys
p=Path(__file__).with_name('frontier-20261028-obstruction-source-regular-band-search-v1.py')
spec=importlib.util.spec_from_file_location('old_search',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# One row has distinct 1 and 3 with the same group image; normalized first row/column.
m.P=((4,4,4),(4,1,3),(4,4,4))
def closure(g):
    c=set(g)
    while True:
        d=c|{m.mul(a,b) for a,b in product(c,repeat=2)}
        if d==c:return c
        c=d
g=[];c=set()
while len(c)<len(m.S):
    _,s=max((len(closure(g+[s])),s) for s in m.S if s not in c)
    g.append(s);c=closure(g)
m.G=tuple(g)
print('ambiguous-row P=',m.P,'source generators=',m.G,'closure=',len(c),flush=True)
lo,hi,ms=map(int,sys.argv[1:4])
for n in range(lo,hi+1):
    for pairs in range(n//2+1):
        if m.search(n,pairs,ms):sys.exit(0)
print('NO_WITNESS_IN_CONCLUDED_CASES; UNKNOWN is not a negative result',flush=True)
