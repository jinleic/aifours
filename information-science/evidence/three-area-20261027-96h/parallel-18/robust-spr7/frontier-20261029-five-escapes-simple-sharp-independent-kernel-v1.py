# Independent monomial convolution and direct interval-to-Bernstein replay.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-five-escapes-simple-sharp-witness-frozen-v1.json','594947a89b7c0234e6baa3676e7934b1691f8680a21a790e18b7c17a796f1add')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));b=list(map(F,z['numerator_ascending']));eps=F(1,10**10000)
assert b==list(map(F,['149999/50','15007499/50','1467398223/100','6031551/25','4801697/2','247137/100','153011/100','1']))
assert all(v>0 for v in b) and b[7]==1 and all(lo[j]+F(1,100)<b[j]<hi[j]-F(1,100) for j in (0,1)) and all(b[j]>hi[j] for j in range(2,7))
corners=[]
for e in (-1,1):
 for o in (-1,1):corners.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def pair(a,b):
 p=[F(0)]*8
 for i in range(8):
  for j in range(8):
   if (i+j)%2==0:p[(i+j)//2]+=b[i]*a[j]*(-1)**((i+j)//2+j)
 return p
def compact(p):
 out=[F(0)]*8
 for k in range(8):
  for j in range(k,8):out[j]+=p[k]*comb(7-k,j-k)*(-1)**(j-k)
 return out
def bern(q,l,r):
 v=[sum(q[j]*comb(j,k)*l**(j-k)*(r-l)**k for j in range(k,8)) for k in range(8)]
 return [sum(v[k]*F(comb(i,k),comb(7,k)) for k in range(i+1)) for i in range(8)]
minimum=None;count=0
for i,a in enumerate(corners):
 q=compact(pair(a,b));last=F(0)
 for l,r in sorted((F(x),F(y)) for x,y in z['frequency_leaves'][i]):
  assert l==last and l<r<=1;values=bern(q,l,r);assert all(v>0 for v in values);minimum=min(values) if minimum is None else min(minimum,*values);count+=len(values);last=r
 assert last==1
assert minimum==F(z['minimum_bernstein_coefficient']) and minimum>F(1,10**10)
assert 14*eps*sum(b)<minimum and eps<F(1,100)
assert all(lo[j]+eps<hi[j]-eps for j in range(7)) and eps<F(1,10**370)
bad=b[:];bad[0]=0;assert compact(pair(corners[0],bad))[0]==0
print({'positive_bernstein_coefficients':count,'leaf_counts':[len(x) for x in z['frequency_leaves']],'b0_b1_each_distance_gt':'1/100','b2_to_b6_above_endpoints':True,'uniform_radius':'10^-10000','margin_gt':'1/10000000000','zero_b0_control':True})
