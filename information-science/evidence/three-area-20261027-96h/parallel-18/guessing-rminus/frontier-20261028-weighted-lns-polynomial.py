#!/usr/bin/env python3
"""Bounded exact-weight local-neighborhood search for a q=2 polynomial witness.

For each fixed integer weight vector, Z3 searches replacements in a subset
of a valid support. Every SAT proposal is independently checked for graph FDs
and the strict integer polynomial. Failures are only local solver results.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from random import Random
from time import monotonic
import json
from z3 import Bool,Not,Or,PbGe,Solver,is_true,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
EXPECTED='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUTPUT=ROOT/'frontier-20261028-weighted-lns-polynomial-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
MAX_SECONDS=28;MAX_CASES=8;TRIALS_PER_CASE=5;SOLVER_MS=1000;POOL_MAX=220


def main():
    started=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    seed=set(json.loads(raw)['support_words_one_based_bitsets'])
    masks={v:sum(1<<(u-1) for u in ns) for v,ns in N.items()}
    bad={d for d in range(1,1024) if any(d&(1<<(v-1)) and not(d&m) for v,m in masks.items())}
    if len(bad)!=113:raise ValueError('BAD_GRAPH')
    conflict=[sum(1<<(x^d) for d in bad) for x in range(1024)];universe=(1<<1024)-1
    def valid(W):return all((a^b) not in bad for a,b in combinations(sorted(W),2))
    if len(seed)!=88 or not valid(seed):raise ValueError('SEED_FD')
    rng=Random(2026102812);records=[];witness=None
    for case in range(MAX_CASES):
        if monotonic()-started>=MAX_SECONDS:break
        skew=set(rng.sample(range(10),4));t=[[1,1] if v not in skew else ([2,3] if rng.randrange(2) else [3,2]) for v in range(10)]
        weights=[];D=1
        for a,b in t:D*=(a**3+b**3)**2
        for w in range(1024):
            x=1
            for v in range(10):x*=t[v][(w>>v)&1]**2
            weights.append(x)
        current=set(seed);initial=sum(weights[w] for w in current)
        caseinfo={'weights_t':t,'initial_weight_sum':str(initial),'trials':[]}
        for trial in range(TRIALS_PER_CASE):
            if monotonic()-started>=MAX_SECONDS:break
            count=min(len(current),(16,20,24,28,32)[trial]);removed=set(rng.sample(sorted(current),count));keep=current-removed
            blocked=0
            for w in keep:blocked|=conflict[w]|(1<<w)
            avail=universe&~blocked;pool=[w for w in range(1024) if avail>>w&1]
            if not removed<=set(pool):raise ValueError('POOL')
            if len(pool)>POOL_MAX:
                caseinfo['trials'].append({'removed':count,'pool':len(pool),'status':'SKIPPED_POOL_LIMIT'});continue
            x=[Bool(f'x_{case}_{trial}_{i}') for i in range(len(pool))];solver=Solver();solver.set(timeout=SOLVER_MS)
            for i,j in combinations(range(len(pool)),2):
                if (pool[i]^pool[j]) in bad:solver.add(Or(Not(x[i]),Not(x[j])))
            target=sum(weights[w] for w in removed)+1
            solver.add(PbGe([(x[i],weights[w]) for i,w in enumerate(pool)],target));status=solver.check()
            row={'removed':count,'pool':len(pool),'status':str(status),'before_weight':str(sum(weights[w] for w in current))}
            if status==sat:
                model=solver.model();chosen={pool[i] for i,xv in enumerate(x) if is_true(model.eval(xv,model_completion=True))};current=keep|chosen
                if not valid(current):raise ValueError('SAT_FD')
                S=sum(weights[w] for w in current)
                if S<=int(row['before_weight']):raise ValueError('SAT_NOT_IMPROVED')
                row.update({'after_size':len(current),'after_weight':str(S),'strict_integer_witness':S**3>D})
                if S**3>D:witness={'words':sorted(current),'weights_t':t,'S':str(S),'D':str(D)}
            caseinfo['trials'].append(row)
            if witness:break
        caseinfo['final_weight_sum']=str(sum(weights[w] for w in current));caseinfo['final_support_size']=len(current);records.append(caseinfo)
        if witness:break
    out={'input_support_sha256':EXPECTED,'seed':2026102812,'forbidden_differences':len(bad),
         'solver_ms':SOLVER_MS,'pool_limit':POOL_MAX,'cases':records,'strict_integer_witness':witness,
         'elapsed_seconds':monotonic()-started,
         'limits':'Bounded q2 fixed-weight local neighborhoods only. Solver UNKNOWN/UNSAT is not a global bound; a positive witness requires independent proof and balancing/type-class construction.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_integer_witness'},indent=2))
    if witness:print('STRICT INTEGER WITNESS: independent verification required')


if __name__=='__main__':main()
