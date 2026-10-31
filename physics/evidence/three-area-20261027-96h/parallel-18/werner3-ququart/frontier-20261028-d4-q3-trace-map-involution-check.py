#!/usr/bin/env python3
"""Formal Fraction check of W²=I for commuting D_i²=4D_i."""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-q3-trace-map-involution-check-results.json'
W={mask:F(-1,2)**mask.bit_count() for mask in range(8)}

def square(dimension):
    out={m:F(0) for m in range(8)}
    for a,x in W.items():
        for b,y in W.items():out[a|b]+=x*y*dimension**((a&b).bit_count())
    return out

actual=square(4);wrong=square(3)
expected={m:F(int(m==0)) for m in range(8)}
r={'kind':'formal_original_q3_trace_map_involution',
   'source_W_coefficients':{str(k):str(v) for k,v in W.items()},
   'square_coefficients':{str(k):str(v) for k,v in actual.items()},
   'all_eight_coefficients_correct':actual==expected,
   'wrong_local_dimension_fault_detected':wrong!=expected,
   'scope':'Formal Fraction algebra for commuting trace insertions satisfying D_i²=4D_i only; does not check derivative, source nonnegativity, equality classification, physical state, formal kernel or family review.',
   'verdict':'PASS' if actual==expected and wrong!=expected else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
