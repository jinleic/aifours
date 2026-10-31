#!/usr/bin/env python3
"""All-order JLL check at trace-square-forced shift 31/6, exactly."""
from fractions import Fraction as F
from pathlib import Path
import json
z=F(8,9);t=F(31,6);R=F(83,100)
assert t*t+(12-t)**2/6-F(310,9)==F(7,216)>0
assert F(657,961)<R*R
A10=1+F(13,31)**10+F(1,31)**10+4*R**10
A1=1+F(13,31)+F(1,31)+4*R;B20=1-4*R**20
assert 1-4*R**10>0 and B20>0 and A10<7 and A1<7
assert A10*A10<7*B20 and 7*(A1/7)**20<B20
C=F(1);D=F(0);s=[]
for k in range(9*19+1):
 s.append(t**k+(t-3)**k+(t-5)**k+4*C)
 C,D=(t-1)*C-z*D,C+(t-1)*D
assert all(s[k]>0 for k in range(1,10))
pairs=0
for k in range(1,10):
 for m in range(2,20):
  assert s[k]**m<7**(m-1)*s[k*m],(k,m)
  pairs+=1
out=Path(__file__).resolve().parent/'frontier-20261028-ph7-jll-sharp-shift-certificate.json'
out.write_text(json.dumps({'forced_shift':'31/6','diagonal_Cauchy_margin':'7/216',
 'spectral_ratio_upper':'sqrt(657)/31 < 83/100','finite_k_1to9_m_2to19_pairs':pairs,
 'proof':'nonnegative power sums and all strict JLL by exact finite check plus rational geometric tails',
 'scope':'necessary spectral constraints only; no nonnegative matrix or PH witness'},indent=2)+'\n')
print('Exact Fraction PASS: shift31/6 forced, all power sums and all JLL inequalities; finite pairs',pairs)
