#!/usr/bin/env python3
"""Search the next coefficientwise lower-tail candidate using actual pairs."""
import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('erasure',ROOT/'frontier-20261028-04-erasure-probe.py')
l=importlib.util.module_from_spec(spec);spec.loader.exec_module(l)
b=l.base
STARTS=500
ITERATIONS=150


def pair_sum(x):
    out=np.zeros((16,16),dtype=complex)
    for i,j in itertools.combinations(range(4),2):
        out+=4*l.one_erasure(l.one_erasure(x,i),j)
    return out


def search(psi):
    previous=np.inf
    for step in range(ITERATIONS):
        vals,vecs=np.linalg.eigh(pair_sum(b.pure_density(psi)))
        basis=vecs[:,:6];Q=basis@basis.conj().T
        dual,duvec=np.linalg.eigh(pair_sum(Q))
        psi=duvec[:,0]
        value=float(dual[0])
        if abs(previous-value)<1e-13:break
        previous=value
    vals,vecs=np.linalg.eigh(pair_sum(b.pure_density(psi)))
    basis=vecs[:,:6]
    return float(sum(vals[:6])),psi,basis,step+1


def main():
    rng=np.random.default_rng(2026102895)
    runs=[search(b.random_unit_vector(rng)) for _ in range(STARTS)]
    value,psi,basis,steps=min(runs,key=lambda z:z[0])
    rho=b.pure_density(psi);Q=basis@basis.conj().T
    val=float(np.trace(Q@pair_sum(rho)).real)
    p=2/3;out=b.direct_pauli_channel(rho,p)
    zero=np.zeros(16,dtype=complex);zero[0]=1
    ref=b.direct_pauli_channel(b.pure_density(zero),p)
    oeig=np.linalg.eigvalsh(out);reig=np.linalg.eigvalsh(ref)
    print(json.dumps({'candidate':'sum of six smallest eigenvalues of pair-marginal sum H2 >= 1',
                     'scope':'numerical coefficientwise test; not original-channel violation or universal proof',
                     'seed':2026102895,'starts':STARTS,'max_iterations':ITERATIONS,
                     'smallest_found':value,'same_Q_trace':val,'steps':steps,
                     'input_min_eig':float(np.linalg.eigvalsh(rho)[0]),
                     'projector_idempotence':float(np.linalg.norm(Q@Q-Q)),
                     'p':p,'actual_original_top10':float(sum(oeig[-10:])),
                     'product_reference_top10':float(sum(reig[-10:])),
                     'candidate_below_one_by_1e-9':bool(val<1-1e-9),
                     'state_vector':b.complex_array(psi)},indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':main()
