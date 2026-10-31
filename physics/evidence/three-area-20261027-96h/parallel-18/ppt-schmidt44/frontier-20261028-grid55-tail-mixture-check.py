#!/usr/bin/env python3
"""Exact mixed-tail 4x5/5x4 Gram decomposition checks."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid55-single-coordinate-check.py'
expected='963dd8014c9f614b02433168325e37293f1375c8c2482f3da5bd3b6b35c7660f'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['cases_count']==10
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2=h['combine'],h['outer'],h['psd'],h['rank2rect']
basis,weights,roots,scale=h['basis'],h['weights'],h['roots'],h['scale']
def projected(edges,side,r):
 v=[Z]*20
 for a,b in edges:
  if side=='alice':
   coeff=r if a==4 else O;aa=3 if a==4 else a;k=5*aa+b
  else:
   coeff=r if b==4 else O;bb=3 if b==4 else b;k=4*a+bb
  v[k]=add(v[k],coeff)
 return v
def cross(m,c,v,w):
 for i,x in enumerate(v):
  for j,y in enumerate(w):m[i][j]=add(m[i][j],mul(c,mul(x,conj(y))))
cases=[]
for side in ('alice','bob'):
 for r in (Z,O,(F(0),F(1)),(F(2),F(0))):
  v=[projected(q,side,r) for q in basis]
  nrow,ncol=(4,5) if side=='alice' else (5,4)
  loop,edge=(3,6) if side=='alice' else (2,4)
  target=[[Z for _ in range(20)] for _ in range(20)]
  for w,q in zip(weights,v):outer(target,w,q)
  Y=combine((O,v[edge]),(neg(r),v[7]))
  actual=[[Z for _ in range(20)] for _ in range(20)]
  for z in roots:
   q=combine((O,v[0]),(scale(z,F(2)),v[loop]),(scale(conj(z),F(1,2)),Y))
   assert rank2(q,nrow,ncol);outer(actual,F(1,4),q)
  rr=mul(r,conj(r));t=(O,neg(r));basis2=(v[edge],v[7])
  H=[[add((F(1 if i==j else 0),F(0)),neg(scale(mul(t[i],conj(t[j])),F(1,4))))
      for j in range(2)] for i in range(2)]
  for i,left in enumerate(basis2):
   for j,right in enumerate(basis2):cross(actual,H[i][j],left,right)
  for i,(w,q) in enumerate(zip(weights,v)):
   if i not in {0,loop,edge,7}:
    assert rank2(q,nrow,ncol);outer(actual,w,q)
  assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
  pt=[[target[ncol*(i//ncol)+j%ncol][ncol*(j//ncol)+i%ncol] for j in range(20)] for i in range(20)]
  assert psd(pt) is not None
  gram=psd(H)
  assert (gram is not None)==(rr[0]<=3)
  cases.append({'side':side,'r':list(map(str,r)),'gram_pivots':gram,'pt_rank':len(psd(pt)),
                'entries_checked':400,'rank2_phase_vectors':4})
print(json.dumps({'cases':cases,'total_cases':len(cases),'total_entries_checked':3200,
 'source_weights':'trace24 weighted 5x5 grid','negative_control':'r=2 fails this Gram only',
 'previous_single_coordinate_cases_replayed':True,'previous_checker_sha256':expected},indent=2))
