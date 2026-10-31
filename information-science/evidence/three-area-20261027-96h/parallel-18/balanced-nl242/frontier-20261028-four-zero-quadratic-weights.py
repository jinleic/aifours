#!/opt/homebrew/bin/python3
"""Find a four-zero histogram satisfying three quadratic-weight restrictions.

A satisfying formal vector is NOT a Boolean function, quadratic placement, or code.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

WEIGHTS=(0,64,96,112,120,128,136,144,160,192,256)


def base_module():
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('histogram_base',path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if not 1<=args.timeout_ms<=60000: raise ValueError('invalid timeout')
    if args.output.exists(): raise FileExistsError(args.output)
    base=base_module(); a={t:z3.Int(f'c_{t:+d}') for t in range(-7,8)}
    s=z3.Solver(); s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()])
    s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]); s.add(z3.Or(evenfirst==0,evenfirst==128))
    for j in range(15):
        s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    peakunit=a[-7]+a[-1]+a[1]+a[7]
    signquad=a[-5]+a[-1]+a[3]+a[7]
    xorsum=peakunit+signquad-2*(a[-1]+a[7])
    for value in (peakunit,signquad,xorsum): s.add(z3.Or(*[value==w for w in WEIGHTS]))
    started=time.monotonic(); status=s.check(); elapsed=time.monotonic()-started
    result={'status':str(status),'timeout_ms':args.timeout_ms,'elapsed_seconds':elapsed,
            'quadratic_weight_set':WEIGHTS,'scope':'formal histogram only; no quadratic placement or Boolean realization'}
    if status==z3.unknown: result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model(); v={t:m.eval(a[t]).as_long() for t in a}
        pp=v[-7]+v[-1]+v[1]+v[7]; qq=v[-5]+v[-1]+v[3]+v[7]
        rr=pp+qq-2*(v[-1]+v[7])
        assert all(x in WEIGHTS for x in (pp,qq,rr))
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128
        assert sum(t*t*v[t] for t in v)==16384 and sum(v[t] for t in v if t%2)==256
        assert v[-7]+v[7]>=92 and sum(t*v[t] for t in v if not t%2) in (0,128)
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(n%512==0 and n>=0 for n in nums)
        d=[n//512 for n in nums]; assert d[0]==1 and d[1]==d[2]==d[256]==0 and d[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'peakunit_weight':pp,'sign_weight':qq,'xor_weight':rr,
                       'dual_coefficients_decimal':[str(x) for x in d],'all_257_integral_and_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2,sort_keys=True); out.write('\n')
    print('status=',status,'solve_seconds=',round(elapsed,3),'weights=',[result.get(x) for x in ('peakunit_weight','sign_weight','xor_weight')],flush=True)


if __name__=='__main__': main()
