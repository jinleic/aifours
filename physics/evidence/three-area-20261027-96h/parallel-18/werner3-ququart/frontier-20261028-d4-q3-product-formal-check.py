#!/usr/bin/env python3
"""Exact formal eight-subset product identity; no physical state sampled."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-q3-product-formal-check-results.json'

def multiply(A,B):
    out={}
    for a,x in A.items():
        for b,y in B.items():
            m=tuple(sorted(a+b));out[m]=out.get(m,F(0))+x*y
    return {m:c for m,c in out.items() if c}

factored={():F(1)}
for i in range(3):factored=multiply(factored,{(f'n{i}',):F(1),(f't{i}',):F(-1,2)})
by_subset={}
for choices in itertools.product((0,1),repeat=3):
    monomial=tuple(sorted(f't{i}' if choices[i] else f'n{i}' for i in range(3)))
    by_subset[monomial]=F(-1,2)**sum(choices)
fault=dict(by_subset);fault[tuple(sorted(('t0','n1','n2')))]=F(1,2)
errors=[list(k) for k in set(factored)|set(by_subset) if factored.get(k,F(0))!=by_subset.get(k,F(0))]
faults=[list(k) for k in set(factored)|set(fault) if factored.get(k,F(0))!=fault.get(k,F(0))]
r={'kind':'exact_q3_tensor_product_formal_expansion','formal_variables':'n_i=||X_i||HS², t_i=|Tr X_i|²',
   'monomials_checked':len(by_subset),'errors':errors,'wrong_single_trace_sign_fault_mismatches':len(faults),
   'scope':'Formal product expansion only; not a selected physical state, SVD equality proof, full nonproduct q3, independent-family or formal-kernel review.',
   'verdict':'PASS' if len(by_subset)==8 and not errors and faults else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
