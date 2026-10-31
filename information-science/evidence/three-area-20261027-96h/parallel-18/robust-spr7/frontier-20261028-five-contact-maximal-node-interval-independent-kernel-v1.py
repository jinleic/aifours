# Independent four-parameter tensor replay, one branch per call.
# Bareiss determinants, dyadic de Casteljau and monomial Vandermonde-based
# parameter transforms; all arithmetic exact. The polynomial degree proof is
# stated separately and bounds degrees (23,6,3,3).
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb,lcm
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-five-contact-maximal-node-interval-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='46abb1c91770cc14137f317efdfbc16383fa306331efd59e298627d7837cac19':raise ValueError('HASH')
d=json.loads(raw)
if d['w_interval']!=['8','18'] or d['degrees']!=[23,6,3,3] or d['clearing_u_power']!=6:raise ValueError('DOMAIN')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def rootpoly(roots,scale):
 out=[Q(1)]
 for r in roots:out=mul(out,[-r,Q(1)])
 return [-scale*v for v in out]
def boundary(u,lam,v,w):
 E0=rootpoly([u,Q(3),Q(6)],lam);E1=rootpoly([Q(1),Q(2),w],Q(1));O0=rootpoly([Q(1),Q(6),w],Q(1));O1=rootpoly([Q(2),Q(3),v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]
def determinant(A):
 den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];sign=1;prev=1;n=len(M)
 for k in range(n-1):
  if M[k][k]==0:
   r=next((r for r in range(k+1,n) if M[r][k]),None)
   if r is None:return Q(0)
   M[k],M[r]=M[r],M[k];sign=-sign
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=M[i][j]*pivot-M[i][k]*M[k][j]
    if z%prev:raise ValueError('BAREISS')
    M[i][j]=z//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return Q(sign*M[-1][-1],den**n)
def pair(a,b):
 E=lambda p:[p[0],-p[2],p[4],-p[6]];O=lambda p:[p[1],-p[3],p[5],-p[7]]
 x=mul(E(a),E(b));y=mul(O(a),O(b));out=x+[Q(0)]
 for j,v in enumerate(y):out[j+1]+=v
 return out
def divide(p,r):
 out=[Q(0)]*(len(p)-1);out[-1]=p[-1]
 for j in range(len(out)-2,-1,-1):out[j]=p[j+1]+r*out[j+1]
 if p[0]+r*out[0]!=0:raise ValueError('DIVISIBILITY')
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def split(beta):
 levels=[beta]
 while len(levels[-1])>1:levels.append([(a+b)/2 for a,b in zip(levels[-1],levels[-1][1:])])
 return [row[0] for row in levels],[row[-1] for row in levels[::-1]]
def leaf(poly,left,right):
 n=len(poly)-1;vals=[poly[j]/comb(n,j) for j in range(n+1)];l=Q(0);r=Q(1)
 for depth in range(80):
  if l==left and r==right:return vals
  mid=(l+r)/2;L,R=split(vals)
  if right<=mid:r=mid;vals=L
  elif left>=mid:l=mid;vals=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('LEAF_DEPTH')
leaves=[[(Q(l),Q(r)) for l,r in arr] for arr in d['frequency_leaves']]
for arr in leaves:
 at=Q(0)
 for l,r in sorted(arr):
  if l!=at or not l<r:raise ValueError('COVER')
  at=r
 if at!=1:raise ValueError('COVER')
