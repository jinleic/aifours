#!/usr/bin/env python3
"""Exact search for a BH(10,5) five-row subframe with five orthogonal pairs.

A SAT result is a half-frame only; it need not extend to a full BH(10,5).
UNKNOWN or an unverified solver UNSAT is not a theorem.
"""
import argparse
import json
from pathlib import Path
import time
import z3

ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,default=30000);args=p.parse_args()
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=751)
    A=[[z3.Int(f'a_{i}_{j}') for j in range(10)] for i in range(5)]
    for row in A:
        for x in row:s.add(x>=0,x<5)
    for j in range(10):s.add(A[0][j]==0)
    for i in range(5):s.add(A[i][0]==0,A[i][1]==i)
    # Pairwise full-row differences have each fifth-root phase exactly twice.
    for i in range(5):
        for j in range(i+1,5):
            for k in range(5):
                s.add(z3.Sum([z3.If((A[i][c]-A[j][c])%5==k,1,0) for c in range(10)])==2)
    # Each of the five designated column pairs is orthogonal on these five rows.
    for col in range(0,10,2):
        for k in range(5):
            s.add(z3.Sum([z3.If((A[i][col]-A[i][col+1])%5==k,1,0) for i in range(5)])==1)
    start=time.monotonic();verdict=s.check();elapsed=time.monotonic()-start
    record={'verdict':str(verdict),'timeout_ms':args.timeout_ms,'elapsed_seconds':elapsed,
            'reason_unknown':s.reason_unknown() if verdict==z3.unknown else None,
            'scope':'one normalized 5x10 half-frame; SAT does not imply BH extension or QLS'}
    if verdict==z3.sat:
        model=s.model()
        record['exponents']=[[model.eval(A[i][j]).as_long() for j in range(10)] for i in range(5)]
    output=ROOT/'frontier-20261028-bh5-half-frame-smt-result-v1.json'
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('BH5 half-frame',verdict,'elapsed',round(elapsed,3),'reason',record['reason_unknown'])
    if verdict==z3.sat:
        for row in record['exponents']:print(''.join(map(str,row)))
        print('SAT requires independent exact check and does not establish full BH extension')
    print('wrote',output.name)


if __name__=='__main__':main()
