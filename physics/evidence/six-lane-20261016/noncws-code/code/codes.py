"""Explicit test codes (state-vector bases) used as positive/negative controls."""
import itertools

import numpy as np

from pauli_tools import apply_pauli


def pauli_from_string(sstr):
    """'XZIY...' -> (x,z) masks with qubit l = character l."""
    x = z = 0
    for l, ch in enumerate(sstr):
        if ch in "XY":
            x |= 1 << l
        if ch in "ZY":
            z |= 1 << l
    return x, z


def stabilizer_code_basis(gens, n, seed=0):
    """Orthonormal basis of the common +1 eigenspace of Hermitian Pauli generators (strings)."""
    N = 2 ** n
    P = np.eye(N, dtype=complex)
    for g in gens:
        sgn = 1
        if g.startswith("-"):
            sgn, g = -1, g[1:]
        x, z = pauli_from_string(g)
        E = np.zeros((N, N), dtype=complex)
        for col in range(N):
            e = np.zeros(N, dtype=complex)
            e[col] = 1
            E[:, col] = apply_pauli(x, z, e, n)
        P = P @ (np.eye(N) + sgn * E) / 2
    w, v = np.linalg.eigh((P + P.conj().T) / 2)
    B = v[:, w > 0.5]
    return B


def steane():
    gens = ["XXXXIII", "XXIIXXI", "XIXIXIX", "ZZZZIII", "ZZIIZZI", "ZIZIZIZ"]
    return stabilizer_code_basis(gens, 7)


def five_qubit():
    gens = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
    return stabilizer_code_basis(gens, 5)


def code_8_3_3():
    gens = ["XXXXXXXX", "ZZZZZZZZ", "IXIXYZYZ", "IXZYIXZY", "IYXZXZIY"]
    return stabilizer_code_basis(gens, 8)


def tensor_zero(B, extra):
    """Append `extra` qubits in |0> as the highest-index qubits: basis index s has bit l = qubit l,
    so the new vectors are B padded with zeros for indices >= 2^n."""
    N = B.shape[0]
    out = np.zeros((N * 2 ** extra, B.shape[1]), dtype=complex)
    out[:N, :] = B
    return out


def random_subcode(B, K, seed):
    rng = np.random.default_rng(seed)
    G = rng.normal(size=(B.shape[1], K)) + 1j * rng.normal(size=(B.shape[1], K))
    Q, _ = np.linalg.qr(G)
    return B @ Q


def random_subspace(n, K, seed):
    rng = np.random.default_rng(seed)
    G = rng.normal(size=(2 ** n, K)) + 1j * rng.normal(size=(2 ** n, K))
    Q, _ = np.linalg.qr(G)
    return Q
