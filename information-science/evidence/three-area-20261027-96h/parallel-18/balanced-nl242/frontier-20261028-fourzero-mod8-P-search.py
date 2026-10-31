#!/opt/homebrew/bin/python3
"""Bounded search for odd P in one fixed even mod8 polynomial extension coset."""
import argparse
import itertools
import json
import pathlib
import random
import time


def anf(values,n):
    a=list(values)
    for i in range(n):
        for x in range(1<<n):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--seed',type=int,required=True);p.add_argument('--max-trials',type=int,required=True)
    p.add_argument('--max-seconds',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.max_trials<=10000000 or not 1<=args.max_seconds<=120:raise ValueError('bad bounds/output')
    k=json.loads(args.input.read_text(encoding='utf-8'))['spectrum_k']
    if len(k)!=512:raise ValueError('spectrum size')
    terms=[sum(1<<i for i in I) for d in range(3) for I in itertools.combinations(range(8),d)];assert len(terms)==37
    masks=[sum(1<<x for x in range(256) if x&t==t) for t in terms];tables=[]
    for start in range(0,len(masks),8):
        group=masks[start:start+8];tab=[0]*(1<<len(group))
        for j in range(1,len(tab)):bit=j&-j;tab[j]=tab[j^bit]^group[bit.bit_length()-1]
        tables.append(tab)
    base=sum(1<<x for x in range(256) if (k[x]//2)%4 in (0,3))
    Q=sum(1<<x for x in range(256) if (k[x]//2)%2);assert Q.bit_count()==144
    rng=random.Random(args.seed);start=time.monotonic();found=None;hits=0;trials=0
    for trials in range(1,args.max_trials+1):
        coeff=rng.getrandbits(37);v=coeff;P=base
        for tab in tables:P^=tab[v&(len(tab)-1)];v>>=8
        if P.bit_count()==160:
            hits+=1
            if (P&Q).bit_count()==86:found=(coeff,P);break
        if trials%65536==0 and time.monotonic()-start>=args.max_seconds:break
    result={'seed':args.seed,'trials':trials,'weight160_hits':hits,'found':found is not None,
            'scope':'formal P with fixed even mod8 polynomial and common Q; no target realization'}
    if found:
        coeff,P=found;poly=anf([(P>>x)&1 for x in range(256)],8)
        quartic=[x for x,v in enumerate(poly) if v and x.bit_count()==4]
        assert quartic==[15,51,60] and not any(v and x.bit_count()>4 for x,v in enumerate(poly))
        result.update({'quadratic_shift_coefficients_hex':format(coeff,'x'),'P_bits_le_hex':format(P,'064x'),
                       'P_weight':160,'P_Q1_intersection':86,'quartic_terms':quartic,'actual_boolean_witness':False})
    result['elapsed_seconds']=time.monotonic()-start
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('trials=',trials,'weight_hits=',hits,'found=',found is not None,flush=True)


if __name__=='__main__':main()
