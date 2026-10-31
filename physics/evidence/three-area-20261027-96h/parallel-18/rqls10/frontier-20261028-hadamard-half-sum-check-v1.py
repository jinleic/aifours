#!/usr/bin/env python3
"""Exact five-root vanishing-sum checks for Hadamard-product transversals."""
from itertools import combinations_with_replacement
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cy',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec);spec.loader.exec_module(cy)
for q in (2,3,4,5,6,7,8,9,10,12,14,15,20):
    phi=cy.cyclotomic(q); count=0; example=None
    for terms in combinations_with_replacement(range(q),5):
        coeff=[0]*q
        for x in terms:coeff[x]+=1
        if cy.div_monic(cy.trim(coeff),phi)[1]==[0]:
            count+=1
            if example is None:example=terms
    print('q',q,'five-root zero multisets',count,'first',example,flush=True)
print('finite local conditions only; no global Hadamard or QLS claim')
