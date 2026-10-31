# Standalone exact replay of the derivative/integration obstruction.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-derivative-lift-box-obstruction-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='46d821081629ba035892b827c0bcd9d62580304d0843d30a4012d76f02e5c9ef':raise ValueError('HASH')
d=json.loads(raw);p=[Q(comb(7,j)) for j in range(8)];q=[Q(comb(6,j)) for j in range(7)];c=q[:];c[0]+=2;r=Q(d['radius'])
if [str(x) for x in p]!=d['septic_center'] or [str(x) for x in q]!=d['derivative_center'] or [str(x) for x in c]!=d['derivative_common_numerator']:raise ValueError('CENTER')
lo=[p[j]-r for j in range(7)];hi=[p[j]+r for j in range(7)];ql=[Q(j+1,7)*lo[j+1] for j in range(6)];qh=[Q(j+1,7)*hi[j+1] for j in range(6)]
if [str(x) for x in lo]!=d['lower'] or [str(x) for x in hi]!=d['upper'] or [str(x) for x in ql]!=d['derivative_lower'] or [str(x) for x in qh]!=d['derivative_upper']:raise ValueError('BOX')
if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
def corners(lo,hi,n):
 out=[]
 for e in (0,1):
  for o in (0,1):
   a=[Q(0)]*(n+1);a[n]=Q(1)
   for j in range(0,n,2):a[j]=lo[j] if ((j//2)%2==0)==(e==0) else hi[j]
   for j in range(1,n,2):a[j]=lo[j] if ((j//2)%2==0)==(o==0) else hi[j]
   out.append(a)
 return out
pcs=corners(lo,hi,7);qcs=corners(ql,qh,6)
def det(m):
 A=[[Q(x) for x in row] for row in m];ans=Q(1);sign=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sign=-sign
  v=A[k][k];ans*=v
  for i in range(k+1,n):
   f=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
   A[i][k]=Q(0)
 return sign*ans
def minors(a):
 n=len(a)-1;v=a[::-1]
 def co(j):return v[j] if 0<=j<=n else Q(0)
 return [det([[co(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
if not all(v>0 for a in pcs+qcs for v in minors(a)):raise ValueError('HURWITZ')
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def parity(a):return [a[j]*(-1)**(j//2) for j in range(0,len(a),2)],[a[j]*(-1)**((j-1)//2) for j in range(1,len(a),2)]
def pair(a,b):
 E,O=parity(a);F,G=parity(b);ee=mul(E,F);oo=mul(O,G);out=ee+[Q(0)]*max(0,len(oo)+1-len(ee))
 for j,v in enumerate(oo):out[j+1]+=v
 return out
def ev(poly,t):return sum(v*t**j for j,v in enumerate(poly))
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def cover(poly,proof,status):
 if proof['status']!=status:raise ValueError('STATUS')
 arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);vals=[]
 for leaf in arr:
  lo,hi=Q(leaf['left']),Q(leaf['right'])
  if lo!=at or not lo<hi:raise ValueError('COVER')
  v=beta(poly,lo,hi)
  if v!=[Q(x) for x in leaf['coefficients']] or not all(x>0 for x in v):raise ValueError('LEAF')
  vals.extend(v);at=hi
 if at!=1:raise ValueError('COVER')
 return len(arr),vals
H=pair(q,c)
if [str(v) for v in H]!=d['derivative_center_polynomial']:raise ValueError('H')
_,vals=cover(H,d['derivative_center_proof'],'NONNEGATIVE_PROVED');hmin=min(vals)
if hmin!=Q(5,1024) or hmin-sum(abs(x) for x in c)*3*r!=Q(d['derivative_uniform_margin']) or 1-sum(abs(x) for x in p)*7*r!=Q(d['septic_center_margin']):raise ValueError('MARGINS')
B=[Q(0)]+[Q(7,j+1)*c[j] for j in range(7)]
if [str(x) for x in B]!=d['integrated_without_constant'] or [Q(j,7)*B[j] for j in range(1,8)]!=c:raise ValueError('INTEGRAL')
P=pair(p,B);E,_=parity(p)
if [str(v) for v in P]!=d['integrated_pairing_polynomial'] or [str(v) for v in E]!=d['center_even_polynomial']:raise ValueError('LINE')
if (ev(E,Q(1)),ev(P,Q(1)),ev(E,Q(1,2)),ev(P,Q(1,2)))!=(Q(8),Q(8),Q(-13,8),Q(-2421,128)):raise ValueError('TWO_FREQUENCIES')
pc=[];qc=[]
for i,a in enumerate(pcs):
 v=pair(a,p)
 if [str(x) for x in v]!=d['septic_corner_pairings'][i]:raise ValueError('P_PAIR')
 n,_=cover(v,d['septic_corner_proofs'][i],'STRICT_POSITIVITY');pc.append(n)
for i,a in enumerate(qcs):
 v=pair(a,c)
 if [str(x) for x in v]!=d['derivative_corner_pairings'][i]:raise ValueError('Q_PAIR')
 n,_=cover(v,d['derivative_corner_proofs'][i],'NONNEGATIVE_PROVED');qc.append(n)
# Different lower-order numerator q integrates to p itself with beta=1.
control=[Q(1)]+[Q(7,j+1)*q[j] for j in range(7)]
if control!=p:raise ValueError('POSITIVE_CONTROL')
print('independent derivative-lift obstruction:',{'p_corner_minors_positive':28,'q_corner_minors_positive':24,'p_leaf_counts':pc,
 'q_leaf_counts':qc,'q_center_margin':str(hmin),'q_uniform_margin':d['derivative_uniform_margin'],'p_uniform_margin':d['septic_center_margin'],
 'beta_lower':'-1','beta_upper':'-2421/208','different_numerator_positive_control':True})
