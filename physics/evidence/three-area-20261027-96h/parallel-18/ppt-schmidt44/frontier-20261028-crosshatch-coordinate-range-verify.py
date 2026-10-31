#!/usr/bin/env python3
"""Independent exact replay of all CH⊗CH coordinate range certificates."""
from itertools import combinations,product
from hashlib import sha256
from collections import Counter
import json
file='frontier-20261028-crosshatch-coordinate-certificates-v1.json'
expected='a1accb5d3cebb13ee94326dc47c5f1d69f98cbaf5b842c048046fa8254d542ae'
raw=open(file,'rb').read();assert sha256(raw).hexdigest()==expected
records=json.loads(raw)['certificates'];bykey={}
for rec in records:
 key=(tuple(rec['alice']),tuple(rec['bob']),rec['anchor'])
 assert key not in bykey
 bykey[key]=rec['low_terms']
# Independently verify the 3x3 crosshatch PT as four disjoint rank-one edges.
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
rho=edge_matrix(edges);rhs=edge_matrix(flipped)
pt=[[rho[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert pt==rhs and sum(rho[i][i] for i in range(9))==8
# Tensor source basis; each 4-term vector has disjoint support from all others.
coords=[]
for e1,e2 in product(edges,repeat=2):
 coords.append(tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(e1,e2)))
allcoords=[x for q in coords for x in q]
assert len(coords)==16 and len(allcoords)==len(set(allcoords))==64
R=list(combinations(range(4),3))
def det(m,r,c):
 a,b,d=r;x,y,z=c
 return (m[4*a+x]*(m[4*b+y]*m[4*d+z]-m[4*b+z]*m[4*d+y])-
         m[4*a+y]*(m[4*b+x]*m[4*d+z]-m[4*b+z]*m[4*d+x])+
         m[4*a+z]*(m[4*b+x]*m[4*d+y]-m[4*b+y]*m[4*d+x]))
seen=0;outputs=0;minor_checks=0;hist=Counter()
for aa,bb in product(combinations(range(9),4),repeat=2):
 outputs+=1;A={v:i for i,v in enumerate(aa)};B={v:i for i,v in enumerate(bb)}
 mats=[];counts=[]
 for q in coords:
  m=[0]*16
  for a,b in q:
   if a in A and b in B:m[4*A[a]+B[b]]+=1
  # Projected edge kets remain partial permutation matrices.
  assert all(sum(m[4*i+j] for j in range(4))<=1 for i in range(4))
  assert all(sum(m[4*i+j] for i in range(4))<=1 for j in range(4))
  mats.append(m);counts.append(sum(m))
 active=[i for i,x in enumerate(counts) if x];low={i for i in active if counts[i]<=2};high=[i for i in active if counts[i]>2]
 assert active and len(high)<=2
 hist[len(high)]+=1
 for anchor in high:
  key=(aa,bb,anchor);assert key in bykey
  terms=bykey.pop(key);assert len(terms)<=3
  ids=[term[0] for term in terms];assert len(ids)==len(set(ids)) and all(i in low for i in ids)
  assert all(s in (-1,1) for _,s in terms)
  q=mats[anchor][:]
  for idx,sign in terms:q=[x+sign*y for x,y in zip(q,mats[idx])]
  for rows in R:
   for cols in R:
    assert det(q,rows,cols)==0;minor_checks+=1
  seen+=1
assert not bykey and seen==len(records)==2256 and outputs==15876
print(json.dumps({'coordinate_pairs':outputs,'high_rank_anchor_certificates':seen,'minor_checks':minor_checks,
 'high_anchor_histogram':dict(hist),'crosshatch_pt_entries_verified':81,'crosshatch_trace':8,
 'tensor_generator_support_disjoint':True,'tensor_trace':64,'certificate_sha256':expected,
 'limits':'Exact SR2 range-spanning for these coordinate cuts only; no claim that any cut has SN<=2.'},indent=2))
