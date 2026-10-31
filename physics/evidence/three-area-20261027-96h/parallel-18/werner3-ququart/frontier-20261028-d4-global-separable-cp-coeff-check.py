#!/usr/bin/env python3
"""Formal Fraction check of all eight D/K tensor coefficients; no input state."""
import collections
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-global-separable-cp-coeff-check-results.json'
words=list(product('DK',repeat=3))
lhs={w:F(1,8) for w in words}

def rhs(sfactor):
    c=collections.defaultdict(F)
    for i in range(3):
        for choice in 'DK':
            w=['D']*3;w[i]=choice;c[tuple(w)]+=sfactor/2
    for i in range(3):
        w=['D']*3;w[i]='K';c[tuple(w)]+=F(1,12)
    for i in range(3):
        for j in range(i+1,3):
            w=['D']*3;w[i]=w[j]='K';c[tuple(w)]+=F(1,8)
    c[('K','K','K')]+=F(1,8)
    return dict(c)

actual=rhs(F(1,12));bad=rhs(F(1,8))
mismatches={''.join(w):str(actual.get(w,F(0))-lhs[w]) for w in words if actual.get(w,F(0))!=lhs[w]}
faults={''.join(w):str(bad.get(w,F(0))-lhs[w]) for w in words if bad.get(w,F(0))!=lhs[w]}
r={'kind':'exact_global_separable_cp_decomposition_coefficients',
   'tensor_words_checked':len(words),'lhs_coefficients':{''.join(w):str(lhs[w]) for w in words},
   'rhs_coefficients':{''.join(w):str(actual.get(w,F(0))) for w in words},
   'mismatches':mismatches,'wrong_separable_factor_fault_mismatches':faults,
   'scope':'Formal Fraction tensor coefficients only; does not establish local EB, residual PPT, q3, source novelty, formal kernel or independent-family review. No physical input/state selected.',
   'verdict':'PASS' if not mismatches and bool(faults) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
