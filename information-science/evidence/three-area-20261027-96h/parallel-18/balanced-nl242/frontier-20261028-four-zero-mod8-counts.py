#!/opt/homebrew/bin/python3
"""Formal rank-six four-zero counts with the exact mod8 residue census."""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

ALLOWED={144:(28,52,56,60,84),112:(36,44,52,60,68,72,76,84,92,100,108)}
PHASE=((112,12),(112,28),(128,16),(144,4),(144,20))


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'i_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    evenfirst=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(evenfirst==0,evenfirst==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];n3=a[-2]+a[6]
    s.add(z3.Or(*[z3.And(z==k,z3.Or(*[n3==v for v in vals])) for k,vals in ALLOWED.items()]))
    s.add(z3.Or(w==112,w==128,w==144),P%4==0,P<=224,P!=220)
    s.add(z3.Implies(P==224,z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(P==216,z3.If(w==128,c==20,c%8==4)))
    s.add(z3.Implies(z3.And(P==212,w==112),c>=16))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
         'scope':'formal counts only; no spatial, code or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model();v={t:m.eval(a[t]).as_long() for t in a};Z=4+v[-4]+v[4];W=v[-5]+v[-1]+v[3]+v[7]
        Pn=v[-7]+v[-1]+v[1]+v[7];C=v[-5]+v[3];n=v[-2]+v[6]
        assert Z in ALLOWED and n in ALLOWED[Z] and W in (112,128,144) and Pn%4==0 and Pn<=224 and Pn!=220
        if Pn==224:assert (W,C) in PHASE
        if Pn==216:assert C==20 if W==128 else C%8==4
        if Pn==212 and W==112:assert C>=16
        assert v[0]==3 and sum(v.values())==511 and sum(t*v[t] for t in v)==128 and sum(t*t*v[t] for t in v)==16384
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums)
        dual=[x//512 for x in nums];assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':Z,'odd_Q_weight':W,
          'peakunit_weight':Pn,'nonpeak_Q_intersection':C,'even_g3_count':n,'peak_count':v[-7]+v[7],
          'dual_coefficients_decimal':[str(x) for x in dual],'all_257_integral_nonnegative':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'z=',result.get('q_zero_count'),'g3=',result.get('even_g3_count'),flush=True)


if __name__=='__main__':main()
