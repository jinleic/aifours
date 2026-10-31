#!/usr/bin/env python3
"""Exact coefficient identity for a 5/7 theta graph with unequal outer rates."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
s,e2,t,r,z,y,delta=S.symbols('s e2 t r z y delta',real=True)
p=s+t-4;q=e2+t*s+r-4*p-(6+2*z)
T=S.Poly(S.expand(y*((y+1)**2+z)**2*(y*y+p*y+q)),y)
e3=S.factor(T.nth(4)-t*e2-r*s);e4=S.factor(T.nth(3)-t*e3-r*e2)
F=S.factor((r-t*t)*e4-t*r*e3-T.nth(1)+t*T.nth(2))
L=S.factor(T.nth(2)-t*e4-r*e3)
C=S.factor(-S.diff(F,e2));B=S.factor(F.subs(e2,0));assert S.expand(F-(B-C*e2))==0
M=(r-t+1-z)**2+z*(t-2)**2
assert S.cancel(L.subs(e2,B/C)*C-(s-4)*M**2)==0
Cdelta=S.factor(16*C.subs(r,(t*t-delta)/4))
expected=delta**2+2*delta*(5*t*t-16*t+4*z+12)+(t*t-4*t+4*z+4)*(5*t*t-12*t+4*z+4)
assert S.expand(Cdelta-expected)==0
assert S.expand(t*t-4*t+4*z+4-((t-2)**2+4*z))==0
assert S.expand(5*t*t-12*t+4*z+4-(5*(t-S.Rational(6,5))**2+4*z-S.Rational(16,5)))==0
assert S.expand(5*t*t-16*t+4*z+12-(5*(t-S.Rational(8,5))**2+4*z-S.Rational(4,5)))==0
out=ROOT/'frontier-20261028-ph7-theta-unequal-outer-invariant-certificate.json'
out.write_text(json.dumps({'scope':'all real common rates, two positive real outer rates, positive long cycle; z>4/5',
 'definitions':{'t':'v1+v2','r':'v1*v2','delta':'t^2-4r',
  'C':'negative e2-coefficient of F','B':'F at e2=0','M':'(r-t+1-z)^2+z*(t-2)^2'},
 'identity':'L=(s-4)*M^2/C after F=0','C_delta_SOS':str(expected),
 'conclusion':'C>0 and M>0, hence positive long cycle forces s>4'},indent=2)+'\n')
print('SymPy',S.__version__,'exact all-variable unequal-outer theta identity and C sum-of-squares PASS')
