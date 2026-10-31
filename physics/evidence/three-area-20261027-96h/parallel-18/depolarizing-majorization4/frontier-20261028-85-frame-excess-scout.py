#!/usr/bin/env python3
"""Variationally search physical states for frame positive-excess counterexamples."""
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location('frame', ROOT / 'frontier-20261028-07-pauli-frame-probe.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
b = f.base
RNG = np.random.default_rng(2026102885)
STARTS = 250
ITERATIONS = 150


def search(rank, initial):
    psi = initial
    previous = -np.inf
    for step in range(ITERATIONS):
        values, vectors = np.linalg.eigh(f.pauli_frame(b.pure_density(psi)))
        basis = vectors[:, -rank:]
        projector = basis @ basis.conj().T
        dual = f.pauli_frame(projector)
        dual_values, dual_vectors = np.linalg.eigh(dual)
        psi = dual_vectors[:, -1]
        objective = float(dual_values[-1] - 2 * rank)
        if abs(objective - previous) < 1e-12:
            break
        previous = objective
    values, vectors = np.linalg.eigh(f.pauli_frame(b.pure_density(psi)))
    basis = vectors[:, -rank:]
    projector = basis @ basis.conj().T
    value = float(sum(values[-rank:]) - 2 * rank)
    return value, psi, projector, step + 1


def main():
    outputs = []
    for rank in range(1, 5):
        runs = [search(rank, b.random_unit_vector(RNG)) for _ in range(STARTS)]
        value, psi, projector, iterations = max(runs, key=lambda x: x[0])
        rho = b.pure_density(psi)
        p = 0.2
        zero = np.zeros(16, dtype=complex)
        zero[0] = 1
        original = np.linalg.eigvalsh(b.direct_pauli_channel(rho, p))
        reference = np.linalg.eigvalsh(b.direct_pauli_channel(b.pure_density(zero), p))
        frame_eig = np.linalg.eigvalsh(f.pauli_frame(rho))
        outputs.append({'rank': rank, 'best_excess': value, 'iterations': iterations,
                        'frame_top4': frame_eig[-4:][::-1].tolist(),
                        'projector_residual': float(np.linalg.norm(projector @ projector - projector)),
                        'input_min_eigenvalue': float(np.linalg.eigvalsh(rho)[0]),
                        'p': p, 'original_top3': float(sum(original[-3:])),
                        'reference_top3': float(sum(reference[-3:])),
                        'state_vector': b.complex_array(psi)})
    print(json.dumps({'candidate': 'Tr(F(rho)-2I)_+ <= 2', 'starts_per_rank': STARTS,
                      'max_iterations': ITERATIONS, 'seed': 2026102885,
                      'scope': 'numerical actual-state search, not a universal proof or original-channel violation',
                      'runs': outputs}, indent=2, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
