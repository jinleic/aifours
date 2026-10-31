#!/usr/bin/env python3
"""Exact unit-root sieve for every q6 rectangle half polynomial."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text());idx=D['catalog_class_1based']
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[idx-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
R=set(D['rows']);C=set(D['columns']);mask=[[int(t in R and c in C) for c in range(10)] for t in range(10)]
Z=(Q(0),Q(0));O=(Q(1),Q(0));six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def conj(a):return a[0]+a[1],-a[1]
def inv(a):
 n=mul(a,conj(a));assert n[1]==0 and n[0]>0
 b=conj(a);return b[0]/n[0],b[1]/n[0]
def div(a,b):return mul(a,inv(b))
def trim(a):
 a=a[:]
 while a and a[-1]==Z:a.pop()
 return a
def poldiv(a,b):
 a=trim(a);b=trim(b);q=[Z]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  k=len(a)-len(b);v=div(a[-1],b[-1]);q[k]=v
  for j,x in enumerate(b):a[k+j]=sub(a[k+j],mul(v,x))
  a=trim(a)
 return trim(q),a
def gcd(a,b):
 a,b=trim(a),trim(b)
 while b:_,r=poldiv(a,b);a,b=b,r
 if not a:return []
 return [div(v,a[-1]) for v in a]
def key(a):
 a=trim(a)
 if not a:return None
 v=a[-1]
 return tuple(div(x,v) for x in a)
@__import__('functools').lru_cache(None)
def perfect(adj,maskbits=1023):
 if not maskbits:return True
 b=maskbits&-maskbits;i=b.bit_length()-1;left=maskbits^b;can=adj[i]&left
 while can:
  x=can&-can;can-=x
  if perfect(adj,left^x):return True
 return False
unique=set();generic=0;count=0
for E in combinations(range(10),5):
 adj=[0]*10
 for c,d in combinations(range(10),2):
  a=[Z,Z,Z]
  for t in E:
   k=mask[t][d]-mask[t][c]+1
   v=tuple(map(Q,six[(H[t][d]-H[t][c])%6]));a[k]=add(a[k],v)
  ky=key(a);count+=1
  if ky is None:adj[c]|=1<<d;adj[d]|=1<<c
  else:unique.add(ky)
 if perfect(tuple(adj)):generic+=1
assert count==11340 and generic==0 and len(unique)==42
sixset={tuple(map(Q,v)) for v in six};hist=Counter();unit=set();quadratic=[]
for a in unique:
 p=list(a)+[Z]*(3-len(a));star=[conj(p[2]),conj(p[1]),conj(p[0])]
 g=gcd(p,star);deg=len(g)-1;hist[deg]+=1
 if deg==1:
  root=neg(g[0]);norm=mul(root,conj(root));assert norm[1]==0
  if norm[0]==1:
   assert root in sixset;unit.add(root)
 elif deg>=2:quadratic.append(a)
assert not quadratic and unit==sixset
print('PASS 11340 half-polynomials; 42 nonzero projective classes; generic halfgraphs have NO matching')
print('exact gcd-degree histogram',dict(hist),'unit roots',sorted(unit))
print('PASS every unit-circle root of a nonidentity half polynomial is in mu6')
print('At mu6 the matrix is BH6; base-class no-transversal must be supplied separately.')
