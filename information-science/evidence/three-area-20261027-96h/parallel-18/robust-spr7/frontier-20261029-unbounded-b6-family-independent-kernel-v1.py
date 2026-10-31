# Independent symbolic replay using exact Laurent arithmetic, recursive
# determinants, parity convolution and sign coefficients in R=100+u.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-unbounded-b6-family-signs-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='e595395eed59d1dd26d223b1997a2e42f57f41c47bdc5ca9e7e881b979071bb9'
z=json.loads(raw)
class P:
 def __init__(self,x=0):
  if isinstance(x,P):self.d=x.d.copy()
  elif isinstance(x,dict):self.d={int(k):F(v) for k,v in x.items() if v}
  else:self.d={} if x==0 else {0:F(x)}
 def __add__(self,y):
  y=P(y);a=self.d.copy()
  for k,v in y.d.items():a[k]=a.get(k,F(0))+v
  return P(a)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,y):return self+-P(y)
 def __rsub__(self,y):return P(y)+-self
 def __mul__(self,y):
  y=P(y);a={}
  for k,v in self.d.items():
   for l,w in y.d.items():a[k+l]=a.get(k+l,F(0))+v*w
  return P(a)
 __rmul__=__mul__
 def __truediv__(self,y):return self*F(1,y)
 def __pow__(self,k):
  if k<0:
   assert len(self.d)==1
   (i,a),=self.d.items();return P({i*k:a**k})
  q=P(1)
  for _ in range(k):q=q*self
  return q

def determinant(A):
 n=len(A)
 if n==1:return A[0][0]
 s=P()
 for j in range(n):
  sub=[row[:j]+row[j+1:] for row in A[1:]]
  s=s+((-1)**j)*A[0][j]*determinant(sub)
 return s

