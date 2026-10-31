#!/usr/bin/env python3
"""Exact Q(zeta60) verification of coupled-gap phase and coefficient identities."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('field',P/'frontier-20261028-pair-triangle-cyclotomic-check-v1.py')
f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
x=f.xp;one=f.one;add=f.add;neg=f.neg;mul=f.mul;scale=f.scale;conj=f.conj;eq=f.eq
s3=f.s3;s5=f.s5;lam=x(55);ii=x(15);w=x(12)
# (1+lambda)/(1-lambda)=-i(2+sqrt3) and (1-i)/[(1-lambda)e^(i*pi/3)]=-(1+sqrt3).
left=add(one,lam);right=mul(neg(mul(ii,add(scale(one,2),s3))),add(one,neg(lam)))
assert eq(left,right)
assert eq(add(one,neg(ii)),mul(neg(add(one,s3)),mul(add(one,neg(lam)),x(10))))

def real(a):return scale(add(a,conj(a)),Q(1,2))
def y(t,u,v):return add(add(scale(x(24*t),u),scale(x(36*t),-u-v)),scale(x(48*t),v))
for u,v in ((1,0),(0,1),(1,1),(2,1)):
 yy1=y(1,u,v);yy2=y(2,u,v)
 assert eq(real(yy1),scale(s5,Q(v,2)))
 rhs=add(add(scale(s5,u*u),scale(s5,Q(u*v,2))),
         neg(scale(add(scale(one,5),s5),Q(v*v,4))))
 assert eq(real(mul(yy1,yy2)),rhs)
print('PASS exact lambda ratios in Q(zeta60)')
print('PASS Re(y1)=sqrt5*v/2 and Re(y1*y2)=sqrt5*u²+sqrt5*u*v/2-(5+sqrt5)*v²/4')
print('Integer field identities only; gamma and interval logic are in the written proof.')
