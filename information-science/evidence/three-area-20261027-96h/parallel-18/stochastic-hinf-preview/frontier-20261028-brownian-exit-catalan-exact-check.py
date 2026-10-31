#!/usr/bin/env python3
"""Exact rational enclosure for the Brownian exit E[sqrt(tau)] constant."""
from fractions import Fraction as F


def atan_partial(q,last):
    return sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(last+1)),F(0))


def main():
    pi_lo=16*atan_partial(5,11)-4*atan_partial(239,2)
    pi_hi=16*atan_partial(5,10)-4*atan_partial(239,3)
    G_hi=sum((F((-1)**k,(2*k+1)**2) for k in range(201)),F(0))
    G_lo=G_hi-F(1,403**2)
    lower_sq=F(32)*G_lo**2/pi_hi**3
    upper_sq=F(32)*G_hi**2/pi_lo**3
    assert pi_lo>0 and G_lo>0 and pi_lo<pi_hi and G_lo<G_hi
    assert lower_sq>F(9305,10000)**2
    assert upper_sq<F(9306,10000)**2
    print('PASS: exact alternating-series rational enclosures')
    print('9305/10000 < E[sqrt(tau)] < 9306/10000')
    print('10000/9306 < 1/E[sqrt(tau)] < 10000/9305')
    print('scope: rational arithmetic conditional on named Brownian exit-series and Machin identity')


if __name__=='__main__':main()
