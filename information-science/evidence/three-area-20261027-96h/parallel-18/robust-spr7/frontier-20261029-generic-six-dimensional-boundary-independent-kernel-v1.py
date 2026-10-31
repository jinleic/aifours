# Independent exact factor expansion and monomial-derivative replay of a
# 4x4 boundary tangent minor; the general compactness argument is written.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-generic-five-contact-span-rigidity-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='ec10b639d8fcc0cc9299b21be2cf8549cd015e3a91a13218d15dfb63aec1a0bf':raise ValueError('PIN')
f=json.loads(raw);ts=list(map(F,f['nodes']));u=F(f['u']);v=F(f['v']);alpha=F(f['alpha']);beta=F(f['beta'])
if not 0<u<ts[0]<ts[1]<ts[2]<ts[3]<ts[4]<v or not(alpha>0 and beta>0):raise ValueError('ORDER')
def cubic(roots,scale):
 p=[-scale]
 for r in roots:
  q=[F(0)]*(len(p)+1)
  for i,x in enumerate(p):q[i]-=r*x;q[i+1]+=x
  p=q
 return p
Em=cubic([u,ts[2],ts[3]],beta);Ep=cubic([ts[0],ts[1],ts[4]],alpha);Om=cubic([ts[0],ts[3],ts[4]],F(1));Op=cubic([ts[1],ts[2],v],F(1))
lo=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]];hi=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]]
if list(map(str,lo))!=f['boundary_lower'] or list(map(str,hi))!=f['boundary_upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
def member(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],F(1)]
cs=[member(Em,Om),member(Em,Op),member(Ep,Om),member(Ep,Op)]
G=[[cs[2*e][j] if j%2==0 else F(0) for j in range(8)] for e in (0,1)]+[[cs[o][j] if j%2 else F(0) for j in range(8)] for o in (0,1)]
def pairing(a,b,t):
 out=F(0)
 for j in range(8):
  for k in range(8):
   if (j+k)%2:continue
   out+=a[j]*b[k]*(1 if ((k-j)//2)%2==0 else -1)*t**((j+k)//2)
 return out
def derivative(a,b,t):
 out=F(0)
 for j in range(8):
  for k in range(8):
   if (j+k)%2 or j+k==0:continue
   q=(j+k)//2;out+=a[j]*b[k]*(1 if ((k-j)//2)%2==0 else -1)*q*t**(q-1)
 return out
T=[]
for ci,t in f['contacts']:
 ci=int(ci);t=F(t)
 if any(pairing(cs[ci],g,t)!=0 for g in G):raise ValueError('CONTACT')
 T.append([derivative(cs[ci],g,t) for g in G])
def det(A):
 n=len(A);den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];sgn=1;prev=1
 for k in range(n-1):
  if M[k][k]==0:
   i=next((i for i in range(k+1,n) if M[i][k]),None)
   if i is None:return F(0)
   M[i],M[k]=M[k],M[i];sgn=-sgn
  p=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=M[i][j]*p-M[i][k]*M[k][j]
    if x%prev:raise ValueError('BAREISS')
    M[i][j]=x//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sgn*M[-1][-1],den**n)
d=det([T[i] for i in f['minor_rows']])
if d!=F(f['minor_determinant']) or d==0:raise ValueError('MINOR')
print('generic boundary-rigidity independent replay:',{'strict_widths':7,'contact_rows':5,'independent_tangent_minor':str(d),'rank_at_least':4,'scope':'specific nonzero polynomial minor; generic conclusion uses written algebraic and compactness arguments'})

raw6=(root/'frontier-20261029-generic-six-dimensional-boundary-frozen-v1.json').read_bytes()
if sha256(raw6).hexdigest()!='380cf257268e41b9744ea7157e3ac22b4df0a1195df9e9c03c81b1ef7942f891':raise ValueError('SIX_PIN')
g=json.loads(raw6);mid=[(lo[j]+hi[j])/2 for j in range(7)]+[F(1)];D1=[F(j+1)*mid[j+1] for j in range(7)]+[F(0)];D2=[F(j+1)*D1[j+1] for j in range(7)]+[F(0)];G6=G+[D1,D2];TT=[[derivative(cs[int(ci)],h,F(t)) for h in G6] for ci,t in f['contacts']];x=det(TT+[[pairing(cs[0],h,F(0)) for h in G6]]);y=det(TT+[[pairing(cs[0],h,F(5)) for h in G6]])
if x!=F(g['origin_extended_determinant']) or y!=F(g['fifth_frequency_extended_determinant']) or not(x>0 and y<0):raise ValueError('SIX_DETERMINANTS')
print('generic six-dimensional independent replay:',{'origin_extended_determinant':str(x),'positive_frequency_extended_determinant':str(y),'opposite_signs':True,'scope':'one shape has an open neighborhood where all sufficiently near-boundary boxes have no common numerator in real endpoint-plus-two-derivatives span'})
