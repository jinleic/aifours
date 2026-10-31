# Reconstruct actual monomial pairings, exact universal halfspace, and the
# cofactor/determinant neighborhood; no optimizer or producer import.
from fractions import Fraction as F
from math import lcm,factorial
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
atoms=load('frontier-20261029-universal-simple-even-halfspace-frozen-v1.json','91074e96c0e7c201380c348247551658485fd81a1c93aacfc9c37800e7408487')
z=load('frontier-20261029-universal-even-halfspace-open-frozen-v1.json','d6cc440cf07351675680929a662f144e6be49353fcb0b3cbd64f8b56dd7ee223')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));eps=F(1,10**2000);assert z['radius']=='10^-2000' and all(0<lo[j]-eps and lo[j]+eps<hi[j]-eps for j in range(7))
cs=[]
for e in (-1,1):
 for o in (-1,1):cs.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):
 return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0) for j in range(8)]
s=atoms['support'];assert len(s)==8 and all(int(a['weight'])>0 and F(a['t'])>0 and 0<=a['corner']<4 for a in s)
r=[row(cs[a['corner']],F(a['t'])) for a in s];w=[int(a['weight']) for a in s];C=[sum(w[i]*r[i][j] for i in range(8)) for j in range(8)]
d=hi[0]-2*lo[2]+20*hi[4];assert d==F(atoms['threshold_hi0_minus_2lo2_plus_20hi4'])==F(66093999512432059,2000000000000)
assert C[0]>0 and [str(v/C[0]) for v in C]==atoms['expected_normalized_monomial_coordinates']
good=list(map(F,box['good_numerator']));assert good[0]-2*good[2]+20*good[4]-d*good[7]>0
M=[[r[i][j] for i in range(8)] for j in (1,3,5,6)]+[[v[2]+2*v[0] for v in r],[v[4]-20*v[0] for v in r],[v[7]+d*v[0] for v in r]];A=M+[[v[0] for v in r]];D=lcm(*(x.denominator for row in A for x in row));assert D==int(z['common_denominator']) and D<10**37
def det(B):
 B=[r[:] for r in B];n=len(B);sgn=1;prev=1
 for k in range(n-1):
  q=next((i for i in range(k,n) if B[i][k]),None)
  if q is None:return 0
  if q!=k:B[k],B[q]=B[q],B[k];sgn=-sgn
  v=B[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    a=B[i][j]*v-B[i][k]*B[k][j];assert a%prev==0;B[i][j]=a//prev
   B[i][k]=0
  prev=v
 return sgn*B[-1][-1]
Mi=[[int(x*D) for x in row] for row in M];co=[(-1)**i*det([[row[j] for j in range(8) if j!=i] for row in Mi]) for i in range(8)]
if all(x<0 for x in co):co=[-x for x in co]
assert all(x>0 for x in co) and all(co[i]*w[0]==co[0]*w[i] for i in range(8))
assert det([[int(x*D) for x in row] for row in A])!=0 and sum(F(co[i])*r[i][0] for i in range(8))>0
Mb=10**43;Lb=10**39
assert 2*factorial(7)*7*Mb**6*Lb*eps<F(1,D**7) and 2*factorial(8)*8*Mb**7*Lb*eps<F(1,D**8)
assert max(hi)<10**10 and abs(d)<10**5 and all(F(a['t'])<2000 for a in s)
assert eps<F(1,10**370) and 14*eps*sum(good)<F(box['good_compactified_margin'])
assert not all(x>0 for x in [-co[0]]+co[1:])
print({'positive_atoms':8,'exact_even_halfspace':'b0 - 2*b2 + 20*b4 > (66093999512432059/2000000000000)*b7','free_odd_coordinates':[1,3,5],'positive_cofactors':8,'augmented_determinant_nonzero':True,'endpoint_radius':'10^-2000','determinant_bound_checks':2,'good_numerator_margin_preserved':True,'mutation_controls':1})
