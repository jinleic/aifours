#!/usr/bin/env python3
"""Exact finite checks of the common-projector first-order k3 certificate."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("purity_check",ROOT/"frontier-20261028-40-purity-certificate-check.py")
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
w,b,e=a.w,a.b,a.e


def nonnegative_sqrt_sum_bound(Z,X,Y):
    assert X>=0 and Y>=0
    if Z<=0 or Z*Z<=X+Y:return True
    return (Z*Z-X-Y)**2<=4*X*Y


def main():
    paulis=list(a.pauli_strings())
    projectors=[a.projector(0,15,3,12),a.projector(3,12,5,10)]
    Pstar=e.zero(16)
    for i in (0,1,2):Pstar[i][i]=e.ONE
    projectors.append(Pstar)
    B=[]
    for P in projectors:
        values=[F(0)]*5
        for weight,op in paulis:
            value=e.trace(e.matmul(P,op))
            assert value[1]==0
            values[weight]+=value[0]**2
        assert values[0]==9 and sum(values)==48 and values[1]<=20
        B.append(values)
    assert B[2][1]==20
    parameters=(F(0),F(1,2),F(4,5),F(1),F(6,5),F(4,3))
    checks=0;states=0;stricts=0
    for name,rho in a.states():
        if name=="complex_sparse":continue
        assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
        raw=[b.diagonal_radii(rho)[i] for i in range(4)]
        radii=sorted(raw);S=sum(x*x for x in radii);L=radii[0]+radii[1]+3*radii[2]+3*radii[3]
        if name=="product":assert L==8
        else:assert L<8
        Avec=[F(0)]*5
        rho_coeff=[]
        for weight,op in paulis:
            x=e.trace(e.matmul(rho,op));assert x[1]==0
            rho_coeff.append((weight,x[0]));Avec[weight]+=x[0]**2
        assert Avec[1]==S and sum(Avec)==16 and sum(Avec[2:])==15-S
        states+=1
        for P,Bvec in zip(projectors,B):
            C1=F(0)
            for (weight,op),(weight2,x) in zip(paulis,rho_coeff):
                assert weight==weight2
                if weight==1:
                    y=e.trace(e.matmul(P,op));assert y[1]==0
                    C1+=x*y[0]
            assert C1<=L and C1*C1<=S*Bvec[1]
            for p in parameters:
                out=e.channel(rho,p);value=e.trace(e.matmul(P,out));assert value[1]==0
                t=abs(1-p);u=t*t*S;v=sum(t**(2*k)*Avec[k] for k in (2,3,4))
                Z=16*value[0]-3-t*L
                assert Z<=0 or Z*Z<=t**4*39*(15-S)
                if S==0:
                    boundZ=16*value[0]-3
                    assert boundZ<=0 or boundZ*boundZ<=39*v
                elif u+v==0:
                    assert 16*value[0]<=3
                else:
                    cap=L*L/S;assert cap<=20
                    star=39*u/(u+v)
                    if star<=cap:
                        boundZ=16*value[0]-3
                        assert boundZ<=0 or boundZ*boundZ<=39*(u+v)
                    else:
                        boundZ=16*value[0]-3
                        assert nonnegative_sqrt_sum_bound(boundZ,u*cap,v*(39-cap))
                aa,bb=(1+t)/2,(1-t)/2
                reference=aa**4+2*aa**3*bb
                if t and L<8:
                    condition=(8-L)/t+5
                    if condition>0 and condition**2>39*(15-S):
                        assert value[0]<reference
                        stricts+=1
                checks+=1
    W=dict(a.states())["W"]
    Ptop=e.zero(16);Ptop[0][0]=e.ONE;Ptop=e.add_matrix(Ptop,W)
    for i in range(16):
        for j in range(16):
            if i.bit_count()==j.bit_count()==2:Ptop[i][j]=e.z(F(1,6))
    assert Ptop==e.adjoint(Ptop) and e.matmul(Ptop,Ptop)==Ptop and e.trace(Ptop)==e.z(3)
    expected={F(54,625):2,F(45,625):4,F(39,625):3,F(36,625):2,F(34,625):1,F(30,625):3,F(24,625):1}
    for p in (F(4,5),F(6,5)):
        out=e.channel(W,p);assert out==b.direct_pauli(W,p)
        for value,multiplicity in expected.items():
            shifted=[[out[i][j][0]-(value if i==j else 0) for j in range(16)] for i in range(16)]
            assert all(out[i][j][1]==0 for i in range(16) for j in range(16))
            assert 16-w.rank_fraction(shifted)==multiplicity
        P=Ptop if p==F(4,5) else e.global_spinflip(Ptop)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        assert e.trace(e.matmul(P,out))==e.z(F(153,625))
    assert 546<625
    print(json.dumps({"scope":"finite exact common-projector checks; not all-state proof or original-channel violation", "states":states,"projectors":len(projectors),"parameters":len(parameters),"state_projector_parameter_checks":checks,"strict_condition_cases":stricts,"sharp_B1_reference_projector":str(B[2][1]),"W_p_four_fifths_and_six_fifths":{"exact_output_spectrum_over_625":[[54,2],[45,4],[39,3],[36,2],[34,1],[30,3],[24,1]],"actual_top3":"153/625","actual_top_projector_trace":"153/625","reference_top3":"189/625","exact_gap":"36/625","state_dependent_gap_lower":"(25-sqrt(546))/400","full_Pauli_mixture_exact_checks":2}},indent=2,sort_keys=True))


if __name__=="__main__":main()
