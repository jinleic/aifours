#!/usr/bin/env python3
"""Exact GME counterexample to pointwise output lambda_2 domination, not k3."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("inertia",ROOT/"frontier-20261028-35-entangled-frame-saturation.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
sc,c,b,e=m.sc,m.c,m.b,m.e


def main():
    v=[F(0)]*16
    for i,value in ((0,10),(3,1),(5,1),(15,1)):v[i]=F(value)
    rho=[[e.z(v[i]*v[j]/103) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    cuts=[]
    for size in (1,2):
        for active in itertools.combinations(range(4),size):
            if size==2 and 0 not in active:continue
            rest=tuple(i for i in range(4) if i not in active)
            matrix=[[F(0) for _ in range(2**len(rest))] for _ in range(2**len(active))]
            for index in range(16):
                bits=[(index>>(3-i))&1 for i in range(4)]
                row=sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col=sum(bits[i]*2**(len(rest)-1-j) for j,i in enumerate(rest))
                matrix[row][col]=v[index]
            rank=sc.rectangular_rank(matrix);assert rank>=2
            cuts.append({"parties_zero_based":list(active),"schmidt_rank":rank})
    p=F(1,5);out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
    assert len(c.positive_definite_ldl(out))==16
    reference_lambda2=F(729,10000);reference_top3=F(8019,10000)
    u=[F(0)]*16;u[0]=1
    w=[F(0)]*16;w[2]=20;w[4]=20;w[7]=3
    assert sum(x*x for x in w)==809
    def form(x,y):
        value=e.ZERO
        for i in range(16):
            for j in range(16):value=e.add(value,e.scale(out[i][j],x[i]*y[j]))
        return value
    diagonal0=form(u,u);diagonalw=e.scale(form(w,w),F(1,809));cross=form(u,w)
    assert diagonal0[1]==diagonalw[1]==0 and cross==e.ZERO
    assert diagonal0[0]>reference_lambda2 and diagonalw[0]>reference_lambda2
    P=e.zero(16);P[0][0]=e.ONE;P[8][8]=e.ONE
    for i in range(16):
        for j in range(16):P[i][j]=e.add(P[i][j],e.z(F(w[i]*w[j],809)))
    assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
    sameP=e.trace(e.matmul(P,out));assert sameP[1]==0
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    upper1=e.add_matrix(e.scale_matrix(ident,F(81,125)),e.scale_matrix(out,-1))
    assert len(c.positive_definite_ldl(upper1))==16
    upper2=e.add_matrix(e.scale_matrix(ident,F(73,1000)),e.scale_matrix(out,-1))
    assert m.hermitian_inertia(upper2)==(15,1,0)
    bound=F(81,125)+2*F(73,1000)
    assert bound==F(397,500) and reference_top3-bound==F(79,10000)>0
    matrix=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
    eigen=np.linalg.eigvalsh(matrix)[::-1]
    print(json.dumps({"scope":"exact GME violation of individual lambda2 comparison, not an original k3 violation", "state":"(10|0000>+|0011>+|0101>+|1111>)/sqrt(103)","physical_p":"1/5","reference_lambda2":str(reference_lambda2),"reference_top3":str(reference_top3),"schmidt_cut_ranks":cuts,"positive_subspace_rayleigh_0":str(diagonal0[0]),"positive_subspace_rayleigh_w":str(diagonalw[0]),"positive_subspace_cross":"0","w_integer_support":{"2":20,"4":20,"7":3},"w_norm_squared":809,"physical_rank3_projector_trace":str(sameP[0]),"output_positive_ldl_pivots":16,"upper_lambda1_81_over_125_ldl_pivots":16,"upper_lambda2_73_over_1000_inertia":[15,1,0],"certified_top3_upper":str(bound),"certified_reference_margin_lower":"79/10000","numerical_top3_eigenvalues":[float(x) for x in eigen[:3]],"numerical_top3_sum":float(sum(eigen[:3]))},indent=2,sort_keys=True))


if __name__=="__main__":main()