def sample(branch,w,x,z,y):
 umin=(9*w-36)/(6*w+25);us=9*w/(8*w+27);umax=w/(w+1)
 u=(1-x)*umin+x*us if branch==1 else (1-x)*us+x*umax
 low=(2+3*w)/(9*u+18);high=(w+3)/(u+9) if branch==1 else w/(9*u)
 if low>high:raise ValueError('BOUNDS')
 lam=(1-z)*low+z*high;v=(1-y)*(w+2)+y*7*w/5
 den=(9*u+18)*(u+9) if branch==1 else (9*u+18)*(9*u)
 clear=((6*w+25)*(8*w+27) if branch==1 else (8*w+27)*(w+1))**6
 if den<=0 or clear<=0:raise ValueError('CLEAR')
 vertices=boundary(u,lam,v,w);contacts=[(2,Q(1)),(3,Q(2)),(1,Q(3)),(0,Q(6)),(2,w)];rows=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in rows];rhs=[-row[0]-1000*row[6]-row[7] for row in rows];D=determinant(A)
 b=[Q(0)]*8;b[0]=-D*den**3;b[6]=-1000*D*den**3;b[7]=-D*den**3
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=-determinant(M)*den**3
 if any(sum(row[j]*b[j] for j in range(8)) for row in rows):raise ValueError('TANGENCY')
 vals=b[:];groups={i:[] for i in range(4)}
 for ci,t in contacts:groups[ci].append(t)
 for ci,a in enumerate(vertices):
  P=pair(a,b)
  for t in groups[ci]:P=divide(divide(P,t),t)
  for l,r in leaves[ci]:vals.extend(leaf(P,l,r))
 center=[sum(a[j] for a in vertices)/4 for j in range(8)];P=pair(center,b)
 for l,r in leaves[4]:vals.extend(leaf(P,l,r))
 return [v*clear for v in vals]
def inverse(A):
 n=len(A);M=[[Q(v) for v in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  i=next((i for i in range(k,n) if M[i][k]),None)
  if i is None:raise ValueError('INVERSE')
  M[k],M[i]=M[i],M[k];v=M[k][k];M[k]=[x/v for x in M[k]]
  for i in range(n):
   if i!=k:
    v=M[i][k];M[i]=[x-v*y for x,y in zip(M[i],M[k])]
 return [row[n:] for row in M]
def conversion(n):
 grid=[Q(j,n) for j in range(n+1)];Vinv=inverse([[x**k for k in range(n+1)] for x in grid])
 T=[[Q(comb(i,j),comb(n,j)) if j<=i else Q(0) for j in range(n+1)] for i in range(n+1)]
 return grid,[[sum(T[i][k]*Vinv[k][j] for k in range(n+1)) for j in range(n+1)] for i in range(n+1)]
wg,Cw=conversion(23);xg,Cx=conversion(6);zg,Cz=conversion(3);yg,Cy=conversion(3)
def independent_max_node_branch(branch):
 layers=[]
 for ww in wg:
  w=Q(8)+10*ww;samples=[[[sample(branch,w,x,z,y) for y in yg] for z in zg] for x in xg];n=len(samples[0][0][0]);shape=[]
  if not all(len(v)==n for plane in samples for row in plane for v in row):raise ValueError('DIMENSION')
  for j in range(n):
   p1=[[[sum(Cx[A][i]*samples[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
   p2=[[[sum(Cz[B][b]*p1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   p3=[[[sum(Cy[C][c]*p2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   shape.extend(v for plane in p3 for row in plane for v in row)
  layers.append(shape)
 if not all(len(v)==len(layers[0]) for v in layers):raise ValueError('LAYERS')
 mins=[]
 for j in range(len(layers[0])):
  vals=[sum(Cw[k][i]*layers[i][j] for i in range(24)) for k in range(24)]
  if not all(v>0 for v in vals):raise ValueError('TENSOR_SIGN')
  mins.append(min(vals))
 frozen=d['branch1'] if branch==1 else d['branch2']
 if min(mins)!=Q(frozen['minimum']) or 24*len(mins)!=frozen['full_tensor_coefficients']:raise ValueError('MINIMUM')
 return {'branch':branch,'shape_coefficients':len(mins),'tensor_coefficients':24*len(mins),'minimum':str(min(mins)),'all_strict':True}
max_node_independent1=independent_max_node_branch(1)
print('independent maximal node interval branch1:',max_node_independent1)
