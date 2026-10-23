"""Brute-force matrix weights (symmetrized pair counts) of explicit stabilizer states / additive codes.

For a stabilizer state rho = |psi><psi| with stabilizer group S (Pauli labels up to sign), AMH's
Gamma_ab = tr(E_a rho) tr(E_b rho) tr(E_a E_b rho) equals 1 if a, b in S and 0 otherwise, so
lambda^{t,p}_{i,j} = #{(a,b) in S x S : wt a = i, wt b = j, |supp a & supp b| = t, #{l: a_l = b_l != 0} = p}.
This module counts pairs directly from the group (independent of the orbit-sum code in the (7,3,3) lane).
"""
import numpy as np


def parse(s):
    x = z = 0
    for l, ch in enumerate(s):
        if ch in "XY":
            x |= 1 << l
        if ch in "ZY":
            z |= 1 << l
    return x, z


def group_from_generators(gens, n):
    """All 2^r products of the generators as (x, z) masks (signs dropped)."""
    X = [0]
    Z = [0]
    for g in gens:
        gx, gz = parse(g)
        X = X + [x ^ gx for x in X]
        Z = Z + [z ^ gz for z in Z]
    X = np.array(X, dtype=np.int64)
    Z = np.array(Z, dtype=np.int64)
    # independence check
    keys = set(zip(X.tolist(), Z.tolist()))
    assert len(keys) == len(X), "generators not independent"
    return X, Z


def symp(x1, z1, x2, z2):
    return (bin(x1 & z2).count("1") + bin(z1 & x2).count("1")) & 1


def check_commuting(gens):
    P = [parse(g) for g in gens]
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if symp(*P[i], *P[j]):
                return False
    return True


def popcount_arr(a):
    a = a.copy()
    c = np.zeros_like(a)
    while np.any(a):
        c += a & 1
        a >>= 1
    return c


def pair_counts(X, Z, n):
    N = len(X)
    S = X | Z
    lut = {}
    counts = {}
    pcS = popcount_arr(S)
    full = (1 << n) - 1
    for a in range(N):
        sa, xa, za = S[a], X[a], Z[a]
        i = pcS[a]
        tt = popcount_arr(S & sa)
        diff = (X ^ xa) | (Z ^ za)
        pp = popcount_arr(S & sa & (~diff & full))
        key = ((i * (n + 1) + pcS) * (n + 1) + tt) * (n + 1) + pp
        u, c = np.unique(key, return_counts=True)
        for kk, cc in zip(u.tolist(), c.tolist()):
            counts[kk] = counts.get(kk, 0) + cc
    out = {}
    for kk, cc in counts.items():
        p = kk % (n + 1)
        r = kk // (n + 1)
        t = r % (n + 1)
        r //= (n + 1)
        j = r % (n + 1)
        i = r // (n + 1)
        out[(i, j, t, p)] = cc
    return out


def weight_distribution(X, Z, n):
    w = popcount_arr(X | Z)
    return np.bincount(w, minlength=n + 1)


HEXACODE_F4 = None  # built in controls.py from F4 generator matrix

FIVE_QUBIT = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
