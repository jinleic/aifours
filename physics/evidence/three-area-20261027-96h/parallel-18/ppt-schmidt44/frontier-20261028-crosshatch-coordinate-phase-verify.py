#!/usr/bin/env python3
"""Independent exact replay: all CH⊗CH coordinate cuts admit SR2 decompositions."""
from itertools import combinations,product
from hashlib import sha256
from collections import Counter
import json
file='frontier-20261028-crosshatch-coordinate-phase-certificates-v1.json'
expected='c89fd917447d81b79883d23582541fd9012c3d9c63122c1d0d1e311477718226'
raw=open(file,'rb').read();assert sha256(raw).hexdigest()==expected
records=json.loads(raw)['certificates'];bykey={}
for rec in records:
 key=(tuple(rec['alice']),tuple(rec['bob']),rec['anchor'])
 assert key not in bykey;bykey[key]=rec
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
flipped=(((1,2),(0,0)),((2,2),(1,0)),((0,1),(2,0)),((0,2),(2,1)))
def edge_matrix(es):
 m=[[0]*9 for _ in range(9)]
 for edge in es:
  v=[0]*9
  for a,b in edge:v[3*a+b]+=1
  for i in range(9):
   for j in range(9):m[i][j]+=v[i]*v[j]
 return m
rho=edge_matrix(edges);pt=[[rho[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert pt==edge_matrix(flipped) and sum(rho[i][i] for i in range(9))==8
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(e1,e2)) for e1,e2 in product(edges,repeat=2)]
allcoords=[x for q in coords for x in q]
assert len(coords)==16 and len(allcoords)==len(set(allcoords))==64
R=list(combinations(range(4),3))
terms=(((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1))
def all_minor_polynomials_zero(m):
 for rr in R:
  for cc in R:
   cyc=[0]*7
   for perm,sgn in terms:
    a=m[4*rr[0]+cc[perm[0]]];b=m[4*rr[1]+cc[perm[1]]];c=m[4*rr[2]+cc[perm[2]]]
    if a is not None and b is not None and c is not None:
     cyc[(a[1]+b[1]+c[1])%7]+=sgn*a[0]*b[0]*c[0]
   assert not any(cyc)
outputs=0;anchors=0;minor_polynomials=0;hist=Counter();max_terms=0
for aa,bb in product(combinations(range(9),4),repeat=2):
 outputs+=1;A={v:i for i,v in enumerate(aa)};B={v:i for i,v in enumerate(bb)}
 matrices=[];counts=[]
 for q in coords:
  m=[0]*16
  for a,b in q:
   if a in A and b in B:m[4*A[a]+B[b]]+=1
  assert all(sum(m[4*i+j] for j in range(4))<=1 for i in range(4))
  assert all(sum(m[4*i+j] for i in range(4))<=1 for j in range(4))
  matrices.append(m);counts.append(sum(m))
 active=[i for i,x in enumerate(counts) if x];low={i for i in active if counts[i]<=2};high=[i for i in active if counts[i]>2]
 assert active and len(high)<=2;hist[len(high)]+=1;used=set()
 for anchor in high:
  key=(aa,bb,anchor);assert key in bykey;rec=bykey.pop(key)
  low_terms=rec['low_terms'];degrees=rec['degrees'];assert len(low_terms)==len(degrees)<=3
  ids=[idx for idx,sign in low_terms]
  assert len(ids)==len(set(ids)) and all(i in low for i in ids) and not used.intersection(ids)
  assert all(sign in (-1,1) for idx,sign in low_terms)
  assert all(isinstance(d,int) and 1<=d<=6 for d in degrees) and len(set(degrees))==len(degrees)
  used.update(ids);max_terms=max(max_terms,len(ids))
  m=[None]*16
  for idx,sign,degree in [(anchor,1,0)]+[(idx,sign,deg) for (idx,sign),deg in zip(low_terms,degrees)]:
   for j,x in enumerate(matrices[idx]):
    if x:assert m[j] is None;m[j]=(sign,degree)
  all_minor_polynomials_zero(m);minor_polynomials+=16;anchors+=1
 # Distinct phase residues yield exactly one projector for anchor and each used low;
 # other low-rank source projectors remain untouched. No source budget is shared.
assert not bykey and outputs==15876 and anchors==len(records)==2256
print(json.dumps({'coordinate_pairs':outputs,'phase_anchor_certificates':anchors,
 'cyclic_3x3_minor_polynomials':minor_polynomials,'cyclic_integer_coefficients_checked':7*minor_polynomials,
 'high_anchor_histogram':dict(hist),'max_low_terms_per_phase':max_terms,
 'source_pt_entries_checked':81,'source_trace':8,'tensor_trace':64,
 'disjoint_low_budgets_verified':True,'certificate_sha256':expected,
 'limits':'Proves SN<=2 and PPT for these coordinate cuts only; non-coordinate maps remain open.'},indent=2))
