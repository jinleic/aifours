#!/opt/homebrew/bin/python3
"""Assign signed odd values to one fixed common-q/mod8/quartic formal P."""
import argparse
import json
import pathlib
import time
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--base',type=pathlib.Path,required=True)
    p.add_argument('--P',type=pathlib.Path,required=True);p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('bad bounds/output')
    base=json.loads(args.base.read_text(encoding='utf-8'))['spectrum_k'];pdoc=json.loads(args.P.read_text(encoding='utf-8'))
    if not pdoc['found']:raise ValueError('no P candidate')
    P=int(pdoc['P_bits_le_hex'],16);q=[(base[x]//2)%2 for x in range(256)]
    assert P.bit_count()==160 and sum(q)==144 and sum(((P>>x)&1)*q[x] for x in range(256))==86
    # Four odd Q/P classes; alternative counts match the pinned model histogram.
    profiles={(0,1):(-7,1,1),(0,0):(5,-3,2),(1,1):(7,-1,0),(1,0):(-5,3,3)}
    defaults=[];delta=[];groups={key:[] for key in profiles}
    bits=[]
    for x in range(256):
        key=(q[x],(P>>x)&1);a,b,want=profiles[key];defaults.append(a);delta.append(b-a)
        v=z3.Bool('flip_'+str(x));bits.append(v);groups[key].append(v)
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    for key,vs in groups.items():s.add(z3.PbEq([(v,1) for v in vs],profiles[key][2]))
    for r in (64,128,192):
        even=sum(base[a]*base[a^r] for a in range(256))
        assert even%2==0
        terms=[];constant=0
        for x in range(256):
            y=x^r
            if x>=y:continue
            constant+=defaults[x]*defaults[y]
            terms.append(z3.If(bits[x],delta[x]*defaults[y],0))
            terms.append(z3.If(bits[y],delta[y]*defaults[x],0))
            terms.append(z3.If(z3.And(bits[x],bits[y]),delta[x]*delta[y],0))
        s.add(even//2+constant+z3.Sum(terms)==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'scope':'fixed q, even mod8, odd quartic P and histogram; three radical correlations only'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();k=base[:]
        for x in range(256):k[256|x]=defaults[x]+(delta[x] if z3.is_true(model.eval(bits[x],model_completion=True)) else 0)
        expected={-7:73,-6:53,-5:55,-4:56,-3:2,-2:1,-1:0,0:4,1:1,2:19,3:3,4:52,5:36,6:71,7:86}
        assert {t:k.count(t) for t in range(-7,8)}==expected and sum(k)==128 and sum(x*x for x in k)==16384
        shift=[]
        for x in range(256):
            g=(k[x]//2)%4;u=((k[256|x]-1)//2)%4
            assert (u-g)%2==0 and bool((P>>x)&1)==(u in (0,3))
            shift.append(((u-g)%4)//2)
        for i in range(8):
            for x in range(256):
                if x>>i&1:shift[x]^=shift[x^(1<<i)]
        assert not any(v and x.bit_count()>2 for x,v in enumerate(shift))
        corr=[sum(k[a]*k[a^b] for a in range(512)) for b in range(512)]
        assert corr[0]==16384 and all(corr[r]==0 for r in (64,128,192))
        nonrad=[b for b in range(1,512) if b not in (64,128,192) and corr[b]]
        inv=[sum(v*(-1 if (a&x).bit_count()%2 else 1) for a,v in enumerate(k)) for x in range(512)]
        bad=sum(abs(v)!=128 for v in inv)
        if not bad:
            with args.candidate.open('x',encoding='utf-8') as out:json.dump({'format':'boolean-truth-v1','bits':''.join('1' if v<0 else '0' for v in inv)},out,indent=2);out.write('\n')
        result.update({'spectrum_k':k,'radical_correlations':[corr[r] for r in (64,128,192)],
                       'nonradical_correlations_failing':len(nonrad),'first_nonradical_failure':nonrad[0] if nonrad else None,
                       'inverse_nonsign_count':bad,'boolean_candidate_written':not bad})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'nonrad_fail=',result.get('nonradical_correlations_failing'),flush=True)


if __name__=='__main__':main()
