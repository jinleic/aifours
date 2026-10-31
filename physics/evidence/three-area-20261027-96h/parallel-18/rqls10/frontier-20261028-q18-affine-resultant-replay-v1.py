#!/usr/bin/env python3
"""Independent all-half-polynomial resultant/unit-root classification."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text())
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['catalog_class_1based']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
R=set(D['rows']);C=set(D['columns']);M=[[int(t in R and c in C) for c in range(10)] for t in range(10)]
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)];S={tuple(map(Q,z)) for z in six};Z=(Q(0),Q(0))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]
def conj(x):return x[0]+x[1],-x[1]
def norm(x):
 n=mul(x,conj(x));assert n[1]==0 and n[0]>=0;return n[0]
def rootdiv(x,y):
 n=norm(y);assert n>0;v=mul(x,conj(y));return v[0]/n,v[1]/n
stats={'identity':0,'resultant_nonzero':0,'unit_six':0,'zero_monomial':0}
for E in combinations(range(10),5):
 for c,d in combinations(range(10),2):
  coeff=[Z,Z,Z]
  for t in E:
   k=M[t][d]-M[t][c]+1;coeff[k]=add(coeff[k],tuple(map(Q,six[(H[t][d]-H[t][c])%6])))
  cm,b,a=coeff
  if a==b==cm==Z:stats['identity']+=1;continue
  A=norm(a)-norm(cm);B=sub(mul(a,conj(b)),mul(b,conj(cm)))
  res=A*A-norm(B)
  if res!=0:stats['resultant_nonzero']+=1;continue
  if B==Z:
   assert A==0 and a==cm==Z and b!=Z
   stats['zero_monomial']+=1;continue
  root=rootdiv((Q(-A),Q(0)),B)
  assert norm(root)==1 and root in S
  assert add(add(mul(a,mul(root,root)),mul(b,root)),cm)==Z
  stats['unit_six']+=1
assert sum(stats.values())==252*45
print('PASS independent exact resultant for all11340 half-polynomials:',stats)
print('Every nonidentity half polynomial with a unit-circle root has that root in mu6.')
