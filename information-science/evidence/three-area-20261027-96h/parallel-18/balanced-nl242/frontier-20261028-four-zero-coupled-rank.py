#!/opt/homebrew/bin/python3
"""Formal four-zero histogram search with common even/odd quadratic rank.

A satisfying vector is not a code, spatial realization, or Boolean function.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

# Each mapping is q-zero count -> possible odd Q-one counts with the same polar rank.
COMPAT={64:(64,128,192),192:(64,128,192),96:(96,128,160),160:(96,128,160),
        112:(112,128,144),144:(112,128,144),120:(120,136),136:(120,136),
        128:(0,64,96,112,128,144,160,192,256),256:(0,128,256)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if not 1<=args.timeout_ms<=60000 or args.output.exists(): raise ValueError('invalid bounds or output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'e_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()])
    s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(evenfirst==0,evenfirst==128))
    qzeros=4+a[-4]+a[4];qones=a[-5]+a[-1]+a[3]+a[7]
    s.add(z3.Or(*[z3.And(qzeros==z,z3.Or(*[qones==v for v in values])) for z,values in COMPAT.items()]))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
                                                    'scope':'formal histogram only; no quadratic or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model();v={t:m.eval(a[t]).as_long() for t in a};qz=4+v[-4]+v[4];qo=v[-5]+v[-1]+v[3]+v[7]
        assert qz in COMPAT and qo in COMPAT[qz]
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128
        assert sum(t*t*v[t] for t in v)==16384 and sum(v[t] for t in v if t%2)==256
        assert v[-7]+v[7]>=92 and sum(t*v[t] for t in v if not t%2) in (0,128)
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums)
        dual=[x//512 for x in nums];assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':qz,'odd_Q_one_count':qo,
                       'peak_count':v[-7]+v[7],'dual_coefficients_decimal':[str(x) for x in dual],
                       'all_257_nonnegative_integral':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'qzeros=',result.get('q_zero_count'),'Qones=',result.get('odd_Q_one_count'),flush=True)


if __name__=='__main__':main()
