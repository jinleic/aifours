#!/usr/bin/env python3
"""Exact symbolic coefficient checks for selected 121 self-audit identities."""
from fractions import Fraction as F
import json


def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)


def scale(a,c):return trim([x*F(c) for x in a])


def sub(a,b):return add(a,scale(b,-1))


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)


def power(a,n):
    out=[F(1)]
    for _ in range(n):out=mul(out,a)
    return out


def eq(a,b):assert sub(a,b)==[F(0)]


def main():
    one=[F(1)];t=[F(0),F(1)];a=[F(1,2),F(1,2)];b=[F(1,2),F(-1,2)]
    D3=sub(one,mul(a,b));D4=add(power(a,2),power(b,2))
    lam=[mul(power(a,4-i),power(b,i)) for i in range(5)]
    eq(sub(lam[0],lam[2]),mul(power(a,2),t))
    eq(sub(lam[1],lam[3]),mul(mul(a,b),t))
    eq(sub(lam[0],lam[3]),mul(mul(a,t),D3))
    eq(sub(lam[1],lam[4]),mul(mul(b,t),D3))
    eq(sub(lam[0],lam[4]),mul(t,D4))
    # Eq. 19: 32 D3 times the stated upper bound equals the negative factorization.
    terms=add(add(scale(mul(mul(a,t),power(D3,2)),-32),
                  scale(mul(mul(mul(power(a,2),b),t),D3),-64)),
              add(scale(mul(mul(power(t,2),power(b,2)),D3),32),scale(power(t,5),32)))
    f=[F(15),F(24),F(38),F(32),F(3)]
    expected=scale(mul(mul(t,sub(one,t)),f),-1)
    eq(terms,expected)
    # Product-reference exact spectrum and erasure coefficient formula.
    ref=add(power(a,4),scale(mul(power(a,3),b),2))
    eq(scale(ref,16),[F(3),F(8),F(6),F(0),F(-1)])
    p=sub(one,t)
    layers=add(add(power(t,4),scale(mul(power(t,3),p),3)),
               add(scale(mul(power(t,2),power(p,2)),3),
                   add(scale(mul(t,power(p,3)),F(5,4)),scale(power(p,4),F(3,16)))))
    eq(ref,layers)
    # Equal-radius harmonic coefficient identities after clearing denominators.
    ss=t
    eq(sub(scale(sub([F(3)],ss),2),sub([F(4)],ss)),sub([F(2)],ss))
    eq(sub(sub([F(3)],ss),one),sub([F(2)],ss))
    eq(sub(scale(sub([F(3)],ss),2),ss),scale(sub([F(2)],ss),3))
    assert F(580473701,600000000)<1
    assert F(54870831,17600000)<F(13,4)
    assert 2-2*F(441,1000)>F(11,10)
    assert F(81,800)>F(1,10)
    assert F(64,3)+F(16,9)==F(208,9)
    print(json.dumps({'scope':'exact polynomial and scalar identities only; not a proof of matrix, physical-state or universal channel steps',
                     'checks':['five product eigenvalue gaps','weight-three factorization (19)',
                               'reference spectral polynomial and erasure coefficients',
                               'three equal-radius harmonic algebra identities',
                               'displayed remainder, block-gap, far-gap and rank12 moment constants'],
                     'all_checks_passed':True},indent=2,sort_keys=True))


if __name__=='__main__':main()
