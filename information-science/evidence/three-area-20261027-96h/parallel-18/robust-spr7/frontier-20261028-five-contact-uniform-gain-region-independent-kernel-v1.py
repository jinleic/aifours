# Standalone exact replay of a two-parameter uniform-gain certificate.
# Cramer entries have bidegree <=2; boundary pairings bidegree <=3 in each
# parameter, so 4x4 exact interpolation determines every polynomial.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb,lcm
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-five-contact-uniform-gain-region-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='a27225c9497833060eb442f8435aa61eae12ddf155e7ee4c4ad8308c0cda0f71':raise ValueError('HASH')
d=json.loads(raw);l0,l1=map(Q,d['lambda_interval']);v0,v1=map(Q,d['v_interval']);u=Q(d['u']);nodes=[Q(x) for x in d['contacts']]
if not(l0<l1 and v0<v1 and u==Q(1,2) and nodes==[Q(1),Q(2),Q(3),Q(6),Q(8)]):raise ValueError('REGION')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def rootpoly(roots,scale):
 out=[Q(1)]
 for r in roots:out=mul(out,[-r,Q(1)])
 return [-scale*v for v in out]
def boundary(lam,v):
 t1,t2,t3,t4,t5=nodes;E0=rootpoly([u,t3,t4],lam);E1=rootpoly([t1,t2,t5],Q(1));O0=rootpoly([t1,t4,t5],Q(1));O1=rootpoly([t2,t3,v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]
for lam in (l0,l1):
 for v in (v0,v1):boundary(lam,v)
contacts=[(2,nodes[0]),(3,nodes[1]),(1,nodes[2]),(0,nodes[3]),(2,nodes[4])]
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
def tleaf(poly,left,right):
 n=len(poly)-1;vals=[poly[j]/comb(n,j) for j in range(n+1)];l=Q(0);r=Q(1)
 for depth in range(80):
  if l==left and r==right:return vals
  mid=(l+r)/2;L,R=split(vals)
  if right<=mid:r=mid;vals=L
  elif left>=mid:l=mid;vals=R
  else:raise ValueError('NON_DYADIC_LEAF')
 raise ValueError('LEAF_DEPTH')
leaves=[[(Q(l),Q(r)) for l,r in arr] for arr in d['frequency_leaves']]
for arr in leaves:
 at=Q(0)
 for l,r in sorted(arr):
  if l!=at or not l<r:raise ValueError('LEAF_COVER')
  at=r
 if at!=1:raise ValueError('LEAF_COVER')

def sample(lam,v):
 a=boundary(lam,v);rows=[]
 for ci,t in contacts:
  q=a[ci];ep=-q[2]+2*q[4]*t-3*q[6]*t*t;op=-q[3]+2*q[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in rows];rhs=[-row[0]-Q(d['gain'])*row[6]-row[7] for row in rows];D=determinant(A);sgn=d['cramer_sign']
 b=[Q(0)]*8;b[0]=sgn*D;b[6]=sgn*D*Q(d['gain']);b[7]=sgn*D
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=sgn*determinant(M)
 if any(sum(row[j]*b[j] for j in range(8)) for row in rows):raise ValueError('TANGENCY')
 vals=b[:];contactmap={i:[] for i in range(4)}
 for ci,t in contacts:contactmap[ci].append(t)
 for ci,denom in enumerate(a):
  p=pair(denom,b);q=p
  for t in contactmap[ci]:q=divide(divide(q,t),t)
  for l,r in leaves[ci]:vals.extend(tleaf(q,l,r))
 center=[sum(x[j] for x in a)/4 for j in range(8)]
 cp=pair(center,b)
 for l,r in leaves[4]:vals.extend(tleaf(cp,l,r))
 return vals

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
z=[Q(j,3) for j in range(4)];Vi=inverse([[x**k for k in range(4)] for x in z]);samples=[[sample(l0+(l1-l0)*x,v0+(v1-v0)*y) for y in z] for x in z]
n=len(samples[0][0])
if n!=d['parameter_polynomials'] or not all(len(v)==n for row in samples for v in row):raise ValueError('DIMENSION')
mins=[]
for k in range(n):
 power=[[sum(Vi[a][i]*Vi[b][j]*samples[i][j][k] for i in range(4) for j in range(4)) for b in range(4)] for a in range(4)]
 coeff=[[sum(power[a][b]*Q(comb(i,a),comb(3,a))*Q(comb(j,b),comb(3,b)) for a in range(i+1) for b in range(j+1)) for j in range(4)] for i in range(4)]
 if not all(v>0 for row in coeff for v in row):raise ValueError('PARAMETER_SIGN')
 mins.append(min(v for row in coeff for v in row))
if min(mins)!=Q(d['minimum']) or 16*n!=d['parameter_bernstein_coefficients']:raise ValueError('MINIMUM')
Smax=max(1+sum(max(a[j] for a in boundary(lam,v)) for j in range(7)) for lam in (l0,l1) for v in (v0,v1))
if Smax!=Q(d['coefficient_sum_upper']) or min(mins)/Smax**2!=Q(d['ratio_coefficient']):raise ValueError('RATIO')
print('independent uniform-gain bivariate replay:',{'parameter_rectangle':d['lambda_interval']+d['v_interval'],'boundary_width_corner_checks':4,
 'frequency_leaf_counts':[len(x) for x in leaves],'parameter_polynomials':n,'positive_parameter_bernstein_coefficients':16*n,'minimum':str(min(mins))})
