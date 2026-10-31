#!/usr/bin/env python3
"""Exact arithmetic for an abstract all-other-prefix/logdet/Schatten obstruction."""
from fractions import Fraction as F
import json


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def product(roots):
    out=[1]
    for root in roots:out=mul(out,[root,1])
    return out


def main():
    x=[77,42,42,39,39,21]+[20]*5+[10]*4+[5]
    y=[80]+[40]*4+[20]*6+[10]*4+[5]
    assert len(x)==len(y)==16 and sum(x)==sum(y)==405
    assert all(x[i]>=x[i+1] and y[i]>=y[i+1] for i in range(15))
    prefix=[sum(x[:i])-sum(y[:i]) for i in range(1,17)]
    assert prefix==[-3,-1,1,0,-1,0,0,0,0,0,0,0,0,0,0,0]
    xp=product([77,42,42,39,39,21]);yp=product([80,40,40,40,40,20])
    diff=[a-b for a,b in zip(xp,yp)]
    assert diff==[242482148,26418964,1074361,19336,130,0,0]
    assert all(z>=0 for z in diff) and diff[0]>0
    A,Q,R,eps=F(16,81),F(8,81),F(4,81),F(1,405)
    for s in (F(0),eps):
        assert A-3*s>=Q+2*s>=Q-s>=R+s>0
        assert Q-R>=5*s
        assert 3*(A-Q)>=18*s
        assert 3*A-2*Q-R>=20*s
    print(json.dumps({'scope':'abstract spectra only; x is not asserted to be a depolarizing channel output',
                      'denominator':405,'x':x,'product_reference_y':y,
                      'all_prefix_differences_numerator':prefix,
                      'strict_k3_excess':str(F(1,405)),
                      'logdet_difference_polynomial_coefficients_low_to_high':diff,
                      'all_shift_logdet_proof':'nonnegative exact polynomial coefficients',
                      'all_q_schatten_proof':'exact endpoint linear conditions for the written convex/concave power argument',
                      'conditions_hold_at_s_0_and_epsilon':True},indent=2,sort_keys=True))


if __name__=='__main__':main()
