#!/usr/bin/env python3
"""Check exact isolated/K5 witnesses for transpose and all complementary halves."""
from itertools import combinations
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('b',ROOT/'frontier-20261028-butson10-half-matching-v1.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
b.K=tuple(tuple(b.K[j][i] for j in range(10)) for i in range(10)); b.validate()
iso=odd=0
for half in combinations(range(10),5):
    if 0 not in half:continue
    comp=tuple(i for i in range(10) if i not in half)
    edges=b.half_graph(half)
    assert edges==b.half_graph(comp)
    adj=[set() for _ in range(10)]
    for x,y in edges:adj[x].add(y);adj[y].add(x)
    if any(not x for x in adj):iso+=1;continue
    remaining=set(range(10)); sizes=[]
    while remaining:
        queue=[min(remaining)]; component=set()
        while queue:
            node=queue.pop()
            if node in component:continue
            component.add(node);queue.extend(adj[node]-component)
        remaining-=component;sizes.append(len(component))
    assert sorted(sizes)==[5,5]
    odd+=1
assert iso==125 and odd==1
print('transpose all126 half/complement pairs:125 isolated,1 two odd components PASS')
