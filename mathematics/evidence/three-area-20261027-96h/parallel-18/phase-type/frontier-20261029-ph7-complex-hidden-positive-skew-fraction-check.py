#!/usr/bin/env python3
"""Exact positive-skewness exclusion cover for r in [43/20,5/2].

On h²=t*(45r²-72r-58)/63, certifies either -tau3>=0 or both
-(tau4+10tau2²)>0 and (tau4+10tau2²)^2-9tau2*tau3²>0.
All polynomial arithmetic and Bernstein splitting use stdlib Fraction/integers.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm

def clean(a):return {k:v for k,v in a.items()if v}
def add(a,b):
 o=a.copy()
 for k,v in b.items():o[k]=o.get(k,F(0))+v
 return clean(o)
def scale(a,c):return clean({k:v*F(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 o={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():o[i+k,j+l]=o.get((i+k,j+l),F(0))+v*w
 return clean(o)
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
tau4=add(add(powp(shift,4),scale(add(add(powp(a,4),scale(powp(a,2),-6*z)),scale(one,z*z)),4)),scale(add(add(powp(b,4),scale(mul(powp(b,2),v),-6)),powp(v,2)),2))
J=add(tau4,scale(powp(tau2,2),10));polys=[scale(tau3,-1),scale(J,-1),sub(powp(J,2),scale(mul(tau2,powp(tau3,2)),9))];degs=[(3,1),(4,2),(8,4)]

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

for p,deg in zip(polys,degs):assert all(i<=deg[0] and j<=deg[1]for i,j in p)
stack=[('',[grid(p,d)for p,d in zip(polys,degs)])];counts=[0,0]
while stack:
 path,arr=stack.pop()
 if min(arr[0].values())>=0:counts[0]+=1;continue
 if min(arr[1].values())>0 and min(arr[2].values())>0:counts[1]+=1;continue
 assert len(path)<20,('depth limit',path)
 axis=len(path)%2;parts=[split(g,d,axis)for g,d in zip(arr,degs)]
 stack.extend([(path+'1',[q[1]for q in parts]),(path+'0',[q[0]for q in parts])])
assert counts==[12,4]
print('PASS: complete dual selector tree; 12 nonpositive-tau3 leaves and 4 strict positive-tau3 contradiction leaves')
