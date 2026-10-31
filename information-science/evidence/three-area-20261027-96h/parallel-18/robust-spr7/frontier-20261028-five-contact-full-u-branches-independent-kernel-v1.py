# Standalone exact replay of both full admissible u branches.
# Cramer numerator is cleared by d(u)^3; bidegree reasoning gives parameter
# degree <=(6,3,3). Independent Bareiss, frequency de Casteljau and monomial
# Vandermonde -> Bernstein conversion are used throughout.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb,lcm
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-five-contact-full-u-branches-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='64902389e1915aec3218a28ada0e0d9ff791f12ecbcecf0468f44fe144aac81c':raise ValueError('HASH')
d=json.loads(raw);nodes=[Q(x) for x in d['contacts']];gain=Q(d['gain']);v0,v1=map(Q,d['v_interval'])
if nodes!=[Q(1),Q(2),Q(3),Q(6),Q(8)] or gain!=1000 or v0!=10 or v1!=Q(56,5):raise ValueError('INPUT')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def rootpoly(roots,scale):
 out=[Q(1)]
 for r in roots:out=mul(out,[-r,Q(1)])
 return [-scale*v for v in out]
def boundary(u,lam,v):
 t1,t2,t3,t4,t5=nodes;E0=rootpoly([u,t3,t4],lam);E1=rootpoly([t1,t2,t5],Q(1));O0=rootpoly([t1,t4,t5],Q(1));O1=rootpoly([t2,t3,v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)):raise ValueError('WIDTH')
 if not any(lo[j]<hi[j] for j in (0,2,4,6)) or not any(lo[j]<hi[j] for j in (1,3,5)):raise ValueError('PARITY_COLLAPSE')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]
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
def leaf(poly,left,right):
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
  if l!=at or not l<r:raise ValueError('COVER')
  at=r
 if at!=1:raise ValueError('COVER')
def sample(branch,u,z,v):
 low=Q(26)/(9*u+18)
 if branch==1:high=Q(11)/(u+9);den=(9*u+18)*(u+9)
 elif branch==2:high=Q(8)/(9*u);den=(9*u+18)*(9*u)
 else:raise ValueError('BRANCH')
 if low>high or den<=0:raise ValueError('LAMBDA_BOUNDS')
 lam=(1-z)*low+z*high;vertices=boundary(u,lam,v);rows=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in rows];rhs=[-row[0]-gain*row[6]-row[7] for row in rows];D=determinant(A);sgn=d['cramer_sign']
 b=[Q(0)]*8;b[0]=sgn*D*den**3;b[6]=sgn*D*den**3*gain;b[7]=sgn*D*den**3
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=sgn*determinant(M)*den**3
 if any(sum(row[j]*b[j] for j in range(8)) for row in rows):raise ValueError('TANGENCY')
 vals=b[:];mapping={i:[] for i in range(4)}
 for ci,t in contacts:mapping[ci].append(t)
 for ci,a in enumerate(vertices):
  P=pair(a,b)
  for t in mapping[ci]:P=divide(divide(P,t),t)
  for l,r in leaves[ci]:vals.extend(leaf(P,l,r))
 center=[sum(a[j] for a in vertices)/4 for j in range(8)];P=pair(center,b)
 for l,r in leaves[4]:vals.extend(leaf(P,l,r))
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
def power_to_bernstein(deg):return [[Q(comb(i,j),comb(deg,j)) if j<=i else Q(0) for j in range(deg+1)] for i in range(deg+1)]
zu=[Q(j,6) for j in range(7)];z=[Q(j,3) for j in range(4)];Iu=inverse([[x**k for k in range(7)] for x in zu]);Iz=inverse([[x**k for k in range(4)] for x in z]);Tu=power_to_bernstein(6);T=power_to_bernstein(3)
allresults=[]
for branch in d['branches']:
 b=branch['branch'];u0,u1=map(Q,branch['u_interval']);samples=[[[sample(b,u0+(u1-u0)*x,y,v0+(v1-v0)*w) for w in z] for y in z] for x in zu]
 n=len(samples[0][0][0])
 if n!=d['parameter_polynomials'] or not all(len(x)==n for plane in samples for row in plane for x in row):raise ValueError('DIMENSION')
 mins=[]
 for k in range(n):
  p1=[[[sum(Iu[A][i]*samples[i][j][m][k] for i in range(7)) for m in range(4)] for j in range(4)] for A in range(7)]
  p2=[[[sum(Iz[B][j]*p1[A][j][m] for j in range(4)) for m in range(4)] for B in range(4)] for A in range(7)]
  p3=[[[sum(Iz[C][m]*p2[A][B][m] for m in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  q1=[[[sum(Tu[A][i]*p3[i][j][m] for i in range(7)) for m in range(4)] for j in range(4)] for A in range(7)]
  q2=[[[sum(T[B][j]*q1[A][j][m] for j in range(4)) for m in range(4)] for B in range(4)] for A in range(7)]
  q3=[[[sum(T[C][m]*q2[A][B][m] for m in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  if not all(v>0 for plane in q3 for row in plane for v in row):raise ValueError('PARAMETER_SIGN')
  mins.append(min(v for plane in q3 for row in plane for v in row))
 if min(mins)!=Q(branch['minimum']) or 112*n!=d['coefficients_per_branch']:raise ValueError('MINIMUM')
 allresults.append({'branch':b,'u_interval':branch['u_interval'],'parameter_polynomials':n,'positive_bernstein_coefficients':112*n,'minimum':str(min(mins))})
if min(Q(x['minimum']) for x in allresults)!=Q(d['uniform_minimum']) or Q(d['uniform_minimum'])/Q(d['coefficient_sum_bound'])**2!=Q(d['ratio_coefficient']):raise ValueError('RATIO')
print('independent full-u branch replay:',{'branches':allresults,'frequency_leaf_counts':[len(x) for x in leaves],
 'uniform_minimum':d['uniform_minimum'],'S_bound':d['coefficient_sum_bound'],'ratio_coefficient':d['ratio_coefficient']})
