#!/usr/bin/env python3
"""Exhaustive small support-graph controls for the one-excess unitary lemma."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def necessary(rows,n):
    if any(x.bit_count()<2 for x in rows):return False
    cols=[sum(bool(r>>j&1) for r in rows) for j in range(n)]
    if min(cols)<2:return False
    if any((a&b).bit_count()==1 for a,b in itertools.combinations(rows,2)):return False
    return True


def check_8_entry_unitary():
    # 2U has entries in Z[sqrt2], order real then sqrt2 coefficients.
    F=[[(0,1),(0,1),(0,0)],[(1,0),(-1,0),(0,1)],[(1,0),(-1,0),(0,-1)]]
    for i in range(3):
        for j in range(3):
            a=b=0
            for k in range(3):
                x,y=F[i][k];z,w=F[j][k];a+=x*z+2*y*w;b+=x*w+y*z
            if (a,b)!=((4 if i==j else 0),0):raise ValueError('8-entry positive-control Gram')
    return sum(x!=(0,0) for row in F for x in row)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    counts=[]
    for n in (2,3,4):
        hist=Counter();checked=0
        for rows in itertools.product(range(1<<n),repeat=n):
            checked+=1
            if necessary(rows,n):hist[sum(x.bit_count() for x in rows)]+=1
        if hist[2*n+1]:raise ValueError('one-excess support found')
        if n%2 and hist[2*n]:raise ValueError('odd-size degree-two support found')
        counts.append({'n':n,'patterns_checked':checked,'one_excess_patterns':hist[2*n+1],
          'degree_two_patterns':hist[2*n],'necessary_support_histogram':dict(sorted(hist.items()))})
    nnz=check_8_entry_unitary()
    if nnz!=8:raise ValueError('bad positive control')
    result={'matrix_support_enumeration':counts,'exact_3x3_unitary_with_8_entries':nnz,
            'scope':'Finite support-graph and exact positive controls; universal one-excess proof is written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
