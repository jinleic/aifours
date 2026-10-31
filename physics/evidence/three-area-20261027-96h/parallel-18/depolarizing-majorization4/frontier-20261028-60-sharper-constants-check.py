#!/usr/bin/env python3
"""Exact arithmetic audit of proposed sharper uniform-noise constants."""

import json
from fractions import Fraction as F


def main():
    tmax=F(1,4)
    first_order_weight_bound=2*(54*tmax+108*tmax**2+81*tmax**3)
    assert first_order_weight_bound==F(1377,32)<44
    gap=F(3,2)
    S1=4*44/gap
    assert S1==F(352,3)<120
    Q=68+2*44*120+2*6*120**2
    assert Q==183428<190000
    S2=4*190000/gap
    assert S2==F(1520000,3)<600000
    eps_limit=F(1,10**4)
    assert 2*120*eps_limit<F(1,2)
    assert 2*600000*eps_limit**2<F(1,2)
    first=F(6*240**3*2,6)+F(44*240**2*2,2)+68*240*2+136
    assert first==30215176<31*10**6
    second=6*(2*600000)**2*eps_limit+2*44*(2*600000)+2*190000*(2*600000)*eps_limit+31*10**6
    assert second==1046200000<2*10**9
    eps0=F(1,10**11);tstar=F(1,10**24)
    assert eps0<eps_limit and 3*2*10**9*eps0<F(15,32)
    assert 2*eps0**2/(1+eps0**2)>F(1,10**22)
    assert 20*tstar<F(1,10**22)
    print(json.dumps({"scope":"exact arithmetic consistency only; not an independent perturbation theorem proof", "weight_one_elimination_bound":str(first_order_weight_bound),"S1_frobenius_bound":str(S1),"Q_norm_upper":Q,"S2_frobenius_bound":str(S2),"first_conjugation_remainder_coefficient_upper":str(first),"second_conjugation_remainder_coefficient_upper":str(second),"epsilon0":str(eps0),"proposed_uniform_t":str(tstar),"all_constant_inequalities":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
