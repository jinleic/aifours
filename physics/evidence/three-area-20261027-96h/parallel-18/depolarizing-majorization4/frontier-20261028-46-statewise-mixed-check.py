#!/usr/bin/env python3
"""Exact mixed-state example for the state-dependent high-noise k3 theorem."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("dicke",ROOT/"frontier-20261028-26-dicke-pauli-counterexample.py")
d=importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
b,e=d.b,d.e


def main():
    product=e.zero(16);product[0][0]=e.ONE
    W=e.zero(16)
    for i in (1,2,4,8):
        for j in (1,2,4,8):W[i][j]=e.z(F(1,4))
    assert product==e.adjoint(product) and e.matmul(product,product)==product and e.trace(product)==e.ONE
    assert W==e.adjoint(W) and e.matmul(W,W)==W and e.trace(W)==e.ONE
    assert e.matmul(product,W)==e.zero(16)
    rho=e.scale_matrix(e.add_matrix(product,W),F(1,2))
    assert rho==e.adjoint(rho) and e.trace(rho)==e.ONE and e.matmul(rho,rho)==e.scale_matrix(rho,F(1,2))
    for site in range(4):
        local=e.local_marginal(W,site)
        assert local==[[e.z(F(3,4)),e.ZERO],[e.ZERO,e.z(F(1,4))]]
    assert 546 < 25**2  # epsilon_W=2/(sqrt(546)-5)>1/10 > t=1/20
    P=e.add_matrix(product,W)
    P[1][1]=e.add(P[1][1],e.z(F(1,2)))
    P[2][2]=e.add(P[2][2],e.z(F(1,2)))
    P[1][2]=e.add(P[1][2],e.z(-F(1,2)))
    P[2][1]=e.add(P[2][1],e.z(-F(1,2)))
    assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
    rows=[]
    for p in (F(19,20),F(21,20)):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        spectrum=d.original_spectrum(out)
        eig=d.verify_spectrum(out,spectrum)
        assert all(x>=0 for x in eig) and sum(eig)==1
        actualP=P if p==F(19,20) else e.global_spinflip(P)
        assert actualP==e.adjoint(actualP) and e.matmul(actualP,actualP)==actualP and e.trace(actualP)==e.z(3)
        assert e.trace(e.matmul(actualP,out))==e.z(sum(eig[:3]))
        t=abs(1-p);a,c=(1+t)/2,(1-t)/2
        reference=a**4+2*a**3*c
        D=F(2);lower=t*D/32
        assert lower==F(1,320) and reference-sum(eig[:3])>=lower
        rows.append({"p":str(p),"t":str(t),"original_spectrum":[[str(value),spectrum[value]] for value in sorted(spectrum,reverse=True)],"original_top3":str(sum(eig[:3])),"actual_rank3_projector_trace":str(sum(eig[:3])),"product_reference_top3":str(reference),"exact_gap":str(reference-sum(eig[:3])),"statewise_proved_lower_gap":str(lower)})
    print(json.dumps({"scope":"one exact mixed-state example, not a universal proof or original-channel violation", "state":"(W density + |0000><0000|)/2", "rank":2,"spectral_weights":["1/2","1/2"],"W_parameters":{"S":"1","L":"4","delta":"4","D_weighted":"2","epsilon":"2/(sqrt(546)-5)","epsilon_strictly_over":"1/10"},"full_Pauli_matrix_checks":2,"rows":rows},indent=2,sort_keys=True))


if __name__=="__main__":main()
