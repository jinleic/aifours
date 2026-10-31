#!/usr/bin/env python3
"""Bounded original-channel k3/all-index search on a physical GME family."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("physical",ROOT/"frontier-20261028-02-physical-seesaw.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def family(z):
    vector=np.zeros(16,complex)
    vector[0]=1
    vector[[3,5,15]]=z
    return vector/np.linalg.norm(vector)


def reference_spectrum(p):
    a=(1+abs(1-p))/2;c=1-a
    vals=np.array([1.0])
    for _ in range(4):vals=np.kron(vals,[a,c])
    return np.sort(vals)[::-1]


def recompute(row):
    z,p,k=row[1],row[2],row[3]
    psi=family(z);rho=b.pure_density(psi)
    out=b.direct_pauli_channel(rho,p)
    ref=np.zeros((16,16),complex);ref[0,0]=1
    refout=b.direct_pauli_channel(ref,p)
    values,vectors=np.linalg.eigh(out);rv=np.linalg.eigvalsh(refout)
    P=vectors[:,-k:]@vectors[:,-k:].conj().T
    total=float(sum(values[-k:]));refsum=float(sum(rv[-k:]));trace=np.trace(P@out)
    return {"z":z,"p":p,"k":k,"direct_output_partial_sum":total,"direct_reference_partial_sum":refsum,"direct_reference_minus_output":refsum-total,"same_actual_projector_trace":float(trace.real),"projector_trace":float(np.trace(P).real),"projector_idempotence_max_error":float(np.max(np.abs(P@P-P))),"input_trace":float(np.trace(rho).real),"input_min_eigenvalue":float(np.linalg.eigvalsh(rho)[0]),"output_min_eigenvalue":float(values[0]),"candidate_violation_over_1e-9":bool(total>refsum+1e-9)}


def main():
    zs=np.linspace(0.01,1.68,90)
    ps=[i/60 for i in range(1,81) if i!=60]
    best3=bestall=None
    counts=0;pointwise2=0
    for z0 in zs:
        z=float(z0);rho=b.pure_density(family(z))
        for p in ps:
            out=b.channel(rho,p);values=np.linalg.eigvalsh(out)[::-1]
            ref=reference_spectrum(p)
            margins=np.cumsum(ref-values)[:15]
            if values[1]>ref[1]+1e-9:pointwise2+=1
            k=int(np.argmin(margins))+1
            if bestall is None or margins[k-1]<bestall[0]:bestall=(float(margins[k-1]),z,p,k)
            if best3 is None or margins[2]<best3[0]:best3=(float(margins[2]),z,p,3)
            counts+=1
    print(json.dumps({"scope":"bounded numerical actual-family search; no all-word/all-state proof or exact violation", "z_grid_count":len(zs),"p_grid_count":len(ps),"sample_count":counts,"family_z_interval":"[0.01,1.68]", "pointwise_lambda2_above_reference_cases":pointwise2,"worst_sampled_k3":recompute(best3),"worst_sampled_any_k_1_to_15":recompute(bestall)},indent=2,sort_keys=True,allow_nan=False))


if __name__=="__main__":main()
