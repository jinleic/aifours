# Independent signed-monomial and Cramer replay of the fifth escape.
from fractions import Fraction as F
from math import lcm,factorial
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-fifth-forced-coefficient-escape-frozen-v1.json','d680463d33272b2a25b7bb74ad74ae2682a79eb97d04c7bd5a01b3a4e1fad313')
o=load('frontier-20261029-fifth-forced-coefficient-escape-open-frozen-v1.json','ebfb49a7aea63a0975978bdb018d467f7e7204e430e051ec1c7cfaa79172aa9a')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));b=list(map(F,box['good_numerator']));eps=F(1,10**10000);assert o['radius']=='10^-10000'
corners=[]
for e in (-1,1):
 for od in (-1,1):corners.append([(hi[j] if (e if j%2==0 else od)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0) for j in range(8)]
def det(M):
 A=[r[:] for r in M];n=len(A);v=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  if p!=k:A[k],A[p]=A[p],A[k];v=-v
  d=A[k][k];v*=d
  for i in range(k+1,n):
   f=A[i][k]/d
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
 return v
atoms=z['atoms'];assert len(atoms)==6 and all(0<=a['corner']<4 and 0<F(a['t'])<3000 and 0<int(a['weight'])<10**200 for a in atoms)
r=[row(corners[a['corner']],F(a['t'])) for a in atoms];w=[int(a['weight']) for a in atoms];C=[sum(w[i]*r[i][k] for i in range(6)) for k in range(8)]
assert list(map(str,C))==z['aggregate_coordinates'] and C[2]>0 and C[0]<0 and C[4]<0 and all(C[j]==0 for j in (1,3,5,6)) and C[7]==-11000*C[2]
assert hi[2]+eps<10500 and b[2]>11000*b[7]
zeros=z['zero_coordinate_indices'];piv=z['pivot_atom_positions'];free=[i for i in range(6) if i not in piv];assert zeros==[1,3,5,6] and len(piv)==4 and len(free)==2
A=[[r[p][j] for p in piv] for j in zeros];h=[-sum(w[f]*r[f][j] for f in free) for j in zeros];da=det(A);assert da!=0
for n,p in enumerate(piv):
 Ai=[v[:] for v in A]
 for i in range(4):Ai[i][n]=h[i]
 assert det(Ai)==da*w[p]
for vals,expected in [([v[2] for v in r],C[2]),([v[0] for v in r],C[0]),([v[4] for v in r],C[4]),([v[7]+10500*v[2] for v in r],C[7]+10500*C[2])]:
 aug=[A[i]+[h[i]] for i in range(4)]+[[vals[p] for p in piv]+[-sum(w[f]*vals[f] for f in free)]]
 assert expected!=0 and det(aug)==-da*expected
D=lcm(*(v.denominator for rr in r for v in rr));assert D<10**48
Mb=10**251;Lb=10**241;assert 2*factorial(6)*6*Mb**5*Lb*eps<F(1,D**6)
assert max(hi)<10**10 and eps<F(1,10**370) and 14*eps*sum(b)<F(box['good_compactified_margin'])
assert not all(x>0 for x in [-w[0]]+w[1:]) and C[7]+11001*C[2]>0
print({'target_coefficient':2,'anchor_lower_bound':11000,'open_lower_bound':10500,'positive_atoms':6,'zero_rank':4,'strict_negative_coordinates':[0,4],'positive_pivot_weights':4,'strict_augmented_determinants':4,'common_denominator_digits':len(str(D)),'open_radius':'10^-10000','good_numerator_margin_preserved':True,'mutation_controls':2})
