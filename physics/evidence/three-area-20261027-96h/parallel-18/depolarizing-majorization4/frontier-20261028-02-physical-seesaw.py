#!/usr/bin/env python3
"""Bounded four-qubit k=3 seesaw on actual states and projectors.

Deterministic numerical exploration only: it does not prove majorization.  A
positive numerical result is a candidate, not a rigorously certified witness.
"""

import itertools
import json
from fractions import Fraction

import numpy as np

N = 16
QUBITS = 4
SEED = 20261028
STARTS = 12
MAX_ITER = 80
TOL = 1e-13
PARAMETERS = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(5, 4), Fraction(4, 3)]
MIRRORS = [Fraction(1), Fraction(13, 12), Fraction(7, 6), Fraction(5, 4), Fraction(4, 3)]

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = (I, X, Y, Z)


def tensor(operators):
    result = operators[0]
    for operator in operators[1:]:
        result = np.kron(result, operator)
    return result


PAULI_PRODUCTS = [(choice, tensor([PAULI[j] for j in choice])) for choice in itertools.product(range(4), repeat=QUBITS)]
U = tensor([Y] * QUBITS)


def channel(matrix, p):
    """Apply (1-p) A + p I_i/2 tensor Tr_i A to each original site."""
    a = np.asarray(matrix, dtype=complex).reshape((2,) * (2 * QUBITS)).copy()
    for site in range(QUBITS):
        reduced = np.trace(a, axis1=site, axis2=site + QUBITS)
        diagonal = np.zeros_like(a)
        for bit in range(2):
            index = [slice(None)] * (2 * QUBITS)
            index[site] = bit
            index[site + QUBITS] = bit
            diagonal[tuple(index)] = reduced
        a = (1.0 - p) * a + (p / 2.0) * diagonal
    return a.reshape(N, N)


def direct_pauli_channel(matrix, p):
    """Independent channel construction from fourfold Pauli Kraus mixture."""
    weights = (1.0 - 3.0 * p / 4.0, p / 4.0, p / 4.0, p / 4.0)
    result = np.zeros((N, N), dtype=complex)
    for choice, operator in PAULI_PRODUCTS:
        weight = weights[choice[0]] * weights[choice[1]] * weights[choice[2]] * weights[choice[3]]
        result += weight * (operator @ matrix @ operator.conj().T)
    return result


def pure_density(psi):
    return np.outer(psi, psi.conj())


def random_unit_vector(rng):
    v = rng.normal(size=N) + 1j * rng.normal(size=N)
    return v / np.linalg.norm(v)


def random_rank3(rng):
    v = rng.normal(size=(N, 3)) + 1j * rng.normal(size=(N, 3))
    basis, _ = np.linalg.qr(v)
    return basis @ basis.conj().T


def top3(matrix):
    values, vectors = np.linalg.eigh(matrix)
    basis = vectors[:, -3:]
    return float(np.sum(values[-3:])), basis


def reference3(p):
    a = (1.0 + abs(1.0 - p)) / 2.0
    return a * a * a * (2.0 - a)


def seesaw(p, psi):
    previous = None
    count = 0
    for count in range(1, MAX_ITER + 1):
        output = channel(pure_density(psi), p)
        _, basis = top3(output)
        projector = basis @ basis.conj().T
        values, vectors = np.linalg.eigh(channel(projector, p))
        value = float(values[-1])
        psi = vectors[:, -1]
        if previous is not None and abs(value - previous) < TOL:
            break
        previous = value
    output = channel(pure_density(psi), p)
    value, basis = top3(output)
    return value - reference3(p), psi, basis, count


def complex_array(a):
    return [[[float(z.real), float(z.imag)] for z in row] for row in a] if a.ndim == 2 else [[float(z.real), float(z.imag)] for z in a]


