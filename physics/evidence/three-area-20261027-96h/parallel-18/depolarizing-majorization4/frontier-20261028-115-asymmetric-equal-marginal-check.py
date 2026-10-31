#!/usr/bin/env python3
"""Exact GME application beyond several prior named input families."""
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


def pair_density(rho,active):
    other=tuple(i for i in range(4) if i not in active)
    out=e.zero(4)
    for row in range(4):
        for col in range(4):
            for rest in range(4):
                a=[0]*4;bb=[0]*4
                for j,i in enumerate(active):a[i]=(row>>(1-j))&1;bb[i]=(col>>(1-j))&1
                for j,i in enumerate(other):a[i]=bb[i]=(rest>>(1-j))&1
                ia=sum(a[i]<<(3-i) for i in range(4));ib=sum(bb[i]<<(3-i) for i in range(4))
                out[row][col]=e.add(out[row][col],rho[ia][ib])
    return out


def main():
    v=[F(0)]*16
    for i in (1,2,12):v[i]=F(1)
    rho=[[e.z(v[i]*v[j]/3) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    for i in range(4):assert e.local_marginal(rho,i)==[[e.z(F(2,3)),e.ZERO],[e.ZERO,e.z(F(1,3))]]
    cuts=[]
    for size in (1,2):
        for active in itertools.combinations(range(4),size):
            if size==2 and 0 not in active:continue
            other=tuple(i for i in range(4) if i not in active)
            mat=[[F(0) for _ in range(2**len(other))] for _ in range(2**len(active))]
            for idx in range(16):
                bits=[(idx>>(3-i))&1 for i in range(4)]
                row=sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col=sum(bits[i]*2**(len(other)-1-j) for j,i in enumerate(other))
                mat[row][col]=v[idx]
            rank=s.rectangular_rank(mat);assert rank>=2
            cuts.append({'party_indices_zero_based':list(active),'schmidt_rank':rank})
    a=pair_density(rho,(0,1));bb=pair_density(rho,(0,2))
    assert a==[[e.z(F(2,3)),e.ZERO,e.ZERO,e.ZERO],[e.ZERO,e.ZERO,e.ZERO,e.ZERO],
               [e.ZERO,e.ZERO,e.ZERO,e.ZERO],[e.ZERO,e.ZERO,e.ZERO,e.z(F(1,3))]]
    assert bb==[[e.z(F(1,3)),e.ZERO,e.ZERO,e.ZERO],[e.ZERO,e.z(F(1,3)),e.ZERO,e.ZERO],
                [e.ZERO,e.ZERO,e.z(F(1,3)),e.ZERO],[e.ZERO,e.ZERO,e.ZERO,e.ZERO]]
    assert e.trace(e.matmul(a,a))==e.z(F(5,9)) and e.trace(e.matmul(bb,bb))==e.z(F(1,3))
    assert e.trace(e.matmul(rho,e.global_spinflip(rho)))==e.ZERO
    frame=d.local_pauli_frame(rho)
    assert e.trace(e.matmul(frame,frame))==e.z(F(160,9)) and F(160,9)<F(880,39)
    ident=e.zero(16);Q=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    for i in (0,1,2):Q[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(r.c.positive_definite_ldl(out))==16
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(3,25)),e.scale_matrix(out,-1))))==16
        inertia=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(9,100)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        upper=F(3,10);ref=F(32,81);assert upper<ref
        P=Q if p<F(1) else e.global_spinflip(Q)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        trace=e.trace(e.matmul(P,out));assert trace[1]==0 and trace[0]<upper
        rows.append({'p':str(p),'lambda1_upper_LDL_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'top3_upper':str(upper),'reference_k3':str(ref),'gap_lower':str(ref-upper),
                     'same_projector_trace':str(trace[0])})
    print(json.dumps({'scope':'one exact asymmetric GME input; all-p result conditional on unreviewed 114',
                      'state':'(|0001>+|0010>+|1100>)/sqrt(3)','radius':'1/3','C':'0',
                      'frame_square':'160/9','cut_ranks':cuts,'pair12_purity':'5/9',
                      'pair13_purity':'1/3','product_overlap_upper':'2/3','original_channels':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
