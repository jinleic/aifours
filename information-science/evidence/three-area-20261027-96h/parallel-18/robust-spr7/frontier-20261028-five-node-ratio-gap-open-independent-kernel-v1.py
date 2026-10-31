# Independent exact interval replay for an open family satisfying the
# conditional five-frequency ratio-gap obstruction.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=pin('frontier-20261028-five-node-ratio-gap-example-frozen-v1.json','b1e9c982ce2d535ab1e4293dec6c3b59eb0edf261dcba0e5dfaa9c1b047b01ad');g=pin('frontier-20261028-five-node-ratio-gap-open-frozen-v1.json','f515cf1361578578d0c6a7f97821790b9a6226e3d06c593886a5a1cbb4815d4c')
lo=list(map(F,f['lower']));hi=list(map(F,f['upper']));eps=F(g['radius'])
if not all(0<lo[j]-eps and lo[j]+eps<hi[j]-eps for j in range(7)):raise ValueError('WIDTH')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
cs=corners(lo,hi)
def E(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3
def O(a,t):return a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
def eb(t):return eps*(1+t+t*t+t**3)
def ob(t):return eps*(1+t+t*t)
markers=list(map(F,g['markers']));signs=[[-1 if x=='-' else 1 for x in p] for p in g['marker_signs']]
for t,(se,so) in zip(markers,signs):
 for a in cs:
  if se*E(a,t)<=eb(t) or so*O(a,t)<=ob(t):raise ValueError('MARKER_MARGIN')
for ci,typ,t,sign in g['root_side_checks']:
 t=F(t);v=E(cs[ci],t) if typ=='E' else O(cs[ci],t);d=eb(t) if typ=='E' else ob(t)
 if sign*v<=d:raise ValueError('ROOT_SIDE_MARGIN')
pts=list(map(F,g['sample_points']));ids=[3,3,0,0];ranges=[]
for ci,t in zip(ids,pts):
 e=E(cs[ci],t);o=O(cs[ci],t);n=t*abs(o);d=abs(e);dn=t*ob(t);dd=eb(t)
 if e*o>=0 or n<=dn or d<=dd:raise ValueError('RATIO_PHASE')
 ranges.append(((n-dn)/(d+dd),(n+dn)/(d-dd)))
if [[str(a),str(b)] for a,b in ranges]!=g['ratio_intervals']:raise ValueError('RATIO_INTERVAL')
if not(ranges[0][1]<ranges[1][0] and ranges[0][1]<ranges[3][0] and ranges[2][1]<ranges[3][0]):raise ValueError('RATIO_GAPS')
print('open ratio-gap independent replay:',{'endpoint_radius':str(eps),'endpoint_dimensions':14,'strict_marker_corner_signs':40,'strict_root_side_guards':4,'ratio_intervals':len(ranges),'strict_gap_comparisons':3,'scope':'every box in the endpoint cube is stable and satisfies the conditional >=6-positive-frequency certificate obstruction'})
