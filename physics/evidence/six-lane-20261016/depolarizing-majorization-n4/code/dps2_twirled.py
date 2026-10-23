"""Level-2 (Bose-symmetric extension of the sigma side) twirled relaxation for U_s(k) at n = 4.

Variable omega2 on (sigma, sigma', Pi) per site, relaxing sigma (x) sigma (x) Pi (sigma pure, Pi = rank-k projector).
Constraints (all valid for that product and covariant under conj(U) (x) conj(U) (x) U per site):
  omega2 >= 0;  F_{sigma sigma'} omega2 = omega2 (Bose);  Tr_{sigma'} omega2 = omega = sum_S c_S E_S;
  omega2^{T_Pi} >= 0;  omega2^{T_sigma'} >= 0;
  Lam = xi (x) 1 - omega2 >= 0 with xi = Tr_Pi(omega2)/k;  Lam^{T_Pi} >= 0;  Lam^{T_sigma'} >= 0;
  plus all level-1 LP constraints on c.
Twirling: omega2 lies in (x)_l A_l, A_l = commutant of conj(U)(x)conj(U)(x)U on C^8, A_l ~ C + M_2 (spin 3/2 once,
spin 1/2 twice). A faithful *-representation pi: A_l -> 3x3 block-diagonal matrices is built numerically from the
Casimir / weight decomposition, so positivity of an element of (x)A_l <=> pi^{(x)4}(.) (81x81) is PSD.
Partial transposes map into the commutants of conj(U)^{(x)3} (T_Pi) and conj(U)(x)U(x)U (T_sigma'), handled the same
way. Per-site linear maps between the 5-dim algebras are Kronecker-multiplied to global 625-dim maps.
Usage: python dps2_twirled.py <s> <k> [nobose] [noppt2]
"""
import itertools
import sys
from math import comb

import cvxpy as cp
import numpy as np

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0 + 0j, -1.0])
I2 = np.eye(2)
PAULI = [sx, sy, sz]


def k3(a, b, c):
    return np.kron(np.kron(a, b), c)


def generators(signs):
    """signs[j] = -1: factor j carries conj(U) (generator -conj(s)/2); +1: carries U (generator s/2)."""
    G = []
    for s in PAULI:
        mats = [(-np.conj(s) / 2 if sg < 0 else s / 2) for sg in signs]
        G.append(k3(mats[0], I2, I2) + k3(I2, mats[1], I2) + k3(I2, I2, mats[2]))
    return G


def matrix_units(signs):
    Gx, Gy, Gz = generators(signs)
    C = Gx @ Gx + Gy @ Gy + Gz @ Gz
    w, V = np.linalg.eigh(C)
    P32 = V[:, np.isclose(w, 15 / 4)]
    P12 = V[:, np.isclose(w, 3 / 4)]
    assert P32.shape[1] == 4 and P12.shape[1] == 4
    Z = P12.conj().T @ Gz @ P12
    wz, vz = np.linalg.eigh(Z)
    up = P12 @ vz[:, np.isclose(wz, 0.5)]
    assert up.shape[1] == 2
    Gm = Gx - 1j * Gy
    dn = Gm @ up
    assert np.allclose(np.linalg.norm(dn, axis=0), 1)
    B = [P32 @ P32.conj().T]
    pos = [(0, 0)]
    for m in range(2):
        for n in range(2):
            B.append(np.outer(up[:, m], up[:, n].conj()) + np.outer(dn[:, m], dn[:, n].conj()))
            pos.append((1 + m, 1 + n))
    for X in B:                                     # commutant check
        for Gq in (Gx, Gy, Gz):
            assert np.allclose(Gq @ X, X @ Gq)
    return B, pos


def coeffs(X, B):
    """expand X in the HS-orthogonal basis B; assert membership."""
    c = np.array([np.trace(b.conj().T @ X) / np.trace(b.conj().T @ b) for b in B])
    assert np.allclose(sum(ci * b for ci, b in zip(c, B)), X, atol=1e-10), "not in algebra"
    return c


def ptrans(X, j):
    T = X.reshape([2] * 6)
    T = np.swapaxes(T, j, j + 3)
    return T.reshape(8, 8)


def ptrace(X, j):
    T = X.reshape([2] * 6)
    T = np.trace(T, axis1=j, axis2=j + 3)
    return T.reshape(4, 4)


