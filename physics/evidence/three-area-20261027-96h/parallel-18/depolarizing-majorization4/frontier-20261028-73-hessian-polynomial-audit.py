#!/usr/bin/env python3
"""Exact finite polarization/interpolation audit for product Hessian identities.

The written degree argument is required for universal-t extrapolation. The
h2/h3/h4 inequalities are only sampled; this program checks no global theorem.
"""

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
    same=cross=singles=0
    for k in range(1,33):
        t=F(k,33)
        cache={}
        for i in indices:
            v=basis(i);A,M,N=h.data(v,t)
            if i.bit_count()==2:h.h2(v,t,A,M,N)
            elif i.bit_count()==3:h.h3(v,t,A,M,N)
            else:h.h4(t,A,M)
            cache[i]=(A,M,N);singles+=1
        for i,j in itertools.combinations(indices,2):
            for phase in (e.ONE,e.IMAG):
                v=basis(i);v[j]=phase;A,M,N=h.data(v,t)
                if i.bit_count()==j.bit_count():
                    if i.bit_count()==2:h.h2(v,t,A,M,N)
                    elif i.bit_count()==3:h.h3(v,t,A,M,N)
                    else:h.h4(t,A,M)
                    same+=1
                else:
                    Ai,Mi,Ni=cache[i];Aj,Mj,Nj=cache[j]
                    assert N==Ni+Nj and A==(Ni*Ai+Nj*Aj)/N
                    for row in range(4):
                        for col in range(4):
                            expected=e.scale(e.add(e.scale(Mi[row][col],Ni),e.scale(Mj[row][col],Nj)),1/N)
                            assert M[row][col]==expected
                    cross+=1
    print(json.dumps({"scope":"exact basis-polarization/interpolation data; inequalities remain sampled and require written proof", "distinct_rational_shrinkages":32,"shrinkages":"k/33, k=1,...,32", "basis_directions":singles,"same_weight_real_imag_pairs":same,"cross_weight_real_imag_pairs":cross,"total_exact_directions":singles+same+cross,"max_written_cleared_polynomial_degree":31},indent=2,sort_keys=True))


if __name__=="__main__":main()
