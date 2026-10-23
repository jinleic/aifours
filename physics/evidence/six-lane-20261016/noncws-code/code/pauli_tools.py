"""Pauli-string utilities for n <= ~9 qubits (dense state vectors).

Pauli labels: integer pair (x, z) of n-bit masks; Hermitian Pauli E(x,z) = i^{|x&z|} X^x Z^z.
Bit l of a mask refers to qubit l; basis index s has bit l = state of qubit l.
"""
import numpy as np


def popcount(a):
    a = np.asarray(a, dtype=np.int64)
    c = np.zeros_like(a)
    while np.any(a):
        c += a & 1
        a = a >> 1
    return c


def fwht(f):
    """Unnormalized Walsh-Hadamard transform along last axis: F[z] = sum_s (-1)^{z.s} f[s]."""
    f = np.array(f, dtype=complex, copy=True)
    N = f.shape[-1]
    h = 1
    while h < N:
        f = f.reshape(f.shape[:-1] + (N // (2 * h), 2, h))
        a = f[..., 0, :].copy()
        b = f[..., 1, :].copy()
        f[..., 0, :] = a + b
        f[..., 1, :] = a - b
        f = f.reshape(f.shape[:-3] + (N,))
        h *= 2
    return f


def pauli_expectations(W, n):
    """t[x, z] = Tr(P E(x,z)) for P = W W^dag (W: 2^n x K with orthonormal columns)."""
    N = 2 ** n
    s = np.arange(N)
    t = np.zeros((N, N), dtype=complex)
    for x in range(N):
        # f[s] = sum_i conj(psi_i[s]) psi_i[s ^ x]
        f = np.sum(np.conj(W) * W[s ^ x, :], axis=1)
        # <psi| X^x Z^z |psi> = sum_s conj(psi[s]) (X^x Z^z psi)[s]; (X^x Z^z psi)[s] = (Z^z psi)[s^x]
        #   = (-1)^{z.(s^x)} psi[s^x]
        F = fwht(f)  # F[z] = sum_s (-1)^{z.s} f[s]
        zz = np.arange(N)
        sign = (-1.0) ** popcount(zz & x)
        ph = (1j) ** (popcount(np.full(N, x) & zz) % 4)
        t[x, :] = ph * sign * F
    return t


def apply_pauli(x, z, psi, n):
    """Return E(x,z) psi."""
    N = 2 ** n
    s = np.arange(N)
    # (X^x Z^z psi)[s] = (Z^z psi)[s ^ x] = (-1)^{z.(s^x)} psi[s^x]
    out = ((-1.0) ** popcount(z & (s ^ x))) * psi[s ^ x]
    return (1j) ** (int(popcount(np.array([x & z]))[0]) % 4) * out


def weight(x, z):
    return popcount(np.asarray(x) | np.asarray(z))
