#!/usr/bin/env python3
"""Exact reciprocal gcd decomposition for one unresolved path."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f',P/'frontier-20261028-q18-affine-unitroots-v1.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
data=json.loads((P/'frontier-20261028-q18-case8-affine-allpolys-v1.json').read_text())['polynomials']
cycl=[f.neg(f.O)]+[f.Z]*71+[f.O];records=[]
for i,rec in enumerate(data):
 p=[tuple(map(Q,x))for x in rec['coefficients']];g=f.gcd(p,[f.conj(x) for x in reversed(p)])
 if len(g)<=1:continue
 h=f.gcd(g,cycl);q,rem=f.poldiv(g,h);assert not rem
 if len(q)>1:
  records.append({'index':i,'P':rec['coefficients'],'reciprocal_gcd':[[str(a),str(b)]for a,b in g],
                  'residual':[[str(a),str(b)]for a,b in q]})
print('distinct non-cyclotomic residual factors',len(records))
for x in records:print('index',x['index'],'residual',x['residual'])
(P/'frontier-20261028-case8-exception-factors-v1.json').write_text(json.dumps({'records':records},indent=2,sort_keys=True)+'\n')
