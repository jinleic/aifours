"""Symmetry-reduced Gamma-SDP for ((n,K,d))_2 codes (Angles Munne-Huber, arXiv:2603.19901 Eq. (31))
plus NEW operator-level Knill-Laflamme partial-trace constraints.

NEW constraint family (this lane): for every qubit subset S with |S| = s <= d-1, T = complement,
KL on S implies (Tr_S P (x) 1_S) P = (1_T (x) Tr_T(P)/K) P, i.e. with P_U := sum_{supp E in U} Tr(PE) E,
      K P_T P = 2^{n-2s} P_S P.
In moment form (Gamma_ab = t_a t_b w(a,b) t_{a+b} / K^3) this is Gamma lambda^(S) = 0 with
lambda^(S)_b = K [supp b in T] - 2^{n-2s} [supp b in S].  s = 0 is AMH's projector row-sum constraint.
Orbit form, row a with wt(a)=i and |supp a & S| = m:
  sum_{j,t,p} ( K N_T(i,m;j,t,p) - 2^{n-2s} N_S(i,m;j,t,p) ) x[i,j,t,p] = 0.
"""
from math import comb

import numpy as np

from qlp import kraw
from terwilliger import C, I_set, alpha, blocks_index, gamma


def N_T(n, s, i, m, j, t, p, q=4):
    return C(i - m, t) * C(t, p) * (q - 2) ** (t - p) * C(n - s - (i - m), j - t) * (q - 1) ** (j - t)


def N_S(n, s, i, m, j, t, p, q=4):
    return C(m, t) * C(t, p) * (q - 2) ** (t - p) * C(s - m, j - t) * (q - 1) ** (j - t)


def build(n, K, d, partial_trace_sizes=(), lp=False, pure=False, kl=True, row_sum=True):
    """Return (Iset, eqs, ineqs, blocks).
    eqs: list of (dict key->coef, rhs) meaning sum coef*x = rhs.
    ineqs: list of (dict, rhs) meaning sum coef*x >= rhs.
    blocks: list of (a,k, matrix of dict key->coef)."""
    Iset = I_set(n)
    key = {o: k for k, o in enumerate(Iset)}
    eqs, ineqs = [], []
    eqs.append(({(0, 0, 0, 0): 1.0}, 1.0, "norm"))
    for o in Iset:
        i, j, t, p = o
        if (t - p) % 2 == 1:
            eqs.append(({o: 1.0}, 0.0, "anticomm"))
    # triple-permutation symmetry: orbit determined by (i, j, k=i+j-t-p, dd=t-p); value symmetric in (i,j,k)
    cls = {}
    for o in Iset:
        i, j, t, p = o
        if (t - p) % 2:
            continue
        k = i + j - t - p
        cls.setdefault((tuple(sorted((i, j, k))), t - p), []).append(o)
    for members in cls.values():
        for o in members[1:]:
            eqs.append(({members[0]: 1.0, o: -1.0}, 0.0, "triple"))
    # partial-trace (s=0: AMH projector row sums) constraints
    sizes = ([0] if row_sum else []) + list(partial_trace_sizes)
    for s in sizes:
        for i in range(n + 1):
            for m in range(max(0, i - (n - s)), min(i, s) + 1):
                row = {}
                for o in Iset:
                    ii, j, t, p = o
                    if ii != i:
                        continue
                    cf = K * N_T(n, s, i, m, j, t, p) - 2 ** (n - 2 * s) * N_S(n, s, i, m, j, t, p)
                    if cf:
                        row[o] = row.get(o, 0.0) + cf
                if row:
                    eqs.append((row, 0.0, f"ptrace{s}"))
    # enumerators A_i(rho) = lambda[i,0,0,0] = gamma x
    A = {i: ((i, 0, 0, 0), gamma(i, 0, 0, 0, n)) for i in range(n + 1)}
    if kl:
        for jj in range(1, d):
            row = {}
            for i in range(n + 1):
                o, g = A[i]
                row[o] = row.get(o, 0.0) + K * kraw(jj, i, n) * g / 2 ** n
            o, g = A[jj]
            row[o] = row.get(o, 0.0) - g
            eqs.append((row, 0.0, "kl"))
    if lp:
        for jj in range(n + 1):
            # K B_j - A_j >= 0  (B_j(rho) normalized consistently: B_j(Pi)/K^2 = 2^-n sum K_j(i) A_i(rho))
            row = {}
            for i in range(n + 1):
                o, g = A[i]
                row[o] = row.get(o, 0.0) + K * kraw(jj, i, n) * g / 2 ** n
            o, g = A[jj]
            row[o] = row.get(o, 0.0) - g
            if jj >= d:
                ineqs.append((row, 0.0, "KB-A"))
            # shadow S_j >= 0
            row = {}
            for i in range(n + 1):
                o, g = A[i]
                row[o] = row.get(o, 0.0) + (-1) ** i * kraw(jj, i, n) * g / 2 ** n
            ineqs.append((row, 0.0, "shadow"))
    if pure:
        for o in Iset:
            i, j, t, p = o
            k = i + j - t - p
            if {i, j, k} & set(range(1, d)):
                eqs.append(({o: 1.0}, 0.0, "pure"))
    blocks = []
    for (a, k) in blocks_index(n):
        idx = list(range(k, n + a - k + 1))
        M = [[{} for _ in idx] for _ in idx]
        for o in Iset:
            i, j, t, p = o
            if k <= i <= n + a - k and k <= j <= n + a - k:
                v = alpha(i, j, t, p, a, k, n)[0]
                if v != 0:
                    M[i - k][j - k][o] = M[i - k][j - k].get(o, 0.0) + v
        blocks.append((a, k, M))
    return Iset, key, eqs, ineqs, blocks


def residuals(x, Iset, key, eqs, ineqs, blocks):
    xv = lambda o: x[key[o]]
    eq_res = {}
    for row, rhs, tag in eqs:
        r = sum(c * xv(o) for o, c in row.items()) - rhs
        eq_res[tag] = max(eq_res.get(tag, 0.0), abs(r))
    in_res = {}
    for row, rhs, tag in ineqs:
        r = sum(c * xv(o) for o, c in row.items()) - rhs
        in_res[tag] = min(in_res.get(tag, np.inf), r)
    mins = []
    for a, k, M in blocks:
        B = np.array([[sum(c * xv(o) for o, c in ent.items()) for ent in r] for r in M])
        # normalize by the identity block diagonal (congruence) for a meaningful scale
        mins.append(np.linalg.eigvalsh((B + B.T) / 2).min())
    return eq_res, in_res, np.array(mins)
