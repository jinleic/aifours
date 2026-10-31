#!/usr/bin/env python3
"""Exact finite controls for the F2 rectangle parity lemmas at residual n=8."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def graph(m,degrees):
    pairs=list(itertools.combinations(range(m),2));out=[]
    for rows in itertools.product(pairs,repeat=4):
        if tuple(sum(x in r for r in rows) for x in range(m))==degrees:
            out.append(tuple(frozenset(r) for r in rows))
    return out


def rectangle(a,b):
    return sum(1<<(4*x+y) for x in a for y in b)


def zeros(A,B):
    out=[]
    for mask in range(1,16):
        bits=0
        for i in range(4):
            if mask>>i&1:bits^=rectangle(A[i],B[i])
        if not bits:out.append(mask)
    return out


def duplicate_pair(A):
    repeats=[(i,j) for i,j in itertools.combinations(range(4),2) if A[i]==A[j]]
    if len(repeats)!=1:raise ValueError('3-symbol graph duplicate')
    return sum(1<<i for i in repeats[0])


def partition4(A):
    groups={frozenset(i for i in range(4) if A[i]==A[j]) for j in range(4)}
    if len(groups)!=2 or any(len(x)!=2 for x in groups):return None
    return frozenset(groups)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);args=ap.parse_args()
    G4=graph(4,(2,2,2,2));G3=graph(3,(2,3,3))
    if (len(G4),len(G3))!=(90,12):raise ValueError('wrong incidence graph counts')
    c44=Counter();c34=Counter();c33=Counter()
    for U,V in itertools.product(G4,G4):
        for mask in zeros(U,V):
            PU,PV=partition4(U),partition4(V)
            if mask.bit_count() not in (2,4) or PU is None or PU!=PV:
                raise ValueError('4x4 parity classification failure')
            c44[mask.bit_count()]+=1
    for U,V in itertools.product(G3,G4):
        p=duplicate_pair(U)
        for mask in zeros(U,V):
            pv=partition4(V)
            if mask!=p or pv is None or frozenset(i for i in range(4) if mask>>i&1) not in pv:
                raise ValueError('3x4 parity classification failure')
            c34[mask.bit_count()]+=1
    for U,V in itertools.product(G3,G3):
        p,q=duplicate_pair(U),duplicate_pair(V)
        for mask in zeros(U,V):
            if not ((mask==p==q) or (mask==15 and p==((~q)&15))):
                raise ValueError('3x3 parity classification failure')
            c33['same_duplicate_F2' if mask.bit_count()==2 else 'opposite_duplicate_F4']+=1
    if dict(c44)!={2:216,4:108} or dict(c34)!={2:72} or dict(c33)!={'same_duplicate_F2':24,'opposite_duplicate_F4':24}:
        raise ValueError('unexpected parity counts')
    result={'ternary_incidence_graphs':len(G3),'quaternary_incidence_graphs':len(G4),
            '4x4_zero_xor_nonempty_full_fiber_masks':dict(sorted(c44.items())),
            '3x4_zero_xor_nonempty_full_fiber_masks':dict(sorted(c34.items())),
            '3x3_zero_xor_nonempty_full_fiber_masks':dict(sorted(c33.items())),
            'scope':'Finite F2 controls for stated rectangle lemmas; general mathematics is separately written.'}
    with args.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
