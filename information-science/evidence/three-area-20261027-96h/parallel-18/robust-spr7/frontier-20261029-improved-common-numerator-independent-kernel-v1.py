# Reconstruct the improved all-parameter common numerator with exact
# Cramer determinants, residual factors, and split-frequency positivity.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('d=R**-1/10;atom_defs=',1)[0])
raw=(root/'frontier-20261029-improved-common-numerator-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='333d5b76b2bceccfcd6f2a289790ea3ed36e7a572aa55cb47ba278ab938183c9';f=json.loads(raw)
cts=[(2,one),(3,P(F(3,2))),(1,R),(0,R+1),(2,L)];T=[]
for ci,t in cts:
 a=boundary[ci];ed=-a[2]+2*a[4]*t-3*a[6]*t*t;od=-a[3]+2*a[5]*t-3*t*t
 T.append([ed*(-t)**(j//2) if j%2==0 else t*od*(-t)**((j-1)//2) for j in range(8)])
A6=[[row[j] for j in (1,2,3,4,5)] for row in T];h6=[-(row[0]+row[6]) for row in T];D6=-determinant(A6);c=[P() for _ in range(8)];c[0]=D6;c[6]=D6
for col,j in enumerate((1,2,3,4,5)):
 Q=[row[:] for row in A6]
 for i in range(5):Q[i][col]=h6[i]
 c[j]=-determinant(Q)
A7=[[row[j] for j in (2,3,4,5,6)] for row in T];h7=[-(row[0]*base_hi[0]+row[1]*base_hi[1]+row[7]) for row in T];D7=determinant(A7);b=[P() for _ in range(8)];b[0]=base_hi[0]*D7;b[1]=base_hi[1]*D7;b[7]=D7
for col,j in enumerate((2,3,4,5,6)):
 Q=[row[:] for row in A7]
 for i in range(5):Q[i][col]=h7[i]
 b[j]=determinant(Q)
I=[D6*b[j]-F(17,500)*R*R*D7*c[j] for j in range(8)];assert all(not sum((T[i][j]*I[j] for j in range(8)),P()).d for i in range(5))
def product(a,b):
 q=[P() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):q[i+j]=q[i+j]+x*y
 return q
def pairing(a,b):
 E1=[a[0],-a[2],a[4],-a[6]];O1=[a[1],-a[3],a[5],-a[7]];E2=[b[0],-b[2],b[4],-b[6]];O2=[b[1],-b[3],b[5],-b[7]];p=product(E1,E2)+[P()]
 for j,v in enumerate(product(O1,O2)):p[j+1]=p[j+1]+v
 return p
def divrem(p,x):
 q=[P() for _ in range(len(p)-1)];q[-1]=p[-1]
 for j in range(len(q)-2,-1,-1):q[j]=p[j+1]+x*q[j+1]
 return q,p[0]+x*q[0]
res=[]
for ci,a in enumerate(boundary):
 p=pairing(a,I)
 for cj,t in cts:
  if cj==ci:
   p,r1=divrem(p,t);p,r2=divrem(p,t);assert not r1.d and not r2.d
 res.append(p)
checks={'Dd6':D6,'Dd7':D7,**{'b%d'%j:I[j] for j in range(8)}}
for ci in (0,1):
 p=res[ci]
 for j in (0,1,2,3,5):checks['res%d_%d'%(ci,j)]=p[j]
 checks['res%d_gap'%ci]=4*p[3]*p[5]-p[4]*p[4]
for j,x in enumerate(res[2]):checks['res2_%d'%j]=x
h=res[3][1:];q1,hL=divrem(h,L);q2,v=divrem(q1,L);qmin=q2[0]+q2[1]*L/2+q2[2]*L*L/4
checks.update({'res3_0':res[3][0],'res3_Q0':q2[0],'res3_Q1':q2[1],'res3_Q2':q2[2],'res3_qmin':qmin,'res3_highgap':4*qmin*hL-v*v})
for i in range(5):checks['res3_lowbeta%d'%i]=sum((h[j]*(L/2)**j*F(comb(i,j),comb(4,j)) for j in range(i+1)),P())
assert len(checks)==37 and set(checks)==set(f['sign_polynomials']);count=0
for name,p in checks.items():
 low=min(p.d);high=max(p.d);a={k-low:v for k,v in p.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(500)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)];saved=f['sign_polynomials'][name]
 assert all(x>0 for x in v) and saved['min_R_power']==low and saved['max_R_power']==high and list(map(str,v))==saved['shifted_coefficients'];count+=len(v)
assert count==1640
base=z['sign_polynomials'];De=base['Det'];B6=base['B6'];d=list(map(F,De['shifted_coefficients']));b6=list(map(F,B6['shifted_coefficients']));k=2+De['min_R_power']-B6['min_R_power'];assert k==3
prod=[F(0)]*(len(d)+k)
for i,x in enumerate(d):
 for j in range(k+1):prod[i+j]+=x*comb(k,j)*100**(k-j)
upper=[F(1317,8425)*prod[i]-b6[i] for i in range(len(b6))];assert all(x>=0 for x in upper) and upper[0]>0 and list(map(str,upper))==f['base_b6_exact_asymptote_upper_shifted_coefficients']
assert F(1317,8425)-F(17,500)==F(20611,168500)==F(f['improved_b6_upper_coefficient'])
print({'strict_shift_coefficients':count,'sign_polynomials':37,'exact_tangencies':5,'exact_contact_divisions':10,'low_interval_bernstein_coefficients':5,'parameter_scope':'all real R>=500','improved_b6_strict_upper':'(20611/168500)*R^2'})
