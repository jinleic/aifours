#!/usr/bin/env python3
"""Exact Hessian certificate for strict local spectral maximality at v4.

The companion first-order certificate supplies 34 strictly adverse new-edge
costs. Here the exact full tangent Hessian is shown negative definite for
all eight existing-edge directions, using rational polynomial interval bounds.
"""
from fractions import Fraction as Fr
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,v,a,z,y=S.symbols('u v a z y',real=True)
x1,x2,x3,x4,aa,bb,v1,v2,zz=S.symbols('x1 x2 x3 x4 aa bb v1 v2 zz',real=True)
X=[x1,x2,x3,x4,aa,bb,v1,v2,zz];xx=X[:4]
centers=[Fr(1338787907,10**9),Fr(1042029691,10**9),Fr(871488314,10**9),Fr(820420441,10**9)]
radii=[Fr(2,10**9),Fr(2,10**9),Fr(1,10**6),Fr(2,10**9)]

def bound(expr):
 P=S.Poly(S.expand(expr),u,v,a,z);mid=Fr(0);err=Fr(0)
 for powers,c in P.terms():
  coeff=Fr(int(S.numer(c)),int(S.denom(c)));t=Fr(1);ma=Fr(1)
  for j,k in enumerate(powers):t*=centers[j]**k;ma*=(abs(centers[j])+radii[j])**k
  mid+=coeff*t;err+=abs(coeff)*(ma-abs(t))
 return mid-err,mid+err

# Actual row-generator determinant in the eight-edge face; not a free polynomial.
poly=S.prod(y+x for x in xx)*(y+aa+bb)*(y+v1)*(y+v2)-S.prod(xx)*(aa*(y+v1)*(y+v2)+bb*v1*v2)
P=S.Poly(S.expand(poly),y);p=P.nth(6)-4;q=P.nth(5)-4*p-(6+2*zz)
F=S.Matrix([P.nth(4)-(4*q+(6+2*zz)*p+4+4*zz),
 P.nth(3)-((6+2*zz)*q+(4+4*zz)*p+(1+zz)**2),
 P.nth(2)-((4+4*zz)*q+(1+zz)**2*p),P.nth(1)-(1+zz)**2*q])
base={x1:u,x2:u,x3:u,x4:u,aa:a,bb:u-a,v1:v,v2:v,zz:z}
J=F.jacobian(X).subs(base);dep=[0,4,6,8];K=J[:,dep].T
D=S.expand(K.det(method='berkowitz'));nvec=[S.expand(K.cofactor(3,i))for i in range(4)]
assert bound(D)[0]>Fr(-30) and bound(D)[1]<Fr(-20)
assert centers[0]-radii[0] > centers[2]+radii[2] > 0
k=u/(u-a)
Z=S.Matrix.hstack(S.Matrix([-1,1,0,0,0,0,0,0,0]),
 S.Matrix([-1,0,1,0,0,0,0,0,0]),S.Matrix([-1,0,0,1,0,0,0,0,0]),
 S.Matrix([-k,0,0,0,k-1,1,0,0,0]),S.Matrix([0,0,0,0,0,0,-1,1,0]))
assert all(S.cancel(t)==0 for t in J*Z)
assert S.expand(sum(nvec[i]*J[i,8]for i in range(4))-D)==0
for j in range(8):assert S.expand(sum(nvec[i]*J[i,j]for i in range(4)))==0
Hs=[S.hessian(F[i],X).subs(base)for i in range(4)]
# Numerator of the reduced Lagrangian Hessian: actual Hessian is Hnum/D.
HN=S.zeros(5)
for i in range(5):
 for j in range(5):
  HN[i,j]=S.cancel(-sum(nvec[h]*(Z[:,i].T*Hs[h]*Z[:,j])[0]for h in range(4)))
d=HN[0,1];ell=HN[4,4]
shape=S.Matrix([[2*d,d,d,k*d,0],[d,2*d,d,k*d,0],[d,d,2*d,k*d,0],
                [k*d,k*d,k*d,2*k*k*d,0],[0,0,0,0,ell]])
assert all(S.cancel(HN[i,j]-shape[i,j])==0 for i in range(5)for j in range(5))
assert bound(d)[0]>8 and bound(ell)[0]>30
out=ROOT/'frontier-20261028-ph7-all-edge-second-order-certificate.json'
out.write_text(json.dumps({'root_box':'v4/first-order certified U,V,z radius 2e-9, a radius 1e-6',
 'dependent_coordinates':['edge1-2','edge5-1','edge6-7','z'],
 'free_coordinates':['edge2-3','edge3-4','edge4-5','edge5-6','edge7-1'],
 'det_K_box':'(-30,-20)','Hnum12_lower':'>8','Hnum55_lower':'>30',
 'reduced_hessian':'d/D*[[2,1,1,k],[1,2,1,k],[1,1,2,k],[k,k,k,2k^2]] direct-sum ell/D',
 'conclusion':'negative definite on full five-dimensional active-edge tangent',
 'scope':'local spectral maximum, when combined with strict first-order absent-edge signs'},indent=2)+'\n')
print('SymPy',S.__version__,'exact tangent Hessian negative definite PASS: 5 active directions')
