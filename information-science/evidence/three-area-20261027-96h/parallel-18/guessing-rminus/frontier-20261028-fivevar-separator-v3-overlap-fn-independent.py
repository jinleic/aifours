#!/usr/bin/env python3
"""Independent exact overlapping F_n replay by C/D batching and first differences."""
from hashlib import sha256
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v3.json'
EXPECTED='c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-v3-overlap-fn-independent-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=np.array(json.loads(raw)['values_by_subset_mask'],dtype=np.int64)
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    pairs=[(a,b) for a in range(1,32) for b in range(a,32)]
    A=np.repeat(np.array([x[0] for x in pairs],dtype=np.int64),32)
    B=np.repeat(np.array([x[1] for x in pairs],dtype=np.int64),32)
    Z=np.tile(np.arange(32,dtype=np.int64),len(pairs))
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    checked=0;minimum=None;maxn=1;violation=None
    for C in range(1,32):
        for D in range(1,32):
            a=I(A,B,C|Z);delta=I(A,B,Z)-I(A,B,D|Z)-I(C,D,Z)
            d=I(A,C,B|Z)+I(B,C,A|Z);slope=a-delta
            if np.any(a<0) or np.any(d<0):raise ValueError('SHANNON_COMPONENT')
            bad=(d==0)&(slope<0)
            if np.any(bad):
                j=int(np.flatnonzero(bad)[0]);n=int(a[j]//(-slope[j])+1)
                violation={'A':int(A[j]),'B':int(B[j]),'C':C,'D':D,'Z':int(Z[j]),'n':n,
                           'twice_slack':int(2*a[j]+2*n*slope[j])};checked+=len(Z);break
            n=np.ones(len(Z),dtype=np.int64);nz=d>0
            # F_{n+1}-F_n = a-delta+(n+1)d.  First nonnegative
            # difference is at ceil((delta-a)/d)-1, clipped to n>=1.
            n[nz]=np.maximum(1,-np.floor_divide(-(delta[nz]-a[nz]),d[nz])-1)
            maxn=max(maxn,int((n+1).max()))
            bound=int(max(np.max(np.abs(a)),np.max(np.abs(slope)),np.max(np.abs(d)),1))
            if 2*bound*(maxn+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            x=2*a+2*n*slope+n*(n+1)*d;y=2*a+2*(n+1)*slope+(n+1)*(n+2)*d
            local=int(min(x.min(),y.min()));minimum=local if minimum is None else min(minimum,local);checked+=len(Z)
            if local<0:
                j=int(np.flatnonzero((x<0)|(y<0))[0]);k=int(n[j] if x[j]<0 else n[j]+1)
                violation={'A':int(A[j]),'B':int(B[j]),'C':C,'D':D,'Z':int(Z[j]),'n':k,
                           'twice_slack':int(2*a[j]+2*k*slope[j]+k*(k+1)*d[j])};break
        if violation:break
    expected=(31*32//2)*31*31*32
    if not violation and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'point_sha256':EXPECTED,'scope':'all overlapping nonempty A,B,C,D subsets and arbitrary Z; A/B symmetry quotient',
         'enumeration':'C,D outer; ordered A<=B and Z vectorized','substitutions_checked':checked,
         'complete_expected_count':expected,'all_positive_n':'first-difference exact minimization',
         'minimum_twice_slack':minimum,'max_first_difference_neighbor_n':maxn,'first_violation':violation,
         'elapsed_seconds':monotonic()-start,
         'limits':'One F_n family on one five-variable polymatroid; no conclusion about other overlapping families, entropic realization or general novelty.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
