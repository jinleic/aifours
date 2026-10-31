#!/usr/bin/env python3
"""Enumerate every rank-six binary-character system required by m=192.

All calculations are exact bitsets. Mathematical reduction to these constraints
is separate; this program makes no claim about arbitrary group laws by itself.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-coset192-character-enumeration-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
V=tuple(range(1,11));EDGES=tuple((a,b) for a,b in combinations(V,2) if b in N[a])


def subspaces():
    all_spaces=set()
    for x in range(1,256):
        for y in range(x+1,256):all_spaces.add(tuple(sorted((0,x,y,x^y))))
    if len(all_spaces)!=10795:raise ValueError(('GAUSSIAN_BINOMIAL',len(all_spaces)))
    keep={R for R in all_spaces if all(not x or x.bit_count()>=3 for x in R)}
    if len(keep)!=6769:raise ValueError(('DISTINCT_NONZERO',len(keep)))
    return sorted(keep)


def subsets(mask):
    x=mask
    while True:
        yield x
        if not x:break
        x=(x-1)&mask


def canon(x,R):return min(x^r for r in R)


def edgecheck(edge,spaces):
    a,b=edge;others=[v for v in V if v not in edge];idx={v:i for i,v in enumerate(others)}
    na=sum(1<<idx[v] for v in N[a] if v in idx);nb=sum(1<<idx[v] for v in N[b] if v in idx)
    allowed=[];common=[]
    for i,v in enumerate(others):
        allowed.append((1<<i)|sum(1<<idx[w] for w in N[v] if w in idx))
        common.append(a in N[v] and b in N[v])
    base_survivors=0;candidate_s_cosets=0;solutions=[]
    for R in spaces:
        def relation(i,mask,off=0):return any((r^off)&(1<<i) and not ((r^off)&~mask) for r in R)
        if any(not common[i] and not relation(i,allowed[i]) for i in range(8)):continue
        base_survivors+=1
        aa={canon(t,R) for t in subsets(na)};bb={canon(t,R) for t in subsets(nb)}
        for t in sorted((aa&bb)-{0}):
            candidate_s_cosets+=1
            if all(not common[i] or relation(i,allowed[i]) or relation(i,allowed[i],t) for i in range(8)):
                solutions.append({'relation_subspace':R,'sign_coset_representative':t})
    return {'edge':edge,'binary_vertices':others,'common_neighbors':[others[i] for i in range(8) if common[i]],
            'baseline_relation_survivors':base_survivors,'exceptional_sign_cosets_tested':candidate_s_cosets,
            'solutions':solutions}


def main():
    if len(EDGES)!=26 or any(v not in N[w] for v in V for w in N[v]):raise ValueError('GRAPH')
    spaces=subspaces();results=[edgecheck(e,spaces) for e in EDGES]
    out={'graph_neighbors':{str(v):list(N[v]) for v in V},'edge_count':len(EDGES),
         'two_dimensional_relation_subspaces':10795,'nonzero_distinct_character_subspaces':len(spaces),
         'edges_checked':len(results),'total_baseline_relation_survivors':sum(x['baseline_relation_survivors'] for x in results),
         'total_exceptional_sign_cosets_tested':sum(x['exceptional_sign_cosets_tested'] for x in results),
         'total_solutions':sum(len(x['solutions']) for x in results),'edge_results':results,
         'limits':'Exact finite binary-character constraints only; the group-theoretic reduction and numerical index bound are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='edge_results'},indent=2))


if __name__=='__main__':main()
