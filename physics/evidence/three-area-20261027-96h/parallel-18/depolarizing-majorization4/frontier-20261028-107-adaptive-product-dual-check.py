#!/usr/bin/env python3
"""Exact adaptive-product rank-three Q defeating a tempting frame inequality."""
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent

def load(name,filename):
    sp=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
    return mod

s=load('simple','frontier-20261028-33-simple-frame-witness.py')
r=load('rank6','frontier-20261028-97-rank6-tail-check.py')
d,b,e=s.d,s.b,s.e


def main():
    v=[F(0)]*16
    for i,x in ((1,1),(8,4),(12,-2),(14,2)):v[i]=F(x,5)
    rho=[[e.z(v[i]*v[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    cuts=[]
    for size in (1,2):
        for active in itertools.combinations(range(4),size):
            if size==2 and 0 not in active:continue
            other=tuple(i for i in range(4) if i not in active)
            matrix=[[F(0) for _ in range(2**len(other))] for _ in range(2**len(active))]
            for idx in range(16):
                bits=[(idx>>(3-i))&1 for i in range(4)]
                row=sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col=sum(bits[i]*2**(len(other)-1-j) for j,i in enumerate(other))
                matrix[row][col]=v[idx]
            rank=s.rectangular_rank(matrix);assert rank>=2
            cuts.append({'party_indices_zero_based':list(active),'schmidt_rank':rank})
    vecs=[[F(0)]*16 for _ in range(3)]
    vecs[0][0]=1
    for i in (8,12):vecs[1][i]=1
    for i,x in ((8,1),(10,1),(12,-1),(14,-1)):vecs[2][i]=x
    Q=e.zero(16)
    for vec,norm in zip(vecs,(1,2,4)):
        Q=e.add_matrix(Q,[[e.z(vec[i]*vec[j]/norm) for j in range(16)] for i in range(16)])
    assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(3)
    assert Q[8][12]==e.z(F(1,4))
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    fq=d.local_pauli_frame(Q)
    overlap=e.trace(e.matmul(rho,Q));frame=e.trace(e.matmul(rho,fq))
    bad=e.add_matrix(fq,e.scale_matrix(e.add_matrix(ident,Q),-4))
    violation=e.trace(e.matmul(rho,bad))
    assert overlap==e.z(F(6,25)) and frame==e.z(F(138,25)) and violation==e.z(F(14,25))
    results=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(Q,p);assert out==b.direct_pauli(Q,p)
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(3,8)),e.scale_matrix(out,-1))))==16
        actual=e.trace(e.matmul(rho,out));assert actual[1]==0 and actual[0]<F(3,8)<F(32,81)
        results.append({'p':str(p),'actual_same_Q_input_trace':str(actual[0]),
                        'lambda_max_strict_upper':'3/8','ldl_pivots':16,'reference_k3':'32/81',
                        'certified_global_Q_gap_lower':str(F(32,81)-F(3,8))})
    print(json.dumps({'scope':'exact actual rank-three adaptive-product projector and GME input; not an original counterexample',
                     'rank':3,'schmidt_cut_ranks':cuts,'Q_8_12':str(Q[8][12][0]),
                     'input_Q_overlap':str(overlap[0]),'input_FQ_expectation':str(frame[0]),
                     'false_4I_plus_4Q_witness_excess':str(violation[0]),'original_channels':results},
                     indent=2,sort_keys=True))


if __name__=='__main__':main()
