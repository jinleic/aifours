# Standalone exact replay of the maximal two-radius marker region.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-joint-parity-marker-region-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='cc85bd85b5aca4793f8a54ba6adf8240c24f1d19e2ad440212bc98ae2c6a00ee':raise ValueError('HASH')
d=json.loads(raw)
def mul(a,b):
 v=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return v
nom=[Q(2),Q(1)]
for a,w in ((1,3),(2,7),(1,13)):nom=mul(nom,[Q(a*a+w*w),Q(2*a),Q(1)])
if [str(v) for v in nom]!=d['nominal']:raise ValueError('NOMINAL')
sl=[Q(v) for v in d['seed_lower']];sh=[Q(v) for v in d['seed_upper']]
if not all(0<sl[j]<nom[j]<sh[j] for j in range(7)):raise ValueError('SEED')
re=Q(d['even_scale_max']);ro=Q(d['odd_scale_max']);lo=[nom[j]-(re if j%2==0 else ro)*(nom[j]-sl[j]) for j in range(7)];hi=[nom[j]+(re if j%2==0 else ro)*(sh[j]-nom[j]) for j in range(7)]
if [str(v) for v in lo]!=d['outer_lower'] or [str(v) for v in hi]!=d['outer_upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('OUTER')
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
def oe(lo,hi,t):return [lo[0]-hi[2]*t+lo[4]*t*t-hi[6]*t**3,hi[0]-lo[2]*t+hi[4]*t*t-lo[6]*t**3,lo[1]-hi[3]*t+lo[5]*t*t-t**3,hi[1]-lo[3]*t+hi[5]*t*t-t**3]
markers=d['markers']
if len(markers)!=5:raise ValueError('MARKER_COUNT')
for i,m in enumerate(markers):
 t=Q(m['t']);v0=oe(nom[:7],nom[:7],t);v1=oe(lo,hi,t)
 for idx,sign in m['requirements']:
  if sign*v0[idx]<=0:raise ValueError('NOMINAL_MARKER')
  if i<4 and sign*v1[idx]<=0:raise ValueError('OUTER_MARKER')
  if i==4 and sign*v1[idx]!=0:raise ValueError('CONTACT_MARKER')
t=Q(d['boundary_contact_t']);cs=corners(lo,hi)
if t!=Q(markers[-1]['t']) or d['boundary_contact_corner']!=2 or oe(lo,hi,t)[1]!=0 or oe(lo,hi,t)[2]!=0:raise ValueError('CONTACT')
def routh(a):
 rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
 for k in range(6):
  up,cur=rows[-2:]
  if cur[0]<=0:raise ValueError('ROUTH')
  rows.append([(cur[0]*up[j+1]-up[0]*cur[j+1])/cur[0] for j in range(3)]+[Q(0)])
 if not all(r[0]>0 for r in rows):raise ValueError('ROUTH')
 return [r[0] for r in rows]
routh(nom)
b=[Q(v) for v in d['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(v>0 for v in b):raise ValueError('NUMERATOR')
def pair(a,b):
 E=lambda p:[p[0],-p[2],p[4],-p[6]];O=lambda p:[p[1],-p[3],p[5],-p[7]]
 out=mul(E(a),E(b))+[Q(0)]
 for j,v in enumerate(mul(O(a),O(b))):out[j+1]+=v
 return out
def factor(p,res,roots):
 z=res
 for r in roots:z=mul(z,[r*r,-2*r,Q(1)])
 if z!=p:raise ValueError('FACTOR')
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
 l,h=Q(item['left']),Q(item['right'])
 if not 0<=l<h<=1:raise ValueError('LEAF_RANGE')
 v=beta(poly,l,h)
 if v!=[Q(x) for x in item['coefficients']]:raise ValueError('LEAF_MISMATCH')
 if not all(x>0 for x in v):raise ValueError('LEAF_SIGN')
 return v
def cover(poly,proof,status):
 if proof['status']!=status:raise ValueError('STATUS')
 arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
 for item in arr:
  if Q(item['left'])!=at:raise ValueError('COVER')
  values.extend(leaf(poly,item));at=Q(item['right'])
 if at!=1:raise ValueError('COVER')
 return len(arr),values
counts=[]
for i,a in enumerate(cs):
 p=pair(a,b)
 if [str(v) for v in p]!=d['boundary_polynomials'][i]:raise ValueError('BOUNDARY_PAIR')
 res=[Q(v) for v in d['boundary_residuals'][i]];factor(p,res,[Q(v) for v in d['boundary_square_factors'][i]])
 n,_=cover(res,d['boundary_proofs'][i],'NONNEGATIVE_PROVED');counts.append(n)
cp=pair(nom,b)
if [str(v) for v in cp]!=d['center_polynomial']:raise ValueError('CENTER_PAIR')
count,vals=cover(cp,d['center_proof'],'STRICT_POSITIVITY');delta=min(vals);S=1+sum(hi)
if delta!=Q(d['center_margin']) or S!=Q(d['S_outer']) or delta/S**2!=Q(d['ratio_coefficient']):raise ValueError('MARGINS')
controls=[]
def reject(label,reason,f):
 try:f()
 except ValueError as e:
  if str(e)!=reason:raise ValueError('CONTROL_WRONG:'+label)
  controls.append(label);return
 raise ValueError('CONTROL_ACCEPTED:'+label)
fault=deepcopy(d['boundary_proofs'][0]['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
reject('leaf','LEAF_MISMATCH',lambda:leaf([Q(v) for v in d['boundary_residuals'][0]],fault))
rr=[Q(v) for v in d['boundary_residuals'][2]];rr[0]+=1
reject('factor','FACTOR',lambda:factor(pair(cs[2],b),rr,[t]))
print('independent joint-radius region:',{'strict_nominal_markers':10,'strict_outer_markers':8,'zero_binding_markers':2,
 'contact':str(t),'reference_routh_positive':True,'boundary_leaf_counts':counts,'center_leaves':count,'center_margin':str(delta),
 'S_outer':str(S),'ratio_coefficient':str(delta/S**2),'rejected_mutations':controls})
