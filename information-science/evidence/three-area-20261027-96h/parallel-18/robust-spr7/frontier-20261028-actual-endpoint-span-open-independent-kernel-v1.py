# Independent exact replay of a real four-dimensional endpoint-span
# annihilator, strict stability, and an unrestricted common numerator.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-actual-endpoint-span-obstruction-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='95d943653a8ceca71d99950a326a4fe7a3fcd2fac0471c746de82570daab83fb':raise ValueError('PIN')
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
if len(rows)!=5:raise ValueError('SUPPORT')
M=[[sum(rows[i][j]*G[k][j] for j in range(8)) for i in range(5)] for k in range(4)];sums=[sum(M[k][i]*weights[i] for i in range(5)) for k in range(4)]
if not all(v==0 for v in sums):raise ValueError('ANNIHILATOR')
cof=[(-1)**i*det([[M[k][j] for j in range(5) if j!=i] for k in range(4)]) for i in range(5)]
if not all(v>0 for v in cof) or not all(cof[i]*weights[0]==cof[0]*weights[i] for i in range(5)):raise ValueError('COFACTOR')
good_sum=sum(weights[i]*sum(rows[i][j]*b[j] for j in range(8)) for i in range(5))
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
print('endpoint-span independent replay:',{'strict_hurwitz_minors':28,'positive_atom_weights':5,'zero_generator_sums':4,'strict_same_sign_cofactors':5,'good_pairing_coefficients':counts,'good_margin':str(minimum),'good_atom_sum':str(good_sum),'scope':'no numerator in real endpoint span; unrestricted numerator exists'})

openraw=(root/'frontier-20261028-actual-endpoint-span-open-frozen-v1.json').read_bytes()
if sha256(openraw).hexdigest()!='c3a98e16130afeb75d6963a6487cbebc4e21e58d8b4f8f261b814157b1e9bd1e':raise ValueError('OPEN_PIN')
g=json.loads(openraw);eps=F(g['radius']);mincof=min(cof);Bsum=sum(b);delta=F(f['good_compactified_margin']);width=min(hi[j]-lo[j] for j in range(7));low=min(lo);upper=max(hi);Mentry=F(g['entry_bound']);Lentry=F(g['entry_lipschitz']);Lcof=F(g['cofactor_lipschitz'])
if (mincof,Bsum,delta,width,low,upper)!=(F(g['minimum_cofactor']),F(g['Bsum']),F(g['pairing_margin']),F(g['min_width']),F(g['min_lower']),F(g['max_upper'])):raise ValueError('RECOMPUTE')
checks=[eps<=1,4*eps<=width,2*eps<=low,14*eps*Bsum<=delta,2*eps*Lcof<mincof,upper+1<100,all(F(atom['t'])<9 for atom in f['support']),64*10000*9**7<Mentry,64*201*9**7<Lentry,96*Mentry**3*Lentry<Lcof]
if not all(checks):raise ValueError('ROBUST_BOUND')
print('independent open endpoint-span replay:',{'radius':str(eps),'endpoint_dimensions':14,'strict_cofactors':5,'exact_inequalities':len(checks),'all_hold':True,'scope':'each nearby box has no common numerator in its real parity-endpoint span; fixed unrestricted numerator remains common'})
