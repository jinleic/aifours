#!/usr/bin/env python3
"""Exhaust finite p-3 nonzero tuples for the two-missing inverse lemma."""
import argparse
from collections import Counter
import itertools
import json


def check(p):
    stats=Counter()
    for seq in itertools.product(range(1,p),repeat=p-3):
        A={0}
        zero_free=True
        for d in seq:
            if (-d)%p in A:
                zero_free=False
            A |= {(x+d)%p for x in A}
        if len(A)<p-2:
            raise ValueError('subset growth lower bound failed')
        classes={min(d,p-d) for d in seq}
        minimal=len(A)==p-2
        if minimal!=(len(classes)==1):
            raise ValueError('minimum support/opposite-class equivalence failed')
        if minimal and zero_free and len(set(seq))!=1:
            raise ValueError('zero-free minimizer not constant')
        stats['tuples']+=1
        stats['minimum_support']+=int(minimal)
        stats['zero_free']+=int(zero_free)
        stats['minimum_and_zero_free']+=int(minimal and zero_free)
    return dict(stats)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_PMINUS3_INVERSE_AUDIT','instances':{str(p):check(p) for p in (5,7)},
            'scope':'all finite nonzero ordered tuples at these two primes only'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
