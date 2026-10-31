#!/usr/bin/env python3
"""Exact finite checks of four-qubit Pauli purity invariants and k3 bound."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("w_checker", ROOT / "frontier-20261028-18-anisotropic-w-check.py")
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)
b,e = w.b,w.e


def outer(v,denom=1):
    return [[e.scale(e.mul(v[i],e.conj(v[j])),F(1,denom)) for j in range(16)] for i in range(16)]


def projector(first,second,third,fourth):
    out=e.zero(16)
    out[first][first]=out[second][second]=e.ONE
    out[third][third]=out[fourth][fourth]=e.z(F(1,2))
    out[third][fourth]=e.z(0,-F(1,2))
    out[fourth][third]=e.z(0,F(1,2))
    assert out==e.adjoint(out) and e.matmul(out,out)==out and e.trace(out)==e.z(3)
    return out


def pauli_strings():
    I=[[e.ONE,e.ZERO],[e.ZERO,e.ONE]]
    X=[[e.ZERO,e.ONE],[e.ONE,e.ZERO]]
    Y=[[e.ZERO,e.z(0,-1)],[e.IMAG,e.ZERO]]
    Z=[[e.ONE,e.ZERO],[e.ZERO,e.z(-1)]]
    for labels in itertools.product(range(4),repeat=4):
        matrix=[[e.ONE]]
        for label in labels: matrix=b.kron(matrix,(I,X,Y,Z)[label])
        yield sum(label!=0 for label in labels),matrix


def states():
    ans=[]
    v=[e.ZERO]*16;v[0]=e.ONE;ans.append(("product",outer(v)))
    v=[e.ZERO]*16
    for i in (1,2,4,8):v[i]=e.z(F(1,2))
    ans.append(("W",outer(v)))
    ghz=e.zero(16)
    for i in (0,15):
        for j in (0,15):ghz[i][j]=e.z(F(1,2))
    ans.append(("equal_GHZ",ghz))
    v=[e.ZERO]*16;v[0]=e.z(F(3,5));v[15]=e.z(F(4,5));ans.append(("unequal_GHZ",outer(v)))
    v=[e.ZERO]*16;v[0]=e.z(F(3,5));v[15]=e.z(0,F(4,5));ans.append(("complex_GHZ",outer(v)))
    dicke=e.zero(16)
    for i in range(16):
        for j in range(16):
            if i.bit_count()==j.bit_count()==2:dicke[i][j]=e.z(F(1,6))
    ans.append(("Dicke2",dicke))
    support=(2,3,5,8,9,10,12,13,14,15)
    phases=((0,-1),(0,-1),(0,-1),(0,-1),(0,1),(-1,0),(-1,0),(1,0),(0,1),(0,1))
    v=[e.ZERO]*16
    for i,(a,c) in zip(support,phases):v[i]=e.z(a,c)
    ans.append(("complex_sparse",outer(v,10)))
    v=[e.ZERO]*16
    for i,value in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,2)):v[i]=e.z(value)
    ans.append(("balanced_frame_family",outer(v,12)))
    v=[e.ZERO]*16
    for i,value in ((0,4),(5,1),(6,1),(9,1),(10,1),(15,1)):v[i]=e.z(value)
    ans.append(("unbalanced_frame_family",outer(v,21)))
    return ans


def main():
    paulis=list(pauli_strings())
    assert len(paulis)==256
    P0=projector(0,15,3,12);P1=projector(3,12,5,10)
    params=(F(0),F(1,2),F(2,3),F(1),F(4,3))
    rows=[];channel_checks=pair_checks=tight_checks=0
    W_rho=None
    for name,rho in states():
        assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
        local_purities=[]
        for site in range(4):
            local=e.local_marginal(rho,site)
            purity=e.trace(e.matmul(local,local))
            assert purity[1]==0
            erased=e.one_erasure(rho,site)
            complement_purity=e.trace(e.matmul(erased,erased))
            assert complement_purity[1]==0 and purity[0]==2*complement_purity[0]
            local_purities.append(purity[0])
        S=sum(2*x-1 for x in local_purities)
        c2=e.trace(e.matmul(rho,e.global_spinflip(rho)))
        assert c2[1]==0 and 4*c2[0]<=4-S
        C=c2[0]
        A=[F(0)]*5
        for weight,op in paulis:
            coeff=e.trace(e.matmul(rho,op))
            assert coeff[1]==0
            A[weight]+=coeff[0]**2
        expected=[F(1),S,2+S+4*C,8-8*C-S,5-S+4*C]
        assert A==expected and sum(A)==16
        rows.append({"state":name,"S":str(S),"C":str(C),"pauli_weight_squares":[str(x) for x in A]})
        if name=="W":W_rho=rho
        for p in params:
            out=e.channel(rho,p)
            if (name,p) in (("W",F(1,2)),("complex_sparse",F(4,3))):
                assert out==b.direct_pauli(rho,p)
            t=abs(1-p);z=t*t
            Q=sum(t**(2*k)*A[k] for k in range(1,5))
            purity=e.trace(e.matmul(out,out))
            assert purity==e.z((1+Q)/16)
            refpur=(1+z)**4/16
            delta=16*(refpur-purity[0])
            factor=z*(1-z)*((4-S)*(1+z)**2-4*C*z*(1-z))
            lower=z*(1-z)*(4-S)*(1+z+2*z*z)
            assert delta==factor and delta>=lower>=0
            if name in ("equal_GHZ","unequal_GHZ","complex_GHZ"):
                assert delta==lower
                tight_checks+=1
            for P in (P0,P1):
                value=e.trace(e.matmul(P,out))
                assert value[1]==0
                lhs=16*value[0]-3
                assert lhs<=0 or lhs*lhs<=39*Q
                pair_checks+=1
            channel_checks+=1
    assert W_rho is not None
    p=F(1,2);out=e.channel(W_rho,p)
    expected_eigs={F(54,256):1,F(27,256):2,F(18,256):3,F(15,256):3,F(10,256):1,F(9,256):2,F(6,256):3,F(3,256):1}
    for value,mult in expected_eigs.items():
        shifted=[[out[i][j][0]-(value if i==j else 0) for j in range(16)] for i in range(16)]
        assert 16-w.rank_fraction(shifted)==mult
    assert sum(expected_eigs.values())==16
    Ptop=e.zero(16);Ptop[0][0]=e.ONE;Ptop=e.add_matrix(Ptop,W_rho)
    indices=[i for i in range(16) if i.bit_count()==2]
    for i in indices:
        for j in indices:Ptop[i][j]=e.z(F(1,6))
    assert Ptop==e.adjoint(Ptop) and e.matmul(Ptop,Ptop)==Ptop and e.trace(Ptop)==e.z(3)
    assert e.trace(e.matmul(Ptop,out))==e.z(F(27,64))
    assert 12*12*39 < 87*87
    print(json.dumps({"scope":"exact finite checks; not an all-state proof or original-channel counterexample","states":len(rows),"pauli_string_expectations":len(rows)*len(paulis),"state_parameter_checks":channel_checks,"actual_projector_trace_checks":pair_checks,"generalized_GHZ_tight_parameter_checks":tight_checks,"state_invariants":rows,"W_p_half":{"Q":"9/16","full_spectrum_over_256":[[54,1],[27,2],[18,3],[15,3],[10,1],[9,2],[6,3],[3,1]],"original_top3":"27/64","same_top_projector_trace":"27/64","reference_top3":"135/256","exact_spectral_gap":"27/256","HS_certified_gap":"(87-12 sqrt(39))/256"}},indent=2,sort_keys=True))


if __name__=="__main__":
    main()
