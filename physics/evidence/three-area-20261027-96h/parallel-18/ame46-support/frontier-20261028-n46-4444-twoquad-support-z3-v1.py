#!/usr/bin/env python3
"""Finite support-only SMT diagnostic for the (4,4,4,4), two-quad subcase.

No phases or P completion are encoded. UNSAT is unverified solver output, not
an accepted proof or a certificate. The written packet supplies the normal form.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));WORDS=list(itertools.product(range(4),repeat=4))


def Ecell(E,A,r,B,c):
    q=[None]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def build(timeout_ms):
    E={q:z3.Bool('e'+''.join(map(str,q))) for q in WORDS};S=z3.Solver();S.set(timeout=timeout_ms)
    S.add(z3.PbEq([(v,1) for v in E.values()],20))
    for i in range(4):
        for x in range(4):
            count=4 if x<2 else 6
            S.add(z3.PbEq([(v,1) for q,v in E.items() if q[i]==x],count))
    for A in PAIRS:
        i,j=A
        for x,y in itertools.product(range(4),repeat=2):
            values=[(v,1) for q,v in E.items() if q[i]==x and q[j]==y]
            S.add(z3.Or(z3.PbEq(values,0),z3.PbEq(values,2)))
            if (x,y) in ((0,0),(1,1)):S.add(z3.Not(z3.Or(*[v for v,w in values])))
    indices=list(itertools.product(range(4),repeat=2))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A)
        grid={(r,c):Ecell(E,A,r,B,c) for r in indices for c in indices}
        for r in indices:
            for c,d in itertools.combinations(indices,2):
                other=[z3.And(grid[rp,c],grid[rp,d]) for rp in indices if rp!=r]
                S.add(z3.Implies(z3.And(grid[r,c],grid[r,d]),z3.Or(*other)))
    return S,E


def verify(S):
    if len(S)!=20:raise ValueError('wrong E support size')
    for i in range(4):
        if [sum(q[i]==x for q in S) for x in range(4)]!=[4,4,6,6]:raise ValueError('wrong fiber sizes')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in S)
        if len(C)!=10 or set(C.values())!={2} or (0,0) in C or (1,1) in C:raise ValueError('bad pair projection')
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in S:
            r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        for T in (rows,cols):
            if any(len(a&b)==1 for a,b in itertools.combinations(T.values(),2)):raise ValueError('unique overlap')
    return 'PASS: pair projection, multiplicity, fibers and all-cut no-unique-overlap'


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=90000);a=p.parse_args()
    solver,E=build(a.timeout_ms);ans=solver.check();result={'status':str(ans),'timeout_ms':a.timeout_ms,
      'normal_form':'active sizes (4,4,4,4), two all-active P words normalized 0000 and 1111, degree profile (2,2,3,3) at every party',
      'scope':'Necessary E support only, no P completion, no nonzero amplitudes, not a certificate.'}
    if ans==z3.sat:
        m=solver.model();S=sorted(q for q,v in E.items() if z3.is_true(m.eval(v,model_completion=True)))
        result['E_support']=S;result['direct_integer_validation']=verify(S)
    elif ans==z3.unknown:result['reason_unknown']=solver.reason_unknown()
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='E_support'},indent=2))


if __name__=='__main__':main()
