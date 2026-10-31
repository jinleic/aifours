#!/usr/bin/env python3
"""Exact finite checks for an entangled Pauli-frame saturation family."""

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("simple_frame", ROOT / "frontier-20261028-33-simple-frame-witness.py")
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)
d, b, e = sc.d, sc.b, sc.e


def main():
    parameters = sorted({F(n,d) for n in range(1,7) for d in range(1,7)})
    rows=[]
    for a in parameters:
        c=F(1)
        bb=F(4)/a
        norm=a*a+bb*bb+4*c*c
        v=[F(0)]*16
        v[0],v[15]=a,bb
        for k in (5,6,9,10): v[k]=c
        rho=[[e.z(v[i]*v[j]/norm) for j in range(16)] for i in range(16)]
        assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
        frame=d.local_pauli_frame(rho)
        spectrum=Counter()
        for value,mult in ((4*(a*a+bb*bb)/norm,1),(2*(a+bb)**2/norm,2),(2*a*a/norm,2),(2*bb*bb/norm,2),(8*c*c/norm,2),(F(0),7)):
            spectrum[value]+=mult
        eig=d.verify_spectrum(frame,spectrum)
        assert sum(eig[:3])==8
        vectors=[[F(0)]*16 for _ in range(3)]
        vectors[0][0],vectors[0][15]=a,-bb
        for i in (1,2):vectors[1][i]=a
        for i in (7,11):vectors[1][i]=2*c
        for i in (4,8):vectors[2][i]=a
        for i in (13,14):vectors[2][i]=2*c
        norms=[sum(x*x for x in vector) for vector in vectors]
        assert norms==[a*a+bb*bb,2*a*(a+bb),2*a*(a+bb)]
        P=e.zero(16)
        for vector,den in zip(vectors,norms):
            for i in range(16):
                for j in range(16):
                    P[i][j]=e.add(P[i][j],e.z(vector[i]*vector[j]/den))
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        assert e.trace(e.matmul(P,frame))==e.z(8)
        overlap=e.trace(e.matmul(P,rho))
        formula=(a*a-bb*bb)**2/(norm*(a*a+bb*bb))
        assert overlap==e.z(formula) and 0<=formula<1
        t1=e.zero(16)
        for site in range(4):t1=e.add_matrix(t1,e.one_erasure(rho,site))
        assert t1==e.add_matrix(rho,e.scale_matrix(frame,F(1,4)))
        assert e.trace(e.matmul(P,t1))==e.z(2+formula)
        if a in (F(1),F(2),F(4)):
            rows.append({"a":str(a),"b":str(bb),"c":"1","normalization_squared":str(norm),"frame_top3":"8","same_P_input_overlap":str(formula),"same_P_one_erasure_sum":str(2+formula)})
    print(json.dumps({"scope":"finite exact checks of a written all-parameter family; not global frame inequality or original-channel proof","distinct_positive_rational_parameters":len(parameters),"all_frame_spectra_rank_checked":True,"all_actual_projectors_checked":True,"selected_rows":rows},indent=2,sort_keys=True))


if __name__=="__main__":
    main()
