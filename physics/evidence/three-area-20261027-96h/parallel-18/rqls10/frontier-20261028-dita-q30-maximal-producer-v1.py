#!/usr/bin/env python3
"""Produce a maximal-QLS candidate probing a genuine non-q10 Diţă phase."""
import json
from pathlib import Path
E=[(0,0),(0,1),(0,2),(0,3),(1,3)]
O=[(1,0),(1,1),(1,2),(0,4),(1,4)]
rows=[pair for both in zip(E,O) for pair in both]
delta=[0,10,20,1,2]
A=[[[ (3*r*tau+15*rows[tau][0]*h+delta[rows[tau][1]]*h+6*rows[tau][1]*b)%30
      for tau in range(10)] for h in range(2) for b in range(5)] for r in range(10)]
data={'dimension':10,'normalization':'1/sqrt(10)','root':'exp(2*pi*i/30)',
      'row_source_pairs':rows,'delta_exponents':delta,'exponents':A}
out=Path(__file__).resolve().parent/'frontier-20261028-dita-q30-maximal-result-v1.json'
out.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
print('wrote',out.name,'independent verification required')
