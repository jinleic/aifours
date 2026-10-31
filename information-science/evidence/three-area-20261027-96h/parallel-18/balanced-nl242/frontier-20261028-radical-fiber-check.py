#!/opt/homebrew/bin/python3
"""Finite checks for the analytic radical-fiber and pairing obstruction."""
import argparse
import functools
import json
import pathlib


def min_pair(values,counts):
    @functools.lru_cache(None)
    def f(state):
        if not any(state):return 0
        i=next(j for j,x in enumerate(state) if x)
        a=list(state);a[i]-=1;best=None
        for j in range(i,len(a)):
            if not a[j]:continue
            a[j]-=1;v=values[i]*values[j]+f(tuple(a));a[j]+=1
            best=v if best is None else min(best,v)
        if best is None:raise ValueError('unpaired multiset')
        return best
    return f(tuple(counts))


def main():
    p=argparse.ArgumentParser();p.add_argument('--histogram',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    data=json.loads(args.histogram.read_text(encoding='utf-8'));A={int(k):v for k,v in data['histogram'].items()}
    assert data['q_zero_count']==112 and data['even_g3_count']==108 and data['odd_Q_weight']==144
    assert {k:A[k] for k in (-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7)}=={-7:84,-6:36,-5:20,-4:92,-3:0,-2:0,-1:40,1:0,2:0,3:0,4:16,5:28,6:108,7:84}
    N=64;ALL=(1<<N)-1
    qplus=sum(1<<x for x in range(N) if sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2)
    qminus=sum(1<<x for x in range(N) if (sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1))%2)
    assert qplus.bit_count()==28 and qminus.bit_count()==36
    terms=[m for m in range(64) if m.bit_count()<=2]
    masks=[sum(1<<x for x in range(64) if x&m==m) for m in terms];assert len(terms)==22
    value=0;previous=0;contained=[0,0]
    for n in range(1<<22):
        gray=n^(n>>1)
        if n:value^=masks[(gray^previous).bit_length()-1]
        previous=gray
        for j,q in enumerate((qplus,qminus)):
            if not (value&(ALL^q)):
                assert value in (0,q);contained[j]+=1
    assert contained==[2,2]
    q0=min_pair((-7,5),(84,28));q1=min_pair((-5,-1,7),(20,40,84))
    assert q0==392 and q1==-392
    even_lower=36*4*36-27*4*16
    assert even_lower==3456 and even_lower+2*(q0+q1)==3456
    receipt={'quadratic_polynomials_checked':1<<22,'contained_in_qone_counts':contained,
             'quadratic_vanishing_on_qzero_only_zero_or_q':True,
             'Q0_min_unordered_pair_sum':q0,'Q1_min_unordered_pair_sum':q1,
             'odd_ordered_autocorrelation_lower':2*(q0+q1),'even_ordered_autocorrelation_lower':even_lower,
             'full_ordered_autocorrelation_lower':3456,'required_actual_autocorrelation':0,
             'note':'finite controls; all-variable proof and disjoint review remain necessary'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('quadratics=4194304 vanishing kernels=2,2 pair_min=',q0,q1,'R_lower=',even_lower,flush=True)


if __name__=='__main__':main()
