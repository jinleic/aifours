#!/opt/homebrew/bin/python3
"""Linear count relaxation with radical-invariant-residue pairing lower bound."""
import argparse
import importlib.util
import json
import math
import pathlib
import time
import z3

ALLOWED={144:(28,52,60,84),112:(36,44,52,60,68,76,84,92,100,108)}
PHASE=((112,12),(112,28),(128,16),(144,4),(144,20))


def group(s,tag,values,counts):
    pairs={(i,j):z3.Int(tag+'_'+str(i)+'_'+str(j)) for i in range(len(values)) for j in range(i,len(values))}
    s.add(*[v>=0 for v in pairs.values()])
    for i in range(len(values)):
        s.add(2*pairs[i,i]+z3.Sum([p for (j,k),p in pairs.items() if j!=k and (j==i or k==i)])==counts[i])
    return z3.Sum([values[i]*values[j]*p for (i,j),p in pairs.items()])


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec=importlib.util.spec_from_file_location('base',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    a={t:z3.Int(f'j_{t:+d}') for t in range(-7,8)};s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=511) for v in a.values()]);s.add(a[0]==3,z3.Sum(list(a.values()))==511)
    s.add(z3.Sum([t*a[t] for t in a])==128,z3.Sum([t*t*a[t] for t in a])==16384)
    s.add(z3.Sum([a[t] for t in a if t%2])==256,a[-7]+a[7]>=92,a[-7]+a[7]<=234)
    ef=z3.Sum([t*a[t] for t in a if not t%2]);s.add(z3.Or(ef==0,ef==128))
    z=4+a[-4]+a[4];w=a[-5]+a[-1]+a[3]+a[7];P=a[-7]+a[-1]+a[1]+a[7];c=a[-5]+a[3];m=a[-2]+a[6]
    s.add(z3.Or(*[z3.And(z==k,z3.Or(*[m==x for x in vals])) for k,vals in ALLOWED.items()]))
    s.add(z3.Or(w==112,w==128,w==144),P%4==0,P<=224,P!=220)
    s.add(z3.Implies(P==224,z3.Or(*[z3.And(w==x,c==y) for x,y in PHASE])))
    s.add(z3.Implies(P==216,z3.If(w==128,c==20,c%8==4)))
    s.add(z3.Implies(z3.And(P==212,w==112),c>=16))
    # If m is noncentral, lambda=0. A nonzero r in ker(Q|R) preserves
    # qzero, each q-one mod-8 residue, and each odd Q class.
    costs=[group(s,'qzero',(-4,4),(a[-4],a[4])),
           group(s,'g1',(-6,2),(a[-6],a[2])),group(s,'g3',(-2,6),(a[-2],a[6])),
           group(s,'Q0',(-7,-3,1,5),(a[-7],a[-3],a[1],a[5])),
           group(s,'Q1',(-5,-1,3,7),(a[-5],a[-1],a[3],a[7]))]
    s.add(z3.Sum(costs)<=0)
    for j in range(15):s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a])+base.h_coeff(j))%512==0)
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'scope':'formal counts plus existential coarse invariant pairings; no actual placement or Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();v={t:model.eval(a[t]).as_long() for t in a};Z=4+v[-4]+v[4];W=v[-5]+v[-1]+v[3]+v[7];M=v[-2]+v[6]
        assert Z in ALLOWED and M in ALLOWED[Z] and W in (112,128,144)
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(x>=0 and x%512==0 for x in nums);dual=[x//512 for x in nums]
        assert dual[0]==1 and dual[1]==dual[2]==dual[256]==0 and dual[255] in (0,1)
        result.update({'histogram':{str(t):v[t] for t in v},'q_zero_count':Z,'odd_Q_weight':W,
                       'even_g3_count':M,'peakunit_weight':v[-7]+v[-1]+v[1]+v[7],
                       'nonpeak_Q_intersection':v[-5]+v[3],'peak_count':v[-7]+v[7],
                       'chosen_pair_product_sum':model.eval(z3.Sum(costs)).as_long(),
                       'dual_coefficients_decimal':[str(x) for x in dual]})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),'z=',result.get('q_zero_count'),'m=',result.get('even_g3_count'),flush=True)


if __name__=='__main__':main()
