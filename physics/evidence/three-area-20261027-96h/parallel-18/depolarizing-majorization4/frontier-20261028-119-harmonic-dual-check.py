#!/usr/bin/env python3
"""Exact physical unequal-marginal example for the rank-one harmonic k3 criterion."""
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
    for i,x in ((0,4),(3,1),(13,1),(14,2)):v[i]=F(x)
    rho=[[e.z(v[i]*v[j]/22) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    sig=e.global_spinflip(rho)
    rotated=[[sig[i^15][j^15] for j in range(16)] for i in range(16)]
    minors=[F(5,22),F(5,22),F(5,22),F(1,11)]
    for i,pi in enumerate(minors):
        assert e.local_marginal(rho,i)==[[e.z(1-pi),e.ZERO],[e.ZERO,e.z(pi)]]
        assert e.local_marginal(rotated,i)==[[e.z(1-pi),e.ZERO],[e.ZERO,e.z(pi)]]
    radii=[1-2*q for q in minors];S=sum((x*x for x in radii),F(0));ss=sum(minors)
    assert radii==[F(6,11)]*3+[F(9,11)] and sum(radii)==F(27,11)>2
    assert S==F(189,121) and ss==F(17,22)<1
    assert e.trace(e.matmul(rho,sig))==e.ZERO
    H=r.h1(rotated)
    assert all(H[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
    W=F(0)
    for x in range(15):
        denom=H[x][x][0]-1
        prob=rotated[x][x][0]
        assert denom>=0
        if denom==0:assert prob==0
        else:W+=prob/denom
    p4=rotated[15][15][0]
    assert W==F(10042,12103) and p4==0 and W<1
    frame=d.local_pauli_frame(rho);f2=e.trace(e.matmul(frame,frame))
    assert f2==e.z(F(2692,121)) and F(2692,121)<F(208,9)
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
    pair=a.pair_density(rho,(0,1))
    assert pair[0][0]==e.z(F(17,22)) and pair[3][3]==e.z(F(5,22))
    assert all(pair[i][j]==e.ZERO for i in range(4) for j in range(4) if i!=j)
    ident=e.zero(16);Q=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    for i in (0,1,2):Q[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p);assert out==b.direct_pauli(rho,p)
        assert len(r.c.positive_definite_ldl(out))==16
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(4,25)),e.scale_matrix(out,-1))))==16
        inertia=r.end.m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(9,100)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        upper=F(17,50);ref=F(32,81);assert upper<ref
        P=Q if p<F(1) else e.global_spinflip(Q)
        assert P==e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
        tr=e.trace(e.matmul(P,out));assert tr[1]==0 and tr[0]<upper
        rows.append({'p':str(p),'lambda1_upper_LDL_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'top3_upper':str(upper),'reference_k3':str(ref),'gap_lower':str(ref-upper),
                     'same_projector_trace':str(tr[0])})
    print(json.dumps({'scope':'one actual physical unequal-marginal GME input; not a universal proof',
                      'state':'(4|0000>+|0011>+|1101>+2|1110>)/sqrt(22)',
                      'radii':list(map(str,radii)),'sum_radii':str(sum(radii)),'S':str(S),'C':'0',
                      'minority_sum':str(ss),'harmonic_W':str(W),'P4':str(p4),
                      'frame_square':str(f2[0]),'cut_ranks':cuts,'product_overlap_upper':'17/22',
                      'original_channels':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
