# Independent exact replay of a real four-dimensional endpoint-span
# annihilator, strict stability, and an unrestricted common numerator.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-five-dimensional-endpoint-derivative-span-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='0345ecd235b7361d2ba7e52067a0c317f9da8473fe019bf448f5fef2b7fef12b':raise ValueError('PIN')
f=json.loads(raw);lo=list(map(F,f['lower']));hi=list(map(F,f['upper']));b=list(map(F,f['good_numerator']))
if not all(0<lo[j]<hi[j] for j in range(7)) or b[7]!=1 or not all(v>0 for v in b) or sum(hi)+1!=F(f['coefficient_sum_bound']):raise ValueError('INPUT')
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
if len(rows)!=6:raise ValueError('SUPPORT')
M=[[sum(rows[i][j]*G[k][j] for j in range(8)) for i in range(6)] for k in range(5)];sums=[sum(M[k][i]*weights[i] for i in range(6)) for k in range(5)]
if not all(v==0 for v in sums):raise ValueError('ANNIHILATOR')
cof=[(-1)**(i+1)*det([[M[k][j] for j in range(6) if j!=i] for k in range(5)]) for i in range(6)]
if not all(v>0 for v in cof) or not all(cof[i]*weights[0]==cof[0]*weights[i] for i in range(6)):raise ValueError('COFACTOR')
good_sum=sum(weights[i]*sum(rows[i][j]*b[j] for j in range(8)) for i in range(6))
if good_sum!=F(f['good_atom_sum']) or good_sum<=0:raise ValueError('GOOD_SUM')
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
if min(cof)!=F(f['minimum_cofactor']):raise ValueError('MIN_COFACTOR')
print('five-dimensional span independent replay:',{'strict_hurwitz_minors':28,'positive_atoms':6,'zero_generator_sums':5,'strict_positive_cofactors':6,'good_pairing_counts':counts,'good_margin':str(minimum),'good_atom_sum':str(good_sum),'scope':'no common numerator in real endpoint-plus-first-derivative span; unrestricted numerator exists'})

openraw=(root/'frontier-20261028-five-dimensional-endpoint-derivative-open-frozen-v1.json').read_bytes()
if sha256(openraw).hexdigest()!='71336558fd0cf32a16c178a6a0b6b6a01bb5ff77799c8418ebcb574a295d2583':raise ValueError('OPEN_PIN')
g=json.loads(openraw);eps=F(g['radius']);mincof=min(cof);B=sum(b);delta=F(f['good_compactified_margin']);width=min(hi[j]-lo[j] for j in range(7));low=min(lo)
if (mincof,B,delta,width,low)!=(F(g['minimum_cofactor']),F(g['good_numerator_l1']),F(g['good_margin']),F(g['minimum_width']),F(g['minimum_lower'])):raise ValueError('RECOMPUTE')
checks=[eps<=1,4*eps<=width,2*eps<=low,14*eps*B<=delta,2*eps*10**76<mincof,max(hi)+1<100,all(F(a['t'])<9 for a in f['support']),64*100*1000*9**7<10**15,64*1707*9**7<10**13,600*(10**15)**4*(10**13)<10**76]
if not all(checks):raise ValueError('OPEN_BOUNDS')
print('independent 5D open-span replay:',{'radius':str(eps),'endpoint_dimensions':14,'positive_cofactors':6,'exact_inequalities':len(checks),'scope':'no common numerator in real endpoint-plus-first-midpoint-derivative span; a fixed unrestricted numerator exists'})
