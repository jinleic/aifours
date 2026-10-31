#!/opt/homebrew/bin/python3
"""Check kernel-direction affine derivative and fixed-histogram bounds."""
import argparse
import importlib.util
import json
import pathlib


def anf(v,n):
    a=v[:]
    for i in range(n):
        for x in range(1<<n):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--P',type=pathlib.Path,required=True)
    p.add_argument('--model',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    doc=json.loads(args.P.read_text(encoding='utf-8'));P=int(doc['P_bits_le_hex'],16)
    model=json.loads(args.model.read_text(encoding='utf-8'));a={int(k):v for k,v in model['histogram'].items()}
    assert P.bit_count()==160 and model['lambda_mode']==1 and model['qrad_bit']==0
    derivative=[((P>>x)&1)^((P>>(x^128))&1) for x in range(256)]
    coeff=anf(derivative,8);degree=max((i.bit_count() for i,v in enumerate(coeff) if v),default=0)
    assert degree<=1 and sum(derivative)==128
    intersection=sum(((P>>x)&1)*((P>>(x^128))&1) for x in range(256));assert intersection==96
    path=pathlib.Path(__file__).with_name('frontier-20261028-radical-fiber-check.py')
    spec=importlib.util.spec_from_file_location('pairbase',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    # Minima below count each unordered pair once; multiply by two for C(r).
    minima=[base.min_pair((-4,4),(a[-4],a[4])),base.min_pair((-6,2),(a[-6],a[2])),
            base.min_pair((-2,6),(a[-2],a[6]))]
    assert minima==[-800,384,1248]
    even=2*sum(minima);assert even==1664
    exceptions=a[1]+a[-3]+a[-1]+a[3];assert exceptions==6
    baseline=144*intersection-12800;assert baseline==1024
    odd_lower=baseline-112*exceptions;assert odd_lower==352
    assert even+odd_lower==2016
    mutated=P
    # A cubic r0*x0*x1 term changes D_r0P by x0*x1, which is not affine.
    for x in range(256):
        if (x&128) and (x&1) and (x&2):mutated ^= 1<<x
    test=anf([((mutated>>x)&1)^((mutated>>(x^128))&1) for x in range(256)],8)
    assert any(v and x.bit_count()==2 for x,v in enumerate(test))
    result={'P_weight':160,'kernel_derivative_degree':degree,'derivative_weight':128,'P_pair_intersection':intersection,
            'even_pair_lower_bound':even,'odd_baseline':baseline,'signed_exceptions':exceptions,
            'odd_lower_bound':odd_lower,'total_autocorrelation_lower':even+odd_lower,
            'required_boolean_autocorrelation':0,'quadratic_derivative_mutation_rejected':True,
            'scope':'finite control for written all-placement theorem, not target existence'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('affine_derivative=',degree,'even_lower=',even,'odd_lower=',odd_lower,'total=',even+odd_lower,flush=True)


if __name__=='__main__':main()
