# Independently reconstruct signed-monomial pairings and every reported
# compactified Bernstein leaf by direct affine power substitution.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-five-coefficient-escapes-sharp-witness-frozen-v1.json','df61870ceb3b93214af97180e3ed8bbd06f639db0b3a57f6ef556d9effd087c9')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));b=list(map(F,z['numerator_ascending']));eps=F(1,10**10000)
assert b[7]==1 and all(v>0 for v in b)
assert all(lo[j]+eps<b[j]<hi[j]-eps and hi[j]-b[j]==F(1,100) for j in (0,1))
assert all(b[j]>hi[j] for j in range(2,7))
cs=[]
for e in (-1,1):
 for o in (-1,1):cs.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def pairing(a,b):
 p=[F(0)]*8
 for i in range(8):
  for j in range(8):
   if (i+j)%2==0:p[(i+j)//2]+=b[i]*a[j]*(-1)**((i+j)//2+j)
 return p
def compactify(p):
 out=[F(0)]*8
 for k in range(8):
  for j in range(k,8):out[j]+=p[k]*comb(7-k,j-k)*(-1)**(j-k)
 return out
def direct_bern(q,left,right):
 power=[sum(q[j]*comb(j,k)*left**(j-k)*(right-left)**k for j in range(k,8)) for k in range(8)]
 return [sum(power[k]*F(comb(i,k),comb(7,k)) for k in range(i+1)) for i in range(8)]
minimum=None;count=0
for ci,a in enumerate(cs):
 q=compactify(pairing(a,b));leaves=sorted([(F(x),F(y)) for x,y in z['frequency_leaves'][ci]]);last=F(0)
 for l,r in leaves:
  assert l==last and l<r<=1
  vals=direct_bern(q,l,r);assert all(v>0 for v in vals);minimum=min(vals) if minimum is None else min(minimum,*vals);last=r;count+=len(vals)
 assert last==1
assert minimum==F(z['minimum_bernstein_coefficient']) and 14*eps*sum(b)<minimum
assert all(lo[j]+eps<hi[j]-eps for j in range(7)) and eps<F(1,10**370)
# Mutating b0 to zero violates the strict compactified left endpoint.
bad=b[:];bad[0]=0;assert compactify(pairing(cs[0],bad))[0]==0
print({'strict_positive_bernstein_coefficients':count,'partition_leaf_counts':[len(x) for x in z['frequency_leaves']],'b0_b1_inside_with_slack':'1/100','b2_through_b6_above_box':True,'uniform_open_radius':'10^-10000','margin_preserved':True,'zero_b0_mutation_rejected':True})
