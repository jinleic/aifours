#!/usr/bin/env python3
"""Exact single-pair seven-root zero and norm-8 feasibility for selected q.

A common phase rotates any nonempty multiset to contain exponent0. This scans
all sorted multisets containing0; finding both cases does NOT glue a QLS.
"""
import argparse
from itertools import combinations_with_replacement
import importlib.util
import json
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cy',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec); spec.loader.exec_module(cy)


def zero_sum(terms,q,phi):
    coeff=[0]*q
    for v in terms: coeff[v]+=1
    return cy.div_monic(cy.trim(coeff),phi)[1]==[0]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seconds',type=float,default=45)
    p.add_argument('q',nargs='*',type=int,default=[14,18,20,21,24])
    args=p.parse_args()
    start=time.monotonic(); records=[]
    for q in args.q:
        phi=cy.cyclotomic(q)
        checked=0; zero=None; norm=None; complete=True
        for rest in combinations_with_replacement(range(q),6):
            terms=(0,)+rest
            checked+=1
            if zero is None and zero_sum(terms,q,phi): zero=terms
            if norm is None and cy.is_solution(terms,q,phi): norm=terms
            if zero is not None and norm is not None:
                complete=False
                break
            if checked%10000==0 and time.monotonic()-start>=args.seconds:
                complete=False
                break
        rec={'q':q,'zero_example':zero,'norm8_example':norm,'multisets_checked':checked,
             'exhausted_normalized_multisets':complete}
        records.append(rec)
        print('q',q,'checked',checked,'zero',zero,'norm8',norm,'exhausted',complete,flush=True)
        if time.monotonic()-start>=args.seconds: break
    out=ROOT/'frontier-20261028-composite-phase-scan-result-v1.json'
    out.write_text(json.dumps({'records':records,'elapsed_seconds':time.monotonic()-start,
      'caveat':'single-pair conditions only; no QLS or conference-matrix conclusion'},indent=2,sort_keys=True)+'\n')
    print('wrote',out.name,flush=True)


if __name__=='__main__':main()
