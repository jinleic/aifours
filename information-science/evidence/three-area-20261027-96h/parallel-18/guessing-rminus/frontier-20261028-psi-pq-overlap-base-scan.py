#!/usr/bin/env python3
"""Exact fixed-profile Psi scan with overlapping P/Q and singleton C/R/H."""
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
from math import lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
PSI=('frontier-20261028-five-variable-nonshannon-witness-v1.json','def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392')
OUT=ROOT/'frontier-20261028-psi-pq-overlap-base-scan-result.json'
ORIG=tuple('abcdefghij')


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)


def main():
    start=monotonic();src,psi=map(pin,(BASE,PSI));values={0:Fraction(0)}
    for e in src['primal_values']:
        labs=e['entropy_variables']
        if not set(labs)<=set(ORIG):continue
        m=sum(1<<ORIG.index(x) for x in labs)
        if m in values:raise ValueError('DUPLICATE')
        values[m]=Fraction(e['value'])
    if len(values)!=1024:raise ValueError('PROFILE')
    terms=[(int(m),int(c)) for m,c in psi['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0:raise ValueError('PSI_TERMS')
    scale=lcm(*(x.denominator for x in values.values()));h=np.array([int(values[i]*scale) for i in range(1024)],np.int64)
    if max(abs(int(x)) for x in h)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    codes=np.arange(5**7,dtype=np.int64);digits=[(codes//5**i)%5 for i in range(7)]
    checked=0;minimum=None;example=None;violation=None
    for hpq in permutations(range(10),3):
        rem=[i for i in range(10) if i not in hpq];P=np.zeros(len(codes),np.int64);Q=P.copy();Z=P.copy()
        for k,i in enumerate(rem):
            P|=np.where((digits[k]==1)|(digits[k]==3),1<<i,0)
            Q|=np.where((digits[k]==2)|(digits[k]==3),1<<i,0)
            Z|=np.where(digits[k]==4,1<<i,0)
        keep=(P>0)&(Q>0)&((P&Q)>0);P=P[keep];Q=Q[keep];Z=Z[keep]
        blocks=(1<<hpq[0],1<<hpq[1],1<<hpq[2],P,Q);out=np.zeros(len(Z),np.int64)
        for mask,coef in terms:
            key=Z.copy()
            for i in range(5):
                if mask>>i&1:key|=blocks[i]
            out+=coef*h[key]
        checked+=len(out)
        k=int(np.argmin(out));val=int(out[k])
        if minimum is None or val<minimum:
            minimum=val;example={'C':1<<hpq[0],'R':1<<hpq[1],'H':1<<hpq[2],'P':int(P[k]),'Q':int(Q[k]),'Z':int(Z[k])}
        if val<0:violation={'scaled_slack':val,**example};break
    out={'base_sha256':BASE[1],'psi_sha256':PSI[1],
         'scope':'P,Q nonempty, ordered and overlapping; C,R,H distinct ordered singletons disjoint from P,Q,Z; Z arbitrary and disjoint; unused originals allowed',
         'substitutions_checked':checked,'minimum_scaled_slack':minimum,'entropy_integer_scale':str(scale),
         'minimum_example':example,'violation':violation,'elapsed_seconds':monotonic()-start,
         'limits':'One fixed rational original profile and this restricted substitution family only. Psi validity remains separately review-pending; a violation would not exclude alternate auxiliaries.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
