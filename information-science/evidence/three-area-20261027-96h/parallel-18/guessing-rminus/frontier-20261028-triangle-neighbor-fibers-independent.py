#!/usr/bin/env python3
"""Independent per-factor projection count for pinned triangle neighbor fibers."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-triangle-neighbor-fibers-check-result.json','09165f77dc480be2463290cb532da5d8fed04a366404f86a3edb6327af1156a7')
OUT=ROOT/'frontier-20261028-triangle-neighbor-fibers-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def compute(neighbors=N):
    data=[]
    for v in range(1,11):
        counts=[len(set(T)&set(neighbors[v])) for T in TRI]
        if any(k>2 for k in counts):raise ValueError('NEIGHBOR_FULL_FACTOR')
        if sum(counts)!=3*len(neighbors[v]):raise ValueError('INCIDENCE')
        data.append({'vertex':v,'degree':len(neighbors[v]),'factor_projection_sizes':counts,
                     'rank':sum(counts),'fiber_size':2**sum(2-k for k in counts)})
    d={x['vertex']:x['fiber_size'] for x in data};bounds=[]
    for T in TRI:
        if any(v not in neighbors[u] for u,v in combinations(T,2)):raise ValueError('TRIANGLE')
        bounds.append(sum(d[v] for v in T))
    if min(bounds)!=68:raise ValueError('MINIMUM')
    return data,bounds


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);data,bounds=compute();checked=src['exact_checks']
    if not src['all_checked'] or [(x['vertex'],x['rank'],x['fiber_size']) for x in data]!=[(x['vertex'],x['neighbor_bit_rank'],x['fiber_size']) for x in checked['vertices']] or bounds!=[x['disjoint_conflicting_fiber_lower_bound'] for x in checked['triangle_bounds']]:raise ValueError('MISMATCH')
    bad={v:tuple(ns) for v,ns in N.items()};bad[2]=tuple(sorted(bad[2]+(4,)));bad[4]=tuple(sorted(bad[4]+(2,)))
    try:compute(bad)
    except ValueError as exc:
        if str(exc)!='NEIGHBOR_FULL_FACTOR':raise ValueError(('WRONG_REASON',str(exc)))
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'vertices':data,'triangle_bounds':bounds,'minimum_conflicts':min(bounds),
         'all_checked':True,'controls':{'added_k4_edge':'NEIGHBOR_FULL_FACTOR'},
         'limits':'Exact independent factorwise projection count only; conflict disjointness and finite-strategy implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'vertices_checked':len(data),'triangles_checked':len(bounds),'minimum_conflicts':min(bounds),'all_checked':True,'controls':out['controls']},indent=2))


if __name__=='__main__':main()
