"""Brute-force orbit sums lambda[i,j,t,p] = sum_{(a,b) in orbit} Re Gamma_ab for an explicit code,
with Gamma_ab = tr(E_a rho) tr(E_b rho) tr(E_a E_b rho), rho = P/K (Angles Munne-Huber Eq. (17)).
"""
import numpy as np

from terwilliger import I_set, gamma


def _pc_table(bits):
    tab = np.zeros(1 << bits, dtype=np.int64)
    for v in range(1 << bits):
        tab[v] = bin(v).count("1")
    return tab


def orbit_sums(t, n, K, tol=1e-12):
    """t: (2^n, 2^n) array, t[x,z] = Tr(P E(x,z)) (real for Hermitian Paulis)."""
    N = 2 ** n
    pc = _pc_table(n)
    tr = np.real(t).reshape(-1)  # index a = x*N + z
    assert np.allclose(np.imag(t), 0, atol=1e-9)
    X = np.repeat(np.arange(N), N)
    Z = np.tile(np.arange(N), N)
    supp = X | Z
    wt = pc[supp]
    xz = pc[X & Z]
    Iset = I_set(n)
    key = {o: k for k, o in enumerate(Iset)}
    # orbit code -> index lookup table via dense 4D array
    lut = -np.ones((n + 1, n + 1, n + 1, n + 1), dtype=np.int64)
    for o, k in key.items():
        lut[o] = k
    lam = np.zeros(len(Iset))
    nz = np.nonzero(np.abs(tr) > tol)[0]
    for a in nz:
        xa, za = X[a], Z[a]
        xb, zb = X, Z
        xc, zc = xa ^ xb, za ^ zb
        c = xc * N + zc
        tc = tr[c]
        tb = tr
        # phase exponent (mod 4) of E_a E_b = i^e E_c
        e = (xz[a] + xz - pc[xc & zc] + 2 * pc[za & xb]) % 4
        # real part of i^e: e=0 -> 1, e=2 -> -1, e odd -> 0 (product of real t's)
        re = np.where(e == 0, 1.0, np.where(e == 2, -1.0, 0.0))
        g = tr[a] * tb * tc * re / K ** 3
        i = wt[a]
        j = wt
        tt = pc[supp[a] & supp]
        diff = (xa ^ xb) | (za ^ zb)
        p = pc[supp[a] & supp & ~diff & (N - 1)]
        idx = lut[i, j, tt, p]
        assert (idx >= 0).all()
        lam += np.bincount(idx, weights=g, minlength=len(Iset))
    xvals = np.array([lam[k] / gamma(*o, n) for k, o in enumerate(Iset)])
    return Iset, lam, xvals
