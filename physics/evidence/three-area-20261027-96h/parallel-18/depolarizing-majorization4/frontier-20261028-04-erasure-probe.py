#!/usr/bin/env python3
"""Bounded physical test of a candidate common-projector first-order bound."""

import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("physical_seesaw", ROOT / "frontier-20261028-02-physical-seesaw.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

SEED = 2026102804
STARTS = 100
MAX_ITER = 120
TOL = 1e-13


def one_erasure(matrix, site):
    a = np.asarray(matrix, dtype=complex).reshape((2,) * 8)
    reduced = np.trace(a, axis1=site, axis2=site + 4)
    result = np.zeros_like(a)
    for bit in range(2):
        index = [slice(None)] * 8
        index[site] = bit
        index[site + 4] = bit
        result[tuple(index)] = reduced / 2.0
    return result.reshape(16, 16)


def erasure_sum(matrix):
    return sum((one_erasure(matrix, site) for site in range(4)), np.zeros((16, 16), dtype=complex))


def direct_pauli_erasure_sum(matrix):
    result = np.zeros((16, 16), dtype=complex)
    for site in range(4):
        for pauli in base.PAULI:
            operands = [base.I] * 4
            operands[site] = pauli
            operator = base.tensor(operands)
            result += operator @ matrix @ operator.conj().T / 4.0
    return result


def optimize(psi):
    previous = None
    for iteration in range(1, MAX_ITER + 1):
        matrix = erasure_sum(base.pure_density(psi))
        _, basis = base.top3(matrix)
        projector = basis @ basis.conj().T
        values, vectors = np.linalg.eigh(erasure_sum(projector))
        psi = vectors[:, -1]
        value = float(values[-1])
        if previous is not None and abs(value - previous) < TOL:
            break
        previous = value
    value, basis = base.top3(erasure_sum(base.pure_density(psi)))
    return value, psi, basis, iteration


def main():
    rng = np.random.default_rng(SEED)
    reference = np.zeros(16, dtype=complex)
    reference[0] = 1
    reference_value, _ = base.top3(erasure_sum(base.pure_density(reference)))
    candidates = [optimize(base.random_unit_vector(rng)) for _ in range(STARTS)]
    value, psi, basis, iteration = max(candidates, key=lambda item: item[0])
    rho = base.pure_density(psi)
    projector = basis @ basis.conj().T
    direct = direct_pauli_erasure_sum(rho)
    direct_eigen_top3 = float(sum(np.linalg.eigvalsh(direct)[-3:]))
    direct_trace = np.trace(projector @ direct)
    report = {
        "candidate": "for every physical rho and actual rank3 P: sum_i Tr[P E_i(rho)] <= 3",
        "scope": "numerical test only; this is not an original-channel counterexample or an all-variable proof",
        "seed": SEED,
        "starts": STARTS,
        "max_iterations": MAX_ITER,
        "reference_product_value": reference_value,
        "best_optimized_value": value,
        "minimum_final_value": min(item[0] for item in candidates),
        "best_steps": iteration,
        "direct_pauli_top3": direct_eigen_top3,
        "direct_pauli_projector_trace_real": float(direct_trace.real),
        "direct_pauli_projector_trace_imag_abs": float(abs(direct_trace.imag)),
        "direct_vs_partial_trace_max_error": float(np.max(np.abs(direct - erasure_sum(rho)))),
        "rho_min_eigenvalue": float(np.linalg.eigvalsh(rho)[0]),
        "rho_trace": float(np.trace(rho).real),
        "projector_trace": float(np.trace(projector).real),
        "projector_idempotence_max_error": float(np.max(np.abs(projector @ projector - projector))),
        "projector_hermiticity_max_error": float(np.max(np.abs(projector - projector.conj().T))),
        "candidate_greater_than_3_by_1e-9": bool(direct_eigen_top3 > 3 + 1e-9 and direct_trace.real > 3 + 1e-9),
        "state_vector": base.complex_array(psi),
        "projector_basis": base.complex_array(basis),
    }
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    if report["direct_vs_partial_trace_max_error"] > 1e-10 or report["projector_idempotence_max_error"] > 1e-10 or report["rho_min_eigenvalue"] < -1e-10:
        raise SystemExit("physicality or channel cross-check failed")


if __name__ == "__main__":
    main()
