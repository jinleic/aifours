#!/usr/bin/env python3
"""Explore a third-eigenvalue shortcut for the actual local-Pauli frame."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("frame_probe", ROOT / "frontier-20261028-07-pauli-frame-probe.py")
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
base = f.base
SEED = 2026102829
STARTS = 120
MAX_ITER = 100


def third_eigen(psi):
    eig, vectors = np.linalg.eigh(f.pauli_frame(base.pure_density(psi)))
    return float(eig[-3]), vectors[:, -3], eig


def optimize(psi):
    val, phi, eig = third_eigen(psi)
    for iteration in range(1, MAX_ITER + 1):
        action = f.pauli_frame(base.pure_density(phi)) @ psi
        gradient = action - np.vdot(psi, action) * psi
        accepted = False
        step = 1.0
        for _ in range(16):
            candidate = psi + step * gradient
            candidate /= np.linalg.norm(candidate)
            test, test_phi, test_eig = third_eigen(candidate)
            if test > val + 1e-13:
                psi, val, phi, eig = candidate, test, test_phi, test_eig
                accepted = True
                break
            step /= 2
        if not accepted:
            break
    return val, psi, phi, eig, iteration


def main():
    rng = np.random.default_rng(SEED)
    candidates = [optimize(base.random_unit_vector(rng)) for _ in range(STARTS)]
    val, psi, phi, eig, steps = max(candidates, key=lambda row: row[0])
    rho = base.pure_density(psi)
    matrix = f.pauli_frame(rho)
    residual = float(np.linalg.norm(matrix @ phi - val * phi))
    print(json.dumps({"scope": "numerical test of a stronger auxiliary eigenvalue premise; not an original-channel violation or proof", "claim_tested": "for every pure 4-qubit rho, lambda_3(sum_i,a sigma_i^a rho sigma_i^a) <= 2", "seed": SEED, "starts": STARTS, "max_iterations": MAX_ITER, "best_third_eigenvalue": val, "best_top_four_eigenvalues": [float(x) for x in eig[-4:][::-1]], "best_steps": steps, "eigenvector_residual": residual, "state_trace": float(np.trace(rho).real), "state_min_eigenvalue": float(np.linalg.eigvalsh(rho)[0]), "candidate_over_2_by_1e-9": bool(val > 2 + 1e-9), "state_vector": base.complex_array(psi)}, indent=2, sort_keys=True))
    if residual > 1e-10 or np.linalg.eigvalsh(rho)[0] < -1e-10:
        raise SystemExit("numerical physicality/eigenvalue check failed")


if __name__ == "__main__":
    main()
