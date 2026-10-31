#!/usr/bin/env python3
"""Bounded exploratory Z3 border test at n1980; UNSAT is unreviewed."""
from itertools import combinations
from math import gcd
import json,sys,time
import z3
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def run(d,seconds):
    if n%d or not 0<seconds<=90:raise ValueError('unsupported')
    clock=time.monotonic();qs=n//d
    pc=[x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)]
    qc=[x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)]
    P={x:z3.Bool('p%d'%x) for x in pc};Q={x:z3.Bool('q%d'%x) for x in qc}
    side={g:z3.Bool('g%d'%g) for g in range(1,n) if n%g==0}
    s=z3.Solver();s.set(timeout=int(seconds*1000))
    s.add(*(P[x] for x in A),*(Q[y] for y in Y))
    s.add(z3.PbEq([(v,1) for v in P.values()],d),z3.PbEq([(v,1) for v in Q.values()],qs))
    s.add(*(side[g] for g in GA),*(z3.Not(side[g]) for g in GY))
    for x,y in combinations(pc,2):s.add(z3.Or(z3.Not(P[x]),z3.Not(P[y]),side[gcd(x-y,n)]))
    for x,y in combinations(qc,2):s.add(z3.Or(z3.Not(Q[x]),z3.Not(Q[y]),z3.Not(side[gcd(x-y,n)])))
    def counts(V,m):return [z3.Sum([z3.If(v,1,0) for x,v in V.items() if x%m==r]) for r in range(m)]
    for p,r in ((2,2),(3,2),(5,1),(11,1)):
        for k in range(1,r+1):
            m=p**k;unit=p**(k-1);cp=counts(P,m);cq=counts(Q,m)
            eq=lambda c:z3.And(*(c[a]==c[a+j*unit] for a in range(unit) for j in range(1,p)))
            s.add(z3.Or(eq(cp),eq(cq)))
    prep=time.monotonic()-clock;res=s.check();out={'n':n,'P_size':d,'Q_size':qs,
        'timeout':seconds,'prep_seconds':round(prep,3),'result':str(res),'z3':z3.get_version_string()}
    if res==z3.unknown:out['reason']=s.reason_unknown()
    if res==z3.sat:
        m=s.model();p=[x for x,v in P.items() if z3.is_true(m.eval(v,model_completion=True))]
        q=[x for x,v in Q.items() if z3.is_true(m.eval(v,model_completion=True))]
        sums=[(a+b)%n for a in p for b in q]
        if len(p)!=d or len(q)!=qs or not A<=set(p) or not Y<=set(q) or len(set(sums))!=n:
            raise AssertionError('invalid direct-sum witness')
        out.update({'P':p,'Q':q,'raw_sum_verified':True})
    out['elapsed_seconds']=round(time.monotonic()-clock,3);return out

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: script P_size timeout')
    print(json.dumps(run(int(sys.argv[1]),float(sys.argv[2])),indent=2))
