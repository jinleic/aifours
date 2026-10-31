# Independent exact replay of a real four-dimensional endpoint-span
# annihilator, strict stability, and an unrestricted common numerator.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json').read_bytes()
if sha256(raw).hexdigest()!='3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293':raise ValueError('PIN')
f=json.loads(raw);lo=list(map(F,f['lower']));hi=list(map(F,f['upper']));b=list(map(F,f['good_numerator']))
if not all(0<lo[j]<hi[j] for j in range(7)) or b[7]<=0 or not all(v>0 for v in b) or sum(hi)+1!=F(f['coefficient_sum_bound']):raise ValueError('INPUT')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
cs=corners(lo,hi);G=[]
for ei in (0,1):G.append([cs[2*ei][j] if j%2==0 else F(0) for j in range(8)])
for oi in (0,1):G.append([cs[oi][j] if j%2 else F(0) for j in range(8)])
mid=[(lo[j]+hi[j])/2 for j in range(7)]+[F(1)]
G.append([F(j+1)*mid[j+1] for j in range(7)]+[F(0)])
G.append([F(j+1)*G[-1][j+1] for j in range(7)]+[F(0)])
G.append([F(j+1)*G[-1][j+1] for j in range(7)]+[F(0)])
def det(A):
 n=len(A);den=lcm(*(x.denominator for row in A for x in row));M=[[int(x*den) for x in row] for row in A];prev=1;sgn=1
 for k in range(n-1):
  if not M[k][k]:
   q=next((i for i in range(k+1,n) if M[i][k]),None)
   if q is None:return F(0)
   M[q],M[k]=M[k],M[q];sgn=-sgn
  p=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=M[i][j]*p-M[i][k]*M[k][j]
    if v%prev:raise ValueError('BAREISS')
    M[i][j]=v//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sgn*M[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def row(a,t):
 return [sum(a[j]*(1 if ((k-j)//2)%2==0 else -1)*t**((j+k)//2) for j in range(8) if (j+k)%2==0) for k in range(8)]
rows=[];weights=[]
for atom in f['support']:
 t=F(atom['t']);w=F(atom['weight']);ci=atom['corner']
 if not(t>0 and w>0 and 0<=ci<4):raise ValueError('ATOM')
 rows.append(row(cs[ci],t));weights.append(w)
if len(rows)!=8:raise ValueError('SUPPORT')
M=[[sum(rows[i][j]*G[k][j] for j in range(8)) for i in range(8)] for k in range(7)];sums=[sum(M[k][i]*weights[i] for i in range(8)) for k in range(7)]
if not all(v==0 for v in sums):raise ValueError('ANNIHILATOR')
cof=[(-1)**(i+1)*det([[M[k][j] for j in range(8) if j!=i] for k in range(7)]) for i in range(8)]
if not all(v>0 for v in cof) or not all(cof[i]*weights[0]==cof[0]*weights[i] for i in range(8)):raise ValueError('COFACTOR')
good_sum=sum(weights[i]*sum(rows[i][j]*b[j] for j in range(8)) for i in range(8))
if good_sum<=0:raise ValueError('GOOD_SUM')
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]];p=mul(e(a),e(b))+[F(0)]
 for j,x in enumerate(mul(o(a),o(b))):p[j+1]+=x
 return p
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;v=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
minimum=None;counts=[]
for ci,a in enumerate(cs):
 p=pairing(a,b);last=F(0);count=0
 for l,r in sorted(f['good_frequency_leaves'][ci],key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER')
  q=leaf(p,l,r)
  if not all(x>0 for x in q):raise ValueError('SIGN')
  minimum=min(q) if minimum is None else min(minimum,min(q));last=r;count+=len(q)
 if last!=1:raise ValueError('COVER')
 counts.append(count)
if minimum!=F(f['good_compactified_margin']):raise ValueError('MARGIN')
if min(cof)!=F(f['minimum_positive_cofactor']):raise ValueError('MIN_COFACTOR')
print('seven-dimensional span anchor replay:',{'hurwitz_minors':28,'positive_atoms':8,'zero_generator_sums':7,'positive_cofactors':8,'good_pairing_counts':counts,'good_margin':str(minimum),'scope':'real seven-generator span excluded; unrestricted numerator exists'})

rawopen=(root/'frontier-20261029-seven-dimensional-span-obstruction-open-frozen-v1.json').read_bytes()
if sha256(rawopen).hexdigest()!='5c9ef2bce336f60220d93b5e6a9720be4ca0a7971b1e7f96bdf44e9cf4014f11':raise ValueError('OPEN_PIN')
g=json.loads(rawopen);eps=F(g['radius']);mincof=min(cof);B=sum(b);delta=F(f['good_compactified_margin'])
if mincof!=F(g['min_cofactor']) or B!=F(g['good_numerator_l1']) or delta!=F(g['good_margin']):raise ValueError('RECOMPUTE')
from math import factorial
checks=[all(0<lo[j]-eps and lo[j]+eps<hi[j]-eps for j in range(7)),14*eps*B<=delta,max(hi)+1<10**10,210*(max(hi)+1)<10**13,max(F(v['t']) for v in f['support'])<10**4,64*10**10*10**13*10**28<10**53,64*(10**13+210*10**10)*10**28<10**44,factorial(7)*7*10**(53*6+44)<10**367,2*eps*10**367<mincof]
if not all(checks):raise ValueError('OPEN_BOUND')
print('independent 7D open-span replay:',{'radius':str(eps),'endpoint_dimensions':14,'positive_cofactors':8,'bound_checks':len(checks),'scope':'each nearby stable box has fixed unrestricted common numerator but no common numerator in its own seven-generator real span'})
