#!/opt/homebrew/bin/python3
"""Formal counts for one rank8 ten-Z8-point mod8 lift; not a target witness."""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'tz_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==9,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-4]+a[4]==126,a[-2]+a[6]==60,a[-6]+a[2]==60)
    s.add(a[-7]+a[7]>=92,a[-7]+a[7]<=210)
    P=a[-7]+a[-1]+a[1]+a[7];w=a[-5]+a[-1]+a[3]+a[7]
    s.add(P<=210,P%4==2,z3.Or(w==120,w==136))
    ef=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(ef==0,ef==128))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
          'scope':'formal scalar counts compatible with one even mod8 lift; no code or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();v={t:model.eval(a[t]).as_long() for t in a}
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(n%512==0 and n>=0 for n in nums);D=[n//512 for n in nums]
        assert D[0]==1 and D[1]==D[2]==D[256]==0 and D[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':136,
                       'even_g3_count':60,'odd_Q_weight':v[-5]+v[-1]+v[3]+v[7],
                       'peakunit_weight':v[-7]+v[-1]+v[1]+v[7], 'peak_count':v[-7]+v[7],
                       'dual_coefficients_decimal':[str(x) for x in D], 'all_257_duals_integral_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'P=',result.get('peakunit_weight'),flush=True)


if __name__=='__main__':main()
