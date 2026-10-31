#!/usr/bin/env python3
"""Exact 42-edge tangent dual at the isolated algebraic v4 endpoint.

The root is imported from its existing rational contraction certificate. The
full coefficient Jacobian is formed from literal 7x7 rank-one edge changes.
All 34 absent-edge dual costs exceed 1/100 on a rigorously bounded root box.
The resulting statement is FIRST ORDER only, not a local/global optimum.
"""
from fractions import Fraction as Fr
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,v,a,z,y=S.symbols('u v a z y',real=True)
centers=[Fr(1338787907,10**9),Fr(1042029691,10**9),Fr(871488314,10**9),Fr(820420441,10**9)]
radii=[Fr(2,10**9),Fr(2,10**9),Fr(1,10**6),Fr(2,10**9)]
endpoint=json.loads((ROOT/'frontier-20261028-ph7-two-cycle-interval-certificate.json').read_text())
qbound=Fr(endpoint['contraction_exact_q']); bbound=Fr(endpoint['contraction_exact_center_error'])
assert 0<=qbound<Fr(1,100) and bbound<Fr(1,10**9) and bbound/(1-qbound)<radii[0]

def bound(expr):
 P=S.Poly(S.expand(expr),u,v,a,z);mid=Fr(0);err=Fr(0)
 for powers,c in P.terms():
  coeff=Fr(int(S.numer(c)),int(S.denom(c)));x=Fr(1);xx=Fr(1)
  for j,k in enumerate(powers):x*=centers[j]**k;xx*=(abs(centers[j])+radii[j])**k
  mid+=coeff*x;err+=abs(coeff)*(xx-abs(x))
 return mid-err,mid+err

p0=5*u+2*v-4;q0=10*u*u+10*u*v-20*u+v*v-8*v-2*z+10
RR=S.Poly(S.expand((y+u)**5*(y+v)**2-y*((y+1)**2+z)**2*(y*y+p0*y+q0)),y)
D1=RR.nth(2);ac,ar=centers[2],radii[2]
SL=lambda x:S.Rational(x.numerator,x.denominator)
assert bound(D1-SL(ac-ar)*u**4)[0]>0
assert bound(SL(ac+ar)*u**4-D1)[0]>0

# Exact endpoint Markov representative: rates U on four upstream edges;
# at row 4, rates a and U-a; two downstream rates V.
G=S.zeros(7)
for i in range(5):G[i,i]=-u
for i in range(5):G[i,i+1]=u
G[4,0]=a;G[4,5]=u-a;G[5,5]=-v;G[5,6]=v;G[6,6]=-v;G[6,0]=v
M=y*S.eye(7)-G;P=S.expand(M.det(method='berkowitz'));PC=S.Poly(P,y)
p=PC.nth(6)-4;q=PC.nth(5)-4*p-(6+2*z)
T1=(1+z)**2*q;T2=(4+4*z)*q+(1+z)**2*p
T3=(6+2*z)*q+(4+4*z)*p+(1+z)**2;T4=4*q+(6+2*z)*p+4+4*z
FF=S.Matrix([PC.nth(4)-T4,PC.nth(3)-T3,PC.nth(2)-T2,PC.nth(1)-T1]);Jz=FF.diff(z)

def Jedge(i,j):
 bumped=M.copy();bumped[i,i]+=1;bumped[i,j]-=1
 dp=S.Poly(S.expand(bumped.det(method='berkowitz')-P),y)
 P6=dp.nth(6);Q5=dp.nth(5)-4*P6
 return S.Matrix([dp.nth(4)-4*Q5-(6+2*z)*P6,
  dp.nth(3)-(6+2*z)*Q5-(4+4*z)*P6,
  dp.nth(2)-(4+4*z)*Q5-(1+z)**2*P6,dp.nth(1)-(1+z)**2*Q5])

J01,J40,J56=Jedge(0,1),Jedge(4,0),Jedge(5,6)
T=S.Matrix.hstack(J01,J40,J56,Jz).T;den=S.expand(T.det(method='berkowitz'))
# adj(T)[:,3] solves the chosen active and z dual equations with det(T).
numvec=[S.expand(T.cofactor(3,i))for i in range(4)]
assert S.expand(sum(numvec[i]*Jz[i]for i in range(4))-den)==0
lo,hi=bound(den);assert lo>Fr(-30) and hi<Fr(-20)
active={(i,i+1)for i in range(6)}|{(4,0),(6,0)}
count=0;worst=None
for i in range(7):
 for j in range(7):
  if i==j:continue
  col=Jedge(i,j);numer=S.expand(sum(numvec[k]*col[k]for k in range(4)))
  if (i,j) in active:assert numer==0,(i,j)
  else:
   # den<0: numer/den>1/100 iff numer-den/100<0.
   ceiling=bound(numer-den/100)[1];assert ceiling<0,(i,j,ceiling)
   worst=ceiling if worst is None else max(worst,ceiling);count+=1
assert count==34
out=ROOT/'frontier-20261028-ph7-all-edge-first-order-certificate.json'
out.write_text(json.dumps({'root':'frontier-20261028-ph7-two-cycle-interval-certificate.json',
 'box_U_V_z_radius':'2/1000000000','branch_rate_center':'871488314/1000000000','branch_rate_radius':'1/1000000',
 'active_edges':sorted([list(x)for x in active]),'active_dual_slopes':'exactly zero',
 'z_dual_slope':'exactly one','dual_determinant_box':'(-30,-20)',
 'absent_edges_checked':count,'all_absent_edge_dual_slopes':'>1/100',
 'scope':'one-sided first derivative at isolated algebraic endpoint only; not local or global exclusion'},indent=2)+'\n')
print('SymPy',S.__version__,'exact all-42-edge tangent dual PASS: 8 zero, 34 >1/100, z-normalized 1')
