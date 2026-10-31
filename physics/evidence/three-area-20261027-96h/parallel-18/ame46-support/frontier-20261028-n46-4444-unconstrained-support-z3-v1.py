#!/usr/bin/env python3
"""Uncertified SMT E-support search for the 4444 N=46 residual, no P forbidden pairs."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));IJ=list(itertools.product(range(4),repeat=2))


def cell(E,A,r,B,c):
    x=[0]*4
    for i,v in zip(A,r):x[i]=v
    for i,v in zip(B,c):x[i]=v
    return E[tuple(x)]


def solve(kind,timeout):
    target=[[4,4,6,6] for _ in range(4)]
    if kind=='one_degree4':target[0]=[4,4,4,8]
    E={q:z3.Bool('x'+''.join(map(str,q))) for q in Q};s=z3.Solver();s.set(timeout=timeout)
    for i in range(4):
      for x in range(4):s.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==x],target[i][x]))
    for i,j in PAIRS:
      for a,b in IJ:
        v=[(w,1) for q,w in E.items() if q[i]==a and q[j]==b]
        s.add(z3.Or(z3.PbEq(v,0),z3.PbEq(v,2)))
    for A in CUTS:
      B=tuple(i for i in range(4) if i not in A);G={(r,c):cell(E,A,r,B,c) for r in IJ for c in IJ}
      for r in IJ:
       for c,d in itertools.combinations(IJ,2):
        s.add(z3.Implies(z3.And(G[r,c],G[r,d]),z3.Or(*[z3.And(G[t,c],G[t,d]) for t in IJ if t!=r])))
    a=s.check();R={'degree_profile':kind,'status':str(a)}
    if a==z3.sat:
        m=s.model();S=sorted(q for q,v in E.items() if z3.is_true(m.eval(v,model_completion=True)));verify(S,target);R['E_support']=S;R['integer_support_check']='PASS'
    elif a==z3.unknown:R['reason_unknown']=s.reason_unknown()
    return R


def verify(S,T):
    if len(S)!=20:raise ValueError('wrong support')
    for i in range(4):
        if [sum(q[i]==x for q in S) for x in range(4)]!=T[i]:raise ValueError('bad fiber')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in S)
        if len(C)!=10 or set(C.values())!={2}:raise ValueError('bad pair multiplicities')
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in S:rows[tuple(q[i] for i in A)].add(tuple(q[i] for i in B));cols[tuple(q[i] for i in B)].add(tuple(q[i] for i in A))
        if any(len(x&y)==1 for D in (rows,cols) for x,y in itertools.combinations(D.values(),2)):raise ValueError('unique intersection')


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=45000);a=p.parse_args()
    cases=[solve(k,a.timeout_ms) for k in ('no_degree4','one_degree4')]
    res={'cases':cases,'scope':'Necessary E support only; SAT has no coefficients/P completion, UNSAT has no independently checked proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(res,f,indent=2);f.write('\n')
    print(json.dumps({'cases':[{k:v for k,v in r.items() if k!='E_support'} for r in cases],'scope':res['scope']},indent=2))


if __name__=='__main__':main()
