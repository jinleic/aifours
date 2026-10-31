#!/usr/bin/env python3
"""Exact checks of the rank-ten/eleven extensions of the spinflip certificate."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent
sp=importlib.util.spec_from_file_location('prev',ROOT/'frontier-20261028-97-rank6-tail-check.py')
a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
e,c,b=a.e,a.c,a.b


def main():
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    vec=[F(0)]*16
    for i,x in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,1)):vec[i]=F(x,3)
    rho=[[e.z(vec[i]*vec[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    H1,H2=a.h1(rho),a.h2(rho)
    rows=[]
    for rank in (10,11):
        Q=e.zero(16)
        Q[0][0],Q[15][15]=e.z(F(576,625)),e.z(F(49,625))
        Q[0][15]=Q[15][0]=e.z(F(168,625))
        for i in (1,2,4,8):Q[i][i]=e.ONE
        for i in ([3,5,6,9,10] if rank==10 else [3,5,6,9,10,12]):Q[i][i]=e.ONE
        assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(rank)
        HQ=a.h1(Q);spinQ=e.global_spinflip(Q)
        cert=e.add_matrix(e.add_matrix(HQ,spinQ),e.scale_matrix(ident,-(2*rank-5)))
        assert len(c.positive_definite_ldl(cert))==16
        mz=[]
        for site in range(4):
            mask=1<<(3-site)
            mz.append(sum((Q[i][i][0]*(-1 if i&mask else 1) for i in range(16)),F(0)))
        S=sum(mz);cc=(S-10)/2;q=Q[0][0][0]
        assert S>10 and S<=12 and q>=(1+cc)/2
        tr1=e.trace(e.matmul(Q,H1));tr2=e.trace(e.matmul(Q,H2))
        assert tr1[1]==0 and tr1[0]>=2*rank-6
        assert tr2[1]==0 and tr2[0]>=rank-5
        outputs=[]
        for p in (F(2,3),F(4,3)):
            out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
            cur=Q if p<1 else e.global_spinflip(Q)
            assert cur==e.adjoint(cur) and e.matmul(cur,cur)==cur and e.trace(cur)==e.z(rank)
            trace=e.trace(e.matmul(cur,out));bound=F(4*rank-11,81)
            assert trace[1]==0 and trace[0]>bound
            arr=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
            values=np.linalg.eigvalsh(arr)
            outputs.append({'p':str(p),'same_rank_trace':str(trace[0]),'reference_bottom':str(bound),
                            'numerical_bottom_sum':float(sum(values[:rank]))})
        rows.append({'rank':rank,'original_k':16-rank,'local_magnitudes':list(map(str,mz)),
                     'S':str(S),'c':str(cc),'q':str(q),'dual_positive_ldl_pivots':16,
                     'same_Q_H1':str(tr1[0]),'same_Q_H2':str(tr2[0]),'outputs':outputs})
    print(json.dumps({'scope':'exact two non-diagonal projectors and one physical state, not universal proof',
                      'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
