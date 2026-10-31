#!/usr/bin/env python3
"""Exact Bernstein proof E(r,h²)<0 for all positive real roots in low strip.

On r in [569/500,27/8], 0<=t<=1 put h²=r²*t. Reconstructs E with stdlib
Fraction polynomials and certifies -E>0 by a complete binary Bernstein cover.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm


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
rp=add(scale(one,F(569,500)),scale(r,F(27,8)-F(569,500)));qp=mul(power(rp,2),q);trans={}
for (i,j),v in E.items():trans=add(trans,scale(mul(power(rp,i),power(qp,j)),-v))
assert all(i<=6 and j<=3 for i,j in trans)
deg=(6,3);den=lcm(*(v.denominator for v in trans.values()));scale0=den*lcm(*(comb(6,k)for k in range(7)))*lcm(*(comb(3,k)for k in range(4)))
grid={key:0 for key in product(range(7),range(4))}
for (i,j),v in trans.items():
 div=comb(6,i)*comb(3,j);assert scale0%div==0;base=v*(scale0//div);assert base.denominator==1
 for a in range(i,7):
  for b in range(j,4):grid[a,b]+=int(base)*comb(a,i)*comb(b,j)

def split(g,axis):
 L={};R={};d=deg[axis];other=1-axis
 for s in range(deg[other]+1):
  row=[]
  for k in range(d+1):key=[0,0];key[axis]=k;key[other]=s;row.append(g[tuple(key)])
  levels=[row]
  while len(levels[-1])>1:levels.append([x+y for x,y in zip(levels[-1],levels[-1][1:])])
  for k in range(d+1):
   key=[0,0];key[axis]=k;key[other]=s;L[tuple(key)]=levels[k][0]*(1<<(d-k));R[tuple(key)]=levels[d-k][-1]*(1<<k)
 return L,R
stack=[('',grid)];leaves=[]
while stack:
 path,g=stack.pop()
 if min(g.values())>0:leaves.append(path);continue
 assert len(path)<32,('depth limit',path)
 a,b=split(g,len(path)%2);stack.extend([(path+'1',b),(path+'0',a)])
assert len(leaves)==47
print('PASS: full binary cover of [569/500,27/8] x [0,1]; 47 strict exact Bernstein leaves')
