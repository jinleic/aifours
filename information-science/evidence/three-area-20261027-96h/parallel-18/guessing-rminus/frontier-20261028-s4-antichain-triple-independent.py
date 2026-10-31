#!/usr/bin/env python3
"""Independent inverse-closed-set subgroup enumeration and family replay."""
from hashlib import sha256
from itertools import combinations,permutations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-s4-antichain-triple-census-result.json','cd4d16622d7c56bebbc396295542fe7e1d78a274809e9ec0805c21b0889ad282')
OUT=ROOT/'frontier-20261028-s4-antichain-triple-independent-result.json'


def pin():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    return json.loads(raw)


def group():
    elems=[tuple(range(4))]+[p for p in permutations(range(4)) if p!=tuple(range(4))];idx={p:i for i,p in enumerate(elems)}
    table=[[idx[tuple(a[b[k]] for k in range(4))] for b in elems] for a in elems]
    inverse=[next(j for j in range(24) if table[i][j]==0 and table[j][i]==0) for i in range(24)]
    return elems,table,inverse


def all_subgroups(table,inverse):
    unseen=set(range(1,24));orbits=[]
    while unseen:
        x=min(unseen);orb={x,inverse[x]};orbits.append(orb);unseen-=orb
    if len(orbits)!=16:raise ValueError(('INVERSE_ORBITS',len(orbits)))
    masks=[];candidates=0
    for pick in range(1<<len(orbits)):
        members=[0]
        for j,orb in enumerate(orbits):
            if pick>>j&1:members.extend(orb)
        if 24%len(members):continue
        candidates+=1;S=set(members)
        if all(table[a][b] in S for a in members for b in members):masks.append(sum(1<<a for a in members))
    if len(masks)!=30:raise ValueError(('SUBGROUPS',len(masks)))
    return set(masks),len(orbits),candidates


def compatible_family(indices,H):
    if any(H[i]&H[j] in (H[i],H[j]) for i,j in combinations(indices,2)):return False
    if any(H[i]&H[j]==H[i]&H[k]==H[j]&H[k]==1 for i,j,k in combinations(indices,3)):return False
    return True


def family_counts(H):
    ids=[i for i,h in enumerate(H) if 1<h.bit_count()<24];counts=[0]*11;nodes=0
    def visit(pos,chosen):
        nonlocal nodes
        nodes+=1
        if len(chosen)>10:raise ValueError('TEN_OR_MORE')
        if pos==len(ids):counts[len(chosen)]+=1;return
        visit(pos+1,chosen)
        i=ids[pos]
        if compatible_family(chosen+[i],H):visit(pos+1,chosen+[i])
    visit(0,[])
    return counts,nodes


def main():
    src=pin();elements,table,inverse=group();masks,inverse_orbits,inverse_closed_tested=all_subgroups(table,inverse)
    H=[int(x) for x in src['subgroup_masks']]
    if src['elements']!=[list(p) for p in elements] or len(set(H))!=30 or set(H)!=masks:raise ValueError('LATTICE')
    counts,nodes=family_counts(H)
    if counts!=src['incomparable_no_reconstruction_triangle_families_by_size']:raise ValueError(('COUNTS',counts))
    rows=[]
    for K in H:
        if K==1:continue
        n=sum(A!=K and A.bit_count()<24 and A&K==K for A in H)
        if n>=10:raise ValueError('NONTRIVIAL_K')
        rows.append(n)
    if max(rows)!=7 or src['maximum_proper_strict_supergroups_nontrivial_K']!=7:raise ValueError('SUPERS')
    witness=src['controls']['ten_antichain_without_triangle_gate']
    if len(witness)!=10 or compatible_family(witness,H):raise ValueError('TRIPLE_CONTROL')
    if any(H[i]&H[j] in (H[i],H[j]) for i,j in combinations(witness,2)):raise ValueError('ANTICHAIN_CONTROL')
    out={'source_receipt_sha256':SOURCE[1],'inverse_orbits':inverse_orbits,'inverse_closed_divisor_size_sets_checked':inverse_closed_tested,
         'subgroup_count':len(H),'nontrivial_K_cases':len(rows),'maximum_nontrivial_K_proper_supergroups':max(rows),
         'incomparable_no_reconstruction_triangle_families_by_size':counts,'include_exclude_nodes':nodes,
         'all_checked':True,'controls':{'ten_antichain_with_triple':'rejected'},
         'limits':'Exact S4 subgroup and family enumeration; entropy and FD implications are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
