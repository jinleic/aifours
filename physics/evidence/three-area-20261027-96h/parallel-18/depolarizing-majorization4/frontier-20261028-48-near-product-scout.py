#!/usr/bin/env python3
"""Bounded original-channel k3 search near a product input/full noise."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("base",ROOT/"frontier-20261028-02-physical-seesaw.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

SEED=2026102848
SAMPLES_PER_GRID=120
SHRINKS=(0.01,0.03,0.1,0.2,0.3)
RELATIVE_AMPLITUDES=(0.1,0.5,1.0,2.0,5.0)


def main():
    rng=np.random.default_rng(SEED)
    perturbable=np.array([i for i in range(16) if i.bit_count()>=2])
    zero=np.zeros(16,complex);zero[0]=1
    all_rows=[];overall=None
    for t in SHRINKS:
        p=1-t
        for factor in RELATIVE_AMPLITUDES:
            lam=factor*t
            best=None
            for _ in range(SAMPLES_PER_GRID):
                v=rng.normal(size=len(perturbable))+1j*rng.normal(size=len(perturbable))
                v/=np.linalg.norm(v)
                psi=zero.copy();psi[perturbable]=lam*v;psi/=np.linalg.norm(psi)
                out=b.channel(b.pure_density(psi),p)
                value,basis=b.top3(out)
                gap=b.reference3(p)-value
                if best is None or gap<best[0]:best=(gap,psi,basis)
            row={"shrink":t,"p":p,"relative_amplitude":factor,"lambda":lam,"smallest_reference_minus_actual_top3":best[0]}
            all_rows.append(row)
            if overall is None or best[0]<overall[0]:overall=(best[0],p,t,factor,best[1],best[2])
    gap,p,t,factor,psi,basis=overall
    rho=b.pure_density(psi);P=basis@basis.conj().T
    out=b.direct_pauli_channel(rho,p)
    ref=np.zeros((16,16),complex);ref[0,0]=1
    ref_out=b.direct_pauli_channel(ref,p)
    eig=np.linalg.eigvalsh(out);refeig=np.linalg.eigvalsh(ref_out)
    direct_gap=float(sum(refeig[-3:])-sum(eig[-3:]))
    ptrace=np.trace(P@out)
    report={"scope":"bounded numerical near-product/full-noise original-channel search; no global proof or exact witness", "seed":SEED,"samples_per_grid":SAMPLES_PER_GRID,"sample_count":len(SHRINKS)*len(RELATIVE_AMPLITUDES)*SAMPLES_PER_GRID,"grid":all_rows,"worst_p":p,"worst_shrink":t,"worst_factor":factor,"direct_original_top3":float(sum(eig[-3:])),"direct_product_reference_top3":float(sum(refeig[-3:])),"direct_reference_minus_top3":direct_gap,"same_P_trace":float(ptrace.real),"same_P_trace_imag_abs":float(abs(ptrace.imag)),"state_trace":float(np.trace(rho).real),"state_min_eigenvalue":float(np.linalg.eigvalsh(rho)[0]),"original_output_min_eigenvalue":float(eig[0]),"projector_trace":float(np.trace(P).real),"projector_idempotence_max_error":float(np.max(np.abs(P@P-P))),"candidate_violation_over_1e-9":bool(direct_gap < -1e-9 and ptrace.real > sum(refeig[-3:])+1e-9),"state_vector":b.complex_array(psi),"projector_basis":b.complex_array(basis)}
    print(json.dumps(report,indent=2,sort_keys=True,allow_nan=False))
    if report["same_P_trace_imag_abs"]>1e-10 or report["projector_idempotence_max_error"]>1e-10 or report["state_min_eigenvalue"] < -1e-10 or report["original_output_min_eigenvalue"] < -1e-10:
        raise SystemExit("numerical original physicality or projector failure")


if __name__=="__main__":main()
