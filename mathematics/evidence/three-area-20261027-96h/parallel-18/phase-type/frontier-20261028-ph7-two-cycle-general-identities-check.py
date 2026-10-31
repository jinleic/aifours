#!/usr/bin/env python3
"""Exact symbolic full-matrix and all-c normalizer checks for v4 family."""
from itertools import combinations
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,v,z,y,c,w,phi,d1,d2,d3,B,C,K=S.symbols('u v z y c w phi d1 d2 d3 B C K')
G=S.zeros(7)
for i,rate in enumerate([u,u,u,w,u,v,v]):G[i,i]=-rate
for i in range(6):G[i,i+1]=1
G[4,0]=d1;G[5,0]=d2;G[6,0]=d3;G[6,3]=phi
M=y*S.eye(7)-G;beta=S.Matrix([[C,B,1,0,0,0,0]]);e7=S.Matrix([0,0,0,0,0,0,1])
char=M.det(method='berkowitz')
closed=(y+w)*(y+u)**4*(y+v)**2-phi*(y+u)**3-d1*(y+v)**2-d2*(y+v)-d3
assert S.expand(char-closed)==0
Q=(y+u)**2+B*(y+u)+C
assert S.expand((M+e7*beta).det(method='berkowitz')-char-Q)==0

# At free symbolic parameters, the six noncentral recurrence rows are exact.
# The center-row residual reduces to det(cI-G)-K*Q(c), with positive factors.
Qc=Q.subs(y,c);h1=1/Qc;h2=(c+u)*h1;h3=(c+u)*h2;h4=(c+u)*h3
h7=(K+d3*h1+phi*h4)/(c+v);h6=(h7+d2*h1)/(c+v);h5=(h6+d1*h1)/(c+u)
h=S.Matrix([h1,h2,h3,h4,h5,h6,h7]);rows=(c*S.eye(7)-G)*h-K*e7
for i in [0,1,2,4,5,6]:assert S.cancel(rows[i])==0
assert S.cancel((beta*h)[0]-1)==0
assert S.cancel(rows[3]*Qc*(c+u)*(c+v)**2-(char.subs(y,c)-K*Qc))==0

# Insert the v4 algebraic family symbolically, not a rational rate sample.
rates=[u,u,u,u,v,v];e={j:sum(S.prod(a)for a in combinations(rates,j))for j in range(1,7)}
a,b,c3,e4,e5,e6=(e[j]for j in range(1,7));H=b+4*a-a*a-6
L=b-4*a+10-2*z;N=4*H+4-c3-b*(4-a)-4*z
p=N/L;q=(a-4)*p+H-2*z;W=p+4-a;BB=p-2*u;CC=q-u*p+u*u
ph=e4+c3*W-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
R2=e5+e4*W-(4+4*z)*q-(1+z)**2*p
R1=e6+e5*W-(1+z)**2*q;R0=e6*W
D1=R2-3*u*ph;D2=R1-3*u*u*ph-2*v*D1;D3=R0-u**3*ph-v*v*D1-v*D2
sub={w:W,phi:ph,d1:D1,d2:D2,d3:D3,B:BB,C:CC}
Dz=y*((y+1)**2+z)**2;Qt=y*y+p*y+q
assert S.cancel(Q.subs(sub)-Qt)==0
# Clear the single common denominator and compare the complete y polynomial.
# The free-parameter center-row identity above then implies the last row for
# K=D_z(c); avoid expanding the same huge substituted rational seven times.
residual=S.cancel((closed.subs(sub)-Dz*Qt)*L)
assert S.Poly(residual,y).is_zero
out=ROOT/'frontier-20261028-ph7-two-cycle-general-identities-certificate.json'
out.write_text(json.dumps({'scope':'all symbolic U,V,z and c where shown denominators nonzero',
 'checks':['full 7x7 determinant for free raw feedback','full actual adjugate numerator for free B,C',
 'all seven raw normalizer rows symbolically after family substitution','beta*h=1',
 'symbolic general-U,V,z family determinant is D_z*Q'],
 'method':'exact SymPy polynomial/rational identity expansion, no floating arithmetic'},indent=2)+'\n')
print('SymPy',S.__version__,'symbolic U,V,z,c full matrix/adjugate/all-normalizer PASS')
