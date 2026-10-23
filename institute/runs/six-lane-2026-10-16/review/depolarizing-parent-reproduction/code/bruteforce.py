#!/usr/bin/env python3
"""Brute-force reference on the full space R (x) (C^2)^{(x)M}  (dimension 2 * 2^M).
Independent of sym_depol.py except for sharing nothing but numpy."""
import math
import numpy as np


def dicke_matrix(M):
    """rows x = 0..M : normalized Dicke vectors |M;x> in the computational basis."""
    n = 2 ** M
    pop = np.array([bin(i).count("1") for i in range(n)])
    V = np.zeros((M + 1, n))
    for x in range(M + 1):
        idx = pop == x
        V[x, idx] = 1.0 / math.sqrt(idx.sum())
    return V


def apply_depol(rho, M, eta, nR):
    """D_eta on each of the M qubits of a (nR*2^M)-dim operator (R is the leading factor)."""
    d = nR * 2 ** M
    for k in range(M):
        A, B = nR * 2 ** k, 2 ** (M - k - 1)
        t = rho.reshape(A, 2, B, A, 2, B)
        tr = t[:, 0, :, :, 0, :] + t[:, 1, :, :, 1, :]
        new = eta * t
        new[:, 0, :, :, 0, :] += 0.5 * (1 - eta) * tr
        new[:, 1, :, :, 1, :] += 0.5 * (1 - eta) * tr
        rho = new.reshape(d, d)
    return rho


def vn_entropy(rho):
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 0]
    return float(-np.sum(ev * np.log(ev)))


def coherent_information_bf(phis, qs, M, eta):
    """phis: Dicke amplitude vectors (length M+1); purification sum_i sqrt(q_i)|i>_R|phi_i>."""
    V = dicke_matrix(M)
    n = 2 ** M
    psi = np.zeros(2 * n, dtype=complex)
    for i in range(2):
        psi[i * n:(i + 1) * n] = math.sqrt(qs[i]) * (np.asarray(phis[i], dtype=complex) @ V)
    rhoRA = np.outer(psi, psi.conj())
    rhoRB = apply_depol(rhoRA, M, eta, 2)
    rhoB = rhoRB[:n, :n] + rhoRB[n:, n:]
    SB, SRB = vn_entropy(rhoB), vn_entropy(rhoRB)
    return dict(SB=SB, SRB=SRB, Ic_nats=SB - SRB, trace=float(np.real(np.trace(rhoB))))


def singlet_embedding(M, r):
    """Columns: |psi^->^{(x) r} (x) |N;b>, b=0..N, qubits (0,1),...,(2r-2,2r-1) in singlets,
    Dicke state on the last N = M-2r qubits.  Qubit 0 = most significant bit."""
    N = M - 2 * r
    sing = np.array([0.0, 1.0, -1.0, 0.0]) / math.sqrt(2.0)   # (|01>-|10>)/sqrt2
    s = np.array([1.0])
    for _ in range(r):
        s = np.kron(s, sing)
    VN = dicke_matrix(N) if N > 0 else np.ones((1, 1))
    cols = [np.kron(s, VN[b]) for b in range(N + 1)]
    return np.array(cols).T


def block_bf(X_dicke, M, eta, r):
    """Brute-force Schur-Weyl block r of D^{(x)M}(X) through the singlet embedding."""
    V = dicke_matrix(M)
    X = V.T @ X_dicke @ V
    Y = apply_depol(X.astype(complex), M, eta, 1)
    E = singlet_embedding(M, r)
    return E.T @ Y @ E


def SN_bf(Z_dicke, N, eta):
    """Pi_N D^{(x)N}(Z) Pi_N in the Dicke basis."""
    V = dicke_matrix(N)
    Z = V.T @ Z_dicke @ V
    Y = apply_depol(Z.astype(complex), N, eta, 1)
    return V @ Y @ V.T
