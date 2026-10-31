#!/usr/bin/env python3
"""Search an actual-state projected-frame inequality relevant near p=0."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("frame",ROOT/"frontier-20261028-07-pauli-frame-probe.py")
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
b=f.base
SEED=2026102884
STARTS=250
MAX_ITER=100
I=np.eye(16,dtype=complex)


def objective(psi):
    rho=b.pure_density(psi);Q=I-rho
    frame=f.pauli_frame(rho)
    eig,vec=np.linalg.eigh(Q@frame@Q)
    local=np.array([float(np.vdot(psi,P@psi).real) for P in f.OPERATORS])
    S=float(local@local)
    return float(eig[-1]+S/2-4),vec[:,-1],S,eig


def optimize(psi):
    value,phi,S,eig=objective(psi)
    for iteration in range(1,MAX_ITER+1):
        local=np.array([float(np.vdot(psi,P@psi).real) for P in f.OPERATORS])
        action=f.pauli_frame(b.pure_density(phi))@psi
        for r,P in zip(local,f.OPERATORS):action+=r*(P@psi)
        action-=phi*np.vdot(phi,action)
        gradient=action-psi*np.vdot(psi,action)
        step=1.0;accepted=False
        for _ in range(16):
            q=psi+step*gradient;q-=phi*np.vdot(phi,q);q/=np.linalg.norm(q)
            candidate,cphi,cS,ceig=objective(q)
            if candidate>value+1e-12:
                psi,value,phi,S,eig=q,candidate,cphi,cS,ceig;accepted=True;break
            step/=2
        if not accepted:break
    return value,psi,phi,S,eig,iteration


def main():
    rng=np.random.default_rng(SEED)
    results=[optimize(b.random_unit_vector(rng)) for _ in range(STARTS)]
    value,psi,phi,S,eig,iterations=max(results,key=lambda row:row[0])
    rho=b.pure_density(psi);Q=I-rho;frame=f.pauli_frame(rho)
    residual=float(np.linalg.norm(Q@frame@Q@phi-eig[-1]*phi))
    p=0.2;out=b.direct_pauli_channel(rho,p);zero=np.zeros(16,complex);zero[0]=1
    ref=b.direct_pauli_channel(b.pure_density(zero),p)
    oeig=np.linalg.eigvalsh(out);reig=np.linalg.eigvalsh(ref)
    print(json.dumps({"scope":"numerical structural candidate test, not an original-channel violation or universal proof", "candidate":"lambda_max((I-rho) F(rho) (I-rho)) + S/2 <= 4", "seed":SEED,"starts":STARTS,"max_iterations":MAX_ITER,"largest_sampled_excess":value,"S":S,"projected_frame_lambda_max":float(eig[-1]),"eigenvector_residual":residual,"phi_psi_overlap_abs":float(abs(np.vdot(phi,psi))),"input_trace":float(np.trace(rho).real),"input_min_eigenvalue":float(np.linalg.eigvalsh(rho)[0]),"original_p":p,"original_top3":float(sum(oeig[-3:])),"product_reference_top3":float(sum(reig[-3:])),"candidate_excess_over_1e-9":bool(value>1e-9),"state_vector":b.complex_array(psi)},indent=2,sort_keys=True,allow_nan=False))
    if residual>1e-10 or abs(np.vdot(phi,psi))>1e-10:raise SystemExit("projected eigenpair failed")


if __name__=="__main__":main()
