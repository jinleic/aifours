#!/usr/bin/env python3
"""Exact symbolic collisions proving |Q| cannot be 6 or 7."""
C=lambda x:(x,0,0)
U=(0,1,0);V=(0,0,1)
def add(*xs):return tuple(map(sum,zip(*xs)))
def neg(x):return tuple(-i for i in x)
def sub(x,y):return add(x,neg(y))
Y=[C(x) for x in (0,1,7,13,14)];z,o,s,th,fo=Y
A={C(x) for x in (0,3,8,11)}

def row(Q,target,survivors,witness,known):
    assert set(witness)|set(survivors)==set(Q)
    assert not set(witness)&set(survivors)
    for src,(K,p,p2) in witness.items():
        assert K in known and p in Q and p2 in Q and p!=p2
        assert add(sub(target,src),p)==add(K,p2)
    return [sub(target,s) for s in survivors]

def force(Q,t,source,witness,known):
    v=row(Q,t,[source],witness,known)[0];known.add(v);return v


def main():
    # Six tails: Q=Y union {V}; P contains A.
    Q=Y+[V];P=set(A)
    D=force(Q,add(V,C(7)),o,{
       z:(C(8),o,V),s:(z,z,V),th:(C(8),fo,V),fo:(z,s,V),V:(z,z,s)},P)
    assert D==add(V,C(6))
    assert row(Q,add(V,C(12)),[],{
       z:(D,o,s),o:(C(11),z,V),s:(D,o,z),th:(z,o,V),
       fo:(C(11),th,V),V:(z,o,th)},P)==[]
    # Seven tails: Q=Y union {U,V}. Cover V+1.
    Q=Y+[U,V];P=set(A)
    choices=row(Q,add(V,C(1)),[th,U],{
       z:(C(8),s,V),o:(z,z,V),s:(C(8),fo,V),fo:(z,th,V),V:(z,z,o)},P)
    assert choices==[add(V,C(-12)),add(V,neg(U),C(1))]
    # Case I: B=V-12.
    B=choices[0];q=set(P);q.add(B)
    D=force(Q,add(U,C(2)),V,{
       z:(C(3),o,U),o:(C(8),s,U),s:(C(8),th,U),th:(C(3),fo,U),
       fo:(B,V,U),U:(C(3),o,z)},q)
    E=force(Q,add(U,C(1)),V,{
       z:(C(8),s,U),o:(z,z,U),s:(C(8),fo,U),th:(B,V,U),
       fo:(z,th,U),U:(z,z,o)},q)
    assert D==add(U,neg(V),C(2)) and E==add(U,neg(V),C(1))
    assert add(D,z)==add(E,o) and z!=o
    # Case II: B=V-U+1.
    B=choices[1];q=set(P);q.add(B)
    assert row(Q,add(V,C(2)),[],{
       z:(C(3),o,V),o:(C(8),s,V),s:(C(8),th,V),th:(C(3),fo,V),
       fo:(B,th,U),U:(B,z,o),V:(C(3),o,z)},q)==[]
    print('PASS: |Q|=6 and |Q|=7 collision/coverage cases')
    print('Scope: symbolic identities under distinct-Q and direct-tiling hypotheses')

if __name__=='__main__':main()
