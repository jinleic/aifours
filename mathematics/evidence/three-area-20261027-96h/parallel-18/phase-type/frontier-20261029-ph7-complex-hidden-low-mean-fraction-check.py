#!/usr/bin/env python3
"""Exact 6x3 Bernstein proof for the complex-hidden low-mean rectangle.

On r in [43/20,49/20], put h²=t*(45r²-72r-58)/63 with t in [0,1].
The polynomial -E has 28 strictly positive Bernstein coefficients.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm

def add(a,b):
 o=a.copy()
 for k,v in b.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items()if v}
def scale(a,c):return {k:v*F(c)for k,v in a.items()if v*c}
def mul(a,b):
 o={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():o[i+k,j+l]=o.get((i+k,j+l),F(0))+v*w
 return {k:v for k,v in o.items()if v}
def powp(a,k):
 out={(0,0):F(1)}
 for _ in range(k):out=mul(out,a)
 return out
r={(1,0):F(1)};t={(0,1):F(1)};one={(0,0):F(1)}
Fpoly=add(add(add(add(add(scale(powp(r,6),18225),scale(powp(r,5),-87480)),scale(powp(r,4),1701)),scale(powp(r,3),410670)),scale(powp(r,2),-471474)),add(scale(r,271080),scale(one,-360506)))
C=scale(add(add(add(scale(powp(r,4),2025),scale(powp(r,3),-6480)),scale(powp(r,2),-40212)),add(scale(r,94860),scale(one,-20756))),27)
D=scale(add(add(scale(powp(r,2),450),scale(r,-720)),scale(one,1373)),-486)
vmax=scale(add(add(scale(powp(r,2),45),scale(r,-72)),scale(one,-58)),F(1,63))
# Ecomplex = 2F - C v + D v² -127575v³
v=mul(vmax,t);E=add(add(add(scale(Fpoly,2),scale(mul(C,v),-1)),mul(D,powp(v,2))),scale(powp(v,3),-127575))
rp=add(scale(one,F(43,20)),scale(r,F(3,10)));trans={}
for (i,j),val in E.items():trans=add(trans,scale(mul(powp(rp,i),powp(t,j)),-val))
assert all(i<=6 and j<=3 for i,j in trans)
sc=lcm(*(v.denominator for v in trans.values()))*lcm(*(comb(6,k)for k in range(7)))*lcm(*(comb(3,k)for k in range(4)))
grid={key:0 for key in product(range(7),range(4))}
for (i,j),val in trans.items():
 div=comb(6,i)*comb(3,j);assert sc%div==0;base=val*(sc//div);assert base.denominator==1
 for a in range(i,7):
  for b in range(j,4):grid[a,b]+=int(base)*comb(a,i)*comb(b,j)
assert all(v>0 for v in grid.values())
print('PASS: all 28 exact Bernstein coefficients of -E on the complex-hidden low-mean rectangle are positive; scaled minimum',min(grid.values()))
