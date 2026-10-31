#!/usr/bin/env python3
"""Literal locally-regular countermodel to the global four-term lemma."""
from itertools import product
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
a=(0,3,4,1,2)
def m(x,y):return B[x][y]
assert all(m(x,x)==x for x in range(5))
assert all(m(m(x,y),z)==m(x,m(y,z)) for x,y,z in product(range(5),repeat=3))
corners=[]
for e in range(5):
 local={m(m(e,x),e) for x in range(5)}
 corners.append(tuple(sorted(local)))
 assert all(m(x,y) in local for x,y in product(local,repeat=2))
 assert all(m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x) for x,y,z in product(local,repeat=3))
assert corners==[(0,),(1,2,4),(2,),(2,3,4),(4,)]
assert all(a[a[x]]==x for x in range(5))
assert all(a[m(x,y)]==m(a[x],a[y]) for x,y in product(range(5),repeat=2))
assert m(m(m(m(1,0),1),3),1)!=m(m(m(1,0),3),1)
x,u,v,y=0,1,3,1
E=m(m(x,u),y);F=m(m(x,v),y)
assert m(u,v)==u and m(v,u)==v and (E,F)==(2,4)
assert m(E,F)==F and m(F,E)==E and E!=F
common=[h for h in range(5) if all(m(h,w)==w==m(w,h) for w in (x,u,v,y))]
commonEF=[h for h in range(5) if all(m(h,w)==w==m(w,h) for w in (E,F))]
assert common==[] and commonEF==[1,3]
print('PASS B order5, 125 associativity cases, all local corners regular')
print('corners=',corners,'; global regular identity failure x,y,z=(1,0,3)',sep='')
print('u,v=',u,v,' E,F=',E,F,' uv,vu,EF,FE=',m(u,v),m(v,u),m(E,F),m(F,E),sep='')
print('C2 involutory automorphism=',a,'; common-upper all inputs=',common,' E/F=',commonEF,sep='')
print('LIMIT not a faithful host for any source; only the four-term lemma fails locally')
