#!/usr/bin/env python3
"""Test a stronger same-pair Pauli-frame certificate, not original-channel violation."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("physical_seesaw", ROOT / "frontier-20261028-02-physical-seesaw.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

SEED = 2026102807
STARTS = 100
MAX_ITER = 100
OPERATORS = []
for site in range(4):
    for pauli in (base.X, base.Y, base.Z):
        ops = [base.I] * 4
        ops[site] = pauli
        OPERATORS.append(base.tensor(ops))


def pauli_frame(matrix):
    return sum((operator @ matrix @ operator.conj().T for operator in OPERATORS), np.zeros((16, 16), dtype=complex))


def optimize(psi):
    previous = None
    for step in range(1, MAX_ITER + 1):
        _, basis = base.top3(pauli_frame(base.pure_density(psi)))
        projector = basis @ basis.conj().T
        eigen, vectors = np.linalg.eigh(pauli_frame(projector))
        value = float(eigen[-1])
        psi = vectors[:, -1]
        if previous is not None and abs(value - previous) < 1e-13:
            break
        previous = value
    value, basis = base.top3(pauli_frame(base.pure_density(psi)))
    return value, psi, basis, step


def main():
    rng = np.random.default_rng(SEED)
    results = [optimize(base.random_unit_vector(rng)) for _ in range(STARTS)]
    value, psi, basis, steps = max(results, key=lambda x: x[0])
    rho = base.pure_density(psi)
    projector = basis @ basis.conj().T
    frame = pauli_frame(rho)
    objective = np.trace(projector @ frame)
    control_psi = np.eye(16, dtype=complex)[:, 0]
    control_P = np.diag([1.0, 1.0, 1.0] + [0.0] * 13)
    control = np.trace(control_P @ pauli_frame(base.pure_density(control_psi))).real
    report = {
        "scope": "numerical stronger auxiliary certificate only; not an original-channel violation or universal proof",
        "claim_tested": "sum_(i,a=x,y,z) Tr[P sigma_i^a rho sigma_i^a] <= 8 for actual rho and rank3 P",
        "seed": SEED,
        "starts": STARTS,
        "max_iterations": MAX_ITER,
        "control": float(control),
        "best_value": value,
        "worst_final": min(x[0] for x in results),
        "steps_best": steps,
        "same_pair_trace": float(objective.real),
        "trace_imag_abs": float(abs(objective.imag)),
        "rho_trace": float(np.trace(rho).real),
        "rho_min_eigenvalue": float(np.linalg.eigvalsh(rho)[0]),
        "projector_trace": float(np.trace(projector).real),
        "projector_idempotence_max_error": float(np.max(np.abs(projector @ projector - projector))),
        "candidate_above_8_by_1e-9": bool(objective.real > 8 + 1e-9),
        "state_vector": base.complex_array(psi),
        "projector_basis": base.complex_array(basis),
    }
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    if report["trace_imag_abs"] > 1e-10 or report["projector_idempotence_max_error"] > 1e-10 or report["rho_min_eigenvalue"] < -1e-10:
        raise SystemExit("physicality check failed")


if __name__ == "__main__":
    main()
