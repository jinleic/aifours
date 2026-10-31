#!/usr/bin/env python3
"""Search an intermediate spinflip-and-marginal lower-tail inequality."""
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('erasure',ROOT/'frontier-20261028-04-erasure-probe.py')
l=importlib.util.module_from_spec(spec);spec.loader.exec_module(l)
b=l.base
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
U=b.tensor([Y]*4)
STARTS=500
ITERATIONS=150


def spin(x):return U@x.T@U.conj().T


def h1(x):
    out=np.zeros((16,16),dtype=complex)
    for i in range(4):
        z=x
        for j in range(4):
            if i!=j:z=l.one_erasure(z,j)
        out+=8*z
    return out


def transform(x):return h1(x)+spin(x)


def search(psi):
    previous=np.inf
    for step in range(ITERATIONS):
        vals,vecs=np.linalg.eigh(transform(b.pure_density(psi)))
        basis=vecs[:,:6];Q=basis@basis.conj().T
        dual,duvec=np.linalg.eigh(transform(Q))
        psi=duvec[:,0];value=float(dual[0])
        if abs(previous-value)<1e-13:break
        previous=value
    vals,vecs=np.linalg.eigh(transform(b.pure_density(psi)))
    return float(sum(vals[:6])),psi,vecs[:,:6],step+1


def main():
    rng=np.random.default_rng(2026102896)
    runs=[search(b.random_unit_vector(rng)) for _ in range(STARTS)]
    value,psi,basis,steps=min(runs,key=lambda z:z[0])
    rho=b.pure_density(psi);Q=basis@basis.conj().T
    val=float(np.trace(Q@transform(rho)).real)
    out=b.direct_pauli_channel(rho,2/3);zero=np.zeros(16,complex);zero[0]=1
    ref=b.direct_pauli_channel(b.pure_density(zero),2/3)
    print(json.dumps({'candidate':'sum of six smallest eigenvalues of H1+spinflip(rho) >= 7',
                     'scope':'numerical auxiliary test, no original-channel violation or universal proof',
                     'seed':2026102896,'starts':STARTS,'max_iterations':ITERATIONS,
                     'smallest_found':value,'same_Q_trace':val,'steps':steps,
                     'input_min_eigenvalue':float(np.linalg.eigvalsh(rho)[0]),
                     'projector_idempotence':float(np.linalg.norm(Q@Q-Q)),
                     'p':2/3,'original_top10':float(sum(np.linalg.eigvalsh(out)[-10:])),
                     'reference_top10':float(sum(np.linalg.eigvalsh(ref)[-10:])),
                     'candidate_below_7_by_1e-9':bool(val<7-1e-9),
                     'state_vector':b.complex_array(psi)},indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':main()
