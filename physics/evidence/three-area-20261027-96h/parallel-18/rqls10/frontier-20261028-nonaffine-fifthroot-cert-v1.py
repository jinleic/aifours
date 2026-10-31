#!/usr/bin/env python3
"""Exact Q(zeta5) identities and finite affine-orbit coverage."""
from fractions import Fraction as Q
from itertools import permutations,product
p=5
zero=[Q(0)]*5
one=[Q(1),Q(0),Q(0),Q(0),Q(0)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def neg(a):return [-x for x in a]
def scale(a,c):return [Q(c)*x for x in a]
def mul(a,b):return [sum((a[i]*b[(k-i)%5] for i in range(5)),Q(0)) for k in range(5)]
def powr(k):
 v=zero[:];v[k%5]=Q(1);return v
def conj(a):return [a[-i%5] for i in range(5)]
def eq(a,b):return all((a[i]-b[i])==(a[4]-b[4]) for i in range(4))
sigma=(0,1,2,4,3)
delta=[(sigma[(t+1)%5]-sigma[t])%5 for t in range(5)]
assert delta==[1,1,2,4,2]
r2=[]
for v in delta:
 w=add(one,powr(v));r2.append(mul(w,conj(w)))
def dc(k):
 v=zero[:]
 for t in range(5):v=add(v,mul(r2[t],powr(-k*t)))
 return scale(v,Q(1,5))
d0,d1,d2=dc(0),dc(1),dc(2)
g=add(one,scale(add(powr(1),powr(4)),2)) # positive sqrt(5)
assert eq(mul(g,g),scale(one,5))
assert eq(d0,scale(add(scale(one,15),g),Q(1,10)))
assert eq(mul(d1,conj(d1)),scale(add(scale(one,3),neg(g)),Q(1,10)))
assert eq(mul(d2,conj(d2)),scale(add(scale(one,3),g),Q(1,10)))
assert eq(mul(d1,mul(d2,d2)),scale(add(scale(one,5),g),Q(-1,50)))
# Positive roots: |d1|=(5-sqrt5)/10, |d2|=(5+sqrt5)/10.
u=scale(add(scale(one,5),neg(g)),Q(1,10));v=scale(add(scale(one,5),g),Q(1,10))
assert eq(mul(u,u),mul(d1,conj(d1))) and eq(mul(v,v),mul(d2,conj(d2)))
assert eq(add(u,v),one)
# Nonaffine sigma transformations: affine domain, sign/translation output.
orbit={tuple((eps*sigma[(c*t+d)%5]+b)%5 for t in range(5))
       for eps,c,d,b in product((1,4),range(1,5),range(5),range(5))}
nonaffine={s for s in permutations(range(5))
           if not all((s[t]-s[0])%5==((s[1]-s[0])*t)%5 for t in range(5))}
stab=[(eps,c,d,b) for eps,c,d,b in product((1,4),range(1,5),range(5),range(5))
      if all((eps*sigma[(c*t+d)%5]+b)%5==sigma[t] for t in range(5))]
assert len(orbit)==100 and orbit==nonaffine and len(stab)==2
print('PASS exact Phi5 identities d0=(15+sqrt5)/10, |d1|+|d2|=1')
print('PASS d1*d2^2=-(5+sqrt5)/50 < 0; required d0>=2 is impossible')
print('PASS all100 nonaffine permutations form one orbit; stabilizer',stab)
print('Integer/cyclotomic checks; complete spectral and symmetry proof remains written.')
