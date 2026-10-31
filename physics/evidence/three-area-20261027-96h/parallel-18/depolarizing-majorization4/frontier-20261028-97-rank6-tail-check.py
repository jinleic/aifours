#!/usr/bin/env python3
"""Exact rank-six spin-flip certificate and original-channel checks."""
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent

def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

end=load('end','frontier-20261028-66-noise-endpoint-check.py')
fr=load('frame','frontier-20261028-26-dicke-pauli-counterexample.py')
c,b,e=end.c,end.b,end.e


def h1(x):
    result=e.zero(16)
    for i in range(4):
        y=x
        for j in range(4):
            if i!=j:y=e.one_erasure(y,j)
        result=e.add_matrix(result,e.scale_matrix(y,8))
    return result


def h2(x):
    result=e.zero(16)
    for i,j in itertools.combinations(range(4),2):
        result=e.add_matrix(result,e.scale_matrix(e.one_erasure(e.one_erasure(x,i),j),4))
    return result


def main():
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    Q=e.zero(16)
    Q[0][0]=e.z(F(576,625));Q[15][15]=e.z(F(49,625))
    Q[0][15]=Q[15][0]=e.z(F(168,625))
    for i in (1,2,3,4,8):Q[i][i]=e.ONE
    assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(6)
    HQ=h1(Q);spinQ=e.global_spinflip(Q)
    residual=e.add_matrix(e.add_matrix(HQ,spinQ),e.scale_matrix(ident,-7))
    assert len(c.positive_definite_ldl(residual))==16
    mz=[]
    for site in range(4):
        mask=1<<(3-site)
        mz.append(sum((Q[i][i][0] * (-1 if i&mask else 1) for i in range(16)),F(0)))
    S=sum(mz);branch=(S-10)/2;q=Q[0][0][0]
    assert S>10 and S<=12 and q>=(1+branch)/2

    vec=[F(0)]*16
    for i,x in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,1)):vec[i]=F(x,3)
    rho=[[e.z(vec[i]*vec[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    H1,H2=h1(rho),h2(rho)
    frame=fr.local_pauli_frame(rho);tilde=e.global_spinflip(rho)
    lhs=e.add_matrix(e.add_matrix(H2,e.scale_matrix(H1,-1)),ident)
    rhs=e.add_matrix(e.add_matrix(rho,tilde),e.scale_matrix(frame,F(1,2)))
    assert lhs==rhs
    assert e.trace(e.matmul(Q,e.add_matrix(H1,tilde)))[0]>=7
    assert e.trace(e.matmul(Q,H2))[0]>=1
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        if p==F(2,3):
            lower=e.add_matrix(e.add_matrix(e.scale_matrix(ident,F(1,81)),e.scale_matrix(H1,F(1,81))),e.scale_matrix(H2,F(1,81)))
            remainder=e.add_matrix(out,e.scale_matrix(lower,-1))
            assert remainder==e.scale_matrix(e.add_matrix(e.scale_matrix(rho,3),e.scale_matrix(frame,F(1,2))),F(1,81))
        current=Q if p<1 else e.global_spinflip(Q)
        assert current==e.adjoint(current) and e.matmul(current,current)==current and e.trace(current)==e.z(6)
        tr=e.trace(e.matmul(current,out));assert tr[1]==0 and tr[0]>F(13,81)
        arr=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
        eig=np.linalg.eigvalsh(arr)
        rows.append({'p':str(p),'same_rank6_trace':str(tr[0]),'product_bottom6':'13/81',
                     'numerical_bottom6':eig[:6].tolist(),'numerical_top10':float(sum(eig[6:]))})
    print(json.dumps({'scope':'one exact non-diagonal rank-six projector and one physical state, not a universal proof',
                     'rank6_magnitudes':list(map(str,mz)),'S':str(S),'c':str(branch),'q':str(q),
                     'dual_certificate_positive_ldl_pivots':16,'spinflip_H2_identity_exact':True,
                     'same_Q_H1_plus_tilde':str(e.trace(e.matmul(Q,e.add_matrix(H1,tilde)))[0]),
                     'same_Q_H2':str(e.trace(e.matmul(Q,H2))[0]),'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
