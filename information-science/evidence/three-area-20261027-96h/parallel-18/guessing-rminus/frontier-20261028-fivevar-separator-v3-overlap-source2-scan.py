#!/usr/bin/env python3
"""Exact all-k overlapping 2026 Theorem-2 scan on the five-variable separator.

Tests nonempty A,B,C,D and arbitrary Z as overlapping subsets, with no extra
outer conditioning W. A/B orders are both retained.
"""
from hashlib import sha256
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v3.json'
EXPECTED='c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-v3-overlap-source2-scan-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=np.array(json.loads(raw)['values_by_subset_mask'],dtype=np.int64)
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    C=np.repeat(np.arange(1,32,dtype=np.int64),31*32)
    D=np.tile(np.repeat(np.arange(1,32,dtype=np.int64),32),31)
    Z=np.tile(np.arange(32,dtype=np.int64),31*31)
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    checked=0;minimum=None;maxk=1;violation=None
    for A in range(1,32):
        for B in range(1,32):
            g=I(A,B,Z);zt=I(A,Z,B)+I(B,Z,A)
            ct=I(A,C,B)+I(B,C,A)
            ing=-I(A,C,0)+I(A,C,B)+I(A,C,D)+I(B,D,0)
            b=ing+zt
            if np.any(g<0) or np.any(ct<0):raise ValueError('SHANNON_COMPONENT')
            bad=(ct==0)&(b<0)
            if np.any(bad):
                j=int(np.flatnonzero(bad)[0]);k=int(g[j]//(-b[j])+1)
                violation={'A':A,'B':B,'C':int(C[j]),'D':int(D[j]),'Z':int(Z[j]),'k':k,
                           'twice_slack':int(2*g[j]+2*k*b[j])};checked+=len(Z);break
            k=np.ones(len(Z),dtype=np.int64);nz=ct>0
            k[nz]=np.maximum(1,np.floor_divide(ct[nz]-2*b[nz],2*ct[nz]));maxk=max(maxk,int((k+1).max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(b)),np.max(np.abs(ct)),1))
            if 2*bound*(maxk+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            q1=2*g+2*k*b+k*(k-1)*ct;q2=2*g+2*(k+1)*b+(k+1)*k*ct
            local=int(min(q1.min(),q2.min()));minimum=local if minimum is None else min(minimum,local);checked+=len(Z)
            if local<0:
                j=int(np.flatnonzero((q1<0)|(q2<0))[0]);kk=int(k[j] if q1[j]<0 else k[j]+1)
                violation={'A':A,'B':B,'C':int(C[j]),'D':int(D[j]),'Z':int(Z[j]),'k':kk,
                           'twice_slack':int(2*g[j]+2*kk*b[j]+kk*(kk-1)*ct[j])};break
        if violation:break
    expected=31**4*32
    if not violation and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'point_sha256':EXPECTED,'scope':'all nonempty A,B,C,D and arbitrary Z subsets with overlaps; W empty; A/B orders both',
         'substitutions_checked':checked,'complete_expected_count':expected,'all_positive_k':'exact quadratic minimum',
         'minimum_twice_slack':minimum,'max_vertex_neighbor_k':maxk,'first_violation':violation,
         'elapsed_seconds':monotonic()-start,
         'limits':'Only the 2026 source Theorem 2 with no outer conditioning on one 5-variable point; no theorem1 overlap, W != 0, entropic realization or literature completeness claim.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
