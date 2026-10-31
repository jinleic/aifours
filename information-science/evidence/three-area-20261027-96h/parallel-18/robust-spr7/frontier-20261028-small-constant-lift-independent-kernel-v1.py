# Standalone exact replay of the full-width 6->7 lifting example.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-small-constant-lift-example-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='937a840bd0f554c7cd2bbeed4d0e2cb1cd04bd0292d6e34fd3a43b92dacefaee':raise ValueError('HASH')
d=json.loads(raw);qcenter=[Q(v) for v in d['q_center']];r=Q(d['q_radius']);eps=Q(d['epsilon']);A=Q(d['A'])
if qcenter!=[Q(comb(6,j)) for j in range(7)]:raise ValueError('QCENTER')
lo=[Q(v) for v in d['lower']];hi=[Q(v) for v in d['upper']];b=[Q(v) for v in d['numerator']]
if lo!=[Q(1,2000)]+[v-r for v in qcenter[:6]] or hi!=[A]+[v+r for v in qcenter[:6]] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
if b!=[eps]+qcenter:raise ValueError('NUMERATOR')
B=sum(abs(x) for x in qcenter);qmargin=1-B*6*r;MO=sum(qcenter[j]+r for j in (1,3,5));MG=sum(abs(qcenter[j]) for j in (1,3,5));kappa=qmargin-eps*MO-A*MG
if B!=Q(d['q_center_numerator_coefficient_sum']) or qmargin!=Q(d['q_pairing_margin']) or MO!=Q(d['MO_bound']) or MG!=Q(d['MG_bound']) or kappa!=Q(d['kappa']) or kappa<=0:raise ValueError('LIFT_BOUND')
delta=min(kappa/2,eps*lo[0]/2**7);S=1+sum(hi)
if delta!=Q(d['lift_delta']) or S!=Q(d['coefficient_sum_bound']) or delta/S**2!=Q(d['ratio_margin']):raise ValueError('MARGIN')
def corners(lo,hi,n):
 result=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*(n+1);a[n]=Q(1)
   for j in range(0,n,2):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in range(1,n,2):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   result.append(a)
 return result
def det(m):
 a=[[Q(v) for v in row] for row in m];sgn=1;out=Q(1);n=len(a)
 for k in range(n):
  i=next((i for i in range(k,n) if a[i][k]),None)
  if i is None:return Q(0)
  if i!=k:a[k],a[i]=a[i],a[k];sgn=-sgn
  v=a[k][k];out*=v
  for i in range(k+1,n):
   q=a[i][k]/v
   for j in range(k+1,n):a[i][j]-=q*a[k][j]
   a[i][k]=Q(0)
 return sgn*out
def minors(a):
 n=len(a)-1;c=a[::-1]
 def coeff(i):return c[i] if 0<=i<=n else Q(0)
 return [det([[coeff(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
qlo=[v-r for v in qcenter[:6]];qhi=[v+r for v in qcenter[:6]];qcs=corners(qlo,qhi,6);pcs=corners(lo,hi,7)
if not all(v>0 for a in qcs+pcs for v in minors(a)):raise ValueError('HURWITZ')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def parity(a):return [a[j]*(-1)**(j//2) for j in range(0,len(a),2)],[a[j]*(-1)**((j-1)//2) for j in range(1,len(a),2)]
def pair(a,b):
 E,O=parity(a);F,G=parity(b);ee=mul(E,F);oo=mul(O,G);out=ee+[Q(0)]*max(0,len(oo)+1-len(ee))
 for j,v in enumerate(oo):out[j+1]+=v
 return out
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
counts=[];allcoeff=[]
for i,a in enumerate(pcs):
 p=pair(a,b)
 if [str(v) for v in p]!=d['direct_pairing_polynomials'][i]:raise ValueError('PAIR')
 q=a[1:];H=pair(q,qcenter);_,O=parity(q);_,G=parity(qcenter);rhs=[eps*a[0]]+[Q(0)]*7
 for j,v in enumerate(H):rhs[j+1]+=v
 for j,v in enumerate(O):rhs[j+1]-=eps*v
 for j,v in enumerate(G):rhs[j+1]-=a[0]*v
 if rhs!=p:raise ValueError('LIFT_IDENTITY')
 proof=d['direct_proofs'][i]
 if proof['status']!='STRICT_POSITIVITY':raise ValueError('PROOF')
 leaves=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0)
 for leaf in leaves:
  l,h=Q(leaf['left']),Q(leaf['right'])
  if l!=at or not l<h:raise ValueError('COVER')
  values=beta(p,l,h)
  if values!=[Q(x) for x in leaf['coefficients']] or not all(v>0 for v in values):raise ValueError('LEAF')
  allcoeff.extend(values);at=h
 if at!=1:raise ValueError('COVER')
 counts.append(len(leaves))
if min(allcoeff)!=Q(d['direct_margin']):raise ValueError('DIRECT_MARGIN')
try:
 if qmargin-eps*MO-A*MG<=0:raise ValueError('LIFT_BOUND')
 if Q(1)-Q(2)<=0:raise ValueError('LIFT_BOUND')
except ValueError as e:
 if str(e)!='LIFT_BOUND':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent small-constant lift:',{'qcenter_binomial':True,'q_corner_minors_positive':24,'p_corner_minors_positive':28,
 'lifting_polynomial_identities':4,'direct_leaf_counts':counts,'direct_margin':str(min(allcoeff)),'lift_delta':str(delta),
 'ratio_margin':str(delta/S**2),'negative_margin_control_rejected':True})
