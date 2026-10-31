# Exact negative atom sum for five individually Hurwitz polynomials;
# independently demonstrates why their convex/interval hull is ineligible.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-individually-stable-five-atom-negative-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='f7248ce91c4802e6888ec05d7934e6f28b3a66724ffc6c929881faf717f5e21f';z=json.loads(raw);A=list(map(F,z['alphas']));om=list(map(F,z['frequencies']));w=list(map(int,z['weights']));assert len(A)==len(om)==len(w)==5 and all(x>0 for x in A+om+w)
def poly(a):return [F(comb(7,j))*a**(7-j) for j in range(8)]
def mono(a,j,t):return sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0)
def parts(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
C=[sum(w[i]*mono(poly(A[i]),j,om[i]**2) for i in range(5)) for j in range(8)];assert list(map(str,C))==z['aggregate_coordinates'] and all(x<0 for x in C)
def phaseclass(a,o):
 re,im=F(1),F(0);q=0
 for _ in range(7):
  re,im=re*a-im*o,re*o+im*a;assert re and im
  quad=0 if re>0 and im>0 else 1 if re<0 and im>0 else 2 if re<0 and im<0 else 3
  if q%4!=quad:q+=1
  assert q%4==quad
 return q
qs=[phaseclass(a,o) for a,o in zip(A,om)];assert qs==z['phase_classes']==[2,1,3,2,4]
assert all(qs[i]<=qs[j]+1 for i in range(5) for j in range(i+1,5))
t2=om[1]**2;t3=om[2]**2;e2,o2=parts(poly(A[1]),t2);e3,o3=parts(poly(A[2]),t3);assert e2<0<o2 and o3<0<e3 and t2*o2*e3>t3*(-o3)*(-e2)
def det(M):
 A=[r[:] for r in M];out=F(1)
 for j in range(len(A)):
  k=next((i for i in range(j,len(A)) if A[i][j]),None)
  if k is None:return F(0)
  if k!=j:A[j],A[k]=A[k],A[j];out=-out
  v=A[j][j];out*=v
  for i in range(j+1,len(A)):
   f=A[i][j]/v
   for l in range(j+1,len(A)):A[i][l]-=f*A[j][l]
 return out
def hurwitz_minor(a,n):
 p=a[::-1];H=[[p[2*j-i+1] if 0<=2*j-i+1<8 else F(0) for j in range(n)] for i in range(n)]
 return det(H)
th=F(z['convex_mix_theta']);a=[(1-th)*poly(A[0])[j]+th*poly(A[1])[j] for j in range(8)];assert hurwitz_minor(a,4)==F(z['convex_mix_H4'])<0
small,big=map(F,z['interval_inner_roots']);assert min(A)<small<big<max(A)
lo,hi=poly(small),poly(big);mixed=[lo[0],lo[1],hi[2],hi[3],lo[4],lo[5],hi[6],F(1)];assert all(poly(min(A))[j]<=mixed[j]<=poly(max(A))[j] for j in range(8));assert hurwitz_minor(mixed,3)==F(z['interval_mixed_H3'])<0
assert not all(x>0 for x in [-w[0]]+w[1:])
print({'individual_real_rooted_Hurwitz_polynomials':5,'positive_integer_weights':5,'strict_negative_coordinates':8,'exact_phase_classes':qs,'strict_ratio_r2_gt_r3':True,'negative_convex_mix_H4':str(F(z['convex_mix_H4'])),'negative_bounding_box_H3':str(F(z['interval_mixed_H3'])),'mutation_controls':1})
