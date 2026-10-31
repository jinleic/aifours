#!/opt/homebrew/bin/python3
"""Directly verify one labeled formal quotient-placement countercontrol."""
import argparse
import json
import pathlib


def anf(values,n):
    a=list(values)
    for i in range(n):
        for x in range(1<<n):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    return a


def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1)


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--fibers',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    d=json.loads(args.input.read_text(encoding='utf-8'));src=json.loads(args.fibers.read_text(encoding='utf-8'));k=d['spectrum_k']
    assert len(k)==512 and k[0]==0 and max(map(abs,k))<=7
    hist={int(t):v for t,v in src['histogram'].items()};hist[0]+=1
    assert {t:k.count(t) for t in range(-7,8)}==hist
    assert sum(k)==128 and sum(v*v for v in k)==16384
    zeros=[a for a,v in enumerate(k) if not v];assert zeros==[0,64,128,192]
    h=[]
    for x in range(64):
        for r in range(4):
            a=x|(r<<6);q=g0(x)%2
            assert (k[a]&1)==0 and (k[a]//2)%2==q
            assert ((k[256|a]-1)//2)%2==q
            assert (k[a]-k[x]-4*(r&1)*q)%8==0
    for a in range(256):
        diff=((k[a]//2)-g0(a&63))%4;assert diff%2==0;h.append(diff//2)
    coeff=anf(h,8);degree=max((x.bit_count() for x,v in enumerate(coeff) if v),default=0);assert degree<=3
    P=[int(abs(k[256|a]) in (1,7)) for a in range(256)];pcoeff=anf(P,8)
    pdegree=max(x.bit_count() for x,v in enumerate(pcoeff) if v);assert pdegree==d['odd_P_anf_degree']==7
    corr=[sum(k[a]*k[a^b] for a in range(512)) for b in range(512)]
    assert corr[0]==16384 and all(corr[b]==0 for b in (64,128,192))
    failures=[b for b in range(1,512) if b not in (64,128,192) and corr[b]]
    assert len(failures)==d['nonradical_correlations_failing']==506
    direct=[sum(v*(-1 if (a&x).bit_count()%2 else 1) for a,v in enumerate(k)) for x in range(512)]
    bad=sum(abs(v)!=128 for v in direct);assert bad==d['inverse_nonsign_count']==481
    changed=k[:];changed[256]+=2
    assert ((changed[256]-1)//2)%2!=g0(0)%2
    result={'same_histogram_as_formal_fibers':True,'zero_plane':[0,64,128,192],
            'common_q_and_odd_Q_checked':True,'even_mod8_h_anf_degree':degree,
            'lambda':1,'rho':0,'radical_correlations_zero':True,
            'odd_P_degree':pdegree,'odd_P_exceeds_forced_degree4':True,
            'nonradical_correlation_failures':len(failures),'first_failure':failures[0],
            'direct_inverse_nonsign_count':bad,'target_witness':False,
            'Q_mutation_rejected':True,'scope':'formal labeled spectrum, not Boolean realization'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('hdegree=',degree,'Pdegree=',pdegree,'nonrad_fail=',len(failures),'inverse_bad=',bad,flush=True)


if __name__=='__main__':main()
