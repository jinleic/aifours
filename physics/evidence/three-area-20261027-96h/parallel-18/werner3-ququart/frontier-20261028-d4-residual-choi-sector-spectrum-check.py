#!/usr/bin/env python3
"""Exact all-sector Choi spectrum of the fixed CP residual; no state sample."""
import collections
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-residual-choi-sector-spectrum-check-results.json'
hist=collections.Counter();sector_count=0
for sectors in itertools.product((0,1),repeat=3): # 0 symmetric, 1 antisymmetric
    k=sum(sectors);d=2*k
    eig=F(d,12)+F(4*math.comb(k,2),8)+F(8*math.comb(k,3),8)
    multiplicity=10**(3-k)*6**k
    hist[str(eig)]+=multiplicity;sector_count+=1
expected={'0':1000,'1/6':1800,'5/6':1080,'3':216}
# Deliberate omission of the triple-K term must spoil the k=3 sector.
without_triple=F(6,12)+F(4*math.comb(3,2),8)
fault=without_triple!=F(3)
ok=sector_count==8 and dict(hist)==expected and sum(hist.values())==4096 and fault
r={'kind':'exact_fixed_residual_choi_all_sector_spectrum',
   'local_symmetric_dimension':10,'local_antisymmetric_dimension':6,
   'all_sector_count':sector_count,'spectrum_multiplicities':dict(hist),
   'omitted_triple_K_fault_detected':fault,
   'method':'Exact Fraction evaluation on all eight tensor products of local swap eigenspaces; multiplicities follow from dimensions of Sym²(C⁴) and wedge²(C⁴).',
   'scope':'Spectrum of a fixed input-output Choi operator, not a chosen physical state/control, residual output PPT, q3, source novelty, formal/kernel or independent-family result.',
   'verdict':'PASS' if ok else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
