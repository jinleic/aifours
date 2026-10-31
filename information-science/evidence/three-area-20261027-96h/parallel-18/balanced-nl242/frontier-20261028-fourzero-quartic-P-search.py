#!/opt/homebrew/bin/python3
"""Bounded search for a formal P with rank-six quartic and prescribed counts."""
import argparse
import itertools
import json
import pathlib
import random
import time


def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,required=True)
    p.add_argument('--max-trials',type=int,required=True);p.add_argument('--max-seconds',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.max_trials<=10000000 or not 1<=args.max_seconds<=120:raise ValueError('bad bounds/output')
    terms=[sum(1<<i for i in I) for d in range(4) for I in itertools.combinations(range(8),d)]
    masks=[sum(1<<x for x in range(256) if x&t==t) for t in terms];assert len(terms)==93
    tables=[]
    for start in range(0,len(masks),8):
        group=masks[start:start+8];tab=[0]*(1<<len(group))
        for j in range(1,len(tab)):
            bit=j&-j;tab[j]=tab[j^bit]^group[bit.bit_length()-1]
        tables.append(tab)
    quartic=[15,51,60];omega=0
    for term in quartic:omega ^= sum(1<<x for x in range(256) if x&term==term)
    def q(x):return (sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1))%2
    Q=sum(1<<x for x in range(256) if q(x));assert Q.bit_count()==144
    rng=random.Random(args.seed);started=time.monotonic();found=None;trials=0;weight_hits=0
    for trials in range(1,args.max_trials+1):
        coef=rng.getrandbits(len(terms));v=coef;P=omega
        for tab in tables:P^=tab[v&(len(tab)-1)];v>>=8
        if P.bit_count()==160:
            weight_hits+=1
            if (P&Q).bit_count()==86:found=(coef,P);break
        if trials%65536==0 and time.monotonic()-started>=args.max_seconds:break
    result={'seed':args.seed,'trials':trials,'weight160_hits':weight_hits,'found':found is not None,
            'scope':'formal odd P and Q only; no k, autocorrelation or Boolean realization'}
    if found:
        coeff,P=found;anf=[(P>>x)&1 for x in range(256)]
        for i in range(8):
            for x in range(256):
                if x>>i&1:anf[x]^=anf[x^(1<<i)]
        assert [x for x,v in enumerate(anf) if v and x.bit_count()==4]==quartic
        assert not any(v and x.bit_count()>4 for x,v in enumerate(anf))
        result.update({'P_bits_le_hex':format(P,'064x'),'lower_anf_coefficients_hex':format(coeff,'x'),
                       'P_weight':160,'P_Q1_intersection':86,'quartic_terms':quartic,
                       'actual_boolean_witness':False})
    result['elapsed_seconds']=time.monotonic()-started
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('trials=',trials,'weight_hits=',weight_hits,'found=',found is not None,flush=True)


if __name__=='__main__':main()
