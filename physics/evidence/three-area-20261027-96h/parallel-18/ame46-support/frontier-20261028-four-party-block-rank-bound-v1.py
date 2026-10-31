#!/usr/bin/env python3
"""Exhaustively bound arbitrary four 2-level local blocks using block ranks.

For each of 15^4 coordinate-pair choices, partition the 60 source coefficients
by active/inactive membership. Each invariant block is bounded below by a
bipartition flattening rank (mod 17, sqrt2=6). Complex unitaries on selected
pairs preserve these ranks. This is a lower-bound relaxation, not a search for
coherent transformations nor a global AME bound.
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
        positions=[tuple(pairs[i].index(coord[i]) for i in active) for coord,_ in entries]
        if len({x[0] for x in positions})!=len(entries) or len({x[1] for x in positions})!=len(entries):
            raise ValueError('two-active block is not a partial permutation')
        return len(entries)
    if k==3:
        # Any two distinct support tuples differ in >=2 active coordinates;
        # one flattening has two nonzero rows with disjoint column support.
        return 1 if len(entries)==1 else 2
    # Four active axes: use maximum of the three 2|2 modular flattening ranks.
    best=1
    for other in (1,2,3):
        row_axes=(0,other);col_axes=tuple(i for i in range(4) if i not in row_axes)
        matrix=[[0]*4 for _ in range(4)]
        for coord,(a,b) in entries:
            rv=2*pairs[row_axes[0]].index(coord[row_axes[0]])+pairs[row_axes[1]].index(coord[row_axes[1]])
            cv=2*pairs[col_axes[0]].index(coord[col_axes[0]])+pairs[col_axes[1]].index(coord[col_axes[1]])
            matrix[rv][cv]=(matrix[rv][cv]+a+R2*b)%P
        best=max(best,rank4(matrix))
    return best


def main():
    parser=argparse.ArgumentParser();parser.add_argument('table',type=Path);parser.add_argument('verifier',type=Path);parser.add_argument('out',type=Path);a=parser.parse_args()
    if R2*R2%P!=2:raise ValueError('invalid modular root')
    spec=importlib.util.spec_from_file_location('dense',a.verifier);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    tensor,sha=mod.load_table(a.table)
    mod.support_structure(tensor)
    histogram=collections.Counter();minimum=10**9;minima=[]
    for pairs in itertools.product(PAIRS,repeat=4):
        blocks=collections.defaultdict(list)
        for coord,coefficient in tensor.items():
            key=tuple(6 if coord[i] in pairs[i] else coord[i] for i in range(4))
            blocks[key].append((coord,coefficient))
        bound=sum(block_bound(key,entries,pairs) for key,entries in blocks.items())
        histogram[bound]+=1
        if bound<minimum:minimum=bound;minima=[pairs]
        elif bound==minimum:minima.append(pairs)
    result={'table_sha256':sha,'prime':P,'root_of_two':R2,'pair_choices':15**4,
            'histogram':dict(sorted(histogram.items())), 'minimum_lower_bound':minimum,
            'minimizers_count':len(minima),'minimizer_pair_choices':minima,
            'method':'sum independent invariant-block flattening ranks; k=4 uses all 2|2 modular ranks',
            'limitations':'Lower bound only, no assertion that all block ranks can be simultaneously saturated by a common local unitary.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:result[k] for k in ('table_sha256','pair_choices','histogram','minimum_lower_bound','minimizers_count','method','limitations')},sys.stdout,indent=2);print()


if __name__=='__main__':main()
