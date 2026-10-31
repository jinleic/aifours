#!/usr/bin/env python3
"""Independent exact replay of the disjoint cross-copy Psi substitution scan.

Uses a 6+4 base-four enumeration split and directly contracts the original
conditioning complement. It checks one fixed three-family star primal only.
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
OUT=ROOT/'frontier-20261028-psi5-cross-tuple-independent-result.json'
ORIG=tuple('abcdefghij');VS=("d'1","e'1","g'2");WS=("f'3","g'3","h'4");V=tuple(c for k in range(1,4) for c in combinations(VS,k));W=tuple(c for k in range(1,4) for c in combinations(WS,k))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def profile(doc,syms=None):
    data=doc['primal_values'] if syms is None else doc['auxiliary_values'];out=[None]*1024
    if syms is None:out[0]=Fraction(0)
    for e in data:
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
    N=4**6;codes=np.arange(N,dtype=np.int64);low=[np.zeros(N,dtype=np.int64) for _ in range(3)]
    for j in range(6):
        digit=(codes//4**j)%4
        for k in range(3):low[k]|=np.where(digit==k+1,1<<j,0)
    checked=0;minimum=None;first=None
    for high in range(4**4):
        h=[0]*3
        for j in range(4):
            digit=(high//4**j)%4
            if digit:h[digit-1]|=1<<(6+j)
        blocks=[low[k]|h[k] for k in range(3)];valid=np.logical_and.reduce([x>0 for x in blocks])
        if not np.any(valid):continue
        C,R,Hr=[x[valid] for x in blocks];Z=1023^(C|R|Hr)
        for v in V:
            for w in W:
                arrays=(H,D[v],F[w]);value=np.zeros(len(Z),dtype=np.int64)
                for m,c in terms:
                    key=Z.copy()
                    if m&1:key|=C
                    if m&2:key|=R
                    if m&4:key|=Hr
                    index=1 if m&8 else 2 if m&16 else 0
                    value+=c*arrays[index][key]
                checked+=len(value);local=int(value.min());minimum=local if minimum is None else min(minimum,local)
                if local<0:
                    i=int(np.flatnonzero(value<0)[0]);first={'P':list(v),'Q':list(w),'C':int(C[i]),'R':int(R[i]),'H':int(Hr[i]),
                                                            'Z':int(Z[i]),'exact_slack':str(Fraction(int(value[i]),scale))};break
            if first:break
        if first:break
    expected=49*sum((-1)**k*comb(3,k)*(4-k)**10 for k in range(4))
    if not first and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],'psi_sha256':PSI[1],
         'enumeration_split':'base-four six lower / four upper original variables',
         'scope':'nonempty disjoint C,R,H blocks, Z exact original complement, 49 nonempty auxiliary-subtuple pairs',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'first_violation':first,'elapsed_seconds':monotonic()-start,
         'limits':'One fixed star profile and one substitution pattern only; other conditions/blocks and actual entropic realizability remain open.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
