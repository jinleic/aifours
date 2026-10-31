#!/usr/bin/env python3
"""Numerical stress test at the proposed sharper off-block constants."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("audit",ROOT/"frontier-20261028-61-perturbation-block-audit.py")
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
b=a.b


def main():
    rng=np.random.default_rng(2026102876)
    zero=np.zeros(16,complex);zero[0]=1;rho0=b.pure_density(zero)
    max_ratio=0.0;min_gap=float("inf");max_off=0.0;cases=0
    eps=0.01
    for t in (0.0,0.000009,0.001):
        D=a.H(rho0,t);diag=np.diag(D).real
        for _ in range(30):
            v=np.zeros(16,complex);v[a.REST]=rng.normal(size=len(a.REST))+1j*rng.normal(size=len(a.REST));v/=np.linalg.norm(v)
            X1=np.outer(v,zero.conj())+np.outer(zero,v.conj())
            X2=b.pure_density(v)-rho0
            V=a.H(X1,t);W=a.H(X2,t);S1=a.off_solver(V,diag)
            Q=W+a.comm(V,S1)+0.5*a.comm(a.comm(D,S1),S1)
            Qoff=np.array([[Q[i,j] if a.GROUP[i]!=a.GROUP[j] else 0 for j in range(16)] for i in range(16)])
            max_off=max(max_off,float(np.linalg.norm(Qoff,"fro")))
            S2=a.off_solver(Q,diag);Vdiag=V+a.comm(D,S1);Qdiag=Q+a.comm(D,S2)
            psi=(zero+eps*v)/np.sqrt(1+eps*eps);actual=a.H(b.pure_density(psi),t)
            U1=a.exp_anti(S1,eps);U2=a.exp_anti(S2,eps*eps)
            residual=U2.conj().T@U1.conj().T@actual@U1@U2-(D+eps*Vdiag+eps*eps*Qdiag)
            ratio=float(np.linalg.norm(residual,2))/eps**3
            gap=(sum(np.linalg.eigvalsh(D)[-3:])-sum(np.linalg.eigvalsh(actual)[-3:]))/eps**2
            max_ratio=max(max_ratio,ratio);min_gap=min(min_gap,float(gap));cases+=1
            assert ratio<8 and gap>15/32-1e-8 and np.linalg.norm(Qoff,"fro")<8.1
    print(json.dumps({"scope":"bounded floating stress test, not universal proof", "seed":2026102876,"cases":cases,"t_values":[0,0.000009,0.001],"epsilon":eps,"max_remainder_norm_over_epsilon_cubed":max_ratio,"min_rescaled_gap_over_epsilon_squared":min_gap,"max_Q_offblock_frobenius":max_off},indent=2,sort_keys=True))


if __name__=="__main__":main()
