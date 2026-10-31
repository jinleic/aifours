# Independent exact replay of the five-contact extreme-shape example.
# This verifies a particular tangent numerator FAILS and a different numerator
# works on the entire radial family; it is not a counterexample to SPR.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb,lcm
import json
p=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-extreme-contact-tangent-failure-frozen-v1.json')
raw=p.read_bytes()
if sha256(raw).hexdigest()!='57cc93967bbb6662300012922db5d0dfa2d3013a3ff66e11dea41facf13df130':raise ValueError('HASH')
f=json.loads(raw);nodes=list(map(F,f['contact_nodes']));u=F(f['u']);lam=F(f['lambda']);v=F(f['v']);rho=F(f['rho'])

def prodpoly(roots,scale):
 z=[-scale]
 for r in roots:
  out=[F(0)]*(len(z)+1)
  for i,x in enumerate(z):out[i]-=r*x;out[i+1]+=x
  z=out
 return z
em=prodpoly([u,nodes[2],nodes[3]],lam);ep=prodpoly([nodes[0],nodes[1],nodes[4]],F(1));om=prodpoly([nodes[0],nodes[3],nodes[4]],F(1));op=prodpoly([nodes[1],nodes[2],v],F(1))
lo=[em[0],om[0],-ep[1],-op[1],em[2],om[2],-ep[3]];hi=[ep[0],op[0],-em[1],-om[1],ep[2],op[2],-em[3]]
if list(map(str,lo))!=f['boundary_lower'] or list(map(str,hi))!=f['boundary_upper'] or not all(0<x<y for x,y in zip(lo,hi)):raise ValueError('BOUNDARY')
mid=[(x+y)/2 for x,y in zip(lo,hi)]+[F(1)]
L=[(1-rho)*mid[i]+rho*lo[i] for i in range(7)];U=[(1-rho)*mid[i]+rho*hi[i] for i in range(7)]
if list(map(str,L))!=f['actual_lower'] or list(map(str,U))!=f['actual_upper'] or not 0<=rho<1:raise ValueError('RADIAL')
def corners(l,h):
 ret=[]
 for even,odd in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(h[j] if (even if j%2==0 else odd) else l[j]) if j%4 in (0,1) else (l[j] if (even if j%2==0 else odd) else h[j]) for j in range(7)]+[F(1)])
 return ret
boundary=corners(lo,hi);actual=corners(L,U)
def determinant(A):
 n=len(A);den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];prev=1;sgn=1
 for k in range(n-1):
  if not M[k][k]:
   q=next((i for i in range(k+1,n) if M[i][k]),None)
   if q is None:return F(0)
   M[q],M[k]=M[k],M[q];sgn=-sgn
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=M[i][j]*pivot-M[i][k]*M[k][j]
    if x%prev:raise ValueError('BAREISS')
    M[i][j]=x//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return F(sgn*M[-1][-1],den**n)
minor_count=0
for a in actual:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if determinant([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
  minor_count+=1
markers=[F(0)]+nodes;expect=[(1,1),(-1,1),(-1,-1),(1,-1),(1,1),(-1,1)]
def par(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
for a in actual:
 for t,(se,so) in zip(markers,expect):
  e,o=par(a,t)
  if se*e<=0 or so*o<=0:raise ValueError('MARKERS')
 if a[6]<=0 or a[7]!=1:raise ValueError('INFINITY')
def multiply(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def pairing(a,b):
 ea=[a[0],-a[2],a[4],-a[6]];oa=[a[1],-a[3],a[5],-a[7]];eb=[b[0],-b[2],b[4],-b[6]];ob=[b[1],-b[3],b[5],-b[7]]
 x=multiply(ea,eb)+[F(0)];y=multiply(oa,ob)
 for i,z in enumerate(y):x[i+1]+=z
 while len(x)>1 and x[-1]==0:x.pop()
 return x
def val(poly,t):return sum(z*t**j for j,z in enumerate(poly))
def derivative(poly,t):return sum(j*z*t**(j-1) for j,z in enumerate(poly) if j)
def quotient(poly,r):
 out=[F(0)]*(len(poly)-1);out[-1]=poly[-1]
 for j in range(len(out)-2,-1,-1):out[j]=poly[j+1]+r*out[j+1]
 if poly[0]+r*out[0]:raise ValueError('ROOT_DIVISION')
 while len(out)>1 and out[-1]==0:out.pop()
 return out
bad=list(map(F,f['bad_numerator']));good=list(map(F,f['good_numerator']));contacts=[(int(ci),F(t)) for ci,t in f['contacts']]
if bad[0]!=1 or bad[6]!=1000 or bad[7]!=1 or not all(x>0 for x in good) or good[6]/good[7]!=F(6875,6):raise ValueError('NUMERATOR')
for ci,t in contacts:
 for b in (bad,good):
  poly=pairing(boundary[ci],b)
  if val(poly,t)!=0 or derivative(poly,t)!=0:raise ValueError('TANGENCY')
badt=F(f['bad_t']);badval=val(pairing(actual[f['bad_corner']],bad),badt)
if badval!=F(f['bad_pairing']) or badval>=0:raise ValueError('BAD_PAIRING')
def split(beta):
 levels=[beta]
 while len(levels[-1])>1:levels.append([(a+b)/2 for a,b in zip(levels[-1],levels[-1][1:])])
 return [r[0] for r in levels],[r[-1] for r in levels[::-1]]
def leaf(poly,left,right):
 n=len(poly)-1;b=[poly[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for depth in range(100):
  if l==left and r==right:return b
  h=(l+r)/2;L,R=split(b)
  if right<=h:r=h;b=L
  elif left>=h:l=h;b=R
  else:raise ValueError('LEAF_NON_DYADIC')
 raise ValueError('LEAF_DEPTH')
def check_leaves(poly,rows):
 last=F(0);minimum=None;count=0
 for l,r in sorted(rows,key=lambda row:F(row[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('LEAF_COVER')
  bb=leaf(poly,l,r)
  if not all(z>0 for z in bb):raise ValueError('LEAF_SIGN')
  minimum=min(bb) if minimum is None else min(minimum,min(bb));last=r;count+=len(bb)
 if last!=1:raise ValueError('LEAF_COVER')
 return minimum,count
counts=[]
for ci,a in enumerate(boundary):
 poly=pairing(a,good)
 for cj,t in contacts:
  if cj==ci:poly=quotient(quotient(poly,t),t)
 z,n=check_leaves(poly,f['boundary_frequency_leaves'][ci]);counts.append(n)
mm,n=check_leaves(pairing(mid,good),f['midpoint_frequency_leaves'])
if mm!=F(f['midpoint_compact_margin']):raise ValueError('MIDPOINT_MIN')
print('independent extreme-box replay:',{'hurwitz_minors':minor_count,'actual_marker_checks':len(actual)*len(markers),'bad_pairing':str(badval),'good_boundary_bernstein_coefficients':counts,'good_midpoint_coefficients':n,'good_midpoint_margin':str(mm),'all_strict_leaf_signs':True,'scope':'one actual box plus entire radial family; bad numerator is not a box counterexample'})
