#!/usr/bin/env python3
"""Search IPGEN trees by reverse actual adjacent-inverse removal."""
import argparse
import functools
import importlib.util
import json

spec=importlib.util.spec_from_file_location('gen','frontier-20261028-olson-kappa1-gen-parser.py')
gen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def search(word,p):
    explored=0
    @functools.lru_cache(None)
    def rec(seq):
        nonlocal explored
        explored+=1
        tree=gen.parse(seq,p)
        if tree is not None:
            return ('GEN',tree)
        for i in range(len(seq)-1):
            a,b=seq[i],seq[i+1]
            if a[1]!=b[1]:
                continue
            inverse=(a[0]==b[0]) if a[1] else ((a[0]+b[0])%p==0)
            if not inverse:
                continue
            rest=seq[:i]+seq[i+2:]
            if not rest:
                return ('inverse-pair-base',i,a,b)
            child=rec(rest)
            if child is not None:
                return ('inverse-insert',i,a,b,child)
        return None
    tree=rec(word)
    return tree,explored


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    cases=[]
    for p in (11,13):
        b=(-pow(2,-1,p))%p
        original=gen.build(p,b)
        retained=original[1:]
        tree,count=search(retained,p)
        cases.append({'p':p,'rotation':b,'cut':0,'omitted_original_index':0,
                      'actual_sequence':retained,'result':'IPGEN_TREE_FOUND' if tree is not None else 'NO_IPGEN_TREE_FOR_THIS_CUT_OMISSION',
                      'explored_reduced_sequences':count,'tree':tree})
    result={'result':'BOUNDED_ONE_CUT_IPGEN_SEARCH','cases':cases,
            'scope':'one named cut/omission each; no conclusion about other cuts/omissions or full residual'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
