#!/usr/bin/env python3
"""Bound support under four arbitrary 2-level local blocks, exact input.

Exhaust every coordinate-pair choice. Invariant tensor blocks are bounded by
ordinary flattening ranks, plus the exact rank-3 theorem for a 3-term,
no-Hamming-one binary 3-tensor. Four-active blocks use modular flattening rank
(lower bound over C). No local-angle/phase grid or numerical zero test.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys

P=17
R2=6
PAIRS=tuple(itertools.combinations(range(6),2))


def rank4(matrix):
    a=[row[:] for row in matrix]; pivot=0
    for col in range(len(a[0])):
        hit=next((i for i in range(pivot,len(a)) if a[i][col]%P),None)
        if hit is None:continue
        a[pivot],a[hit]=a[hit],a[pivot]
        inv=pow(a[pivot][col],-1,P)
        for i in range(pivot+1,len(a)):
            q=a[i][col]*inv%P
            if q:
                for j in range(col,len(a[0])):a[i][j]=(a[i][j]-q*a[pivot][j])%P
        pivot+=1
        if pivot==len(a):break
    return pivot


def block_bound(key,entries,pairs):
    active=[i for i,z in enumerate(key) if z==6]
    k=len(active)
    if k<=1:
        if len(entries)!=1:raise ValueError('Hamming-one source assumption failed')
        return 1
    if k==2:
        pos=[tuple(pairs[i].index(coord[i]) for i in active) for coord,_ in entries]
        if len({x[0] for x in pos})!=len(entries) or len({x[1] for x in pos})!=len(entries):
            raise ValueError('two-active block is not a partial permutation')
        return len(entries)
    if k==3:
        pos=[tuple(pairs[i].index(coord[i]) for i in active) for coord,_ in entries]
        if any(sum(a!=b for a,b in zip(x,y))==1 for x,y in itertools.combinations(pos,2)):
            raise ValueError('three-active support contains Hamming-one pair')
        count=len(entries)
        if count==1:return 1
        if count==2:return 2
        if count==3:
            # Three independent cube vertices have one parity and hence form
            # the rank-three W support; exact symbolic proof is in manuscript.
            if len({sum(x)%2 for x in pos})!=1:
                raise ValueError('three-point cube support not one parity')
            return 3
        if count==4:return 2
        raise ValueError('unexpected three-active support count')
    best=1
    for other in (1,2,3):
        ra=(0,other);ca=tuple(i for i in range(4) if i not in ra)
        matrix=[[0]*4 for _ in range(4)]
        for coord,(a,b) in entries:
            r=2*pairs[ra[0]].index(coord[ra[0]])+pairs[ra[1]].index(coord[ra[1]])
            c=2*pairs[ca[0]].index(coord[ca[0]])+pairs[ca[1]].index(coord[ca[1]])
            matrix[r][c]=(matrix[r][c]+a+R2*b)%P
        best=max(best,rank4(matrix))
    return best


def main():
    parser=argparse.ArgumentParser();parser.add_argument('table',type=Path);parser.add_argument('verifier',type=Path);parser.add_argument('out',type=Path);args=parser.parse_args()
    if R2*R2%P!=2:raise ValueError('invalid modular root')
    spec=importlib.util.spec_from_file_location('dense',args.verifier);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    tensor,sha=mod.load_table(args.table);mod.support_structure(tensor)
    histogram=collections.Counter();minimum=10**9;minima=[];bad=[]
    for pairs in itertools.product(PAIRS,repeat=4):
        blocks=collections.defaultdict(list)
        for coord,coefficient in tensor.items():
            key=tuple(6 if coord[i] in pairs[i] else coord[i] for i in range(4))
            blocks[key].append((coord,coefficient))
        bound=sum(block_bound(key,entries,pairs) for key,entries in blocks.items())
        histogram[bound]+=1
        if bound<minimum:minimum=bound;minima=[pairs]
        elif bound==minimum:minima.append(pairs)
        if bound<60:bad.append({'pairs':pairs,'lower_bound':bound})
    result={'table_sha256':sha,'prime':P,'root_of_two':R2,'pair_choices':15**4,
            'histogram':dict(sorted(histogram.items())),'minimum_lower_bound':minimum,
            'minimizers_count':len(minima),'minimizer_pair_choices':minima,
            'exceptions_below_60':bad,
            'method':'sum invariant-block flattening ranks plus exact 3-term binary-tensor rank theorem',
            'limitations':'A lower-bound certificate, not a claim of novel global AME minimum or coverage of arbitrary U(6) local maps.'}
    with args.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:result[k] for k in ('table_sha256','pair_choices','histogram','minimum_lower_bound','minimizers_count','method','limitations')},sys.stdout,indent=2);print()


if __name__=='__main__':main()
