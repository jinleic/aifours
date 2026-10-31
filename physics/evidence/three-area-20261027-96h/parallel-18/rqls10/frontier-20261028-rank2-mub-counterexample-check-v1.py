#!/usr/bin/env python3
"""Exact F5 Gauss-sum and rank-two-projector counterexample checks."""
p=5
def red(v):return tuple(v[i]-v[4] for i in range(4))
def mul(a,b):return [sum(a[i]*b[(k-i)%5] for i in range(5)) for k in range(5)]
def conj(a):return [a[(-i)%5] for i in range(5)]
def inner(q,j,c):
    # U† diag(omega^(q t²)) U ; U_t,c=omega^(3tc)/sqrt5.
    v=[0]*5
    for t in range(5):v[(q*t*t+3*(c-j)*t)%5]+=1
    return v
orth=[0]*5
for t in range(5):orth[(3*t)%5]+=1
assert red(orth)==(0,0,0,0)
for q in (3,4):
 for j in range(5):
  for c in (0,1):
   v=inner(q,j,c);sq=mul(v,conj(v));sq[0]-=5
   assert red(sq)==(0,0,0,0)
# In the U basis the ratio of the two W columns is a fifth root.
ratios=[]
for j in range(5):
    a=inner(3,j,0);b=inner(3,j,1)
    shifts=[k for k in range(5) if red([b[i]-a[(i-k)%5] for i in range(5)])==(0,0,0,0)]
    assert len(shifts)==1;ratios.append(shifts[0])
assert len(set(ratios))==5
print('PASS rank2 projector W[:,0:2] has diagonal 2/5 in I,U,D5U')
print('PASS both W columns are orthogonal and unbiased to all three five-dimensional bases')
print('U-basis ratios are fifth roots with exponents',ratios,'so Re(conj(u_j)*v_j) is never zero')
print('Thus flat rank2 projectors exist; the additional cross-phase gate is essential')
