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
OUT=ROOT/'frontier-20261028-triangle-one-word-reweight-result.json'
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
    w=np.zeros(10,dtype=np.uint8);w[0]=1<<inc[1].index(0)
    removed=np.zeros(n,dtype=bool);sizes=[]
    for v in TRI[0]:
        hit=np.ones(n,dtype=bool)
        for u in N[v]:hit &= out[u-1]==w[u-1]
        if np.any(removed&hit):raise ValueError('FIBER_OVERLAP')
        sizes.append(int(hit.sum()));removed|=hit
    if sizes!=[4,32,32] or int(removed.sum())!=68:raise ValueError('FIBER_COUNTS')
    return np.concatenate((out[:,~removed],w[:,None]),axis=1),sizes


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
    out={'factor_count':10,'original_code_size':2**20,'removed_conflicts':sum(sizes),'fiber_sizes':sizes,
         'outside_word':words[:,-1].tolist(),'replacement_support_size':words.shape[1],'starts':records,
         'strict_polynomial_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'One outside word and its maximal compatible old-code subset; bounded floating variational proposals only. Absence of a witness is not a global or exact no-go.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_polynomial_witness'},indent=2))


if __name__=='__main__':main()
