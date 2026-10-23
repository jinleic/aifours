"""Direct Knill-Laflamme checker (independent of the Walsh-Hadamard / orbit machinery).

For a basis W (2^n x K, orthonormal columns) and every Pauli string E of weight <= w,
compute M_E = W^dag E W and the deviation from a scalar multiple of the identity:
   dev(E) = || M_E - (tr M_E / K) I ||_F.
Degenerate codes are allowed (nonzero scalars). Paulis are built from single-qubit
matrices by explicit Kronecker-free index arithmetic.
"""
import itertools

import numpy as np

SQ = {"I": np.eye(2, dtype=complex),
      "X": np.array([[0, 1], [1, 0]], dtype=complex),
      "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
      "Z": np.array([[1, 0], [0, -1]], dtype=complex)}


def apply_local(ops, psi, n):
    """ops: dict qubit -> 2x2 matrix. psi: array (2^n, K). Qubit l = bit l of the basis index."""
    T = psi.reshape([2] * n + [psi.shape[1]])  # axis order: bit n-1, ..., bit 0 (C order)
    for q, U in ops.items():
        ax = n - 1 - q
        T = np.moveaxis(np.tensordot(U, T, axes=([1], [ax])), 0, ax)
    return T.reshape(psi.shape)


def kl_report(W, n, wmax, tol=1e-9):
    K = W.shape[1]
    G = W.conj().T @ W
    worst = 0.0
    worst_E = None
    count = 0
    scalars = {}
    for w in range(1, wmax + 1):
        for sites in itertools.combinations(range(n), w):
            for labels in itertools.product("XYZ", repeat=w):
                ops = {q: SQ[l] for q, l in zip(sites, labels)}
                M = W.conj().T @ apply_local(ops, W, n)
                c = np.trace(M) / K
                dev = np.linalg.norm(M - c * np.eye(K))
                count += 1
                if abs(c) > tol:
                    scalars[(sites, labels)] = c
                if dev > worst:
                    worst, worst_E = dev, (sites, labels)
    return {"orthonormal_dev": float(np.linalg.norm(G - np.eye(K))), "n_paulis": count,
            "max_dev": float(worst), "worst": worst_E, "n_nonzero_scalars": len(scalars)}


def distance(W, n, wmax=None, tol=1e-9):
    """Smallest weight w such that some weight-w Pauli has non-scalar compression."""
    wmax = wmax or n
    for w in range(1, wmax + 1):
        r = kl_report_weight(W, n, w, tol)
        if r > tol:
            return w
    return None


def kl_report_weight(W, n, w, tol=1e-9):
    K = W.shape[1]
    worst = 0.0
    for sites in itertools.combinations(range(n), w):
        for labels in itertools.product("XYZ", repeat=w):
            ops = {q: SQ[l] for q, l in zip(sites, labels)}
            M = W.conj().T @ apply_local(ops, W, n)
            c = np.trace(M) / K
            worst = max(worst, np.linalg.norm(M - c * np.eye(K)))
    return worst
