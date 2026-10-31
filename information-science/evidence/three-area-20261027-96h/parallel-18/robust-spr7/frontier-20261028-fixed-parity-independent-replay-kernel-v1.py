# Standalone exact replay of two fixed-parity septic examples.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def frozen(name,digest):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=digest:raise ValueError('HASH:'+name)
 return json.loads(raw)
d=frozen('frontier-20261028-fixed-parity-septic-examples-frozen-v1.json','bd032a29ef541d3e628209814ba8a8bdd79ec2a786d7b15c076d64e57319736b')
f=frozen('frontier-20261028-five-contact-uniform-numerator-frozen-v1.json','ca236e378ba9e5d9d8686dfe5e7cbc718799edfd59ff6a21bd51104fe7723c45')
lo0=[Q(v) for v in f['boundary_lower']];hi0=[Q(v) for v in f['boundary_upper']];center=[(lo0[j]+hi0[j])/2 for j in range(7)]+[Q(1)]
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def parity(a):return [a[0],-a[2],a[4],-a[6]],[a[1],-a[3],a[5],-a[7]]
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
def det(m):
 A=[[Q(x) for x in row] for row in m];out=Q(1);sign=1;n=len(A)
 for k in range(n):
  r=next((i for i in range(k,n) if A[i][k]),None)
  if r is None:return Q(0)
  if r!=k:A[k],A[r]=A[r],A[k];sign=-sign
  pivot=A[k][k];out*=pivot
  for i in range(k+1,n):
   q=A[i][k]/pivot
   for j in range(k+1,n):A[i][j]-=q*A[k][j]
   A[i][k]=Q(0)
 return sign*out
def minors(a):
 c=a[::-1]
 def v(k):return c[k] if 0<=k<8 else Q(0)
 return [det([[v(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
def pair(a,b):
 E,O=parity(a);F,G=parity(b);p=mul(E,F)+[Q(0)]
 for j,x in enumerate(mul(O,G)):p[j+1]+=x
 return p
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
 l,r=Q(item['left']),Q(item['right'])
 if not 0<=l<r<=1:raise ValueError('LEAF_RANGE')
 coeff=beta(poly,l,r)
 if coeff!=[Q(v) for v in item['coefficients']]:raise ValueError('LEAF_MISMATCH')
 if not all(v>0 for v in coeff):raise ValueError('LEAF_SIGN')
 return coeff
def cover(poly,proof):
 if proof['status']!='STRICT_POSITIVITY':raise ValueError('STATUS')
 arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
 for item in arr:
  if Q(item['left'])!=at:raise ValueError('COVER')
  values.extend(leaf(poly,item));at=Q(item['right'])
 if at!=1:raise ValueError('COVER')
 return len(arr),values
all_results=[]
for ex in d['examples']:
 kind=ex['fixed'];lo=[Q(v) for v in ex['lower']];hi=[Q(v) for v in ex['upper']];eps=Q(ex['epsilon']);b=[Q(v) for v in ex['numerator']]
 ids=(1,3,5) if kind=='odd' else (0,2,4,6)
 if not all(lo[j]==hi[j]==center[j] for j in ids):raise ValueError('FIXED_PARITY')
 for j in range(7):
  if j not in ids and (lo[j]!=center[j]-(hi0[j]-lo0[j])/4 or hi[j]!=center[j]+(hi0[j]-lo0[j])/4):raise ValueError('SUBBOX')
 if len(b)!=8 or not b[-1]>0:raise ValueError('DEGREE')
 E,O=parity(center);F,G=parity(b)
 if kind=='odd':
  zeta=Q(ex['zeta']);der=[j*O[j] for j in range(1,4)];want=mul([-zeta,Q(1)],der)
  if F!=[eps*v for v in want] or G!=O:raise ValueError('ODD_FORMULA')
  if not 0<zeta<Q(1):raise ValueError('ZETA')
  # Standard (uncompactified) cubic Bernstein coefficients on [0,1].
  ocoeff=[sum(O[k]*Q(comb(i,k),comb(3,k)) for k in range(i+1)) for i in range(4)]
  if not all(v>0 for v in ocoeff):raise ValueError('O_POSITIVE')
 elif kind=='even':
  eta=Q(ex['eta']);der=[j*E[j] for j in range(1,4)];want=[-v for v in der]+[-eta]
  if F!=E or G!=[eps*v for v in want]:raise ValueError('EVEN_FORMULA')
 else:raise ValueError('KIND')
 cs=corners(lo,hi)
 if not all(v>0 for a in cs for v in minors(a)):raise ValueError('HURWITZ')
 counts=[];values=[]
 for i,a in enumerate(cs):
  p=pair(a,b)
  if [str(v) for v in p]!=ex['pairing_polynomials'][i]:raise ValueError('PAIR')
  n,co=cover(p,ex['proofs'][i]);counts.append(n);values.extend(co)
 delta=min(values)
 if delta!=Q(ex['margin']):raise ValueError('MARGIN')
 all_results.append({'fixed':kind,'positive_corner_minors':28,'leaf_counts':counts,'margin':str(delta),'formula_reconstructed':True})
fault=deepcopy(d['examples'][0]['proofs'][0]['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
try:leaf(pair(corners([Q(x) for x in d['examples'][0]['lower']],[Q(x) for x in d['examples'][0]['upper']])[0],[Q(x) for x in d['examples'][0]['numerator']]),fault)
except ValueError as e:
 if str(e)!='LEAF_MISMATCH':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent fixed-parity replay:',{'examples':all_results,'odd_O_positive_on_0_1':True,'corrupt_leaf_rejected':True})
