#!/usr/bin/env python3
"""Enumerate all 3-fiber/three-symbol residual supports in the n=5 case.

The written incidence argument supplies the exhaustive normal form. This code
checks the 27^3 finite normal forms, directly constructing each 12-point set.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

SYMBOLS=range(3)


def opts(fixed_fiber):
    doubles=list(itertools.combinations(SYMBOLS,2));out=[]
    for single in SYMBOLS:
        for u in doubles:
            for v in doubles:
                others=iter((u,v))
                out.append(tuple((single,) if fiber==fixed_fiber else next(others) for fiber in SYMBOLS))
    if len(out)!=27:raise ValueError('wrong option count')
    return out


def projection_size(S,i,j):return len({(x[i],x[j]) for x in S})


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    options=[opts(i) for i in SYMBOLS];hist=Counter();total=0;none=0;relaxed=0;example=None
    for choice in itertools.product(*options):
        S=set()
        for fiber in SYMBOLS:
            for v in itertools.product(*(choice[j][fiber] for j in SYMBOLS)):
                S.add((fiber,)+v)
        if len(S)!=12:raise ValueError('fiber normal form is not 12-point')
        allpairs={(i,j):projection_size(S,i,j) for i,j in itertools.combinations(range(4),2)}
        if any(allpairs[(0,j)]!=5 for j in (1,2,3)):raise ValueError('normal-form pair with fiber is not 5')
        p=tuple(allpairs[(i,j)] for i,j in ((1,2),(1,3),(2,3)));hist[p]+=1;total+=1
        if p==(5,5,5):none+=1
        if p==(5,5,6):
            relaxed+=1
            if example is None:example={'options':choice,'residual_points':sorted(S),'projection_sizes':p}
    if total!=19683 or none!=0 or relaxed==0:raise ValueError('unexpected enumeration result')
    result={'normal_forms':total,'choices_per_coordinate':27,'target_projection_sizes':[5,5,5],
            'target_count':none,'relaxed_5_5_6_count':relaxed,'relaxed_witness':example,
            'pair_projection_histogram':{','.join(map(str,k)):v for k,v in sorted(hist.items())},
            'scope':'Exhaustive finite normal forms; validity of the normal form is a separate written incidence argument.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pair_projection_histogram','relaxed_witness')},indent=2))


if __name__=='__main__':main()
