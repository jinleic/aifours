#!/usr/bin/env python3
"""Exact rational checks of product-boundary k3 second-order identities."""

import importlib.util
import json
import random
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("bloch",ROOT/"frontier-20261028-12-bloch-gap-check.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
e=b.e

MASK=(8,4,2,1)
ONES=(8,4,2,1)
REST=tuple(i for i in range(16) if i.bit_count()>=2)


def conj(z):return e.conj(z)
def norm(z):return z[0]*z[0]+z[1]*z[1]
def sub(x,y):return e.add(x,e.scale(y,-1))


def outer(u,v):return [[e.mul(u[i],conj(v[j])) for j in range(16)] for i in range(16)]


def data(v,t):
    N=sum(norm(x) for x in v);assert N>0 and all(v[i]==e.ZERO for i in (0,1,2,4,8))
    zero=[e.ZERO]*16;zero[0]=e.ONE
    unrho=outer(v,v)
    cross=e.add_matrix(outer(v,zero),outer(zero,v))
    sv=e.channel(e.scale_matrix(unrho,1/N),1-t)
    V=e.channel(cross,1-t)
    a,bb=(1+t)/2,(1-t)/2
    eig=[a**(4-i.bit_count())*bb**i.bit_count() for i in range(16)]
    assert V[0][0]==e.ZERO and all(V[i][j]==e.ZERO for i in ONES for j in (0,)+ONES)
    A=sv[0][0][0]-eig[0]+sum(norm(V[k][0])/(N*(eig[0]-eig[k])) for k in REST)
    M=[[e.add(sv[i][j],e.z(-eig[1] if i==j else 0)) for j in ONES] for i in ONES]
    for ii,i in enumerate(ONES):
        for jj,j in enumerate(ONES):
            for k in REST:
                M[ii][jj]=e.add(M[ii][jj],e.scale(e.mul(V[i][k],V[k][j]),1/(N*(eig[1]-eig[k]))))
    return A,M,N


def build(weight,rng):
    v=[e.ZERO]*16
    for i in REST:
        if i.bit_count()==weight:v[i]=e.z(rng.randint(-3,3),rng.randint(-3,3))
    if not any(x!=e.ZERO for x in v):v[next(i for i in REST if i.bit_count()==weight)]=e.ONE
    return v


def h2(v,t,A,M,N):
    a,bb=(1+t)/2,(1-t)/2;u=t*(1-t*t)
    gamma=[[e.ZERO for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k!=i and k!=j:
                    gamma[i][j]=e.add(gamma[i][j],e.scale(e.mul(v[MASK[i]|MASK[k]],conj(v[MASK[j]|MASK[k]])),1/N))
    n=[gamma[i][i][0] for i in range(4)]
    assert all(gamma[i][i][1]==0 and 0<=n[i]<=1 for i in range(4)) and sum(n)==2
    assert A==-a*a*u
    for i in range(4):
        for j in range(4):
            expected=e.z(-a*bb*u*(1-n[i])) if i==j else e.scale(gamma[i][j],a*bb*t*t*(1+t))
            assert M[i][j]==expected
    trace=sum(M[i][i][0] for i in range(4));assert trace==-2*a*bb*u
    centered=F(0)
    for i in range(4):
        for j in range(4):
            x=sub(M[i][j],e.z(trace/4 if i==j else 0))
            centered+=norm(x)
    assert centered<=(F(7,8)*a*u)**2
    return a*u/8


def h3(v,t,A,M,N):
    a,bb=(1+t)/2,(1-t)/2;D=1-a*bb
    g=[v[15^mask] for mask in MASK]
    assert sum(norm(x) for x in g)==N
    assert A==-a*t*D+a*t**5/D
    for i in range(4):
        for j in range(4):
            expected=e.scale(e.mul(conj(g[i]),g[j]),(t*t*bb*bb+t**5*bb/D)/N)
            if i==j:expected=e.add(expected,e.z(-a*a*bb*t-bb*bb*t*(1+t)*norm(g[i])/N))
            assert M[i][j]==expected
    upper=A-2*a*a*bb*t+t*t*bb*bb+t**5*bb/D
    poly=15+24*t+38*t*t+32*t**3+3*t**4
    assert upper==-t*(1-t)*poly/(32*D)<0
    return -upper


def h4(t,A,M):
    a,bb=(1+t)/2,(1-t)/2;D4=a*a+bb*bb
    assert A==-t*D4+t**7/D4
    for i in range(4):
        for j in range(4):assert M[i][j]==e.z(-a*bb*t if i==j else 0)
    upper=A-2*a*bb*t
    assert upper==-t+t**7/D4<0
    return -upper


def main():
    rng=random.Random(2026102857)
    ts=(F(1,100),F(1,10),F(1,4),F(1,2),F(4,5))
    counts={"weight2":0,"weight3":0,"weight4":0,"mixed_weight_exact_decomposition":0}
    for t in ts:
        for _ in range(12):
            v2,v3,v4=(build(h,rng) for h in (2,3,4))
            A2,M2,N2=data(v2,t);k2=h2(v2,t,A2,M2,N2);counts["weight2"]+=1
            A3,M3,N3=data(v3,t);k3=h3(v3,t,A3,M3,N3);counts["weight3"]+=1
            A4,M4,N4=data(v4,t);k4=h4(t,A4,M4);counts["weight4"]+=1
            mixed=[e.add(e.add(v2[i],v3[i]),v4[i]) for i in range(16)]
            Am,Mm,Nm=data(mixed,t)
            assert Nm==N2+N3+N4
            assert Am==(N2*A2+N3*A3+N4*A4)/Nm
            for i in range(4):
                for j in range(4):
                    expect=e.scale(e.add(e.add(e.scale(M2[i][j],N2),e.scale(M3[i][j],N3)),e.scale(M4[i][j],N4)),1/Nm)
                    assert Mm[i][j]==expect
            counts["mixed_weight_exact_decomposition"]+=1
            if t<=F(1,4):assert min(k2,k3,k4)>=F(15,256)*t
    print(json.dumps({"scope":"finite exact checks of derived Hessian identities; not by itself a uniform-noise theorem", "seed":2026102857,"rational_shrinkages":[str(t) for t in ts],"counts":counts,"all_weight_two_centered_frobenius_bounds":True,"all_weight_three_factored_bounds":True,"all_weight_four_bounds":True,"all_mixed_weight_decompositions":True,"explicit_uniform_coefficient_for_t_le_1_over_4":"15/256 times t"},indent=2,sort_keys=True))


if __name__=="__main__":main()
