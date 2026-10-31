#!/usr/bin/env python3
"""Exact checks supporting q=6,10,15 and q=12 overlap statements."""
from itertools import combinations_with_replacement
import importlib.util
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cy',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec); spec.loader.exec_module(cy)


def zero_sum(terms,q,phi):
    coeff=[0]*q
    for x in terms: coeff[x]+=1
    return cy.div_monic(cy.trim(coeff),phi)[1]==[0]


def bit_remainder(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

# Irreducibility of Phi5 modulo2: no monic factor of degree1 or2.
phi5=0b11111
for degree in (1,2):
    for low in range(1<<degree):
        f=(1<<degree)|low
        assert bit_remainder(phi5,f)!=0
print('Phi5 mod2 has no monic degree1/2 factor: irreducible degree4 PASS')
assert {((a*a+a*b+b*b)%3) for a in range(3) for b in range(3)}=={0,1}
print('q6 norm a²+ab+b² residues mod3 exactly {0,1}; 8 impossible PASS')
results=[]
for q in (6,10,12,15):
    phi=cy.cyclotomic(q)
    total=0; first=None
    for seq in combinations_with_replacement(range(q),7):
        if zero_sum(seq,q,phi):
            total+=1
            if first is None: first=list(seq)
    results.append({'q':q,'zero_multiset_count':total,'first':first})
    print('q',q,'zero-sum seven-root multisets',total,'first',first,flush=True)
assert results[-1]['zero_multiset_count']==0
assert zero_sum((0,0,0,4,6,6,8),12,cy.cyclotomic(12))
assert cy.is_solution((0,0,0,3,3,4,8),12,cy.cyclotomic(12))
print('q12 separate zero-sum and squared-magnitude-8 seven-term examples PASS')
out=ROOT/'frontier-20261028-composite-phase-check-result-v1.json'
out.write_text(json.dumps({'results':results,
  'caveat':'single pair equations; no common conference or full QLS claim'},indent=2,sort_keys=True)+'\n')
print('wrote',out.name)
