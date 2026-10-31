# Standalone exact replay of a pointwise mixed-operator obstruction.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
p=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-spr-operator-point-obstruction-frozen-v1.json')
raw=p.read_bytes()
if sha256(raw).hexdigest()!='7c11c8486c61f362e23e68119c8040a265bb2081e998af416fef73ed27b36f34':raise ValueError('HASH')
d=json.loads(raw)
def roots(rs):
 v=[Q(1)]
 for r in rs:
  z=[Q(0)]*(len(v)+1)
  for j,x in enumerate(v):z[j]+=Q(r)*x;z[j+1]+=x
  v=z
 return v
a=roots(d['a_roots']);b=roots(d['b_roots'])
if [str(x) for x in a]!=d['a'] or [str(x) for x in b]!=d['b']:raise ValueError('ROOT_FACTORS')
def derivative(v):return [Q(j)*v[j] for j in range(1,len(v))]
def add(a,b):
 z=[Q(0)]*max(len(a),len(b))
 for j,v in enumerate(a):z[j]+=v
 for j,v in enumerate(b):z[j]+=v
 return z
def pair(a,b,t):
 def parity(v):return sum(v[j]*(-t)**(j//2) for j in range(0,len(v),2)),sum(v[j]*(-t)**((j-1)//2) for j in range(1,len(v),2))
 E,O=parity(a);F,G=parity(b);return E*F+t*O*G,E*E+t*O*O
def det(m):
 A=[[Q(x) for x in row] for row in m];out=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  v=A[k][k];out*=v
  for i in range(k+1,n):
   z=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=z*A[k][j]
   A[i][k]=Q(0)
 return sgn*out
def minors(a):
 n=len(a)-1;c=a[::-1]
 def v(k):return c[k] if 0<=k<=n else Q(0)
 return [det([[v(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,n+1)]
ad=derivative(a);bd=derivative(b);am=add(a,ad);bm=add(b,bd)
if not all(v>0 for poly in (a,b,ad,bd,am,bm) for v in minors(poly)):raise ValueError('HURWITZ')
t=Q(d['t']);p0,d0=pair(a,b,t);p2,d2=pair(ad,bd,t);pm,dm=pair(am,bm,t);p1=pm-p0-p2
if [str(p0),str(p1),str(p2)]!=d['pairing_quadratic_in_h'] or str(pm)!=d['mixed_h1_pairing']:raise ValueError('PAIRING')
if not(p0>0 and p2>0 and pm<0) or [str(p0/d0),str(p2/d2),str(pm/dm)]!=[d['original_ratio'],d['derivative_ratio'],d['mixed_ratio']]:raise ValueError('SIGN')
print('independent mixed-operator point:',{'positive_minors':40,'t':str(t),'original_pairing':str(p0),'derivative_pairing':str(p2),
 'cross_term':str(p1),'mixed_pairing':str(pm),'ratios':[str(p0/d0),str(p2/d2),str(pm/dm)]})
