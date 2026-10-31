#!/usr/bin/env python3
"""Exhaust the least band quotient for the finite original source and its dual."""
from collections import deque
from itertools import product
A=range(5)
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,4),(4,4,3))
th=(0,1,0,1,0)
S=tuple(product(range(3),A,range(3)))
ix={s:i for i,s in enumerate(S)}
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
M=[[ix[sm(a,b)] for b in S] for a in S]

def check(dual):
    op=([[M[b][a] for b in range(45)] for a in range(45)] if dual else M)
    roots=list(range(45)); todo=deque()
    def find(a):
        while roots[a]!=a:
            roots[a]=roots[roots[a]];a=roots[a]
        return a
    def unite(a,b):
        a,b=find(a),find(b)
        if a==b:return
        roots[b]=a;todo.append((a,b))
    for a in range(45):unite(a,op[a][a])
    while todo:
        a,b=todo.popleft()
        for c in range(45):
            unite(op[a][c],op[b][c]);unite(op[c][a],op[c][b])
    for a,b in product(range(45),repeat=2):
        same_rectangle=S[a][0]==S[b][0] and S[a][2]==S[b][2]
        assert (find(a)==find(b))==same_rectangle
    def actor(a):s=S[a];return (s[0],th[s[1]],s[2])
    coll=[(a,b) for a in range(45) for b in range(a)
          if actor(a)==actor(b) and find(a)==find(b)]
    E=[a for a in range(45) if op[a][a]==a]
    pairs=[(a,b) for a,b in product(E,repeat=2) if a!=b and actor(a)==actor(b)]
    rp=[(a,b) for a,b in pairs if op[a][b]==b and op[b][a]==a]
    lp=[(a,b) for a,b in pairs if op[a][b]==a and op[b][a]==b]
    e=ix[(0,0,0)];f=ix[(0,2,0)]
    assert actor(e)==actor(f) and find(e)==find(f) and e!=f
    assert (op[e][f],op[f][e])==((e,f) if dual else (f,e))
    print('dual=%s quotient=%d same_actor_collisions=%d R_pairs=%d L_pairs=%d'%(dual,len({find(a) for a in range(45)}),len(coll),len(rp),len(lp)))
    print('specified pair=',S[e],S[f], 'op products=',S[op[e][f]],S[op[f][e]])

check(False)
check(True)
print('PASS congruence closure and exact quotient; action-trivial host cannot separate specified pair')
