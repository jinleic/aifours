#!/usr/bin/env python3
"""Joint support/weight search for the exact entropy-balance polynomial.

A greedy weighted independent-set proposal is alternated with the Gibbs/KL
marginal update. Any positive float must pass the exact integer polynomial and
then an independent FD / balancing verification. No failed search is a bound.
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
OUTPUT=ROOT/'frontier-20261028-weighted-confusability-search-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
MAX_SECONDS=26;MAX_TRIALS=120;MAX_STEPS=12


def polynomial(words,q,scale):
    ts=[[max(0,int(round(scale*(1-q[v])**(1/3)))),max(0,int(round(scale*q[v]**(1/3))))]
        for v in range(10)]
    if any(a==b==0 for a,b in ts):raise ValueError('ZERO_ROW')
    numerators=[]
    for w in words:
        x=1
        for v in range(10):x*=ts[v][(w>>v)&1]**2
        numerators.append(x)
    S=sum(numerators);D=1
    for a,b in ts:D*=(a**3+b**3)**2
    return {'weights_t':ts,'normalizer_S':str(S),'left_bits':(S**3).bit_length(),
            'right_bits':D.bit_length(),'strict_integer_witness':S**3>D,
            'law_numerators':[str(x) for x in numerators]}


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    seed=set(json.loads(raw)['support_words_one_based_bitsets'])
    masks={v:sum(1<<(u-1) for u in ns) for v,ns in N.items()}
    bad={d for d in range(1,1024) if any((d&(1<<(v-1))) and not(d&m) for v,m in masks.items())}
    if len(bad)!=113:raise ValueError('GRAPH')
    conflict=[sum(1<<(x^d) for d in bad) for x in range(1024)]
    def valid(W):
        return len(W)==len(set(W)) and all(not ((x^y) in bad) for x,y in combinations(W,2))
    if len(seed)!=88 or not valid(seed):raise ValueError('SEED_FD')
    bits=np.array([[(w>>v)&1 for v in range(10)] for w in range(1024)],dtype=float)
    rng=np.random.default_rng(2026102805);allmask=(1<<1024)-1
    def greedy(order):
        available=allmask;chosen=[]
        for x in order:
            x=int(x)
            if available>>x&1:
                chosen.append(x);available &= ~(conflict[x]|(1<<x))
        return chosen
    def improve(chosen,weight,order):
        W=set(chosen);changed=True;passes=0
        while changed and passes<4:
            changed=False;passes+=1
            for x in order:
                x=int(x)
                if x in W:continue
                blocked=[y for y in W if (x^y) in bad]
                if weight[x]>sum(weight[y] for y in blocked)+1e-15:
                    W.difference_update(blocked);W.add(x);changed=True
            if changed:
                eligible=[int(x) for x in order if int(x) not in W and all((int(x)^y) not in bad for y in W)]
                for x in eligible:
                    if all((x^y) not in bad for y in W):W.add(x)
        return sorted(W)
    best=None;witness=None;steps=0;trials=0
    for trial in range(MAX_TRIALS):
        if monotonic()-start>=MAX_SECONDS:break
        q=rng.beta(1.5 if trial%3==0 else 0.55,1.5 if trial%3==0 else 0.55,size=10)
        q=np.clip(q,1e-12,1-1e-12);current=sorted(seed)
        for step in range(MAX_STEPS):
            if monotonic()-start>=MAX_SECONDS:break
            logs=(2/3)*np.sum(np.where(bits>0.5,np.log(q)[None,:],np.log1p(-q)[None,:]),axis=1)
            weight=np.exp(logs)
            candidates=[current,sorted(seed)]
            for _ in range(3):
                jitter=np.exp(np.clip(rng.normal(0,0.28,1024),-2,2))
                order=np.argsort(-(weight*jitter));candidates.append(improve(greedy(order),weight,order))
            current=max(candidates,key=lambda w:float(weight[w].sum()))
            if not valid(current):raise ValueError('INVALID_GREEDY_SUPPORT')
            score=float(weight[current].sum());steps+=1
            if best is None or score>best['score_float']:
                best={'score_float':score,'support_size':len(current),'trial':trial,'step':step,
                      'q_one_probs':q.tolist(),'support':current}
            if score>1+1e-8:
                for scale in (50,200,1000):
                    proof=polynomial(current,q,scale)
                    if proof['strict_integer_witness']:
                        witness={'support':current,'polynomial':proof,'scale':scale};break
                if witness:break
            post=weight[current]/score;q=np.clip(post@bits[current],1e-12,1-1e-12)
        trials+=1
        if witness:break
    out={'input_support_sha256':EXPECTED,'seed':2026102805,'binary_forbidden_differences':len(bad),
         'trials_started':trials,'steps':steps,'best_float_unverified':best,'strict_integer_witness':witness,
         'elapsed_seconds':monotonic()-start,
         'limits':'Bounded joint q2 weighted-support search only. Floats are proposals; even an integer-positive witness needs an independent full-domain FD and balancing/type-class review.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_integer_witness'},indent=2))
    if witness:print('STRICT INTEGER POLYNOMIAL WITNESS: independent verification required')


if __name__=='__main__':main()
