#!/opt/homebrew/bin/python3
"""Necessary four-zero R-fiber count/energy relaxation; no Boolean realization."""
import argparse
import importlib.util
import itertools
import json
import math
import pathlib
import time
import z3

ALLOWED={144:(28,52,56,60,84),112:(36,44,52,60,68,72,76,84,92,100,108)}
PHASE=((112,12),(112,28),(128,16),(144,4),(144,20))


def compositions(n,k):
    if k==1:
        yield (n,);return
    for i in range(n+1):
        for rest in compositions(n-i,k-1):yield (i,)+rest


def add_group(s,tag,values,allowed_comps,counts,trace):
    variables=[z3.Int(tag+'_'+str(i)) for i in range(len(allowed_comps))]
    trace[tag]=(values,allowed_comps,variables)
    s.add(*[v>=0 for v in variables])
    for j,t in enumerate(values):
        s.add(z3.Sum([comp[j]*v for comp,v in zip(allowed_comps,variables)])==counts[t])
    energy=z3.Sum([(sum(c*t for c,t in zip(comp,values))**2)*v for comp,v in zip(allowed_comps,variables)])
    return z3.Sum(variables),energy


def main():
    p=argparse.ArgumentParser();p.add_argument('--lambda-mode',type=int,choices=(0,1),required=True)
    p.add_argument('--qrad-mode',type=int,choices=(0,1),required=True)
    p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'k_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    ef=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(ef==0,ef==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];m=a[-2]+a[6]
    s.add(z3.Or(*[z3.And(z==key,z3.Or(*[m==v for v in vals])) for key,vals in ALLOWED.items()]))
    s.add(z3.Or(w==112,w==144) if args.qrad_mode==0 else w==128)
    s.add(P%4==0,P<=224,P!=220)
    s.add(z3.Implies(P==224,z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(P==216,z3.If(w==128,c==20,c%8==4)))
    s.add(z3.Implies(z3.And(P==212,w==112),c>=16))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    counts=a;trace={}
    n0,E0=add_group(s,'even_zero',(-4,4),list(compositions(4,2)),counts,trace);s.add(4*n0==z-4)
    energies=[E0]
    if args.lambda_mode==0:
        n1,E1=add_group(s,'even_g1',(-6,2),list(compositions(4,2)),counts,trace)
        n3,E3=add_group(s,'even_g3',(-2,6),list(compositions(4,2)),counts,trace)
        s.add(4*(n1+n3)==256-z);energies += [E1,E3]
    else:
        mixed=[u+v for u in compositions(2,2) for v in compositions(2,2)]
        n1,E1=add_group(s,'even_mixed',(-6,2,-2,6),mixed,counts,trace)
        s.add(4*n1==256-z,m==(256-z)/2);energies.append(E1)
    q0=(-7,-3,1,5);q1=(-5,-1,3,7)
    if args.qrad_mode==0:
        nA,EA=add_group(s,'odd_Q0',q0,list(compositions(4,4)),counts,trace)
        nB,EB=add_group(s,'odd_Q1',q1,list(compositions(4,4)),counts,trace)
        s.add(nA+nB==64,4*nB==w);energies += [EA,EB]
    else:
        mixed=[u+v for u in compositions(2,4) for v in compositions(2,4)]
        nA,EA=add_group(s,'odd_mixed',q0+q1,mixed,counts,trace)
        s.add(nA==64);energies.append(EA)
    # Sum_{r in R} R(r) = sum_fibers (sum k)^2 = R(0) = 2^14.
    s.add(z3.Sum(energies)==16384)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'lambda_mode':args.lambda_mode,'qrad_mode':args.qrad_mode,
        'scope':'formal histogram plus aggregate R-fiber energy; not spatial/Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m0=s.model();v={t:m0.eval(a[t]).as_long() for t in a};nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums);dual=[x//512 for x in nums]
        assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result['fiber_groups']={tag:{'values':list(values),'compositions':[
            {'counts':list(comp),'fibers':m0.eval(var).as_long()}
            for comp,var in zip(comps,variables) if m0.eval(var).as_long()!=0]}
            for tag,(values,comps,variables) in trace.items()}
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':4+v[-4]+v[4],
                       'odd_Q_weight':v[-5]+v[-1]+v[3]+v[7],'even_g3_count':v[-2]+v[6],
                       'peakunit_weight':v[-7]+v[-1]+v[1]+v[7],'peak_count':v[-7]+v[7],
                       'aggregate_fiber_energy':m0.eval(z3.Sum(energies)).as_long(),
                       'dual_coefficients_decimal':[str(x) for x in dual]})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('lambda=',args.lambda_mode,'qrad=',args.qrad_mode,'status=',status,'seconds=',round(result['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
