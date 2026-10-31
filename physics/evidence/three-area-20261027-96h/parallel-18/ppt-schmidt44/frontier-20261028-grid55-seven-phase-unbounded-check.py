#!/usr/bin/env python3
"""Exact s=1/v1 variant for the original 5x5 grid."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid55-seven-phase-check.py'
expected='934a8fe1a9b2958458164fdf3ccb2e31b95403d9fc2a0d35dc5c42e8187a13af'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['alice_bob_outputs']==8
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2,scale=h['combine'],h['outer'],h['psd'],h['rank2'],h['scale']
basis,projected,cross=h['basis'],h['projected'],h['cross'];padd,rank2poly=h['padd'],h['rank2laurent']
weights=tuple(map(F,(1,1,1,1,1,1,1,1,2,2,1)))
def div(a,b):
 d=b[0]*b[0]+b[1]*b[1];q=mul(a,conj(b));return(q[0]/d,q[1]/d)
cases=[]
for v0,v1 in (((F(1,2),F(0)),(F(3),F(0))),((F(0),F(1,2)),(F(1),F(1))),
              (Z,O),((F(2),F(0)),(F(3),F(0)))):
 s=div(O,v1);one=add(O,neg(mul(v1,s)))
 t1=(s,one,neg(mul(v1,one)))
 t2=(Z,mul(v0,s),mul(v0,add(O,neg(scale(mul(v1,s),F(2))))))
 t3=(Z,Z,mul(mul(v0,v0),s))
 v=[projected(q,v0,v1,'alice') for q in basis];L=(v[9],v[4],v[5])
 groups=((0,v[0]),(1,v[2]),(-1,combine(*zip(t1,L))),(-2,combine(*zip(t2,L))),(-3,combine(*zip(t3,L))))
 poly=[{} for _ in range(20)]
 for degree,vector in groups:
  for i,x in enumerate(vector):
   if x!=Z:poly[i]=padd(poly[i],{degree:x})
 assert rank2poly(poly)
 target=[[Z for _ in range(20)] for _ in range(20)]
 for wt,q in zip(weights,v):outer(target,wt,q)
 actual=[[Z for _ in range(20)] for _ in range(20)]
 for _,vector in groups:outer(actual,1,vector)
 diag=(F(2),F(1),F(1));H=[]
 for i in range(3):
  row=[]
  for j in range(3):
   x=(diag[i] if i==j else F(0),F(0))
   for t in (t1,t2,t3):x=add(x,neg(mul(t[i],conj(t[j]))))
   row.append(x)
  H.append(row)
 for i,left in enumerate(L):
  for j,right in enumerate(L):cross(actual,H[i][j],left,right)
 for i,(wt,q) in enumerate(zip(weights,v)):
  if i not in {0,2,4,5,9}:
   assert rank2(q,4,5);outer(actual,wt,q)
 assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
 pt=[[target[5*(i//5)+j%5][5*(j//5)+i%5] for j in range(20)] for i in range(20)]
 assert psd(pt) is not None
 vb=[projected(q,v0,v1,'bob') for q in basis];tb=[[Z for _ in range(20)] for _ in range(20)]
 for wt,q in zip(weights,vb):outer(tb,wt,q)
 assert tb==[[target[5*(i%4)+i//4][5*(j%4)+j//4] for j in range(20)] for i in range(20)]
 ptb=[[tb[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(20)] for i in range(20)]
 assert psd(ptb) is not None
 cases.append({'v0':list(map(str,v0)),'v1':list(map(str,v1)),'s':list(map(str,s)),
  'gram_pivots':psd(H),'laurent_minors_all_zero':True,'alice_pt_rank':len(psd(pt)),
  'bob_pt_rank':len(psd(ptb)),'entries_per_output':400})
print(json.dumps({'cases':cases,'source_trace':18,'alice_bob_outputs':8,'total_entries_checked':3200,
 'previous_seven_phase_cases_replayed':True,'previous_checker_sha256':expected},indent=2))
