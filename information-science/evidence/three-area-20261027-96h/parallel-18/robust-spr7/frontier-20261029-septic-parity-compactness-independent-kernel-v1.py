from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-septic-parity-compactness-frozen-v1.json').read_bytes()
assert sha256(raw).hexdigest()=='23f31c32eee919cd958bf6e58d640123f029e086390f81d63f1457544928e2c9'
z=json.loads(raw)
def factor(rs):
 out=[F(-1)]
 for x in rs:
  n=[F(0)]*(len(out)+1)
  for i,v in enumerate(out):n[i]-=x*v;n[i+1]+=v
  out=n
 return out
def det(a):
 A=[r[:] for r in a];p=F(1)
 for j in range(len(A)):
  k=next((i for i in range(j,len(A)) if A[i][j]),None)
  if k is None:return F(0)
  if j!=k:A[j],A[k]=A[k],A[j];p=-p
  v=A[j][j];p*=v
  for i in range(j+1,len(A)):
   fac=A[i][j]/v
   for k in range(j+1,len(A)):A[i][k]-=fac*A[j][k]
 return p
def hminor(a):
 v=a[::-1];H=[[v[2*j-i+1] if 0<=2*j-i+1<8 else F(0) for j in range(7)] for i in range(7)]
 return [det([r[:k] for r in H[:k]]) for k in range(1,8)]
odd=list(map(F,z['shared_odd_part']));oroot=list(map(F,z['shared_odd_roots']));assert odd==factor(oroot)
for tag in ('A','B'):
 even=list(map(F,z['even_'+tag]));eroot=list(map(F,z['even_'+tag+'_roots']));assert even==factor(eroot)
 assert all(eroot[j]<oroot[j] for j in range(3)) and all(oroot[j]<eroot[j+1] for j in range(2))
 a=[even[0],odd[0],-even[1],-odd[1],even[2],odd[2],-even[3],-odd[3]]
 minors=hminor(a);assert minors==list(map(F,z['N1_hurwitz_minors_'+tag])) and all(x>0 for x in minors)
 t=F(z['point_t']);assert sum(x*t**i for i,x in enumerate(even))==F(z['even_'+tag+'_at_point'])
assert F(z['even_A_at_point'])<0<F(z['even_B_at_point'])
print({'positive_Hurwitz_minors':14,'exact_factorizations':3,'interlaced_reference_pairs':2,'opposite_even_signs':'5/8'})
