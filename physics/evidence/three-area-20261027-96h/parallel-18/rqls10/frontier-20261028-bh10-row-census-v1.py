#!/usr/bin/env python3
"""Exact dephased BH(10,5) row-candidate census after canonical second row."""
from collections import Counter
from pathlib import Path
import json

SECOND=(0,0,1,1,2,2,3,3,4,4)
counts=[1,2,2,2,2]
candidates=[]
visited=0

def rec(v):
    global visited
    if len(v)==10:
        visited+=1
        if Counter((v[i]-SECOND[i])%5 for i in range(10))==Counter({j:2 for j in range(5)}):
            candidates.append(tuple(v))
        return
    for x in range(5):
        if counts[x]:
            counts[x]-=1;rec(v+[x]);counts[x]+=1

rec([0])
assert visited==22680
print('all dephased balanced rows',visited)
print('rows orthogonal to canonical second row',len(candidates))
out=Path(__file__).resolve().parent/'frontier-20261028-bh10-row-census-v1.json'
out.write_text(json.dumps({'canonical_second_row':SECOND,'rows':candidates,
 'count':len(candidates),'scope':'row candidates only; not a BH classification'},separators=(',',':'))+'\n')
print('wrote',out.name)
