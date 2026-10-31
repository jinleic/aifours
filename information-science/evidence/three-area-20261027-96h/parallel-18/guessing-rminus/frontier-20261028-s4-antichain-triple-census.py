#!/usr/bin/env python3
"""Exact subgroup antichain / pairwise-intersection-triple census in S4."""
from collections import Counter,deque
from itertools import combinations,permutations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-s4-antichain-triple-census-result.json'


def group():
    elems=list(permutations(range(4)));identity=tuple(range(4));elems.remove(identity);elems.insert(0,identity)
    index={p:i for i,p in enumerate(elems)}
    table=[[index[tuple(p[q[i]] for i in range(4))] for q in elems] for p in elems]
    return elems,table


def generated(H,g,table):
    n=len(table);seen=H;known=[i for i in range(n) if H>>i&1];queue=deque()
    if not seen>>g&1:seen|=1<<g;known.append(g);queue.append(g)
    while queue:
        x=queue.popleft()
        for y in tuple(known):
            for z in (table[x][y],table[y][x]):
                if not seen>>z&1:seen|=1<<z;known.append(z);queue.append(z)
    return seen


def subgroups(table):
    known={1};todo=deque([1]);n=len(table)
    while todo:
        H=todo.popleft()
        for g in range(n):
            if not H>>g&1:
                J=generated(H,g,table)
                if J not in known:known.add(J);todo.append(J)
    out=sorted(known,key=lambda x:(x.bit_count(),x))
    for H in out:
        elements=[i for i in range(n) if H>>i&1]
        if not H&1 or any(not H>>table[a][b]&1 for a in elements for b in elements):raise ValueError('NOT_SUBGROUP')
    if len(out)!=30:raise ValueError('SUBGROUP_COUNT')
    return out


def enumerate_families(H):
    ids=[i for i,A in enumerate(H) if 1<A.bit_count()<24];n=len(ids);allow=[0]*n;meet=[0]*n
    for i,j in combinations(range(n),2):
        A,B=H[ids[i]],H[ids[j]]
        if A&B not in (A,B):allow[i]|=1<<j;allow[j]|=1<<i
        if A&B==1:meet[i]|=1<<j;meet[j]|=1<<i
    counts=[0]*(n+1);largest=[]
    def visit(chosen,candidates):
        counts[len(chosen)]+=1
        if len(chosen)>len(largest):largest[:]=chosen
        while candidates:
            bit=candidates&-candidates;i=bit.bit_length()-1;candidates-=bit
            neighbors=[j for j in chosen if meet[i]>>j&1]
            if any(meet[u]>>v&1 for u,v in combinations(neighbors,2)):continue
            visit(chosen+[i],candidates&allow[i])
    visit([], (1<<n)-1)
    if any(counts[10:]):raise ValueError('TEN_FAMILY')
    return ids,counts,[ids[i] for i in largest]


def main():
    elements,table=group();H=subgroups(table);ids,counts,largest=enumerate_families(H)
    proper_supers=[]
    for K in H:
        if K==1:continue
        candidates=[i for i,A in enumerate(H) if A!=K and A.bit_count()<24 and A&K==K]
        proper_supers.append({'K_mask':str(K),'K_order':K.bit_count(),'proper_strict_supergroups':len(candidates)})
        if len(candidates)>=10:raise ValueError('NONTRIVIAL_K')
    # Without the reconstruction-triangle exclusion, a ten-element antichain exists.
    control=[i for i,A in enumerate(H) if A.bit_count() in (2,3)][:10]
    if len(control)!=10 or any(H[i]&H[j] in (H[i],H[j]) for i,j in combinations(control,2)) or not any(H[i]&H[j]==H[i]&H[k]==H[j]&H[k]==1 for i,j,k in combinations(control,3)):raise ValueError('CONTROL')
    out={'group':'S4','elements':[list(p) for p in elements],'subgroup_masks':[str(x) for x in H],
         'subgroup_order_counts':dict(sorted(Counter(x.bit_count() for x in H).items())),
         'nontrivial_K_cases':proper_supers,'maximum_proper_strict_supergroups_nontrivial_K':max(x['proper_strict_supergroups'] for x in proper_supers),
         'trivial_K_candidate_subgroups':len(ids),'incomparable_no_reconstruction_triangle_families_by_size':counts[:11],
         'largest_family_subgroup_indices':largest,'all_checked':True,
         'controls':{'ten_antichain_without_triangle_gate':control},
         'limits':'Exact S4 subgroup lattice and finite family census only; the graph-entropy implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('elements','subgroup_masks','nontrivial_K_cases')},indent=2))


if __name__=='__main__':main()
