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

augraw=(root/'frontier-20261029-six-span-two-derivative-sign-frozen-v1.json').read_bytes()
if sha256(augraw).hexdigest()!='09eb2644628741f80196fe4d82d4ddd8dcf12d273e8ec036ba1652117d85e72b':raise ValueError('AUG_PIN')
aug=json.loads(augraw);ds=[mid]
for _ in range(4):ds.append([F(j+1)*ds[-1][j+1] for j in range(7)]+[F(0)])
vecs=G+[ds[3],ds[4]];basisdet=det([[vecs[j][i] for j in range(8)] for i in range(8)]);extra=[sum(weights[i]*sum(rows[i][j]*ds[k][j] for j in range(8)) for i in range(7)) for k in (3,4)];cofextra=[sum(cof[i]*sum(rows[i][j]*ds[k][j] for j in range(8)) for i in range(7)) for k in (3,4)]
if basisdet!=F(aug['basis_determinant']) or basisdet==0 or list(map(str,extra))!=aug['additional_derivative_sums'] or not all(v<0 for v in extra) or list(map(str,[-v for v in cofextra]))!=aug['cofactor_weighted_margins']:raise ValueError('AUGMENTED_SIGNS')
rawopen=(root/'frontier-20261029-six-span-two-derivative-sign-open-frozen-v2.json').read_bytes()
if sha256(rawopen).hexdigest()!='96f15eb12225b63c85f9a04c7594269e2d1caf1715b755024533171947f0caa4':raise ValueError('AUG_OPEN_PIN')
h=json.loads(rawopen);eps2=F(h['radius']);minT=min(-v for v in cofextra)
if minT!=F(h['minimum_derivative_cofactor_margin']) or basisdet!=F(h['basis_determinant']) or min(cof)!=F(h['minimum_cofactor']):raise ValueError('AUG_RECOMPUTE')
from math import factorial
checks2=[eps2<=F(g['radius']),2*eps2*10**98<min(cof),2*eps2*10**119<minT,2*eps2*10**70<abs(basisdet),64*100*100000*9**7<10**20,64*200000*9**7<10**18,factorial(6)*(10**16)**6<10**99,7*(10**98*10**20+10**99*10**18)<10**119,max(abs(v) for vec in vecs for v in vec)<10**5,840<10**5,factorial(8)*8*(10**5)**8<10**70]
if not all(checks2):raise ValueError('AUG_OPEN')
print('independent 6+2 full-basis replay:',{'basis_determinant':str(basisdet),'negative_extra_sums':2,'endpoint_radius':str(eps2),'open_checks':len(checks2),'scope':'any common numerator has negative D3 or D4 basis coordinate; fixed unrestricted numerator exists'})

quotraw=(root/'frontier-20261029-quotient-two-direction-cone-frozen-v1.json').read_bytes()
if sha256(quotraw).hexdigest()!='b265082fe04ac8791abacf64d3a1774e3ce1d33b89b95d71b92c71529c4702ee':raise ValueError('QUOT_PIN')
qdata=json.loads(quotraw);qxy=[]
for key in ('low_support','high_support'):
 C=[F(0)]*8
 for atom in qdata[key]:
  t=F(atom['t']);w=F(atom['weight']);ci=atom['corner']
  if not(t>0 and w>0 and 0<=ci<4):raise ValueError('Q_ATOM')
  rr=row(cs[ci],t)
  for j in range(8):C[j]+=w*rr[j]
 if not all(sum(C[j]*G[k][j] for j in range(8))==0 for k in range(6)):raise ValueError('Q_ANNIHILATOR')
 x=sum(C[j]*ds[3][j] for j in range(8));y=sum(C[j]*ds[4][j] for j in range(8))
 if not(x<0 and y<0):raise ValueError('Q_SIGN')
 qxy.append((x,y))
if list(map(str,qxy[0]))!=qdata['low_xy'] or list(map(str,qxy[1]))!=qdata['high_xy'] or not(qxy[0][1]/qxy[0][0]<F(qdata['low_slope_upper']) and qxy[1][1]/qxy[1][0]>F(qdata['high_slope_lower'])) or not(qxy[0][0]*qxy[1][1]-qxy[0][1]*qxy[1][0]>0):raise ValueError('Q_GAPS')
print('independent two-direction quotient replay:',{'positive_atoms_per_certificate':[len(qdata['low_support']),len(qdata['high_support'])],'zero_six_span_sums_each':6,'strict_negative_quotient_coordinates_each':2,'independent_directions':True,'low_slope_below':'267/100','high_slope_above':'27/10','scope':'common numerator must satisfy both corresponding quotient halfplanes; not an unrestricted negative certificate'})
