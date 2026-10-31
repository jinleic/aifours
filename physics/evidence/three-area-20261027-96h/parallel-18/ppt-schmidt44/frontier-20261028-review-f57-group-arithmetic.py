#!/usr/bin/env python3
"""Exact order/prime-part checks of cited maximal-subgroup formulas.

This is arithmetic on source-stated orders, not a group construction or a
proof that the cited maximal-subgroup classifications are complete.
"""
from math import gcd
import json


def ppart(n,p):
    out=1
    while n%p==0:
        n//=p; out*=p
    return out


def proper_divisors(n):
    return [d for d in range(1,n) if n%d==0]


def suzuki(n):
    q=2**n; m=(n-1)//2; theta=2**(m+1)
    total=q*q*(q*q+1)*(q-1)
    orders={'parabolic':q*q*(q-1),'dihedral':2*(q-1),
            'torus_plus':4*(q+theta+1),'torus_minus':4*(q-theta+1)}
    for d in proper_divisors(n):
        s=2**d
        if s>=8: orders['subfield_'+str(s)]=s*s*(s*s+1)*(s-1)
    assert (q+theta+1)*(q-theta+1)==q*q+1
    assert total%3!=0 and ppart(total,2)==q*q
    assert all(total%o==0 for o in orders.values())
    parts={k:ppart(o,2) for k,o in orders.items()}
    assert parts['parabolic']==q*q
    assert all(x<q*q for k,x in parts.items() if k!='parabolic')
    return {'n':n,'q':q,'group_order':total,'parabolic_index':total//orders['parabolic'],
            'orders_compared_including_all_proper_subfields':orders,'their_2parts':parts}


def ree(n):
    q=3**n; m=(n-1)//2; theta=3**(m+1)
    total=q**3*(q**3+1)*(q-1)
    orders={'parabolic':q**3*(q-1),'involution_centralizer':q*(q*q-1),
            'four_group_normalizer':6*(q+1),
            'hall_plus':6*(q+theta+1),'hall_minus':6*(q-theta+1)}
    for d in proper_divisors(n):
        q0=3**d
        orders['subfield_'+str(q0)]=q0**3*(q0**3+1)*(q0-1)
    assert (q+theta+1)*(q-theta+1)==q*q-q+1
    assert (q+1)*(q*q-q+1)==q**3+1
    assert ppart(total,3)==q**3
    assert all(total%o==0 for o in orders.values())
    parts={k:ppart(o,3) for k,o in orders.items()}
    assert parts['parabolic']==q**3
    assert all(x<q**3 for k,x in parts.items() if k!='parabolic')
    return {'n':n,'q':q,'group_order':total,'parabolic_index':total//orders['parabolic'],
            'orders_compared_including_all_proper_subfields':orders,'their_3parts':parts}


print(json.dumps({'suzuki':[suzuki(n) for n in (3,5,7,9,15)],
                  'ree':[ree(n) for n in (3,5,7,9,15)],
                  'limits':'arithmetic checks only; maximality and list completeness are external imports'},indent=2))
