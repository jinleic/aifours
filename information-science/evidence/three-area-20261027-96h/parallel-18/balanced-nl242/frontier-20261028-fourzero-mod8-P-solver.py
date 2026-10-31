#!/opt/homebrew/bin/python3
"""Bounded exact search for odd P in one fixed even mod8 extension coset."""
import argparse
import functools
import itertools
import json
import pathlib
import time
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('bad bounds/output')
    k=json.loads(args.input.read_text(encoding='utf-8'))['spectrum_k']
    terms=[sum(1<<i for i in I) for d in range(3) for I in itertools.combinations(range(8),d)];assert len(terms)==37
    bits=[z3.Bool('p'+str(i)) for i in range(37)];P=[];Q=[]
    for x in range(256):
        v=functools.reduce(z3.Xor,[bits[i] for i,t in enumerate(terms) if x&t==t])
        P.append(z3.Not(v) if (k[x]//2)%4 in (0,3) else v)
        Q.append((k[x]//2)%2)
    assert sum(Q)==144
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(z3.PbEq([(v,1) for v in P],160),z3.PbEq([(P[x],1) for x in range(256) if Q[x]],86))
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
       'scope':'one fixed even-mod8 polynomial extension; no Boolean realization'}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        m=s.model();coef=sum(int(z3.is_true(m.eval(v,model_completion=True)))<<i for i,v in enumerate(bits))
        truth=[]
        for x in range(256):
            shift=sum((coef>>i)&1 for i,t in enumerate(terms) if x&t==t)%2
            truth.append(int((k[x]//2)%4 in (0,3))^shift)
        assert sum(truth)==160 and sum(truth[x] for x in range(256) if Q[x])==86
        result.update({'quadratic_shift_coefficients_hex':format(coef,'x'),
                       'P_bits_le_hex':format(sum(v<<x for x,v in enumerate(truth)),'064x'),
                       'P_weight':160,'P_Q1_intersection':86,'actual_boolean_witness':False})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('status=',status,'seconds=',round(result['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
