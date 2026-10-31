#!/usr/bin/env python3
"""Exact 3x3 sub-OLS census of four source-backed order-10 arrays.

Enumerates only row/column triples in these four finite input arrays; this is
not evidence of exhaustive classification of all order-10 orthogonal arrays.
"""
from itertools import combinations
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('oa',ROOT/'frontier-20261028-coordinate-switch-v1.py')
oa=importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)
n=10

def data_from_rows(rows):
    return [[tuple(map(int,w)) for w in row.split()] for row in rows]

data={
 'Weisner1963-Fig1':[[oa.w1.TABLE[r][c] for c in range(n)] for r in range(n)],
 'Weisner1963-Fig2':data_from_rows(oa.w2.ROWS),
 'Weisner1963-Fig3-inferred00':data_from_rows(oa.w3.ROWS),
 'Parker1959-section3':[[(int(oa.PARKER_A[r][c]),int(oa.PARKER_B[r][c]))
                          for c in range(n)] for r in range(n)],
}
result=[]
for name,table in data.items():
    points=tuple((r,c,*table[r][c]) for r in range(n) for c in range(n))
    oa.check_oa(points)
    pockets=[]
    for rr in combinations(range(n),3):
        for cc in combinations(range(n),3):
            cells=[(r,c) for r in rr for c in cc]
            a={table[r][c][0] for r,c in cells}
            b={table[r][c][1] for r,c in cells}
            if len(a)==3 and len(b)==3:
                assert len({table[r][c] for r,c in cells})==9
                pockets.append({'rows':list(rr),'columns':list(cc),
                                'colors':sorted(a),'labels':sorted(b)})
    disjoint=0
    for x,y in combinations(pockets,2):
        if set(x['rows']).isdisjoint(y['rows']) or set(x['columns']).isdisjoint(y['columns']):
            disjoint+=1
    item={'source':name,'pockets':pockets,'disjoint_cell_pairs':disjoint}
    result.append(item)
    print(name,'OA3 pockets',len(pockets),'disjoint pairs',disjoint)
    for pocket in pockets: print(' ',pocket)

# Universal counting consequences for two disjoint OA3s in OA(4,10,2).
for t in range(4):
    a=84-3*t
    intersection=108-14*t
    a_only=a-intersection
    neither=22-8*t
    print('shared-axis intersection',t,'outside A',a,'A_and_B',intersection,
          'A_only',a_only,'neither',neither,'impossible',a_only<0 or neither<0)
    assert a_only<0 or neither<0
path=ROOT/'frontier-20261028-suboa-census-result-v1.json'
path.write_text(json.dumps({'arrays':result,'claim':'finite census only'},indent=2,sort_keys=True)+'\n')
print('wrote',path.name)
