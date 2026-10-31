#!/usr/bin/env python3
"""Check all half-row matchings for the TRANSPOSE of explicit BH(10,5)."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('b',ROOT/'frontier-20261028-butson10-half-matching-v1.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
b.K=tuple(tuple(b.K[j][i] for j in range(10)) for i in range(10))
b.validate()
hist=Counter();matched=[]
for rows in combinations(range(10),5):
    edges=b.half_graph(rows);m=b.matching(edges)
    hist[len(edges)]+=1
    if m is not None:matched.append((rows,m))
print('transposed BH10 exact orthogonality: PASS')
print('all252 half-row edge-count histogram',dict(sorted(hist.items())))
print('perfect matchings',len(matched),'first',matched[0] if matched else None)
