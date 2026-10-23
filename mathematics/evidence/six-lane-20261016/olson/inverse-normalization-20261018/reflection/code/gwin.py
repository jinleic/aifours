#!/usr/bin/env python3
"""Window formulas for G-words (representations with possibly EMPTY rotation runs).  Used ONLY as a fast filter or as the
object of a stated lemma test; every reported solvability claim is re-decided by code/dp.py.

Representation: lists a, b, l, y of length k; cyclic order R_1 S_1 R_2 S_2 ... R_k S_k; R_i has a_i letters rho_1 and b_i
letters rho_-1 (possibly a_i = b_i = 0), S_i = sigma_(y_i)^(l_i), l_i >= 1; S_i lies between R_i and R_(i+1); y_0 := y_k.
theta_i = y_(i-1) - y_i.
"""

def word_of(a, b, l, y, p, order=None):
    """Explicit word; inside R_i the letters are rho_1^a_i rho_-1^b_i unless order[i] is given (a list of +-1)."""
    w = []
    for i in range(len(a)):
        if order is not None and order[i] is not None:
            w += [('R', s % p) for s in order[i]]
        else:
            w += [('R', 1)] * a[i] + [('R', p - 1)] * b[i]
        w += [('F', y[i] % p)] * l[i]
    return w

def gr0_solvable(a, b, l, y, p):
    """Lemma GR0 criterion (proof-GR.md Sec. 2 verbatim, any representation): solvable iff some z has
    Ach(z) cap (tau(z) + pZ) nonempty.  Brute force over z in {+1,-1}^k."""
    k = len(a)
    F = sum(l); R = sum(a) + sum(b)
    for mask in range(1 << k):
        z = [1 if (mask >> i) & 1 else -1 for i in range(k)]
        f = [1 if z[i] != z[(i + 1) % k] else 0 for i in range(k)]
        Phi = sum(f)
        delta = sum(1 for i in range(k) if (l[i] - f[i]) % 2)
        Cmax = F - delta
        Ep = sum(a[i] if z[i] == 1 else b[i] for i in range(k))
        Em = R - Ep
        s0 = 2 * p - Cmax; s1 = 2 * p - Phi
        lo = max(-s1, s0 - 2 * Em, -Em); hi = min(s1, 2 * Ep - s0, Ep)
        # tau(z) = -2^{-1} sum z_i (y_i - y_{i-1})
        inv2 = (p + 1) // 2
        tau = (-inv2 * sum(z[i] * (y[i] - y[i - 1]) for i in range(k))) % p
        t = lo + (lo % 2)
        while t <= hi:
            if (t - tau) % p == 0:
                return True
            t += 2
    return False

def kappa_of(l, p):
    return p - 1 - sum(x // 2 for x in l)

def lam(Q, a, b, l, p):
    """Lemma H0 lambda(Q) for a proper pattern Q (set of run indices), word length 4p-2 assumed."""
    k = len(a)
    A = sum(a); B = sum(b)
    kap = kappa_of(l, p)
    inQ = [i in Q for i in range(k)]
    # boundary blocks: S_j between R_j and R_(j+1): boundary iff inQ[j] != inQ[j+1]
    bnd = [j for j in range(k) if inQ[j] != inQ[(j + 1) % k]]
    m = len(bnd) // 2
    beta = sum(1 for j in bnd if l[j] % 2 == 0)
    DQ = sum(a[i] - b[i] for i in Q)
    return min(p - m + 1, DQ + B - kap + m - beta, (DQ + B) // 2 + 1)

def h0_solvable(a, b, l, y, p):
    """Lemma H0 criterion at length 4p-2 (normalised A >= B not required): solvable iff some proper Q has u_Q in I(Q)
    mod p, or 0 in I(empty) mod p.  u_Q = 2^{-1} sum_{i in Q} theta_i."""
    k = len(a)
    assert sum(a) + sum(b) + sum(l) == 4 * p - 2
    A = sum(a); B = sum(b); kap = kappa_of(l, p)
    inv2 = (p + 1) // 2
    theta = [(y[i - 1] - y[i]) % p for i in range(k)]
    lo0 = -min(p, A - kap - 1, A // 2); hi0 = min(p, B - kap - 1, B // 2)
    if any(v % p == 0 for v in range(lo0, hi0 + 1)):
        return True
    for mask in range(1, (1 << k) - 1):
        Q = [i for i in range(k) if (mask >> i) & 1]
        Qc = [i for i in range(k) if not (mask >> i) & 1]
        lq = lam(Q, a, b, l, p); lc = lam(Qc, a, b, l, p)
        u = (inv2 * sum(theta[i] for i in Q)) % p
        for v in range(1 - lc, lq):
            if (v - u) % p == 0:
                return True
    return False
