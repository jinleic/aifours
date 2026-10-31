#!/usr/bin/env python3
"""Finite exact search for a q=12 complex conference matrix of order 9.

A SAT result is a single local block, not a resolvable QLS. UNKNOWN is no
conclusion. The solver works over integer exponents and the exact Phi_12 basis.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import time
import z3

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cyclo',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec); spec.loader.exec_module(cy)
q=12; n=9
phi=cy.cyclotomic(q)
assert phi==[1,0,-1,0,1]
table=[]
for exponent in range(q):
    coeff=[0]*(exponent+1); coeff[-1]=1
    _,rem=cy.div_monic(coeff,phi)
    table.append(rem+[0]*(4-len(rem)))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--timeout-ms',type=int,default=25000)
    args=parser.parse_args()
    solver=z3.Solver(); solver.set(timeout=args.timeout_ms,random_seed=912)
    x={(i,j):z3.Int(f'x_{i}_{j}') for i in range(n) for j in range(n) if i!=j}
    for v in x.values(): solver.add(v>=0,v<q)
    for j in range(1,n): solver.add(x[0,j]==0,x[j,0]==0)
    constraints=0
    for orientation in ('rows','columns'):
        for i,j in combinations(range(n),2):
            common=[k for k in range(n) if k not in (i,j)]
            differences=[]
            for k in common:
                a,b=(x[i,k],x[j,k]) if orientation=='rows' else (x[k,i],x[k,j])
                differences.append((a-b)%q)
            for coordinate in range(4):
                terms=[]
                for d in differences:
                    terms.append(z3.Sum([z3.If(d==t,table[t][coordinate],0)
                                         for t in range(q) if table[t][coordinate]]))
                solver.add(z3.Sum(terms)==0)
                constraints+=1
    start=time.monotonic(); verdict=solver.check(); elapsed=time.monotonic()-start
    result={'verdict':str(verdict),'timeout_ms':args.timeout_ms,'elapsed_seconds':elapsed,
            'cyclotomic_coefficients':phi,'orthogonality_integer_equations':constraints,
            'reason_unknown':solver.reason_unknown() if verdict==z3.unknown else None,
            'scope':'one order-9 conference block; not a complete QLS'}
    if verdict==z3.sat:
        model=solver.model()
        result['exponents']=[[None if i==j else model.eval(x[i,j]).as_long() for j in range(n)]
                             for i in range(n)]
    out=ROOT/'frontier-20261028-conference9-q12-smt-result-v1.json'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('q12 conference9',verdict,'equations',constraints,'elapsed',round(elapsed,3),
          'reason',result['reason_unknown'],flush=True)
    print('wrote',out.name,'; SAT must be independently exactly verified',flush=True)


if __name__=='__main__': main()
