#!/opt/homebrew/bin/python3
"""Bounded full mod-8 polynomial-extension search for one formal histogram.

SAT is a formal residue placement, NOT a Boolean target unless independently checked.
"""
import argparse
import functools
import itertools
import json
import pathlib
import time
import z3

TERMS=[sum(1<<i for i in I) for d in range(4) for I in itertools.combinations(range(8),d)]


def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1)

def fwht(k):
    w=k[:];d=1
    while d<len(w):
        for i in range(0,len(w),2*d):
            for j in range(d):a,b=w[i+j],w[i+j+d];w[i+j],w[i+j+d]=a+b,a-b
        d*=2
    return w


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    assert len(TERMS)==93
    coeff=[z3.Bool('h'+str(i)) for i in range(93)]
    h=[]
    for x in range(256):
        selected=[coeff[i] for i,t in enumerate(TERMS) if x&t==t]
        h.append(functools.reduce(z3.Xor,selected))
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    odd=[];even=[]
    for x in range(256):
        g=g0(x)
        if g%2:odd.append(x)
        else:
            even.append(x);rhs=((g//2)&1)^int((x&63)!=0)
            s.add(h[x] if rhs else z3.Not(h[x]))
    assert len(even)==112 and len(odd)==144
    g3=[z3.Xor(h[x],z3.BoolVal(g0(x)%4==3)) for x in odd]
    s.add(z3.PbEq([(v,1) for v in g3],108))
    mu=z3.BitVec('mu',2);L=[z3.BitVec('L'+str(i),2) for i in range(8)]
    C={(i,j):z3.Bool('C'+str(i)+'_'+str(j)) for i in range(8) for j in range(i+1,8)}
    u=[]
    for x in range(256):
        val=mu+z3.BitVecVal(g0(x)%4,2)+z3.If(h[x],z3.BitVecVal(2,2),z3.BitVecVal(0,2))
        for i in range(8):
            if x>>i&1:val=val+L[i]
        for (i,j),c in C.items():
            if x>>i&1 and x>>j&1:val=val+z3.If(c,z3.BitVecVal(2,2),z3.BitVecVal(0,2))
        u.append(val)
    # Fixed surviving histogram: odd k residues 1,3,5,7 have these counts.
    for residue,count in enumerate((84,20,28,124)):
        s.add(z3.PbEq([(v==residue,1) for v in u],count))
    start=time.monotonic();status=s.check();result={'status':str(status),'timeout_ms':args.timeout_ms,
        'solve_seconds':time.monotonic()-start,'scope':'exact full mod8 polynomial residue relaxation; no Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();H=[z3.is_true(model.eval(v,model_completion=True)) for v in h]
        ev=[(g0(x)+2*H[x])%4 for x in range(256)]
        uv=[model.eval(v,model_completion=True).as_long() for v in u]
        assert [uv.count(j) for j in range(4)]==[84,20,28,124]
        assert sum(ev[x]==3 for x in odd)==108
        k=[None]*512
        # The radical is x&63==0, qzero is even g0.
        f4=[x for x in even if x&63];assert len(f4)==108
        for x in even:k[x]=0 if not (x&63) else -4
        for x in f4[:16]:k[x]=4
        for x in odd:k[x]=6 if ev[x]==3 else -6
        r7=[]
        for x,v in enumerate(uv):
            if v==0:k[256+x]=-7
            elif v==1:k[256+x]=-5
            elif v==2:k[256+x]=5
            else:k[256+x]=-1;r7.append(x)
        assert len(r7)==124
        for x in r7[:84]:k[256+x]=7
        expected={-7:84,-6:36,-5:20,-4:92,-3:0,-2:0,-1:40,0:4,1:0,2:0,3:0,4:16,5:28,6:108,7:84}
        assert {t:k.count(t) for t in range(-7,8)}==expected
        assert k[0]==0 and sum(k)==128 and sum(v*v for v in k)==16384
        inv=fwht(k);bad=sum(abs(v)!=128 for v in inv)
        if not bad:
            with args.candidate.open('x',encoding='utf-8') as out:json.dump({'format':'boolean-truth-v1','bits':''.join('1' if v<0 else '0' for v in inv)},out,indent=2);out.write('\n')
        result.update({'spectrum_k':k,'odd_residue_counts':[84,20,28,124],'even_g3_count':108,
                       'inverse_nonsign_count':bad,'candidate_written':not bad})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'candidate=',result.get('candidate_written'),flush=True)


if __name__=='__main__':main()
