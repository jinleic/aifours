# Independent exact replay: two actual boxes, one common numerator, and a
# non-Hurwitz corner of their coefficientwise interval hull.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-two-box-shared-numerator-unstable-hull-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='975116cd772e0bc86123d1f647fd56d8a19b15a11fca657e245c41d0a2769574':raise ValueError('PIN')
f=json.loads(raw);boxes=[(list(map(F,z['lower'])),list(map(F,z['upper']))) for z in f['boxes']];b=list(map(F,f['b']))
if len(boxes)!=2 or len(b)!=8 or b[7]!=1 or not all(x>0 for x in b):raise ValueError('INPUT')
for lo,hi in boxes:
 if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
def det(A):
 n=len(A);den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];prev=1;sgn=1
 for k in range(n-1):
  if not M[k][k]:
   q=next((i for i in range(k+1,n) if M[i][k]),None)
   if q is None:return F(0)
   M[q],M[k]=M[k],M[q];sgn=-sgn
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=M[i][j]*pivot-M[i][k]*M[k][j]
    if z%prev:raise ValueError('BAREISS')
    M[i][j]=z//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return F(sgn*M[-1][-1],den**n)
def H(a):return [[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]];p=mul(e(a),e(b))+[F(0)]
 for i,v in enumerate(mul(o(a),o(b))):p[i+1]+=v
 return p
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;v=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
allcorners=[a for lo,hi in boxes for a in corners(lo,hi)];count=0;minimum=None;counts=[]
for ci,a in enumerate(allcorners):
 h=H(a)
 for n in range(1,8):
  if det([row[:n] for row in h[:n]])<=0:raise ValueError('HURWITZ')
  count+=1
 p=pairing(a,b);last=F(0);c=0
 for l,r in sorted(f['frequency_leaves'][ci],key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER')
  beta=leaf(p,l,r)
  if not all(v>0 for v in beta):raise ValueError('SIGN')
  minimum=min(beta) if minimum is None else min(minimum,min(beta));c+=len(beta);last=r
 if last!=1:raise ValueError('COVER')
 counts.append(c)
if minimum!=F(f['common_compactified_margin']):raise ValueError('MARGIN')
lo=[min(z[0][j] for z in boxes) for j in range(7)];hi=[max(z[1][j] for z in boxes) for j in range(7)]
if list(map(str,lo))!=f['hull_lower'] or list(map(str,hi))!=f['hull_upper'] or 1+sum(hi)!=F(f['coefficient_sum_bound']):raise ValueError('HULL')
a=corners(lo,hi)[f['hull_unstable_corner_index']]
if list(map(str,a))!=f['hull_corner']:raise ValueError('HULL_CORNER')
h=H(a);minor=det([row[:6] for row in h[:6]])
if minor!=F(f['hull_sixth_hurwitz_minor']) or minor>=0:raise ValueError('NONHURWITZ')
print('independent shared-numerator hull replay:',{'boxes':2,'strict_hurwitz_minors':count,'positive_bernstein_coefficients':counts,'minimum':str(minimum),'interval_hull_sixth_minor':str(minor),'scope':'one b works both boxes and their convex hull; independent coefficientwise interval hull is not Hurwitz'})
