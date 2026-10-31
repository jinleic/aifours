#!/usr/bin/env python3
"""Exact Loewner lower-tail check for one genuine four-qubit example."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('endpoint',ROOT/'frontier-20261028-66-noise-endpoint-check.py')
d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
c,b,e=d.c,d.b,d.e


def main():
    v=[F(0)]*16
    for i,x in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,1)):v[i]=F(x,3)
    rho=[[e.z(v[i]*v[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    h=e.zero(16)
    for i in range(4):
        a=rho
        for j in range(4):
            if i!=j:a=e.one_erasure(a,j)
        h=e.add_matrix(h,e.scale_matrix(a,8))
    assert all(h[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
    vals=sorted(h[i][i][0] for i in range(16))
    assert vals==[F(4,3)]+[F(5,3)]*4+[F(2)]*6+[F(7,3)]*4+[F(8,3)]
    assert sum(vals[:5])==8
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    qout=e.channel(rho,F(2,3));assert qout==b.direct_pauli(rho,F(2,3))
    pout=e.channel(rho,F(4,3));assert pout==b.direct_pauli(rho,F(4,3))
    assert pout==e.global_spinflip(qout)
    rows=[]
    for p,out,hs in ((F(2,3),qout,h),(F(4,3),pout,e.global_spinflip(h))):
        rem=e.add_matrix(e.add_matrix(out,e.scale_matrix(ident,-F(1,81))),e.scale_matrix(hs,-F(1,81)))
        assert len(c.positive_definite_ldl(out))==16
        assert len(c.positive_definite_ldl(rem))==16
        # Same explicit rank-five complement; the scalar bound itself is universal in Q.
        Q=e.zero(16)
        for i in (0,1,2,4,8):Q[i][i]=e.ONE
        assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(5)
        tr=e.trace(e.matmul(Q,out));assert tr[1]==0 and tr[0]>F(13,81)
        matrix=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
        eig=np.linalg.eigvalsh(matrix)
        rows.append({'p':str(p),'exact_output_positive_ldl_pivots':16,'exact_remainder_positive_ldl_pivots':16,
                     'same_rank5_trace':str(tr[0]),'bottom5_lower':str(F(13,81)),
                     'product_bottom5':str(F(1,9)),'top11_upper':str(F(68,81)),
                     'reference_top11':str(F(8,9)),'numerical_bottom5':eig[:5].tolist()})
    print(json.dumps({'scope':'exact one-state Loewner check at two physical parameters, not a universal proof',
                     'state':'(2|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/3',
                     'exact_marginal_sum_eigenvalues':[str(x) for x in vals],
                     'exact_smallest5_marginal_sum':'8','rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
