#!/usr/bin/env python3
"""Physical common-projector test of coefficientwise erasure-layer bounds."""

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("erasure_probe", ROOT / "frontier-20261028-04-erasure-probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
base = probe.base
SEED = 2026102805
STARTS = 60
MAX_ITER = 100


def layer(matrix, m):
    result = np.zeros((16, 16), dtype=complex)
    for sites in itertools.combinations(range(4), m):
        current = matrix
        for site in sites:
            current = probe.one_erasure(current, site)
        result += current
    return result


def direct_pauli_layer(matrix, m):
    result = np.zeros((16, 16), dtype=complex)
    for sites in itertools.combinations(range(4), m):
        for labels in itertools.product(range(4), repeat=m):
            operators = [base.I] * 4
            for site, label in zip(sites, labels):
                operators[site] = base.PAULI[label]
            unitary = base.tensor(operators)
            result += unitary @ matrix @ unitary.conj().T / (4 ** m)
    return result


def optimize(m, psi):
    previous = None
    for step in range(1, MAX_ITER + 1):
        value, basis = base.top3(layer(base.pure_density(psi), m))
        projector = basis @ basis.conj().T
        values, vectors = np.linalg.eigh(layer(projector, m))
        value = float(values[-1])
        psi = vectors[:, -1]
        if previous is not None and abs(value - previous) < 1e-13:
            break
        previous = value
    value, basis = base.top3(layer(base.pure_density(psi), m))
    return value, psi, basis, step


def main():
    rng = np.random.default_rng(SEED)
    reference = np.zeros(16, dtype=complex)
    reference[0] = 1
    rho_reference = base.pure_density(reference)
    reference_projector = np.diag([1.0, 1.0, 1.0] + [0.0] * 13)
    rows = []
    for m in (1, 2, 3):
        ref = float(np.trace(reference_projector @ layer(rho_reference, m)).real)
        candidates = [optimize(m, base.random_unit_vector(rng)) for _ in range(STARTS)]
        score, psi, basis, steps = max(candidates, key=lambda item: item[0])
        rho = base.pure_density(psi)
        projector = basis @ basis.conj().T
        direct = direct_pauli_layer(rho, m)
        tr = np.trace(projector @ direct)
        row = {
            "m": m,
            "reference_same_projector": ref,
            "max_numerical_sample": score,
            "min_numerical_sample": min(item[0] for item in candidates),
            "steps_best": steps,
            "direct_pauli_top3": float(sum(np.linalg.eigvalsh(direct)[-3:])),
            "direct_pauli_projector_trace": float(tr.real),
            "direct_trace_imag_abs": float(abs(tr.imag)),
            "candidate_exceeds_reference_by_1e-9": bool(tr.real > ref + 1e-9),
            "direct_vs_partial_trace_max_error": float(np.max(np.abs(direct - layer(rho, m)))),
            "rho_min_eigenvalue": float(np.linalg.eigvalsh(rho)[0]),
            "rho_trace": float(np.trace(rho).real),
            "projector_idempotence_max_error": float(np.max(np.abs(projector @ projector - projector))),
            "projector_trace": float(np.trace(projector).real),
            "state_vector": base.complex_array(psi),
        }
        rows.append(row)
    print(json.dumps({"scope": "finite numerical auxiliary layer test, not a global proof or physical original-channel counterexample", "seed": SEED, "starts_per_layer": STARTS, "max_iterations": MAX_ITER, "rows": rows}, indent=2, sort_keys=True, allow_nan=False))
    if any(row["direct_vs_partial_trace_max_error"] > 1e-10 or row["projector_idempotence_max_error"] > 1e-10 or row["rho_min_eigenvalue"] < -1e-10 for row in rows):
        raise SystemExit("layer physicality or independent channel check failed")


if __name__ == "__main__":
    main()
