#!/usr/bin/env python3
"""Exact rational algebra checks for the written Brownian KKT candidate."""
from fractions import Fraction as F


def variance_pair(times,weights):
    return 2*sum(weights[i]*weights[j]*min(times[i],times[j])**2
                 for i in range(len(times)) for j in range(len(times)))


def variance_tail(times,weights):
    breaks=sorted(set([F(0),F(1),*times])); total=F(0)
    for lo,hi in zip(breaks,breaks[1:]):
        mid=(lo+hi)/2
        tail=sum((weights[i] for i in range(len(times)) if times[i]>=mid),F(0))
        total+=2*(hi*hi-lo*lo)*tail*tail
    return total


def main():
    cases=[
      ((F(0),F(1,4),F(2,3),F(1)),(F(1,3),F(-1,2),F(1,4),F(-1,12))),
      ((F(0),F(1)),(F(1),F(-1))),
      ((F(1,3),F(2,3)),(F(1),F(-1))),
    ]
    for times,weights in cases:
        assert sum(weights)==0
        a=variance_pair(times,weights); b=variance_tail(times,weights)
        assert a==b and a>0
        print('exact signed covariance and tail integral:',a)
    eps=F(1,100); trace=1-eps/2; det=eps*(1-eps)/4
    assert trace<1 and det/trace>det
    print('two-time perturbation exact trace=',trace,'det=',det,
          '; lower small-eigenvalue bound=',det)
    print('scope: finite rational identities only; no continuum/KKT proof or optimizer calculation')


if __name__=='__main__':main()
