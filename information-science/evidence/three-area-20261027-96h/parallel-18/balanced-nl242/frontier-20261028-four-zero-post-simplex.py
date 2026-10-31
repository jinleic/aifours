#!/opt/homebrew/bin/python3
"""Four-zero count relaxation including rank, quartic and boundary simplex filters."""
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
    a={t:z3.Int(f'f_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()])
    s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(evenfirst==0,evenfirst==128))
    qz=4+a[-4]+a[4];qw=a[-5]+a[-1]+a[3]+a[7];pw=a[-7]+a[-1]+a[1]+a[7];intersection=a[-5]+a[3]
    s.add(z3.Or(*[z3.And(qz==z,z3.Or(*[qw==w for w in weights])) for z,weights in COMPAT.items()]))
    s.add(z3.If(z3.Or(qz==120,qz==136),pw%4==2,pw%4==0))
    rank6=z3.Or(qz==112,qz==144,z3.And(qz==128,z3.Or(qw==112,qw==144)))
    s.add(z3.Implies(z3.And(rank6,pw==224),z3.Or(*[z3.And(qw==w,intersection==c) for w,c in PHASE])))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'scope':'formal counts with listed constraints only; no code or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model();v={t:m.eval(a[t]).as_long() for t in a};Z=4+v[-4]+v[4];W=v[-5]+v[-1]+v[3]+v[7]
        P=v[-7]+v[-1]+v[1]+v[7];C=v[-5]+v[3]
        assert Z in COMPAT and W in COMPAT[Z] and P%4==(2 if Z in (120,136) else 0)
        if (Z in (112,144) or (Z==128 and W in (112,144))) and P==224:assert (W,C) in PHASE
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128 and sum(t*t*v[t] for t in v)==16384
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums)
        dual=[x//512 for x in nums];assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':Z,'odd_Q_weight':W,
                       'peakunit_weight':P,'nonpeak_Q_intersection':C,'peak_count':v[-7]+v[7],
                       'dual_coefficients_decimal':[str(x) for x in dual],'all_257_integral_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'z=',result.get('q_zero_count'),'P=',result.get('peakunit_weight'),flush=True)


if __name__=='__main__':main()
