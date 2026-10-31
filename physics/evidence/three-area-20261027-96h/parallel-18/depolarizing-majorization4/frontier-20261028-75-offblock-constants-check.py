#!/usr/bin/env python3
"""Exact Frobenius/off-block and scalar checks for sharpened noise constants."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("bloch",ROOT/"frontier-20261028-12-bloch-gap-check.py")
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
e=b.e
GROUP=[0 if i==0 else 1 if i.bit_count()==1 else 2 for i in range(16)]


def sub(A,B):return e.add_matrix(A,e.scale_matrix(B,-1))
def comm(A,B):return sub(e.matmul(A,B),e.matmul(B,A))
def norm2(A):return sum(x[0]*x[0]+x[1]*x[1] for row in A for x in row)
def off(A):return [[A[i][j] if GROUP[i]!=GROUP[j] else e.ZERO for j in range(16)] for i in range(16)]


def H(X,t):
    out=e.scale_matrix(e.channel(X,1-t),16)
    tr=e.trace(X)
    for i in range(16):out[i][i]=e.add(out[i][i],e.scale(tr,-1))
    return e.scale_matrix(out,1/t)


def H0(X):
    I=[[e.ONE,e.ZERO],[e.ZERO,e.ONE]]
    Xp=[[e.ZERO,e.ONE],[e.ONE,e.ZERO]]
    Y=[[e.ZERO,e.z(0,-1)],[e.IMAG,e.ZERO]]
    Z=[[e.ONE,e.ZERO],[e.ZERO,e.z(-1)]]
    out=e.zero(16)
    for site in range(4):
        for pauli in (Xp,Y,Z):
            U=[[e.ONE]]
            for j in range(4):U=b.kron(U,pauli if j==site else I)
            coeff=e.trace(e.matmul(X,U));assert coeff[1]==0
            out=e.add_matrix(out,e.scale_matrix(U,coeff[0]))
    return out


def solve(A,diag):
    S=e.zero(16)
    for i in range(16):
        for j in range(16):
            if GROUP[i]!=GROUP[j]:S[i][j]=e.scale(A[i][j],-1/(diag[i]-diag[j]))
    assert S==e.scale_matrix(e.adjoint(S),-1)
    return S


def main():
    r0=e.zero(16);r0[0][0]=e.ONE
    vectors=[]
    for idx in (3,7,15):
        v=[e.ZERO]*16;v[idx]=e.ONE;vectors.append(v)
    v=[e.ZERO]*16;v[3]=e.z(F(1,3));v[7]=e.z(0,F(2,3));v[15]=e.z(F(2,3));vectors.append(v)
    checks=0
    for t in (F(1,1000),F(9,10**6)):
        D=H(r0,t);diag=[D[i][i][0] for i in range(16)]
        assert all(D[i][j]==e.ZERO for i in range(16) for j in range(16) if i!=j)
        assert diag[0]-diag[1]>=2 and diag[1]-diag[3]>=2
        for v in vectors:
            assert sum(x[0]*x[0]+x[1]*x[1] for x in v)==1
            rv=[[e.mul(v[i],e.conj(v[j])) for j in range(16)] for i in range(16)]
            x1=e.zero(16)
            for i in range(16):
                x1[i][0]=e.add(x1[i][0],v[i]);x1[0][i]=e.add(x1[0][i],e.conj(v[i]))
            x2=sub(rv,r0);V=H(x1,t);W=H(x2,t);Wzero=H0(x2)
            assert norm2(V)<F(23,1000)**2
            assert norm2(Wzero)<=16**2 and norm2(off(Wzero))<=8**2
            assert norm2(sub(W,Wzero))<F(23,1000)**2
            S1=solve(V,diag);assert norm2(S1)<F(3,250)**2
            Q=e.add_matrix(e.add_matrix(W,comm(V,S1)),e.scale_matrix(comm(comm(D,S1),S1),F(1,2)))
            assert norm2(Q)<17**2 and norm2(off(Q))<F(81,10)**2
            S2=solve(Q,diag);assert norm2(S2)<F(41,10)**2
            checks+=1
    eps=F(1,100);tstar=F(9,10**6)
    assert 512*F(1,1000)**2<F(23,1000)**2
    first=F(5,1)*(F(3,125))**3/F(3)+F(23,1000)*(F(3,125))**2+2*17*F(3,125)+F(1,5)
    second=5*F(41,5)**2*eps+2*F(23,1000)*F(41,5)+2*17*F(41,5)*eps+F(11,10)
    assert first<F(11,10) and second==F(4767,625)<8
    assert 3*8*eps<F(15,32)
    assert 20*tstar<2*eps**2/(1+eps**2)
    print(json.dumps({"scope":"finite exact matrix/off-block and scalar checks, not a universal proof", "shrinkages":["1/1000","9/1000000"], "exact_normal_direction_cases":checks,"first_remainder_coefficient_upper":str(first),"second_remainder_coefficient_upper":str(second),"epsilon0":str(eps),"candidate_uniform_t":str(tstar),"all_Frobenius_and_scalar_checks":True},indent=2,sort_keys=True))


if __name__=="__main__":main()
