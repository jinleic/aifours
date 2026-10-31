#!/usr/bin/env python3
"""Exact small-pattern controls for the 2n+2 unitary support lemma."""
import argparse
import itertools
import json
from pathlib import Path


def necessary(rows,n,both=True):
    if any((a&b).bit_count()==1 for a,b in itertools.combinations(rows,2)):return False
    cols=[sum((bool(rows[i]>>j&1)<<i) for i in range(n)) for j in range(n)]
    if any(c.bit_count()<2 for c in cols):return False
    if both and any((a&b).bit_count()==1 for a,b in itertools.combinations(cols,2)):return False
    return True


def square_components(rows,n):
    remaining=set(range(n))
    while remaining:
        component={next(iter(remaining))}
        while True:
            cols=0
            for i in component:cols|=rows[i]
            grown={i for i in remaining if rows[i]&cols}
            if grown==component:break
            component=grown
        if len(component)!=cols.bit_count():return False
        remaining-=component
    return True


def splits_3_plus_2(rows,n):
    if n<3:return False
    for inds in itertools.combinations(range(n),3):
        cm=0
        for i in inds:cm|=rows[i]
        if cm.bit_count()!=3:continue
        if any(rows[i]&cm for i in range(n) if i not in inds):continue
        if sorted(rows[i].bit_count() for i in inds)!=[2,3,3]:continue
        rest=[i for i in range(n) if i not in inds]
        if any(rows[i].bit_count()!=2 for i in rest):continue
        if not necessary([rows[i]>>0 for i in range(n)],n):continue
        return True
    return False


def scan(n):
    D={k:[m for m in range(1<<n) if m.bit_count()==k] for k in (2,3,4)}
    examined=one4=two3=weak_only=rectangular=0
    for p in range(n):
        for rows in itertools.product(*(D[4] if i==p else D[2] for i in range(n))):
            examined+=1
            if necessary(rows,n):
                if square_components(rows,n):one4+=1
                else:rectangular+=1
            elif necessary(rows,n,both=False):weak_only+=1
    for p,q in itertools.combinations(range(n),2):
        for rows in itertools.product(*(D[3] if i in (p,q) else D[2] for i in range(n))):
            examined+=1
            if necessary(rows,n):
                if not square_components(rows,n):
                    rectangular+=1
                    continue
                two3+=1
                if not splits_3_plus_2(rows,n):raise ValueError(f'nondecomposable survivor n={n}: {rows}')
            elif necessary(rows,n,both=False):weak_only+=1
    if one4 or (n%2==0 and two3):raise ValueError('unexpected even/one4 survivor')
    return {'n':n,'candidate_patterns':examined,'one_degree4_survivors':one4,
            'two_degree3_survivors':two3,'all_survivors_have_3x3_component':True,
            'rectangular_component_rejections':rectangular,
            'row_only_condition_false_positives':weak_only}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    records=[scan(n) for n in (3,4,5)]
    result={'cases':records,'scope':'Exact n<=5 support-graph controls; universal 2n+2 unitary argument is written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
