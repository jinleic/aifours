# Independent exact replay of 29 finite box/numerator instances; no LP solver.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-ultrawide-thirty-boxes-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='d6ef1551da1d58692d436500ee64f279a2824c9306e7c846c4f8c569ee402923':raise ValueError('PIN')
data=json.loads(raw)['cases']
if [r['case'] for r in data]!=list(range(30)):raise ValueError('CASES')
def determinant(A):
 n=len(A);d=lcm(*(v.denominator for row in A for v in row));M=[[int(v*d) for v in row] for row in A];sgn=1;prev=1
 for k in range(n-1):
  if not M[k][k]:
   r=next((r for r in range(k+1,n) if M[r][k]),None)
   if r is None:return F(0)
   M[r],M[k]=M[k],M[r];sgn=-sgn
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=M[i][j]*pivot-M[i][k]*M[k][j]
    if x%prev:raise ValueError('BAREISS')
    M[i][j]=x//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return F(sgn*M[-1][-1],d**n)
def corners(lo,hi):
 ret=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return ret
def multiply(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]];z=multiply(e(a),e(b))+[F(0)]
 for i,v in enumerate(multiply(o(a),o(b))):z[i+1]+=v
 return z
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;beta=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return beta
  m=(l+r)/2;L,R=split(beta)
  if b<=m:r=m;beta=L
  elif a>=m:l=m;beta=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('LEAF_DEPTH')
results=[];minor_total=0;coefficient_total=0
for rec in data:
 rawbox=(root/rec['box']).read_bytes()
 if sha256(rawbox).hexdigest()!=rec['box_sha256']:raise ValueError('BOX_PIN')
 f=json.loads(rawbox);lo=list(map(F,f['lower']));hi=list(map(F,f['upper']));b=list(map(F,rec['b']))
 if not all(0<lo[j]<hi[j] for j in range(7)) or not all(v>0 for v in b) or b[7]!=1:raise ValueError('BOUNDS')
 minimum=None;counts=[]
 for ci,a in enumerate(corners(lo,hi)):
  H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
  for n in range(1,8):
   if determinant([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
   minor_total+=1
  p=pairing(a,b);last=F(0);count=0
  for l,r in sorted(rec['frequency_leaves'][ci],key=lambda x:F(x[0])):
   l,r=F(l),F(r)
   if last!=l or not l<r:raise ValueError('COVER')
   beta=leaf(p,l,r)
   if not all(v>0 for v in beta):raise ValueError('LEAF_SIGN')
   minimum=min(beta) if minimum is None else min(minimum,min(beta));count+=len(beta);last=r
  if last!=1:raise ValueError('COVER')
  counts.append(count);coefficient_total+=count
 if minimum!=F(rec['compactified_minimum']):raise ValueError('MARGIN')
 results.append({'case':rec['case'],'hurwitz_minors':28,'bernstein_coefficients':counts,'minimum':str(minimum)})
 print('independent ultrawide box',rec['case'],'28 minors and',sum(counts),'strict coefficients')
out={'status':'WRITTEN-checked-in-kernel; author candidate, not parent adoption','frozen_sha256':'d6ef1551da1d58692d436500ee64f279a2824c9306e7c846c4f8c569ee402923','boxes':len(results),'hurwitz_minors':minor_total,'strict_bernstein_coefficients':coefficient_total,'cases':results,'scope':'30 specific ultrawide boxes; full all-member stability uses named Kharitonov theorem and all-frequency pairing follows from exact leaves and affine minimization; no arbitrary-box result'}
path=root/'frontier-20261029-ultrawide-thirty-boxes-independent-result-v1.json';text=json.dumps(out,indent=2,sort_keys=True)+'\n';path.write_text(text)
print('ultrawide independent replay',len(results),'boxes',minor_total,'minors',coefficient_total,'positive coefficients','sha256',sha256(text.encode()).hexdigest())
