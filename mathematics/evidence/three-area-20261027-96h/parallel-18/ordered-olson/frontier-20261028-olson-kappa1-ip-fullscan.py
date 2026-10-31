#!/usr/bin/env python3
"""Bounded exhaustive cut/omission IPGEN scan for same-rotation fixture."""
import argparse
import functools
import importlib.util
import json

spec=importlib.util.spec_from_file_location('gen','frontier-20261028-olson-kappa1-gen-parser.py')
gen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def scan(p):
    b=(-pow(2,-1,p))%p
    word=gen.build(p,b)
    unique=set()
    explored=0
    @functools.lru_cache(None)
    def certify(seq):
        nonlocal explored
        explored+=1
        tree=gen.parse(seq,p)
        if tree is not None:
            return ('GEN',tree)
        for i in range(len(seq)-1):
            a,c=seq[i],seq[i+1]
            if a[1]!=c[1]:
                continue
            if (a[1] and a[0]!=c[0]) or (not a[1] and (a[0]+c[0])%p!=0):
                continue
            reduced=seq[:i]+seq[i+2:]
            if not reduced:
                return ('inverse-pair-base',i,a,c)
            child=certify(reduced)
            if child is not None:
                return ('inverse-insert',i,a,c,child)
        return None
    for cut in range(len(word)):
        rotated=word[cut:]+word[:cut]
        for omit in range(len(word)):
            seq=rotated[:omit]+rotated[omit+1:]
            if seq in unique:
                continue
            unique.add(seq)
            tree=certify(seq)
            if tree is not None:
                return {'p':p,'rotation':b,'result':'IPGEN_TREE_FOUND','cut':cut,'omission_in_cut':omit,
                        'unique_cut_omission_words_examined':len(unique),'reduced_sequences_explored':explored,'tree':tree}
    return {'p':p,'rotation':b,'result':'NO_IPGEN_TREE_IN_BOUNDED_SCAN',
            'unique_cut_omission_words_examined':len(unique),'reduced_sequences_explored':explored,
            'scope':'one fixed normalized word; program/grammar completeness requires independent review'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result=scan(args.p)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
