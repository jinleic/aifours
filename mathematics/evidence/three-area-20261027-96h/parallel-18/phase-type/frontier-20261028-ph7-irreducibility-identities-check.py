#!/usr/bin/env python3
"""Verify exact polynomial identities in the all-topology PH7 SCC barrier."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
r,z,u,s,delta=S.symbols('r z u s delta',real=True)
assert S.expand(3*(r*r+2*(1-z))-(r+2)**2-2*((1-r)**2-3*z))==0
assert S.expand(5*(r*r+4*(1-z))-(r+4)**2-4*((1-r)**2-5*z))==0
a=4+u;h=a/6;S2=4*(1-z)+u*u;S3=-4+12*z-u**3
t2=S.factor(S2-a*a/6);t3=S.factor(S3+3*h*S2-2*a**3/36)
assert S.expand(t2-(5*u*u-8*u+8-24*z)/6)==0
assert S.expand(t3+(u-2)*(5*u*u-2*u+18*z+2)/9)==0
T2=S.factor(t2.subs({u:2+s,z:S.Rational(1,2)+delta}))
T3=S.factor(t3.subs({u:2+s,z:S.Rational(1,2)+delta}))
T20=s*(5*s+12)/6;T30=-s*(5*s*s+18*s+27)/9
assert S.expand(T2-(T20-4*delta))==0
assert S.expand(T3-(T30-2*s*delta))==0
assert S.factor(S.Rational(8,15)*T20**3-T30**2+s*s*(30*s*s+116*s+135)/15)==0
out=ROOT/'frontier-20261028-ph7-irreducibility-identities-certificate.json'
out.write_text(json.dumps({'scope':'symbolic polynomial identities, not independent review or full proof of Perron/AM-GM facts',
 'identities':['3 and 5 state trace-square inequalities','6 state centered trace-square/cube expansions',
 'positive-delta monotonic differences and strictly negative delta-zero slack'],
 'six_barrier':'for u>=0 and z>1/2, centered 6-state Metzler necessary trace conditions contradict'},indent=2)+'\n')
print('SymPy',S.__version__,'exact 3/5/6 state SCC barrier identities PASS')
