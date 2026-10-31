#!/usr/bin/env python3
"""Exact physical rank-three obstruction to a product-inspired dual bound."""
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent

def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

s=load('simple','frontier-20261028-33-simple-frame-witness.py')
r=load('rank6','frontier-20261028-97-rank6-tail-check.py')
d,b,e=s.d,s.b,s.e


def main():
    v=[F(0)]*16
    for i,x in ((0,2),(5,1),(6,1),(9,1),(10,1),(15,2)):v[i]=F(x)
    rho=[[e.z(v[i]*v[j]/12) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    cut_ranks=[]
    for size in (1,2):
        for active in itertools.combinations(range(4),size):
            if size==2 and 0 not in active:
                continue
            other=tuple(i for i in range(4) if i not in active)
            matrix=[[F(0) for _ in range(2**len(other))] for _ in range(2**len(active))]
            for index in range(16):
                bits=[(index>>(3-i))&1 for i in range(4)]
                row=sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col=sum(bits[i]*2**(len(other)-1-j) for j,i in enumerate(other))
                matrix[row][col]=v[index]
            rank=s.rectangular_rank(matrix)
            assert rank>=2
            cut_ranks.append({'parties_zero_based':list(active),'rank':rank})
    vectors=[[F(0)]*16 for _ in range(3)]
    vectors[0][0],vectors[0][15]=1,-1
    for i in (1,2,7,11):vectors[1][i]=1
    for i in (4,8,13,14):vectors[2][i]=1
    Q=e.zero(16)
    for vector,norm in zip(vectors,(2,4,4)):
        Q=e.add_matrix(Q,[[e.z(vector[i]*vector[j]/norm) for j in range(16)] for i in range(16)])
    assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(3)
    assert e.matmul(Q,rho)==e.zero(16)
    zeta=[F(0)]*16
    for i,x in ((5,1),(6,-1),(9,-1),(10,1)):zeta[i]=F(x,2)
    Z=[[e.z(zeta[i]*zeta[j]) for j in range(16)] for i in range(16)]
    assert e.matmul(Q,Z)==e.zero(16) and e.matmul(rho,Z)==e.zero(16)
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    fq=d.local_pauli_frame(Q)
    assert fq==e.add_matrix(e.add_matrix(e.scale_matrix(ident,2),e.scale_matrix(rho,6)),e.scale_matrix(Z,-2))
    assert e.matmul(fq,rho)==e.scale_matrix(rho,8)
    d.verify_spectrum(fq,{F(8):1,F(2):14,F(0):1})
    bad=e.add_matrix(fq,e.scale_matrix(e.add_matrix(ident,Q),-4))
    assert e.matmul(bad,rho)==e.scale_matrix(rho,4)
    assert e.trace(e.matmul(rho,bad))==e.z(4)
    T1=e.zero(16);T2=e.zero(16)
    for i in range(4):T1=e.add_matrix(T1,e.one_erasure(Q,i))
    for i,j in itertools.combinations(range(4),2):
        T2=e.add_matrix(T2,e.one_erasure(e.one_erasure(Q,i),j))
    assert T1==e.add_matrix(Q,e.scale_matrix(fq,F(1,4)))
    lhs=e.scale_matrix(T2,4)
    rhs=e.add_matrix(e.add_matrix(e.add_matrix(r.h1(Q),Q),e.global_spinflip(Q)),e.scale_matrix(fq,F(1,2)))
    rhs=e.add_matrix(rhs,e.scale_matrix(ident,-3))
    assert lhs==rhs
    d.verify_spectrum(T1,{F(2):1,F(3,2):3,F(1,2):11,F(0):1})
    d.verify_spectrum(T2,{F(7,4):1,F(3,2):3,F(1):11,F(3,4):1})
    d.verify_spectrum(e.add_matrix(r.h1(Q),e.global_spinflip(Q)),{F(7):3,F(6):13})
    d.verify_spectrum(e.add_matrix(fq,e.scale_matrix(Q,2)),{F(8):1,F(4):3,F(2):11,F(0):1})
    Q0=e.zero(16)
    for i in (0,1,2):Q0[i][i]=e.ONE
    refbad=e.add_matrix(d.local_pauli_frame(Q0),e.scale_matrix(e.add_matrix(ident,Q0),-4))
    assert all(refbad[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
    assert all(refbad[i][i][1]==0 and refbad[i][i][0]<=0 for i in range(16))
    outputs=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(Q,p);assert out==b.direct_pauli(Q,p)
        d.verify_spectrum(out,{F(20,81):1,F(19,81):3,F(14,81):11,F(4,27):1})
        assert e.matmul(out,rho)==e.scale_matrix(rho,F(20,81))
        outputs.append({'p':str(p),'dual_operator_max':'20/81','product_reference_k3':'32/81',
                        'witness_trace':'20/81','dual_bound_gap':'4/27'})
    print(json.dumps({'scope':'exact actual rank-three projector and physical input; not global original counterexample',
                     'Q_rank':3,'cut_ranks':cut_ranks,'input_Q_overlap':'0','FQ_spectrum':{'8':1,'2':14,'0':1},
                     'FQ_on_input':'8','false_bound_4I_plus_4Q_violation':'4',
                     'all_alpha_positive_bound_8I_minus_alpha_I_minus_Q':'violated by alpha',
                     'reference_Q_satisfies_false_stronger_bound':True,
                     'T1_max':'2','T2_max':'7/4','H1_plus_spinQ_max':'7',
                     'FQ_plus_2Q_max':'8','original_channels':outputs},indent=2,sort_keys=True))


if __name__=='__main__':main()
