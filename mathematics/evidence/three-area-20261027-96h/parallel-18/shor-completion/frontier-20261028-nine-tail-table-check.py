#!/usr/bin/env python3
"""Check explicit all-order collision tables excluding eight-element Q."""
C=lambda x:(x,0,0,0)
U=(0,1,0,0);V=(0,0,1,0);W=(0,0,0,1)
def add(*xs):return tuple(map(sum,zip(*xs)))
def neg(x):return tuple(-a for a in x)
def sub(x,y):return add(x,neg(y))
z,o,s,th,fo=[C(x) for x in (0,1,7,13,14)]
Q=[z,o,s,th,fo,U,V,W];A={C(x) for x in (0,3,8,11)}

def row(t,survivors,w,known):
    assert set(w)|set(survivors)==set(Q) and not set(w)&set(survivors)
    for src,(anchor,p,p2) in w.items():
        assert anchor in known and p in Q and p2 in Q and p!=p2
        assert add(sub(t,src),p)==add(anchor,p2)
    return [sub(t,p) for p in survivors]

def force(t,survivor,w,known):
    out=row(t,[survivor],w,known)[0];known.add(out);return out


def main():
    known=set(A)
    root=row(add(W,C(1)),[th,U,V],{
      z:(C(8),s,W),o:(z,z,W),s:(C(8),fo,W),fo:(z,th,W),W:(z,z,o)},known)
    assert root==[add(W,C(-12)),add(W,neg(U),C(1)),add(W,neg(V),C(1))]
    # The last two branches are symmetric under U <-> V.
    B=root[0];common=set(known);common.add(B)
    second=row(add(V,C(1)),[U,W],{
      z:(C(8),s,V),o:(z,z,V),s:(C(8),fo,V),th:(B,W,V),
      fo:(z,th,V),V:(z,z,o)},common)
    assert second==[add(V,neg(U),C(1)),add(V,neg(W),C(1))]

    # Case A1: B=W-12 and T=V-U+1.
    T=second[0];p=set(common);p.add(T)
    D=force(add(V,C(2)),W,{
      z:(C(3),o,V),o:(C(8),s,V),s:(C(8),th,V),th:(C(3),fo,V),
      fo:(B,W,V),U:(T,z,o),V:(C(3),o,z)},p)
    assert D==add(V,neg(W),C(2))
    E=force(add(U,C(2)),V,{
      z:(C(3),o,U),o:(C(8),s,U),s:(C(8),th,U),th:(C(3),fo,U),
      fo:(B,W,U),U:(C(3),o,z),W:(D,V,U)},p)
    assert E==add(U,neg(V),C(2))
    F=force(C(2),V,{
      z:(C(3),o,z),o:(z,z,o),s:(C(8),th,z),th:(C(3),fo,z),
      fo:(z,th,o),U:(T,V,o),W:(D,V,z)},p)
    assert F==add(C(2),neg(V)) and add(E,z)==add(F,U) and z!=U

    # Case A2: B=W-12 and T=V-W+1.
    T=second[1];p=set(common);p.add(T)
    D=force(add(V,C(2)),U,{
      z:(C(3),o,V),o:(C(8),s,V),s:(C(8),th,V),th:(C(3),fo,V),
      fo:(B,W,V),V:(C(3),o,z),W:(T,z,o)},p)
    assert D==add(V,neg(U),C(2))
    E=force(add(U,C(1)),V,{
      z:(C(8),s,U),o:(z,z,U),s:(C(8),fo,U),th:(B,W,U),
      fo:(z,th,U),U:(z,z,o),W:(T,V,U)},p)
    assert E==add(U,neg(V),C(1))
    assert row(C(2),[],{
      z:(C(3),o,z),o:(z,z,o),s:(C(8),th,z),th:(C(3),fo,z),
      fo:(z,th,o),U:(D,V,z),V:(E,U,o),W:(T,V,o)},p)==[]

    # Case B: B=W-U+1 (the remaining root option is symmetric).
    B=root[1];p=set(known);p.add(B)
    D=force(add(W,C(2)),V,{
      z:(C(3),o,W),o:(C(8),s,W),s:(C(8),th,W),th:(C(3),fo,W),
      fo:(B,th,U),U:(B,z,o),W:(C(3),o,z)},p)
    assert D==add(W,neg(V),C(2))
    E=force(C(2),W,{
      z:(C(3),o,z),o:(z,z,o),s:(C(8),th,z),th:(C(3),fo,z),
      fo:(z,th,o),U:(B,W,o),V:(D,W,z)},p)
    assert E==sub(C(2),W)
    F=force(add(V,C(1)),th,{
      z:(C(8),s,V),o:(z,z,V),s:(C(8),fo,V),fo:(z,th,V),
      U:(B,W,V),V:(z,z,o),W:(E,o,V)},p)
    assert F==add(V,C(-12))
    G=force(add(U,C(2)),fo,{
      z:(C(3),o,U),o:(C(8),s,U),s:(C(8),th,U),th:(C(3),fo,U),
      U:(C(3),o,z),V:(D,W,U),W:(E,z,U)},p)
    assert G==add(U,C(-12)) and add(F,U)==add(G,V) and U!=V
    print('PASS: explicit 8-tail table identities, branch coverage, both collision types')
    print('Assumptions: direct tiling; Q=Y plus three distinct extras; A subset P')

if __name__=='__main__':main()