def mul_t(a,b):
 out=[P() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return out

def cubic(a,b,c,scale=1):
 q=[P(-scale)]
 for t in (a,b,c):q=mul_t(q,[-P(t),P(1)])
 return q
R=P({1:1});one=P(1);L=R*R/5;rho=one-R**-4
Em=cubic(F(1,20),R,R+1,F(1001,1000));Ep=cubic(1,F(3,2),L)
Om=cubic(1,R+1,L);Op=cubic(F(3,2),R,L+1)
base_lo=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]]
base_hi=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]]
lo=[(base_lo[j]+base_hi[j]-rho*(base_hi[j]-base_lo[j]))/2 for j in range(7)]
hi=[(base_lo[j]+base_hi[j]+rho*(base_hi[j]-base_lo[j]))/2 for j in range(7)]
def corners(lo,hi):
 return [[(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[one] for e in (-1,1) for o in (-1,1)]
actual=corners(lo,hi);boundary=corners(base_lo,base_hi)
def evpart(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t*t*t

def odpart(a,t):return a[1]-a[3]*t+a[5]*t*t-a[7]*t*t*t

def atomrow(a,t):
 E=evpart(a,t);O=odpart(a,t)
 return [E*(-t)**(j//2) if j%2==0 else t*O*(-t)**((j-1)//2) for j in range(8)]
d=R**-1/10;atom_defs=[(3,F(3,2)*(one+d)),(1,R*(one+d)),(0,(R+1)*(one-d)),(0,P(F(1,3))),(0,L*F(4093,6000))]
rows=[atomrow(actual[i],t) for i,t in atom_defs];M=[[rows[i][j] for i in range(5)] for j in (1,2,3,5)]
w=[(-1)**(i+1)*determinant([[row[j] for j in range(5) if j!=i] for row in M]) for i in range(5)]
C=[sum((w[i]*rows[i][j] for i in range(5)),P()) for j in range(8)]
assert all(not C[j].d for j in (1,2,3,5));slack=C[7]+L*C[6]/4
checks={**{'w%d'%i:x for i,x in enumerate(w)},'minus_C0':-C[0],'minus_C4':-C[4],'C6':C[6],'minus_slack':-slack}
checks.update({'width%d'%j:base_hi[j]-base_lo[j] for j in range(7)})
checks.update({'lower%d'%j:base_lo[j] for j in range(7)})
cts=[(2,one),(3,P(F(3,2))),(1,R),(0,R+1),(2,L)];T=[]
for ci,t in cts:
 a=boundary[ci];Ed=-a[2]+2*a[4]*t-3*a[6]*t*t;Od=-a[3]+2*a[5]*t-3*t*t
 T.append([Ed*(-t)**(j//2) if j%2==0 else t*Od*(-t)**((j-1)//2) for j in range(8)])
A=[[row[j] for j in (2,3,4,5,6)] for row in T];h=[-(row[0]*base_hi[0]+row[1]*base_hi[1]+row[7]) for row in T];D=determinant(A);B=[P() for _ in range(8)];B[0]=base_hi[0]*D;B[1]=base_hi[1]*D;B[7]=D
for col,j in enumerate((2,3,4,5,6)):
 Anew=[row[:] for row in A]
 for i in range(5):Anew[i][col]=h[i]
 B[j]=determinant(Anew)
assert all(not sum((T[i][j]*B[j] for j in range(8)),P()).d for i in range(5))
checks['Det']=D;checks.update({'B%d'%j:B[j] for j in range(8)})
def pairing(a,b):
 Ea=[a[0],-a[2],a[4],-a[6]];Oa=[a[1],-a[3],a[5],-a[7]];Eb=[b[0],-b[2],b[4],-b[6]];Ob=[b[1],-b[3],b[5],-b[7]]
 p=mul_t(Ea,Eb)+[P()];q=mul_t(Oa,Ob)
 for j,v in enumerate(q):p[j+1]=p[j+1]+v
 return p

def divrem(p,a):
 q=[P() for _ in range(len(p)-1)];q[-1]=p[-1]
 for j in range(len(q)-2,-1,-1):q[j]=p[j+1]+a*q[j+1]
 return q,p[0]+a*q[0]
res=[]
for ci,a in enumerate(boundary):
 p=pairing(a,B)
 for cj,t in cts:
  if cj==ci:
   p,r1=divrem(p,t);p,r2=divrem(p,t);assert not r1.d and not r2.d
 res.append(p)
for ci in (0,1):
 p=res[ci]
 for j in (0,1,2,3,5):checks['res%d_%d'%(ci,j)]=p[j]
 checks['res%d_gap'%ci]=4*p[3]*p[5]-p[4]*p[4]
for j,x in enumerate(res[2]):checks['res2_%d'%j]=x
h3=res[3][1:];q1,s1=divrem(h3,L);q2,s2=divrem(q1,L);hL=s1
# h(t)=(t-L)^2*q2(t)+s2*(t-L)+h(L).
assert not (sum((res[3][j]*L**j for j in range(1,6)),P())-L*hL).d
checks.update({'res3_0':res[3][0],'res3_Q0':q2[0],'res3_Q1':q2[1],'res3_Q2':q2[2],'res3_gap':4*q2[0]*hL-s2*s2})
assert len(checks)==z['sign_certificate_count']==53 and set(checks)==set(z['sign_polynomials'])
count=0
for name,p in checks.items():
 assert p.d;low=min(p.d);high=max(p.d);a={k-low:v for k,v in p.d.items()};degree=max(a)
 shifted=[sum(v*comb(i,j)*F(100)**(i-j) for i,v in a.items() if i>=j) for j in range(degree+1)]
 assert all(v>0 for v in shifted)
 saved=z['sign_polynomials'][name];assert saved['min_R_power']==low and saved['max_R_power']==high and list(map(str,shifted))==saved['shifted_coefficients'];count+=len(shifted)
assert count==1194
# Controls: a corrupted coefficient and an all-zero contact remainder are distinguished.
assert -F(z['sign_polynomials']['w0']['shifted_coefficients'][0])<0
print({'strict_shift_coefficients':count,'symbolic_sign_polynomials':len(checks),'exact_zero_dual_coordinates':[1,2,3,5],'boundary_tangent_identities':5,'exact_contact_divisions':10,'residual_quadratic_gaps':3,'parameter_scope':'all real R>=100','mutation_controls':1})
