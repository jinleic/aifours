#!/usr/bin/env python3
"""Exact rational consistency checks for all-parameter product-tube constants."""

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


def constants(delta):
    gap=2*delta
    s1=F(1020,1)/delta
    q0=510+2*510*s1+2*16*s1*s1
    s2=2*q0/delta
    limit=min(F(1),1/(4*s1),1/(4*s2),gap/8160,gap/(8*q0))
    first=16*(2*s1)**3*F(2,6)+510*(2*s1)**2+510*(2*s1)*2+1020
    C=16*(2*s2)**2*limit+2*510*(2*s2)+2*q0*(2*s2)*limit+first
    radius=min(limit,delta/(6*C))
    assert 2*limit*s1<=F(1,2) and 2*limit*limit*s2<=F(1,2)
    assert 2040*limit<=gap/4
    assert 510*limit+q0*limit*limit<gap/4
    assert 3*C*radius<=delta/2
    return {"delta":str(delta),"gap":str(gap),"temporary_limit":str(limit),"matrix_remainder_bound":str(C),"product_radius":str(radius)}


def main():
    delta=F(1,10);rng=random.Random(2026102868);checks=0
    for t in (delta,F(1,2),1-delta):
        for _ in range(5):
            for weight,fn in ((2,h.h2),(3,h.h3),(4,h.h4)):
                v=h.build(weight,rng);A,M,N=h.data(v,t)
                k=fn(v,t,A,M,N) if weight!=4 else fn(t,A,M)
                assert k>=t*delta/16
                checks+=1
    print(json.dumps({"scope":"finite exact Hessian and scalar constant checks; not an all-state proof", "rational_delta_cases":[constants(F(1,10)),constants(F(1,4))], "weight_t_checks":checks,"all_margin_and_constant_checks":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
