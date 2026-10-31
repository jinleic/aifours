#!/usr/bin/env python3
"""Exact symbolic certificate ruling out 7-element Shor P borders.

A symbolic tuple is constant + coefficient_U U + coefficient_V V +
coefficient_W W. Every collision is certified as q+p=known_q+p' with
p,p' distinct members of P. Distinctness in a specialization is the theorem
hypothesis, not a claim that formal variables are numerically independent.
"""

C=lambda x:(x,0,0,0)
U=(0,1,0,0);V=(0,0,1,0);W=(0,0,0,1)
def plus(*xs):return tuple(map(sum,zip(*xs)))
def neg(x):return tuple(-i for i in x)
def minus(x,y):return plus(x,neg(y))
P=[C(0),C(3),C(8),C(11),U,V,W]
zero,three,eight,eleven=P[:4]
Y=[C(0),C(1),C(7),C(13),C(14)]
EU=plus(C(4),U,neg(V));EW=plus(C(4),W,neg(U))


def partition(target,survivors,witnesses,known):
    # Witness indexed by the P value used to represent target: the tuple
    # (known-q,p,p') certifies target-source+p = known-q+p'.
    assert set(witnesses)|set(survivors)==set(P)
    assert not set(witnesses)&set(survivors)
    for source,(anchor,p,p2) in witnesses.items():
        assert source in P and p in P and p2 in P and p!=p2 and anchor in known
        assert plus(minus(target,source),p)==plus(anchor,p2)
    return [minus(target,s) for s in survivors]


def force(target,survivor,witnesses,known):
    out=partition(target,[survivor],witnesses,known)[0]
    known.add(out);return out


def main():
    known=set(Y)
    first=partition(plus(U,C(4)),[V,W],{
       zero:(C(7),three,U),three:(C(1),zero,U),eight:(C(7),eleven,U),
       eleven:(C(1),eight,U),U:(C(1),zero,three)},known)
    assert first==[EU,plus(C(4),U,neg(W))]
    # The two remaining possibilities are exchanged by V<->W. WLOG EU.
    known.add(EU)
    assert force(plus(W,C(4)),U,{
       zero:(C(7),three,W),three:(C(1),zero,W),eight:(C(7),eleven,W),
       eleven:(C(1),eight,W),V:(EU,U,W),W:(C(1),zero,three)},known)==EW
    second=partition(plus(W,C(9)),[zero,V],{
       three:(C(14),eight,W),eight:(C(1),zero,W),eleven:(C(1),three,W),
       U:(EW,three,eight),W:(C(1),zero,eight)},known)
    assert second==[plus(W,C(9)),plus(W,neg(V),C(9))]

    # Branch I: W+9 is a Q element.
    q=set(known);T1=second[0];q.add(T1)
    T2=force(plus(U,C(9)),W,{
       zero:(T1,W,U),three:(C(14),eight,U),eight:(C(1),zero,U),
       eleven:(C(1),three,U),U:(C(1),zero,eight),V:(EU,three,eight)},q)
    assert T2==plus(U,neg(W),C(9))
    T3=force(plus(U,C(12)),zero,{
       three:(T1,W,U),eight:(C(7),three,U),eleven:(C(1),zero,U),
       U:(C(1),zero,eleven),V:(EU,zero,eight),W:(T2,zero,three)},q)
    assert T3==plus(U,C(12))
    T4=force(plus(W,neg(V),C(12)),V,{
       zero:(T1,V,three),three:(T1,V,zero),eight:(EU,U,W),
       eleven:(C(1),V,W),U:(EW,V,eight),W:(C(1),V,eleven)},q)
    assert T4==plus(W,neg(V),neg(V),C(12))
    assert partition(plus(U,neg(V),W,C(12)),[],{
       zero:(T3,V,W),three:(T1,V,U),eight:(EU,zero,W),eleven:(EU,three,W),
       U:(T1,V,three),V:(T4,zero,U),W:(EU,zero,eight)},q)==[]

    # Branch II: W−V+9 is a Q element.
    q=set(known);T1=second[1];q.add(T1)
    T2=force(plus(W,C(12)),zero,{
       three:(T1,zero,V),eight:(C(7),three,W),eleven:(C(1),zero,W),
       U:(EW,zero,eight),V:(T1,zero,three),W:(C(1),zero,eleven)},q)
    assert T2==plus(W,C(12))
    T3=force(plus(U,neg(V),W,C(12)),V,{
       zero:(T2,V,U),three:(T1,zero,U),eight:(EU,zero,W),eleven:(EU,three,W),
       U:(T1,zero,three),W:(EU,zero,eight)},q)
    assert T3==plus(U,neg(V),neg(V),W,C(12))
    T4=force(plus(W,neg(V),C(15)),V,{
       zero:(T2,V,three),three:(T1,zero,three),eight:(C(7),V,W),
       eleven:(EU,U,W),U:(EW,V,eleven),W:(C(7),V,eight)},q)
    assert T4==plus(W,neg(V),neg(V),C(15))
    assert plus(T3,three)==plus(T4,U) and three!=U
    print('PASS: both seven-head branches contradict direct cyclic coverage')
    print('PASS: root dichotomies, forced alternatives, collision identities and endpoint contradiction')
    print('Scope: formal integer-coefficient identity certificate; logical proof requires distinct P and tiling assumptions')


if __name__=='__main__':main()
