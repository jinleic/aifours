# Standalone exact replay using explicit reversal and differentiation.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-spr-reciprocal-operator-example-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='7637ba34ca2348aa440dbab6d3b531e28dc7487dfe8dd4ada3191793d5f7fa72':raise ValueError('HASH')
d=json.loads(raw)
def derivative(v):return [Q(j)*v[j] for j in range(1,len(v))]
def comp(v):return derivative(v[::-1])[::-1]
def op(v,h):
 rev=v[::-1];drv=derivative(rev);rev2=rev[:]
 for j,x in enumerate(drv):rev2[j]+=h*x
 return rev2[::-1]
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def parity(a):return [a[j]*(-1)**(j//2) for j in range(0,len(a),2)],[a[j]*(-1)**((j-1)//2) for j in range(1,len(a),2)]
def pair(a,b):
 E,O=parity(a);F,G=parity(b);x=mul(E,F);y=mul(O,G);out=x+[Q(0)]*max(0,len(y)+1-len(x))
 for j,v in enumerate(y):out[j+1]+=v
 return out
def det(m):
 A=[[Q(v) for v in row] for row in m];out=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  z=A[k][k];out*=z
  for i in range(k+1,n):
   f=A[i][k]/z
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
   A[i][k]=Q(0)
 return sgn*out
def minors(a):
 n=len(a)-1;c=a[::-1]
 def v(i):return c[i] if 0<=i<=n else Q(0)
 return [det([[v(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
def beta(poly,left,right):
 n=len(poly)-1;power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
 l,h=Q(item['left']),Q(item['right'])
 if not 0<=l<h<=1:raise ValueError('RANGE')
 vals=beta(poly,l,h)
 if vals!=[Q(x) for x in item['coefficients']]:raise ValueError('MISMATCH')
 if not all(x>0 for x in vals):raise ValueError('SIGN')
 return vals
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1;results=[];minor_count=0
for row in d['levels']:
 if row['operator']=='complement':aa=comp(a);bb=comp(b)
 elif row['operator']=='reciprocal_T':aa=op(a,Q(row['h']));bb=op(b,Q(row['h']))
 else:raise ValueError('OPERATOR')
 if [str(x) for x in aa]!=row['denominator'] or [str(x) for x in bb]!=row['numerator']:raise ValueError('TRANSFORM')
 allmin=minors(aa)+minors(bb);minor_count+=len(allmin)
 if not all(v>0 for v in allmin):raise ValueError('HURWITZ')
 P=pair(aa,bb)
 if [str(x) for x in P]!=row['pairing_polynomial']:raise ValueError('PAIR')
 proof=row['proof'];arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
 if proof['status']!='NONNEGATIVE_PROVED':raise ValueError('STATUS')
 for item in arr:
  if Q(item['left'])!=at:raise ValueError('COVER')
  values.extend(leaf(P,item));at=Q(item['right'])
 if at!=1 or min(values)!=Q(row['margin']):raise ValueError('MARGIN')
 results.append({'operator':row['operator'],'h':row['h'],'margin':str(min(values)),'leaves':len(arr)})
fault=deepcopy(d['levels'][0]['proof']['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
try:leaf(pair(comp(a),comp(b)),fault)
except ValueError as e:
 if str(e)!='MISMATCH':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent reciprocal operator replay:',{'levels':results,'positive_hurwitz_minors':minor_count,'corrupt_leaf_rejected':True})
