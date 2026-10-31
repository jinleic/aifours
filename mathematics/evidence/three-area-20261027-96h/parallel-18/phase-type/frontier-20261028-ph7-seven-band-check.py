#!/usr/bin/env python3
"""Certify a nonuniform 3+3 PH7 band using exact symbolic arithmetic.

For fixed positive rational six-chain rates, derive all coefficients from the
SAME matrix, check the full determinant and adjugate numerator as polynomial
identities in y,z, and establish their strict signs via exact Bernstein
coefficients on [7/9,813/1000]. This is a checked construction, not a proof of
an optimal endpoint or formal/independent acceptance.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp
z,y=sp.symbols('z y', real=True)
u1,u2,u3,v1,v2,v3=map(sp.Rational,['657/500','34/25','701/500','333/250','973/1000','1083/1000'])
rates=[u1,u2,u3,v1,v2,v3]
A1=sum(rates); A2=sum(rates[i]*rates[j] for i in range(6) for j in range(i+1,6))
A3=sum(rates[i]*rates[j]*rates[k] for i in range(6) for j in range(i+1,6) for k in range(j+1,6))
A4=sum(rates[i]*rates[j]*rates[k]*rates[l] for i in range(6) for j in range(i+1,6) for k in range(j+1,6) for l in range(k+1,6))
A5=sum(sp.prod(rates[j] for j in range(6) if j!=i) for i in range(6)); A6=sp.prod(rates)
h0=A2+4*A1-A1**2-6; L=sp.expand(A2-4*A1+10-2*z)
N=sp.expand(4*h0+4-A3-A2*(4-A1)-4*z)
p=N/L; q=(A1-4)*p+h0-2*z; w=p+4-A1
B=p-u1-u2; C=q-u1*u2-u1*B
phi=A4+A3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
R2=A5+A4*w-(4+4*z)*q-(1+z)**2*p
R1=A6+A5*w-(1+z)**2*q; R0=A6*w
D1=R2-phi*(u1+u2+u3)
D2=R1-phi*(u1*u2+u1*u3+u2*u3)-(v2+v3)*D1
D3=R0-phi*u1*u2*u3-v2*v3*D1-v3*D2
items={'L':L,'p':p,'q':q,'w':w,'B':B,'C':C,'phi':phi,'D1':D1,'D2':D2,'D3':D3}
assert all(sp.denom(sp.cancel(v*L))==1 for k,v in items.items() if k!='L')

G=sp.zeros(7)
for i,r in enumerate([u1,u2,u3,w,v1,v2,v3]): G[i,i]=-r
for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)): G[i,j]=1
G[4,0],G[5,0],G[6,0],G[6,3]=D1,D2,D3,phi
M=y*sp.eye(7)-G
U=sp.prod(y+u for u in (u1,u2,u3)); V=sp.prod(y+v for v in (v1,v2,v3))
Dz=y*((y+1)**2+z)**2; Q=y*y+p*y+q
# Symbolic 7x7 determinant and direct first-column/last-column cofactor identity.
assert sp.cancel(M.det(method='domain-ge')-Dz*Q)==0
beta=sp.Matrix([[C,B,1,0,0,0,0]])
gamma=sp.Matrix([0,0,0,0,0,0,1])
# Adjugate identity is checked using determinant rank-one update, not assumed.
assert sp.cancel((M+gamma*beta).det(method='domain-ge')-M.det(method='domain-ge')-Q)==0

def frac(x): return F(int(sp.numer(x)),int(sp.denom(x)))
def bern(poly,lo,hi):
    p=sp.Poly(sp.cancel(poly),z)
    if p.is_zero: return [F(0)]
    cs=[frac(v) for v in reversed(p.all_coeffs())]; n=len(cs)-1; w=hi-lo
    power=[sum(cs[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(power[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
lo=F(7,9); hi=F(813,1000)
cert={}
for name,expr in items.items():
    polynomial=expr if name=='L' else sp.cancel(expr*L)
    c=bern(polynomial,lo,hi)
    assert all(v>0 for v in c),(name,c)
    cert[name]=[str(v) for v in c]
report={'z_interval':[str(lo),str(hi)],'rates':[str(v) for v in rates],
        'rational_coefficients':{k:str(sp.factor(v)) for k,v in items.items()},
        'positive_bernstein_coefficients_for_L_and_L_times_others':cert,
        'checks':['actual symbolic 7x7 det(yI-G)=D_z(y)Q(y) for all y,z',
                  'actual symbolic adjugate numerator factor Q via rank-one determinant update',
                  'L and all nine L-times-coefficients strictly positive on entire closed z interval'],
        'scope':'actual common-matrix PH7 upper bound in indicated interval, all c,d>0 after positive normalization; not global optimum or 8/9'}
out=ROOT/'frontier-20261028-ph7-seven-band-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'Fraction exact symbolic determinant/numerator/positivity assertions PASS')
for name,cs in cert.items(): print(name,', '.join(cs))
print('saved:',out)
