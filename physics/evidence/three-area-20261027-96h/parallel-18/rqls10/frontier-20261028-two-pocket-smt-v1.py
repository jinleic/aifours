#!/usr/bin/env python3
"""Bounded exact OLS(10) search with two specified disjoint 3x3 sub-OAs.

One concrete normalized ansatz only. If SAT, exports an actual rational QLS
with two local Householder switches. UNKNOWN/UNSAT imply no global claim.
"""
import argparse
import json
from pathlib import Path
import time
import z3

ROOT=Path(__file__).resolve().parent
N=10


def solve(label_set, timeout_ms):
    solver=z3.Solver()
    solver.set(timeout=timeout_ms, random_seed=247)
    A=[[z3.Int(f'a_{r}_{c}') for c in range(N)] for r in range(N)]
    L=[[z3.Int(f'l_{r}_{c}') for c in range(N)] for r in range(N)]
    for row in A+L:
        for v in row: solver.add(v>=0,v<N)
    for r in range(N):
        solver.add(z3.Distinct(A[r]),z3.Distinct(L[r]))
    for c in range(N):
        solver.add(z3.Distinct([A[r][c] for r in range(N)]))
        solver.add(z3.Distinct([L[r][c] for r in range(N)]))
    solver.add(z3.Distinct([10*A[r][c]+L[r][c] for r in range(N) for c in range(N)]))
    for c in range(N):
        solver.add(A[0][c]==c,L[0][c]==c)
    for r in range(3):
        for c in range(3):
            solver.add(A[r][c]==(r+c)%3,L[r][c]==(2*r+c)%3)
            solver.add(A[r+3][c+3]==3+(r+c)%3,
                       L[r+3][c+3]==label_set[(2*r+c)%3])
    start=time.monotonic()
    verdict=solver.check()
    elapsed=time.monotonic()-start
    record={'second_label_set':label_set,'timeout_ms':timeout_ms,
            'verdict':str(verdict),'elapsed_seconds':elapsed,
            'reason_unknown':solver.reason_unknown() if verdict==z3.unknown else None}
    if verdict==z3.sat:
        model=solver.model()
        aa=[[model.eval(A[r][c]).as_long() for c in range(N)] for r in range(N)]
        ll=[[model.eval(L[r][c]).as_long() for c in range(N)] for r in range(N)]
        record['A']=aa; record['L']=ll
        expected=set(range(N))
        assert all(set(row)==expected for row in aa+ll)
        assert all({aa[r][c] for r in range(N)}==expected and {ll[r][c] for r in range(N)}==expected for c in range(N))
        assert len({(aa[r][c],ll[r][c]) for r in range(N) for c in range(N)})==100
        array=[]
        for r in range(N):
            row=[]
            for c in range(N):
                color=aa[r][c]
                v=[0]*N
                if r<3 and c<3:
                    for k in range(3): v[k]=(3 if k==color else 0)-2
                elif 3<=r<6 and 3<=c<6:
                    for k in range(3,6): v[k]=(3 if k==color else 0)-2
                else:
                    v[color]=3
                row.append(v)
            array.append(row)
        record['partial_witness']={'source':'two-pocket SMT witness','denominator':3,
                                   'array':array,'labels':ll,'ray_count':16}
    print('label_set',label_set,'verdict',verdict,'elapsed',round(elapsed,3),
          'reason',record['reason_unknown'],flush=True)
    return record


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--timeout-ms',type=int,default=20000)
    args=p.parse_args()
    if args.timeout_ms<1: raise ValueError('timeout must be positive')
    records=[]
    for label_set in ([0,1,2],[0,1,3]):
        result=solve(label_set,args.timeout_ms)
        records.append(result)
        if result['verdict']=='sat': break
    output=ROOT/'frontier-20261028-two-pocket-smt-result-v1.json'
    output.write_text(json.dumps({'records':records,'caveat':'fixed ansatz only; UNKNOWN is no verdict'},indent=2,sort_keys=True)+'\n')
    for result in records:
        if 'partial_witness' in result:
            cert=ROOT/'frontier-20261028-two-pocket-16ray-v1.json'
            cert.write_text(json.dumps({'partial_witness':result['partial_witness']},indent=2,sort_keys=True)+'\n')
            print('SAT candidate wrote',cert.name,'requires independent exact verification',flush=True)
            break
    print('wrote',output.name,flush=True)


if __name__=='__main__': main()
