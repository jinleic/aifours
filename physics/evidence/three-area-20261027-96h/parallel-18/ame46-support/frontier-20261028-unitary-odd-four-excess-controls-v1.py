#!/usr/bin/env python3
"""Exact n=5 support-graph controls for an odd 2n+4 unitary lemma."""
import argparse
import itertools
import json
from pathlib import Path


def square_components(rows,n):
    left=set(range(n))
    while left:
        rr={next(iter(left))}
        while True:
            cols=0
            for i in rr:cols|=rows[i]
            new={i for i in left if rows[i]&cols}
            if new==rr:break
            rr=new
        if len(rr)!=cols.bit_count():return False
        left-=rr
    return True


def necessary(rows,n):
    if any((a&b).bit_count()==1 for a,b in itertools.combinations(rows,2)):return False
    C=[sum((bool(rows[i]>>j&1)<<i) for i in range(n)) for j in range(n)]
    if any(v.bit_count()<2 for v in C):return False
    if any((a&b).bit_count()==1 for a,b in itertools.combinations(C,2)):return False
    return square_components(rows,n)


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    n=5;D={k:[x for x in range(1<<n) if x.bit_count()==k] for k in (2,3,4,5)};counts={'tested':0,'survivors':0}
    def visit(degs):
        for R in itertools.product(*(D[x] for x in degs)):
            counts['tested']+=1
            if necessary(R,n):counts['survivors']+=1
    for p0 in range(n):
      for p1 in range(n):
       if p0!=p1:visit([5 if i==p0 else 3 if i==p1 else 2 for i in range(n)])
    for p0,p1 in itertools.combinations(range(n),2):visit([4 if i in (p0,p1) else 2 for i in range(n)])
    for p0 in range(n):
      for p1,p2 in itertools.combinations([i for i in range(n) if i!=p0],2):visit([4 if i==p0 else 3 if i in (p1,p2) else 2 for i in range(n)])
    for ind in itertools.combinations(range(n),4):visit([3 if i in ind else 2 for i in range(n)])
    if counts!={'tested':2450000,'survivors':0}:raise ValueError(f'wrong counts {counts}')
    result={'n':5,'support_size':14,'counts':counts,
      'scope':'Exact n=5 support-graph control; general odd-size unitary proof is separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
