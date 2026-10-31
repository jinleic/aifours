# Standalone exact replay of two full-width neighborhoods and their bounds.
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
src=frozen('frontier-20261028-fixed-parity-septic-examples-frozen-v1.json','bd032a29ef541d3e628209814ba8a8bdd79ec2a786d7b15c076d64e57319736b')
d=frozen('frontier-20261028-fixed-parity-full-width-frozen-v1.json','2a9cb307380db02fb28a343acaa5574592fd414ddf381049b44924acd534e7d5')
if d['source_examples_sha256']!='bd032a29ef541d3e628209814ba8a8bdd79ec2a786d7b15c076d64e57319736b':raise ValueError('SOURCE_BINDING')
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def pair(a,b):
 E=lambda p:[p[0],-p[2],p[4],-p[6]]
 O=lambda p:[p[1],-p[3],p[5],-p[7]]
 out=mul(E(a),E(b))+[Q(0)]
 for j,v in enumerate(mul(O(a),O(b))):out[j+1]+=v
 return out
def det(m):
 A=[[Q(v) for v in row] for row in m];out=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  v=A[k][k];out*=v
  for i in range(k+1,n):
   f=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
   A[i][k]=Q(0)
 return sgn*out
def minors(a):
 a=a[::-1]
 def c(k):return a[k] if 0<=k<8 else Q(0)
 return [det([[c(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
def beta(poly,left,right):
 n=len(poly)-1
 power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
 l,r=Q(item['left']),Q(item['right'])
 if not 0<=l<r<=1:raise ValueError('LEAF_RANGE')
 v=beta(poly,l,r)
 if v!=[Q(x) for x in item['coefficients']]:raise ValueError('LEAF_MISMATCH')
 if not all(x>0 for x in v):raise ValueError('LEAF_SIGN')
 return v
def bound(delta0,B,count,r):
 v=delta0-count*r*B
 if v<=0:raise ValueError('PERTURBATION_MARGIN')
 return v
results=[]
for ex in d['examples']:
 origin=next(v for v in src['examples'] if v['fixed']==ex['fixed']);fixed=(1,3,5) if ex['fixed']=='odd' else (0,2,4,6)
 r=Q(ex['radius']);lo=[Q(v) for v in origin['lower']];hi=[Q(v) for v in origin['upper']]
 for j in fixed:lo[j]-=r;hi[j]+=r
 if [str(x) for x in lo]!=ex['lower'] or [str(x) for x in hi]!=ex['upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
 b=[Q(v) for v in ex['numerator']]
 if ex['numerator']!=origin['numerator'] or not all(v>0 for v in b):raise ValueError('NUMERATOR')
 B=sum(abs(v) for v in b);delta0=Q(origin['margin']);delta=bound(delta0,B,len(fixed),r);S=1+sum(hi)
 if B!=Q(ex['B']) or delta0!=Q(ex['original_margin']) or len(fixed)*r*B!=Q(ex['perturbation_bound']) or delta!=Q(ex['extended_margin']) or S!=Q(ex['coefficient_sum_bound']) or delta/S**2!=Q(ex['ratio_margin']):raise ValueError('BOUND_BINDING')
 cs=corners(lo,hi)
 if not all(v>0 for a in cs for v in minors(a)):raise ValueError('HURWITZ')
 counts=[];all_values=[]
 for i,a in enumerate(cs):
  p=pair(a,b)
  if [str(x) for x in p]!=ex['direct_pairing_polynomials'][i]:raise ValueError('PAIR')
  proof=ex['direct_proofs'][i]
  if proof['status']!='STRICT_POSITIVITY':raise ValueError('STATUS')
  arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0)
  for item in arr:
   if Q(item['left'])!=at:raise ValueError('COVER')
   all_values.extend(leaf(p,item));at=Q(item['right'])
  if at!=1:raise ValueError('COVER')
  counts.append(len(arr))
 if min(all_values)!=Q(ex['direct_margin']):raise ValueError('DIRECT_MARGIN')
 results.append({'source_fixed':ex['fixed'],'positive_corner_minors':28,'leaf_counts':counts,'general_delta':str(delta),'direct_delta':str(min(all_values)),'ratio':str(delta/S**2)})
try:bound(Q(1),Q(1),1,Q(1))
except ValueError as e:
 if str(e)!='PERTURBATION_MARGIN':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent full-width neighborhood replay:',{'examples':results,'zero_margin_control_rejected':True})
