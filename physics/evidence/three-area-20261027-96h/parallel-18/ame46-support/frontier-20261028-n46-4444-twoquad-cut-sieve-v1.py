#!/usr/bin/env python3
"""Diagnose which no-unique-overlap cuts matter in the two-quad SMT case.

This is a solver exploration, not an UNSAT certificate or complex proof.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));P=list(itertools.product(range(4),repeat=2))


def get(E,A,r,B,c):
    q=[0,0,0,0]
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def create(mask,timeout):
    E={q:z3.Bool('p'+''.join(map(str,q))) for q in Q};z=z3.Solver();z.set(timeout=timeout)
    for i in range(4):
      for x in range(4):z.add(z3.PbEq([(E[q],1) for q in Q if q[i]==x],4 if x<2 else 6))
    for i,j in PAIRS:
      for a,b in P:
        terms=[E[q] for q in Q if q[i]==a and q[j]==b]
        if (a,b) in ((0,0),(1,1)):z.add(z3.Not(z3.Or(*terms)))
        else:z.add(z3.Or(z3.PbEq([(x,1) for x in terms],0),z3.PbEq([(x,1) for x in terms],2)))
    for k,A in enumerate(CUTS):
      if not(mask>>k&1):continue
      B=tuple(i for i in range(4) if i not in A);grid={(r,c):get(E,A,r,B,c) for r in P for c in P}
      for r in P:
       for c,d in itertools.combinations(P,2):
        z.add(z3.Implies(z3.And(grid[r,c],grid[r,d]),z3.Or(*[z3.And(grid[s,c],grid[s,d]) for s in P if s!=r])))
    return z,E


def verify(S,mask):
    if len(S)!=20:raise ValueError('model size')
    for i in range(4):
        if [sum(q[i]==x for q in S) for x in range(4)]!=[4,4,6,6]:raise ValueError('fiber counts')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in S)
        if len(C)!=10 or set(C.values())!={2} or (0,0) in C or (1,1) in C:raise ValueError('pair requirements')
    actual=[]
    for k,A in enumerate(CUTS):
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in S:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        overlap=any(len(x&y)==1 for D in (rows,cols) for x,y in itertools.combinations(D.values(),2));actual.append(overlap)
        if mask>>k&1 and overlap:raise ValueError('selected cut has unique overlap')
    return actual


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=20000);a=p.parse_args()
    cases=[]
    for mask in range(8):
        s,E=create(mask,a.timeout_ms);ans=s.check();item={'mask':mask,'selected_cuts':[CUTS[i] for i in range(3) if mask>>i&1],'status':str(ans)}
        if ans==z3.sat:
            model=s.model();supp=sorted(q for q,v in E.items() if z3.is_true(model.eval(v,model_completion=True)))
            item['support']=supp;item['actual_unique_overlap_by_cut']=verify(supp,mask)
        elif ans==z3.unknown:item['reason_unknown']=s.reason_unknown()
        cases.append(item)
    result={'cases':cases,'timeout_ms_per_case':a.timeout_ms,'scope':'SMT support-only relaxation; UNSAT is not an independently checked certificate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'cases':[{k:v for k,v in c.items() if k!='support'} for c in cases],'scope':result['scope']},indent=2))


if __name__=='__main__':main()
