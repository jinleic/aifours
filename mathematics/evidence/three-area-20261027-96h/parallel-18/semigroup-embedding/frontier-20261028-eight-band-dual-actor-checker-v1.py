#!/usr/bin/env python3
"""Direct exact dual-host check, separate literal table and opposite formula."""
from itertools import product
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,4),(4,4,3));th=(0,1,0,1,0)
B=((0,1,7,0,6,0,6,7),(0,1,1,7,1,6,6,7),
   (0,1,2,7,1,5,6,7),(0,1,7,3,4,0,6,7),
   (0,1,1,3,4,6,6,7),(0,1,2,0,6,5,6,7),
   (0,1,1,0,6,6,6,7),(0,1,7,7,1,0,6,7))
act=(1,0,3,2,5,4,6,7)
beta=((0,0,7),(6,6,0),(6,6,1),(1,1,7),(5,5,2))
S=tuple(product(range(3),range(5),range(3)))
def m(s,t):return (s[0],T[T[s[1]][P[s[2]][t[0]]]][t[1]],t[2])
def op(s,t):return m(t,s)
def q(s):return (s[2],th[s[1]],s[0])
def qop(s,t):return (s[0],(s[1]+th[P[t[0]][s[2]]]+t[1])%2,t[2])
def b(s):
    x=beta[s[1]][s[2]]
    return act[x] if th[s[1]] else x

def bandop(x,y):return B[y][x]
def hostband(s,t):
    w=(th[s[1]]+th[P[t[2]][s[0]]])%2
    y=b(t)
    return bandop(b(s),act[y] if w else y)
assert all(bandop(x,x)==x for x in range(8))
assert all(bandop(bandop(x,y),z)==bandop(x,bandop(y,z)) for x,y,z in product(range(8),repeat=3))
assert all(bandop(bandop(bandop(bandop(x,y),x),z),x)==bandop(bandop(bandop(x,y),z),x)
           for x,y,z in product(range(8),repeat=3))
for s,t in product(S,repeat=2):
    assert q(op(s,t))==qop(q(s),q(t))
    assert b(op(s,t))==hostband(s,t)
    assert s==t or q(s)!=q(t) or b(s)!=b(t)
e=(0,0,0);f=(0,2,0)
assert op(e,f)==e and op(f,e)==f and q(e)==q(f) and b(e)!=b(f)
print('PASS B^op regular band, all2025 opposite-source actor and physical-host products, injectivity')
print('same-actor L-idempotent pair:',e,f,' dual band values=',b(e),b(f))
print('LIMIT source-specific C2 dual; no general original-class conclusion')
