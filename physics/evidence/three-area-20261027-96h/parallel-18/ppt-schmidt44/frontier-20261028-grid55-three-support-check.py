#!/usr/bin/env python3
"""Exact 4x5/5x4 SR2 Gram identities for mixed two-head kernels."""
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
def projected(edges,v0,v1,side):
 v=[Z]*20
 for a,b in edges:
  if side=='alice':
   terms=((0,v0),(1,v1)) if a==3 else ((3,O),) if a==4 else ((a,O),)
   for aa,x in terms:v[5*aa+b]=add(v[5*aa+b],x)
  else:
   terms=((0,v0),(1,v1)) if b==3 else ((3,O),) if b==4 else ((b,O),)
   for bb,x in terms:v[4*a+bb]=add(v[4*a+bb],x)
 return v
def cross(m,c,v,w):
 for i,x in enumerate(v):
  for j,y in enumerate(w):m[i][j]=add(m[i][j],mul(c,mul(x,conj(y))))
cases=[]
for v0,v1 in ((O,O),((F(0),F(1)),(F(1),F(1))),((F(4),F(0)),Z),((F(4),F(0)),O)):
 v=[projected(q,v0,v1,'alice') for q in basis];target=[[Z for _ in range(20)] for _ in range(20)]
 for wt,q in zip(weights,v):outer(target,wt,q)
 actual=[[Z for _ in range(20)] for _ in range(20)]
 Y=combine((O,v[4]),(neg(v1),v[5]))
 for z in roots:
  q=combine((O,v[0]),(scale(z,F(2)),v[2]),(scale(conj(z),F(1,2)),Y),
            (scale(mul(mul(z,z),v0),F(1,4)),v[5]))
  assert rank2(q,4,5);outer(actual,F(1,4),q)
 U0=v0[0]**2+v0[1]**2;U1=v1[0]**2+v1[1]**2;t=(O,neg(v1))
 H=[[add((F(1)-U0/16 if i==j==1 else F(1) if i==j else F(0),F(0)),
         neg(scale(mul(t[i],conj(t[j])),F(1,4)))) for j in range(2)] for i in range(2)]
 for i,left in enumerate((v[4],v[5])):
  for j,right in enumerate((v[4],v[5])):cross(actual,H[i][j],left,right)
 for i,(wt,q) in enumerate(zip(weights,v)):
  if i not in {0,2,4,5}:
   assert rank2(q,4,5);outer(actual,wt,q)
 assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
 pt=[[target[5*(i//5)+j%5][5*(j//5)+i%5] for j in range(20)] for i in range(20)]
 assert psd(pt) is not None
 gram=psd(H);assert (gram is not None)==(3*U0+16*U1<=48)
 vb=[projected(q,v0,v1,'bob') for q in basis];tb=[[Z for _ in range(20)] for _ in range(20)]
 for wt,q in zip(weights,vb):outer(tb,wt,q)
 assert tb==[[target[5*(i%4)+i//4][5*(j%4)+j//4] for j in range(20)] for i in range(20)]
 ptb=[[tb[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(20)] for i in range(20)]
 assert psd(ptb) is not None
 cases.append({'v0':list(map(str,v0)),'v1':list(map(str,v1)),'gram_pivots':gram,
               'alice_pt_rank':len(psd(pt)),'bob_pt_rank':len(psd(ptb)),'entries_per_output':400})
print(json.dumps({'cases':cases,'source_trace':24,'rank2_phase_vectors':16,'alice_bob_outputs':8,
 'total_entries_checked':3200,'previous_checker_sha256':expected,'previous_coordinate_cases_replayed':10},indent=2))
