#!/usr/bin/env python3
"""Exact selected original-channel endpoint checks for the PSD-Hessian candidate."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("endpoint",ROOT/"frontier-20261028-66-noise-endpoint-check.py")
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
m,c,b,e=d.m,d.c,d.b,d.e


def main():
    v=[e.ZERO]*16;v[0],v[3],v[7],v[15]=e.z(1500),e.z(1),e.z(0,2),e.z(2)
    rho=[[e.scale(e.mul(v[i],e.conj(v[j])),F(1,2250009)) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    P=e.zero(16)
    for i in (0,1,2):P[i][i]=e.ONE
    assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    upper1=F("0.06252000226681");upper2=F("0.06250999994662")
    rows=[]
    for p in (1-F(8,100000),1+F(8,100000)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(c.positive_definite_ldl(out))==16
        assert len(c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,upper1),e.scale_matrix(out,-1))))==16
        inertia=m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,upper2),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        t=abs(1-p);a,bb=(1+t)/2,(1-t)/2;ref=a**4+2*a**3*bb;upper=upper1+2*upper2
        assert ref>upper
        actualP=P if p<1 else e.global_spinflip(P)
        assert actualP==e.adjoint(actualP) and e.matmul(actualP,actualP)==actualP and e.trace(actualP)==e.z(3)
        tr=e.trace(e.matmul(actualP,out));assert tr[1]==0 and tr[0]<upper
        matrix=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out]);eig=np.linalg.eigvalsh(matrix)[::-1]
        rows.append({"p":str(p),"full_Pauli_equals_sequential":True,"output_positive_LDL_pivots":16,"lambda1_upper_positive_LDL_pivots":16,"lambda2_upper_inertia":[15,1,0],"certified_top3_upper":str(upper),"reference_top3":str(ref),"certified_gap_lower":str(ref-upper),"same_actual_projector_trace":str(tr[0]),"numerical_top3":[float(x) for x in eig[:3]]})
    print(json.dumps({"scope":"one exact physical input at two endpoints, not universal proof", "state":"(1500|0000>+|0011>+2i|0111>+2|1111>)/sqrt(2250009)","displayed_product_coordinate_epsilon":"1/500","rows":rows},indent=2,sort_keys=True))


if __name__=="__main__":main()
