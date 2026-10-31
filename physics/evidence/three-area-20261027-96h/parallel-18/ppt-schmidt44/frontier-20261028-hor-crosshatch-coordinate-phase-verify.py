#!/usr/bin/env python3
"""Exact Q(sqrt2) replay of 4x12 Horodecki-crosshatch coordinate certificates."""
from fractions import Fraction as F
from itertools import combinations,product
from hashlib import sha256
from collections import Counter
import json
file='frontier-20261028-hor-crosshatch-coordinate-phase-certificates-v1.json'
expected='c340278652fa0e0753bea93595b50287de5f5c824bccbdbe5d2382dbe8ee8c8d'
raw=open(file,'rb').read();assert sha256(raw).hexdigest()==expected
records=json.loads(raw)['certificates'];bykey={}
for rec in records:
 key=(tuple(rec['bob']),rec['anchor']);assert key not in bykey;bykey[key]=rec
Z=(F(0),F(0));O=(F(1),F(0));S=(F(0),F(1))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
 d=b[0]**2-2*b[1]**2;assert d
 return ((a[0]*b[0]-2*a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)
def sign(x):
 a,b=x
 if not a:return (b>0)-(b<0)
 if not b:return (a>0)-(a<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 if a>0:return (a*a>2*b*b)-(a*a<2*b*b)
 return (2*b*b>a*a)-(2*b*b<a*a)
def psd(M):
 a=[row[:] for row in M];piv=[]
 while a:
  if any(sign(a[i][i])<0 for i in range(len(a))):return None
  j=next((i for i in range(len(a)) if sign(a[i][i])>0),None)
  if j is None:return piv if all(x==Z for row in a for x in row) else None
  s=a[j][j];piv.append(s);rem=[i for i in range(len(a)) if i!=j]
  a=[[add(a[i][k],neg(div(mul(a[i][j],a[j][k]),s))) for k in rem] for i in rem]
 return piv
def vec(n,terms):
 v=[Z]*n
 for k,x in terms:v[k]=add(v[k],x)
 return v
def outer(m,v):
 for i,x in enumerate(v):
  for j,y in enumerate(v):m[i][j]=add(m[i][j],mul(x,y))
Hedges=(((0,0,O),),((0,1,O),(1,0,O)),((0,3,O),(1,2,O)),
        ((0,2,O),(1,1,O)),((1,3,S),(1,0,O)))
Cedges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
HR=[[Z for _ in range(8)] for _ in range(8)]
for q in Hedges:outer(HR,vec(8,[(4*a+b,x) for a,b,x in q]))
HPT=[[HR[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(8)] for i in range(8)]
hpsd=psd(HPT);assert hpsd is not None and sum(HR[i][i][0] for i in range(8))==10
# Independent exact PT certificate for the crosshatch input.
def cmatrix(es):
 m=[[0]*9 for _ in range(9)]
 for edge in es:
  v=[0]*9
  for a,b in edge:v[3*a+b]+=1
  for i in range(9):
   for j in range(9):m[i][j]+=v[i]*v[j]
 return m
CR=cmatrix(Cedges);CPT=[[CR[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert CPT==cmatrix((((1,2),(0,0)),((2,2),(1,0)),((0,1),(2,0)),((0,2),(2,1))))
# Alice basis of the paper's projection Pi_A: (0,0),(0,1),(0,2),(1,1).
AA=((0,0),(0,1),(0,2),(1,1));source=[]
for H,C in product(Hedges,Cedges):
 q=[Z]*48
 for (a,b,x),(c,d) in product(H,C):
  if (a,c) in AA:
   k=12*AA.index((a,c))+3*b+d;q[k]=add(q[k],x)
 source.append(q)
trace=Z
for q in source:
 for x in q:trace=add(trace,mul(x,x))
assert trace==(F(44),F(0))
R=list(combinations(range(4),3));perms=(((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1))
def det(v,rr,cc):
 x=Z
 for perm,sgn in perms:
  z=mul(mul(v[4*rr[0]+cc[perm[0]]],v[4*rr[1]+cc[perm[1]]]),v[4*rr[2]+cc[perm[2]]])
  x=add(x,z if sgn==1 else neg(z))
 return x
def rank2(v):return all(det(v,r,c)==Z for r in R for c in R)
def padd(a,b):
 o=dict(a)
 for k,v in b.items():o[k]=add(o.get(k,Z),v)
 return {k:v for k,v in o.items() if v!=Z}
def pmul(a,b):
 o={}
 for i,x in a.items():
  for j,y in b.items():
   k=(i+j)%7;o[k]=add(o.get(k,Z),mul(x,y))
 return {k:v for k,v in o.items() if v!=Z}
def polyzero(m):
 for rr in R:
  for cc in R:
   o={}
   for perm,sgn in perms:
    q=pmul(pmul(m[4*rr[0]+cc[perm[0]]],m[4*rr[1]+cc[perm[1]]]),m[4*rr[2]+cc[perm[2]]])
    if sgn<0:q={k:neg(v) for k,v in q.items()}
    o=padd(o,q)
   assert not o
outputs=0;anchors=0;hist=Counter();minor_polys=0;half_coeff=0;shared=0
for cols in combinations(range(12),4):
 outputs+=1;idx=[12*a+b for a in range(4) for b in cols]
 mats=[[q[i] for i in idx] for q in source]
 active=[i for i,v in enumerate(mats) if any(x!=Z for x in v)]
 low={i for i in active if rank2(mats[i])};high=[i for i in active if i not in low]
 assert active and len(high)<=2;hist[len(high)]+=1;budget=Counter()
 for anchor in high:
  key=(cols,anchor);assert key in bykey;rec=bykey.pop(key);terms=rec['low_terms']
  assert len(terms)<=3 and len({j for j,_,_ in terms})==len(terms)
  assert all(j in low and abs(code) in (1,2) and 1<=degree<=6 for j,code,degree in terms)
  degs=[degree for _,_,degree in terms];assert len(degs)==len(set(degs))
  M=[{} for _ in range(16)]
  for idx0,code,degree in [(anchor,1,0)]+terms:
   coeff=(F(1 if code>0 else -1),F(0)) if abs(code)==1 else (F(0),F(1 if code>0 else -1,2))
   if idx0!=anchor:
    budget[idx0]+=F(1) if abs(code)==1 else F(1,2)
    if abs(code)==2:half_coeff+=1
   for i,x in enumerate(mats[idx0]):
    v=mul(coeff,x)
    if v!=Z:M[i]=padd(M[i],{degree:v})
  polyzero(M);minor_polys+=16;anchors+=1
 assert all(cost<=1 for cost in budget.values())
 if len(high)==2:
  shared+=sum(1 for cost in budget.values() if cost==1)
assert outputs==495 and anchors==len(records)==54 and not bykey
print(json.dumps({'coordinate_cuts':outputs,'high_anchor_certificates':anchors,'high_histogram':dict(hist),
 'cyclic_minor_polynomials':minor_polys,'coefficient_field':'Q(sqrt(2))','half_budget_terms':half_coeff,
 'horodecki_pt_pivot_count':len(hpsd),'horodecki_trace':10,'source_4x12_trace':44,
 'crosshatch_pt_entries_checked':81,'all_low_budgets_at_most_one':True,'certificate_sha256':expected,
 'limits':'Proves SN<=2 and PPT for these 495 coordinate cuts only. Source 4x12 SN3 is attributed to the cited paper.'},indent=2))
