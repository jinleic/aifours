# Independent exact symbolic check of the d0=d6=1 degree-six direction.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('cts=[',1)[0])
raw=(root/'frontier-20261029-unit-endpoint-direction-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='7e28c59115a6d224818d441b54cce32201a7895d6c8105601360be8408088254';f=json.loads(raw)
cts=[(2,one),(3,P(F(3,2))),(1,R),(0,R+1),(2,L)];T=[]
for ci,t in cts:
 a=boundary[ci];ed=-a[2]+2*a[4]*t-3*a[6]*t*t;od=-a[3]+2*a[5]*t-3*t*t;T.append([ed*(-t)**(j//2) if j%2==0 else t*od*(-t)**((j-1)//2) for j in range(8)])
A=[[row[j] for j in (1,2,3,4,5)] for row in T];h=[-(row[0]+row[6]) for row in T];D=-determinant(A);c=[P() for _ in range(8)];c[0]=D;c[6]=D
for col,j in enumerate((1,2,3,4,5)):
 Q=[row[:] for row in A]
 for i in range(5):Q[i][col]=h[i]
 c[j]=-determinant(Q)
assert not c[7].d and all(not sum((T[i][j]*c[j] for j in range(8)),P()).d for i in range(5))
def product(a,b):
 q=[P() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):q[i+j]=q[i+j]+x*y
 return q
def pair(a,b):
 E1=[a[0],-a[2],a[4],-a[6]];O1=[a[1],-a[3],a[5],-a[7]];E2=[b[0],-b[2],b[4],-b[6]];O2=[b[1],-b[3],b[5],-b[7]];p=product(E1,E2)+[P()]
 for j,v in enumerate(product(O1,O2)):p[j+1]=p[j+1]+v
 while len(p)>1 and not p[-1].d:p.pop()
 return p
def divrem(p,x):
 q=[P() for _ in range(len(p)-1)];q[-1]=p[-1]
 for j in range(len(q)-2,-1,-1):q[j]=p[j+1]+x*q[j+1]
 return q,p[0]+x*q[0]
res=[]
for ci,a in enumerate(boundary):
 p=pair(a,c)
 for cj,t in cts:
  if cj==ci:p,r1=divrem(p,t);p,r2=divrem(p,t);assert not r1.d and not r2.d
 res.append(p)
assert [len(p)-1 for p in res]==[4,4,2,4]
h3=res[3][1:];q1,hL=divrem(h3,L);q2,v=divrem(q1,L);gap=4*q2[0]*hL-v*v
checks={'D6':D,**{'c%d'%j:c[j] for j in range(7)}}
for ci in (0,1,2):
 for j,p in enumerate(res[ci]):checks['res%d_%d'%(ci,j)]=p
checks.update({'res3_0':res[3][0],'res3_4':res[3][4],'res3_Q0':q2[0],'res3_Q1':q2[1],'res3_gap':gap});assert len(checks)==26 and set(checks)==set(f['sign_polynomials']);count=0
for name,p in checks.items():
 low=min(p.d);high=max(p.d);a={k-low:v for k,v in p.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(100)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)];saved=f['sign_polynomials'][name]
 assert all(x>0 for x in v) and saved['min_R_power']==low and saved['max_R_power']==high and list(map(str,v))==saved['shifted_coefficients'];count+=len(v)
assert count==600 and -F(f['sign_polynomials']['D6']['shifted_coefficients'][0])<0
print({'strict_shift_coefficients':count,'sign_polynomials':26,'boundary_tangencies':5,'exact_contact_divisions':10,'degree_six_direction':'d0=d6=1,d7=0','parameter_scope':'all real R>=100','mutation_controls':1})
