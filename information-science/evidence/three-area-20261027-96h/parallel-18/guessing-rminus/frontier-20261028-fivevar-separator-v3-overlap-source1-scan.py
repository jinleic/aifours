#!/usr/bin/env python3
"""All finite-staircase source-Theorem-1 overlapping scan, W empty.

A/B swap is quotiented. Negative inner profiles are cached and minimized by
summing their finite negative lattice-cell ideals using exact integers.
"""
from hashlib import sha256
from math import comb
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v3.json'
EXPECTED='c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-v3-overlap-source1-scan-result.json'


def ideal_min(g,v,c,d):
    if v>=0:return g,0
    if c==0 or d==0:return None,None
    result=g;cells=0;i=0
    while v+i*c<0:
        j=0
        while v+i*c+j*d<0:
            result+=comb(i+j,i)*(v+i*c+j*d);cells+=1;j+=1
        i+=1
    return result,cells


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=np.array(json.loads(raw)['values_by_subset_mask'],dtype=np.int64)
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    C=np.repeat(np.arange(1,32,dtype=np.int64),31*32)
    D=np.tile(np.repeat(np.arange(1,32,dtype=np.int64),32),31)
    Z=np.tile(np.arange(32,dtype=np.int64),31*31)
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    checked=0;minimum=None;negative_count=0;cache={};violation=None
    for A in range(1,32):
        for B in range(A,32):
            g=I(A,B,Z);zt=I(A,Z,B)+I(B,Z,A)
            c=I(A,C,B)+I(B,C,A);d=I(A,D,B)+I(B,D,A)
            inner=-I(A,B,0)+I(A,B,C)+I(A,B,D)+I(C,D,0)+zt
            if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('SHANNON_COMPONENT')
            neg=inner<0;negative_count+=int(neg.sum());checked+=len(Z)
            if np.any(neg):
                profiles=np.unique(np.stack((g[neg],inner[neg],c[neg],d[neg]),axis=1),axis=0)
                for row in profiles:
                    key=tuple(int(x) for x in row)
                    if key not in cache:cache[key]=ideal_min(*key)
                    m,cells=cache[key]
                    if m is None or m<0:
                        indices=np.flatnonzero(neg & (g==key[0]) & (inner==key[1]) & (c==key[2]) & (d==key[3]))
                        j=int(indices[0]);violation={'A':A,'B':B,'C':int(C[j]),'D':int(D[j]),'Z':int(Z[j]),
                           'g_inner_c_d':key,'minimum':m,'negative_cells':cells};break
                    minimum=m if minimum is None else min(minimum,m)
            if violation:break
        if violation:break
    expected=(31*32//2)*31*31*32
    if not violation and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'point_sha256':EXPECTED,'scope':'all nonempty A,B,C,D and arbitrary Z subsets with overlaps; W empty; A/B quotient',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'all_finite_staircases':'exact negative-cell order ideal','negative_inner_cases':negative_count,
         'unique_negative_profiles':len(cache),'minimum_negative_ideal_value':minimum,'first_violation':violation,
         'elapsed_seconds':monotonic()-start,
         'limits':'Only source Theorem1 W-empty overlapping substitutions on one rational point; no outer conditioning W, entropy realization, or full literature novelty claim.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
