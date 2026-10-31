#!/usr/bin/env python3
"""Exact finite and rational-constant checks for a sharper k3 noise interval."""

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
    tmax=F(1,100);eps=F(1,500);tstar=F(1,10**7)
    assert 512*tmax*tmax<F(1,16) and 512<23**2
    V=F(1,4);W=F(23);S1=F(1,6);gap=F(3,2)
    assert V/gap==S1
    Q=W+2*V*S1+2*6*S1*S1
    assert Q==F(281,12)<24
    assert F(24,1)/gap==16
    assert 2*S1*eps<F(1,2) and 2*16*eps*eps<F(1,2)
    first=F(6,1)*(2*S1)**3*F(2,6)+V*(2*S1)**2+W*(2*S1)*2+29
    assert first==F(4799,108)<45
    second=6*(2*16)**2*eps+2*V*(2*16)+2*24*(2*16)*eps+45
    assert second==F(1909,25)<77
    assert 3*77*eps<F(15,32)
    assert 2*eps**2/(1+eps**2)>eps**2
    assert 20*tstar<eps**2
    rng=random.Random(2026102864)
    v2,v3,v4=(h.build(k,rng) for k in (2,3,4))
    vals=[]
    for weight,v,fn in ((2,v2,h.h2),(3,v3,h.h3),(4,v4,h.h4)):
        A,M,N=h.data(v,tstar)
        k=fn(v,tstar,A,M,N) if weight!=4 else fn(tstar,A,M)
        assert k>=F(15,256)*tstar
        vals.append({"weight":weight,"identity_verified":True,"kappa_at_least_15t_over_256":True})
    mixed=[e.add(e.add(v2[i],v3[i]),v4[i]) for i in range(16)]
    Am,Mm,Nm=h.data(mixed,tstar)
    components=[h.data(v,tstar) for v in (v2,v3,v4)]
    assert Am==sum(N*A for A,_,N in components)/Nm
    for i in range(4):
        for j in range(4):
            expected=e.ZERO
            for A,M,N in components:expected=e.add(expected,e.scale(M[i][j],N/Nm))
            assert Mm[i][j]==expected
    print(json.dumps({"scope":"finite exact Hessian and constant checks only; not universal proof or perturbation audit", "candidate_uniform_t":str(tstar),"temporary_epsilon_limit":str(eps),"V_F_squared_upper_at_tmax":str(512*tmax*tmax),"Q_frobenius_upper":str(Q),"first_remainder_coefficient_upper":str(first),"second_remainder_coefficient_upper":str(second),"leading_three_hessian_checks":vals,"mixed_weight_decomposition":True,"all_rational_constants_verified":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
