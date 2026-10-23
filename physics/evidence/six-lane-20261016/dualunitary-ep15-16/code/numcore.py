"""Float helpers (candidate generation only; never used as proof).

Same conventions as gates.py: |ij> <-> 3i+j, R: U^R[(i,j),(a,b)] = U[(i,a),(j,b)], G: U^G[(i,b),(j,a)] = U[(i,a),(j,b)].
"""
import numpy as np

d = 3
N = 9


def R(U):
    return U.reshape(d, d, d, d).transpose(0, 2, 1, 3).reshape(N, N)


def G(U):
    return U.reshape(d, d, d, d).transpose(0, 3, 2, 1).reshape(N, N)


def polar(A):
    W, _, Vh = np.linalg.svd(A)
    return W @ Vh


def herm_res(X):
    return X @ X.conj().T - np.eye(X.shape[0])


def dual_residual(U):
    return np.sqrt(np.linalg.norm(herm_res(U)) ** 2 + np.linalg.norm(herm_res(R(U))) ** 2)


def tdual_def(U):
    """||U^G U^G^dag - I||_F^2 ; on D: 1 - e_p = this / 72."""
    return np.linalg.norm(herm_res(G(U))) ** 2


def E_lin(X):
    H = X @ X.conj().T
    return 1 - np.real(np.trace(H @ H)) / 81


def ep(U):
    return (E_lin(R(U)) + E_lin(G(U)) - 8 / 9) / (8 / 9)


def haar(n, rng):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    Q, Rr = np.linalg.qr(Z)
    return Q * (np.diag(Rr) / np.abs(np.diag(Rr)))


def mr_map(U, iters=2000, tol=1e-13):
    """Alternating polar projections (source M_R map) to a dual unitary."""
    for k in range(iters):
        U = R(polar(R(U)))
        U = polar(U)
        if dual_residual(U) < tol:
            break
    return U, k


# ---- real-coordinate Jacobians ----
def real_basis():
    B = []
    for k in range(N * N):
        E = np.zeros(N * N, complex)
        E[k] = 1
        B.append(E.reshape(N, N))
        E = np.zeros(N * N, complex)
        E[k] = 1j
        B.append(E.reshape(N, N))
    return B


BASIS = real_basis()
IU = np.triu_indices(N)


def herm_vec(H, w_off=1.0):
    """real coordinates of Hermitian H: diag (1 each), off-diagonal real and imag parts (weight w_off)."""
    out = [np.real(np.diag(H))]
    iu = np.triu_indices(N, 1)
    out.append(w_off * np.real(H[iu]))
    out.append(w_off * np.imag(H[iu]))
    return np.concatenate(out)


def jac_dual(U):
    """Jacobian of (U U^dag - I, U^R U^R^dag - I) in real coordinates; 162 x 162."""
    UR = R(U)
    cols = []
    for X in BASIS:
        A = X @ U.conj().T + U @ X.conj().T
        XR = R(X)
        Bm = XR @ UR.conj().T + UR @ XR.conj().T
        cols.append(np.concatenate([herm_vec(A), herm_vec(Bm)]))
    return np.array(cols).T


def jac_G(U):
    """Jacobian of U^G U^G^dag - I (81 x 162)."""
    UG = G(U)
    cols = []
    for X in BASIS:
        XG = G(X)
        cols.append(herm_vec(XG @ UG.conj().T + UG @ XG.conj().T))
    return np.array(cols).T


def lu_tangent(U):
    """33(+3) real tangent vectors of the LU orbit at U (as 162-vectors)."""
    gens = []
    # basis of u(3): i*E_kk, E_kl - E_lk, i(E_kl + E_lk)
    for k in range(d):
        A = np.zeros((d, d), complex)
        A[k, k] = 1j
        gens.append(A)
    for k in range(d):
        for l in range(k + 1, d):
            A = np.zeros((d, d), complex)
            A[k, l], A[l, k] = 1, -1
            gens.append(A)
            A = np.zeros((d, d), complex)
            A[k, l], A[l, k] = 1j, 1j
            gens.append(A)
    I3 = np.eye(d)
    vecs = []
    for A in gens:
        for X in (np.kron(A, I3) @ U, np.kron(I3, A) @ U, U @ np.kron(A, I3), U @ np.kron(I3, A)):
            vecs.append(to_vec(X))
    return np.array(vecs).T


def to_vec(X):
    """complex 9x9 -> real 162 in BASIS order (Re, Im interleaved)."""
    v = np.empty(2 * N * N)
    v[0::2] = X.real.ravel()
    v[1::2] = X.imag.ravel()
    return v


def from_vec(v):
    return (v[0::2] + 1j * v[1::2]).reshape(N, N)
