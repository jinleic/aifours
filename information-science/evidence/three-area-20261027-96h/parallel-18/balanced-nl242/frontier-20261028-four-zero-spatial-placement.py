#!/opt/homebrew/bin/python3
"""Construct a FORMAL placed spectrum satisfying selected spatial filters only.

This deliberately tests inverse realizability, and must not be called a witness.
"""
import argparse
import itertools
import json
import pathlib
import random
import time


def fwht(values):
    result=list(values); step=1
    while step<len(result):
        for i in range(0,len(result),2*step):
            for j in range(step):
                a,b=result[i+j],result[i+j+step]
                result[i+j],result[i+j+step]=a+b,a-b
        step*=2
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--histogram',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--seed',type=int,required=True)
    p.add_argument('--max-trials',type=int,required=True)
    p.add_argument('--max-seconds',type=int,required=True)
    args=p.parse_args()
    if args.output.exists() or args.candidate.exists(): raise FileExistsError('output exists')
    if not 1<=args.max_trials<=10000000 or not 1<=args.max_seconds<=120: raise ValueError('invalid bounds')
    source=json.loads(args.histogram.read_text(encoding='utf-8'))
    a={int(t):n for t,n in source['histogram'].items()}
    pweight=a[-7]+a[-1]+a[1]+a[7]
    qweight=a[-5]+a[-1]+a[3]+a[7]
    both=a[-1]+a[7]
    # Q is the nondegenerate quadratic x0*x1+x2*x3+x4*x5+x6*x7.
    qbits=sum(1<<x for x in range(256) if sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(4))%2)
    if (pweight,qweight,both,qbits.bit_count())!=(150,120,80,120): raise ValueError('input histogram not the pinned instance')
    terms=[sum(1<<i for i in subset) for d in range(5) for subset in itertools.combinations(range(8),d)]
    masks=[sum(1<<x for x in range(256) if x&term==term) for term in terms]
    tables=[]
    for base in range(0,len(masks),8):
        group=masks[base:base+8]; tab=[0]*(1<<len(group))
        for v in range(1,len(tab)):
            bit=v&-v; tab[v]=tab[v^bit]^group[bit.bit_length()-1]
        tables.append(tab)
    rng=random.Random(args.seed); start=time.monotonic(); found=None; trials=0
    for trials in range(1,args.max_trials+1):
        coeff=rng.getrandbits(len(terms)); q=coeff; bits=0
        for tab in tables:
            bits ^= tab[q & (len(tab)-1)]; q >>= 8
        if bits.bit_count()==pweight and (bits&qbits).bit_count()==both:
            found=(coeff,bits); break
        if trials%65536==0 and time.monotonic()-start>=args.max_seconds: break
    result={'rng':'python.Random MT19937','rng_seed':args.seed,'trials':trials,'max_trials':args.max_trials,
            'elapsed_seconds':time.monotonic()-start,'found_formal_placement':found is not None,
            'scope':'selected spatial filters only; not an actual Boolean spectrum'}
    if found:
        coeff,pbits=found
        # Independent Mobius transform recovers the algebraic normal form.
        anf=[(pbits>>x)&1 for x in range(256)]
        for bit in range(8):
            for x in range(256):
                if x&(1<<bit): anf[x]^=anf[x^(1<<bit)]
        degree=max((x.bit_count() for x,v in enumerate(anf) if v),default=0)
        assert degree<=4
        assert pbits.bit_count()==150 and (pbits&qbits).bit_count()==80
        # Distinct disjoint linear/affine planes realize the zero and |k|=4 XOR filters.
        k=[None]*512; zero={0,1,2,3}; four={4,5,6,7}
        for x in zero: k[x]=0
        for x in four: k[x]=4
        even=[x for x in range(256) if k[x] is None]
        vals=[-6]*a[-6]+[2]*a[2]+[6]*a[6]
        assert len(even)==len(vals)==248
        for x,v in zip(even,vals): k[x]=v
        classes={
            (1,0):[-7]*a[-7]+[1]*a[1], (1,1):[-1]*a[-1]+[7]*a[7],
            (0,0):[-3]*a[-3]+[5]*a[5], (0,1):[-5]*a[-5]+[3]*a[3],
        }
        for key,values in classes.items():
            coords=[x for x in range(256) if ((pbits>>x)&1,(qbits>>x)&1)==key]
            assert len(coords)==len(values)
            for x,v in zip(coords,values): k[256+x]=v
        assert all(x is not None for x in k)
        assert {t:k.count(t) for t in range(-7,8)}=={t:a[t]+(t==0) for t in range(-7,8)}
        assert k[0]==0 and max(map(abs,k))==7 and sum(k)==128 and sum(x*x for x in k)==16384
        assert all((v&1)==(x>>8) for x,v in enumerate(k))
        inv=fwht(k); bad=[x for x,v in enumerate(inv) if abs(v)!=128]
        if not bad:
            candidate={'format':'boolean-truth-v1','bits':''.join('1' if v==-128 else '0' for v in inv)}
            with args.candidate.open('x',encoding='utf-8') as out: json.dump(candidate,out,indent=2); out.write('\n')
        result.update({'p_anf_degree':degree,'p_anf_coefficients_hex':format(coeff,'x'),
                       'p_truth_bits_le_hex':format(pbits,'064x'),'q_truth_bits_le_hex':format(qbits,'064x'),
                       'p_weight':pweight,'q_weight':qweight,'p_q_intersection':both,
                       'zero_indices':sorted(zero),'absolute4_indices':sorted(four),
                       'spectrum_k':k,'inverse_nonsign_count':len(bad),
                       'inverse_max_abs':max(map(abs,inv)),'actual_boolean_witness_candidate':not bad})
    with args.output.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2,sort_keys=True); out.write('\n')
    print('formal_found=',found is not None,'trials=',trials,'inverse_nonsign=',result.get('inverse_nonsign_count'),flush=True)


if __name__=='__main__': main()
