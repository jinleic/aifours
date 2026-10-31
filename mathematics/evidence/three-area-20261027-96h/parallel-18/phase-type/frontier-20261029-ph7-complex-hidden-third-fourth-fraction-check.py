#!/usr/bin/env python3
"""Exact dual Bernstein cover for complex hidden mean r in [43/20,5/2].

Certifies either -(25/42*tau2^3-tau3^2)>0 or -(tau4+10*tau2^2)>0
on r=43/20+(7/20)x, v=t*(45r²-72r-58)/63, (x,t) in [0,1]^2.
All polynomial arithmetic and subdivision use Python stdlib Fraction/integer.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm

def clean(a):return {k:v for k,v in a.items()if v}
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))+v
 return clean(out)
def scale(a,c):return clean({k:v*F(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+v*w
 return clean(out)
def powp(a,k):
 out={(0,0):F(1)}
 for _ in range(k):out=mul(out,a)
 return out
R={(1,0):F(1)};V={(0,1):F(1)};one={(0,0):F(1)}
r=add(scale(one,F(43,20)),scale(R,F(7,20)))
vmax=scale(add(add(scale(powp(r,2),45),scale(r,-72)),scale(one,-58)),F(1,63));v=mul(vmax,V)
shift=scale(add(scale(one,4),scale(r,2)),F(1,7));a=sub(shift,one);b=sub(shift,r);z=F(8,9)
tau2=scale(add(add(add(scale(powp(r,2),45),scale(r,-72)),scale(v,-63)),scale(one,-58)),F(2,63))
k=add(add(add(add(scale(powp(r,3),45),scale(powp(r,2),-108)),scale(r,260)),scale(one,-354)),scale(mul(sub(scale(r,315),scale(one,252)),v),-1))
tau3=scale(k,F(-2,147))
tau4=add(add(powp(shift,4),scale(add(add(powp(a,4),scale(mul(powp(a,2),one),-6*z)),scale(one,z*z)),4)),scale(add(add(powp(b,4),scale(mul(powp(b,2),v),-6)),powp(v,2)),2))
E=scale(sub(scale(powp(tau2,3),F(25,42)),powp(tau3,2)),-1)
J=scale(add(tau4,scale(powp(tau2,2),10)),-1)

def grid(poly,deg):
 den=lcm(*(v.denominator for v in poly.values()));sc=den
 for d in deg:sc*=lcm(*(comb(d,k)for k in range(d+1)))
 arr={key:0 for key in product(*(range(d+1)for d in deg))}
 for ex,c in poly.items():
  div=1
  for d,i in zip(deg,ex):div*=comb(d,i)
  assert sc%div==0;base=c*(sc//div);assert base.denominator==1
  for key in product(*(range(i,d+1)for i,d in zip(ex,deg))):
   val=int(base)
   for x,i in zip(key,ex):val*=comb(x,i)
   arr[key]+=val
 return arr

def split(g,deg,axis):
 L={};R={};d=deg[axis];other=1-axis
 for s in range(deg[other]+1):
  row=[]
  for k in range(d+1):key=[0,0];key[axis]=k;key[other]=s;row.append(g[tuple(key)])
  lev=[row]
  while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
  for k in range(d+1):
   key=[0,0];key[axis]=k;key[other]=s;L[tuple(key)]=lev[k][0]*(1<<(d-k));R[tuple(key)]=lev[d-k][-1]*(1<<k)
 return L,R

assert all(i<=6 and j<=3 for i,j in E) and all(i<=4 and j<=2 for i,j in J)
stack=[('',grid(E,(6,3)),grid(J,(4,2)))];leaves=[[],[]]
while stack:
 path,A,B=stack.pop()
 if min(A.values())>0:leaves[0].append(path);continue
 if min(B.values())>0:leaves[1].append(path);continue
 assert len(path)<20,('depth limit',path)
 axis=len(path)%2;AL,AR=split(A,(6,3),axis);BL,BR=split(B,(4,2),axis)
 stack.extend([(path+'1',AR,BR),(path+'0',AL,BL)])
assert [len(x)for x in leaves]==[13,5]
print('PASS: complete dual Bernstein tree, strict tau3/tau4 contradiction leaves 13/5')
