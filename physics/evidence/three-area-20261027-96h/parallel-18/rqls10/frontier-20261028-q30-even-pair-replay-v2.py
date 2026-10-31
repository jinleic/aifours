#!/usr/bin/env python3
"""Corrected Phi30 replay: compute w3 then w4=-(w0+w1+w2+w3).

The v1 replay omitted w3 from w4 and is INVALID; it is preserved unchanged.
"""
import datetime,hashlib,json,time
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
v=[];z=[1]+[0]*7
for k in range(30):
 v.append(tuple(z));u=z[7];z=[-u,z[0]-u,z[1],z[2]+u,z[3]+u,z[4]+u,z[5],z[6]-u]
assert z==[1]+[0]*7
W={}
for a in range(30):
 for b in range(a,30):
  key=tuple(v[a][i]+v[b][i] for i in range(8))
  W.setdefault(key,(a,b))
assert len(W)==451
vals=list(W);zero=(0,)*8
R=[]
for a,b in W.values():
 R.append([tuple(v[(a+6*u)%30][i]+v[(b+6*u)%30][i] for i in range(8)) for u in range(5)])
inv={tuple(r[3][i]-r[4][i] for i in range(8)):j for j,r in enumerate(R)}
assert len(inv)==451
A=[tuple(r[4][i]-r[1][i] for i in range(8)) for r in R]
B=[tuple(r[4][i]-r[2][i] for i in range(8)) for r in R]
hist=[0]*6
for b0 in range(30):
 w0=tuple(v[0][i]+v[b0][i] for i in range(8))
 r0=tuple(v[24][i]+v[(b0+24)%30][i] for i in range(8))
 t0=tuple(r0[i]-w0[i] for i in range(8));nz0=(w0!=zero)
 for i,w1 in enumerate(vals):
  q=tuple(t0[k]+A[i][k] for k in range(8));neg01=tuple(-w0[k]-w1[k] for k in range(8));n1=(w1!=zero)
  for j,w2 in enumerate(vals):
   key=tuple(q[k]+B[j][k] for k in range(8));l=inv.get(key)
   if l is None:continue
   w3=vals[l]
   w4=tuple(neg01[k]-w2[k]-w3[k] for k in range(8))
   if w4 not in W:continue
   hist[nz0+n1+(w2!=zero)+(w3!=zero)+(w4!=zero)]+=1
obj={'basis':'Phi30 polynomial','method':'exact one-equation inversion and corrected w4 membership',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.monotonic()-start,6),
 'unique_two_root_sums':len(W),'distinct_coefficient_shape_histogram':hist,
 'v1_correction':'v1 omitted w3 in w4; its histogram is INVALID'}
(P/'frontier-20261028-q30-even-pair-replay-v2.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
