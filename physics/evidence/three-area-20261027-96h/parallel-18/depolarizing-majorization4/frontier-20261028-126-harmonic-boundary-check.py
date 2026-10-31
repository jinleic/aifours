#!/usr/bin/env python3
"""Exact diagnostics for harmonic zero-support, equality and s=1/0 cases."""
import importlib.util
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
e,d=s.e,s.d


def state(entries,N):
    v=[F(0)]*16
    for i,x in entries:v[i]=F(x)
    out=[[e.z(v[i]*v[j]/N) for j in range(16)] for i in range(16)]
    assert out==e.adjoint(out) and e.matmul(out,out)==out and e.trace(out)==e.ONE
    return out


def main():
    cases=[
      ('zero_denominator',[(0,2),(12,1)],5,[F(1,5),F(1,5),F(0),F(0)],
       {F(18,5):1,F(3):2,F(13,5):2,F(12,5):1,F(2):5,F(7,5):2,F(1):3},[7,11],F(41,91)),
      ('harmonic_equality',[(0,3),(7,1),(11,1),(13,1),(14,1)],13,[F(3,13)]*4,
       {F(40,13):1,F(3):1,F(33,13):3,F(2):6,F(19,13):5},[],F(1)),
      ('s_equals_one',[(0,1),(12,1)],2,[F(1,2),F(1,2),F(0),F(0)],
       {F(3):4,F(2):9,F(1):3},None,None),
      ('product_s_zero',[(0,1)],1,[F(0)]*4,
       {F(4):1,F(3):4,F(2):6,F(1):5},None,None)]
    rows=[]
    for name,entries,N,minorities,spectrum,expected_zero,expected_W in cases:
        sigma=state(entries,N);rho=e.global_spinflip(sigma);H=r.h1(sigma)
        for i,pi in enumerate(minorities):
            assert e.local_marginal(sigma,i)==[[e.z(1-pi),e.ZERO],[e.ZERO,e.z(pi)]]
        assert all(H[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
        ss=sum(minorities);T=e.add_matrix(r.h1(rho),sigma);eigs=d.verify_spectrum(T,spectrum)
        assert eigs[1]<=3
        row={'name':name,'minorities':list(map(str,minorities)),'s':str(ss),
             'lambda2':str(eigs[1]),'exact_T_spectrum':{str(k):v for k,v in spectrum.items()}}
        if 0<ss<1:
            zeros=[];W=F(0)
            for x in range(15):
                denominator=H[x][x][0]-1;prob=sigma[x][x][0]
                assert denominator>=0
                if denominator==0:
                    zeros.append(x);assert prob==0
                else:W+=prob/denominator
            q4=sigma[15][15][0]
            assert zeros==expected_zero and W==expected_W and W<=1+q4/(1-ss)
            row.update({'zero_denominator_indices':zeros,'all_zero_components_vanish':True,
                        'W':str(W),'q4':str(q4),'rhs':str(1+q4/(1-ss))})
        elif ss==1:
            assert all(H[x][x][0]>=1 for x in range(16))
            row['s_equals_one_psd_diagonal_checked']=True
        rows.append(row)
    print(json.dumps({'scope':'four exact physical boundary examples, not an all-state proof',
                      'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
