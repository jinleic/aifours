#!/usr/bin/env python3
"""Bounded exact Z3 search for actual cyclic border factorizations at n=1320.

Sands gcd-class conditions plus cardinalities are equivalent to tiling. SAT
witnesses are checked by raw sums; UNSAT is an unreviewed solver result, not a
certificate. UNKNOWN is never treated as UNSAT. No assertion about codes.
"""
import json,sys,time
from itertools import combinations
from math import gcd
import z3

n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(x-y,n) for x,y in combinations(A,2)}
GY={gcd(x-y,n) for x,y in combinations(Y,2)}

def val(v,p):
    z=0
    while v%p==0:z+=1;v//=p
    return z

def run(d,seconds):
    if n%d or d<1 or not 0<seconds<=90:raise ValueError('unsupported')
    started=time.monotonic();qsize=n//d
    pc=[x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)]
    qc=[x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)]
    P={i:z3.Bool('p%d'%i) for i in pc};Q={i:z3.Bool('q%d'%i) for i in qc}
    divs=[j for j in range(1,n) if n%j==0];side={j:z3.Bool('d%d'%j) for j in divs}
    solver=z3.Solver();solver.set(timeout=int(seconds*1000));solver.add(*(P[x] for x in A),*(Q[y] for y in Y))
    solver.add(z3.PbEq([(v,1) for v in P.values()],d),z3.PbEq([(v,1) for v in Q.values()],qsize))
    solver.add(*(side[g] for g in GA),*(z3.Not(side[g]) for g in GY))
    for x,y in combinations(pc,2):
        g=gcd(x-y,n);solver.add(z3.Or(z3.Not(P[x]),z3.Not(P[y]),side[g]))
    for x,y in combinations(qc,2):
        g=gcd(x-y,n);solver.add(z3.Or(z3.Not(Q[x]),z3.Not(Q[y]),z3.Not(side[g])))
    def class_counts(V,mod):
        return [z3.Sum([z3.If(v,1,0) for x,v in V.items() if x%mod==r]) for r in range(mod)]
    for p in (3,5,11):
        T=P if d%p==0 else Q;count=d if T is P else qsize
        cs=class_counts(T,p);solver.add(*(c==count//p for c in cs))
    # Each power of 2 cyclotomic polynomial divides at least one side.
    for k in (1,2,3):
        mod=2**k;half=mod//2;cp=class_counts(P,mod);cq=class_counts(Q,mod)
        solver.add(z3.Or(z3.And(*(cp[r]==cp[r+half] for r in range(half))),
                         z3.And(*(cq[r]==cq[r+half] for r in range(half)))))
    prep=time.monotonic()-started;answer=solver.check()
    out={'n':n,'P_size':d,'Q_size':qsize,'timeout_seconds':seconds,'prepare_seconds':round(prep,3),
         'z3_version':z3.get_version_string(),'result':str(answer)}
    if answer==z3.unknown:out['reason']=solver.reason_unknown()
    elif answer==z3.sat:
        model=solver.model();pp=[x for x,v in P.items() if z3.is_true(model.eval(v,model_completion=True))]
        qq=[x for x,v in Q.items() if z3.is_true(model.eval(v,model_completion=True))]
        sums=[(x+y)%n for x in pp for y in qq]
        if len(pp)!=d or len(qq)!=qsize or not A<=set(pp) or not Y<=set(qq) or len(set(sums))!=n:
            raise AssertionError('INVALID raw-sum witness')
        out['P']=pp;out['Q']=qq;out['raw_sums_verified']=True
    out['elapsed_seconds']=round(time.monotonic()-started,3)
    return out

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: solver.py P_size timeout_seconds')
    print(json.dumps(run(int(sys.argv[1]),float(sys.argv[2])),indent=2))
