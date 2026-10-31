#!/usr/bin/env python3
"""Stdlib exact bivariate Bernstein replay for the unit hidden-gap strip.

Shows E(r,q)<0 on [3/2,37/20] x [0,1] by checking the four quadrants'
strictly negative degree-(6,3) Bernstein coefficients. E is the exact centered
trace polynomial shown in the accompanying manuscript; no generator sample.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm

# Sparse power coefficients in (r,q).
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items()if v}
def scale(a,c):return {k:v*F(c)for k,v in a.items()if v*c}
def mul(a,b):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+v*w
 return {k:v for k,v in out.items()if v}
def power(a,k):
 out={(0,0):F(1)}
 for _ in range(k):out=mul(out,a)
 return out
r={(1,0):F(1)};q={(0,1):F(1)};one={(0,0):F(1)}
Fpoly=add(add(add(add(add(scale(power(r,6),18225),scale(power(r,5),-87480)),scale(power(r,4),1701)),scale(power(r,3),410670)),scale(power(r,2),-471474)),add(scale(r,271080),scale(one,-360506)))
C=scale(add(add(add(scale(power(r,4),2025),scale(power(r,3),-6480)),scale(power(r,2),-40212)),add(scale(r,94860),scale(one,-20756))),27)
D=scale(add(add(scale(power(r,2),450),scale(r,-720)),scale(one,1373)),-486)
E=add(add(add(scale(Fpoly,2),mul(C,q)),mul(D,power(q,2))),scale(power(q,3),127575))
# Change r=3/2+(7/20)X; q=Y, negate E; recover exact power dictionary.
rp=add(scale(one,F(3,2)),scale(r,F(7,20)));trans={}
for (i,j),v in E.items():trans=add(trans,scale(mul(power(rp,i),power(q,j)),-v))
deg=(6,3);den=lcm(*(v.denominator for v in trans.values()));scale0=den*lcm(*(comb(6,k)for k in range(7)))*lcm(*(comb(3,k)for k in range(4)))
grid={key:0 for key in product(range(7),range(4))}
for (i,j),v in trans.items():
 div=comb(6,i)*comb(3,j);base=v*(scale0//div);assert scale0%div==0 and base.denominator==1
 for a in range(i,7):
  for b in range(j,4):grid[a,b]+=int(base)*comb(a,i)*comb(b,j)

def split(g,axis):
 L={};R={};d=deg[axis];other=1-axis
 for s in range(deg[other]+1):
  row=[]
  for k in range(d+1):key=[0,0];key[axis]=k;key[other]=s;row.append(g[tuple(key)])
  lev=[row]
  while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
  for k in range(d+1):
   key=[0,0];key[axis]=k;key[other]=s;L[tuple(key)]=lev[k][0]*(1<<(d-k));R[tuple(key)]=lev[d-k][-1]*(1<<k)
 return L,R
first=split(grid,0);quads=[child for half in first for child in split(half,1)]
mins=[min(g.values())for g in quads];assert all(v>0 for v in mins)
print('PASS: four exact degree-(6,3) Bernstein quadrant grids strictly positive for -E; scaled minima',mins)
