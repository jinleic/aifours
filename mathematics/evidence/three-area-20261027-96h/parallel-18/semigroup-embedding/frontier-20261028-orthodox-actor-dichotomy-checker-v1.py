#!/usr/bin/env python3
"""Exact orthodox/nonorthodox and unseparated-actor sanity checks."""
from itertools import product
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sig=(0,3,4,1,2)
def signatures(S,m):
 E={s for s in S if m(s,s)==s};contexts=(None,)+S
 def ctx(a,s,b):
  x=s if a is None else m(a,s)
  return x if b is None else m(x,b)
 return E,{s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
# Orthodox B0⋊C2, E locally regular but globally nonregular.
S=tuple(product(range(5),range(2)))
def m(a,b):return(B[a[0]][sig[b[0]] if a[1] else b[0]],a[1]^b[1])
E,ss=signatures(S,m)
assert all(m(a,b) in E for a,b in product(E,repeat=2))
assert all((ss[a]==ss[b])==(a[1]==b[1]) for a,b in product(S,repeat=2))
assert B[B[B[B[1][0]][1]][3]][1]!=B[B[B[1][0]][3]][1]
print('orthodox source=',len(S),' E=',len(E),' actual_actor=',len(set(ss.values())),' globally_nonregular_E=true',sep='')
# A pure auxiliary CS actor with extra rows/columns need not itself be a group.
D=tuple(product(range(2),range(2),range(2)))
def d(a,b):return(a[0],a[1]^b[1],b[2])
Ed,ds=signatures(D,d)
assert all(d(a,b) in Ed for a,b in product(Ed,repeat=2))
assert all((ds[a]==ds[b])==(a[1]==b[1]) for a,b in product(D,repeat=2))
print('orthodox rectangular-group source=',len(D),' pure auxiliary actor=',len(D),' actual_tau_group=',len(set(ds.values())),sep='')
# Nonorthodox source from the explicit local-band host packet.
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));th=(0,1,0,1,0)
P=((4,4,4),(4,1,3),(4,4,1));U=tuple(product(range(3),range(5),range(3)))
def p(a,b):return(a[0],A[A[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
Eu,us=signatures(U,p)
assert any(p(a,b) not in Eu for a,b in product(Eu,repeat=2))
assert all((us[a]==us[b])==((a[0],th[a[1]],a[2])==(b[0],th[b[1]],b[2])) for a,b in product(U,repeat=2))
print('nonorthodox source=',len(U),' actual_actor=',len(set(us.values())),' group_order=2 and nontrivial rectangle',sep='')
print('PASS all actual idempotence signatures; auxiliary-actor distinction retained')
print('LIMIT finite same-author checks; general dichotomy is symbolic')
