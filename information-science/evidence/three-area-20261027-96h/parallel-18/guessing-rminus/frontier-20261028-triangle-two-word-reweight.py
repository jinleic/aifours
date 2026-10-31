#!/usr/bin/env python3
"""Bounded variational search on one exact triangle-code replacement support.

Floating iterations propose distributions only. An exact polynomial test is
performed before any strict witness is claimed.
"""
from math import prod
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-triangle-two-word-reweight-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def codewords():
    n=1<<20;bits=np.arange(n,dtype=np.uint32);out=np.zeros((10,n),dtype=np.uint8)
    inc={v:[t for t,T in enumerate(TRI) if v in T] for v in range(1,11)}
    for t,(a,b,c) in enumerate(TRI):
        x=((bits>>(2*t))&1).astype(np.uint8);y=((bits>>(2*t+1))&1).astype(np.uint8)
        for v,z in ((a,x),(b,y),(c,x^y)):out[v-1]|=z<<inc[v].index(t)
    w1=np.array((1,0,0,0,0,0,0,0,0,0),dtype=np.uint8)
    w2=np.array((1,4,1,1,4,6,6,0,0,0),dtype=np.uint8)
    def syndrome(w):return sum((sum((int(w[v-1])>>inc[v].index(t))&1 for v in T)%2)<<t for t,T in enumerate(TRI))
    if (syndrome(w1),syndrome(w2))!=(1,2):raise ValueError('SYNDROME')
    D={v for v in range(1,11) if w1[v-1]!=w2[v-1]}
    if any(not any(u in D for u in N[v]) for v in D):raise ValueError('OUTLIER_CONFLICT')
    removed=[];sizes=[]
    for w,t in ((w1,0),(w2,1)):
        block=np.zeros(n,dtype=bool);fs=[]
        for v in TRI[t]:
            hit=np.ones(n,dtype=bool)
            for u in N[v]:hit &= out[u-1]==w[u-1]
            if np.any(block&hit):raise ValueError('FIBER_OVERLAP')
            fs.append(int(hit.sum()));block|=hit
        if sorted(fs)!=[4,32,32] or int(block.sum())!=68:raise ValueError('FIBER_COUNTS')
        removed.append(block);sizes.append(fs)
    intersection=int((removed[0]&removed[1]).sum());union=removed[0]|removed[1]
    if intersection!=5 or int(union.sum())!=131:raise ValueError('UNION')
    return np.concatenate((out[:,~union],w1[:,None],w2[:,None]),axis=1),sizes


def exact_polynomial(words,q):
    for scale in (8,32):
        t=np.rint(scale*np.cbrt(q)).astype(np.int64)
        D=prod(sum(int(x)**3 for x in row)**2 for row in t)
        # Exact arbitrary-precision sum; used only if a positive proposal appears.
        S=0
        for j in range(words.shape[1]):S+=prod(int(t[i,int(words[i,j])])**2 for i in range(10))
        if S**3>D:return {'scale':scale,'integer_rows':t.tolist(),'S':str(S),'D':str(D)}
    return None


def main():
    start=monotonic();words,sizes=codewords();rng=np.random.default_rng(2026102810)
    starts=[np.full((10,8),1/8)]+[rng.dirichlet(np.full(8,.7),size=10) for _ in range(2)]
    records=[];witness=None
    for sid,q in enumerate(starts):
        best=-1.;steps=0;change=None
        for step in range(60):
            if monotonic()-start>55:break
            lookup=np.maximum(q,1e-300)**(2/3);weights=np.ones(words.shape[1],dtype=np.float64)
            for i in range(10):weights*=lookup[i,words[i]]
            S=float(weights.sum());best=max(best,S);steps+=1
            new=np.empty((10,8))
            for i in range(10):new[i]=np.bincount(words[i],weights=weights,minlength=8)/S
            change=float(np.max(np.abs(new-q)));q=new
            if S>1+1e-8:
                witness=exact_polynomial(words,q)
                if witness:break
            if change<1e-12:break
        records.append({'start':sid,'iterations':steps,'maximum_S_float_unverified':best if steps else None,'final_max_coordinate_change':change})
        if witness:break
    out={'factor_count':10,'original_code_size':2**20,'removed_conflicts':131,'fiber_sizes':sizes,'fiber_overlap':5,
         'outside_words':words[:,-2:].T.tolist(),'replacement_support_size':words.shape[1],'starts':records,
         'strict_polynomial_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Two outside words and their maximal compatible old-code subset; bounded floating variational proposals only. Absence of a witness is not a global or exact no-go.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_polynomial_witness'},indent=2))


if __name__=='__main__':main()
