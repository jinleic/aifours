#!/opt/homebrew/bin/python3
"""Bounded half-energy placement search for one fixed four-zero formal family."""
import argparse
import json
import pathlib
import time
import z3

N=512


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True)
    p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds or output')
    original=json.loads(args.input.read_text(encoding='utf-8'))['spectrum_k']
    if len(original)!=N:raise ValueError('wrong spectrum size')
    even=[a for a in range(256) if original[a]%4==2]
    odd=[a for a in range(256,512) if abs(original[a]) in (1,7)]
    odd1=[a for a in odd if original[a]%4==3];odd0=[a for a in odd if original[a]%4==1]
    assert (len(even),len(odd),len(odd1),len(odd0))==(112,224,128,96)
    E={a:z3.Bool(f'E_{a}') for a in even};U={a:z3.Bool(f'U_{a}') for a in odd}
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(z3.PbEq([(v,1) for v in E.values()],8))
    s.add(z3.PbEq([(U[a],1) for a in odd1],10),z3.PbEq([(U[a],1) for a in odd0],14))
    # Replace each |k|=2/6 even square by baseline 36, and each |k|=1/7
    # odd square by baseline 49. E and U reduce those baselines by 32 and 48.
    base=[v*v for v in original]
    for a in even:base[a]=36
    for a in odd:base[a]=49
    for direction in range(1,N):
        inside=[a for a in range(N) if not (a&direction).bit_count()%2]
        constant=sum(base[a] for a in inside)
        if constant%16:raise ValueError('fixed residue already violates half-energy condition')
        terms=[z3.If(E[a],2,0) for a in inside if a in E]+[z3.If(U[a],3,0) for a in inside if a in U]
        s.add(z3.Sum(terms)%8==(constant//16)%8)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'timeout_ms':args.timeout_ms,'scope':'fixed q,Q,P,zero-plane and histogram; 511 half-energy congruences only'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model(); e=[a for a,v in E.items() if z3.is_true(m.eval(v,model_completion=True))]
        u=[a for a,v in U.items() if z3.is_true(m.eval(v,model_completion=True))]
        assert len(e)==8 and len(u)==24
        k=original[:]
        for a in even:k[a]=2 if a in e else -6
        for a in [v for v in even if v not in e][:4]:k[a]=6
        for a in odd1:k[a]=-1 if a in u else 7
        for a in odd0:k[a]=1 if a in u else -7
        assert all(sum(k[a]*k[a] for a in range(N) if not (a&v).bit_count()%2)%128==0 for v in range(1,N))
        assert sum(x*x for x in k)==16384 and sum(k)==128 and k[0]==0
        inverse=[sum(t*(-1 if (a&x).bit_count()%2 else 1) for a,t in enumerate(k)) for x in range(N)]
        bad=sum(abs(v)!=128 for v in inverse)
        if not bad:
            with args.candidate.open('x',encoding='utf-8') as out:
                json.dump({'format':'boolean-truth-v1','bits':''.join('1' if v<0 else '0' for v in inverse)},out,indent=2);out.write('\n')
        result.update({'spectrum_k':k,'all_511_half_energy_mod128':True,'inverse_nonsign_count':bad,
                       'inverse_l1':sum(map(abs,inverse)),'candidate_written':not bad})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'candidate=',result.get('candidate_written'),flush=True)


if __name__=='__main__':main()
