#!/usr/bin/env python3
"""Produce explicit permuted-block Diţă product vectors over 30th roots."""
from pathlib import Path
import json
rows=[(a,t) for t in range(5) for a in range(2)]
mu=[0,1,2,4,3];delta=[0,10,20,1,2]
A=[[[ (3*r*tau+15*rows[tau][0]*h+delta[rows[tau][1]]*h
       +6*b*(mu[rows[tau][1]] if h else rows[tau][1]))%30
      for tau in range(10)] for h in range(2) for b in range(5)] for r in range(10)]
out=Path(__file__).resolve().parent/'frontier-20261028-dita-mu-q30-result-v1.json'
out.write_text(json.dumps({'dimension':10,'normalization':'1/sqrt(10)',
    'root':'exp(2*pi*i/30)','source_rows':rows,'mu':mu,'delta_exponents':delta,
    'exponents':A},sort_keys=True,separators=(',',':'))+'\n')
print('wrote',out.name,'independent verification required')
