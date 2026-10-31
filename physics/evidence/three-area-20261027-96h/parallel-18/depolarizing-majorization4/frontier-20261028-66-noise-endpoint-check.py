#!/usr/bin/env python3
"""Exact original-channel endpoint checks for one near-product complex input."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("inertia",ROOT/"frontier-20261028-35-entangled-frame-saturation.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
c,b,e=m.c,m.b,m.e


def main():
    v=[e.ZERO]*16
    v[0],v[3],v[7],v[15]=e.z(1500),e.z(1),e.z(0,2),e.z(2)
    N=2250009
    rho=[[e.scale(e.mul(v[i],e.conj(v[j])),F(1,N)) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    P=e.zero(16)
    for k in (0,1,2):P[k][k]=e.ONE
    assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    upper1=F("0.06250002499984")
    upper2=F("0.06250001249994")
    rows=[]
    for p in (1-F(1,10**7),1+F(1,10**7)):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        assert len(c.positive_definite_ldl(out))==16
        H1=e.add_matrix(e.scale_matrix(ident,upper1),e.scale_matrix(out,-1))
        assert len(c.positive_definite_ldl(H1))==16
        H2=e.add_matrix(e.scale_matrix(ident,upper2),e.scale_matrix(out,-1))
        inertia=m.hermitian_inertia(H2)
        assert inertia==(15,1,0)
        t=abs(1-p);a,bb=(1+t)/2,(1-t)/2
        reference=a**4+2*a**3*bb
        top_upper=upper1+2*upper2
        assert reference>top_upper
        actualP=P if p<1 else e.global_spinflip(P)
        assert actualP==e.adjoint(actualP) and e.matmul(actualP,actualP)==actualP and e.trace(actualP)==e.z(3)
        same=e.trace(e.matmul(actualP,out));assert same[1]==0 and same[0]<=top_upper
        arr=np.array([[complex(float(z[0]),float(z[1])) for z in row] for row in out])
        eig=np.linalg.eigvalsh(arr)[::-1]
        rows.append({"p":str(p),"t":str(t),"full_original_Pauli_matrix_matches":True,"output_positive_ldl_pivots":16,"lambda1_upper_ldl_pivots":16,"lambda2_upper_inertia":[15,1,0],"upper1":str(upper1),"upper2_and_3":str(upper2),"rigorous_top3_upper":str(top_upper),"product_reference_top3":str(reference),"certified_gap_lower":str(reference-top_upper),"actual_rank3_projector_trace":str(same[0]),"numerical_top3":[float(x) for x in eig[:3]]})
    print(json.dumps({"scope":"one exact near-product endpoint example; not a universal proof", "state":"(1500|0000>+|0011>+2i|0111>+2|1111>)/sqrt(2250009)","gauge_epsilon":"1/500","original_channel_checks":rows},indent=2,sort_keys=True))


if __name__=="__main__":main()
