#!/usr/bin/env python3
"""Exact top-ten partition entropy envelope for selected six-atom laws."""
from itertools import product
from math import prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-sixpoint-entropy-envelope-check-result.json'
CASES=((8,4,2,1,1,1),(10,5,3,2,1,1),(15,7,3,2,1,1))
CONTROL=(71,61,38,6,4,1)


def canonical(seq):
    labels={};out=[]
    for x in seq:
        if x not in labels:labels[x]=len(labels)
        out.append(labels[x])
    return tuple(out)


def parts():
    P={canonical(x) for x in product(range(6),repeat=6)}
    out=sorted(x for x in P if 1<len(set(x))<6)
    if len(out)!=201:raise ValueError('PARTITIONS')
    return out


def compare(w,P):
    W=sum(w)
    def factor(part):
        blocks={}
        for value,weight in zip(part,w):blocks[value]=blocks.get(value,0)+weight
        return prod(s**s for s in blocks.values())
    ranked=sorted(((factor(p),p) for p in P),reverse=True);best=prod(x for x,p in ranked[:10])
    threshold=W**(17*W)*prod(x**(3*x) for x in w)
    return best*best<threshold,[list(p) for x,p in ranked[:10]]


def main():
    P=parts();cases=[]
    for w in CASES:
        strict,top=compare(w,P)
        if not strict:raise ValueError(('NO_MARGIN',w))
        cases.append({'weights':w,'strict_envelope_obstruction':strict,'ten_minimum_entropy_partitions':top})
    if compare(CONTROL,P)[0]:raise ValueError('CONTROL_ACCEPTED')
    out={'partition_count':len(P),'cases':cases,'all_checked':True,
         'controls':{'skewed_weight_vector_outside_envelope':{'weights':CONTROL,'rejected':True}},
         'limits':'Exact entropy-envelope comparisons only; graph FD and continuity deductions are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'partition_count':len(P),'case_count':len(cases),'all_checked':True,'controls':out['controls']},indent=2))


if __name__=='__main__':main()
