# Standalone exact replay of the no-inversion finite-grid dual example.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=digest:raise ValueError('HASH:'+name)
 return json.loads(raw)
d=load('frontier-20261028-parity-band-dual-example-frozen-v1.json','71b05ba27638705787c6a7e5d77534f1f77b634ed42e3411a3ffaa1c7d255b17')
f=load('frontier-20261028-five-contact-uniform-numerator-frozen-v1.json','ca236e378ba9e5d9d8686dfe5e7cbc718799edfd59ff6a21bd51104fe7723c45')
lo1=[Q(x) for x in f['boundary_lower']];hi1=[Q(x) for x in f['boundary_upper']];c=[(lo1[j]+hi1[j])/2 for j in range(7)]+[Q(1)];rho=Q(d['scale'])
lo=[c[j]-rho*(hi1[j]-lo1[j])/2 for j in range(7)];hi=[c[j]+rho*(hi1[j]-lo1[j])/2 for j in range(7)]
if [str(x) for x in lo]!=d['lower'] or [str(x) for x in hi]!=d['upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
def parity(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
cs=corners(lo,hi)
for t,sgn in [(Q(1),(-1,1)),(Q(2),(-1,-1)),(Q(3),(1,-1)),(Q(6),(1,1)),(Q(8),(-1,1)),(Q(11),(-1,-1))]:
 if not all(sgn[0]*e>0 and sgn[1]*o>0 for e,o in (parity(a,t) for a in cs)):raise ValueError('BAND_MARKER')
def det(m):
 A=[[Q(v) for v in row] for row in m];ans=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  v=A[k][k];ans*=v
  for i in range(k+1,n):
   q=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=q*A[k][j]
   A[i][k]=Q(0)
 return sgn*ans
def minors(a):
 a=a[::-1]
 def c(k):return a[k] if 0<=k<8 else Q(0)
 return [det([[c(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
if not all(v>0 for a in cs for v in minors(a)):raise ValueError('HURWITZ')
def prod(roots):
 out=[Q(1)]
 for r in roots:
  a=[Q(0)]*(len(out)+1)
  for j,v in enumerate(out):a[j]+=r*v;a[j+1]+=v
  out=a
 return out
Er=[Q(x) for x in d['even_reference_roots']];Or=[Q(x) for x in d['odd_reference_roots']]
if not(0<Er[0]<1<Or[0]<2<Er[1]<3<Or[1]<6<Er[2]<8<Or[2]<11):raise ValueError('ROOT_BANDS')
E=prod(Er);O=prod(Or);b=[Q(0)]*8
for j,x in enumerate(E):b[2*j]=x
for j,x in enumerate(O):b[2*j+1]=x
if [str(x) for x in b]!=d['numerator'] or not all(x>0 for x in b):raise ValueError('NUMERATOR')
def pair(a,b,t):
 ea,oa=parity(a,t);eb,ob=parity(b,t);return ea*eb+t*oa*ob
grid=[Q(x) for x in d['grid']]
if sorted(set(Er+Or))!=grid:raise ValueError('GRID')
vals=[]
for a in cs:
 for t in grid:vals.append(pair(a,b,t)/(1+t)**7)
 vals.append(pair(a,b,Q(0)))
vals.append(b[7])
if len(vals)-1!=d['finite_atoms'] or not all(v>0 for v in vals) or min(vals)!=Q(d['minimum_normalized_pairing']):raise ValueError('GRID_PAIRING')
try:
 if not all(v>0 for v in [Q(1),Q(-1)]):raise ValueError('SIGN')
except ValueError as e:
 if str(e)!='SIGN':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent parity-band example:',{'strict_markers':6,'positive_corner_minors':28,'finite_atoms':len(vals)-1,
 'infinity_positive':b[7]>0,'minimum_normalized_pairing':str(min(vals)),'negative_control_rejected':True})
