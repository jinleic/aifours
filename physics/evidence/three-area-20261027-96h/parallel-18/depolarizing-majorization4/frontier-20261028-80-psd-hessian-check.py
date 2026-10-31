#!/usr/bin/env python3
"""Exact checks of the weight-two PSD Hessian improvement and constants."""

import importlib.util
import json
import random
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("hessian",ROOT/"frontier-20261028-57-product-hessian-exact.py")
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
e=h.e


def weight2(v,t,A,M,N):
    a,bb=(1+t)/2,(1-t)/2
    gamma=[[e.ZERO for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k!=i and k!=j:
                    gamma[i][j]=e.add(gamma[i][j],e.scale(e.mul(v[h.MASK[i]|h.MASK[k]],e.conj(v[h.MASK[j]|h.MASK[k]])),1/N))
    n=[gamma[i][i][0] for i in range(4)]
    assert sum(n)==2 and all(0<=x<=1 for x in n)
    K=[[e.add(e.scale(gamma[i][j],t),e.z((1-2*t)*n[i] if i==j else 0)) for j in range(4)] for i in range(4)]
    assert sum(K[i][i][0] for i in range(4))==2*(1-t)
    for i in range(4):
        for j in range(4):
            target=e.scale(e.add(K[i][j],e.z(-(1-t) if i==j else 0)),a*bb*t*(1+t))
            assert M[i][j]==target
    assert A==-a*a*t*(1-t*t)
    return a*a*t*(1-t*t)


def main():
    rng=random.Random(2026102880);count=0
    for t in (F(1,1000),F(1,10),F(1,2)):
        for _ in range(20):
            v=h.build(2,rng);A,M,N=h.data(v,t);k=weight2(v,t,A,M,N)
            assert k>0;count+=1
    for _ in range(5):
        t=F(1,1000)
        v2,v3,v4=(h.build(weight,rng) for weight in (2,3,4))
        A2,M2,N2=h.data(v2,t);k2=weight2(v2,t,A2,M2,N2)
        A3,M3,N3=h.data(v3,t);k3=h.h3(v3,t,A3,M3,N3)
        A4,M4,N4=h.data(v4,t);k4=h.h4(t,A4,M4)
        assert min(k2,k3,k4)>=F(15,64)*t
    tmax=F(1,1000);eps=F(3,100);target=F(8,100000)
    assert 512*tmax*tmax<F(23,1000)**2
    assert F(23,1000)/2<F(3,250)
    Qoff=8+F(23,1000)+2*F(23,1000)*F(3,250)+2*5*F(3,250)**2
    Q=16+F(23,1000)+2*F(23,1000)*F(3,250)+2*5*F(3,250)**2
    assert Qoff<F(81,10) and Q<17 and F(81,10)/2<F(41,10)
    R=F(23,1000)+17*eps;assert R<F(27,50)
    first=F(5,1)*F(3,125)**3/F(3)+F(23,1000)*F(3,125)**2+2*17*F(3,125)+F(27,50)
    assert first<F(7,5)
    second=5*F(41,5)**2*eps+2*F(23,1000)*F(41,5)+2*17*F(41,5)*eps+F(7,5)
    assert second==F(12642,625)<F(203,10)
    assert 3*F(203,10)*eps<F(15,8)
    assert 20*target<2*eps**2/(1+eps**2)
    print(json.dumps({"scope":"finite exact matrix and scalar checks; not a universal theorem or operator review", "seed":2026102880,"weight2_PSD_decomposition_cases":count,"mixed_weight_margin_cases":5,"Q_offblock_upper":str(Qoff),"first_remainder_upper":str(first),"second_remainder_upper":str(second),"gamma":"15/4","epsilon0":str(eps),"candidate_uniform_t":str(target),"all_exact_checks":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
