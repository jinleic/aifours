#!/usr/bin/env python3
"""Check seminormality for every 2x2 binary evaluation-selector band."""
from itertools import product
U=tuple(('u',i) for i in range(2));V=tuple(('v',i) for i in range(2));W=tuple(('w',i) for i in range(2));T=U+V+W
count=0
for bits in product(range(2),repeat=4):
 f=(bits[:2],bits[2:])
 def m(a,b):
  if b[0]!='u':return b
  if a[0] in ('u','w'):return a
  return W[f[a[1]][b[1]]]
 assert all(m(a,a)==a for a in T)
 assert all(m(m(a,b),c)==m(a,m(b,c)) for a,b,c in product(T,repeat=3))
 for x,y,z,w in product(T,repeat=4):
  def wd(*a):
   t=a[0]
   for k in a[1:]:t=m(t,k)
   return t
  assert wd(x,y,z,w,x)==wd(x,y,z,x,z,w,x)
  count+=1
 assert all(m(m(z,x),z)==z for x in U for z in T)
assert count==20736
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
def bd(*a):
 t=a[0]
 for x in a[1:]:t=B[t][x]
 return t
assert all(bd(x,y,z,w,x)==bd(x,y,z,x,z,w,x) for x,y,z,w in product(range(5),repeat=4))
N=((0,2,2,0,4,5),(1,1,1,1,1,1),(2,2,2,2,2,2),(0,1,2,3,4,5),(0,5,2,4,4,5),(5,5,5,5,5,5))
def nd(*a):
 t=a[0]
 for x in a[1:]:t=N[t][x]
 return t
assert nd(0,4,3,1,0)!=nd(0,4,3,0,3,1,0)
print('PASS all16 selector tables, 20736 seminormal identities and associativity')
print('PASS explicit B5 seminormal all625 identities; nonseminormal six-band negative control')
print('LIMIT finite same-author check; universal evaluation-band proof is symbolic')
