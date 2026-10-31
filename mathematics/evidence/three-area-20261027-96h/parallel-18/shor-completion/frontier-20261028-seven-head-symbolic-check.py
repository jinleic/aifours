#!/usr/bin/env python3
"""Symbolic integer-identity checks for the all-order |P|>=7 certificate.

Triples (constant, coeff_U, coeff_V) are formal integer expressions. The
mathematical reason a collision refutes a candidate is distinctness of the
listed P members in the underlying direct factorization; identities alone do
not independently prove existence of such a factorization.
"""

Z=(0,0,0);C=lambda n:(n,0,0);U=(0,1,0);V=(0,0,1)
def add(*xs):return tuple(map(sum,zip(*xs)))
def neg(x):return tuple(-a for a in x)
def sub(x,y):return add(x,neg(y))

P=[C(0),C(3),C(8),C(11),U,V]
# Each item: candidate q, p used with q, forced/old q, p used there.
def check_step(first,second):
    edge=add(C(4),first,neg(second))
    t4=add(first,C(4))
    tab4=[(add(first,C(4)),C(3),C(7),first),
          (add(first,C(1)),C(0),C(1),first),
          (add(first,C(-4)),C(11),C(7),first),
          (add(first,C(-7)),C(8),C(1),first),
          (C(4),C(0),C(1),C(3))]
    assert set(q for q,_,_,_ in tab4)|{edge}=={sub(t4,p) for p in P}
    for q,p,anchor,p2 in tab4:
        assert p!=p2 and add(q,p)==add(anchor,p2)
    t9=add(first,C(9))
    tab9=[(add(first,C(6)),C(8),C(14),first),
          (add(first,C(1)),C(0),C(1),first),
          (add(first,C(-2)),C(3),C(1),first),
          (C(9),C(0),C(1),C(8)),
          (add(edge,C(5)),C(3),edge,C(8))]
    assert set(q for q,_,_,_ in tab9)|{t9}=={sub(t9,p) for p in P}
    for q,p,anchor,p2 in tab9:
        assert p!=p2 and add(q,p)==add(anchor,p2)
    return edge,t9


def main():
    e1,q1=check_step(U,V);e2,q2=check_step(V,U)
    assert add(q1,V)==add(q2,U)==add(U,V,C(9))
    # The P-size-five step is the same target4 table with no V option.
    # The earlier P=A no-go: target6, Q contains 0 and 1.
    tab0=[(C(6),C(3),C(1),C(8)),(C(3),C(0),C(0),C(3)),
          (C(-2),C(3),C(1),C(0)),(C(-5),C(8),C(0),C(3))]
    assert {q for q,_,_,_ in tab0}=={sub(C(6),p) for p in P[:4]}
    for q,p,anchor,p2 in tab0:assert p!=p2 and add(q,p)==add(anchor,p2)
    # A known SAT control if the Shor Q anchors are removed.
    for n in (60,1320):
        S={0,3,8,11,19,28};Q=set(range(0,n,6))
        sums=[(p+q)%n for p in S for q in Q]
        assert len(sums)==len(set(sums))==n
        assert not {0,1,7,13,14}<=Q
    print('PASS: formal collision identities, candidate coverage, symmetry, final double-hit')
    print('PASS: cyclic SAT controls n=60,1320 when old Q anchors are removed')
    print('Scope: algebraic identity checks only; unbounded theorem uses the written directness proof')

if __name__=='__main__':main()
