#!/usr/bin/env python3
"""Exact all-k scan of Csirmaz & Csirmaz (2026), Theorem 2, on one LP point.

Visual PDF equation (43), not the ambiguous extracted text, is used. Five
original-variable blocks are disjoint, with Z allowed empty. The point is not
claimed entropic; a violation proposes a valid source inequality, not a bound.
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
OUTPUT=ROOT/'frontier-20261028-five-variable-family-scan-result.json'
SOURCE=ROOT/'frontier-20261028-csirmaz-2026-five-variable.pdf'
SOURCE_SHA='401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6'


def main():
    start=time.monotonic();raw=INPUT.read_bytes();pdf=SOURCE.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(pdf).hexdigest()!=SOURCE_SHA:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];vals={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    B='abcdefghij';h=[Fraction(0)]+[vals[tuple(B[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('SCALE_RANGE')
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    low_count=6**7;codes=np.arange(low_count,dtype=np.int64)
    low=[np.zeros(low_count,dtype=np.int64) for _ in range(5)];t=codes.copy()
    for i in range(7):
        digit=t%6;t//=6
        for j in range(5):low[j]|=np.where(digit==j+1,1<<i,0)
    count=0;found=None;max_k=1;min_twice=None
    for code in range(6**3):
        t=code;high=[0]*5
        for i in range(7,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        sets=[low[j]|high[j] for j in range(5)]
        valid=(sets[0]>0)&(sets[1]>0)&(sets[2]>0)&(sets[3]>0)
        A,B,C,D,Z=(x[valid] for x in sets);count+=len(A)
        if not len(A):continue
        g=I(A,B,Z)
        ing=-I(A,C,0)+I(A,C,B)+I(A,C,D)+I(B,D,0)
        zterm=I(A,Z,B)+I(B,Z,A)
        cterm=I(A,C,B)+I(B,C,A)
        b=ing+zterm
        if np.any(g<0) or np.any(cterm<0):raise ValueError('SHANNON_COMPONENT_NEGATIVE')
        zero=(cterm==0)&(b<0)
        if np.any(zero):
            j=int(np.flatnonzero(zero)[0]);k=int(g[j]//(-b[j])+1)
        else:
            kstar=np.ones(len(A),dtype=np.int64);nz=cterm>0
            kstar[nz]=np.maximum(1,-np.floor_divide(b[nz],cterm[nz]))
            max_k=max(max_k,int(kstar.max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(b)),np.max(np.abs(cterm)),1))
            if 2*bound*(max_k+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            twice=2*g+2*kstar*b+kstar*(kstar-1)*cterm
            least=int(twice.min());min_twice=least if min_twice is None else min(min_twice,least)
            bad=np.flatnonzero(twice<0)
            if not len(bad):continue
            j=int(bad[0]);k=int(kstar[j])
        slack=Fraction(int(2*g[j]+2*k*b[j]+k*(k-1)*cterm[j]),2*scale)
        if slack>=0:raise ValueError('FALSE_VIOLATION')
        found={'masks':[int(x[j]) for x in (A,B,C,D,Z)],'k':k,
               'g_scaled':int(g[j]),'b_scaled':int(b[j]),'c_scaled':int(cterm[j]),
               'exact_slack':str(slack)}
        break
    out={'input_sha256':EXPECTED,'source_pdf_sha256':SOURCE_SHA,'base_scale':scale,
         'formula':'I(A;B|Z)+k([A C B D]+I(A;Z|B)+I(B;Z|A))+k(k-1)/2*(I(A;C|B)+I(B;C|A)) >= 0',
         'scope':'pairwise disjoint A,B,C,D,Z original-vertex blocks, A,B,C,D nonempty, Z may be empty, A/B ordered',
         'all_positive_k_checked_via_quadratic_minimum':True,
         'substitutions_checked_before_stop':count,'witness':found,
         'min_twice_slack_scaled':min_twice,'max_candidate_k':max_k,'elapsed_s':time.monotonic()-start,
         'limits':'Exact scan of one non-entropic-feasibility-unestablished LP point. Source theorem is an external mathematical import pending full proof/source audit; no original guessing-number bound follows from this scan alone.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
