#!/usr/bin/env python3
"""Exact cover counts for the ten standard triangle factors."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-syndrome-cover-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def check(tri=TRI):
    if len(tri)!=10 or len(set(tri))!=10 or any(any(v not in N[u] for u,v in combinations(T,2)) for T in tri):raise ValueError('TRIANGLES')
    counts={str(k):0 for k in range(11)};minimum=[]
    for mask in range(1<<10):
        covered=set()
        for t,T in enumerate(tri):
            if mask>>t&1:covered.update(T)
        if covered==set(N):
            counts[str(mask.bit_count())]+=1
            if mask.bit_count()==4:minimum.append([i+1 for i in range(10) if mask>>i&1])
    expected={'0':0,'1':0,'2':0,'3':0,'4':19,'5':90,'6':145,'7':110,'8':45,'9':10,'10':1}
    if counts!=expected or len(minimum)!=19:raise ValueError('COVER_COUNTS')
    return {'factor_subsets_checked':1024,'cover_counts_by_size':counts,'minimum_cover_size':4,'minimum_covers':minimum}


def main():
    result=check();bad=list(TRI);bad[0]=(1,2,4)
    try:check(tuple(bad))
    except ValueError as exc:
        if str(exc)!='TRIANGLES':raise ValueError(('WRONG_REASON',str(exc)))
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'exact_checks':result,'all_checked':True,'controls':{'nontriangle_factor':'TRIANGLES'},
         'limits':'Finite graph/factor cover census only; the entropy tensorization is written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='minimum_covers'},indent=2))


if __name__=='__main__':main()
