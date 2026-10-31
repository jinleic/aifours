#!/usr/bin/env python3
"""Search weights on one existing binary FD support for Delta>0.

Delta=H(V)-(2/3)sum_v H(v). A positive candidate would imply an actual
strict guessing-number gain by the pinned triangle balancing/type-class
construction. Floats only propose; integer entropy products decide a rounded
rational candidate, followed by independent verification.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,math
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
EXPECTED='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUTPUT=ROOT/'frontier-20261028-fd-balance-gap-search-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
RESTARTS=40;ITERATIONS=5000;MAX_SECONDS=25;TOTAL=6000


def rounded(p):
    x=p*TOTAL;w=np.floor(x).astype(np.int64);r=TOTAL-int(w.sum())
    if r:w[np.argsort(-(x-w))[:r]]+=1
    return [int(z) for z in w]


def exact(weights,B):
    n=sum(weights);right=n**(17*n)
    for w in weights:
        if w:right*=w**(3*w)
    left=1;counts=[]
    for v in range(10):
        a=sum(w*int(B[i,v]) for i,w in enumerate(weights));b=n-a;counts.append(a)
        if a:left*=a**(2*a)
        if b:left*=b**(2*b)
    return {'denominator':n,'vertex_one_counts':counts,'strict_positive_balance_gap':left>right,
            'comparison_L_bits':left.bit_length(),'comparison_R_bits':right.bit_length()}


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    words=json.loads(raw)['support_words_one_based_bitsets']
    if len(words)!=88 or len(set(words))!=88:raise ValueError('SUPPORT')
    for x,y in combinations(words,2):
        d=x^y
        if any((d>>(v-1))&1 and all(not ((d>>(u-1))&1) for u in N[v]) for v in range(1,11)):
            raise ValueError(('FD',x,y))
    B=np.array([[(w>>i)&1 for i in range(10)] for w in words],dtype=float)
    rng=np.random.default_rng(2026102804);best=None;candidate=None;steps=0;restarts=0
    for r in range(RESTARTS):
        if monotonic()-start>=MAX_SECONDS:break
        if r==0:logp=np.zeros(len(words))
        else:logp=rng.normal(0,0.5 if r<10 else 1.5 if r<25 else 3.0,len(words))
        for it in range(ITERATIONS):
            if it%100==0 and monotonic()-start>=MAX_SECONDS:break
            logp-=logp.max();p=np.exp(np.maximum(logp,-700));p/=p.sum()
            one=np.clip(p@B,1e-300,1-1e-15)
            joint=-float(np.dot(p,np.log(np.maximum(p,1e-300))))
            marginal=-one*np.log(one)-(1-one)*np.log(1-one)
            gap=joint-(2/3)*float(marginal.sum());steps+=1
            if best is None or gap>best['gap_nats']:
                best={'gap_nats':gap,'gap_bits':gap/math.log(2),'joint_nats':joint,
                      'marginal_one_probs':one.tolist(),'restart':r,'iteration':it}
            if gap>1e-7:
                weights=rounded(p);evidence=exact(weights,B)
                if evidence['strict_positive_balance_gap']:
                    candidate={'weights':weights,'exact_check':evidence};break
            observed=np.where(B>0.5,one[None,:],1-one[None,:])
            grad=-np.log(np.maximum(p,1e-300))-1+(2/3)*np.sum(np.log(np.maximum(observed,1e-300))+1,axis=1)
            logp+=(0.012/math.sqrt(1+it/300))*np.clip(grad,-100,100)
        restarts+=1
        if candidate:break
    out={'support_sha256':EXPECTED,'support_size':88,'original_FD_pair_vertex_checks':88*87//2*10,
         'seed':2026102804,'restarts_started':restarts,'optimizer_steps':steps,
         'best_float_unverified':best,'strict_rational_candidate':candidate,'elapsed_seconds':monotonic()-start,
         'limits':'Search only on the existing 88-word support. Positive float is not proof; any passing integer candidate requires independent verification and balancing/type-class construction.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_rational_candidate'},indent=2))
    if candidate:print('STRICT POSITIVE INTEGER GAP CANDIDATE: independent verification required')


if __name__=='__main__':main()
