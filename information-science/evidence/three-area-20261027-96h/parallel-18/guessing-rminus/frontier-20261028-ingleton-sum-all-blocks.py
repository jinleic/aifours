#!/usr/bin/env python3
"""Exact all-order six-block scan of Csirmaz 2026 theorem 11 on one point.

Tests all disjoint original-variable blocks X,Y,A,B,C,D,W (first six
nonempty), using X/Y and C/D symmetries and discrete quadratic minimization.
An LP point passing a family is not an entropic or full-source LP witness.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
SOURCE=ROOT/'frontier-20261028-csirmaz-ingleton-stability-2026-v1.html'
SOURCE_SHA='36e107ae6654e59885f5ed264237134159238df72ca41072fd0d21e97ccba842'
OUTPUT=ROOT/'frontier-20261028-ingleton-sum-all-blocks-result.json'


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];vals={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    names='abcdefghij';h=[Fraction(0)]+[vals[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('INTEGER_RANGE')
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    def Ing(x,y,a,b,w):return -I(x,y,w)+I(x,y,a|w)+I(x,y,b|w)+I(a,b,w)
    low_n=8**6;codes=np.arange(low_n,dtype=np.int64)
    low=[np.zeros(low_n,dtype=np.int64) for _ in range(7)];t=codes.copy()
    for i in range(6):
        digit=t%8;t//=8
        for j in range(7):low[j]|=np.where(digit==j+1,1<<i,0)
    count=0;minimum=None;maxk=1;violation=None
    for code in range(8**4):
        t=code;high=[0]*7
        for i in range(6,10):
            digit=t%8;t//=8
            if digit:high[digit-1]|=1<<i
        sets=[low[j]|high[j] for j in range(7)]
        ok=(sets[0]>0)&(sets[1]>0)&(sets[2]>0)&(sets[3]>0)&(sets[4]>0)&(sets[5]>0)&(sets[0]<sets[1])&(sets[4]<sets[5])
        X,Y,A,B,C,D,W=(x[ok] for x in sets);count+=len(X)
        if not len(X):continue
        g=I(X,Y,W);a=I(X,A,Y|W)+I(Y,A,X|W)
        S=Ing(X,Y,A,B,W)+Ing(X,Y,C,D,W)+I(X,B,Y|W)+I(Y,B,X|W)
        if np.any(g<0) or np.any(a<0):raise ValueError('NEGATIVE_SHANNON_COMPONENT')
        zero=(a==0)&(S<0)
        if np.any(zero):
            j=int(np.flatnonzero(zero)[0]);k=int(g[j]//(-S[j])+1)
        else:
            kstar=np.ones(len(X),dtype=np.int64);nz=a>0
            kstar[nz]=np.maximum(1,-np.floor_divide(S[nz],2*a[nz]));maxk=max(maxk,int(kstar.max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(S)),np.max(np.abs(a)),1))
            if bound*(maxk+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            slack=g+kstar*S+kstar*(kstar-1)*a
            local=int(slack.min());minimum=local if minimum is None else min(minimum,local)
            negatives=np.flatnonzero(slack<0)
            if not len(negatives):continue
            j=int(negatives[0]);k=int(kstar[j])
        value=int(g[j]+k*S[j]+k*(k-1)*a[j])
        if value>=0:raise ValueError('BAD_WITNESS')
        violation={'masks':[int(x[j]) for x in (X,Y,A,B,C,D,W)],'k':k,
                   'scaled_terms':{'g':int(g[j]),'S':int(S[j]),'A':int(a[j])},
                   'exact_slack':str(Fraction(value,scale))}
        break
    expected=sum((-1)**k*comb(6,k)*(8-k)**10 for k in range(7))//4
    if not violation and count!=expected:raise ValueError(('COUNT',count,expected))
    out={'point_sha256':EXPECTED,'source_sha256':SOURCE_SHA,'scale':scale,
         'scope':'pairwise disjoint X,Y,A,B,C,D,W; first six nonempty; W optional; quotient X/Y and C/D swaps',
         'all_positive_k_by_discrete_quadratic':True,'substitutions_checked':count,'expected_if_complete':expected,
         'minimum_scaled_slack':minimum,'max_candidate_k':maxk,'exact_violation':violation,
         'elapsed_s':time.monotonic()-start,
         'limits':'One rational relaxation point only; empty or overlapping blocks, arbitrary functions, full-source extension and source theorem proof remain outside this scan.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
