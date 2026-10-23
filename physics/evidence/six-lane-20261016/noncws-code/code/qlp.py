"""Quantum weight-enumerator LP utilities (P3 = arXiv:2603.19901 conventions).

Unnormalized enumerators for a rank-K projector Pi on n qubits:
  A_j = sum_{wt E = j} |tr(E Pi)|^2,   B_j = sum_{wt E = j} tr(E Pi E^dag Pi)
MacWilliams:  B_j = 2^-n sum_i K_j(i;n) A_i
Shadow:       S_j = 2^-n sum_i (-1)^i K_j(i;n) A_i >= 0
Constraints:  A_0 = K^2, A_j >= 0, K B_j >= A_j, equality for j < d.

Floating LPs (HiGHS) only *propose*; every claim we record is re-checked
with exact Fractions by the caller.
"""
from fractions import Fraction
from math import comb

import numpy as np
from scipy.optimize import linprog


def kraw(j, i, n):
    """Quaternary Krawtchouk K_j(i;n) = sum_a (-1)^a 3^(j-a) C(i,a) C(n-i,j-a)."""
    return sum((-1) ** a * 3 ** (j - a) * comb(i, a) * comb(n - i, j - a)
               for a in range(0, j + 1))


def mats(n):
    Kmat = np.array([[kraw(j, i, n) for i in range(n + 1)] for j in range(n + 1)], dtype=float)
    Smat = np.array([[(-1) ** i * kraw(j, i, n) for i in range(n + 1)] for j in range(n + 1)], dtype=float)
    return Kmat / 2 ** n, Smat / 2 ** n


def exact_mats(n):
    Kmat = [[Fraction(kraw(j, i, n), 2 ** n) for i in range(n + 1)] for j in range(n + 1)]
    Smat = [[Fraction((-1) ** i * kraw(j, i, n), 2 ** n) for i in range(n + 1)] for j in range(n + 1)]
    return Kmat, Smat


def lp_constraints(n, K, d, pure=False):
    """Return (A_ub, b_ub, A_eq, b_eq) for variables A_0..A_n."""
    Bm, Sm = mats(n)
    N = n + 1
    A_ub, b_ub, A_eq, b_eq = [], [], [], []
    # A0 = K^2
    row = np.zeros(N); row[0] = 1; A_eq.append(row); b_eq.append(K * K)
    for j in range(N):
        # S_j >= 0  ->  -S_j <= 0
        A_ub.append(-Sm[j]); b_ub.append(0.0)
        # K B_j - A_j
        row = K * Bm[j].copy(); row[j] -= 1
        if j < d:
            A_eq.append(row); b_eq.append(0.0)
        else:
            A_ub.append(-row); b_ub.append(0.0)
        if pure and 0 < j < d:
            r = np.zeros(N); r[j] = 1; A_eq.append(r); b_eq.append(0.0)
    return np.array(A_ub), np.array(b_ub), np.array(A_eq), np.array(b_eq)


def lp_opt(n, K, d, c, sense="min", pure=False, extra_eq=None, extra_ub=None):
    A_ub, b_ub, A_eq, b_eq = lp_constraints(n, K, d, pure)
    if extra_eq:
        for row, val in extra_eq:
            A_eq = np.vstack([A_eq, row]); b_eq = np.append(b_eq, val)
    if extra_ub:
        for row, val in extra_ub:
            A_ub = np.vstack([A_ub, row]); b_ub = np.append(b_ub, val)
    cc = np.array(c, dtype=float) * (1 if sense == "min" else -1)
    res = linprog(cc, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)] * (n + 1), method="highs")
    if res.status != 0:
        return None, res
    val = res.fun * (1 if sense == "min" else -1)
    return val, res


def exact_check(n, K, d, A):
    """Exact feasibility check of a rational enumerator vector A (list of Fractions)."""
    Bm, Sm = exact_mats(n)
    B = [sum(Bm[j][i] * A[i] for i in range(n + 1)) for j in range(n + 1)]
    S = [sum(Sm[j][i] * A[i] for i in range(n + 1)) for j in range(n + 1)]
    ok = A[0] == K * K and all(a >= 0 for a in A) and all(s >= 0 for s in S)
    for j in range(n + 1):
        if j < d:
            ok &= (K * B[j] == A[j])
        else:
            ok &= (K * B[j] >= A[j])
    return ok, B, S
