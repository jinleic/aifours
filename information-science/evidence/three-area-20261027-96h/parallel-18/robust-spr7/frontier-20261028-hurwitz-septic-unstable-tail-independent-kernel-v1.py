# Standalone exact replay of a stable full-width septic box whose central
# sextic tail is not Hurwitz. No producer/search imports.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-hurwitz-septic-unstable-tail-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='0c275cf02ae54a1f24185ff4bc3b6732903a06160fc5dee53492d9a7692dfd7c':raise ValueError('HASH')
d=json.loads(raw)
def mul(a,b):
 v=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return v
p=[Q(1),Q(1)]
for w in (4,5,6):p=mul(p,[Q(1+w*w),Q(2),Q(1)])
if [str(v) for v in p]!=d['center'] or d['numerator']!=d['center']:raise ValueError('CENTER')
q=p[1:]
if [str(v) for v in q]!=d['tail']:raise ValueError('TAIL')
def det(m):
 A=[[Q(v) for v in row] for row in m];out=Q(1);sgn=1;n=len(A)
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
 n=len(a)-1;c=a[::-1]
 def v(i):return c[i] if 0<=i<=n else Q(0)
 return [det([[v(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
qm=minors(q)
if [str(v) for v in qm]!=d['tail_hurwitz_minors'] or qm[4]!=Q(d['tail_fifth_minor']) or qm[4]>=0:raise ValueError('TAIL_MINOR')
r=Q(d['radius']);lo=[p[j]-r for j in range(7)];hi=[p[j]+r for j in range(7)]
if [str(v) for v in lo]!=d['lower'] or [str(v) for v in hi]!=d['upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
cs=corners(lo,hi)
if not all(v>0 for a in cs for v in minors(a)):raise ValueError('CORNERS')
def pair(a,b):
 E=lambda p:[p[0],-p[2],p[4],-p[6]];O=lambda p:[p[1],-p[3],p[5],-p[7]]
 out=mul(E(a),E(b))+[Q(0)]
 for j,v in enumerate(mul(O(a),O(b))):out[j+1]+=v
 return out
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def cover(poly,proof):
 if proof['status']!='STRICT_POSITIVITY':raise ValueError('STATUS')
 arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
 for item in arr:
  l,h=Q(item['left']),Q(item['right'])
  if l!=at or not l<h:raise ValueError('COVER')
  v=beta(poly,l,h)
  if v!=[Q(x) for x in item['coefficients']] or not all(x>0 for x in v):raise ValueError('LEAF')
  values.extend(v);at=h
 if at!=1:raise ValueError('COVER')
 return len(arr),values
base=pair(p,p)
if [str(v) for v in base]!=d['base_pairing_polynomial']:raise ValueError('BASE_PAIR')
nb,values=cover(base,d['base_proof']);delta0=min(values);B=sum(abs(v) for v in p);delta=delta0-7*r*B;S=1+sum(hi)
if delta0!=Q(d['base_margin']) or B!=Q(d['B']) or delta!=Q(d['box_margin']) or delta<=0 or S!=Q(d['S']) or delta/S**2!=Q(d['ratio_margin']):raise ValueError('BOUND')
counts=[]
for i,a in enumerate(cs):
 poly=pair(a,p)
 if [str(v) for v in poly]!=d['box_pairing_polynomials'][i]:raise ValueError('BOX_PAIR')
 n,_=cover(poly,d['box_proofs'][i]);counts.append(n)
positive_control=[Q(comb(6,j)) for j in range(7)]
if not all(v>0 for v in minors(positive_control)):raise ValueError('POSITIVE_CONTROL')
print('independent unstable-tail example:',{'center_factorization':True,'tail_delta5':str(qm[4]),'box_corner_minors_positive':28,
 'base_leaf_count':nb,'box_leaf_counts':counts,'base_margin':str(delta0),'box_margin':str(delta),'ratio_margin':str(delta/S**2),
 'stable_tail_positive_control':True})
