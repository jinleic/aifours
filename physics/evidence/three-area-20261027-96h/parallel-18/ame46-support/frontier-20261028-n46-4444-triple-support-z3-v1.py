#!/usr/bin/env python3
"""SMT diagnostics for the remaining 4444 N46 all-low triple subcase.

Only E-support necessities are encoded. SAT is not an AME witness; UNSAT is
not an independently checked certificate. A=4-valued residual alphabets.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));IDX=list(itertools.product(range(4),repeat=2))


def val(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def solve(kind,cutmask,timeout):
    # Normalize one all-low triple P word to (0,0,0,external).
    fibers=[[4,4,6,6] for _ in range(4)]
    if kind=='one_degree4_in_triple':fibers[0]=[4,4,4,8]
    elif kind=='one_degree4_outside_triple':fibers[3]=[4,4,4,8]
    E={q:z3.Bool('e'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=timeout)
    for i in range(4):
      for x in range(4):S.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==x],fibers[i][x]))
    for i,j in PAIRS:
      for x,y in IDX:
        vals=[v for q,v in E.items() if q[i]==x and q[j]==y]
        S.add(z3.Or(z3.PbEq([(v,1) for v in vals],0),z3.PbEq([(v,1) for v in vals],2)))
        if i<3 and j<3 and x==y==0:S.add(z3.Not(z3.Or(*vals)))
    for k,A in enumerate(CUTS):
      if not(cutmask>>k&1):continue
      B=tuple(i for i in range(4) if i not in A);grid={(r,c):val(E,A,r,B,c) for r in IDX for c in IDX}
      for r in IDX:
       for c,d in itertools.combinations(IDX,2):
        S.add(z3.Implies(z3.And(grid[r,c],grid[r,d]),z3.Or(*[z3.And(grid[s,c],grid[s,d]) for s in IDX if s!=r])))
    ans=S.check();result={'profile':kind,'cutmask':cutmask,'status':str(ans)}
    if ans==z3.sat:
        m=S.model();Eset=sorted(q for q,v in E.items() if z3.is_true(m.eval(v,model_completion=True)));verify(Eset,fibers,cutmask)
        result['E_support']=Eset;result['direct_support_validation']='PASS'
    elif ans==z3.unknown:result['reason_unknown']=S.reason_unknown()
    return result


def verify(E,fibers,mask):
    if len(E)!=20 or len(set(E))!=20:raise ValueError('wrong support')
    for i in range(4):
        if [sum(q[i]==x for q in E) for x in range(4)]!=fibers[i]:raise ValueError('fiber mismatch')
    for i,j in PAIRS:
        P=Counter((q[i],q[j]) for q in E)
        if len(P)!=10 or set(P.values())!={2}:raise ValueError('pair multiplicity')
        if i<3 and j<3 and (0,0) in P:raise ValueError('maximal triple conflict')
    for k,A in enumerate(CUTS):
        if not(mask>>k&1):continue
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in E:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        if any(len(x&y)==1 for M in (rows,cols) for x,y in itertools.combinations(M.values(),2)):raise ValueError('unique overlap')


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=15000);a=p.parse_args()
    K=('no_degree4','one_degree4_in_triple','one_degree4_outside_triple')
    cases=[solve(k,mask,a.timeout_ms) for k in K for mask in (0,7)]
    result={'cases':cases,'timeout_ms_per_case':a.timeout_ms,'scope':'Uncertified support-only SMT diagnostics; no P completion or amplitudes.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'cases':[{k:v for k,v in q.items() if k!='E_support'} for q in cases],'scope':result['scope']},indent=2))


if __name__=='__main__':main()
