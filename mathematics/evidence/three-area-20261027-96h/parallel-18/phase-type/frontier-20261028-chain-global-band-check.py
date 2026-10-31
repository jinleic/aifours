#!/usr/bin/env python3
"""Check exact global-z obstruction for the specified PH7 3+3 chain.

All algebra is over Q. Uses local SymPy only for symbolic polynomial
identities and fractions.Fraction for Bernstein coefficients. Scope is the
single specified chain family, not all seven-state PH models.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp

u,z,t,h=sp.symbols('u z t h',real=True)
z0=sp.Rational(389,500)
a=3*u+3; b=3*u**2+9*u+3; c3=u**3+9*u**2+9*u+1; e4=3*u**3+9*u**2+3*u
h0=sp.expand(b+4*a-a*a-6)
L=sp.expand(b-4*a+10-2*z)
N=sp.expand(4*h0+4-c3-b*(4-a)-4*z)
qnum=sp.expand((a-4)*N+(h0-2*z)*L)
wnum=sp.expand(N+(4-a)*L)
Cnum=sp.expand(qnum-u*N+u*u*L)
phinum=sp.expand(e4*L+c3*wnum-(6+2*z)*qnum-(4+4*z)*N-(1+z)**2*L)
P=sp.expand(-phinum)
assert sp.expand(L-(3*u*u-3*u+1-2*z))==0
assert sp.expand(N-(8*u**3-9*u**2+3*u-4*z))==0
assert sp.expand(Cnum-((u*u+4*z)*(u-1)**2+2*z*(2*z-1)))==0
assert sp.factor(N.subs(z,(3*u*u-3*u+1)/2))==(u-1)*(8*u*u-7*u+2)
Pz=sp.expand(sp.diff(P,z).subs(u,1+t))
formula=t*t*(6*t*t-2*t+1)+(30*z-13)*t*t+(6*z-6)*t+18*z*z-6*z
assert sp.expand(Pz-formula)==0
disc=(6*z-6)**2-4*(30*z-13)*(18*z*z-6*z)
assert sp.expand((-disc).subs(z,sp.Rational(1,2)+h)-(2160*h**3+1548*h**2+312*h+3))==0

P0=sp.Poly(P.subs(z,z0),u)
poly=[F(int(sp.numer(v)),int(sp.denom(v))) for v in reversed(P0.all_coeffs())]
def bern(p,lo,hi):
    n=len(p)-1; w=hi-lo
    a=[sum(p[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
minima=[]; details={}
for k in range(8):
    lo=F(1)+F(k,16); hi=lo+F(1,16)
    cs=bern(poly,lo,hi)
    assert all(v>0 for v in cs)
    minima.append(min(cs)); details[f'{lo}:{hi}']=[str(v) for v in cs]
tail=sp.Poly(sp.expand(P0.as_expr().subs(u,sp.Rational(3,2)+t)),t)
tail_coeff=[F(int(sp.numer(v)),int(sp.denom(v))) for v in reversed(tail.all_coeffs())]
assert all(v>0 for v in tail_coeff)
report={
 'scope':'all real u>0, z>=389/500, one specified 3+3 PH7 chain and positive diagonal normalization',
 'exact_derived_identities':{'L':str(L),'N':str(N),'C_times_L':str(Cnum),
  'C_identity':'(u^2+4z)(u-1)^2+2z(2z-1)',
  'N_when_L_zero':'(u-1)(8u^2-7u+2)',
  'P':'-L*phi = '+str(P),
  'z_derivative_at_u_1_plus_t':str(Pz),
  'negative_quadratic_discriminant_at_z_half_plus_h':'2160 h^3+1548 h^2+312 h+3'},
 'z0':str(z0),'P_at_z0':str(P0.as_expr()),
 'bernstein_coefficients_eight_u_intervals':details,
 'bernstein_minimum_each_interval':[str(v) for v in minima],
 'global_min_bernstein':str(min(minima)),
 'positive_shift_coefficients_P0_at_u_3_over_2':[str(v) for v in tail_coeff],
 'result':'For z>=389/500, C>=0 forces L>0 and u>1; P=-L phi>0 for all u>=1, so phi<0. L=0 cannot satisfy coefficient equations. This excludes this chain, not arbitrary PH7.',
 'verification':'SymPy exact symbolic identities, Fraction exact Bernstein and shifted-power sign assertions; no floating-point or numeric-root proof.'}
out=ROOT/'frontier-20261028-chain-global-band-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('sympy',sp.__version__,'all exact identity/sign assertions PASS')
print('Bernstein min',min(minima),'positive tail coefficients',[str(x) for x in tail_coeff])
print('saved:',out)
