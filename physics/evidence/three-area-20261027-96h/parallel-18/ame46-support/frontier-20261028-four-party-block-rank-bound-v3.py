#!/usr/bin/env python3
"""Refine v2 bound using rank-3 W support in four-active constant-leg blocks.

A 3-term binary tensor with one constant leg and 3 no-Hamming-one support
vertices on the other three legs is a product with a rank-3 W-type tensor.
The written proof is separate; this checks the hypotheses in every block.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def bound(key,entries,pairs,base):
    if all(k==6 for k in key) and len(entries)==3:
        bits=[tuple(pairs[j].index(coord[j]) for j in range(4)) for coord,_ in entries]
        for constant_axis in range(4):
            if len({x[constant_axis] for x in bits})!=1:continue
            triple=[tuple(x[j] for j in range(4) if j!=constant_axis) for x in bits]
            if len(set(triple))!=3 or any(sum(a!=b for a,b in zip(x,y))==1 for x,y in itertools.combinations(triple,2)):
                raise ValueError('invalid W-type support')
            if len({sum(x)%2 for x in triple})!=1:
                raise ValueError('3-point binary support not same parity')
            return 3,True
    return base.block_bound(key,entries,pairs),False


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('verifier',type=Path)
    p.add_argument('base',type=Path);p.add_argument('out',type=Path);args=p.parse_args()
    dense=load('dense',args.verifier);base=load('blockv2',args.base)
    tensor,sha=dense.load_table(args.table);dense.support_structure(tensor)
    hist=collections.Counter();minima=[];minimum=10**9;refined=0;exceptions=[]
    for pairs in itertools.product(base.PAIRS,repeat=4):
        blocks=collections.defaultdict(list)
        for coord,coefficient in tensor.items():
            key=tuple(6 if coord[i] in pairs[i] else coord[i] for i in range(4))
            blocks[key].append((coord,coefficient))
        total=0
        for key,entries in blocks.items():
            v,used=bound(key,entries,pairs,base);total+=v;refined+=used
        hist[total]+=1
        if total<minimum:minimum=total;minima=[pairs]
        elif total==minimum:minima.append(pairs)
        if total<60:exceptions.append({'pairs':pairs,'bound':total})
    result={'table_sha256':sha,'pair_choices':15**4,'histogram':dict(sorted(hist.items())),
            'minimum_lower_bound':minimum,'minimizers_count':len(minima),
            'constant_leg_W_refinements':refined,'exceptions_below_60':exceptions,
            'method':'v2 invariant-block rank bound plus rank-3 binary 3-term W lemma when one of four active legs is constant',
            'limitations':'Only block-diagonal local maps with one selected 2x2 sector per party; no unrestricted U(6)^4 or global AME claim.'}
    with args.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
