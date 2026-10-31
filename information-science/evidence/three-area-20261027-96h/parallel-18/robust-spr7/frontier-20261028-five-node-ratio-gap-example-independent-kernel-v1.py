# Independent exact replay of a broad nondegenerate example for the
# conditional five-frequency ratio-gap obstruction. Root locations are
# certified by rational sign changes plus stable-corner interlacing.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-five-node-ratio-gap-example-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='b1e9c982ce2d535ab1e4293dec6c3b59eb0edf261dcba0e5dfaa9c1b047b01ad':raise ValueError('PIN')
f=json.loads(raw);base=list(map(F,f['base']));r=F(f['radius']);lo=[x-r for x in base];hi=[x+r for x in base]
if list(map(str,lo))!=f['lower'] or list(map(str,hi))!=f['upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOUNDS')
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
checks=[O(cs[0],F(9,50))>0,O(cs[0],F(19,100))<0,O(cs[0],F(2))>0,O(cs[0],F(100))<0,
 E(cs[0],F(0))>0,E(cs[0],F(77,100))<0,E(cs[0],F(39,50))>0,
 O(cs[1],F(0))>0,O(cs[1],F(69,50))<0,O(cs[1],F(139,100))>0,
 E(cs[2],F(0))>0,E(cs[2],F(1,5))<0,E(cs[2],F(527,100))>0,E(cs[2],F(132,25))<0]
if not all(checks):raise ValueError('ROOT_SIGNS')
pts=list(map(F,f['sample_points']));phases=[(E(cs[3],pts[0]),O(cs[3],pts[0])),(E(cs[3],pts[1]),O(cs[3],pts[1])),(E(cs[0],pts[2]),O(cs[0],pts[2])),(E(cs[0],pts[3]),O(cs[0],pts[3]))]
if not(phases[0][0]<0<phases[0][1] and phases[1][1]<0<phases[1][0] and phases[2][1]<0<phases[2][0] and phases[3][0]<0<phases[3][1]):raise ValueError('PHASE')
ratios=[-pts[i]*phases[i][1]/phases[i][0] for i in range(4)]
if list(map(str,ratios))!=f['sample_ratios'] or not(ratios[0]<ratios[1] and ratios[0]<ratios[3] and ratios[2]<ratios[3]):raise ValueError('GAPS')
print('ratio-gap example independent replay:',{'strict_hurwitz_minors':28,'rational_root_sign_checks':len(checks),'ratio_bounds':list(map(str,ratios)),'three_strict_gaps':True,'scope':'one broad box satisfies a conditional five-frequency obstruction; no claim for six or more frequencies'})
