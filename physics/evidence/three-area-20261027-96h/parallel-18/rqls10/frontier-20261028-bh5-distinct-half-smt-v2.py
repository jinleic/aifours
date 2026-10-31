#!/usr/bin/env python3
"""Exact search for a nonduplicate five-row BH(10,5) half-frame.

The distinct-column filter is necessary for extension to full BH(10,5);
SAT still does not prove an extension or a resolvable QLS.
"""
import argparse
import json
from pathlib import Path
import time
import z3

ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,default=30000);args=p.parse_args()
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=752)
    A=[[z3.Int(f'a_{i}_{j}') for j in range(10)] for i in range(5)]
    for row in A:
        for x in row:s.add(x>=0,x<5)
    for j in range(10):s.add(A[0][j]==0)
    for i in range(5):s.add(A[i][0]==0,A[i][1]==i)
    for i in range(5):
        for j in range(i+1,5):
            for k in range(5):
                s.add(z3.Sum([z3.If((A[i][c]-A[j][c])%5==k,1,0) for c in range(10)])==2)
    for col in range(0,10,2):
        for k in range(5):
            s.add(z3.Sum([z3.If((A[i][col]-A[i][col+1])%5==k,1,0) for i in range(5)])==1)
    # Any equal half-columns would force an impossible -1 ratio in the other
    # half of a complete fifth-root Hadamard, so this condition is necessary.
    for c in range(10):
        for d in range(c+1,10):s.add(z3.Or([A[i][c]!=A[i][d] for i in range(1,5)]))
    start=time.monotonic();verdict=s.check();elapsed=time.monotonic()-start
    rec={'verdict':str(verdict),'elapsed_seconds':elapsed,'timeout_ms':args.timeout_ms,
         'reason_unknown':s.reason_unknown() if verdict==z3.unknown else None,
         'scope':'normalized 5x10 distinct-column half-frame only; SAT not a full BH'}
    if verdict==z3.sat:
        model=s.model();rec['exponents']=[[model.eval(A[i][j]).as_long() for j in range(10)] for i in range(5)]
    out=ROOT/'frontier-20261028-bh5-distinct-half-smt-result-v2.json'
    out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print('distinct BH5 half-frame',verdict,'elapsed',round(elapsed,3),'reason',rec['reason_unknown'],flush=True)
    if verdict==z3.sat:
        for row in rec['exponents']:print(''.join(map(str,row)))
        print('SAT requires independent exact check and full BH-extension search',flush=True)
    print('wrote',out.name,flush=True)


if __name__=='__main__':main()
