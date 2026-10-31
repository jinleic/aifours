# Exact Cramer/augmented-determinant stability of four independent atom sums.
from fractions import Fraction as F
from math import lcm,factorial
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-four-forced-coefficient-escapes-frozen-v1.json','0880f38b67095511ce397296b19bc978a8fdb7a4a14255488fb95232a4268e28')
openz=load('frontier-20261029-four-forced-coefficient-escapes-open-frozen-v1.json','8376d4a53a457af8fea6da2722b07efd57968f0d0a6f19256e7e328e77d682e9')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));good=list(map(F,box['good_numerator']));eps=F(1,10**10000);assert openz['radius']=='10^-10000'
assert max(hi)<10**10 and all(0<lo[j]-eps and lo[j]+eps<hi[j]-eps for j in range(7))
corners=[]
for e in (-1,1):
 for o in (-1,1):corners.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0) for j in range(8)]
def det(M):
 A=[row[:] for row in M];n=len(A);d=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  if p!=k:A[k],A[p]=A[p],A[k];d=-d
  v=A[k][k];d*=v
  for i in range(k+1,n):
   f=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
 return d
records=[];allrows=[]
for cert in z['certificates']:
 atoms=cert['atoms'];assert all(0<F(a['t'])<2000 and 0<int(a['weight'])<10**200 for a in atoms)
 rows=[row(corners[a['corner']],F(a['t'])) for a in atoms];allrows+=rows;weights=[int(a['weight']) for a in atoms];zeros=cert['zero_coordinate_indices'];negative=cert['negative_coordinate_indices'];piv=cert['pivot_atom_positions'];free=[i for i in range(len(atoms)) if i not in piv];q=len(zeros)
 assert q==len(piv)<=5 and 1<=len(free)<=2
 A=[[rows[p][k] for p in piv] for k in zeros];h=[-sum(weights[f]*rows[f][k] for f in free) for k in zeros];da=det(A);assert da!=0
 for n,p in enumerate(piv):
  replaced=[a[:] for a in A]
  for i in range(q):replaced[i][n]=h[i]
  assert det(replaced)==da*weights[p]
 C=[sum(weights[i]*rows[i][k] for i in range(len(rows))) for k in range(8)];j=cert['target_index'];T=cert['open_threshold'];assert T==openz['open_lower_bounds'][str(j)] and T<=10**6
 assert all(C[k]==0 for k in zeros) and all(C[k]<0 for k in negative) and C[j]>0 and C[7]+T*C[j]<0 and hi[j]+eps<T
 tests=[([v[j] for v in rows],C[j])]+[([v[k] for v in rows],C[k]) for k in negative]+[([v[7]+T*v[j] for v in rows],C[7]+T*C[j])]
 for vals,expected in tests:
  bottom=[vals[p] for p in piv]+[-sum(weights[f]*vals[f] for f in free)];aug=[A[i]+[h[i]] for i in range(q)]+[bottom]
  assert det(aug)==-da*expected and det(aug)!=0
 records.append({'target':j,'fixed_free_weights':len(free),'positive_pivot_weights':q,'negative_coordinate_tests':len(negative),'augmented_determinants':len(tests),'open_threshold':T})
D=lcm(*(v.denominator for R in allrows for v in R));assert D<10**37
Mb=10**251;Lb=10**241;assert 2*factorial(6)*6*Mb**5*Lb*eps<F(1,D**6)
assert eps<F(1,10**370) and 14*eps*sum(good)<F(box['good_compactified_margin'])
print({'open_radius':'10^-10000','common_denominator_digits':len(str(D)),'records':records,'uniform_determinant_bound_passed':True,'good_numerator_margin_preserved':True})
