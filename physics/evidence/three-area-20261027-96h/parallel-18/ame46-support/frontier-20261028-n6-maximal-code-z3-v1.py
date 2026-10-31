#!/usr/bin/env python3
"""Diagnostic exact finite search for the P-code constraints at N=46,t=30.

A SAT model is checked independently as a combinatorial P code. UNSAT/UNKNOWN
is solver output only, not a certificate or global proof. No E amplitudes or
unitary completion are asserted for a SAT model.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import z3

PAIRS=list(itertools.combinations(range(4),2));CATS=[(i,) for i in range(4)]+PAIRS


def build():
    words={};s=z3.Solver();s.set(timeout=90000)
    for cat in CATS:
        for x in range(3):
            v=[z3.Int(f'w_{"".join(map(str,cat))}_{x}_{i}') for i in range(4)]
            for i in range(4):
                s.add(v[i]>=0,v[i]<=2) if i in cat else s.add(v[i]>=3,v[i]<=5)
            s.add(v[cat[0]]==x);words[cat,x]=v
    for ij in PAIRS:
        i,j=ij;s.add(z3.Distinct(*[6*v[i]+v[j] for v in words.values()]))
    # Output-coordinate relabel symmetries: first singleton's three external
    # coordinates, and three P active-active matchings from party zero.
    for x in range(3):
        for j in (1,2,3):s.add(words[(0,),x][j]==3+x)
        for j in (1,2,3):s.add(words[(0,j),x][j]==x)
        s.add(words[(1,),x][0]==3+x)
    return s,words


def verify(model):
    if len(model)!=30:raise ValueError('wrong word count')
    W=[tuple(x['coordinates']) for x in model]
    for record in model:
        if tuple(i for i,x in enumerate(record['coordinates']) if x<3)!=tuple(record['active']):raise ValueError('wrong active category')
    pair_counts={}
    for i,j in PAIRS:
        pairs=[(x[i],x[j]) for x in W]
        if len(set(pairs))!=30:raise ValueError('pair collision')
        active={(a,b) for a,b in pairs if a<3 and b<3}
        if len(active)!=3 or len({a for a,b in active})!=3 or len({b for a,b in active})!=3:
            raise ValueError('active-active P pairs not a perfect matching')
        pair_counts[f'{i}{j}']={'unique_P_pairs':30,'active_active_matching':sorted(active)}
    hist=Counter(len(x['active']) for x in model)
    if dict(hist)!={1:12,2:18}:raise ValueError('active-count distribution')
    return pair_counts


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    solver,words=build();ans=solver.check();result={'solver':'Z3','timeout_ms':90000,'status':str(ans),
      'scope':'Only 30-word maximal classical code with necessary active-category and pair-injectivity constraints; no E support or AME amplitudes.'}
    if ans==z3.sat:
        m=solver.model();records=[{'active':cat,'coordinates':[m.eval(v[i]).as_long() for i in range(4)]}
            for (cat,x),v in words.items()];result['records']=records;result['direct_integer_pair_verification']=verify(records)
    elif ans==z3.unknown:result['reason_unknown']=solver.reason_unknown()
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':main()
