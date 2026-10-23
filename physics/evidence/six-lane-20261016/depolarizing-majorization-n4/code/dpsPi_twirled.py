"""Level-2 extension on the Pi side WITH idempotency, twirled (walled-Brauer, per-site C + M_2), for U_s(k) at n = 4.

Relaxes omP = sigma (x) Pi (x) Pi'  (sigma state, Pi = Pi' a rank-k PROJECTOR; the bilinear maximum is attained at
projectors, so this restriction is harmless).  Constraints, each valid for that product and covariant under
conj(U) (x) U (x) U per site:
  omP >= 0; invariant under conjugation by F_{Pi Pi'};  omega := Tr_{Pi'}(omP)/k  (level-1 variable, all LP constraints);
  PPT w.r.t. Pi, Pi', sigma;
  L1 = (Tr_Pi(omP)/k)_{sigma Pi'} (x) 1_Pi - omP = sigma (x) (1-Pi) (x) Pi >= 0 (+ PPTs);
  L2 = sigma(x)1(x)1 - omega(x)1 - (omega on sigma Pi') (x) 1_Pi + omP = sigma (x) (1-Pi) (x) (1-Pi) >= 0 (+ PPTs);
  idempotency: Tr_{Pi Pi'}[omP (1 (x) F_{Pi Pi'})] = Tr(Pi^2) sigma = k sigma  (twirled: scalar equation).
Usage: python dpsPi_twirled.py <s> <k> [noidem]
"""
import itertools
import sys
from math import comb

import cvxpy as cp
import numpy as np

from dps2_twirled import matrix_units, coeffs, ptrans, ptrace, I2


