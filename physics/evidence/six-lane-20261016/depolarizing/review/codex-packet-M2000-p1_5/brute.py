"""Brute-force coherent information through D_eta^{(x)M} on the full 2^M space (validation only, M <= 8)."""
from __future__ import annotations

import math

import numpy as np


def dicke(M: int, k: int) -> np.ndarray:
    v = np.zeros(2 ** M)
    for x in range(2 ** M):
        if bin(x).count("1") == k:
            v[x] = 1.0
    return v / np.linalg.norm(v)


def depolarize_all(rho: np.ndarray, M: int, eta: float, ref_dim: int) -> np.ndarray:
    """rho on C^{ref_dim} (x) (C^2)^{(x)M}; apply D_eta to each of the M qubits."""
    shape = [ref_dim] + [2] * M
    T = rho.reshape(shape + shape)
    nax = M + 1
    for j in range(1, M + 1):
        # partial trace over qubit j then tensor I/2
        tr = np.trace(T, axis1=j, axis2=j + nax)  # removes both axes
        # re-insert identity/2 at positions j and j+nax
        tr = np.expand_dims(tr, axis=j)
        tr = np.expand_dims(tr, axis=j + nax)
        eye_shape = [1] * (2 * nax)
        eye_shape[j] = 2
        eye_shape[j + nax] = 2
        I2 = np.eye(2).reshape(eye_shape)
        T = eta * T + (1 - eta) * 0.5 * tr * I2
    d = ref_dim * 2 ** M
    return T.reshape(d, d)


def entropy_bits(m: np.ndarray) -> float:
    ev = np.linalg.eigvalsh(m)
    ev = ev[ev > 1e-15]
    return float(-(ev * np.log2(ev)).sum())


def brute_ic(M: int, eta: float, cs, qs) -> float:
    r = len(cs)
    psi = np.zeros(r * 2 ** M, dtype=np.complex128)
    for i in range(r):
        v = sum(c * dicke(M, k) for k, c in enumerate(cs[i]) if c != 0)
        psi[i * 2 ** M:(i + 1) * 2 ** M] = math.sqrt(qs[i]) * v
    rho = np.outer(psi, psi.conj())
    out = depolarize_all(rho, M, eta, r)
    d = 2 ** M
    B = sum(out[i * d:(i + 1) * d, i * d:(i + 1) * d] for i in range(r))
    return entropy_bits(B) - entropy_bits(out)
