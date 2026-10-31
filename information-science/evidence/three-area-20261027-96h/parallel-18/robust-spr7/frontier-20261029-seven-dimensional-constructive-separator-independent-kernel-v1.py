# Independent exact replay of a real four-dimensional endpoint-span
# annihilator, strict stability, and an unrestricted common numerator.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-six-dimensional-endpoint-derivatives-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='93aaebc291516b3d4ff81b4cf7b1435ad3d4b3440f9ff38fb1f2ba1438971a0c':raise ValueError('PIN')
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
if len(rows)!=7:raise ValueError('SUPPORT')
M=[[sum(rows[i][j]*G[k][j] for j in range(8)) for i in range(7)] for k in range(6)];sums=[sum(M[k][i]*weights[i] for i in range(7)) for k in range(6)]
if not all(v==0 for v in sums):raise ValueError('ANNIHILATOR')
cof=[(-1)**i*det([[M[k][j] for j in range(7) if j!=i] for k in range(6)]) for i in range(7)]
if not all(v>0 for v in cof) or not all(cof[i]*weights[0]==cof[0]*weights[i] for i in range(7)):raise ValueError('COFACTOR')
good_sum=sum(weights[i]*sum(rows[i][j]*b[j] for j in range(8)) for i in range(7))
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
print('six-dimensional span anchor replay:',{'hurwitz_minors':28,'positive_atoms':7,'zero_generator_sums':6,'positive_cofactors':7,'good_pairing_counts':counts,'good_margin':str(minimum),'scope':'restricted real span excluded; unrestricted b exists'})
openraw=(root/'frontier-20261029-six-dimensional-endpoint-derivatives-open-frozen-v1.json').read_bytes()
if sha256(openraw).hexdigest()!='22a95b0643672af140b6b1c824790d9d715d20658c2e17acac8e82c2ccbce71d':raise ValueError('OPEN_PIN')
g=json.loads(openraw);eps=F(g['radius']);mincof=min(cof);B=sum(b);delta=F(f['good_compactified_margin']);width=min(hi[j]-lo[j] for j in range(7));low=min(lo)
if (mincof,B,delta,width,low)!=(F(g['minimum_cofactor']),F(g['good_numerator_l1']),F(g['good_margin']),F(g['minimum_width']),F(g['minimum_lower'])):raise ValueError('RECOMPUTE')
checks=[eps<=1,4*eps<=width,2*eps<=low,14*eps*B<=delta,2*eps*10**98<mincof,max(hi)+1<100,all(F(a['t'])<9 for a in f['support']),64*100*5000*9**7<10**16,64*10105*9**7<10**14,4320*(10**16)**5*(10**14)<10**98]
if not all(checks):raise ValueError('OPEN_BOUNDS')
print('independent 6D open-span replay:',{'radius':str(eps),'endpoint_dimensions':14,'positive_cofactors':7,'exact_inequalities':len(checks),'scope':'no common numerator in real endpoint-plus-first-two-midpoint-derivatives span; a fixed unrestricted numerator exists'})

raw7=(root/'frontier-20261029-seven-dimensional-constructive-separator-frozen-v1.json').read_bytes()
if sha256(raw7).hexdigest()!='20bd10e2128df44cab2575d1e7eea098baf612c4d134f80e1f324cb039a6a054':raise ValueError('SEVEN_PIN')
h=json.loads(raw7);c=list(map(F,h['span_coefficients']));b7=list(map(F,h['b']));D3=[F(j+1)*G[-1][j+1] for j in range(7)]+[F(0)];D4=[F(j+1)*D3[j+1] for j in range(7)]+[F(0)];G7=G+[D3]
if len(c)!=7 or not all(sum(c[k]*G7[k][j] for k in range(7))==b7[j] for j in range(8)) or b7[7]!=1 or not all(x>0 for x in b7):raise ValueError('SPAN7')
minimum7=None;count7=0
for ci,a in enumerate(cs):
 p=pairing(a,b7);last=F(0)
 for l,r in sorted(h['frequency_leaves'][ci],key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER7')
  v=leaf(p,l,r)
  if not all(x>0 for x in v):raise ValueError('SIGN7')
  minimum7=min(v) if minimum7 is None else min(minimum7,min(v));last=r;count7+=len(v)
 if last!=1:raise ValueError('COVER7')
if minimum7!=F(h['compactified_minimum']):raise ValueError('MARGIN7')
print('independent seven-dimensional synthesis:',{'exact_generator_reconstruction':True,'positive_pairing_coefficients':count7,'compactified_margin':str(minimum7),'scope':'the exact anchor box has a common numerator in endpoint-plus-first-three-midpoint-derivative span'})
