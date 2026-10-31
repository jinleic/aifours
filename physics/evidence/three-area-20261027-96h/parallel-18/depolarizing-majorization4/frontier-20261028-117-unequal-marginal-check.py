#!/usr/bin/env python3
"""Exact unequal-marginal GME example for the low-Bloch-sum k3 candidate."""
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
sp=importlib.util.spec_from_file_location('prev',ROOT/'frontier-20261028-115-asymmetric-equal-marginal-check.py')
a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
e,b,d,r,s=a.e,a.b,a.d,a.r,a.s


def main():
    v=[F(0)]*16
    for i,x in ((1,1),(2,2),(12,2)):v[i]=F(x,3)
    rho=[[e.z(v[i]*v[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    minorities=[F(4,9),F(4,9),F(4,9),F(1,9)]
    for i,q in enumerate(minorities):
        assert e.local_marginal(rho,i)==[[e.z(1-q),e.ZERO],[e.ZERO,e.z(q)]]
    radii=[1-2*q for q in minorities]
    assert radii==[F(1,9),F(1,9),F(1,9),F(7,9)] and sum(radii)==F(10,9)<2
    S=sum((z*z for z in radii),F(0));assert S==F(52,81)
    assert e.trace(e.matmul(rho,e.global_spinflip(rho)))==e.ZERO
    frame=d.local_pauli_frame(rho);frame2=e.trace(e.matmul(frame,frame))
    assert frame2==e.z(F(1504,81)) and F(1504,81)<F(880,39)
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
    p12=a.pair_density(rho,(0,1));p13=a.pair_density(rho,(0,2))
    assert e.trace(e.matmul(p12,p12))==e.z(F(41,81))
    assert e.trace(e.matmul(p13,p13))==e.z(F(11,27))
    assert p12[0][0]==e.z(F(5,9)) and p12[3][3]==e.z(F(4,9))
    assert all(p12[i][j]==e.ZERO for i in range(4) for j in range(4) if i!=j)
    ident=e.zero(16);Q=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    for i in (0,1,2):Q[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(r.c.positive_definite_ldl(out))==16
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(3,25)),e.scale_matrix(out,-1))))==16
        inertia=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(19,200)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        upper=F(31,100);ref=F(32,81);assert upper<ref
        P=Q if p<F(1) else e.global_spinflip(Q)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        tr=e.trace(e.matmul(P,out));assert tr[1]==0 and tr[0]<upper
        rows.append({'p':str(p),'lambda1_upper_LDL_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'top3_upper':str(upper),'reference_k3':str(ref),'gap_lower':str(ref-upper),
                     'same_projector_trace':str(tr[0])})
    print(json.dumps({'scope':'one physical unequal-marginal GME state; finite evidence, not universal proof',
                     'state':'(|0001>+2|0010>+2|1100>)/3','radii':list(map(str,radii)),
                     'sum_radii':str(sum(radii)),'S':str(S),'C':'0','frame_square':str(frame2[0]),
                     'cut_ranks':cuts,'pair12_purity':'41/81','pair13_purity':'11/27',
                     'product_overlap_upper':'5/9','original_channels':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
