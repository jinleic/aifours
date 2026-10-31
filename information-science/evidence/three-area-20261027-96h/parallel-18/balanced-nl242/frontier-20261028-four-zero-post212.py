#!/opt/homebrew/bin/python3
"""Formal four-zero counts surviving currently written rank/phase candidates."""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

COMPAT={64:(64,128,192),192:(64,128,192),96:(96,128,160),160:(96,128,160),
        112:(112,128,144),144:(112,128,144),120:(120,136),136:(120,136),
        128:(0,64,96,112,128,144,160,192,256),256:(0,128,256)}
PHASE=((112,12),(112,28),(128,16),(144,4),(144,20))


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'g_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()])
    s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(evenfirst==0,evenfirst==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3]
    s.add(z3.Or(*[z3.And(z==k,z3.Or(*[w==v for v in vals])) for k,vals in COMPAT.items()]))
    rank8=z3.Or(z==120,z==136)
    rank6=z3.Or(z==112,z==144,z3.And(z==128,z3.Or(w==112,w==144)))
    s.add(z3.If(rank8,P%4==2,P%4==0))
    s.add(z3.Implies(rank8,P<=210),z3.Implies(rank6,z3.And(P<=224,P!=220)))
    s.add(z3.Implies(z3.And(rank6,P==224),z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(z3.And(rank6,P==216),z3.If(w==128,c==20,c%8==4)))
    s.add(z3.Implies(z3.And(rank6,P==212,w==112),c>=16))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
      'scope':'formal counts only; no spatial, code or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model();v={t:m.eval(a[t]).as_long() for t in a};Z=4+v[-4]+v[4];W=v[-5]+v[-1]+v[3]+v[7]
        Pn=v[-7]+v[-1]+v[1]+v[7];C=v[-5]+v[3]
        assert Z in COMPAT and W in COMPAT[Z] and Pn%4==(2 if Z in (120,136) else 0)
        r6=Z in (112,144) or (Z==128 and W in (112,144));r8=Z in (120,136)
        assert not r8 or Pn<=210
        if r6:
            assert Pn<=224 and Pn!=220
            if Pn==224:assert (W,C) in PHASE
            if Pn==216:assert C==20 if W==128 else C%8==4
            if Pn==212 and W==112:assert C>=16
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128 and sum(t*t*v[t] for t in v)==16384
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums)
        dual=[x//512 for x in nums];assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':Z,'odd_Q_weight':W,
          'peakunit_weight':Pn,'nonpeak_Q_intersection':C,'peak_count':v[-7]+v[7],
          'dual_coefficients_decimal':[str(x) for x in dual],'all_257_integral_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'z=',result.get('q_zero_count'),'P=',result.get('peakunit_weight'),flush=True)


if __name__=='__main__':main()
