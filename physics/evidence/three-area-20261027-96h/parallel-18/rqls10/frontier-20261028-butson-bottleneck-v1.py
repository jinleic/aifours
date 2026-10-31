#!/usr/bin/env python3
"""Exact minimum over half-row partitions and perfect matchings of the
largest opposite-row squared-overlap obstruction for explicit BH(10,5).

Weights are pairs U,V with 2|sum fifth roots|²=U+V sqrt(5). Dynamic
programming explores ALL perfect matchings on ten vertices.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from pathlib import Path
import importlib.util
import json

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('b',ROOT/'frontier-20261028-butson10-half-matching-v1.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)


def sign(a,b):
    if b==0:return (a>0)-(a<0)
    if b>0:
        if a>=0:return 1
        return 1 if 5*b*b>a*a else -1
    if a<=0:return -1
    return 1 if a*a>5*b*b else -1

def compare(x,y):return sign(x[0]-y[0],x[1]-y[1])

def weight(a):
    squares=sum(x*x for x in a); p1=p2=0
    for i,j in combinations(range(5),2):
        if (j-i)%5 in (1,4):p1+=a[i]*a[j]
        else:p2+=a[i]*a[j]
    return (2*squares-p1-p2,p1-p2)


def run(label,K):
    hist=Counter();best=None;example=None
    for rows in combinations(range(10),5):
        W={}
        for i,j in combinations(range(10),2):
            a=[0]*5
            for t in rows:a[(K[t][i]-K[t][j])%5]+=1
            W[i,j]=weight(a)
        @lru_cache(None)
        def optimal(mask):
            if not mask:return ((0,0),())
            bit=mask&-mask;i=bit.bit_length()-1;left=mask^bit
            best_here=None
            for j in range(i+1,10):
                if not left&(1<<j):continue
                prior,matching=optimal(left^(1<<j))
                edge=W[i,j]
                worst=edge if compare(edge,prior)>0 else prior
                if best_here is None or compare(worst,best_here[0])<0:
                    best_here=(worst,((i,j),)+matching)
            return best_here
        bottleneck,matching=optimal((1<<10)-1)
        hist[bottleneck]+=1
        if best is None or compare(bottleneck,best)<0:
            best=bottleneck;example={'rows':rows,'matching':matching}
    print(label,'exact bottleneck 2|E|²=',best,'example',example)
    print(label,'bottleneck histogram',dict(sorted(hist.items())))
    return {'label':label,'best_twice_squared_half_sum':best,'example':example,
            'histogram':[[list(k),v] for k,v in sorted(hist.items())]}


b.validate()
results=[run('source',b.K),run('transpose',tuple(tuple(b.K[j][i] for j in range(10)) for i in range(10)))]
out=ROOT/'frontier-20261028-butson-bottleneck-result-v1.json'
out.write_text(json.dumps({'results':results,'scope':'necessary opposite-row pairs; not full QLS optimization'},indent=2,sort_keys=True)+'\n')
print('wrote',out.name)
