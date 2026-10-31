#!/usr/bin/env python3
"""Gaussian-rational replay of a weighted source and mixed-kernel SR2 Gram."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid-unbounded-plane-check.py'
expected='03de2fa6e1670e2f5ab7c7906169ce8da3dcdae7ad00bc25d00a195ee0214ca3'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf): h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['cases'])==5
O,Z=h['O'],h['Z'];add,neg,mul=h['add'],h['neg'],h['mul'];conj=h['conj']
vec,combine,cross,outer=h['vec'],h['combine'],h['cross'],h['outer']
rank2,psd=h['rank2'],h['psd']
a,b,d,g,e,f,j,k,n=map(F,(1,1,2,3,9,9,9,6,7))
v0=(F(1,2),F(0));v2=(F(4),F(0));U=F(1,4);V=F(16)
assert a==b==1
C=1/e+U/j+V/k; K=F(1)
s=(-C*f*F(1,2)*K/(1+C*f*U),F(0))
assert s==(F(-202,117),F(0))
A=vec((0,0,O),(1,1,O),(2,2,O));B=vec((0,1,O),(1,2,O))
D=vec((1,0,O),(2,1,neg(O)));V_C=vec((0,2,O),(3,3,O))
E=vec((2,0,O),(3,0,v0),(3,2,v2));V_F=vec((2,0,v0),(2,2,v2))
G=vec((3,0,O));V_I=vec((3,2,O));V_H=vec((0,3,O));X=vec((2,0,O))
target=[[Z for _ in range(16)] for _ in range(16)]
for w,x in zip((a,b,d,g,e,f,j,k,n),(A,B,D,V_C,E,V_F,G,V_I,V_H)):outer(target,w,x)
actual=[[Z for _ in range(16)] for _ in range(16)]
W=combine((neg(O),X),(s,combine((O,V_F),(neg(v0),X))))
for z in h['ROOTS']:
 z2=mul(z,z);z3=mul(z2,z)
 q=combine((z,A),(O,B),(z2,D),(z3,W))
 assert rank2(q);outer(actual,F(1,4),q)
for w,x in ((d-1,D),(g,V_C),(n,V_H)):outer(actual,w,x)
t=(neg(add(O,mul(s,v0))),mul(add(O,mul(s,v0)),v0),
   mul(add(O,mul(s,v0)),v2),s)
weights=(e,j,k,f)
H=[[add((weights[i] if i==q else F(0),F(0)),neg(mul(t[i],conj(t[q]))))
    for q in range(4)] for i in range(4)]
for i,left in enumerate((E,G,V_I,V_F)):
 for q,right in enumerate((E,G,V_I,V_F)):cross(actual,H[i][q],left,right)
assert all(actual[i][q]==target[i][q] for i in range(16) for q in range(16))
actual2=[[Z for _ in range(16)] for _ in range(16)]
V_Z=vec((2,2,O));q0=combine((O,A),(neg(O),V_Z))
assert rank2(q0);outer(actual2,F(1,2),q0)
beta=(F(1),F(1));delta=(F(1),F(-1))
for z in h['ROOTS']:
 q=combine((z,A),(z,V_Z),(mul(beta,mul(z,z)),B),(delta,D))
 assert rank2(q);outer(actual2,F(1,8),q)
for w,x in ((d-1,D),(g,V_C),(n,V_H)):outer(actual2,w,x)
dv=h['div']
t2=(neg(dv(v0,v2)),dv(mul(v0,v0),v2),v0,dv(O,v2))
H2=[[add((weights[i] if i==q else F(0),F(0)),neg(mul(t2[i],conj(t2[q]))))
     for q in range(4)] for i in range(4)]
for i,left in enumerate((E,G,V_I,V_F)):
 for q,right in enumerate((E,G,V_I,V_F)):cross(actual2,H2[i][q],left,right)
assert all(actual2[i][q]==target[i][q] for i in range(16) for q in range(16))
cost2=U/(V*e)+U*U/(V*j)+U/k+F(1)/(V*f)
assert cost2==F(13,256)
pt=[[target[4*(i//4)+q%4][4*(q//4)+i%4] for q in range(16)] for i in range(16)]
def vec5(*terms):
 v=[Z]*20
 for aa,bb,c in terms:v[5*aa+bb]=add(v[5*aa+bb],c)
 return v
basis5=(vec5((0,0,O),(1,1,O),(2,2,O)),vec5((0,1,O),(1,2,O)),
 vec5((1,0,O),(2,1,neg(O))),vec5((0,2,O),(3,4,O)),
 vec5((2,0,O),(3,3,O)),vec5((2,3,O)),vec5((3,0,O)),vec5((3,2,O)),vec5((0,4,O)))
rho=[[Z for _ in range(20)] for _ in range(20)]
for w,x in zip((a,b,d,g,e,f,j,k,n),basis5):outer(rho,w,x)
pt5=[[rho[5*(i//5)+q%5][5*(q//5)+i%5] for q in range(20)] for i in range(20)]
assert psd(H) is not None and psd(H2) is not None and psd(pt) is not None and psd(pt5) is not None
print(json.dumps({'source_weights':list(map(str,(a,b,d,g,e,f,j,k,n))),'v0':'1/2','v2':'4',
  'C':str(C),'s':list(map(str,s)),'first_cost':str(C/(1+C*f*U)),'second_cost':str(cost2),
  'first_gram_pivots':psd(H),'second_gram_pivots':psd(H2),
  'projection_pt_pivots':psd(pt),'source_pt_pivots':psd(pt5),
  'rank2_phase_vectors':9,'source_pt_entries_checked':400,'projection_entries_checked_per_formula':256,
  'helper_hash':expected,'helper_cases_replayed':5},indent=2))
