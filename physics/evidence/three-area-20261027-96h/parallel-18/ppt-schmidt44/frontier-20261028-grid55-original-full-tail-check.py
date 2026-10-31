#!/usr/bin/env python3
"""Exact all-tail theorem instance for the ORIGINAL trace18 5x5 source."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid55-full-tail-check.py'
expected='26ba57e2dc58733d94e9306bf707afd87120b4379d428ff118d323ef05bf9936'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['cases'])==2
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2=h['combine'],h['outer'],h['psd'],h['rank2']
basis,roots,scale=h['basis'],h['roots'],h['scale']
weights=tuple(map(F,(1,1,1,1,1,1,1,1,2,2,1)))
t=(F(3,4),F(0));U=F(9,16);p=F(16,25);s=1-p
s0=F(5,4);w=F(5,3);c=F(27,125);lam=(F(4,3),F(0))
assert p*s0*s0==1 and s*w*w==1 and w*c==s and lam[0]==p*t[0]/s

def projected(edges,side):
 v=[Z]*20
 for a,b in edges:
  if side=='alice':coeff=t if a==3 else O;aa=3 if a==4 else a;k=5*aa+b
  else:coeff=t if b==3 else O;bb=3 if b==4 else b;k=4*a+bb
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
 vcost=U*p/s;assert vcost==1
 coeff=p*p+s**4/U;vv=(neg(t),O)
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
print(json.dumps({'source_trace':18,'t':'3/4','p':str(p),'s':str(s),
 'phase_coefficients':{'s0':str(s0),'w':str(w),'c':str(c),'lambda':str(lam[0])},
 'V_cost':str(vcost),'gram_cost':str(coeff*(1+U)), 'cases':cases,
 'previous_weighted_full_tail_replayed':True,'previous_checker_sha256':expected},indent=2))
