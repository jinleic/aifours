# Standalone exact replay of base-node shape widths and constants for the
# four-node continuation theorem. Universal derivative bound is written.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=digest:raise ValueError('HASH:'+name)
 return json.loads(raw)
d=load('frontier-20261028-five-contact-four-node-neighborhood-frozen-v1.json','70ad5d5e8530286c301c2f8a7385c45756485c867e59967dcaa1bc1d78d4daf7')
t=load('frontier-20261028-five-contact-trivariate-gain-frozen-v1.json','e7472e4aff2f02e04e8257724886409cbdc4a3632ebd1cd0fc2e6aa055e05764')
if d['source_trivariate_frozen_sha256']!='e7472e4aff2f02e04e8257724886409cbdc4a3632ebd1cd0fc2e6aa055e05764':raise ValueError('BINDING')
ur=list(map(Q,d['shape_u']));lr=list(map(Q,d['shape_lambda']));vr=list(map(Q,d['shape_v']))
for small,full in ((ur,t['u_interval']),(lr,t['lambda_interval']),(vr,t['v_interval'])):
 a,b=map(Q,full)
 if not a<small[0]<small[1]<b:raise ValueError('SUBBOX')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def rootpoly(roots,scale):
 out=[Q(1)]
 for r in roots:out=mul(out,[-r,Q(1)])
 return [-scale*v for v in out]
def bounds(u,lam,v):
 em=rootpoly([u,Q(3),Q(6)],lam);ep=rootpoly([Q(1),Q(2),Q(8)],Q(1));om=rootpoly([Q(1),Q(6),Q(8)],Q(1));op=rootpoly([Q(2),Q(3),v],Q(1))
 lo=[em[0],om[0],-ep[1],-op[1],em[2],om[2],-ep[3]];hi=[ep[0],op[0],-em[1],-om[1],ep[2],op[2],-em[3]]
 return lo,hi
lower=[];width=[]
for u in ur:
 for lam in lr:
  for v in vr:
   lo,hi=bounds(u,lam,v);lower.extend(lo);width.extend(hi[j]-lo[j] for j in range(7))
if min(lower)!=Q(d['minimum_boundary_lower']) or min(width)!=Q(d['minimum_boundary_width']) or min(lower)<=0 or min(width)<=0:raise ValueError('WIDTH')
m=Q(t['minimum'])
if m!=Q(d['base_tensor_minimum']) or m<=1 or m/(2*Q(d['S_bound'])**2)!=Q(d['ratio_coefficient']):raise ValueError('RATIO')
if d['radius']!='(2*10^12)^(-2^(10^9+1))' or d['H']!='10^12' or d['N']!='10^9':raise ValueError('RADIUS')
if 1+20+80+60+65+12+18+2>=Q(d['S_bound']):raise ValueError('S_BOUND')
print('independent four-node base replay:',{'shape_corners':8,'minimum_lower':str(min(lower)),'minimum_width':str(min(width)),
 'source_tensor_minimum':str(m),'ratio_coefficient':d['ratio_coefficient'],'symbolic_radius_binding':True})
