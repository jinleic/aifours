#!/usr/bin/env python3
"""Exact finite controls for 12 maximal rays and the LU support gap."""
import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def parity(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2


def analyze_perms(want):
    P=[p for p in itertools.permutations(range(4)) if parity(p)==want]
    counts={(i,g):sum(p[i]==g for p in P) for i in range(4) for g in range(4)}
    if len(P)!=12 or any(v!=3 for v in counts.values()):raise ValueError('wrong permutation occurrence count')
    masks=range(16);maximum=0;checked=0
    for m in itertools.product(masks,repeat=4):
        if m==(15,15,15,15):continue
        t=sum(all(m[i]>>p[i]&1 for i in range(4)) for p in P)
        maximum=max(maximum,t);checked+=1
    if maximum!=9:raise ValueError('wrong surviving-ray maximum')
    return {'parity':want,'tuple_count':len(P),'each_party_color_occurrences':3,
            'incomplete_mask_cases_checked':checked,'max_coordinate_rays_when_a_color_missing':maximum}


def pair_min_nonmonomial(a,b):
    if a!=b:return 4
    size=a.bit_count()
    return 4-(1<<(3-size))


def axis_bound():
    counts=Counter();examples={};n=0
    for m in itertools.product(range(1,8),repeat=4):
        total=sum(pair_min_nonmonomial(m[i],m[j]) for i,j in itertools.combinations(range(4),2))
        normal=all(x.bit_count()==1 for x in m) and len(set(m))==1
        if normal and total!=0:raise ValueError('bad equality support')
        if not normal and total<12:raise ValueError(f'bad gap for axis masks {m}')
        counts[str(total)]+=1
        if str(total) not in examples:examples[str(total)]=m
        n+=1
    return {'axis_mask_cases':n,'minimum_when_not_shared_axis':12,'lower_bound_histogram':dict(sorted(counts.items(),key=lambda x:int(x[0]))),
            'tight_mask_example':examples['12']}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    phases=[analyze_perms(0),analyze_perms(1)];axes=axis_bound()
    result={'permutation_classes':phases,'axis_block_lower_bounds':axes,
      'scope':'Finite combinatorial controls; product-saturator classification and unitary orbit proof are separate written arguments.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
