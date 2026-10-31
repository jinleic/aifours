#!/usr/bin/env python3
"""Exact replay of a non-half-half optimal interpolation witness."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid-phase-interpolation-check.py'
expected='d5955daf860ccb7de7858c25d444b926ba5835505883f3ac1709f1709fdbb96a'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf): h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['cases'])==3
O,Z=h['O'],h['Z']; add,neg,mul=h['add'],h['neg'],h['mul']
vec,combine,cross,outer=h['vec'],h['combine'],h['cross'],h['outer']
padd,rank2pol,rank2,psd=h['padd'],h['rank2pol'],h['rank2'],h['psd']
v0=(F(1),F(0));v1=(F(2),F(0));v2=(F(1,10),F(0));p=F(13,44)
A=vec((0,0,O),(1,1,O),(2,2,O)); B=vec((0,1,O),(1,2,O))
D=vec((1,0,O),(2,1,neg(O)));C=vec((0,2,O),(3,3,O))
E=vec((2,0,O),(3,0,v0),(3,1,v1),(3,2,v2))
V_F=vec((2,0,v0),(2,1,v1),(2,2,v2));G=vec((3,0,O));V_I=vec((3,2,O));V_H=vec((0,3,O))
X=combine((O,E),(neg(v0),G),(neg(v2),V_I))
target=[[Z for _ in range(16)] for _ in range(16)]
for w,x in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):outer(target,w,x)
actual=[[Z for _ in range(16)] for _ in range(16)]
parts=((0,O,B),(1,O,A),(2,neg(O),D),(3,neg(O),X),(4,neg(v1),G))
assert len({k%5 for k,_,_ in parts})==5
qp=[{} for _ in range(16)]
for degree,c,b in parts:
 for j,x in enumerate(b):
  y=mul(c,x)
  if y!=Z:qp[j]=padd(qp[j],{degree:y})
assert rank2pol(qp)
for _,c,b in parts:outer(actual,p*(c[0]*c[0]+c[1]*c[1]),b)
for z in h['ROOTS']:
 z2=mul(z,z);z3=mul(z2,z)
 q=combine((z,A),(O,B),(neg(mul(z2,v1)),V_I),(neg(z3),X))
 assert rank2(q)
 outer(actual,(1-p)/4,q)
outer(actual,1-p,D)
for v in (C,V_F,V_H):outer(actual,3,v)
T=v1[0]*v1[0]+v1[1]*v1[1];t=(O,neg(v0),neg(v2))
diag=(F(3),F(3)-p*T,F(3)-(1-p)*T)
H=[[add((diag[i] if i==j else F(0),F(0)),neg(mul(t[i],h['conj'](t[j])))) for j in range(3)] for i in range(3)]
for i,left in enumerate((E,G,V_I)):
 for j,right in enumerate((E,G,V_I)):cross(actual,H[i][j],left,right)
assert all(actual[i][j]==target[i][j] for i in range(16) for j in range(16))
pt=[[target[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
assert psd(H) is not None and psd(pt) is not None
schur=F(1,3)+F(1)/diag[1]+F(1,100)/diag[2]
assert schur==F(563,600)
print(json.dumps({'previous_checker_sha256':expected,'replayed_previous_cases':3,'p':str(p),'v':['1','2','1/10'],
                  'gram_pivots':psd(H),'pt_pivots':psd(pt),'schur_sum':str(schur),
                  'state_entries_checked':256,'five_phase_minor_polynomials_zero':True,'four_phase_rank2_vectors':4},indent=2))
