#!/usr/bin/env python3
"""Exact Pauli-block and physical checks for vacuum-plus-three-excitation family."""
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


def make(a,g):
    vec=[e.ZERO]*16;vec[0]=e.z(a)
    for i,z in enumerate(g):vec[15^(1<<(3-i))]=z
    norm=F(a*a)+sum((z[0]*z[0]+z[1]*z[1] for z in g),F(0))
    return [[e.scale(e.mul(vec[i],e.conj(vec[j])),1/norm) for j in range(16)] for i in range(16)],norm


def main():
    cases=[(5,[e.z(2),e.z(1),e.z(1),e.z(1)]),
           (1,[e.z(4),e.z(1),e.z(1),e.z(1)]),
           (3,[e.z(1,1),e.z(2),e.z(0,-1),e.z(1)]),
           (0,[e.z(4),e.z(1),e.z(1),e.z(1)]),
           (1,[e.ZERO,e.ZERO,e.ZERO,e.ZERO])]
    rows=[]
    for aa,g in cases:
        rho,N=make(aa,g);assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
        A=F(aa*aa)/N;weights=[(z[0]*z[0]+z[1]*z[1])/N for z in g];B=sum(weights)
        frame=d.local_pauli_frame(rho)
        i0=[0]+[15^(1<<(3-i)) for i in range(4)]
        i1=[1<<(3-i) for i in range(4)]+[15]
        pairs=list(itertools.combinations(range(4),2))
        i2=[15^(1<<(3-i))^(1<<(3-j)) for i,j in pairs]
        groups=[i0,i1,i2]
        for x in range(3):
            for y in range(3):
                if x!=y:assert all(frame[i][j]==e.ZERO for i in groups[x] for j in groups[y])
        F0=e.zero(5);F1=e.zero(5)
        F0[0][0]=e.z(4*A);F1[4][4]=e.z(2*B)
        for i in range(4):
            F0[i+1][i+1]=e.z(4*weights[i]);F1[i][i]=e.z(2*A)
            F0[0][i+1]=e.scale(e.conj(g[i]),F(-2*aa,N));F0[i+1][0]=e.conj(F0[0][i+1])
            F1[i][4]=e.scale(e.conj(g[i]),F(2*aa,N));F1[4][i]=e.conj(F1[i][4])
        assert all(frame[i0[i]][i0[j]]==F0[i][j] for i in range(5) for j in range(5))
        assert all(frame[i1[i]][i1[j]]==F1[i][j] for i in range(5) for j in range(5))
        V=[[e.ZERO]*4 for _ in range(6)]
        for k,(i,j) in enumerate(pairs):V[k][i]=g[j];V[k][j]=g[i]
        F2=e.zero(6)
        for i in range(6):
            for j in range(6):
                for k in range(4):
                    F2[i][j]=e.add(F2[i][j],e.scale(e.mul(V[i][k],e.conj(V[j][k])),F(2,N)))
        assert all(frame[i2[i]][i2[j]]==F2[i][j] for i in range(6) for j in range(6))
        rows.append({'a':aa,'g':[[str(x[0]),str(x[1])] for x in g],
                     'B':str(B),'full_three_block_identities':True})
    rho,N=make(*cases[0]);assert N==32
    minorities=[F(3,32),F(6,32),F(6,32),F(6,32)]
    for i,p in enumerate(minorities):assert e.local_marginal(rho,i)==[[e.z(1-p),e.ZERO],[e.ZERO,e.z(p)]]
    radii=[1-2*p for p in minorities];assert radii==[F(13,16),F(5,8),F(5,8),F(5,8)]
    S=sum(x*x for x in radii);assert S==F(469,256)
    assert 4*S>F(64,9) and e.trace(e.matmul(rho,e.global_spinflip(rho)))==e.ZERO
    v=[F(0)]*16
    for i,x in ((0,5),(7,2),(11,1),(13,1),(14,1)):v[i]=F(x)
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
    ident=e.zero(16);Q=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    for i in (0,1,2):Q[i][i]=e.ONE
    frame=d.local_pauli_frame(rho)
    assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(17,5)),e.scale_matrix(frame,-1))))==16
    in2=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(201,100)),e.scale_matrix(frame,-1)))
    in3=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(8,5)),e.scale_matrix(frame,-1)))
    assert in2==(15,1,0) and in3==(14,2,0)
    assert F(17,5)+F(201,100)+F(8,5)<8
    outs=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(17,100)),e.scale_matrix(out,-1))))==16
        inertia=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(9,100)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        P=Q if p<1 else e.global_spinflip(Q)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        trace=e.trace(e.matmul(P,out));assert trace[1]==0 and trace[0]<F(7,20)<F(32,81)
        outs.append({'p':str(p),'lambda1_upper_LDL_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'top3_upper':'7/20','product_reference':'32/81','gap_lower':str(F(32,81)-F(7,20)),
                     'same_projector_trace':str(trace[0])})
    print(json.dumps({'scope':'five exact physical examples; written argument, not these checks, carries all-family scope',
                     'cases':rows,'example_cut_ranks':cuts,'example_radii':list(map(str,radii)),
                     'example_S':str(S),'example_C':'0','example_G_upper':'25/32',
                     'frame_upper_inertias':[list(in2),list(in3)],'original_channels':outs},indent=2,sort_keys=True))


if __name__=='__main__':main()