def build(s, k, idem=True):
    A, posA = matrix_units([-1, +1, +1])        # (sigma, Pi, Pi')
    AT1, pos1 = matrix_units([-1, -1, +1])      # T_Pi
    AT2, pos2 = matrix_units([-1, +1, -1])      # T_Pi'
    AT0, pos0 = matrix_units([+1, +1, +1])      # T_sigma
    phi = np.zeros(4, dtype=complex); phi[0] = phi[3] = 1 / np.sqrt(2)
    E2 = [np.outer(phi, phi.conj()), np.eye(4) - np.outer(phi, phi.conj())]     # on (sigma, Pi)
    F = np.zeros((4, 4)); F[0, 0] = F[3, 3] = 1; F[1, 2] = F[2, 1] = 1
    FPP = np.kron(I2, F)                                                         # swap Pi <-> Pi'
    SW12 = np.kron(F, I2)                                                        # swap sigma <-> Pi (relabel)
    # per-site maps
    M_trPp = np.array([coeffs(ptrace(b, 2), E2) for b in A]).T          # Tr_Pi' -> (sigma,Pi)
    M_trP = np.array([coeffs(ptrace(b, 1), E2) for b in A]).T           # Tr_Pi  -> (sigma,Pi')
    M_conjF = np.array([coeffs(FPP @ b @ FPP, A) for b in A]).T
    M_t1 = np.array([coeffs(ptrans(b, 1), AT1) for b in A]).T
    M_t2 = np.array([coeffs(ptrans(b, 2), AT2) for b in A]).T
    M_t0 = np.array([coeffs(ptrans(b, 0), AT0) for b in A]).T
    # embeddings of (sigma,X)-operators e in E2 into A: e on (sigma,Pi') (x) 1_Pi  and e on (sigma,Pi) (x) 1_Pi'
    def emb_on(e, which):
        if which == "sigmaPi":          # e on (sigma, Pi), identity on Pi'
            return np.kron(e, I2)
        T = np.kron(e, I2).reshape([2] * 6)          # e on (sigma, Pi'), identity on Pi: permute Pi <-> Pi'
        return T.transpose(0, 2, 1, 3, 5, 4).reshape(8, 8)
    M_emb_sP = np.array([coeffs(emb_on(e, "sigmaPi"), A) for e in E2]).T
    M_emb_sPp = np.array([coeffs(emb_on(e, "sigmaPip"), A) for e in E2]).T
    one = coeffs(np.eye(8), A)
    idem_fun = np.array([np.trace(b @ FPP) / 2 for b in A])          # Tr_{Pi Pi'}[b F] = a 1_sigma, Tr = 2a
    kr = lambda M: np.kron(np.kron(M, M), np.kron(M, M))

    def placement(pos):
        rows, cols = [], []
        for idx in itertools.product(range(5), repeat=4):
            rows.append(sum(pos[i][0] * 3 ** (3 - l) for l, i in enumerate(idx)))
            cols.append(sum(pos[i][1] * 3 ** (3 - l) for l, i in enumerate(idx)))
        return rows, cols
    pl = {name: placement(p) for name, p in (("A", posA), ("1", pos1), ("2", pos2), ("0", pos0))}
    idxT = {}
    for r in range(5):
        for T in itertools.combinations(range(4), r):
            idxT[T] = [sum(d[l] * 3 ** (3 - l) for l in range(4))
                       for d in itertools.product(*[(1, 2) if l in T else (0,) for l in range(4)])]
    ET = {T: np.eye(81)[:, idx] for T, idx in idxT.items()}

    def to81(vec, name):
        rows, cols = pl[name]
        Pm = np.zeros((81 * 81, 625))
        for t, (r, c_) in enumerate(zip(rows, cols)):
            Pm[r * 81 + c_, t] = 1
        return cp.reshape(Pm @ vec, (81, 81), order="C")

    def psd(vec, name):
        M = to81(vec, name)
        return [ET[T].T @ M @ ET[T] >> 0 for T in idxT]

    Sel = np.zeros((625, 81 * 81))
    for t, (r, c_) in enumerate(zip(*pl["A"])):
        Sel[t, r * 81 + c_] = 1
    Bv = {T: cp.Variable((len(idx), len(idx)), hermitian=True) for T, idx in idxT.items()}
    W = sum(ET[T] @ Bv[T] @ ET[T].T for T in idxT)
    x = Sel @ cp.vec(W, order="C")
    cons = [Bv[T] >> 0 for T in idxT]
    cons.append(kr(M_conjF) @ x == x)
    subsets = [S for r in range(5) for S in itertools.combinations(range(4), r)]
    kron_index = {S: sum((0 if l in S else 1) * 2 ** (3 - l) for l in range(4)) for S in subsets}
    om = kr(M_trPp) @ x / k                       # omega on (sigma, Pi), 16 coeffs in (Phi+,1-Phi+) kron order
    omp = kr(M_trP) @ x / k                       # sigma (x) Pi' on (sigma, Pi')
    cvec = cp.Variable(16)
    cons += [om[kron_index[S]] == cvec[i] for i, S in enumerate(subsets)]
    g = lambda inS, t: (0.5 if t == 0 else -0.5) if inS else (0.5 if t == 0 else 1.5)
    cons += [cvec >= 0, cvec <= 1 / 16, sum(cvec[i] * 3 ** (4 - len(S)) for i, S in enumerate(subsets)) == k]
    for tau in itertools.product((0, 1), repeat=4):
        e = sum(cvec[i] * np.prod([g(l in S, tau[l]) for l in range(4)]) for i, S in enumerate(subsets))
        cons += [e >= 0, e <= 1 / 16]
    for vec in (x,):
        cons += psd(kr(M_t1) @ vec, "1") + psd(kr(M_t2) @ vec, "2") + psd(kr(M_t0) @ vec, "0")
    L1 = kr(M_emb_sPp) @ omp - x                                  # sigma (x) (1-Pi) (x) Pi'
    sig1 = kr(one[:, None]).ravel() / 16                           # sigma_tw (x) 1 (x) 1 = 1/16
    L2 = sig1 - kr(M_emb_sP) @ om - kr(M_emb_sPp) @ omp + x       # sigma (x) (1-Pi) (x) (1-Pi')
    for L in (L1, L2):
        cons += psd(L, "A") + psd(kr(M_t1) @ L, "1") + psd(kr(M_t2) @ L, "2") + psd(kr(M_t0) @ L, "0")
    if idem:
        cons.append(kr(idem_fun[None, :]) @ x == k / 16)
    obj = [comb(len(S), s) * 2 ** s * 3 ** (4 - len(S)) for S in subsets]
    return cp.Problem(cp.Maximize(sum(obj[i] * cvec[i] for i in range(16))), cons)


if __name__ == "__main__":
    s, k = int(sys.argv[1]), int(sys.argv[2])
    idem = "noidem" not in sys.argv
    prob = build(s, k, idem)
    val = prob.solve(solver=cp.CLARABEL)
    eig = sorted([comb(z, s) for z in range(5) for _ in range(comb(4, z))], reverse=True)
    print(f"U{s} k={k} Pi-extension idem={idem} value={val:.8f} target={sum(eig[:k])} status={prob.status}")
