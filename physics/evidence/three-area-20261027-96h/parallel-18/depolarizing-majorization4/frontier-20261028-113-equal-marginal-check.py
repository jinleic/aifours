#!/usr/bin/env python3
"""Exact equal-marginal GME saturation and full original-channel examples."""
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
e,b,d=s.e,s.b,s.d


def main():
    v=[F(0)]*16;v[0]=F(3)
    for i in (7,11,13,14):v[i]=F(1)
    rho=[[e.z(v[i]*v[j]/13) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    for i in range(4):
        assert e.local_marginal(rho,i)==[[e.z(F(10,13)),e.ZERO],[e.ZERO,e.z(F(3,13))]]
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
    tilde=e.global_spinflip(rho)
    assert e.trace(e.matmul(rho,tilde))==e.ZERO
    T=e.add_matrix(r.h1(rho),tilde)
    eig=d.verify_spectrum(T,{F(40,13):1,F(3):1,F(33,13):3,F(2):6,F(19,13):5})
    assert eig[1]==3 and sum(eig[:3])==F(112,13)<10
    frame=d.local_pauli_frame(rho)
    purity=e.trace(e.matmul(frame,frame));assert purity==e.z(F(3488,169))
    assert F(3488,169)<F(880,39)
    ident=e.zero(16);Q=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    for i in (0,1,2):Q[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(r.c.positive_definite_ldl(out))==16
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(3,20)),e.scale_matrix(out,-1))))==16
        inertia=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(17,200)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        upper=F(8,25);ref=F(32,81);assert upper<ref
        P=Q if p<F(1) else e.global_spinflip(Q)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        trace=e.trace(e.matmul(P,out));assert trace[1]==0 and trace[0]<upper
        rows.append({'p':str(p),'output_positive_LDL_pivots':16,'lambda1_upper_LDL_pivots':16,
                     'lambda2_upper_inertia':list(inertia),'top3_upper':str(upper),
                     'reference_top3':str(ref),'gap_lower':str(ref-upper),
                     'same_projector_trace':str(trace[0])})
    print(json.dumps({'scope':'one exact equal-marginal GME state; finite example not universal proof',
                      'cut_ranks':cuts,'one_qubit_minority':'3/13','bloch_radius':'7/13',
                      'spinflip_overlap':'0','T_spectrum':{'40/13':1,'3':1,'33/13':3,'2':6,'19/13':5},
                      'T_second_eigenvalue':'3','T_top3':str(sum(eig[:3])),
                      'frame_trace_square':str(purity[0]),'original_channels':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
