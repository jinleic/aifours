# Standalone exact replay of 28 D^k(I+hD) example pairings.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-spr-operator-hierarchy-example-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='0c4c3977ab80ff30918342a16a48c5eb640bc7ec8eb35b5c3cd2e249b8a2789c':raise ValueError('HASH')
d=json.loads(raw)
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
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1;results=[]
for k in range(7):
 n=7-k
 for offset,h in enumerate((Q(0),Q(1,10),Q(1),Q(10))):
  row=d['levels'][4*k+offset]
  if row['order']!=k or Q(row['h'])!=h:raise ValueError('ORDER')
  aa=a[:];bb=b[:]
  for j in range(n):aa[j]+=h*(j+1)*a[j+1];bb[j]+=h*(j+1)*b[j+1]
  expected=mul([Q(comb(n-1,j)) for j in range(n)],[Q(1)+n*h,Q(1)])
  if aa!=expected or [str(x) for x in aa]!=row['denominator'] or [str(x) for x in bb]!=row['numerator']:raise ValueError('TRANSFORM')
  H=pair(aa,bb)
  if [str(x) for x in H]!=row['pairing_polynomial']:raise ValueError('PAIR')
  proof=row['proof'];arr=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);vals=[]
  if proof['status']!='NONNEGATIVE_PROVED':raise ValueError('STATUS')
  for item in arr:
   if Q(item['left'])!=at:raise ValueError('COVER')
   vals.extend(leaf(H,item));at=Q(item['right'])
  if at!=1 or min(vals)!=Q(row['margin']):raise ValueError('MARGIN')
  results.append({'order':k,'h':str(h),'margin':str(min(vals)),'leaves':len(arr)})
 if n>1:a=[Q(j+1,n)*a[j+1] for j in range(n)];b=[Q(j+1,n)*b[j+1] for j in range(n)]
fault=deepcopy(d['levels'][0]['proof']['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
a=[Q(comb(7,j)) for j in range(8)];b=a[:];b[1]+=1
try:leaf(pair(a,b),fault)
except ValueError as e:
 if str(e)!='MISMATCH':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent operator hierarchy:',{'levels':len(results),'min_margin':str(min(Q(x['margin']) for x in results)),
 'max_leaves':max(x['leaves'] for x in results),'denominator_factorizations':len(results),'corrupt_leaf_rejected':True})
