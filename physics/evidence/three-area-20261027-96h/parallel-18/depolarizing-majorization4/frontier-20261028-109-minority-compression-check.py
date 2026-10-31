#!/usr/bin/env python3
"""Exact physical rank-three compression refuting a fixed-minority PSD shortcut."""
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
e,b=s.e,s.b


def main():
    v=[F(0)]*16
    for i,x in ((1,9),(2,9),(4,9),(7,9),(8,17)):v[i]=F(x)
    rho=[[e.z(v[i]*v[j]/613) for j in range(16)] for i in range(16)]
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
    marg=[e.local_marginal(rho,i) for i in range(4)]
    expected=[F(289,613)]+[F(162,613)]*3
    for matrix,pi in zip(marg,expected):
        assert matrix==[[e.z(1-pi),e.ZERO],[e.ZERO,e.z(pi)]] and pi<F(1,2)
    ident=e.zero(16);minor=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    minor[15][15]=e.ONE
    H=r.h1(rho);A=e.add_matrix(e.add_matrix(H,e.scale_matrix(ident,-1)),minor)
    assert all(A[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
    denom={1:775,2:775,4:775,7:197,8:1029}
    for i,dn in denom.items():assert A[i][i]==e.z(F(dn,613))
    R=sum((v[i]*v[i]/denom[i] for i in denom),F(0))
    assert R==F(157977809,157102575)>1
    u=[F(0)]*16
    for i,dn in denom.items():u[i]=v[i]/dn
    norm=sum(x*x for x in u)
    W=[[e.z(u[i]*u[j]/norm) for j in range(16)] for i in range(16)]
    Q=e.add_matrix(W,minor);Q[11][11]=e.ONE
    assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(3)
    assert e.matmul(Q,W)==W and e.matmul(W,W)==W
    bad=e.add_matrix(A,e.scale_matrix(rho,-1))
    value=e.trace(e.matmul(W,bad))
    exact=F(-138267549682306,41828213810472121)
    assert value==e.z(exact) and exact==R*(1-R)/(613*norm)<0
    compressed=e.matmul(e.matmul(Q,bad),Q)
    assert e.trace(e.matmul(W,compressed))==e.z(exact)
    target=e.trace(e.matmul(Q,e.add_matrix(H,e.scale_matrix(rho,-1))))
    assert target[1]==0 and target[0]>2
    results=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(Q,p);assert out==b.direct_pauli(Q,p)
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(39,100)),e.scale_matrix(out,-1))))==16
        val=e.trace(e.matmul(rho,out));assert val[1]==0 and val[0]<F(39,100)<F(32,81)
        results.append({'p':str(p),'same_Q_state_trace':str(val[0]),'dual_upper':'39/100',
                        'upper_LDL_pivots':16,'reference_k3':'32/81','gap_lower':str(F(32,81)-F(39,100))})
    print(json.dumps({'scope':'one actual GME state and actual rank-three Q; false shortcut only, not original-channel violation',
                      'marginal_minority_probabilities':list(map(str,expected)),'cut_ranks':cuts,
                      'rank_Q':3,'R':str(R),'negative_compression_rayleigh':str(exact),
                      'same_Q_actual_H1_minus_rho_trace':str(target[0]),'original_channels':results},
                     indent=2,sort_keys=True))


if __name__=='__main__':main()
