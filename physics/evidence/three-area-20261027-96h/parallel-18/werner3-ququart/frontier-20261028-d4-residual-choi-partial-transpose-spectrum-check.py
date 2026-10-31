#!/usr/bin/env python3
"""Exact all-sector output-transposed residual Choi spectrum; no target state."""
import collections
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-residual-choi-partial-transpose-spectrum-check-results.json'

def value(flags,bell_value=-3):
    t=[bell_value if x else 1 for x in flags]
    return F(sum(t),12)+F(sum(t[i]*t[j] for i in range(3) for j in range(i+1,3)),8)+F(t[0]*t[1]*t[2],8)

hist=collections.Counter();bad=0
for flags in itertools.product((0,1),repeat=3):
    k=sum(flags);hist[str(value(flags))]+=15**(3-k) # local Bell dim1, orthogonal dim15
    bad+=value(flags,-2)!=value(flags)
expected={'3/4':3375,'-13/12':675,'13/12':45,'-3/4':1}
r={'kind':'exact_residual_choi_output_partial_transpose_all_sector_spectrum',
   'all_sector_count':8,'spectrum_multiplicities':dict(hist),
   'wrong_bell_eigenvalue_fault_sector_count':bad,
   'method':'Exact Fraction polynomial on all tensor products of local maximally-entangled/orthogonal projectors; uses F^(T_out)=|Omega><Omega| and ||Omega||²=4.',
   'scope':'Spectrum of fixed input-output Choi partial transpose only, not a selected physical target state, 2-positivity, residual PPT for qubit reference, q3, source novelty, formal or family review.',
   'verdict':'PASS' if dict(hist)==expected and sum(hist.values())==4096 and bad>0 else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
