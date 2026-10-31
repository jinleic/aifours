#!/usr/bin/env python3
"""Exhaustive exact2x2 controls for generalized binary-phase row formulas."""
import argparse
from collections import defaultdict
import itertools
import json
from pathlib import Path


def inner_zero(a,b,c,d,L):
    # Exact polynomial reduction of zeta^(a-c)+zeta^(b-d), for2-power L.
    half=L//2;v=defaultdict(int)
    for k in ((a-c)%L,(b-d)%L):v[k%half]+=1 if k<half else -1
    return not any(v.values())


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);args=ap.parse_args();records=[]
    for bits in range(1,5):
        L=1<<bits;n=good=mismatch=wrong_sign_mismatch=0
        for a,b,c,d in itertools.product(range(L),repeat=4):
            actual=inner_zero(a,b,c,d,L);sr=(a+b)%L;ss=(c+d)%L
            encoded=(sr-ss-2*a+2*c)%L==L//2
            wrong=(sr-ss+2*a-2*c)%L==L//2
            n+=1;good+=actual;mismatch+=actual!=encoded;wrong_sign_mismatch+=actual!=wrong
        if mismatch or good!=L**3:raise ValueError('formula/control mismatch')
        if bits>=3 and not wrong_sign_mismatch:raise ValueError('sign mutation not detected')
        records.append({'bits':bits,'assignments':n,'orthogonal_assignments':good,'formula_mismatches':mismatch,'deliberate_wrong_sign_mismatches':wrong_sign_mismatch})
    # At L=8, show invariance under arbitrary row/column phase gauge shifts.
    L=8;gauges=0
    for a,b,c,d in ((0,0,0,0),(0,0,0,4),(1,3,2,0),(7,1,4,2)):
        before=inner_zero(a,b,c,d,L)
        for row1,row2,col1,col2 in itertools.product(range(L),repeat=4):
            after=inner_zero((a+row1+col1)%L,(b+row1+col2)%L,(c+row2+col1)%L,(d+row2+col2)%L,L)
            if before!=after:raise ValueError('gauge changed orthogonality')
            gauges+=1
    receipt={'scope':'Exact finite controls of generalized2x2 binary-phase encoding and gauge; no global state theorem.','phase_formula':records,'gauge_controls':gauges,'arithmetic':'Integer sparse reduction by X^(L/2)+1, no floats'}
    with args.out.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
