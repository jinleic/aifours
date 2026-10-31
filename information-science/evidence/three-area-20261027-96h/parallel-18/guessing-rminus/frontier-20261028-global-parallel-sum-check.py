#!/usr/bin/env python3
"""Exact Shannon check of the canonical additive amalgam of the two star blocks.

This is a representation test, not an optimization or entropy-realizability claim.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
OUT=ROOT/'frontier-20261028-global-parallel-sum-check-result.json'
X=tuple('abcdefghij');U=("b'0",);V=("d'1","e'1","g'2");W=("f'3","g'3","h'4");ALL=X+U+V+W


def pin(item):
    data=(ROOT/item[0]).read_bytes()
    if sha256(data).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(data)


def block(base,doc,variables,common=None):
    out={0:Fraction(0)};index={v:i for i,v in enumerate(variables)}
    for e in base['primal_values']:
        labs=e['entropy_variables']
        if not set(labs)<=set(X):continue
        m=sum(1<<index[x] for x in labs)
        if m in out:raise ValueError('BASE_DUPLICATE')
        out[m]=Fraction(e['value'])
    if common is not None:
        for m in range(1024,2048):out[m]=common[m]
    for e in doc['auxiliary_values']:
        labs=e['entropy_variables']
        if not set(labs)<=set(variables):raise ValueError('BLOCK_LABEL')
        m=sum(1<<index[x] for x in labs)
        if m in out:raise ValueError('AUX_DUPLICATE')
        out[m]=Fraction(e['value'])
    if len(out)!=2**len(variables):raise ValueError('BLOCK_SIZE')
    return out


def main():
    base,c12,c13=map(pin,(BASE,C12,C13));v=block(base,c12,X+U+V);w=block(base,c13,X+U+W,v)
    for m in range(2048):
        if v[m]!=w[m]:raise ValueError('COMMON_OVERLAP')
    scale=lcm(*(q.denominator for q in v.values()),*(q.denominator for q in w.values()))
    a=np.array([int(v[m]*scale) for m in range(16384)],dtype=np.int64)
    b=np.array([int(w[m]*scale) for m in range(16384)],dtype=np.int64)
    if max(abs(int(k)) for k in np.concatenate((a,b)))*12>=2**62:raise ValueError('INTEGER_RANGE')
    z=np.arange(2**17,dtype=np.int64);common=z&2047;vi=z&16383;wi=common|((z>>3)&14336)
    h=a[vi]+b[wi]-a[common]
    checks=0;negative=0;minimum=None;worst=None;full=2**17-1
    def record(values,kind,i,j,conditioning):
        nonlocal checks,negative,minimum,worst
        checks+=len(values);negative+=int(np.count_nonzero(values<0))
        k=int(values.argmin());m=int(values[k]);
        if minimum is None or m<minimum:
            minimum=m;worst={'kind':kind,'i':ALL[i],'j':ALL[j] if j is not None else None,
                             'conditioning_mask':int(conditioning[k]),'exact_slack':str(Fraction(m,scale))}
    for i in range(17):
        record(np.array([h[full]-h[full^(1<<i)]],dtype=np.int64),'conditional_entropy',i,None,np.array([full^(1<<i)],dtype=np.int64))
    for i,j in combinations(range(17),2):
        ii,jj=1<<i,1<<j;free=full^ii^jj
        t=np.arange(2**15,dtype=np.int64);lo=t&((1<<i)-1);mid=((t>>i)&((1<<(j-i-1))-1))<<(i+1);hi=(t>>(j-1))<<(j+1);cond=lo|mid|hi
        if np.any(cond&~free) or len(np.unique(cond))!=2**15:raise ValueError('SUBSET_ENUMERATION')
        delta=h[cond|ii]+h[cond|jj]-h[cond|ii|jj]-h[cond]
        record(delta,'conditional_mutual_information',i,j,cond)
    if checks!=4456465:raise ValueError(('COUNT',checks))
    # Conditional mutual information I((U,V);W|X) in this specific amalgam.
    xm=1023;um=1<<10;vm=(7<<11);wm=(7<<14)
    block_ci=Fraction(int(h[xm|um|vm]+h[xm|wm]-h[xm|um|vm|wm]-h[xm]),scale)
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'construction':'h(S)=h_XUV(S∩(X,U,V))+h_XUW(S∩(X,U,W))-h_XU(S∩(X,U))',
         'elemental_checks':checks,'violated_elemental_rows':negative,'minimum_exact_slack':str(Fraction(minimum,scale)),
         'worst':worst,'all_checked_nonnegative':negative==0,'block_independence_I_UV_W_given_X':str(block_ci),
         'scale_digits':len(str(scale)),'limits':'Tests this single additive amalgam, not every global Shannon extension or an entropy realization.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
