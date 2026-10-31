#!/usr/bin/env python3
"""Literal 45-element source for a universal regular-band-host obstruction."""
from itertools import product
A=range(5)
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
S=tuple(product(range(3),A,range(3)))
def m(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def q(s):return (s[0],th[s[1]],s[2])
def qm(a,b):return (a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
def idem(s):return m(s,s)==s
assert all(m(m(a,b),c)==m(a,m(b,c)) for a,b,c in product(S,repeat=3))
assert all(any(m(m(a,b),a)==a and m(m(b,a),b)==b for b in S) for a in S)
E=tuple(a for a in S if idem(a));Es=set(E)
for a in S:
    assert not ({m(e,a) for e in E}&{m(a,e) for e in E}&Es) or idem(a)
for e in E:
    local={m(m(e,a),e) for a in S}
    le=tuple(a for a in local if idem(a))
    assert all(idem(m(a,b)) for a,b in product(le,repeat=2))
    assert all(m(m(m(m(a,b),a),c),a)==m(m(m(a,b),c),a) for a,b,c in product(le,repeat=3))
assert any(not idem(m(a,b)) for a,b in product(E,repeat=2))
e0=(0,4,0);local={m(m(e0,a),e0) for a in S};le=tuple(a for a in local if idem(a))
assert any(m(a,b)!=m(b,a) for a,b in product(le,repeat=2))
assert all(q(m(a,b))==qm(q(a),q(b)) for a,b in product(S,repeat=2))
assert all(idem(a)==(qm(q(a),q(a))==q(a)) for a in S)
contexts=(None,)+S
def ctx(a,s,b):
    x=s if a is None else m(a,s)
    return x if b is None else m(x,b)
sig={s:bytes(ctx(a,s,b) in Es for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[a]==sig[b])==(q(a)==q(b)) for a,b in product(S,repeat=2))
e=(1,1,1);f=(1,3,1);a=(1,4,0);b=(2,4,0);z=(0,4,1);s=(1,4,1)
t1=m(a,z);t2=m(b,z)
assert e!=f and idem(e) and idem(f) and q(e)==q(f)
assert m(e,f)==f and m(f,e)==e
assert m(a,b)==a and m(b,a)==b
assert m(s,t1)==e and m(s,t2)==f
assert (th[s[1]]+th[P[s[2]][t1[0]]])%2==1
assert (th[s[1]]+th[P[s[2]][t2[0]]])%2==1
print('source=',len(S),' idempotents=',len(E),' actual_actor=',len(set(map(q,S))),sep='')
print('PASS associativity, regularity, weak-E, local r-orthodox, nonorthodox, non-locally-inverse')
print('PASS purity and actual tau via 46^2 contexts/source')
print('same-q R-idempotents e,f=',e,f,'; ef,fe=',m(e,f),m(f,e))
print('left-zero source a,b=',a,b,'; e=s(az), f=s(bz), equal action weight=1')
print('LIMIT finite source identities only; universal regular-band obstruction is written proof')
