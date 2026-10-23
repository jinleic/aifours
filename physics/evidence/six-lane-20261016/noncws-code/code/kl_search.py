"""Riemannian (Stiefel) gradient search for ((n,K,d))_2 codes: exploratory numerics ONLY.

Loss L(W) = sum_{1<=wt(E)<=d-1} || W^dag E W - (tr/K) I ||_F^2 over Hermitian Paulis E,
W in C^{2^n x K} with orthonormal columns (degenerate codes allowed: scalars free).
Optional restriction: W = B @ C where B is an orthonormal basis of a symmetry-adapted subspace.
Barzilai-Borwein steps with QR retraction and nonmonotone safeguard.
"""
import itertools
import json
import sys
import time

import numpy as np


def pauli_actions(n, wmin, wmax):
    """Return perm (m, 2^n), phase (m, 2^n) with (E psi)[s] = phase[s] * psi[perm[s]], labels."""
    N = 2 ** n
    s = np.arange(N)
    perms, phases, labels = [], [], []
    for w in range(wmin, wmax + 1):
        for sites in itertools.combinations(range(n), w):
            for lab in itertools.product("XYZ", repeat=w):
                x = z = 0
                ny = 0
                for q, ch in zip(sites, lab):
                    if ch in "XY":
                        x |= 1 << q
                    if ch in "ZY":
                        z |= 1 << q
                    if ch == "Y":
                        ny += 1
                # E = i^{ny} X^x Z^z ; (X^x Z^z psi)[s] = (-1)^{z.(s^x)} psi[s^x]
                par = np.array([bin(v).count("1") & 1 for v in (z & (s ^ x))])
                ph = (1j) ** ny * (1 - 2 * par)
                perms.append(s ^ x)
                phases.append(ph)
                labels.append((sites, lab))
    return np.array(perms), np.array(phases), labels


class KLLoss:
    def __init__(self, n, K, d, basis=None):
        self.n, self.K = n, K
        self.perm, self.phase, self.labels = pauli_actions(n, 1, d - 1)
        self.B = basis  # optional (2^n, m) orthonormal

    def full(self, C):
        return C if self.B is None else self.B @ C

    def value_grad(self, C):
        W = self.full(C)
        EW = self.phase[:, :, None] * W[self.perm]          # (m, N, K)
        M = np.einsum("si,esj->eij", W.conj(), EW)          # (m, K, K)
        tr = np.trace(M, axis1=1, axis2=2).real / self.K
        D = M - tr[:, None, None] * np.eye(self.K)[None]
        L = float(np.sum(np.abs(D) ** 2))
        G = 2 * np.einsum("esi,eij->sj", EW, D)             # dL/dconj(W)
        if self.B is not None:
            G = self.B.conj().T @ G
        return L, G


def retract(C):
    Q, R = np.linalg.qr(C)
    return Q * np.sign(np.diag(R).real + 1e-300)[None, :]


def search(loss, C0, iters=4000, tol=1e-28, verbose=False):
    C = retract(C0)
    L, G = loss.value_grad(C)
    Gr = G - C @ ((C.conj().T @ G + G.conj().T @ C) / 2)
    step = 1e-2
    hist = [L]
    Cprev = Grprev = None
    for it in range(iters):
        if Cprev is not None:
            S = C - Cprev
            Y = Gr - Grprev
            sy = np.real(np.vdot(S, Y))
            if sy > 0:
                step = np.real(np.vdot(S, S)) / sy
            step = min(max(step, 1e-6), 10.0)
        # nonmonotone backtracking
        Lref = max(hist[-10:])
        gn2 = np.real(np.vdot(Gr, Gr))
        t = step
        for _ in range(30):
            Cn = retract(C - t * Gr)
            Ln, Gn = loss.value_grad(Cn)
            if Ln <= Lref - 1e-4 * t * gn2:
                break
            t *= 0.5
        Cprev, Grprev = C, Gr
        C, L, G = Cn, Ln, Gn
        Gr = G - C @ ((C.conj().T @ G + G.conj().T @ C) / 2)
        hist.append(L)
        if L < tol or np.real(np.vdot(Gr, Gr)) < 1e-30:
            break
    return C, L, it


def run(n, K, d, restarts, seed, iters, basis=None):
    loss = KLLoss(n, K, d, basis)
    rng = np.random.default_rng(seed)
    m = (2 ** n) if basis is None else basis.shape[1]
    out = []
    best = None
    for r in range(restarts):
        C0 = rng.normal(size=(m, K)) + 1j * rng.normal(size=(m, K))
        t0 = time.time()
        C, L, it = search(loss, C0, iters)
        out.append({"restart": r, "loss": L, "iters": it, "sec": round(time.time() - t0, 2)})
        if best is None or L < best[0]:
            best = (L, C)
    return out, best


if __name__ == "__main__":
    n, K, d, restarts, seed, iters = [int(a) for a in sys.argv[1:7]]
    out, best = run(n, K, d, restarts, seed, iters)
    Ls = sorted(o["loss"] for o in out)
    print(json.dumps({"n": n, "K": K, "d": d, "restarts": restarts, "seed": seed, "iters": iters,
                      "best": Ls[0], "quantiles": [Ls[int(q * (len(Ls) - 1))] for q in (0, 0.1, 0.5, 0.9, 1)]}))
    np.save(f"../evidence/kl_search_best_n{n}_K{K}_d{d}_seed{seed}.npy", best[1])
