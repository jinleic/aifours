#!/usr/bin/env python3
"""Finite combinatorial audits for the all-high written argument."""
import argparse
from collections import Counter
import itertools
import json


def audit_patterns(p):
    F=p+3
    examined=normal=0
    kinds=Counter()
    for adj in itertools.combinations(range(F-1),4):
        examined+=1
        edges=set(adj)
        candidates=[(i,i+1) for i in adj]
        matching=max((len(chosen) for size in range(5) for chosen in itertools.combinations(candidates,size)
                      if len({x for pair in chosen for x in pair})==2*size),default=0)
        if matching!=2:
            continue
        normal+=1
        lengths=[]
        length=1
        for i in range(F-1):
            if i in edges:
                length+=1
            else:
                if length>1:
                    lengths.append(length)
                length=1
        if length>1:
            lengths.append(length)
        if sorted(lengths) not in ([5],[3,3]):
            raise ValueError('adjacency normal form failed')
        interior=[pair for pair in candidates if 0 not in pair and F-1 not in pair]
        possible=[(a,b) for a,b in itertools.combinations(interior,2) if len(set(a+b))==4]
        if not possible:
            raise ValueError('cannot insert two disjoint pairs avoiding endpoints')
        kinds[str(sorted(lengths))]+=1
    return {'patterns_with_four_boundaries':examined,'normal_patterns':normal,'types':dict(kinds)}


def audit_missing_set_lemma(p):
    checked=0
    elements=list(range(1,p))
    for E in itertools.chain(({u} for u in elements), (set(x) for x in itertools.combinations(elements,2))):
        for a,b in itertools.product(E,repeat=2):
            if (a+b)%p in E:
                if a!=b or E!={a,2*a%p}:
                    raise ValueError('two-pair missing-set lemma failed')
                for c in E:
                    if (a+c)%p in E and (b+c)%p in E and (a+b+c)%p in E:
                        raise ValueError('three-pair missing-set lemma failed')
            checked+=1
    return checked


def audit_subsets(p):
    checked=zero_free=0
    for seq in itertools.product(range(1,p),repeat=p-3):
        checked+=1
        A={0}
        ok=True
        for d in seq:
            if (-d)%p in A:
                ok=False
                break
            A |= {(x+d)%p for x in A}
        if not ok:
            continue
        zero_free+=1
        if len(A)<p-2 or 0 not in A:
            raise ValueError('zero-free subset support bound failed')
    return {'nonzero_tuples':checked,'zero_free':zero_free}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_ALL_HIGH_FINITE_STRUCTURAL_AUDIT',
            'adjacency_patterns':{str(p):audit_patterns(p) for p in (3,5,7,11,13)},
            'missing_set_pairs':{str(p):audit_missing_set_lemma(p) for p in (3,5,7,11,13)},
            'subset_sequences':{str(p):audit_subsets(p) for p in (3,5,7)},
            'scope':'finite combinatorial lemmas only; not all-word or peer-review proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
