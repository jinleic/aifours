# Independent integer/Fraction replay of one exact anisotropic stable box
# and its simplified common numerator. No LP solver is used here.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import comb,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=load('frontier-20261029-norm-gap-conservative-example-frozen-v1.json','d757dcccd39947165ad495a81e83577c5360d72aba1123284e476fd0749f8e2d')
g=load(f['source_box'],f['source_box_sha256'])
lo=list(map(F,g['lower']));hi=list(map(F,g['upper']));b=list(map(F,f['midpoint']))
if not all(F(0)<lo[j]<hi[j] for j in range(7)) or len(b)!=8 or b[7]!=1 or not all(x>0 for x in b):raise ValueError('BOX_OR_NUMERATOR')
def parity_corner(es,os):
 ret=[]
 for j in range(7):
  side=es if j%2==0 else os
  ret.append((lo[j] if side==0 else hi[j]) if j%4 in (0,1) else (hi[j] if side==0 else lo[j]))
 return ret+[F(1)]
cs=[parity_corner(e,o) for e,o in ((0,0),(0,1),(1,0),(1,1))]
def bareiss(M):
 n=len(M);den=lcm(*(v.denominator for row in M for v in row));A=[[int(v*den) for v in row] for row in M];sgn=1;prev=1
 for k in range(n-1):
  if A[k][k]==0:
   q=next((i for i in range(k+1,n) if A[i][k]),None)
   if q is None:return F(0)
   A[k],A[q]=A[q],A[k];sgn=-sgn
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=A[i][j]*pivot-A[i][k]*A[k][j]
    if x%prev:raise ValueError('BAREISS')
    A[i][j]=x//prev
  for i in range(k+1,n):A[i][k]=0
  prev=pivot
 return F(sgn*A[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if bareiss([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def mul(x,y):
 a=[F(0)]*(len(x)+len(y)-1)
 for i,u in enumerate(x):
  for j,v in enumerate(y):a[i+j]+=u*v
 return a
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]]
 p=mul(e(a),e(b))+[F(0)]
 for i,v in enumerate(mul(o(a),o(b))):p[i+1]+=v
 return p
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [row[0] for row in rows],[row[-1] for row in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;beta=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return beta
  m=(l+r)/2;L,R=split(beta)
  if b<=m:r=m;beta=L
  elif a>=m:l=m;beta=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('LEAF_DEPTH')
mins=[];counts=[]
for ci,a in enumerate(cs):
 p=pairing(a,b);last=F(0);vals=[];rows=sorted(f['center_frequency_leaves'][ci],key=lambda r:F(r[0]))
 for l,r in rows:
  l,r=F(l),F(r)
  if last!=l or l>=r:raise ValueError('LEAF_COVER')
  beta=leaf(p,l,r)
  if not all(v>0 for v in beta):raise ValueError('LEAF_SIGN')
  vals.extend(beta);last=r
 if last!=1:raise ValueError('LEAF_COVER')
 mins.append(min(vals));counts.append(len(vals))
if min(mins)!=F(f['center_compactified_margin']):raise ValueError('MARGIN')
r=list(map(F,f['radii']));mid=[(lo[j]+hi[j])/2 for j in range(7)]+[F(1)]
if mid!=b or any(r[j]!=(hi[j]-lo[j])/2 for j in range(7)):raise ValueError('MIDPOINT')
E=lambda p:[p[0],-p[2],p[4],-p[6]];O=lambda p:[p[1],-p[3],p[5],-p[7]];V=mul(E(b),E(b))+[F(0)]
for j,z in enumerate(mul(O(b),O(b))):V[j+1]+=z
A=[r[j] for j in (0,2,4,6)];B=[r[j] for j in (1,3,5)];H=mul(A,A)+[F(0)]
for j,z in enumerate(mul(B,B)):H[j+1]+=z
t=F(f['negative_gap_t']);value=sum((V[j]-H[j])*t**j for j in range(8))
if value!=F(f['negative_gap_value']) or value>=0:raise ValueError('NEGATIVE_GAP')
print('independent norm-gap conservatism replay:',{'strict_hurwitz_minors':28,'strict_center_pairing_coefficients':sum(counts),'negative_norm_gap_t':str(t),'negative_gap':str(value),'scope':'center is common on full box though V-H criterion fails'})
