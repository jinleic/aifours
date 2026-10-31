#!/usr/bin/env python3
"""Exact small-pattern controls for the 2n+3 unitary support lemma."""
import argparse
import itertools
import json
from pathlib import Path


def necessary(rows,n):
    if any((a&b).bit_count()==1 for a,b in itertools.combinations(rows,2)):return False
    cols=[sum((bool(rows[i]>>j&1)<<i) for i in range(n)) for j in range(n)]
    if any(c.bit_count()<2 for c in cols):return False
    return not any((a&b).bit_count()==1 for a,b in itertools.combinations(cols,2))


def components(rows,n):
    remain=set(range(n));out=[]
    while remain:
        rr={next(iter(remain))}
        while True:
            cols=0
            for i in rr:cols|=rows[i]
            grow={i for i in remain if rows[i]&cols}
            if grow==rr:break
            rr=grow
        out.append((tuple(sorted(rr)),cols));remain-=rr
    return out


def scan(n):
    D={k:[x for x in range(1<<n) if x.bit_count()==k] for k in (2,3,4,5)}
    cnt={'tested':0,'quadrangular':0,'rectangular_rejected':0,'square_survivors':0}
    def consider(rows):
        cnt['tested']+=1
        if not necessary(rows,n):return
        cnt['quadrangular']+=1;parts=components(rows,n)
        if any(len(rr)!=cols.bit_count() for rr,cols in parts):cnt['rectangular_rejected']+=1;return
        cnt['square_survivors']+=1
        sizes=sorted(len(rr) for rr,cols in parts)
        if sizes!=[2]*((n-3)//2)+[3] or any(len(rr)==3 and any(rows[i].bit_count()!=3 for i in rr) for rr,cols in parts):
            raise ValueError(f'unexpected square support n={n} {rows}')
    for p in range(n):
        for R in itertools.product(*(D[5] if i==p else D[2] for i in range(n))):consider(R)
    for p in range(n):
        for q in range(n):
            if p==q:continue
            for R in itertools.product(*(D[4] if i==p else D[3] if i==q else D[2] for i in range(n))):consider(R)
    for idx in itertools.combinations(range(n),3):
        for R in itertools.product(*(D[3] if i in idx else D[2] for i in range(n))):consider(R)
    return {'n':n,**cnt}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    cases=[scan(n) for n in (3,4,5)]
    if [x['square_survivors'] for x in cases]!=[1,0,100]:raise ValueError('unexpected survivor count')
    result={'cases':cases,'scope':'Exact n<=5 support-graph controls; universal unitary classification is written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
