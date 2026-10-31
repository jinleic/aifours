#!/usr/bin/env python3
"""Formal coefficient check of complex V qubit-corner Choi decomposition.

All 8x8 entries are polynomials in independent V/conjugate(V) symbols; the
difference is checked to equal the exact isometry Gram relation, not sampled.
"""
import collections
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-local-eb-formal-choi-check-results.json'

def poly(terms):
    c=collections.Counter()
    for coeff,monomial in terms:c[tuple(sorted(monomial))]+=coeff
    return {k:v for k,v in c.items() if v}

def difference(A,B):
    c=collections.Counter(A);c.subtract(B);return {k:v for k,v in c.items() if v}

def v(a,k):return f'v{a}{k}'
def bar(a,k):return f'b{a}{k}'

errors=[];faults=0;count=0
for a,k,b,l in itertools.product(range(4),range(2),range(4),range(2)):
    # Twice direct J(Psi o Ad_V): 2 delta_ab (V†V)_{l,k} - bar(V)_{a,l} V_{b,k}.
    direct=[]
    if a==b:direct.extend((2,(v(c,k),bar(c,l))) for c in range(4))
    direct.append((-1,(bar(a,l),v(b,k))))
    # Twice claimed complement-plus-embedded-(I-F/2) decomposition.
    decomp=[]
    if a==b and k==l:decomp.append((2,()))
    decomp.append((-1,(bar(a,l),v(b,k))))
    # Difference should be exactly 2 delta_ab [(V†V)_{l,k} - delta_lk].
    gram=[]
    if a==b:
        gram.extend((2,(v(c,k),bar(c,l))) for c in range(4))
        if k==l:gram.append((-2,()))
    if difference(poly(direct),poly(decomp))!=poly(gram):errors.append([a,k,b,l])
    bad=[]
    if a==b and k==l:bad.append((2,()))
    bad.append((-1,(v(a,l),v(b,k)))) # intentional missing output conjugation
    faults+=difference(poly(direct),poly(bad))!=poly(gram);count+=1
r={'kind':'formal_complex_isometry_choi_decomposition','entries_checked':count,
   'coefficient_errors':errors,'missing_output_conjugation_fault_entries':faults,
   'identity':'2(J_direct-J_decomposition)_{ak,bl}=2 delta_ab[(V†V)_{l,k}-delta_lk] on all formal V symbols',
   'scope':'Exact formal coefficient identity for local qubit-corner Choi decomposition only; does not establish Haar moments, full EB proof, tensor stability, q3, formal kernel or independent-family review.',
   'verdict':'PASS' if count==64 and not errors and faults>0 else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
