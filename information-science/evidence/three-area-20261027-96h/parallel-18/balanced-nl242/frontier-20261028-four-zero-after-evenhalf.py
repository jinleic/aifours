#!/opt/homebrew/bin/python3
"""Bounded formal four-zero count search including the even-half lower bound.

Any result remains a count relaxation, not a Boolean code/function.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

QWEIGHTS=(0,64,96,112,120,128,136,144,160,192,256)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True); args=p.parse_args()
    if not 1<=args.timeout_ms<=60000: raise ValueError('bad timeout')
    if args.output.exists(): raise FileExistsError(args.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('histogram_base',path); base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    a={t:z3.Int(f'd_{t:+d}') for t in range(-7,8)}
    s=z3.Solver(); s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()])
    s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]); s.add(z3.Or(evenfirst==0,evenfirst==128))
    s.add(a[-4]+a[4]>=60)
    # The already adopted odd-half sign function is genuinely quadratic;
    # unlike the earlier exploratory file, no degree-two claim is made for P.
    signweight=a[-5]+a[-1]+a[3]+a[7]
    s.add(z3.Or(*[signweight==v for v in QWEIGHTS]))
    for j in range(15):
        s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    started=time.monotonic(); status=s.check(); elapsed=time.monotonic()-started
    result={'status':str(status),'solve_seconds':elapsed,'timeout_ms':args.timeout_ms,
            'scope':'formal count relaxation; no Boolean realization'}
    if status==z3.unknown: result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model(); v={t:m.eval(a[t]).as_long() for t in a}
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128
        assert sum(t*t*v[t] for t in v)==16384 and sum(v[t] for t in v if t%2)==256
        assert v[-4]+v[4]>=60 and v[-7]+v[7]>=92
        assert sum(t*v[t] for t in v if not t%2) in (0,128)
        assert v[-5]+v[-1]+v[3]+v[7] in QWEIGHTS
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(n%512==0 and n>=0 for n in nums)
        d=[n//512 for n in nums]; assert d[0]==1 and d[1]==d[2]==d[256]==0 and d[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v}, 'magnitude16_count':v[-4]+v[4],
                       'magnitude28_count':v[-7]+v[7], 'odd_sign_weight':v[-5]+v[-1]+v[3]+v[7],
                       'dual_coefficients_decimal':[str(x) for x in d], 'all_257_integral_and_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'solve_seconds=',round(elapsed,3),'F=',result.get('magnitude16_count'),flush=True)


if __name__=='__main__': main()
