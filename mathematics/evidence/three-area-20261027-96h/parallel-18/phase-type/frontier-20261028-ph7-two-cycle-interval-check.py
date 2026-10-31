#!/usr/bin/env python3
"""Rational contraction certificate for a two-cycle PH7 endpoint.

Proves a unique real zero of the three formal coefficient equations in an
explicit rational box using a rational preconditioned contraction. Verifies
all sign predicates on a whole z interval uniformly over the rate box, plus
full exact matrix coefficient identities. No floating root is a proof input.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp
u,v,z,y=sp.symbols('u v z y',real=True)
s,t,r=sp.symbols('s t r',real=True)
center=[F(1338787907,10**9),F(1042029691,10**9),F(820420441,10**9)]
rad=F(1,10**7)
S=lambda x:sp.Rational(x.numerator,x.denominator)

p0=5*u+2*v-4
q0=10*u*u+10*u*v-20*u+v*v-8*v-2*z+10
Dz=y*((y+1)**2+z)**2
R=sp.Poly(sp.expand((y+u)**5*(y+v)**2-Dz*(y*y+p0*y+q0)),y)
D1=R.coeff_monomial(y**2)
E4=R.coeff_monomial(y**4);E3=R.coeff_monomial(y**3);E1=sp.expand(R.coeff_monomial(y)-2*v*D1)
D3=sp.expand(R.coeff_monomial(1)-v*v*D1)
FF=sp.Matrix([E4,E3,E1]);JJ=FF.jacobian([u,v,z])
cv={u:S(center[0]),v:S(center[1]),z:S(center[2])}
J0=JJ.subs(cv); A=J0.inv(); assert A*J0==sp.eye(3)


def frac(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def local_bound(poly,variables,centers,radius):
    shifts=sp.symbols('x0:'+str(len(variables)))
    expanded=sp.Poly(sp.expand(poly.subs({x:S(c)+d for x,c,d in zip(variables,centers,shifts)})),*shifts)
    c0=F(0);error=F(0)
    for powers,co in expanded.terms():
        f=frac(co)
        if sum(powers)==0:c0=f
        else:error+=abs(f)*radius**sum(powers)
    return c0,error

# Rational norm bound for I-A*J(X), using A*J(center)=I exactly.
errJ=[[local_bound(JJ[i,j],[u,v,z],center,rad)[1]for j in range(3)]for i in range(3)]
qbound=max(sum(sum(abs(frac(A[i,k]))*errJ[k][j] for k in range(3)) for j in range(3)) for i in range(3))
res=A*FF.subs(cv);bbound=max(abs(frac(x))for x in res)
assert qbound<F(1,100) and bbound<rad/F(100)
assert bbound+qbound*rad<rad

# Generic nonuniform-family numerators for fixed unknown u,v and arbitrary z.
rates=[u,u,u,u,v,v]; ee={k:sum(sp.prod(a)for a in combinations(rates,k))for k in range(1,7)}
a,b,c3,e4,e5,e6=(ee[k]for k in range(1,7));h0=b+4*a-a*a-6
L=sp.expand(b-4*a+10-2*z);N=sp.expand(4*h0+4-c3-b*(4-a)-4*z)
p=N/L;q=(a-4)*p+h0-2*z;w=p+4-a;B=p-2*u;C=q-u*p+u*u
phi=e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
R2=e5+e4*w-(4+4*z)*q-(1+z)**2*p
R1=e6+e5*w-(1+z)**2*q;R0=e6*w
D1g=R2-3*u*phi;D2g=R1-3*u*u*phi-2*v*D1g;D3g=R0-u**3*phi-v*v*D1g-v*D2g
poly={name:sp.cancel(expr*L)for name,expr in {'p':p,'q':q,'w':w,'B':B,'C':C,'phi':phi,'D1':D1g,'D2':D2g,'D3':D3g}.items()}
assert all(sp.denom(expr)==1 for expr in poly.values())
assert sp.expand(E4-(L*p0-N))==0

# Bernstein coefficients in z, each a polynomial in u,v. Bound each coefficient
# uniformly over the rate box by exact centered-polynomial triangle bounds.
lo=F(7,9);hi=F(820421,10**6)
def bern_z(expr):
    P=sp.Poly(sp.expand(expr),z); n=P.degree(); cs=[P.nth(i)for i in range(n+1)]
    power=[sum(cs[i]*comb(i,j)*S(lo)**(i-j)*S(hi-lo)**j for i in range(j,n+1))for j in range(n+1)]
    return [sp.expand(sum(power[j]*sp.Rational(comb(k,j),comb(n,j))for j in range(k+1)))for k in range(n+1)]

def cert_lower(expr,threshold):
    margins=[]
    for coeff in bern_z(expr):
        c0,err=local_bound(coeff,[u,v],center[:2],rad)
        margins.append(c0-err)
    assert min(margins)>threshold,(min(margins),threshold)
    return min(margins)

def cert_upper(expr,threshold):
    bounds=[]
    for coeff in bern_z(expr):
        c0,err=local_bound(coeff,[u,v],center[:2],rad)
        bounds.append(c0+err)
    assert max(bounds)<threshold,(max(bounds),threshold)
    return max(bounds)

thresholds={'L':F(1),'p':F(7),'q':F(9),'w':F(2),'B':F(3),'C':F(2),'D1':F(3),'D3':F(2)}
margin={name:cert_lower(L if name=='L' else poly[name],floor)for name,floor in thresholds.items()}
upper_phi=cert_upper(sp.diff(poly['phi'],z),F(-6))
upper_d2=cert_upper(sp.diff(poly['D2'],z),F(-9,10))

# Independent formal identity for the two-cycle matrix with D1,D3 as defined.
G=sp.zeros(7)
for i in range(5):G[i,i]=-u
G[5,5]=G[6,6]=-v
for i in range(6):G[i,i+1]=1
G[4,0]=D1;G[6,0]=D3
matrix_char=sp.expand((y*sp.eye(7)-G).det(method='domain-ge'))
assert sp.expand(matrix_char-((y+u)**5*(y+v)**2-D1*(y+v)**2-D3))==0
assert sp.expand(matrix_char-Dz*(y*y+p0*y+q0)-(E4*y**4+E3*y**3+E1*y))==0
assert center[2]-rad>F(82041,100000) and center[2]+rad<F(8,9)

report={'center':[str(x)for x in center],'box_radius':str(rad),
 'contraction_norm_upper':'<1/100','center_error_upper':'<radius/100',
 'contraction_exact_q':str(qbound),'contraction_exact_center_error':str(bbound),
 'equations':['E4=[y^4]R=0','E3=[y^3]R=0','E1=[y]R-2v[y^2]R=0'],
 'R':'(y+u)^5(y+v)^2-y((y+1)^2+z)^2(y^2+p0*y+q0)',
 'p0':'5u+2v-4','q0':'10u^2+10uv-20u+v^2-8v-2z+10',
 'root_bounds_z':[str(center[2]-rad),str(center[2]+rad)],
 'interval_z_for_sign_certificate':[str(lo),str(hi)],
 'certified_lower_thresholds':{k:str(v)for k,v in thresholds.items()},
 'certified_derivative_upper_thresholds':{'d_z_Lphi':'-6','d_z_LD2':'-9/10'},
 'certified_exact_coefficient_bounds':{k:str(v)for k,v in margin.items()},
 'certified_exact_derivative_upper_bounds':{'d_z_Lphi':str(upper_phi),'d_z_LD2':str(upper_d2)},
 'checks':['rational contraction maps closed box into itself and has norm <1/100',
           'all z-Bernstein signs hold uniformly on rate box by rational centered-polynomial bounds',
           'full 7x7 two-cycle characteristic residual equals E4*y^4+E3*y^3+E1*y'],
 'scope':'explicit isolated algebraic PH7 family endpoint and interval, not optimality or z=8/9'}
out=ROOT/'frontier-20261028-ph7-two-cycle-interval-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'exact rational contraction/interval signs/matrix identity PASS')
print('q <1/100, center error < radius/100; root z in',center[2]-rad,center[2]+rad)
print('all positivity floors',thresholds,'derivatives < -6 and -9/10')
print('saved:',out)
