#!/usr/bin/env python3
"""Exact F_n scan with overlapping A/B and singleton C/D in original variables.

A,B may overlap; C,D are distinct singleton vertices disjoint from A,B,Z;
Z is an arbitrary disjoint block, with other vertices unused. All n>=1 are
minimized analytically. This tests one fixed rational original profile only.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
OUT=ROOT/'frontier-20261028-fn-overlap-base-scan-result.json'
ORIG=tuple('abcdefghij')


def main():
    start=monotonic();raw=(ROOT/BASE[0]).read_bytes()
    if sha256(raw).hexdigest()!=BASE[1]:raise ValueError('HASH')
    src=json.loads(raw);v={0:Fraction(0)}
    for e in src['primal_values']:
        labs=e['entropy_variables']
        if not set(labs)<=set(ORIG):continue
        m=sum(1<<ORIG.index(x) for x in labs)
        if m in v:raise ValueError('DUPLICATE')
        v[m]=Fraction(e['value'])
    if len(v)!=1024:raise ValueError('PROFILE')
    scale=lcm(*(x.denominator for x in v.values()));h=np.array([int(v[i]*scale) for i in range(1024)],np.int64)
    codes=np.arange(5**8,dtype=np.int64);digits=[(codes//5**i)%5 for i in range(8)]
    checked=0;minimum=None;min_example=None;violation=None
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    for c,d in combinations(range(10),2):
        rem=[i for i in range(10) if i not in (c,d)];A=np.zeros(len(codes),np.int64);B=A.copy();Z=A.copy()
        for k,i in enumerate(rem):
            A|=np.where((digits[k]==1)|(digits[k]==3),1<<i,0)
            B|=np.where((digits[k]==2)|(digits[k]==3),1<<i,0)
            Z|=np.where(digits[k]==4,1<<i,0)
        keep=(A>0)&(B>0)&(A<=B)&((A&B)>0);aa=A[keep];bb=B[keep];zz=Z[keep]
        for C,D in ((1<<c,1<<d),(1<<d,1<<c)):
            a=I(aa,bb,C|zz);c0=a+I(aa,bb,D|zz)+I(C,D,zz)-I(aa,bb,zz)
            d0=I(aa,C,bb|zz)+I(bb,C,aa|zz)
            if np.any(a<0) or np.any(d0<0):raise ValueError('SHANNON_FAILURE')
            bad=(d0==0)&(c0<0)
            if np.any(bad):
                k=int(np.flatnonzero(bad)[0]);violation={'kind':'negative_as_n_grows','A':int(aa[k]),'B':int(bb[k]),'C':C,'D':D,'Z':int(zz[k]),'a':int(a[k]),'c':int(c0[k]),'d':int(d0[k])};break
            nn=np.ones(len(aa),dtype=np.int64);ok=d0>0;nn[ok]=np.maximum(1,-np.floor_divide(c0[ok],d0[ok])-1)
            bound=max(int(np.max(np.abs(a))),int(np.max(np.abs(c0))),int(np.max(np.abs(d0))),1);nmax=int(nn.max())
            if 2*bound*(nmax+1)**2>=2**62:raise ValueError('INTEGER_OVERFLOW_RISK')
            twice=2*a+2*nn*c0+nn*(nn+1)*d0;checked+=len(twice)
            if len(twice):
                k=int(np.argmin(twice));val=int(twice[k])
                if minimum is None or val<minimum:minimum=val;min_example={'A':int(aa[k]),'B':int(bb[k]),'C':C,'D':D,'Z':int(zz[k]),'n':int(nn[k])}
                if val<0:violation={'kind':'finite_n','twice_scaled_slack':val,**min_example};break
        if violation:break
    out={'base_sha256':BASE[1],'scope':'A,B nonempty and overlapping; A<=B; C,D ordered distinct singletons disjoint from A,B,Z; Z arbitrary and disjoint; unused originals allowed; all positive n',
         'all_n_minima_checked':checked,'minimum_twice_scaled_slack':minimum,'entropy_integer_scale':str(scale),
         'minimum_example':min_example,'violation':violation,'elapsed_seconds':monotonic()-start,
         'limits':'Fixed original Shannon-LP point and this restricted overlapping substitution family only; no entropy realization or global family claim.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
