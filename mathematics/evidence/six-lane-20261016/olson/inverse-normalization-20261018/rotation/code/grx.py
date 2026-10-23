#!/usr/bin/env python3
"""Lemma GRX decision procedure (rotation slice, 2026-10-18; see ../notes-GRX-v1.md).

Every word with F >= 1 reflections is read cyclically as R_1 S_1 R_2 S_2 ... R_k S_k, where
S_i = sigma_(y_i)^(l_i) are the MAXIMAL constant reflection blocks (a maximal reflection run is cut
at every change of value) and R_i is the (possibly empty) multiset X_i of rotation values between
S_(i-1) and S_i (y_0 := y_k).  theta_i := y_(i-1) - y_i.
For z in {+1} x {+-1}^(k-1): f_i = [z_i != z_(i+1)] (z_(k+1) = z_1), Phi = sum f_i,
delta = #{i : l_i != f_i mod 2}, C_max = F - delta, X^z = multiset union of z_i X_i.
GRX: w has an identity 2p-subword iff for some z and some even C in [Phi, C_max] with
0 <= m := 2p - C <= R, some size-m sub-multiset of X^z sums to T(z) := sum_{z_i = +1} theta_i (mod p).
F = 0: identity 2p-subword iff some 2p rotations sum to 0.
This file implements the criterion literally (no use of rawdp.py).
"""
import itertools


def blocks_of(word, p):
    """Return (ys, ls, Xs) or None if F = 0."""
    n = len(word)
    refl = [i for i in range(n) if word[i][0] == 's']
    if not refl:
        return None
    # find a block end: reflection at i whose cyclic successor is not the same reflection value
    end = None
    for i in refl:
        j = (i + 1) % n
        if not (word[j][0] == 's' and word[j][1] % p == word[i][1] % p):
            end = i
            break
    if end is None:  # every letter is the same reflection value
        return [word[0][1] % p], [n], [[]]
    w = word[end + 1:] + word[:end + 1]
    ys, ls, Xs = [], [], []
    cur = []
    i = 0
    while i < n:
        kind, val = w[i]
        if kind == 'r':
            cur.append(val % p)
            i += 1
            continue
        y = val % p
        l = 0
        while i < n and w[i][0] == 's' and w[i][1] % p == y:
            l += 1
            i += 1
        Xs.append(cur)
        ys.append(y)
        ls.append(l)
        cur = []
    assert not cur  # w ends with a block
    return ys, ls, Xs


def subset_sums_by_size(vals, p, maxm):
    """dp[m] = bitmask of sums of size-m sub-multisets (m <= maxm)."""
    full = (1 << p) - 1
    dp = [0] * (maxm + 1)
    dp[0] = 1
    cnt = 0
    for x in vals:
        x %= p
        cnt += 1
        for m in range(min(cnt, maxm), 0, -1):
            s = dp[m - 1]
            if s:
                rot = ((s << x) | (s >> (p - x))) & full if x else s
                dp[m] |= rot
    return dp


def grx_has_identity(word, p, return_pattern=False):
    b = blocks_of(word, p)
    size = 2 * p
    if b is None:
        rots = [v % p for _, v in word]
        if len(rots) < size:
            return (False, None) if return_pattern else False
        dp = subset_sums_by_size(rots, p, size)
        ok = bool(dp[size] & 1)
        return (ok, ('F0',)) if return_pattern else ok
    ys, ls, Xs = b
    k = len(ys)
    F = sum(ls)
    R = sum(len(X) for X in Xs)
    theta = [(ys[i - 1] - ys[i]) % p for i in range(k)]  # ys[-1] = y_k
    for tail in itertools.product((1, -1), repeat=k - 1):
        z = (1,) + tail
        f = [1 if z[i] != z[(i + 1) % k] else 0 for i in range(k)]
        Phi = sum(f)
        delta = sum(1 for i in range(k) if ls[i] % 2 != f[i])
        Cmax = F - delta
        T = sum(theta[i] for i in range(k) if z[i] == 1) % p
        vals = []
        for i in range(k):
            vals.extend((z[i] * x) % p for x in Xs[i])
        mlo = max(0, size - Cmax)
        mhi = min(R, size - Phi)
        if mlo > mhi:
            continue
        dp = subset_sums_by_size(vals, p, mhi)
        for C in range(Phi, Cmax + 1, 2):
            m = size - C
            if 0 <= m <= R and (dp[m] >> T) & 1:
                return (True, (z, C, m, T)) if return_pattern else True
    return (False, None) if return_pattern else False