def main():
    rng = np.random.default_rng(SEED)
    rho0 = np.zeros((N, N), dtype=complex)
    rho0[0, 0] = 1.0
    validation_rho = pure_density(random_unit_vector(rng))
    validation_projector = random_rank3(rng)
    max_channel_disagreement = 0.0
    max_reference_formula_error = 0.0
    for pf in [Fraction(0), Fraction(2, 3), Fraction(1), Fraction(4, 3)]:
        p = float(pf)
        for matrix in (validation_rho, validation_projector, rho0):
            max_channel_disagreement = max(max_channel_disagreement, float(np.max(np.abs(channel(matrix, p) - direct_pauli_channel(matrix, p)))))
        ref_eigen = np.linalg.eigvalsh(direct_pauli_channel(rho0, p))
        max_reference_formula_error = max(max_reference_formula_error, abs(float(sum(ref_eigen[-3:])) - reference3(p)))

    max_spectrum_error = 0.0
    max_same_pair_error = 0.0
    max_mirror_projector_error = 0.0
    minimum_state_eigenvalue = 0.0
    minimum_output_eigenvalue = 1.0
    for pf in MIRRORS:
        p = float(pf)
        for _ in range(8):
            rho = pure_density(random_unit_vector(rng))
            projector = random_rank3(rng)
            mirrored = U @ projector.T @ U
            out = channel(rho, p)
            out_mirror = channel(rho, 2.0 - p)
            max_spectrum_error = max(max_spectrum_error, float(np.max(np.abs(np.linalg.eigvalsh(out) - np.linalg.eigvalsh(out_mirror)))))
            max_same_pair_error = max(max_same_pair_error, float(abs(np.trace(projector @ out) - np.trace(mirrored @ out_mirror))))
            max_mirror_projector_error = max(max_mirror_projector_error, float(np.max(np.abs(mirrored @ mirrored - mirrored))))
            minimum_state_eigenvalue = min(minimum_state_eigenvalue, float(np.linalg.eigvalsh(rho)[0]))
            minimum_output_eigenvalue = min(minimum_output_eigenvalue, float(np.linalg.eigvalsh(out)[0]))

    rows = []
    best = None
    for pf in PARAMETERS:
        p = float(pf)
        candidates = [seesaw(p, random_unit_vector(rng)) for _ in range(STARTS)]
        margin, psi, basis, iterations = max(candidates, key=lambda x: x[0])
        row = {"p_exact": str(pf), "p_float": p, "max_sampled_k3_minus_reference": margin, "iterations_best": iterations, "minimum_sampled_k3_minus_reference": min(c[0] for c in candidates)}
        rows.append(row)
        if best is None or margin > best[0]:
            best = (margin, pf, psi, basis, iterations)

    margin, pf, psi, basis, iterations = best
    p = float(pf)
    rho = pure_density(psi)
    projector = basis @ basis.conj().T
    direct = direct_pauli_channel(rho, p)
    direct_ref = direct_pauli_channel(rho0, p)
    direct_top3 = float(sum(np.linalg.eigvalsh(direct)[-3:]))
    direct_reference = float(sum(np.linalg.eigvalsh(direct_ref)[-3:]))
    direct_trace = np.trace(projector @ direct)
    checks = {
        "max_partial_trace_vs_pauli_entry_error": max_channel_disagreement,
        "max_reference_formula_error": max_reference_formula_error,
        "max_mirror_spectrum_error": max_spectrum_error,
        "max_mirror_same_pair_trace_error": max_same_pair_error,
        "max_mirror_projector_idempotence_error": max_mirror_projector_error,
        "minimum_sampled_input_eigenvalue": minimum_state_eigenvalue,
        "minimum_sampled_output_eigenvalue": minimum_output_eigenvalue,
        "best_input_min_eigenvalue": float(np.linalg.eigvalsh(rho)[0]),
        "best_input_trace_real": float(np.trace(rho).real),
        "best_output_min_eigenvalue_direct": float(np.linalg.eigvalsh(direct)[0]),
        "best_projector_trace_real": float(np.trace(projector).real),
        "best_projector_idempotence_max_error": float(np.max(np.abs(projector @ projector - projector))),
        "best_projector_hermitian_max_error": float(np.max(np.abs(projector - projector.conj().T))),
        "best_direct_projector_trace_real": float(direct_trace.real),
        "best_direct_projector_trace_imag_abs": float(abs(direct_trace.imag)),
        "best_direct_top3": direct_top3,
        "best_direct_reference_top3": direct_reference,
        "best_direct_margin": direct_top3 - direct_reference,
        "best_trace_margin": float(direct_trace.real) - direct_reference,
    }
    report = {
        "scope": "numerical bounded seesaw; no universal or exact-witness claim",
        "seed": SEED,
        "starts_per_parameter": STARTS,
        "max_iterations_per_start": MAX_ITER,
        "mirror_random_trials": len(MIRRORS) * 8,
        "rows": rows,
        "checks": checks,
        "best_parameter_exact": str(pf),
        "best_final_iterations": iterations,
        "best_state_vector_complex_pairs": complex_array(psi),
        "best_rank3_basis_rows_complex_pairs": complex_array(basis),
        "candidate_over_1e-9": bool(direct_top3 - direct_reference > 1e-9 and float(direct_trace.real) - direct_reference > 1e-9),
    }
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    critical = [max_channel_disagreement, max_reference_formula_error, max_spectrum_error, max_same_pair_error, max_mirror_projector_error, checks["best_projector_idempotence_max_error"], checks["best_projector_hermitian_max_error"], checks["best_direct_projector_trace_imag_abs"]]
    if max(critical) > 1e-10 or checks["best_input_min_eigenvalue"] < -1e-10 or checks["best_output_min_eigenvalue_direct"] < -1e-10:
        raise SystemExit("numerical physicality or channel cross-check FAILED")


if __name__ == "__main__":
    main()
