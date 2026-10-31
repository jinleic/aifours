#!/usr/bin/env python3
"""Exact SR2 decompositions for all 25 coordinate cuts of the published 5x5 grid."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import product
import io,json,runpy
path='frontier-20261028-grid-unbounded-plane-check.py'
expected='03de2fa6e1670e2f5ab7c7906169ce8da3dcdae7ad00bc25d00a195ee0214ca3'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['cases'])==5
O,Z=h['O'],h['Z'];add,conj=h['add'],h['conj']
combine,outer,rank2,psd=h['combine'],h['outer'],h['rank2'],h['psd']
# Published Fig. 2: one 3-edge, three 2-edges and seven distinct loops.
basis=(((0,2),(1,1),(2,0)),((0,0),),((0,1),),((1,0),),
 ((1,2),(3,4)),((1,4),),((2,1),(4,3)),((2,2),(3,3)),
 ((2,3),),((3,2),),((4,1),))
weights=tuple(map(F,(1,1,1,1,1,1,1,1,2,2,1)))
def project(edges,rows,cols):
 v=[Z]*16
 for x,y in edges:
  if x in rows and y in cols:
   k=4*rows.index(x)+cols.index(y);v[k]=add(v[k],O)
 return v
def full(edges):
 v=[Z]*25
 for x,y in edges:v[5*x+y]=add(v[5*x+y],O)
 return v
rho=[[Z for _ in range(25)] for _ in range(25)]
for w,q in zip(weights,basis):outer(rho,w,full(q))
pt5=[[rho[5*(i//5)+j%5][5*(j//5)+i%5] for j in range(25)] for i in range(25)]
assert psd(pt5) is not None
cases=[]
for ra,rb in product(range(5),repeat=2):
 rows=[x for x in range(5) if x!=ra];cols=[x for x in range(5) if x!=rb]
 v=[project(q,rows,cols) for q in basis]
 target=[[Z for _ in range(16)] for _ in range(16)]
 for w,q in zip(weights,v):outer(target,w,q)
 actual=[[Z for _ in range(16)] for _ in range(16)]
 chosen=None
 if ra>=3 and rb>=3:
  chosen=(2,4) if (ra,rb)==(3,4) else (3,6)
  assert weights[0]==weights[chosen[0]]==weights[chosen[1]]==1
  for z in h['ROOTS']:
   q=combine((O,v[0]),(z,v[chosen[0]]),(conj(z),v[chosen[1]]))
   assert rank2(q);outer(actual,F(1,4),q)
  excluded={0,*chosen}
 else:
  assert rank2(v[0]);excluded=set()
 for i,(w,q) in enumerate(zip(weights,v)):
  if i in excluded:continue
  assert rank2(q);outer(actual,w,q)
 assert all(actual[i][j]==target[i][j] for i in range(16) for j in range(16))
 pt=[[target[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
 piv=psd(pt);assert piv is not None
 cases.append({'deleted':[ra,rb],'phase_seed_generators':list(chosen) if chosen else None,
               'entries_checked':256,'pt_rank':len(piv)})
print(json.dumps({'source':'https://arxiv.org/html/2402.12966v1 Figure 2',
 'source_pt_pivots':psd(pt5),'source_trace':str(sum(rho[i][i][0] for i in range(25))),
 'cases':cases,'cases_count':len(cases),'original_rank2_anchor_cases':21,
 'four_phase_cases':4,'rank2_phase_vector_checks':16,'total_4x4_entries_checked':25*256,
 'helper_hash':expected,'helper_cases_replayed':5},indent=2))
