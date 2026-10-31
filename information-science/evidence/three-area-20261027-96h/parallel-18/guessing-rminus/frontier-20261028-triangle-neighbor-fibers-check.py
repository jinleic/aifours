#!/usr/bin/env python3
"""Exact F2 generator-rank check for ten-triangle neighbor fibers."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-triangle-neighbor-fibers-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def rank(rows):
    piv={}
    for row in rows:
        x=row
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)


def verify(neighbors=N,drop_row=None):
    if any(u not in neighbors[v] for v in neighbors for u in neighbors[v]):raise ValueError('ASYMMETRIC')
    if any(sum(v in tri for tri in TRI)!=3 for v in range(1,11)):raise ValueError('INCIDENCE')
    rows={v:[] for v in range(1,11)}
    for t,(a,b,c) in enumerate(TRI):
        if any(v not in neighbors[u] for u,v in combinations((a,b,c),2)):raise ValueError('TRIANGLE')
        rows[a].append(1<<(2*t));rows[b].append(1<<(2*t+1));rows[c].append((1<<(2*t))|(1<<(2*t+1)))
    results=[]
    for v in range(1,11):
        R=[(u,k,row) for u in neighbors[v] for k,row in enumerate(rows[u])]
        if drop_row is not None:R=[z for z in R if (v,z[0],z[1])!=drop_row]
        rankv=rank([x[2] for x in R]);expected=3*len(neighbors[v])
        if rankv!=expected:raise ValueError('NEIGHBOR_RANK')
        if any(set(tri)<=set(neighbors[v]) for tri in TRI):raise ValueError('NEIGHBOR_TRIANGLE')
        results.append({'vertex':v,'degree':len(neighbors[v]),'neighbor_bit_rank':rankv,'fiber_size':1<<(20-rankv)})
    sizes={x['vertex']:x['fiber_size'] for x in results};triangle_bounds=[]
    for tri in TRI:triangle_bounds.append({'triangle':tri,'disjoint_conflicting_fiber_lower_bound':sum(sizes[v] for v in tri)})
    if min(x['disjoint_conflicting_fiber_lower_bound'] for x in triangle_bounds)!=68:raise ValueError('MINIMUM')
    return {'factor_count':10,'source_bits':20,'codewords':1<<20,'vertices':results,'triangle_bounds':triangle_bounds,
            'minimum_forced_old_word_deletions_per_new_word':68}


def main():
    checks=verify();controls={}
    bad={v:tuple(ns) for v,ns in N.items()};bad[2]=tuple(sorted(bad[2]+(4,)));bad[4]=tuple(sorted(bad[4]+(2,)))
    for name,kwargs,reason in (
        ('removed_projection_row',{'drop_row':(1,2,0)},'NEIGHBOR_RANK'),
        ('added_k4_edge',{'neighbors':bad},'NEIGHBOR_RANK')):
        try:verify(**kwargs)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact binary linear projection ranks and factor incidence only; conflict-set disjointness and strategy consequences are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
