#!/usr/bin/env python3
"""Exclude z=8/9 for common rates 3U+2W and arbitrary real outer rates."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,w,t,r,y=S.symbols('u w t r y',real=True);z=S.Rational(8,9)
base=(y+u)**3*(y+w)**2*(y*y+t*y+r);B=S.Poly(base,y)
p=B.nth(6)-4;q=B.nth(5)-4*p-(6+2*z)
R=S.Poly(S.expand(base-y*((y+1)**2+z)**2*(y*y+p*y+q)),y)
e4,e3=R.nth(4),R.nth(3)
assert all(S.degree(e,t)<=1 and S.degree(e,r)<=1 and S.diff(e,t,r)==0 for e in (e4,e3))
a00,a01=S.diff(e4,t),S.diff(e4,r);a10,a11=S.diff(e3,t),S.diff(e3,r)
b0,b1=e4.subs({t:0,r:0}),e3.subs({t:0,r:0})
den=S.factor(a00*a11-a01*a10);tn=S.factor(-b0*a11+a01*b1);rn=S.factor(-a00*b1+b0*a10)
D=S.expand(den*S.Rational(81,2));N=S.expand(-(tn*tn-4*rn*den)*6561)
assert (S.degree(D,u),S.degree(D,w),S.degree(N,u),S.degree(N,w))==(4,4,10,8)

def coeff2(poly):
 P=S.Poly(poly,u,w);m=P.degree(u);n=P.degree(w)
 def frac(c):return F(int(S.numer(c)),int(S.denom(c)))
 return [[frac(P.coeff_monomial(u**i*w**j))/comb(m,i)/comb(n,j)for j in range(n+1)]for i in range(m+1)]
def split1(row):
 a=[row]
 while len(a[-1])>1:a.append([(x+y)/2 for x,y in zip(a[-1],a[-1][1:])])
 return [x[0]for x in a],[x[-1]for x in a][::-1]
def split2(A):
 m=len(A);n=len(A[0]);L=[[F(0)]*n for _ in range(m)];R=[[F(0)]*n for _ in range(m)]
 for j in range(n):
  ll,rr=split1([A[i][j]for i in range(m)])
  for i in range(m):L[i][j]=ll[i];R[i][j]=rr[i]
 LL=[];LH=[];RL=[];RH=[]
 for i in range(m):
  ll,lh=split1(L[i]);rl,rh=split1(R[i]);LL.append(ll);LH.append(lh);RL.append(rl);RH.append(rh)
 return [LL,LH,RL,RH]
def cover(poly):
 stack=[('',coeff2(poly),F(0),F(1),F(0),F(1))];leaves=[]
 while stack:
  path,A,x0,x1,y0,y1=stack.pop();corners=[(x0,y0,A[0][0]),(x0,y1,A[0][-1]),(x1,y0,A[-1][0]),(x1,y1,A[-1][-1])]
  if min(min(row)for row in A)>=0 and all(val>0 for x,y,val in corners if x<1 and y<1):leaves.append(path);continue
  assert len(path)<10,path
  xm=(x0+x1)/2;ym=(y0+y1)/2;coords=[(x0,xm,y0,ym),(x0,xm,ym,y1),(xm,x1,y0,ym),(xm,x1,ym,y1)]
  for j,block in enumerate(split2(A)):stack.append((path+str(j),block,*coords[j]))
 return sorted(leaves)
Dcover,Ncover=cover(D),cover(N);assert (len(Dcover),len(Ncover))==(10,16)
out=ROOT/'frontier-20261028-ph7-three-two-unequal-outer-critical-certificate.json'
out.write_text(json.dumps({'z':'8/9','D_polynomial':str(D),'N_polynomial':str(N),
 'D_degrees_U_W':[4,4],'N_degrees_U_W':[10,8],
 'D_positive_compactified_bernstein_leaf_paths':Dcover,'N_positive_compactified_bernstein_leaf_paths':Ncover,
 'compactification':'U=x/(1-x), W=y/(1-y); multiply by (1-x)^degU(1-y)^degW',
 'identity':'det linear coefficient system=2D/81; t^2-4r=-N/(6561*det^2)',
 'scope':'3U+2W common rates positive, arbitrary outer real rates; one 5/7-theta graph only'},indent=2)+'\n')
print('SymPy',S.__version__,'Fraction bivariate Bernstein PASS: 3U+2W common rates exclude ALL real outer rates at 8/9')
print('compactified cover leaves D,N:',len(Dcover),len(Ncover));print('saved:',out)
