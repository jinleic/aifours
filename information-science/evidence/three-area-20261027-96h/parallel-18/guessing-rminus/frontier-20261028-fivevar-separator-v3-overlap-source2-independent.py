#!/usr/bin/env python3
"""Independent all-k overlapping source-Theorem-2 replay by C/D batching."""
from hashlib import sha256
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v3.json'
EXPECTED='c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-v3-overlap-source2-independent-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=np.array(json.loads(raw)['values_by_subset_mask'],dtype=np.int64)
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    A=np.repeat(np.arange(1,32,dtype=np.int64),31*32)
    B=np.tile(np.repeat(np.arange(1,32,dtype=np.int64),32),31)
    Z=np.tile(np.arange(32,dtype=np.int64),31*31)
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    checked=0;minimum=None;maxk=1;violation=None
    for C in range(1,32):
        for D in range(1,32):
            g=I(A,B,Z);zt=I(A,Z,B)+I(B,Z,A);c=I(A,C,B)+I(B,C,A)
            inner=-I(A,C,0)+I(A,C,B)+I(A,C,D)+I(B,D,0)+zt
            if np.any(g<0) or np.any(c<0):raise ValueError('SHANNON_COMPONENT')
            bad=(c==0)&(inner<0)
            if np.any(bad):
                j=int(np.flatnonzero(bad)[0]);k=int(g[j]//(-inner[j])+1)
                violation={'A':int(A[j]),'B':int(B[j]),'C':C,'D':D,'Z':int(Z[j]),'k':k,
                           'twice_slack':int(2*g[j]+2*k*inner[j])};checked+=len(Z);break
            k=np.ones(len(Z),dtype=np.int64);nz=c>0
            # q(k+1)-q(k)=inner+k*c; first nonnegative difference.
            k[nz]=np.maximum(1,-np.floor_divide(inner[nz],c[nz]));maxk=max(maxk,int((k+1).max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(inner)),np.max(np.abs(c)),1))
            if 2*bound*(maxk+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            q1=2*g+2*k*inner+k*(k-1)*c;q2=2*g+2*(k+1)*inner+(k+1)*k*c
            local=int(min(q1.min(),q2.min()));minimum=local if minimum is None else min(minimum,local);checked+=len(Z)
            if local<0:
                j=int(np.flatnonzero((q1<0)|(q2<0))[0]);kk=int(k[j] if q1[j]<0 else k[j]+1)
                violation={'A':int(A[j]),'B':int(B[j]),'C':C,'D':D,'Z':int(Z[j]),'k':kk,
                           'twice_slack':int(2*g[j]+2*kk*inner[j]+kk*(kk-1)*c[j])};break
        if violation:break
    expected=31**4*32
    if not violation and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'point_sha256':EXPECTED,'scope':'all overlapping nonempty A,B,C,D, arbitrary Z, W empty; A/B orders both',
         'enumeration':'C,D outer; A,B,Z vectorized','substitutions_checked':checked,'complete_expected_count':expected,
         'all_positive_k':'exact first-difference minimization','minimum_twice_slack':minimum,
         'max_first_difference_neighbor_k':maxk,'first_violation':violation,'elapsed_seconds':monotonic()-start,
         'limits':'One source theorem with W empty on one rational point; no outer-condition overlap, theorem1 overlap, entropic realization or full novelty claim.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
