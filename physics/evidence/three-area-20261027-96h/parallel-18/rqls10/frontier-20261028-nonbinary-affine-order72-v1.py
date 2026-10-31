#!/usr/bin/env python3
"""Exact gcd divisibility triage for reciprocal roots of the 4-mask family."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f',P/'frontier-20261028-q18-affine-unitroots-v1.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
data=json.loads((P/'frontier-20261028-q18-nonbinary-affine-allpolys-v1.json').read_text());count=0;fails=[];hist={}
cycl=[f.neg(f.O)]+[f.Z]*71+[f.O]
for idx,rec in enumerate(data['polynomials']):
 p=[tuple(map(Q,x)) for x in rec['coefficients']];star=[f.conj(x) for x in reversed(p)];g=f.gcd(p,star)
 if len(g)<=1:continue
 _,rem=f.poldiv(cycl,g);count+=1;deg=len(g)-1;hist[deg]=hist.get(deg,0)+1
 if rem:fails.append({'index':idx,'degree':deg,'coefficients':rec['coefficients']})
print('nonconstant reciprocal gcds',count,'degrees',hist,'not dividing z^72-1',len(fails))
(P/'frontier-20261028-nonbinary-affine-order72-result-v1.json').write_text(json.dumps({'nonconstant_gcds':count,'degree_histogram':hist,'not_dividing':fails,
 'scope':'exact reciprocal-gcd overapprox; nondivisibility not evidence of unit root'},indent=2,sort_keys=True)+'\n')
