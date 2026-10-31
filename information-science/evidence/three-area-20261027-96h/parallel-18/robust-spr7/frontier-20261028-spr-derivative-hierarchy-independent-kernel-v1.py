# Standalone exact replay of seven normalized derivative pairings.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-spr-derivative-hierarchy-example-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='166c1adc298d35dfb90c89187ca70a5a7a846a8f6e81776a8e3bbc124dc674c2':raise ValueError('HASH')
d=json.loads(raw)
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def parity(a):return [a[j]*(-1)**(j//2) for j in range(0,len(a),2)],[a[j]*(-1)**((j-1)//2) for j in range(1,len(a),2)]
def pair(a,b):
 E,O=parity(a);F,G=parity(b);u=mul(E,F);v=mul(O,G);out=u+[Q(0)]*max(0,len(v)+1-len(u))
 for j,x in enumerate(v):out[j+1]+=x
 return out
def beta(poly,left,right):
 n=len(poly)-1;power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
 sub=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
 return [sum(sub[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
 l,h=Q(item['left']),Q(item['right'])
 if not 0<=l<h<=1:raise ValueError('RANGE')
 v=beta(poly,l,h)
 if v!=[Q(x) for x in item['coefficients']]:raise ValueError('MISMATCH')
 if not all(x>0 for x in v):raise ValueError('SIGN')
 return v
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1;result=[]
for k,row in enumerate(d['levels']):
 if row['derivative_order']!=k or [str(x) for x in a]!=row['denominator'] or [str(x) for x in b]!=row['numerator']:raise ValueError('RECURRENCE')
 n=7-k
 if a!=[Q(comb(n,j)) for j in range(n+1)]:raise ValueError('STABLE_BINOMIAL')
 H=pair(a,b)
 if [str(x) for x in H]!=row['pairing_polynomial']:raise ValueError('PAIR')
 proof=row['proof'];arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
 if proof['status']!='NONNEGATIVE_PROVED':raise ValueError('STATUS')
 for item in arr:
  if Q(item['left'])!=at:raise ValueError('COVER')
  values.extend(leaf(H,item));at=Q(item['right'])
 if at!=1 or min(values)!=Q(row['margin']):raise ValueError('MARGIN')
 result.append({'order':k,'degree':n,'leaves':len(arr),'margin':str(min(values))})
 if n>1:a=[Q(j+1,n)*a[j+1] for j in range(n)];b=[Q(j+1,n)*b[j+1] for j in range(n)]
fault=deepcopy(d['levels'][0]['proof']['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
a0=[Q(comb(7,j)) for j in range(8)];b0=a0[:];b0[1]+=1
try:leaf(pair(a0,b0),fault)
except ValueError as e:
 if str(e)!='MISMATCH':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent derivative hierarchy:',{'levels':result,'corrupt_leaf_rejected':True})
