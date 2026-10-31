# Independent exact replay of a broad nondegenerate example for the
# conditional five-frequency ratio-gap obstruction. Root locations are
# certified by rational sign changes plus stable-corner interlacing.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-five-node-ratio-gap-no-corner-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='ac46440c5a57f054eac084e9dce400428a4850149e2da4c01bd00044ff8572dd':raise ValueError('PIN')
f=json.loads(raw);lo=list(map(F,f['lower']));hi=list(map(F,f['upper']))
if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOUNDS')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
cs=corners(lo,hi)
def det(A):
 n=len(A);den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];prev=1;sign=1
 for k in range(n-1):
  if not M[k][k]:
   q=next((i for i in range(k+1,n) if M[i][k]),None)
   if q is None:return F(0)
   M[q],M[k]=M[k],M[q];sign=-sign
  p=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=M[i][j]*p-M[i][k]*M[k][j]
    if z%prev:raise ValueError('BAREISS')
    M[i][j]=z//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sign*M[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def E(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3
def O(a,t):return a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
# These strict sign sequences isolate the indicated root indexes, using the
# already verified simple-positive-root interlacing of the stable corners.
checks=[O(cs[0],F(40))>0,O(cs[0],F(41))<0,O(cs[0],F(300))>0,O(cs[0],F(100000))<0,
 E(cs[0],F(0))>0,E(cs[0],F(119))<0,E(cs[0],F(120))>0,
 O(cs[1],F(0))>0,O(cs[1],F(142))<0,O(cs[1],F(143))>0,
 E(cs[2],F(0))>0,E(cs[2],F(50))<0,E(cs[2],F(6679))>0,E(cs[2],F(6680))<0]
if not all(checks):raise ValueError('ROOT_SIGNS')
pts=list(map(F,f['ratio_points']));phases=[(E(cs[3],pts[0]),O(cs[3],pts[0])),(E(cs[3],pts[1]),O(cs[3],pts[1])),(E(cs[0],pts[2]),O(cs[0],pts[2])),(E(cs[0],pts[3]),O(cs[0],pts[3]))]
if not(phases[0][0]<0<phases[0][1] and phases[1][1]<0<phases[1][0] and phases[2][1]<0<phases[2][0] and phases[3][0]<0<phases[3][1]):raise ValueError('PHASE')
ratios=[-pts[i]*phases[i][1]/phases[i][0] for i in range(4)]
if list(map(str,ratios))!=f['ratios'] or not(ratios[0]<ratios[1] and ratios[0]<ratios[3] and ratios[2]<ratios[3]):raise ValueError('GAPS')

def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]];p=mul(e(a),e(b))+[F(0)]
 for i,v in enumerate(mul(o(a),o(b))):p[i+1]+=v
 return p
for item in f['corner_failures']:
 t=F(item['t']);v=sum(x*t**j for j,x in enumerate(pairing(cs[item['denominator_corner']],cs[item['numerator_corner']])))
 if v!=F(item['pairing']) or v>=0:raise ValueError('CORNER_FAILURE')
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(p,a,b):
 from math import comb
 n=len(p)-1;v=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
b=list(map(F,f['good_numerator']));minimum=None;count=0
if b[7]!=1 or not all(v>0 for v in b):raise ValueError('NUMERATOR')
for ci,a in enumerate(cs):
 p=pairing(a,b);last=F(0)
 for l,r in sorted(f['good_frequency_leaves'][ci],key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER')
  beta=leaf(p,l,r)
  if not all(x>0 for x in beta):raise ValueError('SIGN')
  minimum=min(beta) if minimum is None else min(minimum,min(beta));last=r;count+=len(beta)
 if last!=1:raise ValueError('COVER')
if minimum!=F(f['good_compactified_minimum']):raise ValueError('MARGIN')
print('nontrivial ratio-gap independent replay:',{'hurwitz_minors':28,'root_sign_checks':len(checks),'ratio_bounds':list(map(str,ratios)),'failing_corner_numerators':len(f['corner_failures']),'good_bernstein_coefficients':count,'good_margin':str(minimum),'scope':'all four corner numerators fail; a different common numerator works; ratio tests exclude five-node strict certificates conditionally'})
