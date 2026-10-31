# Independent exact factor, real/imaginary cross and interval Bernstein replay.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import comb,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-incompatible-resonance-segment-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='8261c3ed39d6e4b9422629b0f6653d581f5eb167d0b315f7f7320b029a61590b':raise ValueError('PIN')
f=json.loads(raw)
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
p=[F(1),F(1)]
for _ in range(3):p=mul(p,[F(10001,10000),F(1,50),F(1)])
q=[p[j]*4**(7-j) for j in range(8)]
if list(map(str,p))!=f['p1'] or list(map(str,q))!=f['p2'] or p[7]!=1 or q[7]!=1:raise ValueError('FACTORS')
def EO(a,w):
 t=w*w;return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,w*(a[1]-a[3]*t+a[5]*t*t-t**3)
def cross(a,b,w):
 e,o=EO(a,w);E,O=EO(b,w);return e*E+o*O,o*E-e*O
wl,wh=map(F,f['segment_frequency_interval']);rl,il=cross(p,q,wl);rh,ih=cross(p,q,wh)
if il!=F(f['imag_cross_at_left']) or ih!=F(f['imag_cross_at_right']) or not(il>0 and ih<0):raise ValueError('IMAG_SIGN')
E=lambda a:[a[0],-a[2],a[4],-a[6]];O=lambda a:[a[1],-a[3],a[5],-a[7]]
poly=mul(E(p),E(q))+[F(0)]
for j,v in enumerate(mul(O(p),O(q))):poly[j+1]+=v
n=len(poly)-1;a=wl*wl;b=wh*wh;power=[sum(poly[j]*comb(j,k)*a**(j-k)*(b-a)**k for j in range(k,n+1)) for k in range(n+1)];beta=[sum(power[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]
if list(map(str,beta))!=f['real_cross_bernstein'] or not all(v<0 for v in beta):raise ValueError('REAL_SIGN')
lo=[min(p[j],q[j]) for j in range(7)];hi=[max(p[j],q[j]) for j in range(7)];a=[hi[j] if j%4 in (0,3) else lo[j] for j in range(7)]+[F(1)] # E+, O- actual corner 2
H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)];minor=H[0][0]*H[1][1]-H[0][1]*H[1][0]
if minor!=F(f['hull_corner2_second_hurwitz_minor']) or minor>=0:raise ValueError('HULL_MINOR')
print('incompatible resonance independent replay:',{'stable_factorizations':2,'imaginary_cross_signs':['+','-'],'negative_real_cross_bernstein_coefficients':len(beta),'hull_corner_2_hurwitz_minor':str(minor),'scope':'actual segment has an imaginary-axis member; no strictly stable convex box contains both polynomials'})
