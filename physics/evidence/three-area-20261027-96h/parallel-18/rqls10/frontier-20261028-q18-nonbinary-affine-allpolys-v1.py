#!/usr/bin/env python3
"""Exact reciprocal-gcd triage for one 4-rectangle affine subfamily."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
from collections import Counter
import importlib.util,json
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f',P/'frontier-20261028-q18-affine-unitroots-v1.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
D=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'][0]
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
R=[[sum(co*int(t in mask['rows'] and c in mask['columns']) for co,mask in zip(D['coefficients'],D['rectangles'])) for c in range(10)]for t in range(10)]
N=max(map(max,R));assert N==6
@lru_cache(None)
def classify(key):
 p=list(key);star=[f.conj(x) for x in reversed(p)];g=f.gcd(p,star)
 if len(g)<=1:return 'no_unit_possible',0
 sixth=[f.neg(f.O)]+[f.Z]*5+[f.O];_,rem=f.poldiv(sixth,g)
 return ('mu6_only' if not rem else 'extra_possible'),len(g)-1
@lru_cache(None)
def match(adj,mask=1023):
 if not mask:return True
 bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;can=adj[i]&rest
 while can:
  b=can&-can;can-=b
  if match(adj,rest^b):return True
 return False
categories=Counter();generic=0;unique={};extra=[]
for E in combinations(range(10),5):
 adj=[0]*10
 for c,d in combinations(range(10),2):
  co=[f.Z]*(2*N+1)
  for t in E:
   e=R[t][d]-R[t][c]+N;co[e]=f.add(co[e],tuple(map(f.Q,f.six[(H[t][d]-H[t][c])%6])))
  while co and co[-1]==f.Z:co.pop()
  while co and co[0]==f.Z:co.pop(0)
  if not co:categories['identity']+=1;adj[c]|=1<<d;adj[d]|=1<<c;continue
  pivot=co[-1];ky=tuple(f.div(x,pivot) for x in co);typ,deg=classify(ky);categories[typ]+=1
  unique[ky]=(typ,deg)
  if typ=='extra_possible' and len(extra)<10:extra.append({'E':list(E),'columns':[c,d],'degree_gcd':deg,
      'coefficients':[[str(x),str(y)] for x,y in ky]})
 if match(tuple(adj)):generic+=1
out={'case':0,'mask_max':N,'half_polynomials':252*45,'categories':dict(categories),
     'unique_polynomials':len(unique),'generic_matching_halves':generic,'examples_extra':extra,
     'scope':'reciprocal-gcd overapprox; extra_possible may have no unit root and is not a transversal'}
out['polynomials']=[{'coefficients':[[str(x),str(y)] for x,y in ky],'type':v[0],'gcd_degree':v[1]} for ky,v in unique.items()]
(P/'frontier-20261028-q18-nonbinary-affine-allpolys-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('categories',dict(categories),'unique',len(unique),'generic_matching_halves',generic,'extra examples',len(extra),flush=True)
