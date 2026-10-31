#!/usr/bin/env python3
"""Exact weighted variant of all coordinate cuts of the 5x5 grid source."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import product
import io,json,runpy
path='frontier-20261028-grid55-all-coordinate-sn2-check.py'
expected='18961d59d173b3987bc3072284552b5394b0f0d1a3078c69ab2705e8f569bd76'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['cases_count']==25
O,Z=h['O'],h['Z'];conj=h['conj'];combine,outer,rank2,psd=h['combine'],h['outer'],h['rank2'],h['psd']
basis=h['basis'];project,full=h['project'],h['full']; roots=h['h']['ROOTS']
weights=tuple(map(F,(1,1,4,4,1,1,1,1,2,2,1)))
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
 if ra>=3 and rb>=3:
  loop,edge=(2,4) if (ra,rb)==(3,4) else (3,6)
  assert weights[0]==weights[edge]==1 and weights[loop]==4
  for z in roots:
   q=combine((O,v[0]),(h['h']['scale'](z,F(2)),v[loop]),
             (h['h']['scale'](conj(z),F(1,2)),v[edge]))
   assert rank2(q);outer(actual,F(1,4),q)
  outer(actual,F(3,4),v[edge]);excluded={0,loop,edge}
 else:
  assert rank2(v[0]);excluded=set()
 for i,(w,q) in enumerate(zip(weights,v)):
  if i not in excluded:
   assert rank2(q);outer(actual,w,q)
 assert all(actual[i][j]==target[i][j] for i in range(16) for j in range(16))
 pt=[[target[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
 piv=psd(pt);assert piv is not None
 cases.append({'deleted':[ra,rb],'entries_checked':256,'pt_rank':len(piv)})
print(json.dumps({'weights':list(map(str,weights)),'source_trace':str(sum(rho[i][i][0] for i in range(25))),
 'source_pt_pivots':psd(pt5),'cases_count':len(cases),'all_output_pt_nonnegative':True,
 'four_phase_cases':4,'phase_vectors_checked':16,'total_4x4_entries_checked':25*256,
 'previous_25_cases_replayed':True,'previous_checker_sha256':expected,'cases':cases},indent=2))