def build(s, k, bose=True, ppt2=True):
    A, posA = matrix_units([-1, -1, +1])          # omega2 algebra
    AP, posP = matrix_units([-1, -1, -1])         # image of T_Pi
    AS, posS = matrix_units([-1, +1, +1])         # image of T_sigma'
    phi = np.zeros(4, dtype=complex); phi[0] = phi[3] = 1 / np.sqrt(2)
    E2 = [np.outer(phi, phi.conj()), np.eye(4) - np.outer(phi, phi.conj())]   # on (sigma, Pi)
    F = np.zeros((4, 4)); F[0, 0] = F[3, 3] = 1; F[1, 2] = F[2, 1] = 1        # swap on (sigma, sigma')
    Psym, Panti = (np.eye(4) + F) / 2, (np.eye(4) - F) / 2
    Fs = np.kron(F, I2)
    # per-site maps (rows: target coeffs, cols: source basis index)
    M_trs = np.array([coeffs(ptrace(b, 1), E2) for b in A]).T            # Tr_sigma' -> span{Phi+, 1-Phi+}
    M_tpP = np.array([coeffs(ptrans(b, 2), AP) for b in A]).T            # T_Pi
    M_tpS = np.array([coeffs(ptrans(b, 1), AS) for b in A]).T            # T_sigma'
    M_F = np.array([coeffs(Fs @ b, A) for b in A]).T                     # left mult by F
    M_trP = np.array([coeffs(ptrace(b, 2), [Psym, Panti]) for b in A]).T # Tr_Pi -> span{Psym, Panti}
    M_emb = np.array([coeffs(np.kron(g, I2), A) for g in (Psym, Panti)]).T   # xi (x) 1 -> A
    kr = lambda M: np.kron(np.kron(M, M), np.kron(M, M))
    # placement of 625 coefficients into 81x81 (pi^{(x)4})
    def placement(pos):
        rows, cols = [], []
        for idx in itertools.product(range(5), repeat=4):
            r = sum(pos[i][0] * 3 ** (3 - l) for l, i in enumerate(idx))
            c_ = sum(pos[i][1] * 3 ** (3 - l) for l, i in enumerate(idx))
            rows.append(r); cols.append(c_)
        return rows, cols
    rA, cA = placement(posA)
    rP, cP = placement(posP)
    rS, cS = placement(posS)
    Sel = np.zeros((625, 81 * 81))
    for t, (r, c_) in enumerate(zip(rA, cA)):
        Sel[t, r * 81 + c_] = 1
    def to81(vec, rows, cols):
        Pm = np.zeros((81 * 81, 625))
        for t, (r, c_) in enumerate(zip(rows, cols)):
            Pm[r * 81 + c_, t] = 1
        return cp.reshape(Pm @ vec, (81, 81), order="C")

    idxT = {}
    for r in range(5):
        for T in itertools.combinations(range(4), r):
            idxT[T] = [sum(d[l] * 3 ** (3 - l) for l in range(4))
                       for d in itertools.product(*[(1, 2) if l in T else (0,) for l in range(4)])]
    ET = {T: np.eye(81)[:, idx] for T, idx in idxT.items()}
    Bv = {T: cp.Variable((len(idx), len(idx)), hermitian=True) for T, idx in idxT.items()}
    W = sum(ET[T] @ Bv[T] @ ET[T].T for T in idxT)                    # block-diagonal pi^{(x)4}(omega2)
    x = Sel @ cp.vec(W, order="C")                                      # omega2 coefficients
    cons = [Bv[T] >> 0 for T in idxT]

    def psd81(M):
        return [ET[T].T @ M @ ET[T] >> 0 for T in idxT]
    # Tr_sigma' -> omega coefficients over S (index 0 = Phi+ at that site)
    trs = kr(M_trs) @ x                                                  # 16, kron order over (Phi+,1-Phi+)
    subsets = [S for r in range(5) for S in itertools.combinations(range(4), r)]
    cvec = cp.Variable(16)
    kron_index = {S: sum((0 if l in S else 1) * 2 ** (3 - l) for l in range(4)) for S in subsets}
    for i, S in enumerate(subsets):
        cons.append(trs[kron_index[S]] == cvec[i])
    # level-1 LP constraints on c
    g = lambda inS, t: (0.5 if t == 0 else -0.5) if inS else (0.5 if t == 0 else 1.5)
    cons += [cvec >= 0, cvec <= 1 / 16, sum(cvec[i] * 3 ** (4 - len(S)) for i, S in enumerate(subsets)) == k]
    for tau in itertools.product((0, 1), repeat=4):
        e = sum(cvec[i] * np.prod([g(l in S, tau[l]) for l in range(4)]) for i, S in enumerate(subsets))
        cons += [e >= 0, e <= 1 / 16]
    if bose:
        cons.append(kr(M_F) @ x == x)
    if ppt2:
        cons += psd81(to81(kr(M_tpP) @ x, rP, cP))
        cons += psd81(to81(kr(M_tpS) @ x, rS, cS))
    xi = kr(M_trP) @ x / k                                              # 16 coeffs on (Psym,Panti)^{(x)4}
    lam = kr(M_emb) @ xi - x
    cons += psd81(to81(lam, rA, cA))
    if ppt2:
        cons += psd81(to81(kr(M_tpP) @ lam, rP, cP))
        cons += psd81(to81(kr(M_tpS) @ lam, rS, cS))
    obj = [comb(len(S), s) * 2 ** s * 3 ** (4 - len(S)) for S in subsets]
    prob = cp.Problem(cp.Maximize(sum(obj[i] * cvec[i] for i in range(16))), [c for c in cons if c is not None])
    return prob


if __name__ == "__main__":
    s, k = int(sys.argv[1]), int(sys.argv[2])
    bose = "nobose" not in sys.argv
    ppt2 = "noppt2" not in sys.argv
    prob = build(s, k, bose, ppt2)
    val = prob.solve(solver=cp.SCS, eps=1e-7, max_iters=200000) if "scs" in sys.argv else prob.solve(solver=cp.CLARABEL)
    eig = sorted([comb(z, s) for z in range(5) for _ in range(comb(4, z))], reverse=True)
    print(f"U{s} k={k} bose={bose} ppt2={ppt2} level2={val:.8f} target={sum(eig[:k])} status={prob.status}")
