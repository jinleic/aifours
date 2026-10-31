#!/usr/bin/env python3
"""Exact 4x5 and 5x4 coordinate cuts of weighted 5x5 grid source."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid55-weighted-coordinate-check.py'
expected='06ccda149c67d34d6b4b2931189530ece1a3df60c05e26c8b49d76e05fb108ce'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['cases_count']==25
O,Z=h['O'],h['Z'];conj,outer,psd=h['conj'],h['outer'],h['psd']
add,neg,mul=h['h']['add'],h['h']['h']['neg'],h['h']['h']['mul']
basis=h['basis'];weights=h['weights']; scale=h['h']['h']['scale'];roots=h['roots']
def combine(*terms):
 out=[Z]*20
 for c,v in terms:out=[add(x,mul(c,y)) for x,y in zip(out,v)]
 return out
def projected(edges,rows,cols):
 v=[Z]*20
 for x,y in edges:
  if x in rows and y in cols:
   k=len(cols)*rows.index(x)+cols.index(y);v[k]=(v[k][0]+1,v[k][1])
 return v
def rank2rect(v,nrow,ncol):
 from itertools import combinations
 m=[v[ncol*i:ncol*(i+1)] for i in range(nrow)]
 for r in combinations(range(nrow),3):
  for c in combinations(range(ncol),3):
   a,b,d=r;x,y,z=c
   z3=add(add(mul(m[a][x],add(mul(m[b][y],m[d][z]),neg(mul(m[b][z],m[d][y])))),
             neg(mul(m[a][y],add(mul(m[b][x],m[d][z]),neg(mul(m[b][z],m[d][x])))))),
          mul(m[a][z],add(mul(m[b][x],m[d][y]),neg(mul(m[b][y],m[d][x])))))
   if z3!=Z:return False
 return True
cases=[]
for side in ('alice','bob'):
 for delete in range(5):
  rows=[x for x in range(5) if side!='alice' or x!=delete]
  cols=[x for x in range(5) if side!='bob' or x!=delete]
  v=[projected(q,rows,cols) for q in basis]
  target=[[Z for _ in range(20)] for _ in range(20)]
  for w,q in zip(weights,v):outer(target,w,q)
  actual=[[Z for _ in range(20)] for _ in range(20)]
  chosen=None
  if delete>=3:
   if (side=='alice' and delete==3) or (side=='bob' and delete==4):chosen=(2,4)
   else:chosen=(3,6)
   loop,edge=chosen
   for z in roots:
    q=combine((O,v[0]),(scale(z,F(2)),v[loop]),(scale(conj(z),F(1,2)),v[edge]))
    assert rank2rect(q,len(rows),len(cols));outer(actual,F(1,4),q)
   outer(actual,F(3,4),v[edge]);excluded={0,loop,edge}
  else:
   assert rank2rect(v[0],len(rows),len(cols));excluded=set()
  for i,(w,q) in enumerate(zip(weights,v)):
   if i not in excluded:
    assert rank2rect(q,len(rows),len(cols));outer(actual,w,q)
  assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
  ncol=len(cols)
  pt=[[target[ncol*(i//ncol)+j%ncol][ncol*(j//ncol)+i%ncol] for j in range(20)] for i in range(20)]
  piv=psd(pt);assert piv is not None
  cases.append({'side':side,'deleted':delete,'pt_rank':len(piv),'entries':400,
                'phase_seed_generators':list(chosen) if chosen else None})
print(json.dumps({'weighted_source_trace':'24','cases_count':len(cases),'cases':cases,
 'rank2_phase_vector_checks':16,'total_entries_checked':4000,'all_partial_transposes_psd':True,
 'previous_weighted_25_cases_replayed':True,'previous_checker_sha256':expected},indent=2))
