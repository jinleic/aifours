#!/usr/bin/env python3
"""Exact Q(sqrt2) source-wide spectral pencil for a 4x4 CES projector."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-hor-crosshatch-coordinate-phase-verify.py'
expected='603aa8aef5591211fbaee1379b9cbb30f842a7ff87270e113c9513c179b9beed'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['coordinate_cuts']==495
Z=h['Z'];add,neg,mul,psd=h['add'],h['neg'],h['mul'],h['psd'];source=h['source']
def fac(x):return (F(x),F(0))
def ket(*terms):
 v=[F(0)]*16
 for a,b,c in terms:v[4*a+b]+=F(c)
 return v
a=ket((0,0,1),(1,1,1),(2,2,1),(3,3,1))
d=ket((0,0,1),(1,1,5),(2,2,-9),(3,3,3))
u=ket((0,1,1),(1,2,1),(2,3,1));l=ket((1,0,1),(2,1,1),(3,2,1))
P=[[F(0) for _ in range(16)] for _ in range(16)]
for weight,v in ((F(1,4),a),(F(1,116),d),(F(1,3),u),(F(1,3),l)):
 for i,x in enumerate(v):
  for j,y in enumerate(v):P[i][j]+=weight*x*y
assert all(sum(P[i][k]*P[k][j] for k in range(16))==P[i][j] for i in range(16) for j in range(16))
q=ket((1,1,5),(2,2,-9));overlap=sum(q[i]*P[i][j]*q[j] for i in range(16) for j in range(16));norm=sum(x*x for x in q)
lower=overlap/norm;assert lower==F(2925,3074) and lower>F(3,5)
PT=[[P[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
x=ket((1,3,1),(2,2,2),(3,1,1));ptval=sum(x[i]*(F(int(i==j))-PT[i][j])*x[j] for i in range(16) for j in range(16));assert ptval<0
G=[[Z for _ in range(48)] for _ in range(48)];H=[[Z for _ in range(48)] for _ in range(48)]
for qsrc in source:
 nonzero=[(a,j,qsrc[12*a+j]) for a in range(4) for j in range(12) if qsrc[12*a+j]!=Z]
 for ai,j,x in nonzero:
  for aj,k,y in nonzero:
   xy=mul(x,y)
   for b in range(4):
    for c in range(4):
     r=12*b+j;t=12*c+k
     if ai==aj and b==c:G[r][t]=add(G[r][t],xy)
     if P[4*ai+b][4*aj+c]:H[r][t]=add(H[r][t],mul(xy,fac(P[4*ai+b][4*aj+c])))
D=[[add(mul(fac(3),G[i][j]),neg(mul(fac(5),H[i][j]))) for j in range(48)] for i in range(48)]
piv=psd(D);assert piv is not None and len(piv)==48
print(json.dumps({'source_filter_variable_dimension':48,'strict_pencil_positive_pivots':len(piv),
 'source_overlap_upper':'3/5','rank2_test_overlap':str(lower),'non_copositive_I_minus_P_test':str(ptval),
 'source_coordinate_certificates_replayed':495,'source_checker_sha256':expected,
 'limits':'Exact source-wide bound for Bob filters only; no assertion about arbitrary Alice filters or all PPT states.'},indent=2))
