#!/usr/bin/env python3
"""Cheap exact falsification controls for the supplementary moment proof.
Only t<=8 is evaluated; passing these moments never asserts planarity.
The proof is self-contained and this script is not a production filter.
"""
import json
from math import comb
from pathlib import Path


def main():
    rows=[]
    for n in (8,24,90,512):
        p=n*n+n+1;m=n+1;tests=[]
        for t in range(2,min(n-2,8)+1,2):
            integer=sum((-1)**j*comb(t*m,j*m) for j in range(t+1))
            residue=integer%p
            tests.append(dict(t=t,full_alternating_binomial_sum=str(integer),residue=residue))
        if n==8:assert all(r['residue']==0 for r in tests),'criterion rejected classical n=8'
        rows.append(dict(n=n,p=p,moments=tests,first_failed_t=next((r['t'] for r in tests if r['residue']),None)))
    out=dict(controls=rows,excluded_boundary_control=dict(n=2,central_binomial_residue=comb(6,3)%7,
             reason='t=2 is outside the criterion at n=2'),
             limitation='Small arithmetic controls only; no novelty and no general-range inference.')
    Path('evidence/epoch2/moment-controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:r[k] for k in ('n','p','first_failed_t')} for r in rows],indent=2))


if __name__=='__main__':main()
