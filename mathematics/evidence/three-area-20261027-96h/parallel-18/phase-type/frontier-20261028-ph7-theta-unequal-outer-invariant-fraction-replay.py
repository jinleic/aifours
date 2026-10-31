#!/usr/bin/env python3
"""Independent exact interpolation proof of unequal-outer theta identities."""
from fractions import Fraction as Q
from itertools import product

def mul(a,b):
 o=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o

def quantities(s,e,t,r,z):
 p=s+t-4;q=e+t*s+r-4*p-(6+2*z)
 D=mul([Q(0),Q(1)],mul([1+z,Q(2),Q(1)],[1+z,Q(2),Q(1)]))
 T=mul(D,[q,p,Q(1)]);e3=T[4]-t*e-r*s;e4=T[3]-t*e3-r*e
 F=(r-t*t)*e4-t*r*e3-T[1]+t*T[2]
 L=T[2]-t*e4-r*e3
 return F,L

# Identity in (s,t,r,z): each side has degrees bounded respectively by
# (2,8,4,4). Cartesian-grid interpolation proves the polynomial equality.
for s0,t0,r0,z0 in product(range(3),range(9),range(5),range(5)):
 s,t,r,z=map(Q,(s0,t0,r0,z0));F0,L0=quantities(s,Q(0),t,r,z);F1,L1=quantities(s,Q(1),t,r,z)
 C=F0-F1;B=F0;M=(r-t+1-z)**2+z*(t-2)**2
 assert C*L0+(L1-L0)*B==(s-4)*M*M,(s,t,r,z)

# C after r=(t^2-delta)/4, with multidegrees <=(4,2,2).
for t0,delta0,z0 in product(range(5),range(3),range(3)):
 t,delta,z=map(Q,(t0,delta0,z0));r=(t*t-delta)/4
 f0,_=quantities(Q(0),Q(0),t,r,z);f1,_=quantities(Q(0),Q(1),t,r,z);C=f0-f1
 rhs=delta**2+2*delta*(5*t*t-16*t+4*z+12)+(t*t-4*t+4*z+4)*(5*t*t-12*t+4*z+4)
 assert 16*C==rhs,(t,delta,z)
print('Independent stdlib Fraction PASS: 675 multivariate identity values and 45 SOS identity values, exact degree bounds')
