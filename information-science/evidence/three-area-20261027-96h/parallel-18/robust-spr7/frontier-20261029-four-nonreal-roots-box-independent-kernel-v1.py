# Independent exact arithmetic for a nonreal-root necessity example.
# All-member stability and root-count phase arguments are written deductions.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-four-nonreal-roots-box-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='58b4dade994bc008bdda290c11e8c3d352be9d2fe5379cc1911417678f42ae15':raise ValueError('PIN')
f=json.loads(raw)
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
p=[F(1),F(1)];q=[F(10001,10000),F(1,50),F(1)]
for _ in range(3):p=mul(p,q)
if list(map(str,p))!=f['center'] or list(map(str,p))!=f['numerator'] or p[7]!=1:raise ValueError('CENTER')
eta=F(1,100);A=1+eta*eta;c=F(f['factor_lower_c']);r=F(f['endpoint_radius']);S=sum(abs(x) for x in p)
qdiff=[A*A-c,-2*A+4*eta*eta-2*c,1-c];D=qdiff[1]**2-4*qdiff[0]*qdiff[2];delta=c**3
if list(map(str,qdiff))!=f['factor_difference_coefficients'] or D!=F(f['factor_difference_discriminant']) or not(D<0 and qdiff[2]>0):raise ValueError('QUAD_BOUND')
if delta!=F(f['anchor_compactified_margin']) or S!=F(f['numerator_coefficient_l1']) or not(14*r*S<=delta and all(x>r for x in p[:7])):raise ValueError('BOX_BOUND')
wlo,whi=map(F,f['endpoint_frequencies']);lo=A-wlo*wlo;hi=whi*whi-A;ilo=2*eta*wlo;ihi=2*eta*whi
if not(0<wlo<1<whi and lo>0 and hi>0 and ilo>0 and ihi>0):raise ValueError('PHASE_QUADRANT')
deficit=ilo/lo+ihi/hi
if deficit!=F(f['quadratic_phase_deficit_upper']) or not deficit<F(1,4):raise ValueError('PHASE_DEFICIT')
# log(whi/wlo)<whi/wlo-1=2/9, so seven real-root factors move <7/9;
# at most five real-root factors move <5/9. pi>3 is a written elementary import.
if not(whi/wlo-1==F(2,9) and F(5,2)*(whi/wlo-1)==F(5,9) and F(3,4)+F(5,9)<3):raise ValueError('PHASE_BUDGET')
print('nonreal-root box independent replay:',{'factor_expansion_degree':7,'quadratic_difference_discriminant':str(D),'positive_compact_margin':str(delta),'endpoint_radius':str(r),'quadratic_phase_deficit_upper':str(deficit),'real_factor_phase_budget':'5/9','scope':'every common monic septic numerator has at least two nonreal conjugate pairs; center numerator works throughout the stable box'})
