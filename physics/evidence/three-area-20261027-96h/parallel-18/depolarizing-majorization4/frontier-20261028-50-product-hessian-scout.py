#!/usr/bin/env python3
"""Second-order original-channel k3 stress test at a pure product input."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("physical",ROOT/"frontier-20261028-02-physical-seesaw.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
SEED=2026102850
STARTS=500
SHRINKS=(0.03,0.1,0.25,0.5,0.8)
I1=np.array([1,2,4,8])
I2=np.array([i for i in range(16) if i.bit_count()>=2])
ZERO=np.zeros(16,complex);ZERO[0]=1


def hessian(t,v):
    p=1-t
    a,c=(1+t)/2,(1-t)/2
    vals=np.array([a**(4-i.bit_count())*c**i.bit_count() for i in range(16)])
    lam0,lam1=vals[0],vals[1]
    sigma0=b.channel(b.pure_density(ZERO),p)
    sigmav=b.channel(b.pure_density(v),p)
    V=b.channel(np.outer(v,ZERO.conj())+np.outer(ZERO,v.conj()),p)
    if max(abs(V[0,0]),float(np.max(np.abs(V[np.ix_(I1,I1)]))),float(np.max(np.abs(V[I1,0]))))>1e-12:
        raise RuntimeError("first-order block did not vanish")
    a0=float((sigmav[0,0]-lam0).real+sum(abs(V[k,0])**2/(lam0-vals[k]) for k in I2))
    M=sigmav[np.ix_(I1,I1)]-lam1*np.eye(4,dtype=complex)
    for k in I2:
        M+=np.outer(V[I1,k],V[k,I1])/(lam1-vals[k])
    if np.max(np.abs(M-M.conj().T))>1e-11:
        raise RuntimeError("effective Hessian is not Hermitian")
    eig=np.linalg.eigvalsh(M)
    return a0+float(sum(eig[-2:])),a0,eig


def main():
    rng=np.random.default_rng(SEED)
    rows=[];best=None
    for t in SHRINKS:
        candidate=None
        for _ in range(STARTS):
            vector=rng.normal(size=len(I2))+1j*rng.normal(size=len(I2));vector/=np.linalg.norm(vector)
            v=np.zeros(16,complex);v[I2]=vector
            coeff,a0,eig=hessian(t,v)
            if candidate is None or coeff>candidate[0]:candidate=(coeff,v,a0,eig)
        coeff,v,a0,eig=candidate
        epsilon=0.01
        psi=(ZERO+epsilon*v)/np.sqrt(1+epsilon**2)
        rho=b.pure_density(psi);p=1-t
        direct=b.direct_pauli_channel(rho,p)
        ref=b.direct_pauli_channel(b.pure_density(ZERO),p)
        values,basis=np.linalg.eigh(direct)
        top=float(sum(values[-3:]));ref_top=float(sum(np.linalg.eigvalsh(ref)[-3:]))
        P=basis[:,-3:]@basis[:,-3:].conj().T
        finite=(top-ref_top)/(epsilon**2)
        row={"shrink":t,"p":p,"max_sampled_second_order_coefficient":coeff,"lambda0_second_order":a0,"degenerate_lambda1_second_order_eigenvalues":[float(x) for x in eig],"epsilon":epsilon,"actual_finite_difference_coefficient":finite,"actual_reference_minus_top3":ref_top-top,"actual_input_min_eigenvalue":float(np.linalg.eigvalsh(rho)[0]),"actual_output_min_eigenvalue":float(values[0]),"actual_projector_trace":float(np.trace(P).real),"actual_projector_idempotence_max_error":float(np.max(np.abs(P@P-P))),"candidate_original_violation_over_1e-9":bool(top>ref_top+1e-9)}
        rows.append(row)
        if best is None or coeff>best[0]:best=(coeff,t,v)
    print(json.dumps({"scope":"bounded numerical second-order product-boundary stress test, not a global proof or exact witness","seed":SEED,"random_directions_per_shrink":STARTS,"direction_support":"computational basis weights 2,3,4", "rows":rows,"best_direction":[[float(z.real),float(z.imag)] for z in best[2]]},indent=2,sort_keys=True,allow_nan=False))
    if any(row["actual_input_min_eigenvalue"] < -1e-10 or row["actual_output_min_eigenvalue"] < -1e-10 or row["actual_projector_idempotence_max_error"]>1e-10 for row in rows):
        raise SystemExit("physicality check failed")


if __name__=="__main__":main()
