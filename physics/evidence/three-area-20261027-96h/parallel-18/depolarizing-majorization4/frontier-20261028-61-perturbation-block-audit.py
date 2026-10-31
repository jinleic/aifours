#!/usr/bin/env python3
"""Bounded numerical stress test of the explicit uniform block-rotation argument."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("physical",ROOT/"frontier-20261028-02-physical-seesaw.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
SEED=2026102861
REST=[i for i in range(16) if i.bit_count()>=2]
GROUP=[0 if i==0 else 1 if i.bit_count()==1 else 2 for i in range(16)]


def H(X,t):
    out=np.zeros((16,16),complex)
    for labels,P in b.PAULI_PRODUCTS:
        k=sum(j!=0 for j in labels)
        if k:out+=(t**(k-1))*np.trace(X@P)*P
    return out


def comm(A,B):return A@B-B@A


def off_solver(A,diagonal):
    S=np.zeros_like(A)
    for i in range(16):
        for j in range(16):
            if GROUP[i]!=GROUP[j]:S[i,j]=-A[i,j]/(diagonal[i]-diagonal[j])
    assert np.max(np.abs(S+S.conj().T))<1e-10
    return S


def exp_anti(S,scale):
    eigen,vectors=np.linalg.eigh(-1j*S)
    return (vectors*np.exp(1j*scale*eigen))@vectors.conj().T


def main():
    rng=np.random.default_rng(SEED)
    worst_ratio=0.0;worst_gap_error=float("inf");max_V=0.0;max_S1=0.0;max_Q=0.0;max_S2=0.0;cases=0
    zero=np.zeros(16,complex);zero[0]=1;rho0=b.pure_density(zero)
    for t in (0.0,0.01,0.25):
        D=H(rho0,t);diag=np.diag(D).real
        assert np.max(np.abs(D-np.diag(diag)))<1e-10
        for _ in range(10):
            v=np.zeros(16,complex);v[REST]=rng.normal(size=len(REST))+1j*rng.normal(size=len(REST));v/=np.linalg.norm(v)
            rho1=np.outer(v,zero.conj())+np.outer(zero,v.conj())
            Wraw=b.pure_density(v)-rho0
            V=H(rho1,t);W=H(Wraw,t)
            for i in range(16):
                for j in range(16):
                    if GROUP[i] in (0,1) and GROUP[j] in (0,1):assert abs(V[i,j])<1e-10
            S1=off_solver(V,diag)
            Vdiag=V+comm(D,S1)
            Q=W+comm(V,S1)+0.5*comm(comm(D,S1),S1)
            S2=off_solver(Q,diag)
            Qdiag=Q+comm(D,S2)
            max_V=max(max_V,float(np.linalg.norm(V,2)));max_S1=max(max_S1,float(np.linalg.norm(S1,2)))
            max_Q=max(max_Q,float(np.linalg.norm(Q,2)));max_S2=max(max_S2,float(np.linalg.norm(S2,2)))
            for eps in (1e-4,1e-5):
                psi=(zero+eps*v)/np.sqrt(1+eps*eps)
                actual=H(b.pure_density(psi),t)
                U1=exp_anti(S1,eps);U2=exp_anti(S2,eps*eps)
                rotated=U2.conj().T@U1.conj().T@actual@U1@U2
                target=D+eps*Vdiag+eps*eps*Qdiag
                err=float(np.linalg.norm(rotated-target,2))
                ratio=err/eps**3
                worst_ratio=max(worst_ratio,ratio)
                old=float(sum(np.linalg.eigvalsh(D)[-3:]));new=float(sum(np.linalg.eigvalsh(actual)[-3:]))
                normalized=(old-new)/(eps*eps)
                worst_gap_error=min(worst_gap_error,normalized)
                assert ratio<2e9 and normalized>15/32-1e-4
                cases+=1
    print(json.dumps({"scope":"bounded numerical audit of the proposed matrix perturbation; not an all-state proof", "seed":SEED,"states_per_t":10,"t_values":[0,0.01,0.25],"epsilon_values":[1e-4,1e-5],"cases":cases,"max_observed_remainder_norm_over_epsilon_cubed":worst_ratio,"minimum_observed_rescaled_k3_gap_over_epsilon_squared":worst_gap_error,"max_V_operator_norm":max_V,"max_S1_operator_norm":max_S1,"max_Q_operator_norm":max_Q,"max_S2_operator_norm":max_S2},indent=2,sort_keys=True))


if __name__=="__main__":main()
