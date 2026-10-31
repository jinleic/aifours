#!/usr/bin/env python3
"""Independent partition-generation and exact strict-nonedge color replay."""
from hashlib import sha256
from itertools import combinations,product
from math import prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-sixpoint-mi-color-certificate-result.json','11b8bda399a8e2636595a79bd62b5b135eda00ec94e59ae2e9976196c3f2dc61')
OUT=ROOT/'frontier-20261028-sixpoint-mi-color-independent-result.json'


def canonical(seq):
    lab={};out=[]
    for x in seq:
        if x not in lab:lab[x]=len(lab)
        out.append(lab[x])
    return tuple(out)


def factor(part,weights):
    blocks={}
    for x,w in zip(part,weights):blocks[x]=blocks.get(x,0)+w
    return prod(z**z for z in blocks.values())


def verify(parts,case):
    w=tuple(case['weights']);colors=case['partition_colors'];k=case['color_count'];n=len(parts)
    if len(w)!=6 or any(not isinstance(x,int) or x<=0 for x in w) or len(colors)!=n or not 1<=k<=9 or set(colors)!=set(range(k)):raise ValueError('CASE')
    f=[factor(p,w) for p in parts];total=sum(w)**sum(w);checked=0;potential_edges=0;cross_edge=None
    for i,j in combinations(range(n),2):
        fj=factor(tuple(zip(parts[i],parts[j])),w);den=total*fj*fj
        is_potential=f[i]*f[j]*f[j]>=den and f[j]*f[i]*f[i]>=den
        if is_potential:
            potential_edges+=1
            if colors[i]==colors[j]:raise ValueError(('COLOR',i,j))
            if cross_edge is None:cross_edge=(i,j)
        elif colors[i]==colors[j]:checked+=1
    if potential_edges!=case['potential_mi_edges'] or cross_edge is None:raise ValueError('EDGE_COUNT')
    return {'weights':list(w),'color_count':k,'potential_edges':potential_edges,
            'same_color_strict_nonedge_pairs':checked},cross_edge


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);parts=[tuple(p) for p in src['partitions']]
    independent={canonical(x) for x in product(range(6),repeat=6)}
    independent={x for x in independent if 1<len(set(x))<6}
    if len(independent)!=201 or len(parts)!=201 or len(set(parts))!=201 or set(parts)!=independent:raise ValueError('PARTITIONS')
    results=[];controls=[]
    for case in src['cases']:
        checked,(i,j)=verify(parts,case);results.append(checked)
        bad=json.loads(json.dumps(case));bad['partition_colors'][j]=bad['partition_colors'][i]
        try:verify(parts,bad)
        except ValueError:controls.append('rejected')
        else:raise ValueError('MUTATION_ACCEPTED')
    if len(results)!=6 or controls!=['rejected']*6:raise ValueError('CASE_COUNT')
    out={'source_receipt_sha256':SOURCE[1],'independent_partition_count':len(independent),
         'cases':results,'all_checked':True,'controls':{'merged_adjacent_colors':controls},
         'limits':'Exact potential-MI graph coloring checks only; graph-FD and continuity deductions are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
