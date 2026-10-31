#!/usr/bin/env python3
"""Independent exact verification of two disjoint-block 2026 source families.

Scans ordered A,B,C,D and optional Z using a different base-6 split and
quadratic-vertex formula from the exploratory producers. No source theorem is
claimed independently proved by this finite point check.
"""
from fractions import Fraction
from hashlib import sha256
from math import lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-five-variable-independent-check-result.json'


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values'];values={tuple(x['entropy_variables']):Fraction(x['value']) for x in items}
    if len(values)!=len(items):raise ValueError('DUPLICATE')
    names='abcdefghij';h=[Fraction(0)]+[values[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(v.denominator for v in h));H=np.array([int(v*scale) for v in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('INTEGER_RANGE')
    nlow=6**6;codes=np.arange(nlow,dtype=np.int64);low=[np.zeros(nlow,dtype=np.int64) for _ in range(5)]
    t=codes.copy()
    for i in range(6):
        digit=t%6;t//=6
        for j in range(5):low[j]|=np.where(digit==j+1,1<<i,0)
    def MI(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    total=0;neg1=0;neg2=0;min_v=None;min_twice=None;max_tested_k=1
    for code in range(6**4):
        t=code;high=[0]*5
        for i in range(6,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        groups=[low[j]|high[j] for j in range(5)]
        ok=(groups[0]>0)&(groups[1]>0)&(groups[2]>0)&(groups[3]>0)
        A,B,C,D,Z=(x[ok] for x in groups);total+=len(A)
        if not len(A):continue
        g=MI(A,B,Z)
        zz=MI(A,Z,B)+MI(B,Z,A)
        first=-MI(A,B,0)+MI(A,B,C)+MI(A,B,D)+MI(C,D,0)+zz
        Cterm=MI(A,C,B)+MI(B,C,A)
        Dterm=MI(A,D,B)+MI(B,D,A)
        if np.any(g<0) or np.any(Cterm<0) or np.any(Dterm<0):raise ValueError('SHANNON_COMPONENT')
        neg1+=int(np.count_nonzero(first<0))
        least=int(first.min());min_v=least if min_v is None else min(min_v,least)
        second=-MI(A,C,0)+MI(A,C,B)+MI(A,C,D)+MI(B,D,0)+zz
        if np.any((Cterm==0)&(second<0)):
            neg2+=int(np.count_nonzero((Cterm==0)&(second<0)))
        positive=Cterm>0
        k0=np.ones(len(A),dtype=np.int64)
        k0[positive]=np.maximum(1,np.floor_divide(Cterm[positive]-2*second[positive],2*Cterm[positive]))
        k1=k0+1;max_tested_k=max(max_tested_k,int(k1.max()))
        bound=int(max(np.max(np.abs(g)),np.max(np.abs(second)),np.max(np.abs(Cterm)),1))
        if 2*bound*(max_tested_k+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
        q0=2*g+2*k0*second+k0*(k0-1)*Cterm
        q1=2*g+2*k1*second+k1*(k1-1)*Cterm
        local=np.minimum(q0,q1);neg2+=int(np.count_nonzero(local<0))
        least=int(local.min());min_twice=least if min_twice is None else min(min_twice,least)
    expected=6**10-4*5**10+6*4**10-4*3**10+2**10
    if total!=expected:raise ValueError(('ENUMERATION_COUNT',total,expected))
    out={'input_sha256':EXPECTED,'scale':scale,'ordered_disjoint_substitutions':total,
         'theorem1_Ingleton_plus_Z_negative_count':neg1,'theorem1_min_scaled':min_v,
         'theorem2_all_positive_k_violation_count':neg2,'theorem2_min_twice_scaled':min_twice,
         'largest_adjacent_integer_checked':max_tested_k,'elapsed_s':time.monotonic()-started,
         'limits':'Exact finite-coordinate test on one relaxation point. Source theorem and full copy-LP feasibility remain separately unverified; no original bound follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
