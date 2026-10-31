#!/opt/homebrew/bin/python3
"""Construct an actual balanced four-block control with prescribed block XORs.

No peak bound is assumed; any target candidate must be independently verified.
"""
import argparse
import json
import pathlib
import random


def fwht(values):
    v=list(values);d=1
    while d<len(v):
        for i in range(0,len(v),2*d):
            for j in range(d):a,b=v[i+j],v[i+j+d];v[i+j],v[i+j+d]=a+b,a-b
        d*=2
    return v


def rank(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,required=True)
    p.add_argument('--max-attempts',type=int,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.candidate.exists() or args.output.exists() or not 1<=args.max_attempts<=10000:raise ValueError('invalid bounds/output')
    rng=random.Random(args.seed);found=None
    for attempt in range(1,args.max_attempts+1):
        blocks=[]
        for desired in (1,0,0,0):
            for _ in range(1000):
                chosen=set(rng.sample(range(128),63));xor=desired
                for x in chosen:xor^=x
                if xor not in chosen:chosen.add(xor);break
            else:raise RuntimeError('block generation failed')
            assert len(chosen)==64
            blocks.append(chosen)
        bits=[int((x&127) in blocks[x>>7]) for x in range(512)]
        W=fwht([1-2*v for v in bits]);assert all(w%4==0 for w in W)
        k=[w//4 for w in W];basis=[1<<i for i in range(1,9)]
        if k[0] or any(k[r] for r in (128,256,384)):raise AssertionError('four block zeros failed')
        def q(a):return (k[a]//2)%2
        rows=[sum((q(a^b)^q(a)^q(b))<<j for j,b in enumerate(basis)) for a in basis]
        if rank(rows)!=6:continue
        radical=[a for a in range(0,512,2) if all((q(a^b)^q(a)^q(b))==0 for b in basis)]
        if set(radical)!={0,128,256,384}:continue
        found=(attempt,bits,k,radical);break
    if found is None:
        with args.output.open('x',encoding='utf-8') as out:json.dump({'found':False,'attempts':args.max_attempts},out,indent=2);out.write('\n')
        print('found=false',flush=True);return
    attempt,bits,k,radical=found
    with args.candidate.open('x',encoding='utf-8') as out:json.dump({'format':'boolean-truth-v1','bits':''.join(map(str,bits))},out,indent=2);out.write('\n')
    peak=4*max(map(abs,k));zeros=[a for a,v in enumerate(k) if not v]
    receipt={'found':True,'seed':args.seed,'attempt':attempt,'block_support_xors':[1,0,0,0],
             'weight':sum(bits),'T':1,'zero_plane':[0,128,256,384],
             'even_polar_rank':6,'even_polar_radical':radical,'peak':peak,'zero_count':len(zeros),
             'target_candidate':peak<=28,'scope':'actual balanced control; no target claim unless independently verified'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('attempt=',attempt,'peak=',peak,'zeros=',len(zeros),'target=',peak<=28,flush=True)


if __name__=='__main__':main()
