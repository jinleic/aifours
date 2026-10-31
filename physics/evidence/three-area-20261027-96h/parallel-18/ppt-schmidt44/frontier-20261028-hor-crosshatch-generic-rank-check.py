#!/usr/bin/env python3
"""Exact Q(sqrt2) full-rank and strict-PPT witness for a 4x12 local filter."""
from contextlib import redirect_stdout
from hashlib import sha256
from fractions import Fraction as F
import io,json,runpy
path='frontier-20261028-hor-crosshatch-coordinate-phase-verify.py'
expected='603aa8aef5591211fbaee1379b9cbb30f842a7ff87270e113c9513c179b9beed'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['coordinate_cuts']==495
Z,O=h['Z'],h['O'];add,mul,psd=h['add'],h['mul'],h['psd'];source=h['source']
K=((0,1,0,0,1,0,0,0,0,0,-1,1),
   (0,0,-1,0,-1,0,0,0,-1,0,0,1),
   (1,0,0,0,-1,0,0,0,0,1,0,1),
   (-1,0,0,0,0,0,1,1,0,0,0,-1))
def fac(n):return (F(n),F(0))
proj=[]
for q in source:
 v=[Z]*16
 for a in range(4):
  for b in range(4):
   for j in range(12):v[4*a+b]=add(v[4*a+b],mul(fac(K[b][j]),q[12*a+j]))
 proj.append(v)
rho=[[Z for _ in range(16)] for _ in range(16)]
for q in proj:
 for i,x in enumerate(q):
  for j,y in enumerate(q):rho[i][j]=add(rho[i][j],mul(x,y))
pt=[[rho[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
rp=psd(rho);pp=psd(pt);assert rp is not None and pp is not None and len(rp)==len(pp)==16
rd=O;pd=O
for x in rp:rd=mul(rd,x)
for x in pp:pd=mul(pd,x)
trace=Z
for i in range(16):trace=add(trace,rho[i][i])
print(json.dumps({'filter_matrix':K,'state_positive_pivots':len(rp),'pt_positive_pivots':len(pp),
 'state_determinant_Qsqrt2':list(map(str,rd)),'pt_determinant_Qsqrt2':list(map(str,pd)),
 'trace_Qsqrt2':list(map(str,trace)),'source_coordinate_certificates_replayed':495,
 'limits':'Full-rank strictly PPT output is NOT a proof of its Schmidt number.'},indent=2))
