#!/usr/bin/env python3
"""Exact extreme-rational checks for product Hessian and conservative constants."""

import importlib.util
import json
import random
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("hessian",ROOT/"frontier-20261028-57-product-hessian-exact.py")
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
e=h.e


def main():
    rng=random.Random(2026102858)
    rows=[]
    for t in (F(1,10**33),F(1,10**6),F(1,4)):
        data=[]
        for weight,func in ((2,h.h2),(3,h.h3),(4,h.h4)):
            v=h.build(weight,rng);A,M,N=h.data(v,t)
            k=func(v,t,A,M,N) if weight!=4 else func(t,A,M)
            assert k>=F(15,256)*t
            data.append((v,A,M,N,k))
        mixed=[e.add(e.add(data[0][0][i],data[1][0][i]),data[2][0][i]) for i in range(16)]
        Am,Mm,Nm=h.data(mixed,t)
        assert Nm==sum(entry[3] for entry in data)
        assert Am==sum(entry[3]*entry[1] for entry in data)/Nm
        for i in range(4):
            for j in range(4):
                expected=e.ZERO
                for entry in data:expected=e.add(expected,e.scale(entry[2][i][j],entry[3]/Nm))
                assert Mm[i][j]==expected
        gap01=2*(1+t)**3
        gap12=2*(1+t)**2*(1-t)
        assert gap01>=2 and gap12>=F(3,2)
        rows.append({"shrink":str(t),"all_three_hessian_identities":True,"mixed_weight_decomposition":True,"rescaled_reference_gap01":str(gap01),"rescaled_reference_gap12":str(gap12)})
    Qbound=68+2*68*800+2*6*800**2
    assert Qbound<8*10**6
    R1=F(6*1600**3*2,6)+F(68*1600**2*2,2)+68*1600*2+136
    assert R1<9*10**9
    R2=F(6*(2*10**8)**2*2,2)*F(1,10**6)+68*(2*10**8)*2+8*10**6*(2*10**8)*2*F(1,10**6)+9*10**9
    assert R2<10**12
    eps0=F(1,10**15);tstar=F(1,10**33)
    assert eps0<F(1,10**6) and 3*10**12*eps0<F(15,32)
    assert 2*eps0**2/(1+eps0**2)>F(1,10**30)
    assert 20*tstar<F(1,10**30)
    print(json.dumps({"scope":"finite exact endpoint/constant consistency checks, not a proof of universal perturbation theory", "rows":rows,"second_order_offblock_bound":str(Qbound),"first_conjugation_remainder_coefficient_upper":str(R1),"second_conjugation_remainder_coefficient_upper":str(R2),"epsilon0":str(eps0),"candidate_uniform_shrink_bound":str(tstar),"all_rational_constant_inequalities":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
