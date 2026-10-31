#!/opt/homebrew/bin/python3
"""Bounded exact search for one small odd-complement support with forced quartic.

A SAT result is only a Boolean P placement, not an NL242 witness.
"""
import argparse
import functools
import json
import pathlib
import time
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('bad bounds/output')
    # rank-6 even-half q=x0*x1+x2*x3+x4*x5; Q=q+1 has 144 ones.
    def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2
    quartic=[15,51,60]  # x0x1x2x3, x0x1x4x5, x2x3x4x5
    terms=[m for m in range(256) if m.bit_count()<=3]
    c={m:z3.Bool('c_'+str(m)) for m in terms}
    pbits=[]
    for x in range(256):
        selected=[c[m] for m in terms if x&m==m]
        parity=functools.reduce(z3.Xor,selected)
        const=sum(x&m==m for m in quartic)%2
        pbits.append(z3.Not(parity) if const else parity)
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    # P has weight 224; its complement has 16 points in each Q class.
    missing=[z3.Not(v) for v in pbits]
    s.add(z3.PbEq([(v,1) for v in missing],32))
    s.add(z3.PbEq([(missing[x],1) for x in range(256) if q(x)==0],16))
    started=time.monotonic();status=s.check()
    result={'status':str(status),'solve_seconds':time.monotonic()-started,'timeout_ms':args.timeout_ms,
            'scope':'fixed rank-6 q/Q, quartic part and histogram weights only; no Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();coef={m:z3.is_true(model.eval(v,model_completion=True)) for m,v in c.items()}
        P=[]
        for x in range(256):
            value=sum(coef[m] for m in terms if x&m==m)%2 ^ sum(x&m==m for m in quartic)%2
            P.append(value)
        assert sum(P)==224 and sum(not P[x] for x in range(256) if q(x)==0)==16
        result.update({'P_truth_bits':''.join(map(str,P)),'lower_anf_terms':[m for m in terms if coef[m]],
                       'quartic_anf_terms':quartic,'degree':4,'boolean_target_witness':False})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
