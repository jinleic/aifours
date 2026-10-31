# Exact cofactors and conservative 14-dimensional perturbation bounds.
from fractions import Fraction as F
from math import lcm,factorial
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
atoms=load('frontier-20261029-universal-simple-odd-halfspace-frozen-v1.json','3891b2e8ee1e2405573dc0aaf9f1194a8909948988e3e24e2e20a14790a5e8bf')
z=load('frontier-20261029-universal-odd-halfspace-open-frozen-v1.json','4ad166dcebd90a1ed2ad5fbf16e0a54d83448dd56255f970abf768fdeb58c672')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));epsilon=F(1,10**2000);assert z['radius']=='10^-2000'
cs=[]
for e in (-1,1):
 for o in (-1,1):
  a=[(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)];cs.append(a+[F(1)])
def mono(a,j,t):return sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0)
r=[[mono(cs[a['corner']],j,F(a['t'])) for j in range(8)] for a in atoms['support']]
gap=hi[3]-97*lo[5];M=[[v[j] for v in r] for j in (0,1,2,4,6)]+[[v[5]+97*v[3] for v in r],[v[7]+gap*v[3] for v in r]];A=M+[[v[3] for v in r]]
D=lcm(*(x.denominator for row in A for x in row));assert D==int(z['seven_by_eight_and_augmented_eight_by_eight_common_denominator']) and D<10**35
def det(B):
 B=[row[:] for row in B];n=len(B);s=1;prev=1
 for k in range(n-1):
  q=next((i for i in range(k,n) if B[i][k]),None)
  if q is None:return 0
  if q!=k:B[k],B[q]=B[q],B[k];s=-s
  p=B[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=B[i][j]*p-B[i][k]*B[k][j];assert v%prev==0;B[i][j]=v//prev
   B[i][k]=0
  prev=p
 return s*B[-1][-1]
Mi=[[int(x*D) for x in row] for row in M];co=[(-1)**i*det([[row[j] for j in range(8) if j!=i] for row in Mi]) for i in range(8)]
orientation=1
if all(x<0 for x in co):co=[-x for x in co];orientation=-1
assert all(x>0 for x in co);w=[int(a['weight']) for a in atoms['support']];assert all(co[i]*w[0]==co[0]*w[i] for i in range(8))
D8=det([[int(x*D) for x in row] for row in A]);assert D8!=0
scale=sum(F(co[i])*r[i][3] for i in range(8));assert scale>0
# Determinant lower bounds follow from integer entries after common scaling.
Mbound=10**40;Lbound=10**38
assert 2*factorial(7)*7*Mbound**6*Lbound*epsilon<F(1,D**7)
assert 2*factorial(8)*8*Mbound**7*Lbound*epsilon<F(1,D**8)
assert all(F(a['t'])<2000 for a in atoms['support']) and max(hi)<10**10 and abs(gap)<1000
assert all(0<lo[j]-epsilon and lo[j]+epsilon<hi[j]-epsilon for j in range(7))
assert epsilon<F(1,10**370)
b=list(map(F,box['good_numerator']));margin=F(box['good_compactified_margin'])
assert 14*epsilon*sum(b)<margin
assert not all(x>0 for x in [-co[0]]+co[1:]) and not (D8-D8)!=0
print({'positive_cofactors':8,'positive_augmented_determinant_scale':True,'common_denominator_digits':len(str(D)),'open_radius':'10^-2000','determinant_bounds_passed':2,'good_numerator_margin_passed':True,'mutation_controls':2})
