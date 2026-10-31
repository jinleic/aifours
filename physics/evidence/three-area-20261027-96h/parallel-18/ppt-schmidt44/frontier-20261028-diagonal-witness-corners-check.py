#!/usr/bin/env python3
"""Exact polynomial and rational checks for all nonsymmetric diagonal coefficients."""
from fractions import Fraction as F
import json

def add(*a):
 n=max(map(len,a));return tuple(sum(v[i] if i<len(v) else 0 for v in a) for i in range(n))
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return tuple(out)
def scale(a,c):return tuple(c*x for x in a)
def norm(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return tuple(a)
def sub(a,b):return norm(add(a,scale(b,-1)))
def eq(a,b):assert norm(a)==norm(b),(norm(a),norm(b))
X=(0,1);one=(1,);two=(2,);three=(3,)
Xm1=sub(X,one);twomX=sub(two,X);threemX=sub(three,X);X2=mul(X,X);X3=mul(X2,X)
# Low interval 1<=D<=2: multiply all matrix entries by D to clear s denominator.
d=X2;r=mul(X,twomX);s=sub(two,X2)
one_edge=sub(mul(add(d,s),add(d,r)),scale(mul(r,r),4))
tri=sub(mul(d,add(d,scale(s,2))),scale(mul(r,r),3))
star=sub(mul(d,add(d,scale(r,2))),scale(mul(s,s),3))
eq(one_edge,scale(mul(mul(X,Xm1),add(scale(X2,-1),scale(X,3),(-1,))),4))
eq(tri,scale(mul(mul(X2,Xm1),twomX),4))
eq(star,scale(mul(Xm1,add(scale(X3,-1),scale(X,3),three)),4))
# High interval 2<=D<=3: no denominator.
d=X;r=twomX;s=(-1,)
one_edge=sub(mul(add(d,s),add(d,r)),scale(mul(r,r),4))
tri=sub(mul(d,add(d,scale(s,2))),scale(mul(r,r),3))
star=sub(mul(d,add(d,scale(r,2))),scale(mul(s,s),3))
eq(one_edge,scale(mul(threemX,sub(scale(X,2),three)),2))
eq(tri,scale(mul(sub(X,two),threemX),2))
eq(star,mul(Xm1,threemX))
# Two-adjacent-edge 3x3 determinant and two needed principal-minor identities.
for d,r,s in ((X2,mul(X,twomX),sub(two,X2)),(X,twomX,(-1,))):
 tri=sub(mul(d,add(d,scale(s,2))),scale(mul(r,r),3))
 det=add(mul(mul(d,d),add(d,s)),scale(mul(mul(d,mul(s,s)),(-2,)),1),scale(mul(sub(d,s),mul(r,r)),-3))
 eq(det,mul(sub(d,s),tri))
 eq(sub(mul(d,add(d,s)),scale(mul(s,s),2)),mul(sub(d,s),add(d,scale(s,2))))
 eq(scale(sub(mul(d,add(d,s)),scale(mul(r,r),2)),3),add(scale(tri,2),mul(d,sub(d,s))))
def psd(M):
 x=[r[:] for r in M];rank=0
 while x:
  if any(x[i][i]<0 for i in range(len(x))):return None
  j=next((i for i in range(len(x)) if x[i][i]>0),None)
  if j is None:return rank if all(z==0 for row in x for z in row) else None
  p=x[j][j];R=[i for i in range(len(x)) if i!=j]
  x=[[x[i][k]-x[i][j]*x[j][k]/p for k in R] for i in R];rank+=1
 return rank
patterns=((),((0,1),),((0,1),(0,2)),((0,1),(0,2),(0,3)),((0,1),(0,2),(1,2)))
points=(F(1),F(6,5),F(3,2),F(5,3),F(7,4),F(9,5),F(19,10),F(2),F(21,10),F(5,2),F(11,4),F(29,10),F(3))
count=0
for D in points:
 g=max(F(0),1-D+2/D);delta=3-D;r=delta-1;s=g-1
 for edges in patterns:
  E={tuple(sorted(e)) for e in edges}
  M=[[D if i==j else (s if tuple(sorted((i,j))) in E else r) for j in range(4)] for i in range(4)]
  assert psd(M) is not None,(D,edges);count+=1
print(json.dumps({'piecewise_polynomial_determinant_identities':6,
 'two_edge_polynomial_identities_per_branch':3,'rational_corner_PSD_checks':count,
 'covered_graph_types':['empty','one edge','two adjacent edges','three-edge star','triangle'],
 'scope':'Exact algebra and finite checks; the all-parameter signs and rank-two forcing are written proofs.'},indent=2))
