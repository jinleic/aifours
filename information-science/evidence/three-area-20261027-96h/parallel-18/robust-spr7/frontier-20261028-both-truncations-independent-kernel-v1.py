# Standalone exact replay: the stable frozen septic center has an unstable
# constant-truncated tail AND an unstable leading-term-truncated head.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
p=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-hurwitz-septic-unstable-tail-frozen-v1.json')
raw=p.read_bytes()
if sha256(raw).hexdigest()!='0c275cf02ae54a1f24185ff4bc3b6732903a06160fc5dee53492d9a7692dfd7c':raise ValueError('HASH')
d=json.loads(raw);a=[Q(v) for v in d['center']];tail=a[1:];head=a[:-1];reverse_tail=[v/head[0] for v in head[::-1]]
def det(m):
 M=[[Q(v) for v in row] for row in m];out=Q(1);sign=1;n=len(M)
 for k in range(n):
  i=next((i for i in range(k,n) if M[i][k]),None)
  if i is None:return Q(0)
  if i!=k:M[k],M[i]=M[i],M[k];sign=-sign
  p=M[k][k];out*=p
  for i in range(k+1,n):
   q=M[i][k]/p
   for j in range(k+1,n):M[i][j]-=q*M[k][j]
   M[i][k]=Q(0)
 return sign*out
def minor(poly,k):
 c=poly[::-1];return det([[c[2*j-i] if 0<=2*j-i<len(c) else Q(0) for j in range(1,k+1)] for i in range(1,k+1)])
t5=minor(tail,5);h4=minor(head,4);r5=minor(reverse_tail,5)
if t5!=Q(-1933582924) or h4!=Q(-7108113901) or r5!=Q(-103753464527335,584911245809539914512):raise ValueError('MINOR_BINDING')
if not(t5<0 and h4<0 and r5<0):raise ValueError('SIGN')
print('independent two-sided truncation replay:',{'tail_delta5':str(t5),'head_delta4':str(h4),'reciprocal_tail_delta5':str(r5),
 'head_coefficients':[str(v) for v in head],'reciprocal_tail_coefficients':[str(v) for v in reverse_tail]})
