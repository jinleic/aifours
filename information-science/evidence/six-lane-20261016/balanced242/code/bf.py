"""Exact Boolean-function utilities on F_2^n (numpy, int64; no floating point).

Conventions: a truth table is a uint8 array t of length 2^n with t[x]=f(x),
x_i=(x>>i)&1.  Walsh: W_f(a)=sum_x (-1)^(f(x)+a.x).  ANF via Moebius transform.
"""
import numpy as np

def fwht(v):
    """Unnormalized Walsh-Hadamard transform of an integer vector (exact int64)."""
    a = np.array(v, dtype=np.int64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy(); y = a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y
        a = a.reshape(n)
        h *= 2
    return a

def walsh(t):
    return fwht(1 - 2 * np.asarray(t, dtype=np.int64))

def anf(t):
    """Moebius transform over F_2: returns ANF coefficient vector (uint8)."""
    a = np.array(t, dtype=np.uint8).copy() & 1
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        a[:, 1, :] ^= a[:, 0, :]
        a = a.reshape(n)
        h *= 2
    return a

def popcount_array(N):
    idx = np.arange(N, dtype=np.int64)
    pc = np.zeros(N, dtype=np.int64)
    x = idx.copy()
    while x.any():
        pc += x & 1
        x >>= 1
    return pc

def degree(t):
    c = anf(t)
    if not c.any():
        return -1
    pc = popcount_array(len(t))
    return int(pc[c.astype(bool)].max())

def parity_dot(a, x):
    """(a.x) mod 2 for integer masks (numpy broadcasting)."""
    v = np.bitwise_and(a, x)
    r = np.zeros(np.broadcast(a, x).shape, dtype=np.int64)
    while np.any(v):
        r ^= v & 1
        v >>= 1
    return r

def dot_matrix(n):
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    return parity_dot(idx[:, None], idx[None, :]).astype(np.uint8)

def direct_walsh(t, n):
    """Independent direct character sums (O(4^n)); used for verification."""
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    s = 1 - 2 * np.asarray(t, dtype=np.int64)
    out = np.zeros(N, dtype=np.int64)
    for a in range(N):
        chi = 1 - 2 * parity_dot(np.int64(a), idx)
        out[a] = int(np.dot(s, chi))
    return out

def quad_polar_matrix(t, n):
    """For a function of degree<=2 given by truth table, return polar (alternating) matrix B (n x n, 0/1)."""
    c = anf(t)
    B = np.zeros((n, n), dtype=np.uint8)
    for i in range(n):
        for j in range(i + 1, n):
            if c[(1 << i) | (1 << j)]:
                B[i, j] = B[j, i] = 1
    return B

def rank_gf2(M):
    M = np.array(M, dtype=np.uint8).copy() & 1
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]:
                piv = i; break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        r += 1
        if r == rows:
            break
    return r

def support_xor(t):
    s = 0
    for x in np.nonzero(np.asarray(t))[0]:
        s ^= int(x)
    return s

def digits_T(W, nd=4):
    """T=W/4 (requires 4|W); return list of digit truth tables d_k of (T mod 16)."""
    assert np.all(W % 4 == 0)
    T = W // 4
    R = np.mod(T, 16)
    return [((R >> k) & 1).astype(np.uint8) for k in range(nd)], T

def pf4_function(B, n):
    """Truth table of the quartic sum_{|I|=4} Pf(B_I) x^I (Pf over F_2 of 4x4 principal minor)."""
    N = 1 << n
    coeff = np.zeros(N, dtype=np.uint8)
    from itertools import combinations
    for I in combinations(range(n), 4):
        i, j, k, l = I
        pf = (B[i, j] & B[k, l]) ^ (B[i, k] & B[j, l]) ^ (B[i, l] & B[j, k])
        if pf:
            coeff[(1 << i) | (1 << j) | (1 << k) | (1 << l)] = 1
    return anf(coeff)  # Moebius is an involution: ANF->truth table
