#!/usr/bin/env python3
"""Independent exact k3 certificate for the illustrative q=4/5,z=1/10 point."""
from pathlib import Path
from fractions import Fraction as F
import json
ns={}
exec((Path(__file__).parent/'review-check.py').read_text().split('\nresult=')[0],ns)
G=ns['G']; q=F(4,5); z=F(1,10)
M=ns['tensor_output'](q,{0:G(1),3:G(z),5:G(z),15:G(z)})
c1=F(81,125);c2=F(73,1000)
i1=ns['inertia_ldl'](ns['shift'](M,c1));i2=ns['inertia_ldl'](ns['shift'](M,c2))
assert i1==(16,0,0) and i2==(15,1,0)
a,b=(1+q)/2,(1-q)/2
ref=a**4+2*a**3*b; cap=c1+2*c2
assert ref==F(8019,10000) and cap==F(397,500) and ref-cap==F(79,10000)
print(json.dumps({'q':str(q),'z':str(z),'lambda1_bound':str(c1),'lambda1_shift_inertia':i1,'lambda2_and_3_bound':str(c2),'lambda2_shift_inertia':i2,'reference':str(ref),'top3_cap':str(cap),'strict_gap_lower':str(ref-cap)},indent=2))
