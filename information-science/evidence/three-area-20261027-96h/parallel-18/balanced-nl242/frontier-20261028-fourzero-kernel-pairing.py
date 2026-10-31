#!/opt/homebrew/bin/python3
"""Formal four-zero count relaxation with an affine kernel-direction P derivative."""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

PHASE=((112,12),(112,28),(128,16),(144,4),(144,20))


def group(s,tag,values,counts,flags=None):
    v={(i,j):z3.Int(tag+'_'+str(i)+'_'+str(j)) for i in range(len(values)) for j in range(i,len(values))}
    s.add(*[x>=0 for x in v.values()])
    for i in range(len(values)):
        s.add(2*v[i,i]+z3.Sum([x for (j,k),x in v.items() if j!=k and (j==i or k==i)])==counts[i])
    C=z3.Sum([values[i]*values[j]*x for (i,j),x in v.items()])
    X=z3.Sum([x for (i,j),x in v.items() if flags and flags[i]!=flags[j]]) if flags else z3.IntVal(0)
    return C,X,v


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'p_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    ef=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(ef==0,ef==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];m=a[-2]+a[6]
    s.add(z3.Or(z==112,z==144),z3.Or(w==112,w==144),2*m==256-z,P%4==0,P<=224,P!=220)
    s.add(z3.Implies(P==224,z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(P==216,c%8==4),z3.Implies(z3.And(P==212,w==112),c>=16))
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    specs=[('zero',(-4,4),(a[-4],a[4]),None),('g1',(-6,2),(a[-6],a[2]),None),
           ('g3',(-2,6),(a[-2],a[6]),None),('Q0',(-7,-3,1,5),(a[-7],a[-3],a[1],a[5]),(1,0,1,0)),
           ('Q1',(-5,-1,3,7),(a[-5],a[-1],a[3],a[7]),(0,1,0,1))]
    C=[];X=[];trace={}
    for tag,values,counts,flags in specs:
        cc,xx,variables=group(s,tag,values,counts,flags);C.append(cc);X.append(xx);trace[tag]=(values,variables)
    s.add(z3.Sum(C)==0)
    crossing=z3.Sum(X);s.add(z3.Or(crossing==0,crossing==64,z3.And(P==128,crossing==128)))
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'scope':'formal signed counts and one kernel-direction pairing; no common placement or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();v={t:model.eval(a[t]).as_long() for t in a};nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums);dual=[x//512 for x in nums]
        assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':4+v[-4]+v[4],
                       'odd_Q_weight':v[-5]+v[-1]+v[3]+v[7],'even_g3_count':v[-2]+v[6],
                       'peakunit_weight':v[-7]+v[-1]+v[1]+v[7],'peak_count':v[-7]+v[7],
                       'kernel_P_crossing_pairs':model.eval(crossing).as_long(),
                       'kernel_pair_correlation':model.eval(z3.Sum(C)).as_long(),
                       'pairings':{tag:[{'values':[values[i],values[j]],'pairs':model.eval(var).as_long()}
                              for (i,j),var in variables.items() if model.eval(var).as_long()!=0]
                              for tag,(values,variables) in trace.items()},
                       'dual_coefficients_decimal':[str(x) for x in dual]})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'crossing=',result.get('kernel_P_crossing_pairs'),flush=True)


if __name__=='__main__':main()
