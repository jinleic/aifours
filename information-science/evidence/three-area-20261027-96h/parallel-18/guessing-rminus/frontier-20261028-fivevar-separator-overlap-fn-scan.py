#!/usr/bin/env python3
"""Exact all-order F_n overlap scan on the five-variable separator.

All nonempty A,B,C,D subsets and any Z subset may overlap. A/B exchange is
quotiented. A found violation disproves only broader-family independence;
absence covers exactly this named family on this one polymatroid.
"""
from hashlib import sha256
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v2.json'
EXPECTED='84ac1e3c87db445e0c4b3d4eb9388c58f040591cd8ca6b799c93630e3ac187f4'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-overlap-fn-scan-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=np.array(json.loads(raw)['values_by_subset_mask'],dtype=np.int64)
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    c=np.repeat(np.arange(1,32,dtype=np.int64),31*32)
    d=np.tile(np.repeat(np.arange(1,32,dtype=np.int64),32),31)
    z=np.tile(np.arange(32,dtype=np.int64),31*31)
    def I(a,b,x):return h[a|x]+h[b|x]-h[a|b|x]-h[x]
    checked=0;minimum=None;maxn=1;violation=None
    for A in range(1,32):
        for B in range(A,32):
            a=I(A,B,c|z);delta=I(A,B,z)-I(A,B,d|z)-I(c,d,z)
            t=I(A,c,B|z)+I(B,c,A|z);linear=a-delta
            if np.any(a<0) or np.any(t<0):raise ValueError('SHANNON_COMPONENT')
            unbounded=(t==0)&(linear<0)
            if np.any(unbounded):
                j=int(np.flatnonzero(unbounded)[0]);n=int(a[j]//(-linear[j])+1)
                violation={'A':A,'B':B,'C':int(c[j]),'D':int(d[j]),'Z':int(z[j]),'n':n,'twice_slack':int(2*a[j]+2*n*linear[j])}
                checked+=len(z);break
            n=np.ones(len(z),dtype=np.int64);nz=t>0
            n[nz]=np.maximum(1,np.floor_divide(-(2*linear[nz]+t[nz]),2*t[nz]));maxn=max(maxn,int((n+1).max()))
            bound=int(max(np.max(np.abs(a)),np.max(np.abs(linear)),np.max(np.abs(t)),1))
            if 2*bound*(maxn+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            x=2*a+2*n*linear+n*(n+1)*t;y=2*a+2*(n+1)*linear+(n+1)*(n+2)*t
            local=int(min(x.min(),y.min()));minimum=local if minimum is None else min(minimum,local);checked+=len(z)
            if local<0:
                j=int(np.flatnonzero((x<0)|(y<0))[0]);k=int(n[j] if x[j]<0 else n[j]+1)
                violation={'A':A,'B':B,'C':int(c[j]),'D':int(d[j]),'Z':int(z[j]),'n':k,
                           'twice_slack':int(2*a[j]+2*k*linear[j]+k*(k+1)*t[j])};break
        if violation:break
    expected=(31*32//2)*31*31*32
    if not violation and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'point_sha256':EXPECTED,'scope':'all nonempty A,B,C,D subsets and any Z subset of five variables, overlaps allowed; A/B symmetry quotient',
         'substitutions_checked':checked,'complete_expected_count':expected,'all_positive_n':'quadratic exact minimum',
         'minimum_twice_slack':minimum,'max_vertex_neighbor_n':maxn,'first_violation':violation,
         'elapsed_seconds':monotonic()-start,
         'limits':'One named F_n family on one five-variable polymatroid. No Csirmaz-family overlapping coverage, entropy realization or broad novelty follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
