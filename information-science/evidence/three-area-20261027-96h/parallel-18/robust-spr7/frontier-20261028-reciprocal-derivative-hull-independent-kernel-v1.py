# Standalone exact replay: actual Vp/a6 stable, rectangular hull unstable.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def read_frozen(name,digest):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=digest:raise ValueError('HASH:'+name)
 return json.loads(raw)
f=read_frozen('frontier-20261028-five-contact-uniform-numerator-frozen-v1.json','ca236e378ba9e5d9d8686dfe5e7cbc718799edfd59ff6a21bd51104fe7723c45')
d=read_frozen('frontier-20261028-reciprocal-derivative-interval-hull-frozen-v1.json','ff50db82bd86d6fecfd28caf4ef6e7dc8d30f60cdacf5ccdd73a8d3c0f4358d3')
if d['source_five_contact_sha256']!='ca236e378ba9e5d9d8686dfe5e7cbc718799edfd59ff6a21bd51104fe7723c45':raise ValueError('SOURCE')
l0=[Q(x) for x in f['boundary_lower']];u0=[Q(x) for x in f['boundary_upper']];c=[(l0[j]+u0[j])/2 for j in range(7)];rho=Q(d['scale'])
lo=[c[j]-rho*(u0[j]-l0[j])/2 for j in range(7)];hi=[c[j]+rho*(u0[j]-l0[j])/2 for j in range(7)]
if [str(x) for x in lo]!=d['original_lower'] or [str(x) for x in hi]!=d['original_upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
def corners(lo,hi,n):
 out=[]
 for e in (0,1):
  for o in (0,1):
   a=[Q(0)]*(n+1);a[n]=Q(1)
   for j in range(0,n,2):a[j]=lo[j] if ((j//2)%2==0)==(e==0) else hi[j]
   for j in range(1,n,2):a[j]=lo[j] if ((j//2)%2==0)==(o==0) else hi[j]
   out.append(a)
 return out
def det(m):
 A=[[Q(x) for x in row] for row in m];out=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  v=A[k][k];out*=v
  for i in range(k+1,n):
   z=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=z*A[k][j]
   A[i][k]=Q(0)
 return sgn*out
def minors(a):
 n=len(a)-1;rev=a[::-1]
 def v(k):return rev[k] if 0<=k<=n else Q(0)
 return [det([[v(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
if not all(x>0 for a in corners(lo,hi,7) for x in minors(a)):raise ValueError('SEPTIC_MINORS')
vl=[Q(7-j)*lo[j]/hi[6] for j in range(6)];vu=[Q(7-j)*hi[j]/lo[6] for j in range(6)]
if [str(v) for v in vl]!=d['hull_lower'] or [str(v) for v in vu]!=d['hull_upper']:raise ValueError('HULL')
q=corners(vl,vu,6)[d['unstable_hull_corner']]
if [str(v) for v in q]!=d['unstable_hull_polynomial']:raise ValueError('HULL_CORNER')
D=minors(q)[3]
if D!=Q(d['fourth_hurwitz_minor']) or D>=0:raise ValueError('HULL_MINOR')
# q0 attains its lower bound only with a0=lo0,a6=hi6; q2 attains its
# upper bound only with a2=hi2,a6=lo6. Strict lo6<hi6 makes these incompatible.
if q[0]!=7*lo[0]/hi[6] or q[2]!=5*hi[2]/lo[6] or not 0<lo[6]<hi[6]:raise ValueError('NONATTAINABILITY')
actual=[Q(7-j)*c[j]/c[6] for j in range(6)]+[Q(1)]
if not all(v>0 for v in minors(actual)):raise ValueError('ACTUAL_CONTROL')
print('independent reciprocal-derivative hull:',{'original_corner_minors_positive':28,'hull_corner':d['unstable_hull_corner'],
 'hull_delta4':str(D),'shared_denominator_endpoint_conflict':True,'actual_center_minors_positive':6})
