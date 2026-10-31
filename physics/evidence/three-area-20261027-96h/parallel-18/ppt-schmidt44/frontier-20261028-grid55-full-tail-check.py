#!/usr/bin/env python3
"""Exact opposite tail-chart mixed phase certificate for the trace24 grid."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid55-tail-mixture-check.py'
expected='89c0f2856580ed70d8091faba221a34690a1967525d2ddca3ae4fc8510adb0a8'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['total_cases']==8
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2=h['combine'],h['outer'],h['psd'],h['rank2']
basis,weights,roots,scale=h['basis'],h['weights'],h['roots'],h['scale']
t=(F(27,125),F(0));U=F(729,15625);s=F(9,25);p=1-s
s0=F(5,4);w=F(10,3);c=F(27,250);lam=(F(48,125),F(0))
assert s**3==U and p*s0*s0==1 and s*w*w==4 and w*c==s
assert lam[0]==p*t[0]/s
# Previous checker projected K3=1,K4=r. Here K3=t,K4=1.
def projected(edges,side):
 v=[Z]*20
 for a,b in edges:
  if side=='alice':
   coeff=t if a==3 else O;aa=3 if a==4 else a;k=5*aa+b
  else:
   coeff=t if b==3 else O;bb=3 if b==4 else b;k=4*a+bb
  v[k]=add(v[k],coeff)
 return v
def cross(m,c,v,w):
 for i,x in enumerate(v):
  for j,y in enumerate(w):m[i][j]=add(m[i][j],mul(c,mul(x,conj(y))))
cases=[]
for side in ('alice','bob'):
 v=[projected(q,side) for q in basis];nr,nc=(4,5) if side=='alice' else (5,4)
 V,W,C=(2,3,6) if side=='alice' else (3,2,4)
 target=[[Z for _ in range(20)] for _ in range(20)]
 for wt,q in zip(weights,v):outer(target,wt,q)
 actual=[[Z for _ in range(20)] for _ in range(20)]
 invt=(1/t[0],F(0));qB=combine((O,v[7]),(neg(t),v[C]));qC=combine((O,v[C]),(neg(invt),v[7]))
 for z in roots:
  B=combine((O,v[0]),(neg(t),v[V]),(scale(z,s0),v[1]),(scale(conj(z),1/s0),qB))
  Q=combine((O,v[0]),(lam,v[V]),(scale(z,w),v[W]),(scale(conj(z),c),qC))
  assert rank2(B,nr,nc) and rank2(Q,nr,nc)
  outer(actual,p/4,B);outer(actual,s/4,Q)
 vcost=U*p/s;assert vcost<weights[V]
 outer(actual,weights[V]-vcost,v[V])
 coeff=p*p+s**4/(4*U);vv=(neg(t),O)
 H=[[add((F(1 if i==j else 0),F(0)),neg(scale(mul(vv[i],conj(vv[j])),coeff)))
    for j in range(2)] for i in range(2)]
 for i,left in enumerate((v[C],v[7])):
  for j,right in enumerate((v[C],v[7])):cross(actual,H[i][j],left,right)
 for i,(wt,q) in enumerate(zip(weights,v)):
  if i not in {0,1,V,W,C,7}:
   assert rank2(q,nr,nc);outer(actual,wt,q)
 assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
 pt=[[target[nc*(i//nc)+j%nc][nc*(j//nc)+i%nc] for j in range(20)] for i in range(20)]
 assert psd(H) is not None and psd(pt) is not None
 cases.append({'side':side,'gram_pivots':psd(H),'pt_rank':len(psd(pt)),
               'state_entries_checked':400,'rank2_phase_vectors':8})
print(json.dumps({'t':'27/125','s':str(s),'p':str(p),'phase_coefficients':{'s0':str(s0),'w':str(w),'c':str(c),'lambda':str(lam[0])},
 'V_cost':str(vcost),'gram_rank_one_factor':str(coeff),'cases':cases,
 'previous_mixed_tail_cases_replayed':True,'previous_checker_sha256':expected},indent=2))
