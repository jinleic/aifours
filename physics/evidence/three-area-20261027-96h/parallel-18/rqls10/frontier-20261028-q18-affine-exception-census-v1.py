#!/usr/bin/env python3
"""Exact half-polynomial census, plus explicitly nonproof float root triage."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import cmath,json
import numpy as np
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text());idx=D['catalog_class_1based']
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[idx-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
R=set(D['rows']);C=set(D['columns']);mask=[[int(t in R and c in C) for c in range(10)] for t in range(10)]
roots=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def prod(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def conj(a):return a[0]+a[1],-a[1]
def canon(co):
 pivot=next((v for v in co if v!=(0,0)),None)
 if pivot is None:return None
 n=prod(pivot,conj(pivot));assert n[1]==0 and n[0]>0
 return tuple(tuple(str(Q(v,n[0])) for v in prod(x,conj(pivot))) for x in co)
def match(adj):
 @lru_cache(None)
 def rec(mask):
  if not mask:return True
  x=mask&-mask;i=x.bit_length()-1;rest=mask^x;bits=adj[i]&rest
  while bits:
   y=bits&-bits;bits-=y
   if rec(rest^y):return True
  return False
 return rec(1023)
unique=set();generic=0;edgeshist=Counter();pairs=0
for E in combinations(range(10),5):
 adj=[0]*10
 for c,d in combinations(range(10),2):
  co=[(0,0),(0,0),(0,0)]
  for t in E:
   co[mask[t][d]-mask[t][c]+1]=plus(co[mask[t][d]-mask[t][c]+1],roots[(H[t][d]-H[t][c])%6])
  key=canon(co);pairs+=1
  if key is None:adj[c]|=1<<d;adj[d]|=1<<c
  else:unique.add(key)
 if match(adj):generic+=1
 edgeshist[sum(v.bit_count() for v in adj)//2]+=1
assert generic==0
print('exact half pairs',pairs,'distinct normalized nonzero polynomials',len(unique),'generic matching halves',generic,flush=True)
z6=cmath.exp(1j*cmath.pi/3);near=[]
for key in sorted(unique):
 coeff=[complex(float(Q(a)),0)+float(Q(b))*z6 for a,b in key] # powers -1,0,1
 if abs(coeff[2])<1e-12:
  rr=[] if abs(coeff[1])<1e-12 else [-coeff[0]/coeff[1]]
 else:rr=np.roots([coeff[2],coeff[1],coeff[0]])
 for z in rr:
  if abs(abs(z)-1)<1e-8:near.append([key,round(cmath.phase(z)/(2*cmath.pi),12)])
print('numeric unit-circle root occurrences',len(near),'distinct rounded phases',len(set(x[1] for x in near)),flush=True)
out={'source_q6_class':idx,'rows':sorted(R),'columns':sorted(C),'half_pairs':pairs,
     'generic_matching_halves':generic,'distinct_nonzero_polynomials':len(unique),
     'generic_edge_histogram':dict(edgeshist),'unit_root_float_occurrences':near,
     'numeric_caveat':'unit roots are float triage only; not exact coverage or no-go'}
(P/'frontier-20261028-q18-affine-exception-census-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
