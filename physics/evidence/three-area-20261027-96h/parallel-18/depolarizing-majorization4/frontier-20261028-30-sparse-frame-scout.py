#!/usr/bin/env python3
"""Find a simple physical sparse counterexample to a Pauli-frame shortcut."""

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("frame_probe", ROOT / "frontier-20261028-07-pauli-frame-probe.py")
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
base = f.base
SEED = 2026102830
MAX_SAMPLES = 12000


def main():
    rng = np.random.default_rng(SEED)
    phases = np.array([1, -1, 1j, -1j], dtype=complex)
    best = None
    found = None
    for sample in range(1, MAX_SAMPLES + 1):
        size = int(rng.choice([4, 5, 6, 7, 8, 9, 10]))
        support = np.sort(rng.choice(16, size=size, replace=False))
        phase_labels = rng.integers(0, 4, size=size)
        psi = np.zeros(16, dtype=complex)
        psi[support] = phases[phase_labels] / np.sqrt(size)
        matrix = f.pauli_frame(base.pure_density(psi))
        eig = np.linalg.eigvalsh(matrix)
        val = float(eig[-3])
        if best is None or val > best[0]:
            best = (val, support.copy(), phase_labels.copy(), eig.copy(), sample)
        if val > 2.05:
            for indices in itertools.combinations(range(16), 3):
                sub = matrix[np.ix_(indices, indices)]
                smallest = float(np.linalg.eigvalsh(sub)[0])
                if smallest > 2.000001:
                    found = (val, support.copy(), phase_labels.copy(), eig.copy(), sample, indices, smallest)
                    break
            if found is not None:
                break
    entry = found if found is not None else best
    val, support, labels, eig, sample = entry[:5]
    report = {"scope": "numerical auxiliary-frame scout only; no original-channel violation claimed", "seed": SEED, "max_samples": MAX_SAMPLES, "actual_samples_run": sample if found is not None else MAX_SAMPLES, "best_sample_index": sample, "support": [int(i) for i in support], "amplitudes_before_common_normalization": [[int(phases[label].real), int(phases[label].imag)] for label in labels], "lambda3": val, "top3": [float(x) for x in eig[-3:][::-1]], "coordinate_projector_found": found is not None}
    if found is not None:
        report["coordinate_indices"] = list(found[5])
        report["coordinate_min_frame_eigenvalue"] = found[6]
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
