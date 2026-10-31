#!/usr/bin/env python3
"""Exact independent-vertex triples and triangle-syndrome hyperplane maps."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-syndrome-hyperplane-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def check(triples):
    seen=set();rows=[]
    for I in triples:
        if len(I)!=3 or any(v in N[u] for u,v in combinations(I,2)):raise ValueError('NOT_INDEPENDENT')
        occ=[sum(v in T for v in I) for T in TRI]
        if any(x>1 for x in occ) or sum(occ)!=9 or occ.count(0)!=1:raise ValueError('SYNDROME_RANK')
        missing=occ.index(0)+1
        if missing in seen:raise ValueError('DUPLICATE_FACTOR')
        seen.add(missing);rows.append({'independent_vertices':I,'missing_factor_one_based':missing,'syndrome_rank':sum(occ),'clique_size':8**3})
    if seen!={1,2,3,6,8,10}:raise ValueError('FACTORS')
    return rows


def main():
    triples=[I for I in combinations(range(1,11),3) if all(v not in N[u] for u,v in combinations(I,2))]
    if len(triples)!=6:raise ValueError('TRIPLE_COUNT')
    rows=check(triples);bad=triples.copy();bad[0]=(1,2,3)
    try:check(bad)
    except ValueError as exc:
        if str(exc)!='NOT_INDEPENDENT':raise ValueError(('WRONG_REASON',str(exc)))
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'independent_vertex_triples':rows,'hyperplane_cosets':2**20,'clique_size':2**9,'all_checked':True,
         'controls':{'triangle_replacing_independent_triple':'NOT_INDEPENDENT'},
         'limits':'Exact graph/factor incidence only; clique tiling and cardinality argument is written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
