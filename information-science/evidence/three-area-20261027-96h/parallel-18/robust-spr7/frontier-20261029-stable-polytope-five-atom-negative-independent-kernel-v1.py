# Exact replay for a stable convex polytope with a five-atom negative sum.
# Its independent coefficient interval hull is explicitly unstable.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-stable-polytope-five-atom-negative-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='eca087b6a3290627a12b8121c8359f12b5b4814a839500a7638f331f2de61bab';z=json.loads(raw)
e2=list(map(F,z['E_middle_roots']));o1=list(map(F,z['O_first_roots']));lam=list(map(F,z['even_scales']));omega=list(map(F,z['frequencies']));w=list(map(int,z['integer_weights']));assert all(x>0 for x in lam+omega+w)
def cub(a,b,c,k=F(1)):return [k*a*b*c,-k*(a*b+a*c+b*c),k*(a+b+c),-k]
A=[]
for i in range(5):
 E=cub(F(1,2),e2[i],F(5),lam[i]);O=cub(o1[i],F(9,2),F(7));A.append([E[0],O[0],-E[1],-O[1],E[2],O[2],-E[3],-O[3]])
 assert F(1,2)<o1[i]<e2[i]<F(9,2)<F(5)<F(7)
def parts(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
def mono(a,j,t):return sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0)
C=[sum(w[i]*mono(A[i],j,omega[i]**2) for i in range(5)) for j in range(8)];assert list(map(str,C))==z['aggregate_coordinates'] and all(x<0 for x in C)
for t,es,os in z['markers_t_even_odd_sign']:
 for a in A:
  e,o=parts(a,F(t));assert es*e>0 and os*o>0
expected=[(-1,-1),(-1,1),(1,-1),(-1,-1),(1,1)];vals=[]
for i,(es,os) in enumerate(expected):
 e,o=parts(A[i],omega[i]**2);assert es*e>0 and os*o>0;vals.append((e,o))
e2v,o2v=vals[1];e3v,o3v=vals[2];assert omega[1]**2*o2v*e3v>omega[2]**2*(-o3v)*(-e2v)
def det(M):
 B=[r[:] for r in M];d=F(1)
 for j in range(len(B)):
  k=next((i for i in range(j,len(B)) if B[i][j]),None)
  if k is None:return F(0)
  if k!=j:B[j],B[k]=B[k],B[j];d=-d
  v=B[j][j];d*=v
  for i in range(j+1,len(B)):
   f=B[i][j]/v
   for l in range(j+1,len(B)):B[i][l]-=f*B[j][l]
 return d
def hurwitz(a,n):
 v=a[::-1];return det([[v[2*j-i+1] if 0<=2*j-i+1<8 else F(0) for j in range(n)] for i in range(n)])
assert all(hurwitz(a,j)>0 for a in A for j in range(1,8))
lo=[min(a[j] for a in A) for j in range(7)];hi=[max(a[j] for a in A) for j in range(7)];assert all(lo[j]<hi[j] for j in range(7));b=list(map(F,z['unstable_interval_member']));assert all(lo[j]<=b[j]<=hi[j] for j in range(7)) and b[7]==1 and hurwitz(b,3)==F(z['unstable_interval_member_H3'])<0
assert not all(x>0 for x in [-w[0]]+w[1:])
print({'individually_Hurwitz_minors':35,'common_marker_signs':60,'strict_negative_coordinates':8,'positive_integer_atom_weights':5,'common_root_bands':True,'strict_ratio_r2_gt_r3':True,'unstable_interval_member_H3':str(hurwitz(b,3)),'mutation_controls':1})
