#!/usr/bin/env python3
"""Exact Psi5 scan on cross-copy marginals of the three-family star point, including tuple auxiliaries.

Roles C,R,H are disjoint nonempty blocks of the original ten variables, Z is
their complement, and P,Q are a branch-2/branch-3 auxiliary pair. Only this
specified substitution scope on one fixed LP point is checked.
"""
from fractions import Fraction
from itertools import combinations
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
PSI=('frontier-20261028-five-variable-nonshannon-witness-v1.json','def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392')
OUT=ROOT/'frontier-20261028-psi5-cross-tuple-scan-result.json'
ORIG=tuple('abcdefghij');VS=("d'1","e'1","g'2");WS=("f'3","g'3","h'4");V=tuple(c for k in range(1,4) for c in combinations(VS,k));W=tuple(c for k in range(1,4) for c in combinations(WS,k))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def profile(doc,syms=None):
    items=doc['primal_values'] if syms is None else doc['auxiliary_values'];out=[None]*1024
    if syms is None:out[0]=Fraction(0)
    for e in items:
        labs=e['entropy_variables'];selected=set(syms) if syms else set();allowed=set(ORIG)|selected
        if not set(labs)<=allowed or (syms is not None and not selected<=set(labs)):continue
        m=sum(1<<ORIG.index(v) for v in labs if v in ORIG)
        if out[m] is not None:raise ValueError('DUPLICATE')
        out[m]=Fraction(e['value'])
    if any(x is None for x in out):raise ValueError(('PROFILE_SIZE',syms))
    return out


def main():
    start=monotonic();base,c12,c13,psi=map(pin,(BASE,C12,C13,PSI))
    H=profile(base);D={v:profile(c12,v) for v in V};F={w:profile(c13,w) for w in W}
    scale=lcm(*(x.denominator for arr in [H,*D.values(),*F.values()] for x in arr))
    def integer(arr):return np.array([int(x*scale) for x in arr],dtype=np.int64)
    H=integer(H);D={k:integer(x) for k,x in D.items()};F={k:integer(x) for k,x in F.items()}
    terms=[(int(m),int(c)) for m,c in psi['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0 or any(m&24==24 for m,c in terms):raise ValueError('TERM_MAP')
    if max(abs(int(x)) for arr in [H,*D.values(),*F.values()] for x in arr)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    lowN=4**5;codes=np.arange(lowN,dtype=np.int64);low=[np.zeros(lowN,dtype=np.int64) for _ in range(3)]
    for i in range(5):
        digit=(codes//(4**i))%4
        for j in range(3):low[j]|=np.where(digit==j+1,1<<i,0)
    checked=0;minimum=None;viol=[]
    for high in range(4**5):
        masks=[0]*3
        for i in range(5):
            digit=(high//(4**i))%4
            if digit:masks[digit-1]|=1<<(5+i)
        roles=[low[j]|masks[j] for j in range(3)];ok=np.logical_and.reduce([x>0 for x in roles])
        if not np.any(ok):continue
        C,R,Hrole=[x[ok] for x in roles];z=1023^(C|R|Hrole)
        for v in V:
            for w in W:
                arr=(H,D[v],F[w]);result=np.zeros(len(z),dtype=np.int64)
                for m,c in terms:
                    q=z.copy()
                    for j,role in enumerate((C,R,Hrole)):
                        if m&(1<<j):q|=role
                    k=1 if m&8 else 2 if m&16 else 0
                    result+=c*arr[k][q]
                checked+=len(z);local=int(result.min());minimum=local if minimum is None else min(minimum,local)
                if local<0:
                    for i in np.flatnonzero(result<0)[:20]:
                        viol.append({'P':list(v),'Q':list(w),'C':int(C[i]),'R':int(R[i]),'H':int(Hrole[i]),
                                     'Z':int(z[i]),'exact_slack':str(Fraction(int(result[i]),scale))})
                    break
            if viol:break
        if viol:break
    expected=49*sum((-1)**k*comb(3,k)*(4-k)**10 for k in range(4))
    if not viol and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],'psi_sha256':PSI[1],
         'scope':'nonempty disjoint C,R,H blocks; conditioning exactly their complement in X; P/Q range over 49 nonempty auxiliary-subtuple pairs',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'violations':viol,'elapsed_seconds':monotonic()-start,
         'limits':'One fixed rational star point and one substitution pattern only. A violation excludes that fixed point if the written universal proof is admitted, not the original profile with different copies.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
