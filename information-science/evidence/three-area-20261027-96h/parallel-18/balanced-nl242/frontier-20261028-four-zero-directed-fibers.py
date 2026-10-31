#!/opt/homebrew/bin/python3
"""Formal count relaxation with all three radical autocorrelations enforced."""
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


def canonical(row):return min(tuple(row[i^shift] for i in range(4)) for shift in range(4))

def tuples_uniform(values):return sorted({canonical(row) for row in itertools.product(values,repeat=4)})

def tuples_split(A,B,bit):
    rows=set()
    for offset in (0,1):
        domains=[A if ((i&bit)!=0)^offset==0 else B for i in range(4)]
        for row in itertools.product(*domains):rows.add(canonical(row))
    return sorted(rows)


def add_group(s,tag,rows,vals,counts,trace):
    v=[z3.Int(tag+'_'+str(i)) for i in range(len(rows))];s.add(*[x>=0 for x in v]);trace[tag]=(rows,v)
    for t in vals:s.add(z3.Sum([row.count(t)*x for row,x in zip(rows,v)])==counts[t])
    corrs=[z3.Sum([sum(row[i]*row[i^d] for i in range(4) if i<(i^d))*x for row,x in zip(rows,v)]) for d in (1,2,3)]
    return z3.Sum(v),corrs


def main():
    p=argparse.ArgumentParser();p.add_argument('--lambda-mode',type=int,choices=(0,1),required=True)
    p.add_argument('--qrad-bit',type=int,choices=(0,1,2),required=True)
    p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000 or (not args.lambda_mode and args.qrad_bit==2):raise ValueError('invalid bounds/mode')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'df_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    ef=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(ef==0,ef==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];m=a[-2]+a[6]
    s.add(z3.Or(*[z3.And(z==key,z3.Or(*[m==v for v in allowed])) for key,allowed in ALLOWED.items()]))
    s.add(z3.Or(w==112,w==144) if args.qrad_bit==0 else w==128)
    s.add(P%4==0,P<=224,P!=220)
    s.add(z3.Implies(P==224,z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(P==216,z3.If(w==128,c==20,c%8==4)))
    s.add(z3.Implies(z3.And(P==212,w==112),c>=16))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    trace={};C=[]
    n0,c0=add_group(s,'zero',tuples_uniform((-4,4)),(-4,4),a,trace);s.add(4*n0==z-4);C.append(c0)
    if not args.lambda_mode:
        n1,c1=add_group(s,'g1',tuples_uniform((-6,2)),(-6,2),a,trace)
        n3,c3=add_group(s,'g3',tuples_uniform((-2,6)),(-2,6),a,trace)
        s.add(4*(n1+n3)==256-z);C += [c1,c3]
    else:
        ne,ce=add_group(s,'evenmixed',tuples_split((-6,2),(-2,6),1),(-6,2,-2,6),a,trace)
        s.add(4*ne==256-z,2*m==256-z);C.append(ce)
    Q0=(-7,-3,1,5);Q1=(-5,-1,3,7)
    if args.qrad_bit==0:
        nA,cA=add_group(s,'odd0',tuples_uniform(Q0),Q0,a,trace)
        nB,cB=add_group(s,'odd1',tuples_uniform(Q1),Q1,a,trace)
        s.add(nA+nB==64,4*nB==w);C += [cA,cB]
    else:
        no,co=add_group(s,'oddmixed',tuples_split(Q0,Q1,args.qrad_bit),Q0+Q1,a,trace)
        s.add(no==64);C.append(co)
    for i in range(3):s.add(z3.Sum([group[i] for group in C])==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
       'lambda_mode':args.lambda_mode,'qrad_bit':args.qrad_bit,'tuple_types':{tag:len(rows) for tag,(rows,_) in trace.items()},
       'scope':'formal tuple multiset; no common frequency placement or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m0=s.model();v={t:m0.eval(a[t]).as_long() for t in a};nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums);dual=[x//512 for x in nums]
        assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result['fiber_groups']={tag:[{'tuple':list(row),'fibers':m0.eval(var).as_long()}
            for row,var in zip(rows,variables) if m0.eval(var).as_long()!=0] for tag,(rows,variables) in trace.items()}
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':4+v[-4]+v[4],
          'odd_Q_weight':v[-5]+v[-1]+v[3]+v[7],'even_g3_count':v[-2]+v[6],
          'peakunit_weight':v[-7]+v[-1]+v[1]+v[7],'peak_count':v[-7]+v[7],
          'directed_autocorrelations':[m0.eval(z3.Sum([group[i] for group in C])).as_long() for i in range(3)],
          'dual_coefficients_decimal':[str(x) for x in dual]})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('lambda=',args.lambda_mode,'qradbit=',args.qrad_bit,'status=',status,'seconds=',round(result['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
