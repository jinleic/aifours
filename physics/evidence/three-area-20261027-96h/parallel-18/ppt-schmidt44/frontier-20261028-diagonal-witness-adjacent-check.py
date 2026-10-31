#!/usr/bin/env python3
"""Exact determinant identities for the actual two-adjacent-edge corner."""
from fractions import Fraction as F
import json

def add(*args):
 n=max(len(x) for x in args)
 return tuple(sum(a[i] if i<len(a) else 0 for a in args) for i in range(n))
def scale(a,c):return tuple(c*x for x in a)
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return tuple(out)
def norm(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return tuple(a)
def sub(a,b):return norm(add(a,scale(b,-1)))
def eq(a,b):assert norm(a)==norm(b),(norm(a),norm(b))
X=(0,1);one=(1,);two=(2,);three=(3,);four=(4,)
X2=mul(X,X);X3=mul(X2,X);xm1=sub(X,one);twomx=sub(two,X);threemx=sub(three,X)
def det(d,r,s):return add(mul(mul(d,d),add(d,r)),scale(mul(d,mul(s,s)),-2),mul(add(scale(s,4),scale(d,-3),scale(r,-1)),mul(r,r)))
def firstminor(d,r,s):return sub(mul(d,add(d,r)),scale(mul(s,s),2))
# Scale low-interval matrices by D to clear denominators.
d=X2;r=mul(X,twomx);s=sub(two,X2)
eq(det(d,r,s),scale(mul(mul(X2,mul(xm1,xm1)),add(scale(X2,-1),X,three)),8))
eq(firstminor(d,r,s),scale(mul(xm1,add(scale(X3,-1),scale(X,4),four)),2))
eq(sub(mul(d,add(d,r)),scale(mul(r,r),2)),mul(sub(d,r),add(d,scale(r,2))))
# High interval has polynomial entries directly.
d=X;r=twomx;s=(-1,)
eq(det(d,r,s),scale(mul(threemx,add(X2,X,(-4,))),2))
eq(firstminor(d,r,s),scale(xm1,2))
eq(sub(mul(d,add(d,r)),scale(mul(r,r),2)),mul(sub(d,r),add(d,scale(r,2))))
# The unmarked pair is (1,2), so its anti-symmetric eigenvalue is D-r.
for D in (F(1),F(6,5),F(3,2),F(7,4),F(2),F(9,4),F(5,2),F(11,4),F(3)):
 g=max(F(0),1-D+2/D);r=2-D;s=g-1
 assert D-r>=0 and D*(D+r)-2*s*s>=0 and D*D-r*r>=0 and (D-r)*(D+2*r)>=0
 actual=D*D*(D+r)-2*D*s*s+(4*s-3*D-r)*r*r
 target=(8*(D-1)**2*(-D*D+D+3)/D) if D<=2 else 2*(3-D)*(D*D+D-4)
 assert actual==target and actual>=0
print(json.dumps({'correct_two_edge_determinant_identities':2,'correct_top_center_minor_identities':2,
 'correct_other_minor_identities':2,'exact_rational_D_checks':9,
 'scope':'Correct corner has unmarked 1-2 edge r; these exact identities supersede the predecessor checker\'s mislabeled two-edge block.'},indent=2))
