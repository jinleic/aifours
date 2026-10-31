#!/usr/bin/env python3
"""Compact exact certificate: each half-BH graph has an isolated vertex
or is two odd K5 components. No generic matching solver is required.
"""
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
rows=('0000000000','0123424130','0241332104','0314234012','0432120314',
      '0322301441','0204411323','0131043422','0013142243','0440213231')
K=[list(map(int,row)) for row in rows]


def graph(half):
    adj=[set() for _ in range(10)]
    for a,b in combinations(range(10),2):
        diffs=[(K[t][a]-K[t][b])%5 for t in half]
        if len(set(diffs))==5:
            adj[a].add(b);adj[b].add(a)
    return adj


certificate=[]
for half in combinations(range(10),5):
    if 0 not in half:continue # complement yields identical graph
    complement=tuple(x for x in range(10) if x not in half)
    adj=graph(half)
    assert adj==graph(complement)
    isolated=[i for i in range(10) if not adj[i]]
    if isolated:
        certificate.append({'rows':half,'reason':'isolated','vertex':isolated[0]})
    else:
        assert half==(0,1,2,3,4)
        assert all(adj[i]==set(range(0,5))-{i} for i in range(5))
        assert all(adj[i]==set(range(5,10))-{i} for i in range(5,10))
        certificate.append({'rows':half,'reason':'two_disjoint_K5',
                            'parts':[[0,1,2,3,4],[5,6,7,8,9]]})
assert len(certificate)==126
assert sum(x['reason']=='isolated' for x in certificate)==125
assert sum(x['reason']=='two_disjoint_K5' for x in certificate)==1
out=ROOT/'frontier-20261028-butson-half-obstruction-cert-v1.json'
out.write_text(json.dumps({'matrix_exponent_rows':rows,'half_representatives':certificate,
  'complement_graph_identity':'verified by exact calculation',
  'scope':'this explicit BH10, all row permutations; not all BH10 matrices'},indent=2,sort_keys=True)+'\n')
print('PASS all126 half/complement pairs:125 isolated-vertex certificates,1 two-K5 certificate')
print('covers all252 five-row choices; no perfect matching')
print('wrote',out.name)
