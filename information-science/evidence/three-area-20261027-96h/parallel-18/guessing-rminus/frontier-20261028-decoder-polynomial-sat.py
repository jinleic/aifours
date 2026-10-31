#!/usr/bin/env python3
"""Bounded exact-PB search for q=2 polynomial witnesses with decoder variables.

For each fixed integer weight vector, one Boolean decoder output per vertex
and neighbour pattern enforces all-domain graph consistency. SAT proposals
are verified by integer arithmetic and still need an independent replay.
UNSAT/unknown statuses concern only the listed fixed weights.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from random import Random
from time import monotonic
import json
from z3 import Bool,Implies,Not,PbGe,Solver,is_true,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
EXPECTED='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUTPUT=ROOT/'frontier-20261028-decoder-polynomial-sat-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
CASE_MS=2500;MAX_CASES=8;MAX_SECONDS=30


def icbrt(n):
    a,b=0,1<<((n.bit_length()+2)//3)
    while a<b:
        m=(a+b+1)//2
        if m*m*m<=n:a=m
        else:b=m-1
    return a


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    rng=Random(2026102806);cases=[];candidate=None
    for case in range(MAX_CASES):
        if monotonic()-start>=MAX_SECONDS:break
        skew=set(rng.sample(range(10),4))
        t=[[1,1] if v not in skew else ([1,2] if rng.randrange(2) else [2,1]) for v in range(10)]
        D=1
        for a,b in t:D*=(a**3+b**3)**2
        threshold=icbrt(D)+1
        weights=[]
        for w in range(1024):
            n=1
            for v in range(10):n*=t[v][(w>>v)&1]**2
            weights.append(n)
        x=[Bool(f'w_{case}_{w}') for w in range(1024)]
        dec={(v,p):Bool(f'd_{case}_{v}_{p}') for v,ns in N.items() for p in range(1<<len(ns))}
        solver=Solver();solver.set(timeout=CASE_MS)
        for w in range(1024):
            for v,ns in N.items():
                pattern=sum(((w>>(u-1))&1)<<j for j,u in enumerate(ns));b=dec[v,pattern]
                solver.add(Implies(x[w],b if (w>>(v-1))&1 else Not(b)))
        solver.add(PbGe([(x[w],weights[w]) for w in range(1024)],threshold))
        status=solver.check();entry={'integer_weights_t':t,'target_sum_threshold':threshold,
                                    'solver_status':str(status)}
        if status==sat:
            model=solver.model();W=[w for w in range(1024) if is_true(model.eval(x[w],model_completion=True))]
            for u,v in combinations(W,2):
                d=u^v
                if any(d&(1<<(a-1)) and all(not d&(1<<(b-1)) for b in ns) for a,ns in N.items()):
                    raise ValueError('SOLVER_FD_CONFLICT')
            S=sum(weights[w] for w in W)
            if S**3<=D:raise ValueError('SOLVER_POLYNOMIAL_FAILURE')
            candidate={'support':W,'integer_weights_t':t,'S':str(S),'D':str(D),'strict_S_cubed_gt_D':True}
            entry['candidate_support_size']=len(W)
        cases.append(entry)
        if candidate:break
    out={'input_sha256':EXPECTED,'seed':2026102806,'max_solver_milliseconds':CASE_MS,
         'cases':cases,'strict_integer_candidate':candidate,'elapsed_seconds':monotonic()-start,
         'limits':'Fixed sampled q=2 weight vectors only. Unknown means no conclusion. UNSAT is an unverified solver status. SAT requires independent original-graph and finite-law verification.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_integer_candidate'},indent=2))
    if candidate:print('STRICT INTEGER CANDIDATE: independent verification required')


if __name__=='__main__':main()
