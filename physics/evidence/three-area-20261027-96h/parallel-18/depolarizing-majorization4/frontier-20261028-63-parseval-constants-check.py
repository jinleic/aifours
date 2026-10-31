#!/usr/bin/env python3
"""Exact scalar audit of Frobenius/Parseval perturbation constants."""

import json
from fractions import Fraction as F


def main():
    assert 4**2*2==32<6**2
    assert 16**2*2==512<23**2
    gap=F(3,2)
    assert F(6,1)/gap==4
    Q=23+2*6*4+2*6*4**2
    assert Q==263
    S2=F(Q,1)/gap
    assert S2==F(526,3)<176
    lim=F(1,1000)
    assert 2*4*lim<F(1,2) and 2*176*lim**2<F(1,2)
    first=F(6*8**3*2,6)+F(6*8**2*2,2)+23*8*2+29
    assert first==1805<1900
    second=6*(2*176)**2*lim+2*6*(2*176)+2*263*(2*176)*lim+1900
    assert second==F(881572,125)<8000
    eps0=F(1,10**5);tstar=F(1,10**12)
    assert eps0<lim and 3*8000*eps0<F(15,32)
    assert 2*eps0**2/(1+eps0**2)>F(1,10**10)
    assert 20*tstar<F(1,10**10)
    print(json.dumps({"scope":"exact scalar consistency only, not an independent operator or global proof", "V_Frobenius_upper":"4 sqrt(2) < 6", "W_Frobenius_upper":"16 sqrt(2) < 23", "Q_Frobenius_upper":Q, "S2_bound":str(S2), "first_remainder_coefficient_upper":str(first), "second_remainder_coefficient_upper":str(second), "epsilon0":str(eps0), "proposed_uniform_t":str(tstar), "all_rational_checks":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
