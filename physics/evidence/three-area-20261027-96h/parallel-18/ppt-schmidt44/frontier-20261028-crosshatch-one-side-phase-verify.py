#!/usr/bin/env python3
"""Independent exact replay of all 4x9/9x4 coordinate cuts of CH⊗CH."""
from itertools import combinations,product
from hashlib import sha256
from contextlib import redirect_stdout
from collections import Counter
import io,json,runpy
file='frontier-20261028-crosshatch-one-side-phase-certificates-v1.json'
expected='437644f970d927f4f7877ff6284b2635f657921d568847d5111013c5ea2e368a'
raw=open(file,'rb').read();assert sha256(raw).hexdigest()==expected
records=json.loads(raw)['certificates'];bykey={}
for rec in records:
 key=(rec['side'],tuple(rec['keep']));assert key not in bykey;bykey[key]=rec
helper='frontier-20261028-crosshatch-one-copy-product-check.py'
hashhelper='c9e90c727a3c74841035e51d3a6fe54c297e0921256b0a1e5ee651f6431b37a5'
assert sha256(open(helper,'rb').read()).hexdigest()==hashhelper
buf=io.StringIO()
with redirect_stdout(buf):runpy.run_path(helper)
assert json.loads(buf.getvalue())['all_cases']==6
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
flipped=(((1,2),(0,0)),((2,2),(1,0)),((0,1),(2,0)),((0,2),(2,1)))
def matrix(es):
 m=[[0]*9 for _ in range(9)]
 for edge in es:
  v=[0]*9
  for a,b in edge:v[3*a+b]+=1
  for i in range(9):
   for j in range(9):m[i][j]+=v[i]*v[j]
 return m
rho=matrix(edges);pt=[[rho[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert pt==matrix(flipped) and sum(rho[i][i] for i in range(9))==8
coords0=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(e1,e2)) for e1,e2 in product(edges,repeat=2)]
flat=[x for q in coords0 for x in q];assert len(coords0)==16 and len(flat)==len(set(flat))==64
factorized={tuple(sorted(3*x+y for x in a for y in b)) for a in combinations(range(3),2) for b in combinations(range(3),2)}
assert len(factorized)==9
R=list(combinations(range(4),3));C=list(combinations(range(9),3))
perms=(((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1))
def rank2_phase(m):
 for rr in R:
  for cc in C:
   cyc=[0]*7
   for perm,sgn in perms:
    a=m[9*rr[0]+cc[perm[0]]];b=m[9*rr[1]+cc[perm[1]]];c=m[9*rr[2]+cc[perm[2]]]
    if a is not None and b is not None and c is not None:
     cyc[(a[1]+b[1]+c[1])%7]+=sgn*a[0]*b[0]*c[0]
   assert not any(cyc)
outputs=0;groups=0;minorpolys=0;factorcases=0;hist=Counter();maxgroup=0
for side in ('alice','bob'):
 coords=coords0 if side=='alice' else [tuple((b,a) for a,b in q) for q in coords0]
 for keep in combinations(range(9),4):
  outputs+=1;index={v:i for i,v in enumerate(keep)};mats=[];counts=[]
  for q in coords:
   m=[0]*36
   for a,b in q:
    if a in index:m[9*index[a]+b]+=1
   assert all(sum(m[9*i+j] for j in range(9))<=1 for i in range(4))
   assert all(sum(m[9*i+j] for i in range(4))<=1 for j in range(9))
   mats.append(m);counts.append(sum(m))
  active={i for i,n in enumerate(counts) if n};high={i for i in active if counts[i]>2};assert active
  if keep in factorized:
   factorcases+=1;assert (side,keep) not in bykey
   # The two factors are 2x3 product-projector sums checked by the one-copy helper.
   continue
  key=(side,keep);assert key in bykey;rec=bykey.pop(key);used=set();hist[len(rec['groups'])]+=1
  for group in rec['groups']:
   anchor=group['anchor'];terms=group['terms'];ids=[anchor]+[i for i,sgn,deg in terms]
   assert anchor in high and len(ids)<=4 and len(ids)==len(set(ids)) and all(i in active for i in ids)
   assert not used.intersection(ids);used.update(ids)
   degrees=[d for i,sgn,d in terms]
   assert all(sgn in (-1,1) and 1<=d<=6 for i,sgn,d in terms) and len(degrees)==len(set(degrees))
   m=[None]*36
   for idx,sgn,degree in [(anchor,1,0)]+terms:
    for j,x in enumerate(mats[idx]):
     if x:assert m[j] is None;m[j]=(sgn,degree)
   rank2_phase(m);minorpolys+=len(R)*len(C);groups+=1;maxgroup=max(maxgroup,len(ids))
  assert high.issubset(used)
  # Distinct residues give one unit of each used source projector; unused are rank<=2.
assert not bykey and outputs==252 and factorcases==18 and groups==496 and len(records)==234
print(json.dumps({'one_side_cuts':outputs,'factorized_separable_cuts':factorcases,
 'nonfactor_phase_certificates':len(records),'rank2_phase_groups':groups,'max_generators_per_group':maxgroup,
 'cyclic_3x3_minor_polynomials':minorpolys,'cyclic_integer_coefficients_checked':7*minorpolys,
 'group_count_histogram':dict(hist),'source_pt_entries_checked':81,'one_copy_product_identities_replayed':6,
 'disjoint_source_budgets_verified':True,'certificate_sha256':expected,'product_helper_sha256':hashhelper,
 'limits':'Proves these one-side coordinate cuts SN<=2; arbitrary opposite maps follow by local SR monotonicity. Non-coordinate maps on both sides remain open.'},indent=2))
