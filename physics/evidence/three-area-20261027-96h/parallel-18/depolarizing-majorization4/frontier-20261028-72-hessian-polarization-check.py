#!/usr/bin/env python3
"""Exact basis/polarization audit of product Hessian identities at fixed t."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("hessian",ROOT/"frontier-20261028-57-product-hessian-exact.py")
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
e=h.e


def basis(index,phase=e.ONE):
    result=[e.ZERO]*16;result[index]=phase;return result


def main():
    indices=[i for i in range(16) if i.bit_count()>=2]
    assert len(indices)==11
    results=[]
    for t in (F(1,10**7),F(1,4),F(4,5)):
        singles={}
        for i in indices:
            v=basis(i);A,M,N=h.data(v,t)
            if i.bit_count()==2:h.h2(v,t,A,M,N)
            elif i.bit_count()==3:h.h3(v,t,A,M,N)
            else:h.h4(t,A,M)
            singles[i]=(A,M,N)
        same=cross=0
        for i,j in itertools.combinations(indices,2):
            for phase in (e.ONE,e.IMAG):
                v=basis(i);v[j]=phase;A,M,N=h.data(v,t)
                if i.bit_count()==j.bit_count():
                    if i.bit_count()==2:h.h2(v,t,A,M,N)
                    elif i.bit_count()==3:h.h3(v,t,A,M,N)
                    else:h.h4(t,A,M)
                    same+=1
                else:
                    Ai,Mi,Ni=singles[i];Aj,Mj,Nj=singles[j]
                    assert N==Ni+Nj and A==(Ni*Ai+Nj*Aj)/N
                    for row in range(4):
                        for col in range(4):
                            expect=e.scale(e.add(e.scale(Mi[row][col],Ni),e.scale(Mj[row][col],Nj)),1/N)
                            assert M[row][col]==expect
                    cross+=1
        results.append({"shrink":str(t),"single_basis_directions":len(indices),"same_weight_real_imag_pair_tests":same,"cross_weight_real_imag_pair_tests":cross})
    print(json.dumps({"scope":"exact basis/polarization checks at three rational shrinkages; no universal-t or global-k3 proof", "results":results,"total_exact_directions":sum(row["single_basis_directions"]+row["same_weight_real_imag_pair_tests"]+row["cross_weight_real_imag_pair_tests"] for row in results)},indent=2,sort_keys=True))


if __name__=="__main__":main()
