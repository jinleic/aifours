# Exact valid-box example where all five-node signs and the ratio obstruction
# hold, yet a positive-coefficient test numerator blocks every atom weight.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json').read_bytes();assert sha256(raw).hexdigest()=='3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293';z=json.loads(raw);lo=list(map(F,z['lower']));hi=list(map(F,z['upper']));b=list(map(F,z['good_numerator']));assert all(x>0 for x in b)
corners=[]
for e in (-1,1):
 for o in (-1,1):corners.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def parts(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
markers=[(F(1),-1,1),(F(3,2),-1,-1),(F(100),1,-1),(F(101),1,1),(F(2000),-1,1)]
for t,es,os in markers:
 for a in corners:
  e,o=parts(a,t);assert es*e>0 and os*o>0
samples=[(0,F(1001,1000)),(3,F(2997,2000)),(2,F(999,10)),(0,F(9999,100)),(0,F(101))];expected=[(-1,-1),(-1,1),(1,-1),(-1,-1),(1,1)];vals=[]
assert all(samples[i][1]<samples[i+1][1] for i in range(4))
for (ci,t),(es,os) in zip(samples,expected):
 e,o=parts(corners[ci],t);assert es*e>0 and os*o>0;E,O=parts(b,t);assert E*e+t*O*o>0;vals.append((e,o))
t2=samples[1][1];t3=samples[2][1];e2,o2=vals[1];e3,o3=vals[2]
assert t2*o2*e3>t3*(-o3)*(-e2)
print({'strict_marker_signs':40,'phase_sequence':[2,1,3,2,4],'strict_required_ratio':'r2>r3','positive_pairings_with_one_positive_coefficient_test':5,'scope':'necessary geometry is not sufficient; actual box has common numerator'})
