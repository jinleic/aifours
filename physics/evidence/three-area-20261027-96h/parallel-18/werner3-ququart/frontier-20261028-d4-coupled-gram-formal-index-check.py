#!/usr/bin/env python3
"""Exact formal factor identity for every coupled d4 Gram entry.

The independent labels i0..i3,j0..j3 are formal index symbols, not selected
vectors; each complex coordinate and its conjugate is a distinct variable.
"""
import collections
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/'frontier-20261028-d4-coupled-gram-formal-index-check-results.json'
U=('a','a','b','a*')
V=('b','b','a','b*')
FAMILIES={'31':'aaab','22':'aabb','13':'bbba'}
RULES={
    'uu':('31',('i0','i1','j3','i2'),('j0','j1','i3','j2')),
    'uv':('22',('i0','i1','i2','j3'),('j2','i3','j0','j1')),
    'vu':('22',('i2','j3','i0','i1'),('j0','j1','j2','i3')),
    'vv':('13',('i0','i1','j3','i2'),('j0','j1','i3','j2')),
}
PAIRS={'uu':(U,U),'uv':(U,V),'vu':(V,U),'vv':(V,V)}


def direct(row,col):
    factors=[]
    for k,(x,y) in enumerate(zip(row,col)):
        factors.append((x[0],f'i{k}',x.endswith('*')))
        factors.append((y[0],f'j{k}',not y.endswith('*')))
    return collections.Counter(factors)


def source(family,ket,bra):
    return collections.Counter([(c,k,False) for c,k in zip(FAMILIES[family],ket)]+
                               [(c,l,True) for c,l in zip(FAMILIES[family],bra)])

results={name:direct(*PAIRS[name])==source(*rule) for name,rule in RULES.items()}
# Each perturbation swaps slots containing DIFFERENT family letters.
faults={}
for name,(f,k,l) in RULES.items():
    a,b=next((a,b) for a in range(4) for b in range(a+1,4) if FAMILIES[f][a]!=FAMILIES[f][b])
    kk=list(k);kk[a],kk[b]=kk[b],kk[a]
    faults[name]=direct(*PAIRS[name])!=source(f,kk,l)
receipt={'kind':'formal_universal_coupled_gram_index_audit',
         'four_row_pair_identities':results,'mismatched_letter_ket_swap_detected':faults,
         'scope':'Formal coordinate-factor identities for arbitrary complex vectors; not certificate PSD, orbit identity, or acceptance.',
         'verdict':'PASS' if all(results.values()) and all(faults.values()) else 'FAIL'}
OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if receipt['verdict']=='PASS' else 1)
